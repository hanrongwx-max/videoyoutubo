# 安全操作化学品 制作工作流

制作方法与 ppplus107 一致：ComfyUI + MiniMax H3，扁平 2D 卡通（熊猫欣欣主持），每镜 5 秒，1280×704、24fps。

| 文件 | 用途 |
|---|---|
| `src.py` | 剧本作者源（修改后运行 `python3 tools/cartoon/build_project.py --only "project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5"`） |
| `shots.json` / `script.md` | 分镜（机器读 / 人读） |
| `prompts.json` | 每镜完整 H3 提示词：`prompt_h3voice`（H3 同时生成画面和配音）、`prompt_tts`（画外音镜头只生成画面和环境声，配音另用 TTS） |
| `subtitles.srt` / `overlay.srt` | 底部字幕（旁白）/ 顶部文字（片名、知识点名） |
| `comfyui/minimax_h3_t2v_av_hq_20step_api.json` | ComfyUI API 工作流（`{{PROMPT}}` `{{SEED}}` `{{LENGTH}}` `{{FPS}}` 占位） |
| `source_map.json` | 知识点 → 镜头 |
| `审查报告.md` | 法规与高校安全教育要求审查、完整性检查、补充知识点、版权处理 |

## 步骤

1. 生成镜头（需本地 ComfyUI 已装 MiniMax H3 模型）：
   `COMFY_URL=http://127.0.0.1:8188 python3 tools/cartoon/generate.py "project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5"`
   片段写入 `project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5/clips/shot_NNN.mp4`（59 镜）；加 `--tts` 时画外音镜头用 `prompt_tts`，
   并把 `project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5/tts/shot_NNN.wav` 合进片段（TTS 用 ppplus107 的 Qwen3-TTS 流程生成，旁白读法见 `prompts.json` 的 `spoken`）。
   每镜生成后检查：配音与旁白一致、结尾不截断、画面无伪字；不合格换种子重做（`--redo 镜号`）。
2. 拼接：`python3 tools/cartoon/assemble.py "project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5"`，按分镜顺序合并，烧录底部字幕、顶部文字和图示文字，
   输出 `project/Lab Safety Training Series/09_Safe Chemical Handling Lab Safety Video Part 5/09_Safe Chemical Handling Lab Safety Video Part 5_cn_cartoon.mp4`。
3. 人工审核：对照 `script.md`、`审查报告.md` 和原视频内容文档核对；学校适用条款由本校实验室安全管理部门确认。
