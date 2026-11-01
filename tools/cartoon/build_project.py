#!/usr/bin/env python3
"""由卡通剧本作者源生成每个视频的制作包（与 ppplus107 的 tools/build_course.py 规则一致）。

作者源：project/<剧集>/<视频名称>/src.py，定义
    META = {
        "title": "中文片名",
        "points": {"K1": "知识点名称", ...},     # 原视频知识点 K*，补充知识点 S*（审查补缺）
    }
    SHOTS = [(知识点编号, 中文画面, 英文画面, 旁白[, 顶部文字[, 图示文字列表]]), ...]
知识点编号用 META["points"] 的键；片头、情景导入、小结、片尾用 "开场" "情景" "小结" "结尾"。
英文画面写给 H3（中文提示词会画伪汉字）；出现 "panda mascot" 的镜头由熊猫对镜说旁白，其余为画外音。

输出（同目录）：shots.json、script.md、subtitles.srt、overlay.srt、source_map.json、
prompts.json（每镜完整的 H3 提示词，含 H3 配音版和 TTS 配音版）、workflow.md、comfyui/（工作流模板）；
以及 project/INDEX.md（全部已编写视频的目录）。

两个版本：原视频内容与国内法规有区别时，同一视频出两版——
    project/<剧集>/<视频名称>/            原著版：META["edition"] = "原著版"，只有原片知识点 K*，内容与原片一致
    project/<剧集>/<视频名称>（国内版）/  国内版：按国内法规和高校安全教育要求改编（含补充知识点 S* 和 审查报告.md）
与国内要求没有区别的视频只有一版，放在 project/<剧集>/<视频名称>/。

用法：python3 tools/cartoon/build_project.py [--only 视频目录 ...]   校验不通过时列出问题并以非零状态退出
"""
import argparse
import importlib.util
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import style  # noqa: E402
from sign_catalog import sign_names  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
COMFY = Path(__file__).resolve().parent / "comfyui"
WORKFLOW = "minimax_h3_t2v_av_hq_20step_api.json"
SHOT_S = 5
MAX_LINE = 20          # 每镜旁白不超过 20 字（不含标点）
SPECIAL = {"开场", "情景", "小结", "结尾"}
MAX_LABELS, MAX_LABEL_CHARS = 5, 8
DOMESTIC = "（国内版）"     # 国内版目录名后缀
LIVE = "【实拍】"           # 中文画面以此开头的镜头建议用真实操作视频（见 docs/实拍素材评估与拍摄规范.md）
COURSE = "高校实验室安全"   # 由全部原视频知识点合并整理的新课程：project/高校实验室安全/<课号_课名>/


def edition_of(d, meta):
    """返回 (原视频名称, 版本)；版本为 原著版 / 国内版 / 单一版。"""
    if d.parent.name == COURSE:
        return d.name, "课程"
    if d.name.endswith(DOMESTIC):
        return d.name[:-len(DOMESTIC)], "国内版"
    return d.name, "原著版" if meta.get("edition") == "原著版" else "单一版"
MIN_SECONDS, MAX_SECONDS = 120, 900
ROLES = {"panda mascot": "欣欣（熊猫主持）", "female graduate student": "小研（研究生，兼实验室安全员）",
         "older man": "老周（实验室负责人）", "young male student": "阿杰（本科生）",
         "safety administrator": "王老师（学院实验室安全管理员）", "facility engineer": "老李（设施工程师）",
         "security officer": "保卫处值班员"}
# 版权：新剧本不得出现原视频的机构名、品牌、型号和主持人姓名（在 src.py 的 META["avoid"] 里补充本片特有的词）
AVOID = ["MIT", "CDC", "ACS", "iGEM", "Eppendorf", "Thermo", "Orion", "NanoDrop", "Beckman", "Sigma", "YouTube"]


def plain(text):
    return re.sub(r"[^\w]|_", "", text)


def srt_time(sec):
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d},000"


