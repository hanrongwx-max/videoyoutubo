"""生成某课的 来源.tsv（并检查漏分、重复分配）。用法：python3 tools/course/mk_sources.py <课号> <课目录> <spec>；spec 每行：K编号 剧集前缀|视频序号|点id [★]"""
import sys, csv
lid, d, spec = sys.argv[1], sys.argv[2], sys.argv[3]
ids = [r["id"] for r in csv.DictReader(open("curriculum/mapping.tsv", encoding="utf-8"), delimiter="\t") if r["lesson_id"] == lid]
rows, used = [], set()
for ln in open(spec, encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"): continue
    k, rest = ln.split(None, 1)
    star = "★" if rest.endswith("★") else ""
    rest = rest.rstrip("★ ").strip()
    ser, num, pt = rest.split("|")
    m = [i for i in ids if i.startswith(ser) and i.split("|")[1].startswith(num + "_") and i.split("|")[2] == pt]
    if len(m) != 1: sys.exit(f"匹配失败 {ln}: {m}")
    if m[0] in used: sys.exit(f"重复 {m[0]}")
    used.add(m[0]); rows.append((k, m[0], star))
miss = [i for i in ids if i not in used]
if miss: sys.exit("未分配：\n" + "\n".join(miss))
with open(f"{d}/来源.tsv", "w", encoding="utf-8") as f:
    f.write("课内编号\t原知识点 id\t采用\n")
    for r in rows: f.write("\t".join(r) + "\n")
print(len(rows), "行；★", sum(1 for r in rows if r[2]))
