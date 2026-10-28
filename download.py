#!/usr/bin/env python3
"""按 playlists.tsv 逐个下载 YouTube 播放列表中的视频（最高清晰度），并推送到 GitHub。

- 目录：<系列名称>/，文件名：<系列名称>_<序号>.mp4（序号为视频在播放列表中的位置）
- 超过 95MiB 的文件分割为 .001/.002/... 后提交（GitHub 单文件上限 100MB）
- 每个视频下载完成后立即提交并推送；已完成记录写入仓库中的 downloaded.tsv，可断点续传
- 本地下载目录超过 --max-gb（默认 25GB）时，删除最早下载且已推送的文件

推送使用一个临时的浅克隆（--depth 1 --filter=blob:none --sparse），
推送后即删除，因此本地 .git 不会随视频增长，删除旧文件能真正释放磁盘空间。

用法：python3 download.py [--out 目录] [--max-gb 25] [--only 序号,...] [--no-push]
依赖：yt-dlp、ffmpeg、git（且 git 已配置好对仓库的推送权限）
"""
import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNK = 95 * 1024 * 1024          # 分割大小，低于 GitHub 100MB 限制
PUSH_BATCH = 1500 * 1024 * 1024   # 单次 push 不超过约 1.5GB（GitHub 单次 push 上限 2GB）
MANIFEST = "downloaded.tsv"
MANIFEST_HEADER = ["video_id", "series", "index", "title", "files", "time"]


def run(cmd, cwd=None, check=True, capture=False):
    r = subprocess.run(cmd, cwd=cwd, text=True,
                       stdout=subprocess.PIPE if capture else None)
    if check and r.returncode != 0:
        raise RuntimeError(f"命令失败 ({r.returncode}): {' '.join(cmd)}")
    return r.stdout if capture else r.returncode


def safe_name(s):
    return re.sub(r'[\\/:*?"<>|]', "_", s).strip()


