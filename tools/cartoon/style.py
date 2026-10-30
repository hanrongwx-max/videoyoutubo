"""卡通教学视频的画风、角色和 MiniMax H3 提示词拼装。

与 hanrongwx-max/ppplus107 的 tools/generate_videos.py 保持一致（扁平 2D 卡通、熊猫欣欣主持、固定角色外观、
画面不出文字、国家标准安全标志式样、GB/T 7144 气瓶颜色），以便两个项目的成片风格统一。
原样摘自 ppplus107（2026-10-30，e9195b4），只把“是否有 TTS 配音”改成参数；ppplus107 更新提示词后请同步本文件。
"""
import re

LOCAL_STYLE = ("Flat 2D cartoon animation for a lab safety training video, bright soft colors, bold clean outlines, "
               "simple clean laboratory background, steady camera. ")
LOCAL_CHARACTERS = {
    "panda mascot": "The panda mascot: a chubby black-and-white giant panda with black eye patches and a round white face, "
            "always wearing a bright yellow hard hat, clear safety goggles and a green cross badge on its chest.",
    "female graduate student": "The female graduate student: a young Chinese woman with a black ponytail, always wearing "
            "a knee-length white lab coat, long pants, closed-toe shoes and safety goggles.",
    "older man": "The older man: a friendly man about fifty with short graying hair and thin-rimmed glasses, always wearing "
            "a dark navy blue lab coat (never a white coat).",
    "young male student": "The young male student: a young Chinese man with short curly hair, always wearing "
            "a light gray hoodie under an open white lab coat.",
    "safety administrator": "The safety administrator: a Chinese woman about forty with short black hair, always wearing "
            "a light blue shirt under a dark green vest with a plain armband and holding a blank clipboard.",
    "facility engineer": "The facility engineer: a stocky Chinese man about forty-five, always wearing a dark gray work "
            "uniform, a white hard hat and a tool belt.",
    "security officer": "The security officer: a tall young Chinese man, always wearing a plain dark blue security uniform "
            "and cap with no badges or lettering.",
}
LOCAL_TAIL = (" Walls are plain and clean, with no posters, whiteboards or signs unless described above; all books, "
              "screens, charts, calendars and labels are blank solid color shapes or simple pictograms; doors are "
              "plain, and any door plate, room sign or nameplate on or above a door is a blank solid-color panel with "
              "no characters, letters or numbers; shelves, binders and bottles have no labels. Absolutely no text, no letters, no Chinese characters, no numbers, no writing "
              "anywhere in the frame; no subtitles, no captions, no title bars, no speech bubbles; the spoken line is "
              "audio only and is never written on screen.")
LOCAL_VOICE = ("Audio: only one voice, a warm, clear young female Mandarin Chinese narrator voice at a natural, "
               "steady pace, speaking standard Putonghua; light soft background ambience, no music.")
# TTS 配音的画外音镜头（2026-10-28）：提示词里不再写中文旁白（伪字 72% 是 H3 把旁白画到了画面上），
# H3 只出画面和环境声，生成后把 courses/<编号>/tts/ 里的配音合进片段
TTS_LINE = ("Nobody in the scene talks: every character keeps a calm closed-mouth expression with lips together the "
            "whole time, no lip movement.")
TTS_AUDIO = "Audio: only soft, quiet room ambience; no voice, no speech, no narration, no music."
TTS_LEAD = 0.15   # 配音在镜头开头留的空（秒）
AUDIO_RATE = 32000   # H3 片段的音频采样率（AAC 立体声），合进来的配音用同样的参数
# 门牌最容易出伪字（用户 2026-10-28 审片发现）：画面里有门时再单独强调门牌是空白色块；要写门牌名的走图示文字 labels 后期叠加。
# 只写“不要门牌”H3 照样画，所以写成“门牌是空白色块”的正向描述
DOOR_GUARD = ("Every door plate, room sign and nameplate on or above any door is a blank plain solid-color panel "
              "without any characters, letters or numbers.")
DOOR_WORDS = re.compile(r"\b(doors?|doorways?|corridors?|hallways?|offices?|entrances?)\b", re.I)
# 安全出口的门例外（用户 2026-10-28）：门上方是绿色安全出口标志图案（GB 2894-2025 / GB 13495.1，同 sign_catalog 的 exit），不带字。
# 只在画面写到安全出口、疏散时才提，免得普通场景也画出出口标志
EXIT_WORDS = re.compile(r"\b(emergency|fire|safety) exits?\b|\bexit (doors?|signs?|routes?)\b|\bevacuat\w*|\bescape routes?\b",
                        re.I)
