# 11_5P's of biosafety biosafety microbiology raqbamicrohub laboratory 原著版卡通剧本作者源
# 完全照原片：K1–K7（5P：病原、人员、场所、个人防护、规程；五者相互作用，共同决定风险与控制措施），无补充知识点；
# 不加国内病原分类方向、安全文化、应急与短板内容
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "生物安全的五个 P",
    "edition": "原著版",
    "points": {
        "K1": "5P：风险评估的五个要素",
        "K2": "P1 病原：先搞清对手",
        "K3": "P2 人员：能力、培训与健康",
        "K4": "P3 场所：设施与级别",
        "K5": "P4 个人防护装备",
        "K6": "P5 操作规程",
        "K7": "五个 P 一起看，定风险",
    },
    "avoid": ["raqbamicrohub", "Ragba Micro Hub", "Ragba", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在微生物实验室里，向镜头招手",
 "The panda mascot stands in a microbiology lab and waves at the camera.",
 "这一课讲生物安全的五个 P。", "生物安全的五个 P"),
("开场", "欣欣伸出五根手指，身旁浮现五个空白图标",
 "The panda mascot holds up five fingers, with five blank icons floating beside it.",
 "五个 P，是风险评估的要点。"),
# 情景
("情景", "阿杰拿着一张新实验任务单，有点发愁",
 "The young male student holds a blank task sheet, looking worried.",
 "阿杰接到一个新实验。"),
("情景", "小研走过来，欣欣也出现",
 "The female graduate student walks over; the panda mascot appears too.",
 "小研说：先按五个 P 评一评。"),
# K1
("K1", "放大镜照着一张空白风险评估表",
 "A magnifying glass over a blank risk assessment form. No people.",
 "做风险评估，要看五个核心要素。", "生物安全的 5 个 P"),
("K1", "五个并排的空白槽位，标 P1 到 P5",
 "Five blank slots in a row. No people.",
 "病原、人员、场所、防护、规程。", "", ["P1", "P2", "P3", "P4", "P5"]),
("K1", "五个槽位依次亮起",
 "The five slots light up one after another. No people.",
 "它们的英文都以 P 开头。"),
# K2
("K2", "一个微生物图标配一只放大镜",
 "A microbe icon with a magnifying glass. No people.",
 "P1 病原：先搞清对手是谁。", "P1 病原"),
("K2", "高低不等的危害条块",
 "Hazard bars of different heights next to a microbe icon. No people.",
 "用的是什么病原，危害有多大。"),
# K3
("K3", "几个人形图标旁边有体检和培训图标",
 "Several figure icons beside a health-check icon and a training icon. No people shown in detail.",
 "P2 人员：谁来做，能力和健康。", "P2 人员"),
("K3", "一张合格的准入胸牌图标",
 "An approved access-badge icon. No people.",
 "能力够不够，培训到不到位。"),
("K3", "体检图标上打绿勾",
 "A health-check icon with a green check mark. No people.",
 "身体状况，也要考虑进去。"),
# K4
("K4", "一栋实验楼配一个级别标牌",
 "A lab building icon next to a level sign. No people.",
 "P3 场所：实验室够不够级别。", "P3 场所"),
("K4", "门口一块生物安全级别标牌",
 "A biosafety-level door sign at a lab entrance. No people.",
 "级别要配得上病原危害。"),
# K5
("K5", "手套、白大褂、口罩、护目镜四个图标",
 "Four icons: gloves, lab coat, mask, goggles. No people.",
 "P4 个人防护：穿戴对装备。", "P4 个人防护"),
("K5", "小研穿戴好全套防护",
 "The female graduate student wears a full set of PPE.",
 "按需要选用防护用品，"),
("K5", "小研对着镜子检查手套和口罩是否戴好",
 "The female graduate student checks in a mirror that her gloves and mask are worn correctly.",
 "并且正确穿戴。"),
# K6
("K6", "一份空白操作规程文件图标",
 "A blank standard-operating-procedure document icon. No people.",
 "P5 操作规程：按步骤来做。", "P5 操作规程"),
("K6", "一张带勾选框的步骤清单",
 "A checklist with step boxes. No people.",
 "规程写清楚，照着做。"),
# K7
("K7", "五个齿轮相互咬合转动",
 "Five gears meshing together. No people.",
 "五个 P 相互影响。", "五个 P 一起看"),
("K7", "一架天平把五个因素合起来称",
 "A balance scale weighing five combined factors. No people.",
 "一起看，才定得准风险。"),
("K7", "欣欣指向一排控制措施图标",
 "The panda mascot points at a row of control-measure icons.",
 "再定该用哪些控制措施。"),
# 小结
("小结", "欣欣身旁排开五个 P 的图标",
 "The panda mascot stands beside five lined-up icons. No text on them.",
 "五个 P：病原、人员、场所、防护、规程。"),
("小结", "欣欣竖起一根手指提醒",
 "The panda mascot raises one finger as a reminder.",
 "五者一起，决定风险和控制措施。"),
# 结尾
("结尾", "欣欣在实验室门口向镜头挥手告别",
 "The panda mascot waves goodbye at the lab door.",
 "记牢五个 P，下次见！"),
]
