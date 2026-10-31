# 11_Laboratory Safety Training Handling Hazardous Materials with Confidence 卡通剧本作者源
# 原片为危险物料课程预览（一般安全责任、安全技术说明书、工艺危害分析）：保留全部知识点 K1–K9，
# 审查补充 S1–S4（最小用量按需领用、混合前查相容性、病原微生物按级别经批准、高危实验不独做）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "危险物料：心中有数再动手",
    "points": {
        "K1": "危险物料，实验室里躲不开",
        "K2": "单位的责任：消除已知危害",
        "K3": "三类重点：易爆、化学、病原",
        "K4": "安全技术说明书随货提供",
        "K5": "说明书里有什么",
        "K6": "说明书是第一依据",
        "K7": "危险化学品先做危害分析",
        "K8": "懂行的人一起分析",
        "K9": "分析看哪几方面",
        "S1": "最小用量，按需领用",
        "S2": "混合之前查相容性",
        "S3": "病原微生物：按级别、经批准",
        "S4": "高危实验不独自做",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "OSH Act", "General Duty Clause", "PHA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在试剂柜前，向镜头招手",
 "The panda mascot stands in front of a closed chemical cabinet with hazard pictograms and waves at the camera.",
 "这一课讲：危险物料，心中有数再动手。", "危险物料：心中有数再动手"),
# 情景
("情景", "阿杰从柜里拿出一瓶新试剂，准备直接倒",
 "The young male student takes a new blank-labeled bottle from a cabinet and is about to pour it straight away.",
 "阿杰拿到一瓶没用过的试剂，就想直接用。"),
("情景", "小研递给他一份空白说明书，指了指",
 "The female graduate student hands him a blank safety data sheet and taps on it.",
 "小研说：先弄清它有什么危险。"),
# K1
("K1", "试剂柜、气瓶、生物安全柜图标并排",
 "Icons of a chemical cabinet, a gas cylinder and a biological safety cabinet side by side. No people.",
 "实验室里，难免会碰到危险物料。", "危险物料，实验室里躲不开"),
# K2
("K2", "学校、学院、实验室三层图标，顶上一面盾牌",
 "Three stacked building icons of decreasing size under a large shield icon. No people.",
 "学校和实验室有责任消除已知危害。", "单位的责任：消除已知危害"),
("K2", "整洁的实验室，通道畅通、台面干净",
 "A tidy lab with clear aisles, clean benches and closed cabinets. No people.",
 "让实验室远离危害，保持整洁有序。"),
# K3
("K3", "爆炸、化学瓶、病原微生物三个图标",
 "Three icons in a row: an exploding bomb pictogram, a chemical bottle and a biohazard symbol with a microbe. No people.",
 "重点三类：易爆物、化学品、病原微生物。", "三类重点：易爆、化学、病原", ["易爆物", "化学品", "病原微生物"]),
# K4
("K4", "试剂箱打开，里面附着一份空白说明书",
 "An opened chemical delivery box with a bottle and a blank safety data sheet inside. No people.",
 "化学品到货，要附安全技术说明书。", "安全技术说明书随货提供"),
("K4", "王老师把说明书放进实验室文件夹",
 "The safety administrator files a blank safety data sheet into a lab binder on a shelf.",
 "实验室收好，人人都能查到。"),
# K5
("K5", "说明书图标展开，浮现名称、厂家、成分图标",
 "A blank document icon unfolding with small icons: a name tag, a factory and a molecule. No people.",
 "里面有名称、生产商和危险成分。", "说明书里有什么", ["名称", "生产商", "危险成分"]),
("K5", "火焰、爆炸、反应箭头、人体健康图标",
 "Icons of a flame, an explosion, a reaction arrow and a human body with a warning mark. No people.",
 "理化特性，火灾爆炸、反应性和健康危害。", "", ["理化特性", "燃爆", "反应性", "健康危害"]),
("K5", "手套、通风柜、盾牌图标",
 "Icons of a glove, a fume hood and a shield. No people.",
 "还有安全操作注意事项和控制措施。", "", ["安全操作", "控制措施"]),
