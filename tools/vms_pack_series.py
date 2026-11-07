#!/usr/bin/env python3
"""把原有各剧集的两版卡通剧本（原著版、国内版）按剧集分别整理成 VMS 课程资料包（vms-course-pack/1）。

每个剧集一个资料包，两版都放进去：
  第 1 章 原著版：集号 01-<序号>，照原片的改编（含原片的外国法规与数值，不纠正）
  第 2 章 国内版：集号 02-<序号>，按国内法规本土化并补充知识点 S，标题加“（国内版）”
国内版有补充知识点、知识点名称也有改动，不符合 VMS “<集号>CN 沿用原集知识点”的写法，所以作为独立剧集，知识点编号各自独立
（01-05.K1、02-05.S1）。镜头转换规则同 tools/vms_pack.py（旁白数字按读法、纯物体镜头加 No people、诱发文字的说法改写）。
materials/<集号>/：内容文档（原片分析）、剧本（script.md）、国内版另有审查报告。docs/：目录、资料包说明、内容不符说明等。

用法：python3 tools/vms_pack_series.py <输出目录> [剧集名 ...]      不给剧集名则全部剧集；每个剧集生成 <代号>/ 和 <代号>.zip
"""
import csv
import json
import re
import runpy
import shutil
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vms_pack import NAMES, ROOT, SPECIAL, avoid_list, fix_prompt  # noqa: E402
from style import LOCAL_CHARACTERS, LOCAL_STYLE, LOCAL_VOICE, spoken  # noqa: E402

CN = "（国内版）"
COURSE = "高校实验室安全"
MIN_S, MAX_S = 120, 900   # 原片改编每集 24–175 镜


def slug(series):
    s = "yt-" + re.sub(r"[^a-z0-9]+", "-", series.lower()).strip("-")
    while len(s) > 40:   # 代号最长 40 位：按词截断
        s = s.rsplit("-", 1)[0]
    return s


