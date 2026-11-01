# 射线的性质与衰变 制作工作流

制作方法与 ppplus107 一致：ComfyUI + MiniMax H3，扁平 2D 卡通（熊猫欣欣主持），每镜 5 秒，1280×704、24fps。

| 文件 | 用途 |
|---|---|
| `src.py` | 剧本作者源（修改后运行 `python3 tools/cartoon/build_project.py --only "project/高校实验室安全/086_射线的性质与衰变"`） |
| `shots.json` / `script.md` | 分镜（机器读 / 人读） |
| `prompts.json` | 每镜完整 H3 提示词：`prompt_h3voice`（H3 同时生成画面和配音）、`prompt_tts`（画外音镜头只生成画面和环境声，配音另用 TTS） |
| `subtitles.srt` / `overlay.srt` | 底部字幕（旁白）/ 顶部文字（片名、知识点名） |
| `comfyui/minimax_h3_t2v_av_hq_20step_api.json` | ComfyUI API 工作流（`{{PROMPT}}` `{{SEED}}` `{{LENGTH}}` `{{FPS}}` 占位） |
| `source_map.json` | 知识点 → 镜头 |
| `来源.tsv` | 本课每个知识点合并了哪些原知识点（★ 为采用的最佳讲解来源） |
| `course/高校实验室安全/086_射线的性质与衰变.md` | 知识点详细内容说明书（课件由它生成） |

## 步骤

1. 生成镜头（需本地 ComfyUI 已装 MiniMax H3 模型）：
   `COMFY_URL=http://127.0.0.1:8188 python3 tools/cartoon/generate.py "project/高校实验室安全/086_射线的性质与衰变"`
   片段写入 `project/高校实验室安全/086_射线的性质与衰变/clips/shot_NNN.mp4`（86 镜）；加 `--tts` 时画外音镜头用 `prompt_tts`，
   并把 `project/高校实验室安全/086_射线的性质与衰变/tts/shot_NNN.wav` 合进片段（TTS 用 ppplus107 的 Qwen3-TTS 流程生成，旁白读法见 `prompts.json` 的 `spoken`）。
   每镜生成后检查：配音与旁白一致、结尾不截断、画面无伪字；不合格换种子重做（`--redo 镜号`）。
2. 拼接：`python3 tools/cartoon/assemble.py "project/高校实验室安全/086_射线的性质与衰变"`，按分镜顺序合并，烧录底部字幕、顶部文字和图示文字，
   输出 `project/高校实验室安全/086_射线的性质与衰变/086_射线的性质与衰变_cn_cartoon.mp4`。
   有 `实拍清单.md` 时：把拍好的片段放到 `project/高校实验室安全/086_射线的性质与衰变/footage/shot_NNN.mp4`，先运行
   `python3 tools/cartoon/live.py "project/高校实验室安全/086_射线的性质与衰变"`（统一规格并合入 TTS 配音，写入 clips/），generate.py 会跳过这些镜头。
3. 人工审核：对照 `script.md`、`来源.tsv` 和说明书 `course/高校实验室安全/086_射线的性质与衰变.md` 核对；学校适用条款由本校实验室安全管理部门确认。
