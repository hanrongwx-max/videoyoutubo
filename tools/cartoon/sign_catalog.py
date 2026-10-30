"""国家标准安全标识目录：画面里出现的标识按国家标准的式样生成（用户 2026-10-27：所有标识卡按国家标准制作）。

依据（2026-10-27 查询的现行版本）：
- GB 2894-2025《安全色和安全标志》（2026-03-01 实施，代替 GB 2894-2008、GB 2893-2008、GB 7231-2003）：
  禁止标志 = 白底、红色圆环加红色斜杠、黑色图形；警告标志 = 黄底、黑色正三角形边框、黑色图形；
  指令标志 = 蓝色圆形、白色图形；提示标志 = 绿色正方形、白色图形。新增“洗眼台”“安全淋浴设施”“紧急集合点”
  “必须通风”“当心电弧”“禁止动火作业”等；“紧急出口”改称“安全出口”。图形与 ISO 7010 对应标志一致。
- GB 13495.1-2015《消防安全标志 第1部分：标志》：红色正方形、白色图形（灭火器、手动火灾报警按钮、火警电话、消火栓箱等）；
  疏散类（安全出口、疏散方向）为绿底白图形。
- GB 30000 系列（化学品分类和标签规范，采用 GHS）：白底、红色菱形边框、黑色图形。
- GB 190-2009 危险货物包装标志（运输车辆、货包用菱形标签，不用 GB 2894 三角形）。
- GB 18871-2002 电离辐射标志（三叶形）；GB 19489-2008 生物危害标志；GB/T 7144-2016 气瓶颜色（见 generate_videos.GAS_COLORS）。

每项：键 -> (触发词正则（英文画面描述里出现就套用）, 中文名, 依据, 标准式样的英文描述)。
画面里的标识一律不带文字说明牌（中文名需要出现时用图示文字 labels 在拼接时叠加）。
"""

import re

NO_TEXT = ("Every safety sign is only the standard pictogram sign itself, with no text panel, caption or "
           "letters on or beneath it.")

