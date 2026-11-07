#!/usr/bin/env python3
"""把《高校实验室安全》整理成 VMS 课程资料包（格式 vms-course-pack/1）。

格式说明和自检工具来自用户提供的 vms-course-pack 交接包（README.md、course_pack.py）。
每节课一集：集号 = 章号两位-课号三位（如 06-061），知识点编号 = 课号.K1；剧本取自 src.py 的 SHOTS（英文画面用原始描述，
画风、角色外观、防伪字句由 VMS 生成时拼装）；旁白按读法写数字（tools/cartoon/style.spoken，119 → 幺幺九，第073课 → 第七十三课）。
资料包不含代码：materials/<集号>/ 放本课说明书、学习课件、来源对照、实拍清单；docs/ 放大纲、汇总、待确认清单和全课程说明书。

用法：python3 tools/vms_pack.py <输出目录>        生成 <输出目录>/gaoxiao-lab-safety/ 和同名 .zip
"""
import csv
import json
import re
import runpy
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "cartoon"))
from style import LOCAL_CHARACTERS, LOCAL_STYLE, LOCAL_VOICE, spoken  # noqa: E402

CODE = "gaoxiao-lab-safety"
COURSE = "高校实验室安全"
PROJ = ROOT / "project" / COURSE
DOCS = ROOT / "course" / COURSE
NAMES = {  # docs/卡通改编规范.md 的固定角色
    "panda mascot": ("欣欣", "熊猫主持"),
    "female graduate student": ("小研", "研究生，兼实验室安全员"),
    "older man": ("老周", "实验室负责人、资深教师"),
    "young male student": ("阿杰", "本科生、新进实验室的学生"),
    "safety administrator": ("王老师", "学院实验室安全管理员"),
    "facility engineer": ("老李", "设施与设备工程师"),
    "security officer": ("保卫处值班员", "学校保卫处"),
}
SPECIAL = ("开场", "情景", "小结", "结尾")
ROLES = tuple(LOCAL_CHARACTERS)
# 泛指的人或身体部位：画面里有人但不是固定角色，不能加 No people
PEOPLE = re.compile(r"\b(person|people|persons|hands?|students?|workers?|man|men|woman|women|figures?|someone|anyone|"
                    r"technicians?|researchers?|staff|colleagues?|operators?|users?|visitors?|teachers?|instructors?|"
                    r"doctors?|nurses?|firefighters?|electricians?|welders?|crowd|team|group|children|child|boy|girl|"
                    r"guests?|engineers?|scientists?|cleaners?|contractors?|arms?|fingers?|face|faces|eyes?|body|"
                    r"employees?|patients?|victims?|he|she|they|his|her|their|helper|rescuer|wearer|supervisors?|"
                    r"members?|officers?|inspectors?|investigators?|speakers?|leaders?|mothers?|fathers?|parents?|"
                    r"drivers?|authors?|responders?|travell?ers?|owners?|hikers?|auditors?|farmers?|neighbou?rs?|"
                    r"bystanders?|watchers?|suppliers?|partners?|recipients?|reviewers?|managers?|attendants?|"
                    r"couriers?|handlers?|trainers?|trainees?|keepers?|runners?|shoulders?|waist|wrists?|trousers?|"
                    r"cheaters?|guards?|pilots?|family|friends?|babies|baby|wife|husband|police|crew|lecturer|"
                    r"professors?|pupils?|novices?|newcomers?|applicants?|candidates?|volunteers?|spectators?|"
                    r"residents?|cook|chef|head|heads|legs?|feet|foot|thighs?|torso|lips?|mouth|nose|skin|"
                    r"silhouettes?)\b", re.I)
# VMS 自检提醒的“要求画出文字”的说法（H3 会画出伪字）：换成不诱发文字的同义说法
REWORD = [(r"\bbeing read\b", "being viewed"), (r"\bread twice\b", "checked twice"),
          (r"\breading (a|an|the)\b", r"looking at \1"), (r"\breading\b", "value"), (r"\breads\b", "looks over"),
          (r"\bread\b", "check"), (r"\blabell?ed\b", "marked"), (r"\bwritten\b", "recorded"), (r"\bsays\b", "suggests"),
          (r"\bsaying\b", "suggesting")]


def fix_prompt(en):
    for a, b in REWORD:
        en = re.sub(a, b, en)
    low = en.lower()
    if not any(r in low for r in ROLES) and "no people" not in low and not PEOPLE.search(en):
        en = "No people. " + en
    return en


