# 22_Fundamentals of Handling Compressed Gas Cylinders Safely – Checking your System 原著版卡通剧本作者源
# 完全照原片：供气系统检漏的操作演示（2 分 07 秒），K1–K12（带压检漏、气泡法或电子检漏仪、严禁明火、方法与气体相容、
# 检漏液或温和肥皂水、持续冒泡即漏、肥皂水可能腐蚀接头、检漏仪校准、先泄压再紧固再复查、仍漏尽快通知实验室主管、记录按 SOP）；
# 原片气瓶未见固定，照原片呈现，无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "压缩气瓶安全操作基础：检查系统泄漏",
    "edition": "原著版",
    "points": {
        "K1": "用气之前，带压检漏",
        "K2": "气泡法或电子检漏仪",
        "K3": "严禁明火检漏",
        "K4": "方法要和气体相容",
        "K5": "检漏液装进洗瓶",
        "K6": "挤在每个接头上",
        "K7": "持续冒泡就是漏",
        "K8": "肥皂水会腐蚀接头",
        "K9": "检漏仪要校准",
        "K10": "先泄压，再紧固，再复查",
        "K11": "还漏就报告",
        "K12": "定期检查，做好记录",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services", "SNOOP", "PerkinElmer"],
}

SHOTS = [
# 开场
("开场", "欣欣手拿一只洗瓶，站在气瓶旁",
 "The panda mascot holds a plastic wash bottle and stands beside an upright gas cylinder fitted with a regulator, waving at the camera.",
 "这一课讲供气系统怎样检漏。", "供气系统检漏"),
("开场", "洗瓶、气泡、扳手、记录本四个图标",
 "Four icons in a row: a wash bottle, soap bubbles, a wrench and a blank logbook. No people.",
 "涂液、看泡、紧固、记录。", "", ["涂液", "看泡", "紧固", "记录"]),
# 情景
("情景", "阿杰闻到异味，凑近接头，手里拿着打火机",
 "The young male student sniffs the air near a gas line connection and pulls a lighter out of his pocket.",
 "阿杰觉得接头漏气，掏出打火机想试试。"),
("情景", "打火机靠近接头的图标被打叉",
 "An icon of a lighter flame held near a gas fitting, crossed out with a red X. No people.",
 "用火找漏气，可能直接引燃。"),
("情景", "小研一把按住阿杰的手，递给他一只洗瓶",
 "The female graduate student quickly stops the young male student's hand and gives him a wash bottle instead.",
 "小研拦下他：检漏，用检漏液。"),
# K1
("K1", "小研站在气瓶旁，两只压力表都有读数",
 "The female graduate student, wearing a lab coat, safety goggles and gloves, stands by the cylinder; both regulator gauges show readings on blank dials.",
 "用气之前，先在带压状态下检漏。", "用气之前，带压检漏"),
# K2
("K2", "洗瓶和手持电子检漏仪并排",
 "A wash bottle and a handheld electronic leak detector with a blank screen side by side. No people.",
 "可以用气泡法，也可以用电子检漏仪。", "气泡法或电子检漏仪", ["气泡法", "电子检漏仪"]),
# K3
("K3", "禁止烟火标志",
 "A no open flames prohibition sign. No people.",
 "无论什么情况，严禁用明火检漏。", "严禁明火检漏"),
# K4
("K4", "小研翻阅空白的操作规程夹",
 "The female graduate student reads a blank standard operating procedure binder beside the cylinder.",
 "先查规程，方法要和这种气体相容。", "方法要和气体相容"),
("K4", "气瓶图标和检漏液瓶之间一个相容的对勾",
 "A gas cylinder icon and a leak test solution bottle linked by a green check mark. No people.",
 "检漏方法和步骤，按实验室规程定。"),
# K5
("K5", "洗瓶里装着肥皂水，贴着空白标签",
 "A plastic wash bottle filled with soapy water, with a blank label. No people.",
 "检漏液或温和的肥皂水，装进洗瓶。", "检漏液装进洗瓶"),
# K6
("K6", "小研用洗瓶在瓶阀接口挤上检漏液",
 "The female graduate student squeezes leak test solution from the wash bottle onto the joint between the cylinder valve and the regulator.",
 "挤在瓶阀和减压器的连接处。", "挤在每个接头上"),
("K6", "出口接头下垫着纸巾，液体挂在接头上",
 "Leak test solution coats the regulator outlet fitting, with a paper towel placed underneath. No people.",
 "出口阀的接头，也要涂到。"),
# K7
("K7", "接头处不断冒出小气泡",
 "Small soap bubbles keep growing and popping at a metal fitting. No people.",
 "气泡不断冒出来，就说明漏气。", "持续冒泡就是漏"),
("K7", "一个接头没有气泡打勾，另一个冒泡打叉",
 "Two fittings side by side: one with no bubbles and a green check, one with bubbles and a red X. No people.",
 "不冒泡，这个接头才算合格。"),
# K8
("K8", "金属接头上出现锈斑图标",
 "A metal fitting with small rust spot icons where soap residue was left. No people.",
 "肥皂水可能腐蚀金属接头。", "肥皂水会腐蚀接头"),
# K9
("K9", "电子检漏仪旁的扳手和对勾日历图标",
 "A handheld electronic leak detector next to a calibration icon and a calendar with a check mark. No people.",
 "电子检漏仪，要定期维护和校准。", "检漏仪要校准"),
("K9", "小研对照空白说明书使用检漏仪",
 "The female graduate student reads a blank instrument manual, then holds the leak detector probe near a fitting.",
 "用前读懂说明书，按说明使用。"),
# K10
("K10", "带压用扳手拧接头的图标被打叉",
 "An icon of a wrench tightening a fitting while the gauge shows pressure, crossed out with a red X. No people.",
 "发现漏气，不要带压去拧。", "先泄压，再紧固，再复查"),
("K10", "小研关上瓶阀，两只表指针回零",
 "The female graduate student closes the cylinder valve; both gauge needles fall back to zero.",
 "先关瓶阀，把系统压力泄掉。"),
("K10", "小研用扳手紧固接头",
 "The female graduate student tightens the leaking fitting with an open-end wrench.",
 "再用扳手紧固接头。"),
("K10", "重新加压后再挤检漏液，没有气泡",
 "After repressurizing, solution is applied again to the fitting and no bubbles appear, with a green check. No people.",
 "重新加压，再检一遍。"),
# K11
("K11", "接头仍在冒泡，小研给老周打电话",
 "Bubbles still appear at the fitting; the female graduate student calls the older man on her phone.",
 "还在漏，尽快通知实验室主管。", "还漏就报告"),
# K12
("K12", "墙上的空白检查日历，几个日期打勾",
 "A blank inspection calendar on the wall with several dates checked. No people.",
 "定好检查周期，定期检漏。", "定期检查，做好记录"),
("K12", "小研在空白检漏记录本上登记",
 "The female graduate student writes in a blank leak test logbook next to the cylinder.",
 "每次检漏都登记，按规程保存。"),
# 小结
("小结", "欣欣身旁浮现洗瓶和禁止烟火标志",
 "The panda mascot stands beside floating icons of a wash bottle and a no open flames sign.",
 "带压检漏，用检漏液，严禁明火。", "小结"),
("小结", "泄压、扳手、复查三个打勾图标",
 "Three icons with green checks: gauges at zero, a wrench and bubble-free fitting. No people.",
 "漏了先泄压，再紧固，再复查。"),
("小结", "电话、记录本两个图标",
 "Icons of a telephone and a blank logbook. No people.",
 "还漏就报告，定期查，记清楚。"),
# 结尾
("结尾", "欣欣在整齐的气瓶旁挥手道别",
 "The panda mascot waves goodbye at the camera beside a gas cylinder with a leak-free regulator.",
 "接头不漏气，用气才安心，下次见！"),
]
