#!/usr/bin/env python3
"""把已按国内法规改编的剧本改名为国内版：project/<剧集>/<视频>/ → project/<剧集>/<视频>（国内版）/，
腾出 project/<剧集>/<视频>/ 给原著版（与原片内容一致，见 docs/handoff/original_brief.md）。

只处理：已提交且没有未提交改动的目录、有 审查报告.md 且审查结论里有“需修改/需本土化”、不是原著版。
正在编写中的视频（有未提交改动）跳过，下次再跑。改名后重建制作包和 INDEX，提交并推送（与 publish.py 共用锁）。

用法：python3 tools/split_editions.py [--dry-run]
      python3 tools/split_editions.py --todo      列出已有国内版、还没有原著版的视频
"""
import argparse
import fcntl
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import publish  # noqa: E402

DOMESTIC = "（国内版）"
DIFF = re.compile(r"\|[^|\n]*(需修改|需本土化)[^|\n]*\|")


def git(*args, check=True):
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)


def candidates():
    for src in sorted(ROOT.glob("project/*/*/src.py")):
        d = src.parent
        if d.name.endswith(DOMESTIC) or (d.parent / f"{d.name}{DOMESTIC}").exists():
            continue
        if re.search(r"""["']edition["']\s*:\s*["']原著版""", src.read_text(encoding="utf-8")):
            continue
        review = d / "审查报告.md"
        if not review.exists() or not DIFF.search(review.read_text(encoding="utf-8")):
            continue
        rel = d.relative_to(ROOT).as_posix()
        if git("ls-files", "--", f"{rel}/src.py").stdout.strip() == "":
            continue                                    # 还没提交（正在编写）
        if git("status", "--porcelain", "--", rel).stdout.strip():
            continue                                    # 有未提交改动（正在修改）
        yield d


def todo():
    for d in sorted(ROOT.glob(f"project/*/*{DOMESTIC}")):
        if not (d.parent / d.name[:-len(DOMESTIC)] / "src.py").exists():
            print(f"{d.parent.name}\t{d.name[:-len(DOMESTIC)]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--todo", action="store_true")
    args = ap.parse_args()
    if args.todo:
        return todo()
    with open(publish.LOCK, "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        moved = list(candidates())
        for d in moved:
            print(("将改名：" if args.dry_run else "改名：") + d.relative_to(ROOT).as_posix())
        if args.dry_run or not moved:
            print(f"共 {len(moved)} 个")
            return
        for d in moved:
            git("mv", str(d.relative_to(ROOT)), str(d.relative_to(ROOT)) + DOMESTIC)
    targets = [str(d.parent / f"{d.name}{DOMESTIC}") for d in moved]
    subprocess.run([sys.executable, str(ROOT / "tools/cartoon/build_project.py"), "--only", *targets], cwd=ROOT)
    for p in ROOT.glob("project/**/__pycache__"):
        subprocess.run(["rm", "-rf", str(p)])
    # git mv 已暂存改名；这里只再加入重建后的国内版目录（不碰其他编写者未提交的文件）
    publish.publish([str(Path(t).relative_to(ROOT)) for t in targets],
                    f"Split {len(moved)} adapted scripts into 国内版 folders (原著版 to follow)")


if __name__ == "__main__":
    main()
