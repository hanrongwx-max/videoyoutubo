#!/usr/bin/env python3
"""汇总全课程实拍建议 → curriculum/实拍汇总.md

来源：各课说明书 course/高校实验室安全/<课号>_<课名>.md 的“实拍建议”一节；
镜头数核对：project/高校实验室安全/<课号>_<课名>/src.py 中以【实拍】开头的中文画面。

用法：python3 tools/course/live_summary.py
"""
import csv
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "course" / "高校实验室安全"
PROJ = ROOT / "project" / "高校实验室安全"
OUT = ROOT / "curriculum" / "实拍汇总.md"


def section(md):
    m = re.search(r"^## 实拍建议\n(.*?)(?=^## )", md, re.S | re.M)
    return [ln for ln in (m.group(1).strip().splitlines() if m else []) if ln.strip()]


def live_shots(src):
    shots = runpy.run_path(str(src))["SHOTS"]
    return len(shots), [i for i, s in enumerate(shots, 1) if s[1].startswith("【实拍】")]


def main():
    with open(ROOT / "curriculum" / "syllabus.tsv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out, chapter, total_live, total_shots, lessons_live, warn = [], None, 0, 0, 0, []
    body = []
    for r in rows:
        lid, name = r["lesson_id"], r["课名"]
        if r["章"] != chapter:
            chapter = r["章"]
            body.append(f"\n## {chapter}\n")
        md = COURSE / f"{lid}_{name}.md"
        src = PROJ / f"{lid}_{name}" / "src.py"
        if not md.exists() or not src.exists():
            body.append(f"### {lid} {name}\n- （尚未编写）\n")
            warn.append(f"{lid} 缺说明书或剧本")
            continue
        n, live = live_shots(src)
        total_shots += n
        total_live += len(live)
        lessons_live += bool(live)
        items = section(md.read_text(encoding="utf-8"))
        nums = set()
        for ln in items:   # “镜 69–72”“镜 39、40”“镜号 5,6”
            for grp in re.findall(r"镜号?\s*(\d+(?:\s*[–\-~、,，和及]\s*\d+)*)", ln):
                for a, b in re.findall(r"(\d+)(?:\s*[–\-~]\s*(\d+))?", grp):
                    nums.update(range(int(a), int(b or a) + 1))
        if live and not nums.issuperset(live):
            warn.append(f"{lid} 说明书未列出的实拍镜：{sorted(set(live) - nums)}")
        body.append(f"### {lid} {name}（实拍 {len(live)}/{n} 镜）\n" + "\n".join(items or ["- 无，全部动画"]) + "\n")
    out.append("# 《高校实验室安全》实拍汇总\n")
    out.append("> 由 `tools/course/live_summary.py` 从各课说明书“实拍建议”和剧本【实拍】标记自动生成，不手改。"
               "拍摄规范见 `docs/实拍素材评估与拍摄规范.md`；每课的拍摄清单见制作包 `实拍清单.md`。\n")
    out.append(f"- 课数：{len(rows)}；含实拍的课：{lessons_live}\n"
               f"- 实拍镜头：{total_live} / {total_shots}（{total_live / max(total_shots, 1):.1%}）\n"
               "- 全部实拍均为正确示范、断电/不接电路/用模拟物，事故后果与违规做法一律用动画\n")
    if warn:
        out.append("\n**待处理**\n" + "\n".join(f"- {w}" for w in warn) + "\n")
    OUT.write_text("\n".join(out + body), encoding="utf-8")
    print(f"写入 {OUT.relative_to(ROOT)}：实拍 {total_live}/{total_shots} 镜，{len(warn)} 条待处理")
    for w in warn:
        print(" ", w)


if __name__ == "__main__":
    main()
