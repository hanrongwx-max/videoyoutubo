#!/usr/bin/env python3
"""把制作包 clips/ 下的镜头片段按分镜顺序拼成成片，并烧录底部字幕、顶部文字和图示文字。
样式与 ppplus107 的 tools/assemble.py 一致（白字黑边底部字幕；顶部文字白字蓝边；图示文字白字深蓝底，一行等分排在物体下方）。

用法：python3 tools/cartoon/assemble.py "project/<剧集>/<视频>" [--soft]
输出：<制作包>/<视频>_cn_cartoon.mp4
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

W, H = 1280, 720
LABEL_Y = 0.60
AUDIO_RATE = 32000
SUB_STYLE = "FontSize=20,MarginV=18"


def ass_time(sec):
    return f"{int(sec // 3600)}:{int(sec % 3600 // 60):02d}:{sec % 60:05.2f}"


def write_labels(spec, d):
    events = []
    for s in spec["shots"]:
        t0, t1 = (s["shot"] - 1) * s["seconds"], s["shot"] * s["seconds"]
        for i, text in enumerate(s.get("labels") or []):
            x = round((i + 0.5) / len(s["labels"]) * W)
            events.append(f"Dialogue: 0,{ass_time(t0)},{ass_time(t1)},Label,,0,0,0,,{{\\pos({x},{round(LABEL_Y * H)})}}{text}")
    if not events:
        return False
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\n\n[V4+ Styles]\n"
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
            "MarginR, MarginV, Encoding\n"
            "Style: Label,Sans,34,&H00FFFFFF,&H00FFFFFF,&H00703010,&H00703010,1,0,0,0,100,100,0,0,3,8,0,5,10,10,10,1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    (d / "labels.ass").write_text(head + "\n".join(events) + "\n", encoding="utf-8")
    return True


def normalize_audio(clips):
    for c in clips:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=sample_rate,channels",
                            "-of", "csv=p=0", str(c)], capture_output=True, text=True)
        if r.stdout.strip() in ("", f"{AUDIO_RATE},2"):
            continue
        tmp = c.with_name(c.stem + ".ar.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(c), "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
                        "-ar", str(AUDIO_RATE), "-ac", "2", str(tmp)], check=True)
        tmp.replace(c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--soft", action="store_true", help="软字幕（默认烧录硬字幕）")
    args = ap.parse_args()
    d = Path(args.package).resolve()
    spec = json.loads((d / "shots.json").read_text(encoding="utf-8"))
    clips = [d / "clips" / f"shot_{s['shot']:03d}.mp4" for s in spec["shots"]]
    missing = [c.name for c in clips if not c.exists()]
    if missing:
        sys.exit(f"缺少 {len(missing)} 个片段：{', '.join(missing[:10])}")
    normalize_audio(clips)
    listing = d / "concat.txt"
    listing.write_text("".join(f"file '{c.as_posix()}'\noutpoint {s['seconds']}\n" for c, s in zip(clips, spec["shots"])),
                       encoding="utf-8")
    joined = d / "joined.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
                    "-vf", "scale=1280:720", "-c:v", "libx264", "-crf", "24", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "96k", "-ar", str(AUDIO_RATE), str(joined)], check=True)
    final = d / f"{spec['id']}_cn_cartoon.mp4"
    if args.soft:
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(joined), "-i", "subtitles.srt", "-c", "copy",
               "-c:s", "mov_text", "-metadata:s:s:0", "language=chi", str(final)]
    else:
        vf = f"subtitles=subtitles.srt:force_style='{SUB_STYLE}'"
        if (d / "overlay.srt").read_text(encoding="utf-8").strip():
            vf += (",subtitles=overlay.srt:force_style='Alignment=6,FontSize=22,Bold=1,PrimaryColour=&H00FFFFFF,"
                   "OutlineColour=&H00B05A1E,BorderStyle=1,Outline=3,Shadow=0,MarginV=14'")
        if write_labels(spec, d):
            vf += ",subtitles=labels.ass"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(joined), "-vf", vf, "-crf", "24", "-c:a", "copy", str(final)]
    subprocess.run(cmd, check=True, cwd=d)   # 在制作包目录运行：滤镜里用相对文件名，避免路径里的特殊字符
    joined.unlink()
    listing.unlink()
    print(final)


if __name__ == "__main__":
    main()
