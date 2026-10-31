# 03_Protect Your Team with Lab Equipment Safety and Maintenance Training 原著版卡通剧本作者源
# 完全照原片：K1–K10（读厂家说明书、由有资质技术人员定期检修、密封件损坏/焦糊味/通风柜失灵三种情况停工报告、
# 电气隐患、定期彻底检查、爱护设备），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "仪器设备的安全与维护",
    "edition": "原著版",
    "points": {
        "K1": "放好、擦净、固定、维护好",
        "K2": "重视校准，更要重视安全",
        "K3": "新设备先读说明书",
        "K4": "定期维护，有资质的技术人员检修",
        "K5": "密封件坏了：停工报告",
        "K6": "闻到焦糊味：停工报告",
        "K7": "通风柜失灵：确保安全后停工报告",
        "K8": "用电设备的电气隐患",
        "K9": "定期、例行、彻底检查",
        "K10": "爱护设备，设备护你",
    },
    "avoid": ["Atlantic", "Atlantic Training", "Samsung"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台大型分析仪旁",
 "The panda mascot stands beside a large benchtop analyzer with a blank screen and waves at the camera.",
 "这一课讲仪器设备的安全与维护。", "仪器设备的安全与维护"),
("开场", "说明书、扳手、放大镜、暂停手势四个图标",
 "Four icons in a row: a blank manual, a wrench, a magnifying glass and a raised stop hand. No people.",
 "读说明、勤维护、常检查、有异常就停。", "", ["读说明", "勤维护", "常检查", "异常就停"]),
# 情景
("情景", "阿杰在仪器前皱眉闻了闻，仪器后面冒出一缕细烟",
 "The young male student sniffs the air with a frown beside an instrument; a thin wisp of grey smoke rises from behind it.",
 "阿杰闻到仪器后面有点焦味。"),
("情景", "阿杰耸耸肩，继续按按钮",
 "The young male student shrugs and keeps pressing buttons on the instrument panel.",
 "他想：先把这批样品测完再说。"),
("情景", "小研快步过来，抬手示意停下",
 "The female graduate student hurries over and raises her hand in a stop gesture.",
 "小研喊停：有焦味，马上停下报告！"),
# K1
("K1", "仪器端正放在稳固台面上",
 "An instrument sits squarely and firmly on a sturdy bench in the right spot. No people.",
 "设备要放得对、放得稳。", "放好、擦净、固定、维护好"),
("K1", "小研用布擦净仪器表面",
 "The female graduate student wipes the surface of an instrument clean with a cloth.",
 "擦干净、维护好，对安全关系重大。"),
# K2
("K2", "校准砝码和天平打勾的图标",
 "An icon of a balance with a calibration weight and a green check. No people.",
 "大家都在乎校准，好让结果稳定可靠。", "重视校准，更要重视安全"),
("K2", "欣欣指着自己的护目镜，眉头一挑",
 "The panda mascot points at its safety goggles and raises an eyebrow.",
 "可说到安全，你真的同样细心吗？"),
# K3
("K3", "小研翻开一本空白说明书，站在新仪器旁",
 "The female graduate student opens a blank instrument manual beside a new instrument still in its packaging.",
 "用新设备前，你读过厂家说明书吗？", "新设备先读说明书"),
("K3", "说明书页面上警示三角和参数表图标",
 "A blank manual page showing a yellow warning triangle icon and an empty specification table. No people.",
 "技术规格和注意事项，先看清楚。"),
# K4
("K4", "老李打开仪器侧板做保养",
 "The facility engineer opens a side panel of an instrument for routine servicing with a toolbox beside him.",
 "设备有没有定期维护？", "定期维护，有资质的技术人员检修"),
("K4", "老李胸前别着资质徽章，在保养记录上签字",
 "The facility engineer with a certification badge on his chest signs a blank service record.",
 "检修是不是由有资质的技术人员来做？"),
# K5
("K5", "仪器门上的密封圈出现裂口的示意图",
 "Close icon of an instrument door seal ring with a visible crack, a yellow warning triangle beside it. No people.",
 "看到密封圈、垫片损坏了？", "密封件坏了：停工报告"),
("K5", "停止手势和电话图标",
 "A raised stop hand icon followed by an arrow to a telephone icon. No people.",
 "立即停止工作，马上报告。", "", ["停工", "报告"]),
# K6
("K6", "仪器背后冒出细烟，鼻子图标",
 "A thin wisp of smoke rises behind an instrument, with a nose icon and a yellow warning triangle. No people.",
 "闻到焦糊味了？", "闻到焦糊味：停工报告"),
("K6", "停止手势和电话图标",
 "A raised stop hand icon followed by an arrow to a telephone icon. No people.",
 "同样立即停工，马上报告。"),
# K7
("K7", "通风柜上的风量报警灯亮红色",
 "A fume hood with its airflow alarm light glowing red and its sash half open. No people.",
 "通风柜不工作了？", "通风柜失灵：确保安全后停工报告"),
("K7", "小研停下手里的操作，走开去打电话",
 "The female graduate student stops her work at the fume hood, steps away and makes a phone call.",
 "在确保安全的前提下，立即停工报告。"),
# K8
("K8", "大型分析仪和电线插头，电气警示标志",
 "A large analyzer with its power cord and plug, a yellow electrical warning sign beside it. No people.",
 "大型分析仪这类设备，有潜在电气危险。", "用电设备的电气隐患"),
("K8", "液体渗漏、冷凝水滴、电线破皮三个图标",
 "Three icons: a liquid leak under an instrument, water condensation drops on a pipe, and a power cord with frayed insulation. No people.",
 "漏液、冷凝水、电线磨损，数都数不完。", "", ["漏液", "冷凝水", "电线磨损"]),
# K9
("K9", "小研拿着空白检查表巡查仪器",
 "The female graduate student walks past a row of instruments holding a blank checklist and a pen.",
 "所有设备都要定期、例行检查，", "定期、例行、彻底检查"),
("K9", "检查表上一项项打勾",
 "A blank checklist getting green check marks one by one beside icons of a cord, a seal and a fan. No people.",
 "而且要查得彻底。"),
# K10
("K10", "精密仪器旁的金币图标和小齿轮图标",
 "A delicate instrument with a coin stack icon and a small gear icon floating beside it. No people.",
 "仪器昂贵精密，也容易出故障。", "爱护设备，设备护你"),
("K10", "小研和阿杰在运转正常的仪器旁并肩工作",
 "The female graduate student and the young male student work side by side, wearing goggles, at a smoothly running instrument.",
 "更要紧的是自己和同事的健康。"),
("K10", "欣欣轻拍仪器，竖起大拇指",
 "The panda mascot pats a clean instrument and gives a thumbs up.",
 "爱护设备，设备也会保护你。"),
# 小结
("小结", "欣欣身旁浮现说明书和扳手图标",
 "The panda mascot stands beside floating icons of a blank manual and a wrench.",
 "先读说明书，定期维护、专业检修。", "小结"),
("小结", "密封圈、鼻子、通风柜三个图标和停止手势",
 "Three icons, a cracked seal, a nose and a fume hood, next to a raised stop hand. No people.",
 "密封坏、有焦味、通风停，停工报告。"),
("小结", "插头和检查表两个图标",
 "Two icons: a power plug with a warning triangle and a blank checklist. No people.",
 "留意电气隐患，设备经常彻底检查。"),
# 结尾
("结尾", "欣欣在整洁的仪器旁挥手道别",
 "The panda mascot waves goodbye at the camera beside a clean, tidy instrument.",
 "照顾好设备，也照顾好自己，下次见！"),
]