EXIT_SIGN = ("the standard green exit sign: a green rectangle with a white running figure moving through a white door "
             "frame and a white arrow pointing the way out, with no words")
DOOR_GUARD_EXIT = DOOR_GUARD[:-1] + f", except the sign above an emergency exit door, which is {EXIT_SIGN}."
TAIL_DOOR = ("any door plate, room sign or nameplate on or above a door is a blank solid-color panel with no characters, "
             "letters or numbers")



def spoken(text):
    """电话号码等三位以上数字按位读（119 → 幺幺九），避免配音读成“一百一十九”；字幕仍显示阿拉伯数字。"""
    return re.sub(r"\d{3,}", lambda m: "".join("零幺二三四五六七八九"[int(d)] for d in m.group()), text)



TEXTY = ("sign", "poster", "label", "screen", "monitor", "tablet", "board", "whiteboard", "notice", "document", "form",
         "paper", "sheet", "checklist", "list", "report", "book", "manual", "binder", "folder", "card", "map", "plan",
         "chart", "badge", "tag", "plate", "calendar", "clipboard", "phone", "laptop", "computer", "certificate",
         "record", "file", "letter", "envelope", "display", "diagram", "icon", "flowchart", "timeline", "table")
FIX_TRIES = 2   # 同一级提示词连续几次出现伪字就再调整一级：首次生成 + 重试 1 次（用户 2026-10-28，原为 3）
BOTTOM_Y = 560  # 文字框上沿低于这个高度（704 高的画面）就当作旁白被画成了底部字幕
DIAGRAM = ("connect", "connects", "arrow", "arrows", "flow", "flows", "diagram", "icon", "icons", "network", "lines",
           "steps", "loop", "chain", "node", "nodes", "timeline", "flowchart")  # 示意图类镜头：H3 爱给每个元素配文字


def text_fix(shot, problems, level):
    """连续出现伪字时的提示词调整：level 1 逐个说明道具空白、底部字幕单独禁止；level 2 再把画面简化成少量大元素。"""
    tops = [int(m) for p in problems if "文字" in p for m in re.findall(r"位置 \[\d+, (\d+),", p)]
    words = re.findall(r"[a-z]+", shot["prompt_en"].lower())
    objs = sorted({w for w in TEXTY if w in words or w + "s" in words})
    return {"level": level, "bottom": any(y >= BOTTOM_Y for y in tops), "objs": objs,
            "diagram": any(w in words for w in DIAGRAM)}


def text_guard(shot):
    """从第一次生成起就防伪字：
    - 有图示文字（shot["labels"]，拼接时按一行等分位置叠加汉字）：要求这几样东西在画面中部排成一行、等距、下方留空，本身不写字；
    - 画面里有卡片、图标、示意图、表单等容易被写上字的东西：逐个说明为空白（同 text_fix 1 级，不含底部字幕那条）。"""
    labels = shot.get("labels") or []
    if labels:
        return (f"The {len(labels)} main items are arranged in one horizontal row across the middle of the frame, "
                "evenly spaced from left to right, each one a plain blank shape or simple pictogram with no writing on it, "
                "with clear empty space directly below each item.")
    f = text_fix(shot, [], 1)
    if not (f["objs"] or f["diagram"]):
        return ""
    return fix_text({**f, "bottom": False}, "")[0]


# H3 常把旁白当字幕画在画面底部（验收判伪字的最大一类）：从第一次生成起就禁止底部字幕、旁白只出声不出字
BOTTOM_BAN = ("The lower fifth of the frame is plain background only: no caption strip, no subtitle line, "
              "no words under the picture.")


def audio_only_line(narration):
    return f"Audio only, never shown as text: an off-screen narrator says \"{narration}\""


