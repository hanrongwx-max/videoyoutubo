# 12_Laboratory Safety Comprehensive Electrical Hazard Awareness Training Course 原著版卡通剧本作者源
# 完全照原片：K1–K9（美国劳工统计局 2017 年 136 人；美国职业安全卫生管理局的培训要求和电气标准；
# 美国国家电气规范与工作场所电气安全标准；联邦法规 1910.331–335 合格与非合格人员；
# 美国消防协会和电气电子工程师学会标准，重点防电弧和电击），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室安全：电气危害意识综合培训",
    "edition": "原著版",
    "points": {
        "K1": "电伤害，伤得重",
        "K2": "每年都有人因电丧命",
        "K3": "培训防五种电气伤害",
        "K4": "识别危害，避开危害",
        "K5": "标准管到设备全过程",
        "K6": "以国家共识标准为基础",
        "K7": "合格人员和非合格人员",
        "K8": "专业组织的设计安装维护规范",
        "K9": "重点防电弧和电击",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "NFPA", "IEEE", "National Electrical Code", "NEC",
              "Bureau of Labor Statistics", "CFR"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台旁，台上有几台仪器和插线板",
 "The panda mascot stands beside a lab bench with several instruments and a power strip, waving at the camera.",
 "这一课讲：认清电气危害。", "电气危害：认得清，躲得开"),
("开场", "闪电警示、培训、标准文本三个图标",
 "Three icons in a row: a lightning warning sign, a training class and a stack of blank standard booklets. No people.",
 "危害有多重，培训防什么，标准怎么定。", "", ["危害", "培训", "标准"]),
# 情景
("情景", "阿杰拿起一台仪器，随手就要插电",
 "The young male student picks up a small instrument and casually reaches to plug it in.",
 "阿杰觉得，插个电而已，有什么好学的。"),
("情景", "小研摇摇头，指着墙上的闪电警示标志",
 "The female graduate student shakes her head and points at an electrical warning sign on the wall.",
 "小研说：电的事，可一点不简单。"),
# K1
("K1", "触电图标和受伤的人形图标",
 "An electric shock warning sign next to an injured person icon with a bandage. No people.",
 "电伤害是一种复杂的创伤，", "电伤害，伤得重"),
("K1", "多个行业图标上都有闪电警示",
 "Icons of a factory, a lab and a construction site, each with a lightning warning mark. No people.",
 "在很多行业里，致残率和死亡率都很高。"),
# K2
("K2", "日历翻页，每页都有一个闪电警示",
 "Calendar pages flipping, each page marked with a small lightning warning symbol. No people.",
 "据美国劳工统计局数据，", "每年都有人因电丧命"),
("K2", "2017年日历和一个数字牌",
 "A calendar page for one year next to a blank counter board with a lightning icon. No people.",
 "2017年因电导致的工伤死亡有136人。", "", ["2017年", "136人"]),
# K3
("K3", "王老师在培训教室讲课，屏幕空白",
 "The safety administrator teaches a training class in front of a blank screen; the young male student listens.",
 "为此，美国职业安全卫生管理局要求培训，", "培训防五种电气伤害"),
("K3", "触电、电击、电弧、爆炸、火灾五个图标",
 "Five icons in a row: a lightning bolt with a person, a shock symbol, an arc flash, an explosion and a flame. No people.",
 "防触电死亡、电击、电弧、爆炸和火灾。", "", ["触电死亡", "电击", "电弧", "爆炸", "火灾"]),
# K4
("K4", "放大镜照着电线和插座",
 "A magnifying glass icon over a power cord and a wall outlet. No people.",
 "电气安全计划，帮员工识别电气危害，", "识别危害，避开危害"),
("K4", "人形图标绕开闪电区域走",
 "A person icon walking around a zone marked with a lightning bolt, with a green check. No people.",
 "并避开它，降低电气伤害的风险。"),
# K5
("K5", "盾牌图标护住一个拿着工具的人形",
 "A shield icon protecting a person icon holding electrical tools. No people.",
 "监管部门执行电气标准，保护作业人员。", "标准管到设备全过程"),
("K5", "检查、安装、操作、维护四个图标连成一圈",
 "Four icons connected in a circle: a magnifying glass, a wrench, a power button and an oil can. No people.",
 "涵盖设备的检查、安装、操作和维护。", "", ["检查", "安装", "操作", "维护"]),
# K6
("K6", "一摞空白标准文本",
 "A stack of blank standard booklets with a plain seal. No people.",
 "这些规定以国家共识标准为基础，", "以国家共识标准为基础"),
("K6", "两本标准书并排",
 "Two blank standard books side by side, one with a plug icon and one with a worker icon. No people.",
 "比如美国国家电气规范、工作场所电气安全标准。", "", ["国家电气规范", "工作场所电气安全"]),
("K6", "标准文本旁出现勾选清单",
 "A blank checklist with green checks appearing beside the booklets. No people.",
 "它们规定了必要的做法和程序。"),
# K7
("K7", "一本空白法规书翻开到某一节",
 "A blank regulation book opened to a section with a bookmark. No people.",
 "比如美国联邦法规1910.331到335条，", "合格人员和非合格人员", ["1910.331起"]),
("K7", "合格电工和非合格人员两个人形",
 "Two person icons: a qualified electrician with a tool bag and a certificate, and an unqualified worker with a pipette. No people.",
 "对合格和非合格人员，分别规定了做法。", "", ["合格人员", "非合格人员"]),
# K8
("K8", "两个专业学会的空白徽章图标",
 "Two blank professional society emblem icons side by side. No people.",
 "美国消防协会和电气电子工程师学会，", "专业组织的设计安装维护规范"),
("K8", "图纸、安装、扳手三个图标",
 "Icons of a blueprint, an installation tool and a wrench. No people.",
 "为设计、安装、维护提供全面指导。", "", ["设计", "安装", "维护"]),
# K9
("K9", "一本空白标准书发着光",
 "A single blank standard book glowing brightly on a stand. No people.",
 "其中领先的工作场所电气安全标准，", "重点防电弧和电击"),
("K9", "电弧闪光图标",
 "An arc flash icon bursting from a switch box. No people.",
 "重点在预防电弧，"),
("K9", "电流穿过人体的示意图被打叉",
 "A diagram of current passing through a person's body from hand to foot, crossed out. No people.",
 "以及预防电击。后面再细讲。"),
# 小结
("小结", "欣欣身旁浮现闪电和受伤图标",
 "The panda mascot stands beside floating icons of a lightning bolt and an injured person.",
 "电伤害很重，每年都有人因此丧命。", "小结"),
("小结", "培训和标准两个打勾图标",
 "Two icons with green checks: a training class and a stack of standard booklets. No people.",
 "培训会识别、会避开，标准防电弧电击。"),
# 结尾
("结尾", "欣欣举起一个插头竖起大拇指，挥手道别",
 "The panda mascot holds up a healthy plug, gives a thumbs-up and waves goodbye.",
 "认得清，躲得开，下次见！"),
]
