#!/usr/bin/env python3
"""同一个视频（YouTube 链接相同）出现在多个剧集里时，把已完成的那一份内容文档和制作包复制到其他剧集，不重复编写。

复制后在内容文档开头注明来源，并重新构建制作包（剧集名、路径按新位置生成）。
用法：python3 tools/copy_duplicates.py [--dry-run]
"""
import argparse
import csv
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEEP = {"src.py", "审查报告.md"}   # 其余文件由 build_project.py 重新生成


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    rows = list(csv.DictReader(open(ROOT / "tools" / "assets.tsv", encoding="utf-8"), delimiter="\t"))
    by_link = defaultdict(list)
    for r in rows:
        if r["链接"]:
            by_link[r["链接"]].append(r)
    copied = []
    for group in by_link.values():
        done = [r for r in group if (ROOT / "project" / r["剧集"] / r["视频名称"] / "src.py").exists()]
        if not done or len(group) < 2:
            continue
        src = done[0]
        sdoc = ROOT / "course" / src["剧集"] / f"{src['视频名称']}.md"
        sdir = ROOT / "project" / src["剧集"] / src["视频名称"]
        for r in group:
            ddir = ROOT / "project" / r["剧集"] / r["视频名称"]
            if ddir.exists():
                continue
            print(f"{src['剧集']}/{src['视频名称']} → {r['剧集']}/{r['视频名称']}")
            if args.dry_run:
                continue
            ddoc = ROOT / "course" / r["剧集"] / f"{r['视频名称']}.md"
            ddoc.parent.mkdir(parents=True, exist_ok=True)
            text = sdoc.read_text(encoding="utf-8")
            head, _, rest = text.partition("\n")
            ddoc.write_text(f"{head}\n\n> 本视频与剧集「{src['剧集']}」的 {src['视频名称']} 是同一个视频（{r['链接']}），"
                            f"内容文档和卡通剧本复制自该剧集，未重复编写。\n{rest}", encoding="utf-8")
            ddir.mkdir(parents=True)
            for f in sdir.iterdir():
                if f.name in KEEP:
                    shutil.copy2(f, ddir / f.name)
            copied.append(ddir)
    if copied:
        subprocess.run([sys.executable, str(ROOT / "tools" / "cartoon" / "build_project.py"), "--only",
                        *map(str, copied)], check=True)
    print(f"复制 {len(copied)} 个视频")


if __name__ == "__main__":
    main()
