# 11_5P's of biosafety biosafety microbiology raqbamicrohub laboratory 卡通剧本作者源
# 原片基本无配音，逐条列出生物安全 5P：Pathogen 病原、Personnel 人员、Place 场所、PPE 个人防护、Procedures 规程，
# 说明五者相互作用、共同决定风险与控制。保留全部知识点 K1–K7，
# 审查补充 S1–S3（第六个 P：安全文化；规程要含应急；按短板优先改进）。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "生物安全的五个 P",
    "points": {
        "K1": "5P：风险评估的五个要素",
        "K2": "P1 病原：先搞清对手",
        "K3": "P2 人员：能力、培训与健康",
        "K4": "P3 场所：设施与级别",
        "K5": "P4 个人防护装备",
        "K6": "P5 操作规程",
        "K7": "五个 P 一起看，定风险",
        "S1": "第六个 P：安全文化，人人尽责",
        "S2": "规程里要写清应急步骤",
        "S3": "哪个 P 薄弱，先补哪个",
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
("K1", "五个并排的空白槽位，标 P1 到 P5",
 "Five blank slots in a row. No people.",
 "病原、人员、场所、防护、规程。", "生物安全的 5 个 P", ["P1", "P2", "P3", "P4", "P5"]),
# K2
("K2", "一个微生物图标配一只放大镜",
 "A microbe icon with a magnifying glass. No people.",
 "P1 病原：先搞清对手是谁。", "P1 病原"),
("K2", "一本空白目录和高低不等的危害条块",
 "A blank catalogue book next to hazard bars of different heights. No people.",
 "查目录定危害，国内第一类最危险。"),
# K3
("K3", "几个人形图标旁边有体检和培训图标",
 "Several figure icons beside a health-check icon and a training icon. No people shown in detail.",
 "P2 人员：谁来做，能力和健康。", "P2 人员"),
("K3", "一张合格的准入胸牌图标",
 "An approved access-badge icon. No people.",
 "先培训、合格，才能上岗。"),
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
 "按评估结果选防护用品。"),
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
# S1
("S1", "在五个 P 后面加上第六个：一群人和一颗心",
 "A sixth slot added after the five, holding a group-of-people icon and a heart. No people shown in detail.",
 "再加一个 P：安全文化。", "第六个 P：文化"),
("S1", "每个人头顶都有一个尽责的对勾",
 "Each figure icon with a responsibility check mark above it. No people shown in detail.",
 "人人尽责，安全才稳。"),
# S2
("S2", "操作规程文件里多出一节应急步骤",
 "A procedure document with an extra emergency-steps section highlighted. No people.",
 "规程里要写清应急步骤。", "别忘了应急"),
("S2", "溢洒、针刺、暴露三个图标配一个上报箭头",
 "Three icons—a spill, a needlestick, and an exposure—next to a reporting arrow. No people shown in detail.",
 "溢洒、针刺、暴露，怎么处置。"),
("S2", "一条逐级上报的箭头链",
 "A chain of upward reporting arrows. No people.",
 "先处置，再逐级上报。"),
# S3
("S3", "五根高度不一的柱子，最矮的被圈出",
 "Five bars of different heights, the shortest one circled. No people.",
 "哪个 P 薄弱，先补哪个。", "补齐短板"),
("S3", "最矮的柱子被补高，风险指针下降",
 "The shortest bar raised up while a risk pointer drops. No people.",
 "短板补上，风险才真降。"),
# 小结
("小结", "欣欣身旁排开五个 P 的图标",
 "The panda mascot stands beside five lined-up icons. No text on them.",
 "五个 P：病原、人员、场所、防护、规程。"),
("小结", "欣欣竖起一根手指提醒",
 "The panda mascot raises one finger as a reminder.",
 "评估到位，再动手。"),
# 结尾
("结尾", "欣欣在实验室门口向镜头挥手告别",
 "The panda mascot waves goodbye at the lab door.",
 "记牢五个 P，安全不踩坑。"),
]
