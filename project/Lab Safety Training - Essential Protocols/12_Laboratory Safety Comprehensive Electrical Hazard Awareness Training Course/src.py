# 12_Laboratory Safety Comprehensive Electrical Hazard Awareness Training Course 卡通剧本作者源
# 原片为电气危害意识课程开头（危害、培训要求、标准体系）：保留全部知识点 K1–K9，审查补充 S1–S4
# （用前查电线插头、离开断电、触电先断电再施救、触电后呼救与就医）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "电气危害：认得清，躲得开",
    "points": {
        "K1": "电伤害，伤得重",
        "K2": "每年都有人因电丧命",
        "K3": "培训防五种电气伤害",
        "K4": "识别危害，避开危害",
        "K5": "标准管到设备全过程",
        "K6": "做法有国家标准可依",
        "K7": "专业人员和普通人员分工",
        "K8": "设计安装维护有规范",
        "K9": "重点防电弧和电击",
        "S1": "用前查电线插头",
        "S2": "人走断电",
        "S3": "有人触电：先断电再施救",
        "S4": "触电之后：呼救、就医",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "NFPA", "IEEE", "National Electrical Code", "NEC",
              "Bureau of Labor Statistics", "CFR"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台旁，台上有几台仪器和插线板",
 "The panda mascot stands beside a lab bench with several instruments and a power strip, waving at the camera.",
 "这一课讲：认清电气危害。", "电气危害：认得清，躲得开"),
# 情景
("情景", "阿杰拿起一台仪器，电线外皮有裂口，他没注意",
 "The young male student picks up a small instrument whose power cord has a cracked insulation spot he does not notice.",
 "阿杰要插电，没看见电线外皮破了。"),
("情景", "小研一把按住他的手，指着破口",
 "The female graduate student stops his hand before he plugs in and points at the damaged cord.",
 "小研赶紧拦住：电，可不能大意。"),
# K1
("K1", "触电图标和受伤的人形图标",
 "An electric shock warning sign next to an injured person icon with a bandage. No people.",
 "电伤害往往很重，致残致死的都不少。", "电伤害，伤得重"),
# K2
("K2", "日历翻页，每页都有一个闪电警示",
 "Calendar pages flipping, each page marked with a small lightning warning symbol. No people.",
 "每年都有人因为触电丢了性命。", "每年都有人因电丧命"),
# K3
("K3", "王老师在培训教室讲课，屏幕空白",
 "The safety administrator teaches a training class in front of a blank screen; the young male student listens.",
 "单位要组织用电安全培训。", "培训防五种电气伤害"),
("K3", "触电、电击、电弧、爆炸、火灾五个图标",
 "Five icons in a row: a lightning bolt with a person, a shock symbol, an arc flash, an explosion and a flame. No people.",
 "防触电、电击、电弧、爆炸和火灾。", "", ["触电", "电击", "电弧", "爆炸", "火灾"]),
# K4
("K4", "放大镜照着电线和插座",
 "A magnifying glass icon over a power cord and a wall outlet. No people.",
 "培训的目的：会识别电气危害，", "识别危害，避开危害"),
("K4", "人形图标绕开闪电区域走",
 "A person icon walking around a zone marked with a lightning bolt, with a green check. No people.",
 "还要会主动避开它。"),
# K5
("K5", "检查、安装、操作、维护四个图标连成一圈",
 "Four icons connected in a circle: a magnifying glass, a wrench, a power button and an oil can. No people.",
 "从检查、安装，到使用、维护，都有标准。", "标准管到设备全过程", ["检查", "安装", "使用", "维护"]),
# K6
("K6", "一摞空白标准文本",
 "A stack of blank standard booklets with a national emblem-free seal. No people.",
 "国家有电气安全标准，", "做法有国家标准可依"),
("K6", "标准文本旁出现勾选清单",
 "A blank checklist with green checks appearing beside the booklets. No people.",
 "规定了该怎么做、按什么程序做。", "", ["以现行标准为准"]),
# K7
("K7", "持证电工和普通实验人员两个人形，各有不同工具",
 "Two person icons: an electrician with a tool bag and a certificate, and a lab worker with a pipette. No people.",
 "专业电工和普通人员，要求不一样。", "专业人员和普通人员分工"),