def fix_text(fix, narration):
    """把 text_fix 的结果写成提示词句子；返回 (加在画面描述后的句子, 旁白那一句的写法)。"""
    if not fix:
        return "", None
    parts = []
    if fix["objs"]:
        parts.append(f"Every {', '.join(fix['objs'])} in this scene is completely blank: a plain colored surface with at "
                     "most one simple pictogram, never any writing, labels or numbers.")
    if fix.get("diagram"):
        parts.append("Every element of the diagram is a simple pictogram icon in a colored circle, with no label, "
                     "caption or word next to it; arrows and lines are plain.")
    if fix["level"] >= 2:
        parts.append("Keep the picture very simple: a few large flat shapes and figures on a plain pastel background with "
                     "lots of empty space, no small details, no small objects.")
    line = None
    if fix["bottom"]:
        parts.append(BOTTOM_BAN)
        line = audio_only_line(narration)
    return " ".join(parts), line


# 国内规范的标志样式：画面描述里出现对应内容时补到提示词里，否则 H3 常按国外习惯画（黄菱形象形图、八角停止牌、绿色氧气瓶等）

GAS_COLORS = [("oxygen", "light blue"), ("hydrogen", "light green"), ("nitrogen", "black"), ("acetylene", "white"),
              ("argon", "silver gray"), ("carbon dioxide", "aluminum white"), ("compressed air", "black")]


def sign_style(scene):
    """按画面内容补充国内规范的标志和气瓶颜色要求。
    标识用 tools/sign_catalog.py 的国家标准式样（GB 2894-2025、GB 13495.1-2015、GB 30000）；旧的 SIGN_STYLES 不再使用
    （它把普通图标 pictogram 也当成化学品危险象形图，会诱导画出危险品菱形）。"""
    s = scene.lower()
    from sign_catalog import sign_prompt  # noqa: E402
    parts = [sign_prompt(scene)] if sign_prompt(scene) else []
    if re.search(r"\bcylinders?\b", s):
        named = [f"{gas} cylinders are {color}" for gas, color in GAS_COLORS if gas in s]
        parts.append("Gas cylinders use the Chinese GB/T 7144 color code: " + ("; ".join(named) + "; " if named else "")
                     + "a cylinder whose gas is not named is plain gray; never paint an oxygen cylinder green.")
    return " ".join(parts)


def local_prompt(shot, tts=False):
    """一镜的完整 H3 提示词。tts=True：画外音镜头由 TTS 另配，提示词里不写中文旁白（ppplus107 2026-10-28 起的做法）。"""
    scene = shot["prompt_en"]
    narration = spoken(shot["narration"])
    extra, fixed_line = fix_text(shot.get("fix"), narration)
    guard = "" if shot.get("fix") else text_guard(shot)   # 已经调整过提示词的镜头，约束已在 extra 里
    if not shot.get("fix") and shot["mode"] != "speaker":
        guard = f"{guard} {BOTTOM_BAN}".strip()
        fixed_line = audio_only_line(narration)   # 画外音镜头：旁白只出声，不画成底部字幕
    exit_scene = bool(EXIT_WORDS.search(scene))
    door = DOOR_GUARD_EXIT if exit_scene else (DOOR_GUARD if DOOR_WORDS.search(scene) else "")
    tail = LOCAL_TAIL.replace(TAIL_DOOR, f"{TAIL_DOOR}, except that an emergency exit door has {EXIT_SIGN}") \
        if exit_scene else LOCAL_TAIL
    scene = f"{scene} {sign_style(scene)} {guard} {door} {extra}".strip()
    people = " ".join(desc for role, desc in LOCAL_CHARACTERS.items() if role in scene)
    if tts and shot["mode"] != "speaker":   # 配音由 TTS 合进来：提示词里不出现中文旁白
        return " ".join(p for p in (LOCAL_STYLE + scene, people, TTS_LINE, TTS_AUDIO) if p) + tail
    if shot["mode"] == "speaker":
        line = ("Medium close-up of the panda mascot, facing the camera with its whole face clearly visible and nothing "
                "in front of its mouth (props are held low, below the chin). The panda speaks the line with clearly "
                f"visible, well-synchronized mouth movements: \"{narration}\" Its mouth moves only while "
                "speaking and closes when the line ends; nobody else talks.")
    elif fixed_line:
        line = (f"{fixed_line} Nobody in the scene talks: every character keeps a calm closed-mouth expression "
                "with lips together the whole time, no lip movement.")
    else:
        line = (f"Voice-over narration from an off-screen narrator: \"{narration}\" "
                "Nobody in the scene talks: every character keeps a calm closed-mouth expression with lips together "
                "the whole time, no lip movement.")
    return " ".join(p for p in (LOCAL_STYLE + scene, people, line, LOCAL_VOICE) if p) + tail

