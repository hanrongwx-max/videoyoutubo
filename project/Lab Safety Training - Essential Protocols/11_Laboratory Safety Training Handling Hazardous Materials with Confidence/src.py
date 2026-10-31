# 11_Laboratory Safety Training Handling Hazardous Materials with Confidence 原著版卡通剧本作者源
# 完全照原片：K1–K9（美国职业安全卫生管理局实验室安全指南中的雇主一般责任；生产商提供 SDS 及原片所列项目；
# 工艺危害分析小组；爆炸物与烟火的分析主题只讲名称，不涉及任何具体数值），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室安全培训：从容处理危险物料",
    "edition": "原著版",
    "points": {
        "K1": "危险物料，实验室里躲不开",
        "K2": "雇主的一般安全责任",
        "K3": "三类重点：易爆、化学、病原",
        "K4": "生产商提供安全技术说明书",
        "K5": "说明书里有什么",
        "K6": "说明书是首要依据",
        "K7": "危险化学品做工艺危害分析",
        "K8": "懂行的人组成分析小组",
        "K9": "分析看哪几方面",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "OSH Act", "General Duty Clause", "PHA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在试剂柜前，向镜头招手",
 "The panda mascot stands in front of a closed chemical cabinet with hazard pictograms and waves at the camera.",
 "这一课讲：危险物料，心中有数再动手。", "危险物料：心中有数再动手"),
("开场", "说明书和分析表两个图标",
 "Two icons: a blank safety data sheet and a blank analysis table. No people.",
 "看说明书，做危害分析。", "", ["说明书", "危害分析"]),
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
 "说实话，最危险的物料，难免在实验室碰上。", "危险物料，实验室里躲不开"),
# K2
("K2", "欣欣举着一本空白指南",
 "The panda mascot holds up a blank guidance booklet.",
 "美国的实验室安全指南，规定了雇主的责任。", "雇主的一般安全责任"),
("K2", "工作场所图标上方，死亡和重伤图标被打叉",
 "A workplace icon with a skull icon and an injury icon above it, both crossed out. No people.",
 "工作场所不能有会致死、致重伤的公认危害。"),
("K2", "整洁的实验室，通道畅通、台面干净",
 "A tidy lab with clear aisles, clean benches and closed cabinets. No people.",
 "也就是让工作场所远离已知危害，保持整洁。"),
# K3
("K3", "爆炸、化学瓶、病原微生物三个图标",
 "Three icons in a row: an exploding bomb pictogram, a chemical bottle and a biohazard symbol with a microbe. No people.",
 "这里关注三类：爆炸性物料、化学品、病原体。", "三类重点：易爆、化学、病原", ["爆炸性物料", "化学品", "危险病原体"]),
# K4
("K4", "工厂图标送出试剂箱，里面附着一份空白说明书",
 "A factory icon sending an opened delivery box with a bottle and a blank safety data sheet inside. No people.",
 "生产商必须向实验室提供安全技术说明书。", "生产商提供安全技术说明书"),
("K4", "王老师把说明书放进实验室文件夹",
 "The safety administrator files a blank safety data sheet into a lab binder on a shelf.",
 "里面有安全维护实验室需要知道的一切。"),
# K5
("K5", "说明书图标展开，浮现名称、厂家、成分图标",
 "A blank document icon unfolding with small icons: a name tag, a factory and a molecule. No people.",
 "化学品名称、生产商、危险成分和识别信息。", "说明书里有什么", ["名称", "生产商", "危险成分"]),
("K5", "火焰、爆炸、反应箭头、人体健康图标",
 "Icons of a flame, an explosion, a reaction arrow and a human body with a warning mark. No people.",
 "理化特性，火灾爆炸、反应性和健康危害。", "", ["理化特性", "火灾爆炸", "反应性", "健康危害"]),
("K5", "手套、通风柜、盾牌图标",
 "Icons of a glove, a fume hood and a shield. No people.",
 "还有安全操作使用注意事项和控制措施。", "", ["安全操作", "控制措施"]),
# K6
("K6", "阿杰认真读说明书，头顶亮起灯泡",
 "The young male student reads a blank safety data sheet carefully with a light bulb glowing above his head.",
 "说明书是实验室物料安全的首要依据。", "说明书是首要依据"),
("K6", "说明书上的爆炸图标亮起，旁边出现一本新规程",
 "An exploding bomb pictogram lights up on a blank sheet, and a second blank rule book appears beside it. No people.",
 "比如知道它有爆炸危险，就要启用新规则。"),
# K7
("K7", "两个试剂瓶图标碰在一起，中间有警示闪光",
 "Two blank bottle icons touching with a warning flash between them. No people.",
 "美国职业安全卫生管理局建议，", "危险化学品做工艺危害分析"),
("K7", "老周在白板前写下空白分析表",
 "The older man draws a blank analysis table on a whiteboard.",
 "对危险化学品做工艺危害分析。", "", ["工艺危害分析"]),
("K7", "一个瓶子碰到另一个瓶子发出警示闪光",
 "A bottle icon meeting another bottle icon with a big warning flash, circled for attention. No people.",
 "包括会和其他化学品爆炸性反应的。"),
# K8
("K8", "老周、王老师、小研围坐讨论",
 "The older man, the safety administrator and the female graduate student sit around a table discussing.",
 "请熟悉爆炸性物料的人组成分析小组，", "懂行的人组成分析小组"),
("K8", "火焰图标连向原因和后果两个问号",
 "A flame icon connected by arrows to two question marks on blank cards. No people.",
 "评估火灾爆炸的可能原因和后果。", "", ["原因", "后果"]),
# K9
("K9", "分子和天平尺子两个图标",
 "Two icons: a molecule, and a balance scale with a ruler. No people.",
 "分析包括物质固有的理化性质，", "分析看哪几方面", ["理化性质", "数量与距离"]),
("K9", "楼房图标",
 "A building cross-section icon. No people.",
 "数量与距离要求、建筑设计，", "", ["建筑设计"]),
("K9", "人形图标和一叠旧事故报告图标",
 "A person icon with a gear, next to a stack of blank old incident reports. No people.",
 "还有人为因素和以往的事故报告。", "", ["人为因素", "事故报告"]),
# 小结
("小结", "欣欣身旁浮现说明书和分析表图标",
 "The panda mascot stands beside floating icons of a safety data sheet and an analysis table.",
 "雇主消除已知危害，说明书是首要依据。", "小结"),
("小结", "分析小组和五个主题图标",
 "Icons of a small team around a table and five small topic cards. No people.",
 "危险化学品，懂行的人一起做危害分析。"),
# 结尾
("结尾", "欣欣抱着一份说明书挥手道别",
 "The panda mascot holds a blank safety data sheet and waves goodbye at the camera.",
 "心中有数，动手才稳，下次见！"),
]
