#!/usr/bin/env python3
"""检查《高校实验室安全》已编写各课：知识点覆盖、剧本与说明书一致、文件齐全。

用法：python3 tools/course/check_course.py [课号 ...]     不带课号时检查全部已编写的课并汇总覆盖率
检查项：
  1. project/高校实验室安全/<课号>_<课名>/ 有 src.py、来源.tsv；course/高校实验室安全/<同名>.md 存在
  2. 来源.tsv 覆盖 curriculum/mapping.tsv 分到本课的全部原知识点，且没有别课的知识点
  3. 来源.tsv 的课内编号都在剧本 META["points"] 里；剧本的每个 K/S 都在说明书 “### K1 名称” 中且名称一致
  4. 说明书有 基本信息、法规与标准依据、知识点、实拍建议、课后练习、来源视频 各节
  5. 每个 K 在 来源.tsv 中正好一个 ★，“合并了 N 个”与行数一致；S 点没有来源行
  6. 每个知识点要点 3–5 条、每条不超过 30 字；法规依据不超过 8 条；课后练习 3–6 题且都有答案
  7. 【实拍】镜头不超过全片 30%
有问题时以非零状态退出。
"""
import csv
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = "高校实验室安全"
PROJ, DOCS, CUR = ROOT / "project" / COURSE, ROOT / "course" / COURSE, ROOT / "curriculum"
SECTIONS = ["基本信息", "法规与标准依据", "知识点", "实拍建议", "课后练习", "来源视频"]


def load_mod(src):
    spec = importlib.util.spec_from_file_location("lesson_src", src)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load_meta(src):
    return load_mod(src).META


def load_shots(src):
    return load_mod(src).SHOTS


def main():
    want = {a.zfill(3) for a in sys.argv[1:]}
    syl = [r for r in csv.DictReader(open(CUR / "syllabus.tsv", encoding="utf-8"), delimiter="\t")]
    mapping = {}
    for r in csv.DictReader(open(CUR / "mapping.tsv", encoding="utf-8"), delimiter="\t"):
        mapping.setdefault(r["lesson_id"], set()).add(r["id"])
    dirs = {d.name[:3]: d for d in PROJ.glob("[0-9][0-9][0-9]_*")} if PROJ.exists() else {}
    bad, done, covered = 0, 0, 0
    for s in syl:
        lid = s["lesson_id"]
        if want and lid not in want:
            continue
        d = dirs.get(lid)
        if not d:
            if want:
                print(f"[{lid}] 未编写")
                bad += 1
            continue
        done += 1
        probs = []
        md = DOCS / f"{d.name}.md"
        for f in (d / "src.py", d / "来源.tsv", md):
            if not f.exists():
                probs.append(f"缺少 {f.relative_to(ROOT)}")
        if not probs:
            meta = load_meta(d / "src.py")
            pts = meta["points"]
            src_rows = list(csv.reader(open(d / "来源.tsv", encoding="utf-8"), delimiter="\t"))
            if src_rows and src_rows[0][:2] == ["课内编号", "原知识点 id"]:
                src_rows = src_rows[1:]
            got = {r[1] for r in src_rows if len(r) > 1}
            need = mapping.get(lid, set())
            miss, extra = need - got, got - need
            if miss:
                probs.append(f"来源.tsv 缺 {len(miss)} 个原知识点，如 {sorted(miss)[:2]}")
            if extra:
                probs.append(f"来源.tsv 有 {len(extra)} 个不属于本课的原知识点，如 {sorted(extra)[:2]}")
            for r in src_rows:
                if len(r) > 1 and r[0] not in pts:
                    probs.append(f"来源.tsv 课内编号 {r[0]} 不在剧本知识点中")
                    break
            covered += len(need & got)
            text = md.read_text(encoding="utf-8")
            heads = dict(re.findall(r"^### ([KS]\d+)\s+(.+)$", text, re.M))
            for k, name in pts.items():
                if heads.get(k, "").strip() != name.strip():
                    probs.append(f"说明书知识点 {k} 与剧本不一致：剧本“{name}”，说明书“{heads.get(k, '缺')}”")
            for k in heads:
                if k not in pts:
                    probs.append(f"说明书多出知识点 {k}")
            for k in pts:
                rs = [r for r in src_rows if len(r) > 2 and r[0] == k]
                stars = sum(r[2] == "★" for r in rs)
                if k.startswith("K") and (not rs or stars != 1):
                    probs.append(f"{k} 在 来源.tsv 中有 {len(rs)} 行、{stars} 个 ★（应至少 1 行、正好 1 个 ★）")
                if k.startswith("S") and rs:
                    probs.append(f"补充知识点 {k} 不应有来源行")
                blk = re.search(rf"^### {k}\s.*?(?=^### |^## |\Z)", text, re.S | re.M)
                if blk:
                    b = blk.group(0)
                    n = re.search(r"合并了 (\d+) 个", b)
                    if k.startswith("K") and n and int(n.group(1)) != len(rs):
                        probs.append(f"{k} 说明书写合并了 {n.group(1)} 个，来源.tsv 有 {len(rs)} 行")
                    pm = re.search(r"\*\*要点\*\*\n(.*?)(?=\n\*\*|\Z)", b, re.S)
                    items = [x.strip()[1:].strip() for x in (pm.group(1).splitlines() if pm else []) if x.strip().startswith("-")]
                    if not 3 <= len(items) <= 5:
                        probs.append(f"{k} 要点 {len(items)} 条（应 3–5 条）")
                    long = [x for x in items if len(re.sub(r"[^\w]", "", x)) > 30]
                    if long:
                        probs.append(f"{k} 要点超过 30 字：{long[0]}")
            basis = re.search(r"^## 法规与标准依据\n(.*?)(?=^## )", text, re.S | re.M)
            if basis and len([x for x in basis.group(1).splitlines() if x.strip().startswith("-")]) > 8:
                probs.append("法规与标准依据超过 8 条（课件只显示前 8 条）")
            quiz = re.search(r"^## 课后练习\n(.*?)(?=^## |\Z)", text, re.S | re.M)
            if quiz:
                qs = re.split(r"^\d+[.、]\s*", quiz.group(1), flags=re.M)[1:]
                if not 3 <= len(qs) <= 6 or any("答案" not in q for q in qs):
                    probs.append(f"课后练习 {len(qs)} 题（应 3–6 题，每题有答案）")
            shots = load_shots(d / "src.py")
            live = sum(1 for s in shots if s[1].startswith("【实拍】"))
            if shots and live / len(shots) > 0.3:
                probs.append(f"【实拍】镜头 {live}/{len(shots)} 超过 30%")
            for sec in SECTIONS:
                if not re.search(rf"^## {sec}", text, re.M):
                    probs.append(f"说明书缺“{sec}”一节")
        print(f"[{lid}] {s['课名']}：" + ("通过" if not probs else "问题："))
        for p in probs:
            print("   ", p)
        bad += bool(probs)
    total = sum(len(v) for k, v in mapping.items() if k != "不收录")
    if not want:
        print(f"\n已编写 {done} / {len(syl)} 课；原知识点覆盖 {covered} / {total}（另有不收录 {len(mapping.get('不收录', []))} 个）")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