def load_src(d):
    spec = importlib.util.spec_from_file_location("src", d / "src.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.META, mod.SHOTS


def build(meta, raw, edition="单一版"):
    problems, shots = [], []
    points = meta["points"]
    if edition == "原著版" and any(not k.startswith("K") for k in points):
        problems.append("原著版只保留原片知识点 K*，不加补充知识点")
    avoid = AVOID + meta.get("avoid", [])
    for i, item in enumerate(raw, 1):
        if len(item) not in (4, 5, 6):
            problems.append(f"镜头 {i}：字段数应为 4–6")
            continue
        sec, zh, en, line = item[:4]
        overlay = [item[4]] if len(item) >= 5 and item[4] else []
        labels = list(item[5]) if len(item) == 6 and item[5] else []
        if len(labels) > MAX_LABELS or any(len(plain(t)) > MAX_LABEL_CHARS for t in labels):
            problems.append(f"镜头 {i}：图示文字最多 {MAX_LABELS} 个、每个不超过 {MAX_LABEL_CHARS} 字：{labels}")
        if sec not in SPECIAL and sec not in points:
            problems.append(f"镜头 {i}：知识点编号 {sec} 不存在")
        n = len(plain(line))
        if n > MAX_LINE:
            problems.append(f"镜头 {i}：旁白 {n} 字超过 {MAX_LINE} 字：{line}")
        if re.search(r"[一-鿿]", en):
            problems.append(f"镜头 {i}：英文画面里有中文")
        for w in avoid:
            if re.search(rf"\b{re.escape(w)}\b", f"{zh} {en} {line} {' '.join(overlay)}", re.I):
                problems.append(f"镜头 {i}：出现原视频的机构/品牌名“{w}”（版权与中立性）")
        shots.append({"shot": i, "seconds": SHOT_S, "section": sec,
                      "section_title": points.get(sec, sec), "scene": zh, "prompt_en": en, "narration": line,
                      "overlay": overlay, "labels": labels,
                      "mode": "speaker" if "panda mascot" in en else "voiceover"})
    if shots and shots[-1]["section"] != "结尾":
        problems.append("最后一镜应为结尾")
    if sum(1 for s in shots if s["section"] == "结尾") > 1:
        problems.append("结尾只能有一镜")
    covered = {s["section"] for s in shots}
    for k, title in points.items():
        if k not in covered:
            problems.append(f"未覆盖知识点 {k} {title}")
    seconds = len(shots) * SHOT_S
    if not MIN_SECONDS <= seconds <= MAX_SECONDS:
        problems.append(f"总时长 {seconds} 秒，应在 {MIN_SECONDS // 60}–{MAX_SECONDS // 60} 分钟之间")
    return shots, problems


def write_package(d, meta, shots):
    rel = d.relative_to(ROOT).as_posix()
    series = d.parent.name
    video, edition = edition_of(d, meta)
    title = meta["title"] + (DOMESTIC if edition == "国内版" else "")
    other = {"原著版": f"国内版见 `../{video}{DOMESTIC}/`", "国内版": f"原著版见 `../{video}/`"}.get(edition)
    basis = {"原著版": "原视频知识点（K），内容与原片一致，未按国内法规改编（含原片的做法和数值）",
             "国内版": "原视频知识点（K）+ 审查补充知识点（S），按国内法规和高校实验室安全教育要求改编；审查记录见 `审查报告.md`",
             "单一版": "原视频知识点（K）+ 审查补充知识点（S），按国内法规和高校实验室安全教育要求改编；审查记录见 `审查报告.md`",
             "课程": "新课程《高校实验室安全》：由全部原视频的知识点合并整理（K），按国内法规和高校实验室安全教学要求编写，"
                     "必要时补充知识点（S）；知识点来源见 `来源.tsv`，教案见 `course/高校实验室安全/`"}[edition]
    spec = {"id": video, "edition": edition, "series": series, "title": title, "seconds": len(shots) * SHOT_S,
            "source_doc": f"course/{series}/{video}.md", "author_source": f"{rel}/src.py",
            "points": meta["points"], "shots": shots}
    (d / "shots.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")

    subs, ovs = [], []
    for s in shots:
        t0, t1 = (s["shot"] - 1) * SHOT_S, s["shot"] * SHOT_S
        subs.append(f"{s['shot']}\n{srt_time(t0)} --> {srt_time(t1)}\n{s['narration']}\n")
        if s["overlay"]:
            ovs.append(f"{s['shot']}\n{srt_time(t0)} --> {srt_time(t1)}\n{'　'.join(s['overlay'])}\n")
    (d / "subtitles.srt").write_text("\n".join(subs), encoding="utf-8")
    (d / "overlay.srt").write_text("\n".join(ovs), encoding="utf-8")

    smap = defaultdict(list)
    for s in shots:
        smap[s["section"]].append(s["shot"])
    (d / "source_map.json").write_text(json.dumps(
        {k: {"title": meta["points"].get(k, k), "kind": "补充" if k.startswith("S") else ("原片" if k.startswith("K") else k),
             "shots": v} for k, v in smap.items()}, ensure_ascii=False, indent=1), encoding="utf-8")

    prompts = []
    for s in shots:
        prompts.append({"shot": s["shot"], "mode": s["mode"], "seconds": SHOT_S, "narration": s["narration"],
                        "spoken": style.spoken(s["narration"]), "labels": s["labels"],
                        "signs": [f"{n}（{b}）" for n, b in sign_names(s["prompt_en"])],
                        "prompt_h3voice": style.local_prompt(s, tts=False),
                        "prompt_tts": style.local_prompt(s, tts=True) if s["mode"] != "speaker" else None})
    (d / "prompts.json").write_text(json.dumps({"video": video, "series": series, "workflow": f"comfyui/{WORKFLOW}",
                                                "fps": 24, "length_frames": 121, "width": 1280, "height": 704,
                                                "shots": prompts}, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / "comfyui").mkdir(exist_ok=True)
    for f in COMFY.glob("*.json"):
        shutil.copy2(f, d / "comfyui" / f.name)

    m, s_ = divmod(len(shots) * SHOT_S, 60)
    speak = sum(1 for s in shots if s["mode"] == "speaker")
    used = [r for en_, r in ROLES.items() if any(en_ in s["prompt_en"] for s in shots)]
    rows = "\n".join(
        f"| {s['shot']} | {srt_time((s['shot'] - 1) * SHOT_S)[3:8]} | {s['section']} | {s['scene']} | {s['narration']} | "
        f"{'　'.join(s['overlay'])} | {'、'.join(s['labels'])} | {'熊猫出镜说' if s['mode'] == 'speaker' else '画外音'} |"
        for s in shots)
    cover = "\n".join(f"- {k} {t}{'（补充）' if k.startswith('S') else ''}：镜头 "
                      f"{'、'.join(map(str, smap[k]))}" for k, t in meta["points"].items() if k in smap)
    (d / "script.md").write_text(f"""# {title}

- 剧集：{series}；对应原视频：{video}（内容分析见 `course/{series}/{video}.md`）
- 版本：{edition}{'；' + other if other else ''}
- 时长：{m} 分 {s_} 秒（{len(shots)} 个镜头 × {SHOT_S} 秒）；熊猫出镜说话 {speak} 镜，画外音 {len(shots) - speak} 镜
- 依据：{basis}
- 角色：{'、'.join(used)}

## 知识点覆盖

{cover}

## 分镜

| 镜号 | 时间 | 知识点 | 画面 | 旁白 | 顶部文字 | 图示文字 | 说话方式 |
|---|---|---|---|---|---|---|---|
{rows}
""", encoding="utf-8")

    live = [s for s in shots if s["scene"].startswith(LIVE)]
    note = d / "实拍清单.md"
    if live:   # 剧本中标【实拍】的镜头：给拍摄组的清单（没有实拍素材时仍按英文提示词生成卡通片段）
        note.write_text(f"# {title} 实拍清单\n\n拍摄规范见 `docs/实拍素材评估与拍摄规范.md`；"
                        f"拍好的 5 秒片段放到 `{rel}/footage/shot_NNN.mp4`，再运行 `python3 tools/cartoon/live.py \"{rel}\"`。\n\n"
                        "| 镜号 | 时间 | 知识点 | 拍摄内容 | 旁白（TTS 配音） |\n|---|---|---|---|---|\n"
                        + "\n".join(f"| {s['shot']} | {srt_time((s['shot'] - 1) * SHOT_S)[3:8]} | {s['section_title']} | "
                                     f"{s['scene'][len(LIVE):].strip()} | {s['narration']} |" for s in live) + "\n",
                        encoding="utf-8")
    elif note.exists():
        note.unlink()

    if edition == "课程":
        review_row = ("| `来源.tsv` | 本课每个知识点合并了哪些原知识点（★ 为采用的最佳讲解来源） |\n"
                      f"| `course/{COURSE}/{video}.md` | 知识点详细内容说明书（课件由它生成） |")
        check_docs = f"`来源.tsv` 和说明书 `course/{COURSE}/{video}.md` "
    else:
        review_row = "| `审查报告.md` | 法规与高校安全教育要求审查、完整性检查、补充知识点、版权处理 |"
        check_docs = "`审查报告.md` 和原视频内容文档"
    (d / "workflow.md").write_text(f"""# {title} 制作工作流

制作方法与 ppplus107 一致：ComfyUI + MiniMax H3，扁平 2D 卡通（熊猫欣欣主持），每镜 5 秒，1280×704、24fps。

| 文件 | 用途 |
|---|---|
| `src.py` | 剧本作者源（修改后运行 `python3 tools/cartoon/build_project.py --only "{rel}"`） |
| `shots.json` / `script.md` | 分镜（机器读 / 人读） |
| `prompts.json` | 每镜完整 H3 提示词：`prompt_h3voice`（H3 同时生成画面和配音）、`prompt_tts`（画外音镜头只生成画面和环境声，配音另用 TTS） |
| `subtitles.srt` / `overlay.srt` | 底部字幕（旁白）/ 顶部文字（片名、知识点名） |
| `comfyui/{WORKFLOW}` | ComfyUI API 工作流（`{{{{PROMPT}}}}` `{{{{SEED}}}}` `{{{{LENGTH}}}}` `{{{{FPS}}}}` 占位） |
| `source_map.json` | 知识点 → 镜头 |
{review_row}

## 步骤

1. 生成镜头（需本地 ComfyUI 已装 MiniMax H3 模型）：
   `COMFY_URL=http://127.0.0.1:8188 python3 tools/cartoon/generate.py "{rel}"`
   片段写入 `{rel}/clips/shot_NNN.mp4`（{len(shots)} 镜）；加 `--tts` 时画外音镜头用 `prompt_tts`，
   并把 `{rel}/tts/shot_NNN.wav` 合进片段（TTS 用 ppplus107 的 Qwen3-TTS 流程生成，旁白读法见 `prompts.json` 的 `spoken`）。
   每镜生成后检查：配音与旁白一致、结尾不截断、画面无伪字；不合格换种子重做（`--redo 镜号`）。
2. 拼接：`python3 tools/cartoon/assemble.py "{rel}"`，按分镜顺序合并，烧录底部字幕、顶部文字和图示文字，
   输出 `{rel}/{video}_cn_cartoon.mp4`。
   有 `实拍清单.md` 时：把拍好的片段放到 `{rel}/footage/shot_NNN.mp4`，先运行
   `python3 tools/cartoon/live.py "{rel}"`（统一规格并合入 TTS 配音，写入 clips/），generate.py 会跳过这些镜头。
3. 人工审核：对照 `script.md`、{check_docs}核对；学校适用条款由本校实验室安全管理部门确认。
""", encoding="utf-8")


MISMATCH = "内容不符说明.md"


def write_index():
    rows, crows = [], []
    for f in sorted(PROJECT.glob("*/*/shots.json")):
        s = json.loads(f.read_text(encoding="utf-8"))
        if s["series"] == COURSE:
            m, sec = divmod(s["seconds"], 60)
            rel = f.parent.relative_to(PROJECT).as_posix()
            crows.append(f"| {s['id']} | {s['title']} | {len(s['shots'])} | {m}:{sec:02d} | {len(s['points'])} | "
                         f"[剧本](<{rel}/script.md>) |")
            continue
        m, sec = divmod(s["seconds"], 60)
        rel = f.parent.relative_to(PROJECT).as_posix()
        k = sum(1 for p in s["points"] if p.startswith("K"))
        ed = s.get("edition", "单一版")
        review = f" · [审查](<{rel}/审查报告.md>)" if (f.parent / "审查报告.md").exists() else ""
        rows.append(f"| {s['series']} | {s['id']} | {ed} | {s['title']} | {len(s['shots'])} | {m}:{sec:02d} | "
                    f"{k} / {len(s['points']) - k} | [剧本](<{rel}/script.md>){review} |")
    import csv
    total = defaultdict(int)
    with open(ROOT / "tools" / "assets.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            total[r["剧集"]] += 1
    videos, orig, need = defaultdict(set), defaultdict(int), defaultdict(int)
    for f in PROJECT.glob("*/*/shots.json"):
        s = json.loads(f.read_text(encoding="utf-8"))
        if s["series"] == COURSE:
            continue
        ed = s.get("edition", "单一版")
        videos[s["series"]].add(s["id"])
        orig[s["series"]] += ed == "原著版"
        need[s["series"]] += ed == "国内版"
    done = {k: len(v) for k, v in videos.items()}

    def label(s):                                   # 剧集名与内容不符的，在目录上标记并链接说明
        note = PROJECT / s / MISMATCH
        if not note.exists():
            return s
        m = re.search(r"结论：\**(全部不符|部分不符)", note.read_text(encoding="utf-8"))
        kind = m.group(1) if m else "不符"
        return f"{s} ⚠ 内容{kind}（[说明](<{s}/{MISMATCH}>)）"
    prog = "\n".join(f"| {label(s)} | {done.get(s, 0)} / {n} | {orig[s]} / {need[s]} |"
                     for s, n in sorted(total.items(), key=lambda x: (-done.get(x[0], 0), x[0])))
    (PROJECT / "INDEX.md").write_text(
        "# 卡通教学视频制作目录\n\n已编写 " + str(sum(done.values())) + f" / {sum(total.values())} 个视频。"
        "与国内法规有区别的视频出两版：原著版（与原片一致）和国内版（按国内要求改编，目录名带“（国内版）”）。剧集名与实际内容不符的剧集标“⚠ 内容全部不符/部分不符”，详见该剧集目录下的 `" + MISMATCH + "`。\n\n"
        "## 各剧集进度\n\n| 剧集 | 已编写 / 附件视频 | 原著版 / 需原著版 |\n|---|---|---|\n" + prog + "\n\n## 已编写视频\n\n知识点：原片 / 补充。\n\n"
        "| 剧集 | 原视频 | 版本 | 卡通片名 | 镜头 | 时长 | 知识点 | 文件 |\n|---|---|---|---|---|---|---|---|\n"
        + "\n".join(rows) + "\n" + (
            f"\n## 新课程《{COURSE}》\n\n由全部原视频知识点合并整理的课程（大纲见 `curriculum/课程大纲.md`），已编写 {len(crows)} 节。\n\n"
            "| 课 | 课名 | 镜头 | 时长 | 知识点 | 文件 |\n|---|---|---|---|---|---|\n" + "\n".join(crows) + "\n" if crows else ""),
        encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="视频目录（project/<剧集>/<视频>）")
    args = ap.parse_args()
    only = {Path(p).resolve() for p in args.only} if args.only else None
    failed = 0
    for src in sorted(PROJECT.glob("*/*/src.py")):
        d = src.parent
        if only and d.resolve() not in only:
            continue
        meta, raw = load_src(d)
        shots, problems = build(meta, raw, edition_of(d, meta)[1])
        write_package(d, meta, shots)
        m, s = divmod(len(shots) * SHOT_S, 60)
        print(f"[{d.parent.name}/{d.name}] {meta['title']}：{len(shots)} 镜，{m} 分 {s} 秒" + ("，问题：" if problems else ""))
        for p in problems:
            print("   ", p)
        failed += bool(problems)
    write_index()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
