#!/usr/bin/env python3
"""把实拍素材接入制作包：<制作包>/footage/shot_NNN.<mp4|mov|mkv|avi> → <制作包>/clips/shot_NNN.mp4。

统一成与 MiniMax H3 卡通片段相同的规格（1280×704、24fps、每镜 5 秒、AAC 32kHz 立体声），
画面等比缩放后补边；不足 5 秒定格最后一帧补足，超过截断；不用现场声，配音用 <制作包>/tts/shot_NNN.wav
（没有 wav 则为静音，提示补配音）。clips/ 里已有的同名片段会被覆盖（实拍优先）；generate.py 跳过已存在的片段。

用法：python3 tools/cartoon/live.py "project/<剧集>/<视频>"
拍摄规范：docs/实拍素材评估与拍摄规范.md；需要实拍的镜头见制作包的 实拍清单.md
"""
import json
import re
import subprocess
import sys
from pathlib import Path

W, H, FPS, RATE, LEAD = 1280, 704, 24, 32000, 0.15


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = Path(sys.argv[1])
    spec = json.loads((d / "shots.json").read_text(encoding="utf-8"))
    sec = {s["shot"]: s["seconds"] for s in spec["shots"]}
    files = sorted(p for p in (d / "footage").glob("shot_*.*") if p.suffix.lower() in {".mp4", ".mov", ".mkv", ".avi"})
    if not files:
        sys.exit(f"没有实拍素材：{d}/footage/shot_NNN.mp4")
    (d / "clips").mkdir(exist_ok=True)
    for f in files:
        m = re.fullmatch(r"shot_(\d{3})", f.stem)
        if not m or int(m.group(1)) not in sec:
            print(f"跳过（镜号不存在）：{f.name}")
            continue
        n, dur = int(m.group(1)), sec[int(m.group(1))]
        wav = d / "tts" / f"shot_{n:03d}.wav"
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
              f"fps={FPS},tpad=stop_mode=clone:stop_duration={dur},setsar=1")
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(f)]
        if wav.exists():
            cmd += ["-i", str(wav), "-filter_complex",
                    f"[0:v]{vf}[v];[1:a]adelay={int(LEAD * 1000)}:all=1,apad[a]", "-map", "[v]", "-map", "[a]"]
        else:
            cmd += ["-f", "lavfi", "-i", f"anullsrc=r={RATE}:cl=stereo", "-filter_complex", f"[0:v]{vf}[v]",
                    "-map", "[v]", "-map", "1:a"]
        dst = d / "clips" / f"shot_{n:03d}.mp4"
        subprocess.run(cmd + ["-t", str(dur), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
                              "-ar", str(RATE), "-ac", "2", str(dst)], check=True)
        print(f"镜头 {n}：{f.name} → {dst.relative_to(d)}" + ("" if wav.exists() else "（无配音，需补 tts/shot_%03d.wav）" % n))


if __name__ == "__main__":
    main()
