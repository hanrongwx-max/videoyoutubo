#!/usr/bin/env python3
"""列出《高校实验室安全》各课说明书和剧本中的跨课引用（“第 NNN 课”），附被引用课的课名和上下文，便于人工核对。

用法：python3 tools/course/xref.py [--bad]     --bad 只列出引用了不存在课号的地方
输出：每行 “引用课 → 被引用课号 被引用课名 ｜ 上下文”；课号不存在的标“！不存在”。
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = "高校实验室安全"
REF = re.compile(r"第\s*0*(\d{1,3})\s*[、，,和至–-]?\s*(?:0*(\d{1,3})\s*)?课")


def main():
    only_bad = "--bad" in sys.argv
    syl = {r["lesson_id"]: r["课名"] for r in
           csv.DictReader(open(ROOT / "curriculum" / "syllabus.tsv", encoding="utf-8"), delimiter="\t")}
    files = sorted((ROOT / "course" / COURSE).glob("[0-9][0-9][0-9]_*.md")) + \
        sorted((ROOT / "project" / COURSE).glob("[0-9][0-9][0-9]_*/src.py"))
    n = bad = 0
    for f in files:
        src = f.parent.name[:3] if f.name == "src.py" else f.name[:3]
        kind = "剧本" if f.name == "src.py" else "说明书"
        for ln in f.read_text(encoding="utf-8").splitlines():
            for m in REF.finditer(ln):
                for g in m.groups():
                    if not g:
                        continue
                    lid = g.zfill(3)
                    title = syl.get(lid)
                    n += 1
                    bad += title is None
                    if only_bad and title:
                        continue
                    ctx = ln.strip()[max(0, m.start() - 30):m.end() + 10]
                    print(f"{src}（{kind}）→ {lid} {title or '！不存在'} ｜ {ctx}")
    print(f"\n共 {n} 处跨课引用，其中课号不存在 {bad} 处", file=sys.stderr)


if __name__ == "__main__":
    main()
