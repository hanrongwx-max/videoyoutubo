#!/usr/bin/env python3
"""由《高校实验室安全》各课的“知识点详细内容说明书”生成学习课件和合订说明书。

输入：course/高校实验室安全/<课号>_<课名>.md（格式见 docs/课程编写规范（高校实验室安全）.md 第二节）
      curriculum/syllabus.tsv（章、课名、顺序）
输出：course/高校实验室安全/课件/<课号>_<课名>.pptx        每课一份学习课件
      course/高校实验室安全/课件/第N章_章名.pptx            每章合订课件
      course/高校实验室安全/说明书/第N章_章名.md            每章说明书
      course/高校实验室安全/说明书/高校实验室安全_知识点详细内容说明书.docx   全课程合订本（pandoc）

用法：python3 tools/course/make_courseware.py [--only 课号 ...] [--no-docx]
课件由说明书自动生成，不要手改 .pptx；改内容请改说明书后重新生成。
"""
import argparse
import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[2]
COURSE = "高校实验室安全"
SRC = ROOT / "course" / COURSE
OUT_PPT = SRC / "课件"
OUT_DOC = SRC / "说明书"
SYLLABUS = ROOT / "curriculum" / "syllabus.tsv"

# 配色：深蓝绿为主色，安全橙为强调色，错误做法用红色
NAVY = RGBColor(0x0B, 0x3C, 0x5D)
TEAL = RGBColor(0x1D, 0x7A, 0x8C)
ORANGE = RGBColor(0xF2, 0x8C, 0x28)
RED = RGBColor(0xC0, 0x39, 0x2B)
INK = RGBColor(0x22, 0x2B, 0x33)
MUTED = RGBColor(0x5F, 0x6B, 0x75)
LIGHT = RGBColor(0xEE, 0xF4, 0xF7)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PINK = RGBColor(0xFB, 0xEC, 0xEA)
FONT = "Microsoft YaHei"
W, H = Inches(13.333), Inches(7.5)
M = Inches(0.6)


# ---------------------------------------------------------------- 解析说明书
def parse(path):
    text = path.read_text(encoding="utf-8")
    les = {"file": path, "title": "", "info": {}, "goals": [], "basis": [], "points": [], "live": [], "quiz": []}
    m = re.search(r"^# (\d{3})\s*(.+)$", text, re.M)
    les["id"], les["title"] = (m.group(1), m.group(2).strip()) if m else (path.stem[:3], path.stem[4:])
    sections = re.split(r"^## ", text, flags=re.M)[1:]
    for sec in sections:
        head, _, body = sec.partition("\n")
        head = head.strip()
        if head == "基本信息":
            goals = False
            for ln in body.splitlines():
                if re.match(r"\s*-\s*学习目标", ln):
                    goals = True
                    continue
                g = re.match(r"\s+\d+[.、]\s*(.+)", ln)
                if goals and g:
                    les["goals"].append(g.group(1).strip())
                    continue
                kv = re.match(r"-\s*([^：:]+)[：:]\s*(.+)", ln)
                if kv:
                    goals = False
                    les["info"][kv.group(1).strip()] = kv.group(2).strip()
        elif head.startswith("法规"):
            les["basis"] = [ln.lstrip("- ").strip() for ln in body.splitlines() if ln.strip().startswith("-")]
        elif head == "知识点":
            for blk in re.split(r"^### ", body, flags=re.M)[1:]:
                h, _, b = blk.partition("\n")
                km = re.match(r"([KS]\d+)\s+(.+)", h.strip())
                p = {"key": km.group(1) if km else "", "name": km.group(2).strip() if km else h.strip(),
                     "bullets": [], "detail": "", "mistakes": [], "source": ""}
                part = None
                for ln in b.splitlines():
                    s = ln.strip()
                    if s.startswith("**要点**"):
                        part = "bullets"
                    elif s.startswith("**详细说明**"):
                        part = "detail"
                    elif s.startswith("**常见错误**"):
                        part = "mistakes"
                    elif s.startswith("**来源**"):
                        p["source"] = re.sub(r"^\*\*来源\*\*[：:]?\s*", "", s)
                        part = None
                    elif part in ("bullets", "mistakes") and s.startswith("-"):
                        p[part].append(s.lstrip("- ").strip())
                    elif part == "detail" and s:
                        p["detail"] += s + "\n"
                les["points"].append(p)
        elif head.startswith("实拍"):
            les["live"] = [ln.lstrip("- ").strip() for ln in body.splitlines() if ln.strip().startswith("-")]
        elif head.startswith("课后练习"):
            for q in re.split(r"^\d+[.、]\s*", body, flags=re.M)[1:]:
                lines = [x.strip() for x in q.strip().splitlines() if x.strip()]
                if not lines:
                    continue
                item = {"q": lines[0], "opts": [], "ans": ""}
                for x in lines[1:]:
                    x = x.lstrip("- ").strip()
                    if x.startswith("答案"):
                        item["ans"] = x
                    else:
                        item["opts"].append(x)
                les["quiz"].append(item)
    return les


