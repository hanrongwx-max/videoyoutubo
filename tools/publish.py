#!/usr/bin/env python3
"""把一个（或几个）视频的资料提交并推送到 GitHub：分析素材 work/<剧集>/<视频>/（转写、镜头、拼图，不含原视频和单帧）、
内容文档 course/<剧集>/<视频>.md、制作包 project/<剧集>/<视频>/，以及 project/INDEX.md。

多个进程（分析队列、各个剧本编写者）会同时调用，用文件锁串行化 git 操作；推送失败按 2/4/8/16 秒重试，
遇到远端有新提交时先 rebase 再推。

用法：
    python3 tools/publish.py "<剧集>" "<视频名称>" [-m 说明]          一个视频
    python3 tools/publish.py "<剧集>" --all [-m 说明]                 整个剧集已有的资料
"""
import argparse
import fcntl
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / ".git" / "publish.lock"
import os
TRAILER = os.environ.get("COMMIT_TRAILER", "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
                         "Claude-Session: https://claude.ai/code/session_0142QtstjsJxFPvhcX4d7ZN2")


def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)


def paths_for(series, video):
    ps = [ROOT / "work" / series / video, ROOT / "course" / series / f"{video}.md", ROOT / "project" / series / video]
    return [str(p.relative_to(ROOT)) for p in ps if p.exists()]


def publish(paths, message):
    for p in ROOT.glob("project/**/__pycache__"):
        subprocess.run(["rm", "-rf", str(p)])
    with open(LOCK, "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        index = ROOT / "project" / "INDEX.md"
        git("add", "--", *paths, *([str(index.relative_to(ROOT))] if index.exists() else []))
        if not git("diff", "--cached", "--quiet", check=False).returncode:
            print("没有需要提交的改动")
            return
        for wait in (1, 2, 4, 8, 0):   # 其他 git 进程持有 index.lock 时稍后重试
            r = git("commit", "-q", "-m", message + TRAILER, check=False)
            if r.returncode == 0:
                break
            if not wait:
                sys.exit(f"提交失败：{r.stderr.strip()}")
            time.sleep(wait)
        branch = git("branch", "--show-current").stdout.strip()
        for wait in (2, 4, 8, 16, 0):
            r = git("push", "-q", "-u", "origin", branch, check=False)
            if r.returncode == 0:
                print("已推送：", message)
                return
            if "fetch first" in r.stderr or "non-fast-forward" in r.stderr:
                git("pull", "-q", "--rebase", "origin", branch, check=False)
            if wait:
                time.sleep(wait)
        sys.exit(f"推送失败：{r.stderr.strip()}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("series")
    ap.add_argument("video", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("-m", "--message")
    args = ap.parse_args()
    if args.all:
        paths = [str(p.relative_to(ROOT)) for p in (ROOT / "work" / args.series, ROOT / "course" / args.series,
                                                    ROOT / "project" / args.series) if p.exists()]
        msg = args.message or f"{args.series}: update materials"
    else:
        if not args.video:
            sys.exit("需要视频名称或 --all")
        paths = paths_for(args.series, args.video)
        msg = args.message or f"{args.series} / {args.video}"
    if not paths:
        sys.exit("没有找到资料")
    publish(paths, msg)


if __name__ == "__main__":
    main()
