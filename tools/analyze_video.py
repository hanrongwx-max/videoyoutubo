#!/usr/bin/env python3
"""下载 Release 附件视频并做分析素材：语音转写、镜头切分、关键帧、关键帧拼图。

输出 work/<剧集>/<视频名称>/（不入库，可随时重建）：
    info.json          时长、分辨率、编码
    transcript.json    语音转写分段 [{start, end, text}]
    transcript.srt     同上，SRT 格式
    shots.json         镜头切分 [{shot, start, end, frame}]（按画面变化切分，过短的合并）
    frames/shot_NNN.jpg 每个镜头中点的关键帧（宽 640）
    sheet_NN.jpg       关键帧拼图（每张 4×3 = 12 个镜头，标镜号和时间），供人工/模型看图写镜头说明
    analysis.md        转写按镜头对齐后的文本（写视频内容文档时的底稿）

用法：
    python3 tools/analyze_video.py --series "General Lab Safety Practices"           整个剧集
    python3 tools/analyze_video.py --series "General Lab Safety Practices" --only 01 04
    python3 tools/analyze_video.py ... --model small.en --keep-video     （默认 auto：英语用 small.en，其他语种译成英文）
依赖：gh（已登录）、ffmpeg、faster-whisper、Pillow
"""
import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
REPO = "hanrongwx-max/videoyoutubo"
FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
SCENE_T = 0.20      # ffmpeg 场景变化阈值（0.3 会漏掉同一场景里远景↔特写的切换）
MIN_SHOT = 2.0      # 短于 2 秒的镜头并入前一镜
MAX_SHOT = 30.0     # 长于 30 秒的镜头按 15 秒补抽关键帧（长镜头内容会变化）


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def load_assets():
    with open(ROOT / "tools" / "assets.tsv", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def ts(sec, srt=False):
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",") if srt else f"{int(h):02d}:{int(m):02d}:{int(s):02d}"


def download(a, d):
    ext = a["asset_name"].rsplit(".", 1)[-1]
    src = d / f"source.{ext}"
    if src.exists() and src.stat().st_size == int(a["size"]):
        return src
    with open(src, "wb") as f:
        subprocess.run(["gh", "api", "-H", "Accept: application/octet-stream",
                        f"repos/{REPO}/releases/assets/{a['asset_id']}"], check=True, stdout=f)
    return src


def probe(src):
    j = json.loads(run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(src)]))
    v = next((s for s in j["streams"] if s["codec_type"] == "video"), {})
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), {})
    return {"duration": float(j["format"]["duration"]), "width": v.get("width"), "height": v.get("height"),
            "video_codec": v.get("codec_name"), "audio_codec": a.get("codec_name"),
            "audio_language": (a.get("tags") or {}).get("language")}


_MODEL = {}


def whisper(name):
    from faster_whisper import WhisperModel
    if name not in _MODEL:
        _MODEL[name] = WhisperModel(name, device="cpu", compute_type="int8")
    return _MODEL[name]


def transcribe(src, d, model_name):
    """model_name="auto"：先用多语种 small 模型识别语种，英语用 small.en 转写，
    其他语种（如印地语）用 small 直接翻译成英文（task=translate），transcript.json 记下原语种。"""
    out = d / "transcript.json"
    if out.exists():
        return json.loads(out.read_text(encoding="utf-8"))
    pcm = run_bytes(["ffmpeg", "-v", "error", "-i", str(src), "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    audio = np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768
    task, lang = "transcribe", None
    if model_name == "auto":
        probe_at = min(len(audio) // 3, 16000 * 120)   # 跳过片头音乐，取 2 分钟附近 30 秒判断语种
        lang, _, _ = whisper("small").detect_language(audio[probe_at:probe_at + 16000 * 30])
        model_name, task = ("small.en", "transcribe") if lang == "en" else ("small", "translate")
    elif model_name.endswith(".en"):
        lang = "en"
    segs, info = whisper(model_name).transcribe(audio, language=lang, task=task, vad_filter=True, beam_size=5)
    segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]
    data = {"language": info.language, "model": model_name, "task": task, "segments": segs}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / "transcript.srt").write_text("\n".join(
        f"{i}\n{ts(s['start'], True)} --> {ts(s['end'], True)}\n{s['text']}\n" for i, s in enumerate(segs, 1)),
        encoding="utf-8")
    return data


def run_bytes(cmd):
    return subprocess.run(cmd, check=True, capture_output=True).stdout


def scene_cuts(src, fps=5):
    """按画面变化找切点：ffmpeg 解出每秒 5 帧的 64×36 灰度小图，相邻两帧的平均像素差和灰度直方图差都大时记为切点。
    （ffmpeg 的 select=scene 对部分 AV1/VP9 文件不出任何帧，所以自己算。）"""
    raw = run_bytes(["ffmpeg", "-v", "error", "-i", str(src), "-an", "-vf", f"fps={fps},scale=64:36,format=gray",
                     "-f", "rawvideo", "-"])
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 36, 64).astype(np.float32)
    # 硬切：相邻帧差大；叠化（淡入淡出）：与 1 秒前的帧差大，取 1 秒窗口内的峰值
    d1 = np.array([0.0] + [np.abs(frames[i] - frames[i - 1]).mean() / 255 for i in range(1, len(frames))])
    d5 = np.array([0.0] * fps + [np.abs(frames[i] - frames[i - fps]).mean() / 255 for i in range(fps, len(frames))])
    cuts = []
    for i in range(1, len(frames)):
        hard = d1[i] > SCENE_T / 2
        soft = d5[i] > SCENE_T and d5[i] == d5[max(0, i - fps):i + fps + 1].max()
        if hard or soft:
            cuts.append(round(i / fps, 2))
    return cuts


