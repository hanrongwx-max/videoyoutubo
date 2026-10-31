# 20_Fundamentals of Handling Compressed Gas Cylinders Safely – Attaching the Regulat 原著版卡通剧本作者源
# 完全照原片：安装气瓶减压器的操作演示（2 分 06 秒），K1–K11（取瓶帽后凭气味、气雾和嘶嘶声确认瓶阀关闭、
# 查螺纹、出口阀顺时针关、调压阀逆时针松、手拧、可燃逆时针不可燃顺时针、防火花扳手、不用钳子、氧气禁油、密封带先问厂家）；
# 原片气瓶直立台边、画面未见固定，照原片呈现，无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "给气瓶装上减压器",
    "edition": "原著版",
    "points": {
        "K1": "用前先检查",
        "K2": "取下瓶帽，确认瓶阀关闭",
        "K3": "检查减压器螺纹",
        "K4": "先关出口流量阀",
        "K5": "调压阀松到底",
        "K6": "用手拧到手紧",
        "K7": "拧不进，别硬拧",
        "K8": "可燃气体接口反向拧",
        "K9": "用扳手拧牢",
        "K10": "不用钳子，氧气禁油",
        "K11": "密封带先问厂家",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services", "Teflon", "INCREASE"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台边的一只气瓶旁，手里拿着减压器",
 "The panda mascot stands beside a gas cylinder standing upright next to a lab bench, holding a pressure regulator with two round gauges, and waves at the camera.",
 "这一课讲怎样给气瓶装上减压器。", "给气瓶装上减压器"),
("开场", "放大镜、关闭的阀门、手、扳手四个图标排成一行",
 "Four icons in a row: a magnifying glass, a closed valve, a hand, and a wrench. No people.",
 "先检查，再归零，手拧上，扳手紧。", "", ["检查", "归零", "手拧", "拧牢"]),
# 情景
("情景", "阿杰拿着一只减压器，伸手去拿老虎钳",
 "The young male student holds a pressure regulator in one hand and reaches for a pair of pliers on the bench with the other.",
 "阿杰拿起一只减压器，又抓起钳子。"),
("情景", "钳子夹螺母的图标被红叉划掉",
 "An icon of pliers gripping a hex nut, crossed out with a red X. No people.",
 "想把它硬拧到气瓶上。"),
