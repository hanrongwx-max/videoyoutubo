#!/usr/bin/env python3
"""给 work/<剧集>/<视频>/ 的分析素材加中文：

- transcript.json 每段加 "zh"（中文译文，由编写者翻译后用 merge 写入；英文 "text" 不动）
- transcript.zh.srt     中文字幕（时间轴同 transcript.srt）
- transcript.en-zh.srt  中英双语字幕（上英下中）
- analysis.md           “该镜头内的语音（转写）”一栏在英文下加“中文：……”（按镜头重新拼接各段译文）
- info.json             加 "中文名称"（序号_中文标题）、"中文标题"、"中文分类名称"（剧集的中文名），来自 tools/zh_names.tsv

用法：
    python3 tools/zh_translate.py todo                       列出还没有完整中文的视频（含英文字数）
    python3 tools/zh_translate.py dump "<剧集>" "<视频>" [文件]  导出待译段落：每行 “序号<TAB>英文”
    python3 tools/zh_translate.py merge "<剧集>" "<视频>" <译文文件> [--push]
                                                             译文文件每行 “序号<TAB>中文”，必须覆盖全部段落；
                                                             写入后生成字幕和 analysis.md，--push 提交并推送
    python3 tools/zh_translate.py dups                       重复视频（同一链接）复制已有译文
    python3 tools/zh_translate.py render [--all | "<剧集>" "<视频>"]   只重新生成（含 info.json 中文名称）
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
NAMES = ROOT / "tools" / "zh_names.tsv"
MARK = "<br>中文："


def ts(sec):
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")


def vdir(series, video):
    d = WORK / series / video
    if not (d / "transcript.json").exists():
        sys.exit(f"没有 {d}/transcript.json")
    return d


def load(d):
    return json.loads((d / "transcript.json").read_text(encoding="utf-8"))


def complete(tr):
    return all(s.get("zh", "").strip() or not s["text"].strip() for s in tr["segments"])


def names():
    if not NAMES.exists():
        return {}
    with open(NAMES, encoding="utf-8") as f:
        return {(r["剧集"], r["视频名称"]): r for r in csv.DictReader(f, delimiter="\t")}


def join(parts):
    """拼接各段译文：前一段没有句末/句中标点时加空格，避免连成一串。"""
    out = ""
    for z in parts:
        if not z:
            continue
        if out and out[-1] not in "，。！？；：、…）」』”》,.!?;:)":
            out += " "
        out += z
    return out


def render(d, table=None):
    tr = load(d)
    segs = tr["segments"]
    if complete(tr) and any(s["text"].strip() for s in segs):   # 无语音的视频不生成
        zh = [s.get("zh", "").strip() for s in segs]
        (d / "transcript.zh.srt").write_text("\n".join(
            f"{i}\n{ts(s['start'])} --> {ts(s['end'])}\n{z}\n" for i, (s, z) in enumerate(zip(segs, zh), 1)),
            encoding="utf-8")
        (d / "transcript.en-zh.srt").write_text("\n".join(
            f"{i}\n{ts(s['start'])} --> {ts(s['end'])}\n{s['text']}\n{z}\n" for i, (s, z) in enumerate(zip(segs, zh), 1)),
            encoding="utf-8")
        shots = json.loads((d / "shots.json").read_text(encoding="utf-8"))
        cell = {}
        for sh in shots:   # 与 analyze_video.align 相同：按段落中点归入镜头
            cell[sh["shot"]] = join([z for s, z in zip(segs, zh) if sh["start"] <= (s["start"] + s["end"]) / 2 < sh["end"]])
        lines = (d / "analysis.md").read_text(encoding="utf-8").split("\n")
        out, in_table = [], False
        for ln in lines:
            if ln.startswith("| 镜头 | 时间 | 关键帧 | 该镜头内的语音"):
                in_table = True
                ln = "| 镜头 | 时间 | 关键帧 | 该镜头内的语音（转写；英文下为中文翻译） |"
            elif in_table and re.match(r"\| \d+ \|", ln):
                parts = ln.split(" | ")
                n = int(parts[0].strip("| "))
                text = parts[-1]
                assert text.endswith(" |") or text.endswith("|"), ln
                text = text[:-1].rstrip()
                text = text.split(MARK)[0].rstrip()
                z = cell.get(n, "").replace("|", "／")
                if text and z:
                    text = f"{text}{MARK}{z}"
                parts[-1] = f"{text} |" if text else " |"
                ln = " | ".join(parts)
            elif in_table and not ln.startswith("|"):
                in_table = False
            out.append(ln)
        (d / "analysis.md").write_text("\n".join(out), encoding="utf-8")
    table = names() if table is None else table
    r = table.get((d.parent.name, d.name))
    if r:
        info = json.loads((d / "info.json").read_text(encoding="utf-8"))
        info["中文名称"] = f"{info['序号']}_{r['中文标题']}"
        info["中文标题"] = r["中文标题"]
        info["中文分类名称"] = r["中文剧集名"]
        (d / "info.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    return complete(tr)


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "todo":
        for f in sorted(WORK.glob("*/*/transcript.json")):
            tr = json.loads(f.read_text(encoding="utf-8"))
            if not complete(tr):
                n = sum(len(s["text"]) for s in tr["segments"])
                print(f"{f.parent.parent.name}\t{f.parent.name}\t{len(tr['segments'])}\t{n}")
    elif cmd == "dump":
        d = vdir(a[1], a[2])
        text = "\n".join(f"{i}\t{s['text']}" for i, s in enumerate(load(d)["segments"], 1))
        if len(a) > 3:
            Path(a[3]).write_text(text + "\n", encoding="utf-8")
        else:
            print(text)
    elif cmd == "merge":
        d = vdir(a[1], a[2])
        tr = load(d)
        got = {}
        for ln in Path(a[3]).read_text(encoding="utf-8").splitlines():
            if not ln.strip():
                continue
            i, _, z = ln.partition("\t")
            got[int(i)] = z.strip()
        segs = tr["segments"]
        missing = [i for i, s in enumerate(segs, 1) if s["text"].strip() and not got.get(i)]
        extra = [i for i in got if not 1 <= i <= len(segs)]
        if missing or extra:
            sys.exit(f"缺少段落 {missing[:20]}… 共 {len(missing)} 段；多余序号 {extra[:20]}")
        for i, s in enumerate(segs, 1):
            s["zh"] = got.get(i, "")
        (d / "transcript.json").write_text(json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
        render(d)
        print(f"已写入 {len(segs)} 段：{d.relative_to(ROOT)}")
        if "--push" in a:
            sys.path.insert(0, str(ROOT / "tools"))
            import publish
            publish.publish([str(d.relative_to(ROOT))], f"{a[1]} / {a[2]}: 中文翻译与中文字幕")
    elif cmd == "dups":   # 同一 YouTube 链接的重复视频：转写相同则复制译文
        with open(ROOT / "tools" / "assets.tsv", encoding="utf-8") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        groups = {}
        for r in rows:
            groups.setdefault(r["链接"], []).append(WORK / r["剧集"] / r["视频名称"])
        n = 0
        for ds in groups.values():
            ds = [d for d in ds if (d / "transcript.json").exists()]
            src = next((d for d in ds if complete(load(d))), None)
            if not src:
                continue
            st = load(src)
            for d in ds:
                tr = load(d)
                if d == src or complete(tr):
                    continue
                if [s["text"] for s in tr["segments"]] != [s["text"] for s in st["segments"]]:
                    print(f"转写不同，未复制：{d.relative_to(ROOT)}")
                    continue
                for s, t in zip(tr["segments"], st["segments"]):
                    s["zh"] = t.get("zh", "")
                (d / "transcript.json").write_text(json.dumps(tr, ensure_ascii=False, indent=1), encoding="utf-8")
                render(d)
                print(f"复制译文：{src.relative_to(ROOT)} → {d.relative_to(ROOT)}")
                n += 1
        print(f"复制 {n} 个")
    elif cmd == "render":
        table = names()
        dirs = sorted(p.parent for p in WORK.glob("*/*/transcript.json")) if a[1:2] == ["--all"] else [vdir(a[1], a[2])]
        done = sum(render(d, table) for d in dirs)
        print(f"处理 {len(dirs)} 个，其中中文翻译完整 {done} 个")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