def load_playlists():
    with open(os.path.join(HERE, "playlists.tsv"), encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    return [(int(r["序号"]), safe_name(r["系列名称"]), r["播放列表ID"]) for r in rows]


def playlist_entries(pid, yt_args):
    out = run(["yt-dlp", "--flat-playlist", "-J", *yt_args,
               f"https://www.youtube.com/playlist?list={pid}"], capture=True)
    return json.loads(out)["entries"]


class Pusher:
    """在临时浅克隆中提交并推送文件，避免本地仓库无限增长。"""

    def __init__(self, remote, branch, enabled):
        self.remote, self.branch, self.enabled = remote, branch, enabled

    def _clone(self):
        tmp = tempfile.mkdtemp(prefix="push_", dir=HERE)
        r = run(["git", "clone", "--quiet", "--depth", "1", "--filter=blob:none",
                 "--sparse", "--branch", self.branch, self.remote, tmp], check=False)
        if r != 0:  # 分支尚不存在
            shutil.rmtree(tmp)
            tmp = tempfile.mkdtemp(prefix="push_", dir=HERE)
            run(["git", "init", "--quiet", "-b", self.branch, tmp])
            run(["git", "remote", "add", "origin", self.remote], cwd=tmp)
        return tmp

    def read_manifest(self):
        if not self.enabled:
            path = os.path.join(HERE, MANIFEST)
            return open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        tmp = self._clone()
        try:
            path = os.path.join(tmp, MANIFEST)
            return open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def push(self, out_dir, rel_files, manifest_row, message):
        """rel_files 为相对 out_dir 的路径；按批提交，最后一批附带 manifest。"""
        if not self.enabled:
            with open(os.path.join(HERE, MANIFEST), "a", encoding="utf-8") as f:
                f.write("\t".join(manifest_row) + "\n")
            return
        batches, cur, size = [], [], 0
        for rel in rel_files:
            sz = os.path.getsize(os.path.join(out_dir, rel))
            if cur and size + sz > PUSH_BATCH:
                batches.append(cur)
                cur, size = [], 0
            cur.append(rel)
            size += sz
        batches.append(cur)
        for i, batch in enumerate(batches):
            last = i == len(batches) - 1
            for attempt in range(5):
                tmp = self._clone()
                try:
                    for rel in batch:
                        dst = os.path.join(tmp, rel)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        try:
                            os.link(os.path.join(out_dir, rel), dst)
                        except OSError:
                            shutil.copy2(os.path.join(out_dir, rel), dst)
                    paths = list(batch)
                    if last:
                        mpath = os.path.join(tmp, MANIFEST)
                        new = not os.path.exists(mpath)
                        with open(mpath, "a", encoding="utf-8") as f:
                            if new:
                                f.write("\t".join(MANIFEST_HEADER) + "\n")
                            f.write("\t".join(manifest_row) + "\n")
                        paths.append(MANIFEST)
                    run(["git", "add", "--sparse", "--", *paths], cwd=tmp)
                    suffix = f" ({i + 1}/{len(batches)})" if len(batches) > 1 else ""
                    run(["git", "commit", "--quiet", "-m", message + suffix], cwd=tmp)
                    if run(["git", "push", "--quiet", "origin", f"HEAD:{self.branch}"],
                           cwd=tmp, check=False) == 0:
                        break
                finally:
                    shutil.rmtree(tmp, ignore_errors=True)
                wait = 2 ** (attempt + 1)
                print(f"  推送失败，{wait}s 后重试…", flush=True)
                time.sleep(wait)
            else:
                raise RuntimeError("推送多次失败，已停止")


def split_file(path):
    """超过 CHUNK 的文件分割为 path.001、path.002…，返回最终文件列表。"""
    if os.path.getsize(path) <= CHUNK:
        return [path]
    parts = []
    with open(path, "rb") as src:
        n = 1
        while True:
            data = src.read(CHUNK)
            if not data:
                break
            part = f"{path}.{n:03d}"
            with open(part, "wb") as dst:
                dst.write(data)
            parts.append(part)
            n += 1
    os.remove(path)
    return parts


def dir_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total


def cleanup(out_dir, pushed, max_bytes):
    """pushed：按下载顺序排列的已推送文件列表（绝对路径）。"""
    while pushed and dir_size(out_dir) > max_bytes:
        p = pushed.pop(0)
        if os.path.exists(p):
            os.remove(p)
            print(f"  已清理：{os.path.relpath(p, out_dir)}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=HERE, help="下载目录（默认为本仓库目录）")
    ap.add_argument("--max-gb", type=float, default=25)
    ap.add_argument("--only", help="只下载指定序号的系列，如 1,5,19")
    ap.add_argument("--remote", default=None, help="推送地址（默认取本仓库 origin）")
    ap.add_argument("--branch", default=None, help="推送分支（默认为当前分支）")
    ap.add_argument("--no-push", action="store_true", help="只下载，不推送")
    ap.add_argument("--yt-arg", action="append", default=[],
                    help="传给 yt-dlp 的额外参数，可多次使用")
    args = ap.parse_args()

    out_dir = os.path.abspath(args.out)
    remote = args.remote or run(["git", "remote", "get-url", "origin"], cwd=HERE, capture=True).strip()
    branch = args.branch or run(["git", "branch", "--show-current"], cwd=HERE, capture=True).strip()
    pusher = Pusher(remote, branch, not args.no_push)

    done = {line.split("\t")[0] for line in pusher.read_manifest().splitlines()[1:] if line}
    only = {int(x) for x in args.only.split(",")} if args.only else None
    max_bytes = int(args.max_gb * 1024 ** 3)
    pushed = []

    for num, series, pid in load_playlists():
        if only and num not in only:
            continue
        print(f"\n=== [{num}] {series}", flush=True)
        try:
            entries = playlist_entries(pid, args.yt_arg)
        except Exception as e:
            print(f"  获取播放列表失败：{e}", flush=True)
            continue
        width = max(2, len(str(len(entries))))
        for idx, e in enumerate(entries, 1):
            vid = e["id"]
            if vid in done:
                continue
            name = f"{series}_{idx:0{width}d}"
            sdir = os.path.join(out_dir, series)
            os.makedirs(sdir, exist_ok=True)
            print(f"  -> {name}  {e.get('title')}", flush=True)
            r = run(["yt-dlp", "--no-playlist", "--no-overwrites", "--continue",
                     "-f", "bv*+ba/b", "--merge-output-format", "mp4",
                     "-o", os.path.join(sdir, f"{name}.%(ext)s"), *args.yt_arg,
                     f"https://www.youtube.com/watch?v={vid}"], check=False)
            video = os.path.join(sdir, f"{name}.mp4")
            if r != 0 or not os.path.exists(video):
                print(f"  下载失败，跳过：{vid}", flush=True)
                continue
            files = split_file(video)
            rels = [os.path.relpath(p, out_dir) for p in files]
            row = [vid, series, str(idx), (e.get("title") or "").replace("\t", " "),
                   ",".join(os.path.basename(p) for p in files),
                   time.strftime("%Y-%m-%d %H:%M:%S")]
            pusher.push(out_dir, rels, row, f"Add {name}")
            done.add(vid)
            pushed.extend(files)
            cleanup(out_dir, pushed, max_bytes)
    print("\n全部完成。", flush=True)


if __name__ == "__main__":
    sys.exit(main())
