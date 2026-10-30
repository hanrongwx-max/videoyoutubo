#!/usr/bin/env python3
"""把一个视频制作包的每个镜头提交给本地 ComfyUI（MiniMax H3）生成 5 秒片段。

提示词取自制作包的 prompts.json（build_project.py 生成，拼装规则与 ppplus107 一致），
工作流取自制作包 comfyui/ 下的 API 格式 JSON，替换 {{PROMPT}} {{SEED}} {{LENGTH}} {{FPS}} 后 POST /prompt，
轮询 /history/<id>，再从 /view 下载结果到 <制作包>/clips/shot_NNN.mp4。已存在的片段跳过（--redo 指定重做）。

用法：
    COMFY_URL=http://127.0.0.1:8188 python3 tools/cartoon/generate.py "project/<剧集>/<视频>" [--tts] [--redo 3 7]
    python3 tools/cartoon/generate.py "project/<剧集>/<视频>" --dry-run      只打印第一镜提示词
--tts：画外音镜头用 prompt_tts（不含旁白），生成后把 tts/shot_NNN.wav 合进片段（无 wav 的镜头仍用 H3 配音）。
"""
import argparse
import json
import os
import random
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

COMFY_URL = os.environ.get("COMFY_URL", "http://127.0.0.1:8188").rstrip("/")
WORKFLOW = os.environ.get("COMFY_WORKFLOW")   # 默认用 prompts.json 里指定的工作流（20 步高质量版）
AUDIO_RATE = 32000   # H3 片段音频参数（AAC 32kHz 立体声），合入的 TTS 配音保持一致，否则拼接后音轨会变长
TTS_LEAD = 0.15


def http(method, path, data=None):
    req = urllib.request.Request(COMFY_URL + path, method=method,
                                 data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def fill(node, values):
    if isinstance(node, dict):
        return {k: fill(v, values) for k, v in node.items()}
    if isinstance(node, list):
        return [fill(v, values) for v in node]
    return values.get(node, node) if isinstance(node, str) else node


def submit(template, prompt, length, fps):
    wf = fill(template, {"{{PROMPT}}": prompt, "{{SEED}}": random.randrange(2 ** 32), "{{LENGTH}}": length, "{{FPS}}": fps})
    return json.loads(http("POST", "/prompt", {"prompt": wf, "client_id": "videoyoutubo-cartoon"}))["prompt_id"]


def wait(pid):
    while True:
        h = json.loads(http("GET", f"/history/{pid}"))
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("status_str") == "error":
                raise RuntimeError(f"ComfyUI 任务失败：{st}")
            for out in h[pid]["outputs"].values():
                for key in ("videos", "gifs", "images"):
                    for f in out.get(key, []):
                        if f["filename"].endswith(".mp4"):
                            return f
            if st.get("completed"):
                raise RuntimeError("任务完成但没有 mp4 输出")
        time.sleep(10)


def download(f, dst):
    q = urllib.parse.urlencode({"filename": f["filename"], "subfolder": f.get("subfolder", ""), "type": f.get("type", "output")})
    tmp = dst.with_suffix(".part")
    tmp.write_bytes(http("GET", f"/view?{q}"))
    tmp.replace(dst)


def dub(clip, wav):
    tmp = clip.with_name(clip.stem + ".dub.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(clip), "-i", str(wav), "-filter_complex",
                    f"[1:a]aresample={AUDIO_RATE},adelay={int(TTS_LEAD * 1000)}:all=1,apad[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
                    "-ar", str(AUDIO_RATE), "-ac", "2", "-shortest", str(tmp)], check=True)
    tmp.replace(clip)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--tts", action="store_true")
    ap.add_argument("--redo", nargs="*", type=int, default=[])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    d = Path(args.package)
    spec = json.loads((d / "prompts.json").read_text(encoding="utf-8"))
    template = json.loads(Path(WORKFLOW or d / spec["workflow"]).read_text(encoding="utf-8"))
    clips = d / "clips"
    clips.mkdir(exist_ok=True)
    for s in spec["shots"]:
        wav = d / "tts" / f"shot_{s['shot']:03d}.wav"
        use_tts = args.tts and s["prompt_tts"] and wav.exists()
        prompt = s["prompt_tts"] if use_tts else s["prompt_h3voice"]
        if args.dry_run:
            print(prompt)
            return
        dst = clips / f"shot_{s['shot']:03d}.mp4"
        if dst.exists() and s["shot"] not in args.redo:
            continue
        print(f"镜头 {s['shot']}/{len(spec['shots'])} {s['narration']}", flush=True)
        f = wait(submit(template, prompt, spec["length_frames"], spec["fps"]))
        download(f, dst)
        if use_tts:
            dub(dst, wav)
    print("全部镜头已生成：", clips)


if __name__ == "__main__":
    sys.exit(main())