def strip_md(s):
    return re.sub(r"\*\*|`", "", s)


# ---------------------------------------------------------------- 课件
def tb(slide, x, y, w, h, text="", size=16, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, name=None):
    box = slide.shapes.add_textbox(x, y, w, h)
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    lines = text if isinstance(text, list) else [text]
    for i, line in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        r = para.add_run()
        r.text = strip_md(line)
        r.font.size, r.font.bold, r.font.name = Pt(size), bold, FONT
        r.font.color.rgb = color
    return box


def rect(slide, x, y, w, h, fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=None):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    if name:
        s.name = name
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.fill.background()
    s.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.08
    return s


def badge(slide, x, y, d, text, fill, color=WHITE, size=16):
    c = rect(slide, x, y, d, d, fill, MSO_SHAPE.OVAL)
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.size, r.font.bold, r.font.name = Pt(size), True, FONT
    r.font.color.rgb = color
    return c


def bullets(slide, x, y, w, h, items, size=17, color=INK, gap=10):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, it in enumerate(items):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.space_after = Pt(gap)
        r = para.add_run()
        r.text = "▪ " + strip_md(it)
        r.font.size, r.font.name = Pt(size), FONT
        r.font.color.rgb = color
    return box


def header(slide, les, title, kicker):
    """内容页统一页眉：左上角小字（课号·课名），大标题；右下角页脚。"""
    tb(slide, M, Inches(0.35), Inches(9), Inches(0.35), kicker, 12, TEAL, True)
    tb(slide, M, Inches(0.7), W - 2 * M, Inches(0.8), title, 30, NAVY, True)
    tb(slide, M, H - Inches(0.45), Inches(8), Inches(0.3), f"《{COURSE}》 {les['id']} {les['title']}", 10, MUTED)


def bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def add_lesson(prs, les, chapter):
    blank = prs.slide_layouts[6]
    kicker = f"{les['id']} · {les['title']}"
    # 封面
    s = prs.slides.add_slide(blank)
    bg(s, NAVY)
    rect(s, M, Inches(1.4), Inches(1.1), Inches(1.1), ORANGE, MSO_SHAPE.OVAL)
    tb(s, M, Inches(1.4), Inches(1.1), Inches(1.1), les["id"], 24, WHITE, True, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
    tb(s, M, Inches(2.9), W - 2 * M, Inches(1.2), les["title"], 44, WHITE, True)
    tb(s, M, Inches(4.2), W - 2 * M, Inches(0.5), chapter, 20, RGBColor(0xCA, 0xDC, 0xE6))
    info = "　".join(f"{k}：{les['info'][k]}" for k in ("课时", "适用对象") if k in les["info"])
    tb(s, M, Inches(4.8), W - 2 * M, Inches(0.5), info, 14, RGBColor(0xCA, 0xDC, 0xE6))
    tb(s, M, H - Inches(0.8), Inches(8), Inches(0.4), f"《{COURSE}》学习课件", 14, ORANGE, True)
    # 学习目标
    if les["goals"]:
        s = prs.slides.add_slide(blank)
        bg(s, WHITE)
        header(s, les, "学习目标", kicker)
        n = len(les["goals"])
        cw = (W - 2 * M - Inches(0.4) * (n - 1)) / n
        for i, g in enumerate(les["goals"]):
            x = M + i * (cw + Inches(0.4))
            rect(s, x, Inches(2.0), cw, Inches(4.3), LIGHT)
            badge(s, x + Inches(0.35), Inches(2.35), Inches(0.75), str(i + 1), TEAL, size=20)
            tb(s, x + Inches(0.35), Inches(3.4), cw - Inches(0.7), Inches(2.7), g, 18, INK)
    # 法规依据
    if les["basis"]:
        s = prs.slides.add_slide(blank)
        bg(s, WHITE)
        header(s, les, "法规与标准依据", kicker)
        items = les["basis"][:8]
        rows = (len(items) + 1) // 2
        rh = min(Inches(1.05), (H - Inches(2.6)) / max(rows, 1))
        cw = (W - 2 * M - Inches(0.4)) / 2
        for i, b in enumerate(items):
            x = M + (i % 2) * (cw + Inches(0.4))
            y = Inches(1.9) + (i // 2) * (rh + Inches(0.15))
            rect(s, x, y, cw, rh, LIGHT)
            badge(s, x + Inches(0.2), y + (rh - Inches(0.5)) / 2, Inches(0.5), "§", NAVY, size=16)
            tb(s, x + Inches(0.9), y + Inches(0.1), cw - Inches(1.1), rh - Inches(0.2), b, 14, INK, anchor=MSO_ANCHOR.MIDDLE)
        if len(les["basis"]) > 8:
            s.notes_slide.notes_text_frame.text = "其余依据：\n" + "\n".join(les["basis"][8:])
    # 知识点
    for p in les["points"]:
        s = prs.slides.add_slide(blank)
        bg(s, WHITE)
        header(s, les, p["name"], kicker)
        badge(s, W - M - Inches(0.9), Inches(0.45), Inches(0.9), p["key"], ORANGE, size=18)
        has_err = bool(p["mistakes"])
        lw = (W - 2 * M) * (0.6 if has_err else 1.0)
        rect(s, M, Inches(1.8), lw, Inches(4.8), LIGHT)
        tb(s, M + Inches(0.4), Inches(2.05), Inches(3), Inches(0.4), "要点", 16, TEAL, True)
        nb = len(p["bullets"]) or 1
        size = 20 if nb <= 4 else 17
        bullets(s, M + Inches(0.4), Inches(2.6), lw - Inches(0.8), Inches(0.62) * nb, p["bullets"] or [p["detail"][:60]], size)
        brief = strip_md(p["detail"].strip().split("\n")[0]) if p["detail"].strip() else ""
        if brief and nb <= 5:   # 详细说明首段作学习提示（全文在备注）
            if len(brief) > 110:
                brief = brief[:108] + "……"
            tb(s, M + Inches(0.4), Inches(2.75) + Inches(0.62) * nb, lw - Inches(0.8), Inches(0.35), "说明", 13, TEAL, True)
            tb(s, M + Inches(0.4), Inches(3.15) + Inches(0.62) * nb, lw - Inches(0.8), Inches(6.3) - Inches(3.15) - Inches(0.62) * nb,
               brief, 14, MUTED)
        if has_err:
            x = M + lw + Inches(0.4)
            ew = W - M - x
            rect(s, x, Inches(1.8), ew, Inches(4.8), PINK)
            badge(s, x + Inches(0.4), Inches(2.0), Inches(0.5), "✕", RED, size=16)
            tb(s, x + Inches(1.05), Inches(2.05), ew - Inches(1.4), Inches(0.4), "常见错误", 16, RED, True)
            bullets(s, x + Inches(0.4), Inches(2.75), ew - Inches(0.8), Inches(3.6), p["mistakes"], 15, INK)
        notes = p["detail"].strip()   # 来源（原视频名称）不进课件，见 来源.tsv
        if notes:
            s.notes_slide.notes_text_frame.text = strip_md(notes)
    # 课后练习：每页两题，答案在备注
    for i in range(0, len(les["quiz"]), 2):
        s = prs.slides.add_slide(blank)
        bg(s, WHITE)
        header(s, les, "课后练习", kicker)
        cw = (W - 2 * M - Inches(0.4)) / 2
        for j, q in enumerate(les["quiz"][i:i + 2]):
            x = M + j * (cw + Inches(0.4))
            rect(s, x, Inches(1.8), cw, Inches(4.8), LIGHT)
            badge(s, x + Inches(0.35), Inches(2.05), Inches(0.6), str(i + j + 1), NAVY, size=16)
            tb(s, x + Inches(1.15), Inches(2.1), cw - Inches(1.5), Inches(1.4), q["q"], 17, INK, True)
            opts = re.split(r"\s+(?=[B-D][.．、])", " ".join(q["opts"])) if q["opts"] else []
            tb(s, x + Inches(1.15), Inches(3.6), cw - Inches(1.5), Inches(2.8), opts, 15, INK)
        s.notes_slide.notes_text_frame.text = "\n".join(f"第 {i + k + 1} 题 {q['ans']}" for k, q in enumerate(les["quiz"][i:i + 2]))
    # 小结
    s = prs.slides.add_slide(blank)
    bg(s, NAVY)
    tb(s, M, Inches(0.6), W - 2 * M, Inches(0.8), "本课小结", 34, WHITE, True)
    names = [f"{p['key']}  {p['name']}" for p in les["points"]]
    half = (len(names) + 1) // 2
    cw = (W - 2 * M - Inches(0.4)) / 2
    for col, chunk in enumerate((names[:half], names[half:])):
        bullets(s, M + col * (cw + Inches(0.4)), Inches(1.8), cw, Inches(5), chunk, 18 if len(names) <= 10 else 15,
                WHITE, 8)


def new_prs():
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    prs.core_properties.title = f"《{COURSE}》学习课件"
    return prs


# ---------------------------------------------------------------- 说明书合订
def chapter_md(chapter, lessons):
    parts = [f"# {chapter}\n"]
    for les in lessons:
        body = les["file"].read_text(encoding="utf-8")
        parts.append(re.sub(r"^#", "##", body, flags=re.M))   # 每级标题降一级，放进章下
    return "\n\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="只生成这些课号的课件，并只重建它们所在章的合订课件和章说明书")
    ap.add_argument("--no-docx", action="store_true")
    args = ap.parse_args()
    syl = list(csv.DictReader(open(SYLLABUS, encoding="utf-8"), delimiter="\t"))
    files = {p.name[:3]: p for p in SRC.glob("[0-9][0-9][0-9]_*.md")}
    OUT_PPT.mkdir(parents=True, exist_ok=True)
    OUT_DOC.mkdir(parents=True, exist_ok=True)
    chapters = {}
    for r in syl:
        if r["lesson_id"] in files:
            chapters.setdefault(r["章"], []).append((r, parse(files[r["lesson_id"]])))
    n = 0
    for chapter, items in chapters.items():
        if args.only and not any(les["id"] in args.only for _, les in items):
            continue   # 只重建包含指定课的章，避免无谓地改写其他章的合订文件
        for r, les in items:
            if args.only and les["id"] not in args.only:
                continue
            prs = new_prs()
            add_lesson(prs, les, chapter)
            prs.save(OUT_PPT / f"{les['file'].stem}.pptx")
            n += 1
        prs = new_prs()
        for r, les in items:
            add_lesson(prs, les, chapter)
        safe = re.sub(r"[\\/:*?\"<>| ]+", "_", chapter)
        prs.save(OUT_PPT / f"{safe}.pptx")
        (OUT_DOC / f"{safe}.md").write_text(chapter_md(chapter, [les for _, les in items]), encoding="utf-8")
    print(f"课件：{n} 课，{len(chapters)} 章合订")
    if not args.no_docx and chapters:
        if not shutil.which("pandoc"):
            sys.exit("没有 pandoc，跳过 docx（可加 --no-docx）")
        mds = [OUT_DOC / f"{re.sub(r'[\\/:*?\"<>| ]+', '_', c)}.md" for c in chapters]
        out = OUT_DOC / f"{COURSE}_知识点详细内容说明书.docx"
        subprocess.run(["pandoc", "--toc", "--toc-depth=3", "-M", f"title=《{COURSE}》知识点详细内容说明书",
                        "-o", str(out), *map(str, mds)], check=True)
        print("说明书：", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