SIGNS = {
    # 提示标志（绿底白图形，正方形）
    # 洗眼器、冲淋器、急救箱本身是设备：只有明确写了“标志”才套用标志式样，否则会诱导模型在墙上多画标志
    "eyewash": (r"\beye ?wash (station )?signs?\b|\bsigns? (for|of) (the )?eye ?wash", "洗眼台", "GB 2894-2025 提示标志（同 ISO 7010 E011）",
                "The eyewash sign is a green square with a white pictogram of a person's face bending toward an "
                "eyewash bowl with two white water jets rising into the eyes."),
    "shower": (r"\b(safety|emergency|drench) shower signs?\b|\bsigns? (for|of) (the )?(safety |emergency )?shower", "安全淋浴设施", "GB 2894-2025 提示标志（同 ISO 7010 E012）",
               "The safety shower sign is a green square with a white pictogram of a standing person under a shower "
               "head with white water streams falling over the body."),
    "first_aid": (r"\bfirst[- ]aid signs?\b|\bgreen (first[- ]aid )?cross sign|\bsigns? (for|of) first[- ]aid", "急救点", "GB 2894-2025 提示标志（同 ISO 7010 E003）",
                  "The first aid sign is a green square with a plain white equal-armed cross in the centre."),
    "exit": (r"\b(emergency |fire )?exit sign|\bevacuation sign|\bescape route|\bemergency exit|\bsafety exit",
             "安全出口", "GB 2894-2025 / GB 13495.1-2015 提示标志（同 ISO 7010 E001/E002）",
             "The exit sign is a green rectangle with a white running figure moving through a white door frame "
             "and a white arrow pointing the way out."),
    "assembly": (r"\bassembly point|\bmuster point", "紧急集合点", "GB 2894-2025 提示标志（同 ISO 7010 E007）",
                 "The emergency assembly point sign is a green square with four white arrows pointing inward to a "
                 "small group of white human figures in the centre."),
    # 消防安全标志（红底白图形，正方形）
    "extinguisher_sign": (r"\bfire extinguisher sign|\bextinguisher sign", "灭火器", "GB 13495.1-2015 消防设施标志",
                          "The fire extinguisher sign is a red square with a white fire extinguisher pictogram "
                          "(never a red extinguisher on a white background)."),
    "alarm": (r"\b(manual )?(fire )?alarm (button|call point)|\bcall point", "手动火灾报警按钮",
              "GB 13495.1-2015 火灾报警装置标志",
              "The manual fire alarm call point sign is a red square with a white pictogram of a hand pressing a "
              "button on a small box."),
    "fire_phone": (r"\bfire (alarm )?(tele)?phone", "火警电话", "GB 13495.1-2015 火灾报警装置标志",
                   "The fire telephone sign is a red square with a white telephone handset pictogram."),
    # 禁止标志（白底红圈红斜杠黑图形）
    "no_fire": (r"\bno (open )?(flames?|fire|smoking)\b|\bno ignition", "禁止烟火 / 禁止吸烟", "GB 2894-2025 禁止标志",
                "The prohibition sign is a white circle with a thick red ring and a red diagonal bar from upper "
                "left to lower right, crossing a black flame or cigarette pictogram."),
    "no_food": (r"\bno (eating|food|drink)", "禁止饮食", "GB 2894-2025 禁止标志",
                "The prohibition sign is a white circle with a thick red ring and a red diagonal bar crossing a "
                "black cup and fork pictogram."),
    # 警告标志（黄底黑边三角形黑图形）
    "flammable": (r"\bflammable (warning|sign)|\bfire warning sign", "当心火灾", "GB 2894-2025 警告标志",
                  "The warning sign is a yellow equilateral triangle with a thick black border and a black flame "
                  "pictogram."),
    "toxic_warn": (r"\b(toxic|poison) (warning|sign)", "当心中毒", "GB 2894-2025 警告标志",
                   "The warning sign is a yellow equilateral triangle with a thick black border and a black skull "
                   "and crossbones pictogram."),
    "corrosive_warn": (r"\bcorrosi(ve|on) (warning|sign)", "当心腐蚀", "GB 2894-2025 警告标志",
                       "The warning sign is a yellow equilateral triangle with a thick black border and a black "
                       "pictogram of liquid dripping from two test tubes onto a hand and a bar."),
    "electric_warn": (r"\b(electric|electrical|shock|high voltage) (warning|hazard sign|sign)", "当心触电",
                      "GB 2894-2025 警告标志",
                      "The warning sign is a yellow equilateral triangle with a thick black border and a black "
                      "zigzag lightning arrow."),
    "biohazard": (r"\bbiohazard", "当心感染 / 生物危害", "GB 2894-2025 警告标志、GB 19489-2008",
                  "The biohazard sign is a yellow equilateral triangle with a thick black border and the black "
                  "three-crescent biohazard symbol."),
    "radiation": (r"\b(radiation|radioactive|ionizing).{0,20}(sign|symbol|warning|trefoil)|\btrefoil",
                  "当心电离辐射", "GB 2894-2025 警告标志、GB 18871-2002",
                  "The ionizing radiation sign is a yellow equilateral triangle with a thick black border and the "
                  "black three-blade trefoil with a central dot."),
    "laser": (r"\blaser (warning|sign|hazard)", "当心激光", "GB 2894-2025 警告标志",
              "The laser warning sign is a yellow equilateral triangle with a thick black border and a black "
              "starburst with a single beam line."),
    "hot_surface": (r"\bhot surface (warning|sign)", "当心烫伤", "GB 2894-2025 警告标志",
                    "The warning sign is a yellow equilateral triangle with a thick black border and a black "
                    "pictogram of a hot surface with three wavy heat lines."),
    "general_warn": (r"\bwarning triangle|\bgeneral warning|\bwarning signs?\b|\bcaution sign", "注意安全（警告标志）",
                     "GB 2894-2025 警告标志",
                     "A warning sign is a yellow equilateral triangle with a thick black border and a black symbol "
                     "(an exclamation mark when no specific hazard is named)."),
    "general_prohibit": (r"\bprohibition signs?|\bno[- ]entry sign|\bforbidden sign", "禁止标志", "GB 2894-2025 禁止标志",
                         "A prohibition sign is a white circle with a thick red ring and a red diagonal bar from upper "
                         "left to lower right over a black symbol; never an octagonal stop sign."),
    "general_mandatory": (r"\bmandatory signs?|\bblue (round )?sign", "指令标志", "GB 2894-2025 指令标志",
                          "A mandatory sign is a solid blue circle with a white symbol."),
    "magnetic": (r"\bmagnetic[- ]field (warning|sign)|\bstrong magnet(ic)? (warning|sign)", "当心磁场",
                 "GB 2894-2025 警告标志（同 ISO 7010 W006）",
                 "The warning sign is a yellow equilateral triangle with a thick black border and a black horseshoe "
                 "magnet pictogram with field lines."),
    "rf_warn": (r"\b(radio[- ]frequency|microwave|non-ionizing|electromagnetic) (radiation )?(warning|sign)",
                "当心电磁辐射", "GB 2894-2025 警告标志（同 ISO 7010 W005）",
                "The warning sign is a yellow equilateral triangle with a thick black border and a black antenna "
                "pictogram emitting curved waves (never the ionizing trefoil)."),
    # 危险货物包装标志（运输车辆、货包用菱形标签，GB 190-2009；不用工作场所的 GB 2894 三角形）
    "transport": (r"\b(transport|shipping|package|dangerous goods) (labels?|markings?|placards?)|\b(truck|vehicle) placards?|\bplacards?\b",
                  "危险货物包装标志", "GB 190-2009",
                  "Dangerous goods labels on packages and vehicles follow GB 190: a square turned on its point "
                  "(diamond) with the class symbol in the upper half and the class number in the bottom corner; "
                  "never a triangular workplace warning sign on a vehicle or package."),
    # 指令标志（蓝圆白图形）；只在明确写了“标志”时才套用，人物戴护目镜、手套不算
    "goggles": (r"\b(goggles|eye protection) (mandatory )?signs?|\bmandatory sign for (goggles|eye protection)", "必须戴防护眼镜",
                "GB 2894-2025 指令标志",
                "The mandatory sign is a solid blue circle with a white pictogram of a head wearing safety goggles."),
    "gloves": (r"\bgloves? (mandatory )?signs?|\bmandatory sign for (protective )?gloves", "必须戴防护手套", "GB 2894-2025 指令标志",
               "The mandatory sign is a solid blue circle with a white pictogram of a pair of protective gloves."),
    "ventilate": (r"\b(must ventilate|ventilation required|mandatory ventilation)", "必须通风",
                  "GB 2894-2025 指令标志",
                  "The mandatory sign is a solid blue circle with a white pictogram of a ventilation fan with "
                  "airflow lines."),
    # 化学品危险象形图（GHS，GB 30000）
    "ghs": (r"\b(GHS|hazard diamond|hazard pictograms?|hazard labels?|red diamond)", "化学品危险象形图",
            "GB 30000 系列（GHS）",
            "Chemical hazard pictograms follow GB 30000 (GHS): a white square turned on its point with a thick "
            "red diamond border and a black symbol inside (flame, skull, corrosion, exclamation mark, health "
            "hazard silhouette, environment, gas cylinder, exploding bomb or flame over circle)."),
}

