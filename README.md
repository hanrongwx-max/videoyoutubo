# 实验室安全 YouTube 系列视频下载

- `playlists.tsv`：30 个播放列表与 PDF 中的系列名称对照（用作目录名）
- `视频清单.md`：每个系列的视频、目标文件名和原链接（2026-10-28 快照，共 600 个视频，约 149 小时）
- `download.py`：下载脚本
- `downloaded.tsv`：运行后自动生成，记录已下载并推送的视频，用于断点续传

## 在本地电脑运行

```bash
pip install -U yt-dlp        # 另需安装 ffmpeg、git 和 deno（yt-dlp 解析 YouTube 需要）
git clone https://github.com/hanrongwx-max/videoyoutubo && cd videoyoutubo
git checkout claude/ecstatic-galileo-kof9rf
python3 download.py                 # 全部下载，每个视频完成后推送到当前分支
python3 download.py --only 1,19     # 只下载指定序号的系列
python3 download.py --no-push       # 只下载到本地，不推送
```

行为说明：

- 目录为 `系列名称/`，文件名为 `系列名称_序号.mp4`，序号为视频在播放列表中的位置
- 以最高清晰度下载（`bv*+ba/b`，合并为 mp4）
- 超过 95MiB 的文件分割为 `.001`、`.002`… 后提交；单次 push 不超过约 1.5GB
- 下载目录超过 25GB（`--max-gb` 可调）时，自动删除最早下载且已推送的文件
- 中断后重新运行即可续传（跳过 `downloaded.tsv` 中已有的视频）

## 合并分割的文件

```bash
cat "名称_01.mp4".0* > "名称_01.mp4"                          # macOS / Linux
copy /b "名称_01.mp4.001"+"名称_01.mp4.002" "名称_01.mp4"     # Windows（按顺序列出全部分片）
```

## 注意

- 全部最高清晰度约需 100GB 以上；GitHub 建议仓库小于 5GB，超大仓库可能被限制，请留意。
- 这些视频版权归各发布机构所有，请勿公开分发（建议将仓库设为私有）。
