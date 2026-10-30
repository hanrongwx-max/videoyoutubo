#!/usr/bin/env python3
"""生成 Release 附件清单 tools/assets.tsv：每个附件视频对应的剧集、序号、原标题、视频名称。

剧集名称取 Release 名称（与 视频清单.md 的系列名称对照，取原标题和链接）；
视频名称 = <两位序号>_<原标题去掉“| 系列名”后缀>，用作 course/、project/ 下的文件和目录名。

用法：python3 tools/manifest.py            （需要 gh 已登录，走 REST API）
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tools" / "assets.tsv"
HEADER = ["剧集", "序号", "视频名称", "原标题", "链接", "release_tag", "asset_id", "asset_name", "size"]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def safe_name(s):
    s = re.sub(r'[\\/:*?"<>|#]+', " ", s)
    return re.sub(r"\s+", " ", s).strip().rstrip(".")[:80].strip()


def load_list():
    """视频清单.md → {norm(系列名): [(原标题, 链接), ...]}"""
    series, cur = {}, None
    for line in (ROOT / "视频清单.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"## \d+\. (.+)", line)
        if m:
            cur = series.setdefault(m.group(1).strip(), [])
            continue
        m = re.match(r"\| .+?\.mp4 \| (.+) \| (https://\S+) \|$", line)
        if m and cur is not None:
            cur.append((m.group(1).replace("\\|", "|").strip(), m.group(2)))
    return series


def match_series(release, series):
    r = norm(release)
    for name in series:
        n = norm(name)
        if n == r or r.startswith(n) or n.startswith(r):
            return name
    return None


def main():
    out = subprocess.run(["gh", "api", "--paginate", "repos/hanrongwx-max/videoyoutubo/releases?per_page=100"],
                         check=True, capture_output=True, text=True).stdout
    releases = json.loads(out.replace("][", ","))
    series = load_list()
    rows = []
    for rel in releases:
        sname = match_series(rel["name"], series)
        if not sname:
            print("未在视频清单中找到系列：", rel["name"], file=sys.stderr)
        for a in rel["assets"]:
            m = re.search(r"_(\d+)\.\w+$", a["name"])
            if not m:
                continue
            idx = int(m.group(1))
            title, link = (series[sname][idx - 1] if sname and idx <= len(series[sname]) else ("", ""))
            short = re.sub(r"\s*\|\s*MIT Digital Lab Techniques Manual\s*$", "", title) or a["name"].rsplit(".", 1)[0]
            rows.append([rel["name"], f"{idx:02d}", f"{idx:02d}_{safe_name(short)}", title, link,
                         rel["tag_name"], a["id"], a["name"], a["size"]])
    rows.sort(key=lambda r: (r[0], r[1]))
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(HEADER)
        w.writerows(rows)
    print(f"{len(rows)} 个附件视频，{len({r[0] for r in rows})} 个剧集 → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