_COMPILED = [(k, re.compile(p, re.I)) for k, (p, *_rest) in SIGNS.items()]


WARN_SPECIFIC = {"flammable", "toxic_warn", "corrosive_warn", "electric_warn", "biohazard", "radiation", "laser",
                 "hot_surface", "magnetic", "rf_warn"}


def find_signs(text):
    """画面描述里出现的标识键（按目录顺序，不重复）；写了具体警告标志时不再加通用的“注意安全”。"""
    if re.search(r"\bno (safety )?signs\b|\bwith no signs?\b", text, re.I):   # 画面写明不挂标志
        return []
    keys = [k for k, rx in _COMPILED if rx.search(text)]
    if WARN_SPECIFIC & set(keys) and "general_warn" in keys:
        keys.remove("general_warn")
    if "transport" in keys:   # 运输标签里的辐射、生物危害等符号画在 GB 190 菱形里，不是工作场所的三角形警告标志
        keys = [k for k in keys if k not in WARN_SPECIFIC and k != "general_warn"]
    return keys


def sign_prompt(text):
    """给画面描述补上所涉标识的国家标准式样，以及“标识不带文字说明牌”；没有标识返回空串。"""
    keys = find_signs(text)
    if not keys:
        return ""
    return " ".join(SIGNS[k][3] for k in keys) + " " + NO_TEXT


def sign_names(text):
    """画面里应出现的标识中文名和依据（复检时人工/模型对照用）。"""
    return [(SIGNS[k][1], SIGNS[k][2]) for k in find_signs(text)]
