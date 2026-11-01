#!/usr/bin/env python3
"""导出某节课分到的全部原知识点（编写新课程时阅读用）。

用法：python3 tools/course/lesson_sources.py <课号> [输出文件]
每行：原知识点 id、类别、知识点名称、国内版旁白；按剧集/视频分组，并附本课大纲范围和对应国内版审查报告路径。
"""
import csv
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CUR = ROOT / "curriculum"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    lid = sys.argv[1].zfill(3)
    syl = {r["lesson_id"]: r for r in csv.DictReader(open(CUR / "syllabus.tsv", encoding="utf-8"), delimiter="\t")}
    if lid not in syl:
        sys.exit(f"没有课号 {lid}")
    ids = {r["id"]: r["备注"] for r in csv.DictReader(open(CUR / "mapping.tsv", encoding="utf-8"), delimiter="\t")
           if r["lesson_id"] == lid}
    groups = OrderedDict()
    for r in csv.DictReader(open(CUR / "source_points.tsv", encoding="utf-8"), delimiter="\t"):
        if r["id"] in ids:
            groups.setdefault((r["剧集"], r["视频"]), []).append(r)
    s = syl[lid]
    out = [f"# 课 {lid} {s['课名']}（{s['章']}，目标 {s['目标分钟']} 分钟）", f"范围：{s['范围']}",
           f"分到本课的原知识点：{len(ids)} 个，来自 {len(groups)} 个视频", ""]
    for (series, video), rows in groups.items():
        out.append(f"## {series} / {video}")
        out.append(f"   审查报告：project/{series}/{video}（国内版）/审查报告.md；内容文档：course/{series}/{video}.md")
        for r in rows:
            note = f"  〔{ids[r['id']]}〕" if ids[r["id"]] else ""
            out.append(f"- {r['id']} [{r['类别']}] {r['知识点']}：{r['国内版旁白']}{note}")
        out.append("")
    text = "\n".join(out)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