def detect_shots(src, duration, d):
    out = d / "shots.json"
    if out.exists():
        return json.loads(out.read_text(encoding="utf-8"))
    cuts = scene_cuts(src)
    bounds = [0.0]
    for c in cuts:
        if c - bounds[-1] >= MIN_SHOT and duration - c >= MIN_SHOT:
            bounds.append(c)
    bounds.append(duration)
    shots = []
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        shots.append({"shot": i + 1, "start": round(a, 2), "end": round(b, 2)})
    (d / "frames").mkdir(exist_ok=True)
    for s in shots:
        t = (s["start"] + s["end"]) / 2
        extra = []
        if s["end"] - s["start"] > MAX_SHOT:   # 长镜头：每 15 秒补一帧
            extra = [s["start"] + k for k in np.arange(7.5, s["end"] - s["start"], 15.0)]
        times = extra or [t]
        s["frames"] = []
        for k, tt in enumerate(times):
            name = f"shot_{s['shot']:03d}" + (f"_{k + 1}" if len(times) > 1 else "") + ".jpg"
            for back in (0, 0.5, 1.5, 3.0):   # 靠近片尾时 ffmpeg 可能取不到帧，往前退一点重试
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(tt - back, 0):.2f}", "-i", str(src),
                                "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "4", str(d / "frames" / name)],
                               check=True)
                if (d / "frames" / name).exists():
                    break
            else:
                continue
            s["frames"].append({"file": name, "t": round(float(tt), 2)})
    out.write_text(json.dumps(shots, ensure_ascii=False, indent=1), encoding="utf-8")
    return shots


def contact_sheets(shots, d, per=12, cols=4):
    font = ImageFont.truetype(FONT, 22)
    tiles = [(s["shot"], f) for s in shots for f in s["frames"]]
    for old in d.glob("sheet_*.jpg"):
        old.unlink()
    n = 0
    for i in range(0, len(tiles), per):
        chunk = tiles[i:i + per]
        ims = [Image.open(d / "frames" / f["file"]).convert("RGB") for _, f in chunk]
        w, h = 640, max(im.height for im in ims)
        rows = (len(ims) + cols - 1) // cols
        sheet = Image.new("RGB", (w * cols, (h + 30) * rows), "white")
        draw = ImageDraw.Draw(sheet)
        for k, ((shot, f), im) in enumerate(zip(chunk, ims)):
            x, y = (k % cols) * w, (k // cols) * (h + 30)
            sheet.paste(im, (x, y + 30))
            draw.text((x + 6, y + 3), f"镜头 {shot}  {ts(f['t'])}", fill="black", font=font)
        n += 1
        sheet.save(d / f"sheet_{n:02d}.jpg", quality=80)
    return n


def align(shots, segs, d, a, info):
    lines = [f"# {a['视频名称']} 分析底稿", "",
             f"- 剧集：{a['剧集']}；原标题：{a['原标题']}；链接：{a['链接']}",
             f"- 时长 {ts(info['duration'])}，{info['width']}×{info['height']}，镜头 {len(shots)} 个，转写 {len(segs)} 段", "",
             "| 镜头 | 时间 | 关键帧 | 该镜头内的语音（转写） |", "|---|---|---|---|"]
    for s in shots:
        text = " ".join(g["text"] for g in segs if s["start"] <= (g["start"] + g["end"]) / 2 < s["end"])
        lines.append(f"| {s['shot']} | {ts(s['start'])}–{ts(s['end'])} | {', '.join(f['file'] for f in s['frames'])} | "
                     f"{text.replace('|', '/')} |")
    (d / "analysis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", required=True)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--model", default="auto", help="auto（按语种选择）、small.en、small 等")
    ap.add_argument("--keep-video", action="store_true", help="保留下载的视频（默认分析完删除，省磁盘）")
    ap.add_argument("--push", action="store_true", help="每分析完一个视频就提交并推送到 GitHub（tools/publish.py）")
    args = ap.parse_args()
    assets = [a for a in load_assets() if a["剧集"] == args.series and (not args.only or a["序号"] in args.only)]
    if not assets:
        sys.exit(f"tools/assets.tsv 中没有剧集 {args.series}")
    for a in assets:
        if (ROOT / "project" / a["剧集"] / a["视频名称"] / "src.py").exists():
            continue   # 已编写（含从其他剧集复制的重复视频），不再分析
        final = WORK / a["剧集"] / a["视频名称"]
        if (final / "analysis.md").exists():
            continue   # 已分析
        # 分析过程中写在 work/.inprogress/（不入库），完成后再移到 work/<剧集>/<视频>/，避免半成品出现在仓库里
        d = final if final.exists() else WORK / ".inprogress" / a["剧集"] / a["视频名称"]
        d.mkdir(parents=True, exist_ok=True)
        print(f"== {a['视频名称']}", flush=True)
        src = download(a, d)
        info = probe(src)
        (d / "info.json").write_text(json.dumps({**a, **info}, ensure_ascii=False, indent=1), encoding="utf-8")
        tr = transcribe(src, d, args.model)
        shots = detect_shots(src, info["duration"], d)
        n = contact_sheets(shots, d)
        align(shots, tr["segments"], d, a, info)
        print(f"   {ts(info['duration'])}，转写 {len(tr['segments'])} 段，镜头 {len(shots)} 个，拼图 {n} 张", flush=True)
        if not args.keep_video:
            src.unlink()
        if d != final:
            final.parent.mkdir(parents=True, exist_ok=True)
            d.rename(final)
        if args.push:
            subprocess.run([sys.executable, str(ROOT / "tools" / "publish.py"), a["剧集"], a["视频名称"],
                            "-m", f"Analyze {a['剧集']} / {a['视频名称']}"], check=False)


if __name__ == "__main__":
    main()
