"""用来源.tsv 生成说明书“来源视频”一节并替换进说明书。用法：python3 tools/course/mk_source_videos.py <课目录> <说明书>"""
import sys, csv, re
from collections import OrderedDict
d, md = sys.argv[1], sys.argv[2]
rows = list(csv.reader(open(f"{d}/来源.tsv", encoding="utf-8"), delimiter="\t"))[1:]
def key(k): return (k[0] != "K", int(k[1:]))
v = OrderedDict()
for k, pid, star in sorted(rows, key=lambda r: (key(r[0]), r[2] != "★")):
    ser, vid, _ = pid.split("|")
    v.setdefault((ser, vid), set()).add(k)
lines = [f"- {s} / {vi}（采用知识点 {'、'.join(sorted(ks, key=key))}）" for (s, vi), ks in v.items()]
text = open(md, encoding="utf-8").read()
text = re.sub(r"## 来源视频\n.*\Z", "## 来源视频\n" + "\n".join(lines) + "\n", text, flags=re.S)
open(md, "w", encoding="utf-8").write(text)
print(len(lines), "个视频")