def table(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def episode(d, vid, edition, seq, series):
    src = runpy.run_path(str(d / "src.py"))
    meta, shots = src["META"], src["SHOTS"]
    kps = [{"id": f"{vid}.{k}", "title": t, "pages": []} for k, t in meta["points"].items()]
    out = []
    for s in shots:
        shot = {"kp": s[0] if s[0] in SPECIAL else f"{vid}.{s[0]}", "scene": s[1], "prompt_en": fix_prompt(s[2]),
                "narration": spoken(s[3])}
        if len(s) > 4 and s[4]:
            shot["overlay"] = s[4]
        if len(s) > 5 and s[5]:
            shot["labels"] = list(s[5])
        out.append(shot)
    title = meta["title"] + (CN if edition == "国内版" else "")
    return {"id": vid, "title": title, "chapter": 1 if edition == "原著版" else 2, "book_sections": [edition],
            "source_lessons": [f"{series}/{seq}"], "knowledge_points": kps, "shots": out}, meta.get("avoid", [])


def build(series, out, assets, zh):
    sd = ROOT / "project" / series
    code = slug(series)
    pack = out / code
    if pack.exists():
        shutil.rmtree(pack)
    (pack / "episodes").mkdir(parents=True)
    videos = sorted(p for p in sd.iterdir() if p.is_dir() and not p.name.endswith(CN))
    eps, avoid, rows = [], [], []
    for v in videos:
        seq = v.name.split("_")[0]
        a = assets.get((series, v.name), {})
        for edition, d, vid in (("原著版", v, f"01-{seq}"), ("国内版", sd / (v.name + CN), f"02-{seq}")):
            if not (d / "src.py").exists():
                sys.exit(f"缺剧本：{d}")
            ep, av = episode(d, vid, edition, seq, series)
            eps.append(ep)
            avoid += av
            (pack / "episodes" / f"{vid}.json").write_text(json.dumps(ep, ensure_ascii=False, indent=1), encoding="utf-8")
            m = pack / "materials" / vid
            m.mkdir(parents=True)
            doc = ROOT / "course" / series / f"{v.name}.md"
            if doc.exists():
                shutil.copy(doc, m / "内容文档.md")
            shutil.copy(d / "script.md", m / "剧本.md")
            if (d / "审查报告.md").exists():
                shutil.copy(d / "审查报告.md", m / "审查报告.md")
            rows.append([vid, edition, ep["title"], len(ep["shots"]), len(ep["shots"]) * 5, len(ep["knowledge_points"]),
                         v.name, a.get("原标题", ""), a.get("链接", "")])
    keep, dropped = avoid_list(avoid, eps)
    (pack / "avoid.txt").write_text("# 原素材的机构、品牌、人名、频道名（剧本不得出现）\n" + "\n".join(keep) + "\n", encoding="utf-8")
    chars = [{"role_en": k, "name_zh": NAMES[k][0], "title_zh": NAMES[k][1], "host": k == "panda mascot",
              "appearance_en": v} for k, v in LOCAL_CHARACTERS.items()]
    (pack / "characters.json").write_text(json.dumps(chars, ensure_ascii=False, indent=1), encoding="utf-8")
    name_zh = zh.get(series, series)
    n_shots = sum(len(e["shots"]) for e in eps)
    manifest = {
        "format": "vms-course-pack/1", "code": code, "name": f"{name_zh}（卡通改编，原著版与国内版）",
        "audience": "高校本科生、研究生和实验室工作人员",
        "style": "扁平 2D 卡通，熊猫“欣欣”主持（与 ppplus107 系列同一画风和角色）",
        "description": f"由 {len(videos)} 个原视频重新创作的卡通剧本，每个视频两版：原著版照原片，国内版按国内法规本土化",
        "basis": "原著版照原片内容改编（保留原片的外国法规与数值）；国内版按国内法律法规、国家标准和"
                 "《高等学校实验室安全规范》本土化，并补充国内要求的知识点",
        "source": {"title": f"{series}（{len(videos)} 个视频）", "kind": "video"},
        "generation": {"style_en": LOCAL_STYLE, "voice_en": LOCAL_VOICE, "max_line": 20,
                       "min_seconds": MIN_S, "max_seconds": MAX_S},
    }
    (pack / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

    docs = pack / "docs"
    docs.mkdir()
    with open(docs / "目录.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["集号", "版本", "标题", "镜头数", "时长（秒）", "知识点数", "原视频名称", "原标题", "原视频链接"])
        w.writerows(sorted(rows, key=lambda r: (r[1] != "原著版", r[0])))
    for f in (sd / "内容不符说明.md", ROOT / "course" / series / "内容不符说明.md"):
        if f.exists():
            shutil.copy(f, docs / "内容不符说明.md")
            break
    for src, name in [("docs/卡通改编规范.md", "卡通改编规范.md"), ("docs/handoff/original_brief.md", "原著版编写说明.md"),
                      ("docs/handoff/standards_current.md", "现行标准清单.md")]:
        shutil.copy(ROOT / src, docs / name)
    peo = sum(1 for e in eps for s in e["shots"]
              if not any(r in s["prompt_en"].lower() for r in LOCAL_CHARACTERS) and "no people" not in s["prompt_en"].lower())
    lens = [len(e["shots"]) for e in eps]
    note = (f"# 资料包说明：{name_zh}\n\n"
            f"- 原剧集：{series}，{len(videos)} 个视频；资料包 {len(eps)} 集（每个视频两版），{n_shots} 镜，"
            f"约 {n_shots * 5 / 3600:.1f} 小时；每集 {min(lens)}–{max(lens)} 镜（时长范围设为 {MIN_S}–{MAX_S} 秒）。\n"
            "- 第 1 章 原著版（集号 01-<序号>）：照原片改编，保留原片的外国法规、数值和说法，不纠正、不标注。\n"
            "- 第 2 章 国内版（集号 02-<序号>，标题带“（国内版）”）：按国内法规本土化，补充知识点 S；改了什么见各集 materials 的审查报告。\n"
            "- 国内版没有用 VMS 的“<集号>CN”写法：国内版有补充知识点、知识点名称也有改动，不能沿用原集的知识点，所以作为独立剧集。"
            "两版英文画面和旁白相同的镜头，VMS 不会自动复用片段。\n"
            "- 知识点编号：<集号>.K1（原片知识点）、<集号>.S1（国内版补充）。\n"
            "- 人物 7 个：欣欣（熊猫主持，host）、小研、老周、阿杰、王老师、老李、保卫处值班员。\n"
            "- 旁白中三位以上的数字按位读（幺幺九）；英文画面里，纯物体镜头前加了 “No people.”，"
            "labeled、reads 等会诱发文字的说法已改写。\n"
            f"- 自检提醒：{peo} 镜画面里有手或泛指的人（不是固定角色），不能写 No people，属正常情况。\n"
            f"- 回避清单：{len(keep)} 个；另有 {len(dropped)} 个会被 VMS 的子串检查误中（被别的词包含，或在另一版中是正常用语），"
            f"未放进 avoid.txt：{'、'.join(dropped) or '无'}。\n"
            "- 每集资料：materials/<集号>/ 下有内容文档（原片讲解内容、画面文字、逐镜头说明）、剧本（分镜表），国内版另有审查报告。\n"
            "- 工作流：未提供，用 VMS 现有的 MiniMax H3 工作流。\n")
    if (docs / "内容不符说明.md").exists():
        note += "- 剧集名与内容不符，见 docs/内容不符说明.md。\n"
    if series == "Health Physics & Nuclear Medicine":
        note += "- 待确认：04 集原著版是否补回讲者“被蛇咬用布扎紧”的错误说法（目前未写入）。\n"
    (docs / "资料包说明.md").write_text(note, encoding="utf-8")

    z = out / f"{code}.zip"
    if z.exists():
        z.unlink()
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(pack.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(out).as_posix())
    return {"剧集": series, "代号": code, "中文名": name_zh, "视频": len(videos), "集": len(eps), "镜": n_shots,
            "zip": z.name, "MB": round(z.stat().st_size / 1e6, 1)}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    assets = {(r["剧集"], r["视频名称"]): r for r in table(ROOT / "tools" / "assets.tsv")}
    zh = {r["剧集"]: r["中文剧集名"] for r in table(ROOT / "tools" / "zh_names.tsv")}
    names = sys.argv[2:] or sorted(p.name for p in (ROOT / "project").iterdir() if p.is_dir() and p.name != COURSE)
    res = [build(s, out, assets, zh) for s in names]
    for r in res:
        print("\t".join(str(v) for v in r.values()))
    (out / "资料包清单.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    if len(res) > 1:   # 全部剧集的 zip 再合成一个下载包
        bundle = out / "VMS资料包_原有剧集两版.zip"
        with zipfile.ZipFile(bundle, "w", zipfile.ZIP_STORED) as zf:
            zf.write(out / "资料包清单.json", "资料包清单.json")
            for r in res:
                zf.write(out / r["zip"], r["zip"])
        print(f"合集：{bundle}（{bundle.stat().st_size / 1e6:.1f} MB）")


if __name__ == "__main__":
    main()
