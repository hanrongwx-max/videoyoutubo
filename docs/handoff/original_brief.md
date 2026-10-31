You are writing the **原著版 (original edition)** cartoon script for ONE lab-safety teaching video in the repo /home/user/videoyoutubo. Deliverables are in Chinese.

Background: each video gets two cartoon editions.
- `project/<剧集>/<视频名称>（国内版）/` is the domestic edition. It is adapted to Chinese laws and university requirements, adds S points and has a 审查报告.md. It already exists. Do not edit it.
- `project/<剧集>/<视频名称>/` is the original edition, which you write. The user wants it **完全照原片**: the same content as the original video, with no localisation, no corrections and no supplementary points.

Read first:
- docs/卡通改编规范.md, for the script tuple format, fixed roles and style.
- docs/交接文档.md, section 五, for environment notes.

Inputs:
- course/<剧集>/<视频名称>.md is the full content document: K points, narration by section, on-screen text and the shot table. This is your main source.
- The domestic src.py, for style and characters only. Its K-point titles are a useful starting list, but the content must follow the original, not the domestic changes.
- work/<剧集>/<视频名称>/ (analysis.md, transcript, sheet_NN.jpg), if you need to check exactly what the original says or shows.

Write `project/<剧集>/<视频名称>/src.py`:
- META = {"title": <the same Chinese title as the domestic edition's META["title"]>, "edition": "原著版", "points": {"K1": …}, "avoid": [...]}
  - points: exactly the K points of the content document, same keys and titles. **No S points.**
  - avoid: copy the domestic edition's list.
- Retell the original faithfully, keeping all of the following as the original has them:
  - Its regulations, agencies and standards, for example a foreign law, agency or emergency number. Say them as the original does, e.g. "按美国职业安全卫生法规", "拨打911".
  - Its numbers, procedures, order of steps, examples and conclusions.
  - Its mistakes and unsafe practices: show them as the original shows them, and do not correct or flag them (user decision: 完全照原片). The content document's error notes stay in the content document only.
  - Its framing, e.g. risk-group numbering exactly as the original states it. Do not add the China-direction note.
  - For an off-topic or promotional video: its actual content, with brands kept out.
- Copyright rules still apply, in every case:
  - New narration in your own words, new scenario and new visuals with the fixed cartoon roles (panda 欣欣 hosting).
  - No original producer, channel, lecturer, university or brand names. Put them in META["avoid"].
  - Real people become cartoon roles.
- Hard safety limit, which overrides faithfulness: no agent-specific weaponization, production, enhancement or dissemination details for biological agents, and no recipe-level instructions for making dangerous substances. If the original contains any, keep that part generic, just as the domestic edition did.
- Format, the same as all scripts:
  - Shots: 5 s each, narration ≤20 characters, English prompt with no Chinese.
  - Structure: 开场 → 情景 → K sections, with 顶部文字 on each section's first shot → 小结 → exactly one 结尾.
  - Length: 2–15 minutes. It is normally close to the domestic edition minus its S sections.

Do not write a 审查报告.md for the original edition. Do not edit the content document or the domestic folder.

Then:
1. Run `python3 tools/cartoon/build_project.py --only "project/<剧集>/<视频名称>"` and fix src.py until it shows no 问题 (exit 0).
2. Remove `__pycache__`.
3. Publish immediately with `python3 tools/publish.py "<剧集>" "<视频名称>" -m "<剧集> / <视频名称>: 原著版 cartoon script"`.

Several writers run in parallel. Touch only your own folders and use unique scratch filenames.

Final reply: one line per video giving the shot count and duration, the number of K points, and anything notable kept from the original.