# K6
("K6", "阿杰认真读说明书，头顶亮起灯泡",
 "The young male student reads a blank safety data sheet carefully with a light bulb glowing above his head.",
 "说明书是用好危险物料的第一依据。", "说明书是第一依据"),
("K6", "说明书上的爆炸图标亮起，旁边出现一本新规程",
 "An exploding bomb pictogram lights up on a blank sheet, and a second blank rule book appears beside it. No people.",
 "一看有爆炸危险，就要按更严的规程来。"),
# K7
("K7", "两个试剂瓶图标碰在一起，中间有警示闪光",
 "Two blank bottle icons touching with a warning flash between them. No people.",
 "危险化学品，特别是会剧烈反应的，", "危险化学品先做危害分析"),
("K7", "老周在白板前写下空白分析表",
 "The older man draws a blank analysis table on a whiteboard.",
 "用之前先做危害分析。"),
# K8
("K8", "老周、王老师、小研围坐讨论",
 "The older man, the safety administrator and the female graduate student sit around a table discussing.",
 "请懂行的人一起分析。", "懂行的人一起分析"),
("K8", "火焰图标连向原因和后果两个问号",
 "A flame icon connected by arrows to two question marks labeled with blank cards. No people.",
 "可能怎么着火爆炸？后果有多严重？", "", ["原因", "后果"]),
# K9
("K9", "分子、天平、楼房三个图标",
 "Three icons: a molecule, a balance scale with a ruler, and a building. No people.",
 "看物质性质、用量和距离、房间条件。", "分析看哪几方面", ["物质性质", "用量与距离", "房间条件"]),
("K9", "人形图标和一叠旧事故报告图标",
 "A person icon with a gear, next to a stack of blank old incident reports. No people.",
 "还要看人的因素，查以往事故教训。", "", ["人的因素", "事故教训"]),
# S1
("S1", "大瓶试剂打叉，小瓶试剂打勾",
 "A huge bottle icon crossed out next to a small bottle icon with a green check. No people.",
 "危险物料用多少领多少，不多存。", "最小用量，按需领用"),
("S1", "小研在空白领用登记本上签字",
 "The female graduate student signs a blank chemical withdrawal logbook at a storeroom window.",
 "领用登记，用剩的按规定退回或处置。"),
# S2
("S2", "两瓶试剂之间放着空白相容性表",
 "Two blank bottles with a blank compatibility chart between them. No people.",
 "两种物料混合前，先查是否相容。", "混合之前查相容性"),
("S2", "两个不相容的瓶子被隔开，废液桶上贴空白标签",
 "Two incompatible bottles separated by a divider, and a waste container with a blank label. No people.",
 "倒废液也一样，不相容的不能倒一起。"),
# S3
("S3", "生物危害标志和空白目录本",
 "A biohazard sign beside a blank catalog book and a lab door with a level icon. No people.",
 "病原微生物，按国家目录定实验室级别。", "病原微生物：按级别、经批准"),
("S3", "王老师在空白审批表上盖章",
 "The safety administrator stamps a blank approval form at a desk.",
 "经过风险评估和批准，才能开始。"),
# S4
("S4", "夜里只有阿杰一人的实验室，被打叉",
 "A lab at night with only the young male student working alone, crossed out with a red X.",
 "高危实验，不一个人做。", "高危实验不独自做"),
("S4", "小研和阿杰一起做实验，互相照应",
 "The female graduate student and the young male student work together at a fume hood, watching out for each other.",
 "有人在场，出事有人照应、有人报警。"),
# 小结
("小结", "欣欣身旁浮现说明书、分析表、小瓶图标",
 "The panda mascot stands beside floating icons of a safety data sheet, an analysis table and a small bottle.",
 "先看说明书，再做危害分析。", "小结"),
("小结", "相容性表、审批章、两人小组图标",
 "Icons of a compatibility chart, an approval stamp and two people working together. No people.",
 "少量领用，查相容，经批准，不独做。"),
# 结尾
("结尾", "欣欣抱着一份说明书挥手道别",
 "The panda mascot holds a blank safety data sheet and waves goodbye at the camera.",
 "心中有数，动手才稳，下次见！"),
]