("情景", "小研拦住阿杰，指向气瓶标签",
 "The female graduate student stops the young male student and points at the blank label on the gas cylinder.",
 "小研拦住他：别急，先检查。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "装减压器，一步都不能省。"),
# K1
("K1", "小研拿着减压器，站在气瓶旁",
 "The female graduate student, wearing a lab coat, safety goggles and gloves, stands beside the cylinder holding a regulator.",
 "上手之前，减压器和气瓶都要检查。", "用前先检查"),
# K2
("K2", "小研双手拧下瓶帽",
 "The female graduate student unscrews the protective cap from the top of the cylinder with both hands.",
 "先取下瓶帽，露出瓶阀。", "取下瓶帽，确认瓶阀关闭"),
("K2", "瓶阀旁的鼻子、眼睛、耳朵图标",
 "A close-up of a closed cylinder valve with a nose icon, an eye icon and an ear icon beside it. No people.",
 "有没有气味、气雾、嘶嘶声？", "", ["闻气味", "看气雾", "听声音"]),
("K2", "瓶阀图标打绿勾",
 "A closed cylinder valve icon with a green check. No people.",
 "都没有，说明瓶阀是关着的。"),
# K3
("K3", "放大镜下的减压器进气接头螺纹",
 "A magnifying glass over the threaded inlet fitting of a pressure regulator. No people.",
 "检查减压器接头的螺纹。", "检查减压器螺纹"),
("K3", "螺纹上的损伤、油污、灰尘三个图标",
 "Three small icons beside the threads: a damaged thread, an oil drop and dust specks. No people.",
 "有损伤、油污、灰尘，都不能装。", "", ["损伤", "油污", "灰尘"]),
# K4
("K4", "手顺时针转动减压器出口小阀，旁边顺时针箭头",
 "A gloved hand turns the small outlet valve of the regulator, with a clockwise arrow beside it. No people.",
 "先把出口流量阀顺时针关上。", "先关出口流量阀"),
# K5
("K5", "手逆时针转动调压手轮，旁边逆时针箭头",
 "A gloved hand turns the large adjusting knob of the regulator, with a counterclockwise arrow beside it. No people.",
 "再把调压手轮逆时针松到底。", "调压阀松到底"),
("K5", "两个关闭状态的阀门图标都打勾",
 "Two valve icons both shown in the closed position, each with a green check. No people.",
 "这样开瓶时，气不会一下子冲出来。"),
# K6
("K6", "小研把减压器对准瓶阀出气口，用手旋入",
 "The female graduate student lines the regulator inlet up with the cylinder valve outlet and screws it in by hand.",
 "对准接口，先用手拧到手紧。", "用手拧到手紧"),
# K7
("K7", "接口歪斜卡住，旁边是停止手势图标",
 "An icon of a regulator fitting jammed at an angle on the valve outlet, with a stop hand icon. No people.",
 "拧不进，就停手，别硬拧。", "拧不进，别硬拧"),
("K7", "减压器和气瓶之间出现问号",
 "A regulator icon and a cylinder icon with a large question mark between them. No people.",
 "配合不好，可能这只表不适合这种气。"),
# K8
("K8", "两个接口图标，一个逆时针箭头配火焰，一个顺时针箭头",
 "Two fitting icons side by side: one with a counterclockwise arrow and a flame pictogram, one with a clockwise arrow. No people.",
 "可燃气体接口，逆时针拧紧。", "可燃气体接口反向拧", ["可燃：逆时针", "不可燃：顺时针"]),
("K8", "小研对着空白规程核对旋向",
 "The female graduate student compares the fitting with a blank procedure card before turning it.",
 "不可燃气体，顺时针拧紧，先认准再拧。"),
# K9
("K9", "小研用开口扳手卡住接头螺母拧紧",
 "The female graduate student tightens the hex nut of the connection firmly with an open-end wrench.",
 "最后用开口扳手或固定扳手拧牢。", "用扳手拧牢"),
("K9", "火焰标志旁一把防火花扳手",
 "A flame pictogram next to a non-sparking wrench with a spark icon crossed out. No people.",
 "可燃气体，要用防火花的扳手。"),
# K10
("K10", "钳子被红叉划掉",
 "A pair of pliers crossed out with a red X. No people.",
 "不得使用钳子。", "不用钳子，氧气禁油"),
("K10", "氧气瓶接头旁，油滴和油手套图标被打叉",
 "An oxygen cylinder fitting next to an oil drop icon and a greasy glove icon, both crossed out with a red X. No people.",
 "氧气减压器，螺纹上绝不能沾油脂。"),
# K11
("K11", "一卷白色密封带，旁边是问号和电话图标",
 "A roll of white thread sealing tape with a question mark and a telephone icon beside it. No people.",
 "想缠密封带，先问厂家或供应商。", "密封带先问厂家"),
# 小结
("小结", "欣欣身旁浮现瓶帽、瓶阀、放大镜图标",
 "The panda mascot stands beside floating icons of a cylinder cap, a closed valve and a magnifying glass.",
 "取下瓶帽，确认阀关，查好螺纹。", "小结"),
("小结", "两个阀门归零、手拧、扳手三个打勾图标",
 "Three icons with green checks: two closed valves, a hand turning a fitting and a wrench. No people.",
 "两阀关好，手拧到位，扳手拧牢。"),
("小结", "钳子、油滴两个图标被打叉，密封带旁一个问号",
 "Pliers and an oil drop crossed out with red X marks, and a roll of sealing tape with a question mark. No people.",
 "不用钳子，氧气禁油，密封带先问。"),
# 结尾
("结尾", "欣欣在装好减压器的气瓶旁挥手道别",
 "The panda mascot waves goodbye at the camera beside a gas cylinder with a regulator fitted.",
 "装好减压器，安全用气，下次见！"),
]