("K7", "老李打开配电箱，小研在旁边只负责报修",
 "The facility engineer opens an electrical panel while the female graduate student stands back holding a phone.",
 "电工修线路，我们只管正确使用和报修。"),
# K8
("K8", "图纸、安装、扳手三个图标",
 "Icons of a blueprint, an installation tool and a wrench. No people.",
 "电气系统的设计、安装和维护，", "设计安装维护有规范"),
("K8", "规范文本盖在图纸上，打勾",
 "A blank standard booklet placed on a blueprint with a green check. No people.",
 "都要按规范来，不能凭感觉。"),
# K9
("K9", "电弧闪光图标",
 "An arc flash icon bursting from a switch box. No people.",
 "电气安全的重点：一防电弧，", "重点防电弧和电击"),
("K9", "电流穿过人体的示意图被打叉",
 "A diagram of current passing through a person's body from hand to foot, crossed out. No people.",
 "二防电击。"),
# S1
("S1", "小研检查电线、插头，发现破皮和焦痕",
 "The female graduate student inspects a power cord and plug and finds cracked insulation and a scorch mark.",
 "用电前，看电线、看插头。", "用前查电线插头"),
("S1", "破皮、发热、焦味三个图标",
 "Three icons: a cracked cord, a hot plug with heat lines, and a smoke wisp. No people.",
 "破皮、发烫、有焦味，立即停用。", "", ["破皮", "发烫", "焦味"]),
("S1", "仪器挂上空白停用牌，阿杰打电话报修",
 "An instrument with a blank out-of-service tag; the young male student calls for repair on the phone.",
 "挂牌停用，找人维修，不自己缠胶布。"),
# S2
("S2", "下班时小研关掉仪器开关、拔下插头",
 "At the end of the day the female graduate student switches off instruments and unplugs them.",
 "离开实验室，关掉不用的电器。", "人走断电"),
("S2", "需要过夜运行的仪器旁挂着空白登记卡",
 "An instrument left running overnight with a blank registration card hanging on it. No people.",
 "要长时间运行的，按规定登记、有人巡查。"),
# S3
("S3", "有人触电倒地的图标，旁边一只手伸过去被打叉",
 "An icon of a person collapsed next to an appliance, with a bare hand reaching toward them crossed out. No people.",
 "看到有人触电，千万别直接用手拉！", "有人触电：先断电再施救"),
("S3", "小研冲向配电箱拉下开关",
 "The female graduate student rushes to the electrical panel and switches off the breaker.",
 "第一步，马上切断电源。"),
("S3", "干燥木棍挑开电线的图标",
 "An icon of a dry wooden stick pushing a power cord away from a person icon. No people.",
 "断不了电，用干燥木棍等绝缘物挑开。"),
# S4
("S4", "电话图标旁有120",
 "A telephone icon with a red cross icon beside it. No people.",
 "立即拨打120。", "触电之后：呼救、就医", ["120"]),
("S4", "受过培训的王老师跪地施救，旁边有自动体外除颤器",
 "The safety administrator, trained in first aid, kneels to help a collapsed person, with an automated external defibrillator box nearby.",
 "受过培训的人进行心肺复苏。"),
("S4", "医院图标，旁边是报告链图标：实验室—学院—保卫处",
 "A hospital icon, next to a chain of icons connected by arrows: a lab, a college building and a security badge. No people.",
 "看着没事也要就医，并报告负责人。", "", ["实验室", "学院", "保卫处"]),
# 小结
("小结", "欣欣身旁浮现五种电气伤害图标",
 "The panda mascot stands beside floating icons of a shock symbol, an arc flash, an explosion and a flame.",
 "电伤害很重，要会识别、会避开。", "小结"),
("小结", "插头检查、关电源两个打勾图标",
 "Two icons with green checks: a plug under a magnifying glass, and a power switch turned off. No people.",
 "用前查电线，人走就断电。"),
("小结", "断电开关、木棍、120电话图标",
 "Icons of a breaker switched off, a dry wooden stick and a telephone with a red cross. No people.",
 "有人触电先断电，再呼救施救。"),
# 结尾
("结尾", "欣欣举起一个插头竖起大拇指，挥手道别",
 "The panda mascot holds up a healthy plug, gives a thumbs-up and waves goodbye.",
 "认得清，躲得开，下次见！"),
]