def lessons():
    with open(ROOT / "curriculum" / "syllabus.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            r["chapter"] = int(re.match(r"第(\d+)章", r["章"]).group(1))
            r["dir"] = f"{r['lesson_id']}_{r['课名']}"
            r["vid"] = f"{r['chapter']:02d}-{r['lesson_id']}"
            yield r


def episode(r):
    d = PROJ / r["dir"]
    src = runpy.run_path(str(d / "src.py"))
    meta, shots = src["META"], src["SHOTS"]
    lid = r["lesson_id"]
    with open(d / "来源.tsv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    videos = []
    for x in rows:
        series, video = x["原知识点 id"].split("|")[:2]
        v = f"{series}/{video.split('_')[0]}"
        if v not in videos:
            videos.append(v)
    kps = [{"id": f"{lid}.{k}", "title": t, "pages": []} for k, t in meta["points"].items()]
    out = []
    for s in shots:
        kp = s[0] if s[0] in SPECIAL else f"{lid}.{s[0]}"
        shot = {"kp": kp, "scene": s[1], "prompt_en": fix_prompt(s[2]), "narration": spoken(s[3])}
        if len(s) > 4 and s[4]:
            shot["overlay"] = s[4]
        if len(s) > 5 and s[5]:
            shot["labels"] = list(s[5])
        out.append(shot)
    ep = {"id": r["vid"], "title": meta["title"], "chapter": r["chapter"], "book_sections": [r["章"]],
          "source_lessons": videos, "knowledge_points": kps, "shots": out}
    return ep, meta.get("avoid", []), rows


def avoid_list(all_avoid, eps):
    """VMS 自检按小写子串查回避词（本项目按整词）：会误中正常用词的短词（如 WHO→whole）不放进 avoid.txt，另列说明。"""
    texts = []
    for e in eps:
        for s in e["shots"]:
            texts.append(" ".join([s["scene"], s["prompt_en"], s["narration"], s.get("overlay", "")] + s.get("labels", [])).lower())
    blob = "\n".join(texts)
    keep, dropped = [], []
    for a in sorted({a.strip() for a in all_avoid if a.strip()}, key=str.lower):
        (dropped if a.lower() in blob else keep).append(a)
    return keep, dropped


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    pack = out / CODE
    if pack.exists():
        shutil.rmtree(pack)
    (pack / "episodes").mkdir(parents=True)
    eps, all_avoid = [], []
    for r in lessons():
        ep, av, rows = episode(r)
        eps.append(ep)
        all_avoid += av
        (pack / "episodes" / f"{ep['id']}.json").write_text(json.dumps(ep, ensure_ascii=False, indent=1), encoding="utf-8")
        m = pack / "materials" / ep["id"]
        m.mkdir(parents=True)
        shutil.copy(DOCS / f"{r['dir']}.md", m / "知识点详细内容说明书.md")
        ppt = DOCS / "课件" / f"{r['dir']}.pptx"
        if ppt.exists():
            shutil.copy(ppt, m / "学习课件.pptx")
        live = PROJ / r["dir"] / "实拍清单.md"
        if live.exists():
            shutil.copy(live, m / "实拍清单.md")
        with open(m / "来源对照.csv", "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["知识点编号", "原知识点 id", "最佳讲解"])
            for x in rows:
                w.writerow([f"{r['lesson_id']}.{x['课内编号']}", x["原知识点 id"], x["采用"]])

    keep, dropped = avoid_list(all_avoid, eps)
    (pack / "avoid.txt").write_text("# 原素材的机构、品牌、人名、频道名（剧本不得出现）\n" + "\n".join(keep) + "\n", encoding="utf-8")

    chars = [{"role_en": k, "name_zh": NAMES[k][0], "title_zh": NAMES[k][1], "host": k == "panda mascot",
              "appearance_en": v} for k, v in LOCAL_CHARACTERS.items()]
    (pack / "characters.json").write_text(json.dumps(chars, ensure_ascii=False, indent=1), encoding="utf-8")

    n_shots = sum(len(e["shots"]) for e in eps)
    manifest = {
        "format": "vms-course-pack/1", "code": CODE, "name": COURSE,
        "audience": "高校本科生、研究生、新进教职工和博士后，以及进入实验室的外来人员",
        "style": "扁平 2D 卡通，熊猫“欣欣”主持（与 ppplus107 系列同一画风和角色）",
        "description": f"由 441 个实验室安全教学视频的全部知识点合并整理的全新卡通微课：15 章 {len(eps)} 节、{n_shots} 镜，"
                       "每节配知识点详细内容说明书和学习课件",
        "basis": "按国内法律法规、国家标准和《高等学校实验室安全规范》（教科信厅函〔2023〕5 号）编写，"
                 "学校—学院—实验室三级管理；拿不准的条款和数值写“以现行文本为准”，见 docs/待确认清单.md",
        "source": {"title": "441 个外国实验室安全（及实验技术）教学视频，25 个剧集", "kind": "video"},
        "generation": {"style_en": LOCAL_STYLE, "voice_en": LOCAL_VOICE, "max_line": 20,
                       "min_seconds": 180, "max_seconds": 600},
    }
    (pack / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

    docs = pack / "docs"
    docs.mkdir()
    for src, name in [("curriculum/课程大纲.md", "课程大纲.md"), ("curriculum/实拍汇总.md", "实拍汇总.md"),
                      ("curriculum/不收录清单.md", "不收录清单.md"), ("docs/课程编写规范（高校实验室安全）.md", "课程编写规范.md"),
                      ("docs/实拍素材评估与拍摄规范.md", "实拍素材评估与拍摄规范.md")]:
        shutil.copy(ROOT / src, docs / name)
    with open(ROOT / "curriculum" / "syllabus.tsv", encoding="utf-8") as f, \
            open(docs / "课程目录.csv", "w", encoding="utf-8-sig", newline="") as g:
        w = csv.writer(g)
        for i, row in enumerate(csv.reader(f, delimiter="\t")):
            w.writerow((["集号"] if i == 0 else [eps[i - 1]["id"]]) + row)
    (docs / "说明书").mkdir()
    for f in sorted((DOCS / "说明书").iterdir()):
        if f.suffix in (".md", ".docx"):
            shutil.copy(f, docs / "说明书" / f.name)
    todo = (ROOT / "docs" / "高校实验室安全_待核对引用清单.md").read_text(encoding="utf-8")
    todo = todo.replace("# 《高校实验室安全》待核对引用清单", "# 待确认清单", 1)
    todo += ("\n## 其他待确认\n\n"
             "- 152 课角色“小研”的孕期设定是否保留。\n"
             "- 196、197 课焊机部件（开关电源、激光电源、安全继电器等）的功能说明按通用知识编写，需设备工程师审核。\n"
             "- 剧本中 `【实拍】` 开头的中文画面建议用本校实拍素材替换（见 docs/实拍汇总.md 和各集 materials/实拍清单.md）；"
             "英文画面是没有实拍素材时的备用卡通描述。\n"
             f"- 回避清单：各课的回避词合并后，有 {len(dropped)} 个会被 VMS 的子串检查误中，未放进 avoid.txt："
             "有的是被别的词包含（如 WHO 在 whole 里），有的在其他课是正常用语（如 MSDS、ISO、BSL）。"
             f"编写时已逐课按整词检查，相应课的剧本不含这些名称：{'、'.join(dropped) or '无'}。\n")
    n_warn_people = sum(1 for e in eps for s in e["shots"]
                        if not any(r in s["prompt_en"].lower() for r in ROLES) and "no people" not in s["prompt_en"].lower())
    (docs / "资料包说明.md").write_text(
        f"# 资料包说明：《{COURSE}》\n\n"
        f"- 集数：{len(eps)} 集（每节微课一集，集号“章-课号”，如 06-061 为第 6 章第 061 课）；镜头 {n_shots} 镜，"
        f"约 {n_shots * 5 / 3600:.1f} 小时；每集 {min(len(e['shots']) for e in eps)}–{max(len(e['shots']) for e in eps)} 镜。\n"
        "- 知识点：编号“课号.K1”（原视频知识点合并）和“课号.S1”（按国内要求补充），名称同说明书。"
        "原知识点来源见各集 materials/来源对照.csv，source_lessons 为原剧集/视频序号。\n"
        "- 人物 7 个：欣欣（熊猫主持，host）、小研、老周、阿杰、王老师、老李、保卫处值班员，外观与 ppplus107 系列一致。\n"
        "- 没有国内版（xxCN）：本课程本身就是按国内法规编写的国内课程。\n"
        "- 工作流：未提供，用 VMS 现有的 MiniMax H3 工作流。\n"
        "- 旁白中的数字已按读法写（幺幺九、第七十三课）。\n"
        "- 英文画面相对仓库剧本的调整：纯物体/示意图镜头前加 “No people.”；"
        "labeled、reads、written 等会诱发文字的说法换成 marked、looks over、recorded 等。\n"
        f"- 自检提醒：{n_warn_people} 镜画面里有手或泛指的人（不是固定角色），不能写 No people，属正常情况。\n"
        "- 中文画面以【实拍】开头的镜头建议用本校实拍素材替换，规范见 docs/实拍素材评估与拍摄规范.md。\n"
        "- 每集资料：materials/<集号>/ 下有知识点详细内容说明书、学习课件（pptx）、来源对照、实拍清单；"
        "docs/说明书/ 有每章说明书和全课程合订本（docx）。\n"
        "- 待确认内容见 docs/待确认清单.md。\n", encoding="utf-8")
    (docs / "待确认清单.md").write_text(todo, encoding="utf-8")

    z = out / f"{CODE}.zip"
    if z.exists():
        z.unlink()
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(pack.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(out).as_posix())
    print(f"{len(eps)} 集、{n_shots} 镜；avoid {len(keep)} 个（未放 {len(dropped)} 个）；{z}（{z.stat().st_size / 1e6:.1f} MB）")


if __name__ == "__main__":
    main()
