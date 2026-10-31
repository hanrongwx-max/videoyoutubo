# 04_Hot Work Safety in hindi Hot Work hazards & precautions in hindi HSE STUDY GUIDE 卡通剧本作者源（原著版）
# 完全照原片：动火作业危害与预防清单，知识点 K1–K25，不加补充知识点、不做本土化
# （保留原片的 PTW 作业许可说法、丙烷丁烷举例、30 mA ELCB 加接地、狭窄区域气体检测，场景为工业现场）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "动火作业的危害与预防措施",
    "edition": "原著版",
    "points": {
        "K1": "什么是动火作业",
        "K2": "动火要先办许可",
        "K3": "危害：火灾和爆炸",
        "K4": "危害：火花",
        "K5": "危害：触电",
        "K6": "危害：有毒烟尘",
        "K7": "危害：烫伤",
        "K8": "危害：强光伤眼",
        "K9": "危害：电弧",
        "K10": "危害：割伤",
        "K11": "危害：噪声和振动",
        "K12": "移走易燃可燃物",
        "K13": "移不走的盖防火毯",
        "K14": "地面清扫干净",
        "K15": "全套焊接防护用品",
        "K16": "漏电保护加接地",
        "K17": "通风不良处先测气体",
        "K18": "焊工和助手都戴面罩",
        "K19": "灭火器材和看火人",
        "K20": "火花封闭，焊接隔间",
        "K21": "砂轮要有护罩",
        "K22": "松手即停开关要好用",
        "K23": "砂轮片转速要够",
        "K24": "噪声大戴耳塞",
        "K25": "双重眼部防护",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSS Study Guide", "Samsung", "SAMSUNG"],
}

SHOTS = [
# 开场
("开场", "欣欣站在白板前，白板旁画着火焰和焊花，向镜头招手",
 "The panda mascot stands in front of a whiteboard with drawings of a flame and welding sparks, waving at the camera.",
 "这一课讲动火作业。", "动火作业的危害与预防措施"),
("开场", "火焰、警示三角、盾牌三个图标",
 "Three icons in a row: a flame, a yellow warning triangle and a shield. No people.",
 "什么是动火，有哪些危害和预防。", "", ["定义", "危害", "预防"]),
# 情景
("情景", "工厂车间里，老李拿着焊接面罩走向一段钢架",
 "In a factory workshop, the facility engineer carries a welding helmet toward a steel frame.",
 "车间里要焊一段钢架。"),
("情景", "阿杰跟在后面，手里拿着角磨机，头顶冒出问号",
 "The young male student follows him holding an angle grinder, with a question mark bubble above him.",
 "阿杰做助手，负责打磨。"),
("情景", "欣欣在白板前竖起手指",
 "The panda mascot stands in front of the whiteboard and raises one finger.",
 "开工之前，先把动火弄明白。"),
# K1
("K1", "喷灯火焰和丙烷、丁烷气瓶图标",
 "Icons of a gas torch flame and two small fuel gas cylinders. No people.",
 "主要用明火的作业，比如丙烷丁烷，", "什么是动火作业", ["丙烷", "丁烷"]),
("K1", "电焊、打磨两个图标，都冒火花",
 "Two icons each throwing sparks: an arc welding torch and an angle grinder. No people.",
 "或者会产生明显火源的，如焊接打磨。", "", ["焊接", "打磨"]),
("K1", "欣欣指着火花图标",
 "The panda mascot points at a sparks icon on the whiteboard.",
 "这些都叫动火作业。"),
# K2
("K2", "空白许可单上盖章打勾",
 "A blank work permit form receiving a stamp and a green check mark. No people.",
 "动火作业，必须先办作业许可PTW。", "动火要先办许可", ["PTW 作业许可"]),
# K3
("K3", "火花落向纸箱燃起火焰，气瓶旁有爆炸图标",
 "Sparks fall onto a cardboard box that catches fire, and a burst icon appears beside a gas cylinder. No people.",
 "危害一：火灾和爆炸。", "危害：火灾和爆炸"),
# K4
("K4", "火花四处飞溅",
 "Sparks flying in all directions across a workshop floor. No people.",
 "危害二：火花。", "危害：火花"),
# K5
("K5", "焊机电缆破皮冒出闪电",
 "An icon of a welding machine with a damaged cable sparking, with an electric shock warning sign. No people.",
 "危害三：焊机砂轮机漏电会触电。", "危害：触电"),
# K6
("K6", "焊点上方升起灰色烟雾，旁边肺部图标",
 "Gray fumes rising from a welding point toward a lung icon with a yellow warning triangle. No people.",
 "危害四：焊接产生有毒烟气。", "危害：有毒烟尘"),
# K7
("K7", "刚焊完发红的工件，伸手去摸的图标",
 "An icon of a freshly welded glowing hot metal piece and a bare hand reaching toward it, with a warning triangle. No people.",
 "危害五：工件很烫，一碰就烫伤。", "危害：烫伤"),
# K8
("K8", "眼睛图标正对强光",
 "An eye icon staring directly at a bright welding light with a warning triangle. No people.",
 "危害六：红外线，裸眼看焊接伤眼。", "危害：强光伤眼"),
# K9
("K9", "焊条与工件之间耀眼的电弧图标",
 "An icon of a bright electric arc between an electrode and a metal plate with a warning triangle. No people.",
 "危害七：电弧。", "危害：电弧"),
# K10
("K10", "没有护罩的砂轮碎裂，碎片飞出",
 "An icon of a grinding wheel without a guard cracking apart with fragments flying, red warning triangle. No people.",
 "危害八：砂轮没护罩，碎了会伤人。", "危害：割伤"),
# K11
("K11", "耳朵和抖动的手两个图标",
 "Two icons: an ear with loud sound waves and two hands with shaking lines. No people.",
 "还有噪声和振动。", "危害：噪声和振动"),
# K12
("K12", "老李和阿杰把纸箱、油桶搬离作业点",
 "The facility engineer and the young male student carry cardboard boxes and a closed oil drum away from the work spot.",
 "预防：把易燃可燃物移出作业区。", "移走易燃可燃物"),
# K13
("K13", "固定的柜子被防火毯盖住",
 "A fixed cabinet covered with a flame resistant fire blanket. No people.",
 "移不走的，用防火毯盖上。", "移不走的盖防火毯"),
# K14
("K14", "阿杰清扫地面，拖干积水",
 "The young male student sweeps the floor and mops up a puddle near the work spot.",
 "地面扫干净，也不能有水。", "地面清扫干净"),
# K15
("K15", "老李穿戴焊接面罩、皮围裙、长袖皮手套",
 "The facility engineer puts on a welding helmet, a leather apron and full length leather gloves.",
 "穿戴防护：长皮手套、围裙、面罩，", "全套焊接防护用品"),
("K15", "皮护腿、袖套、过滤口罩图标",
 "Icons of leather leg guards, leather sleeves and a filter mask. No people.",
 "皮护腿、袖套和过滤口罩。", "", ["面罩", "皮手套", "围裙", "护腿", "袖套"]),
# K16
("K16", "焊机电源接在带漏电保护器的配电箱上，外壳接地",
 "A welding machine connected to a socket box with a residual current breaker, its case linked to a ground symbol. No people.",
 "电源配30毫安ELCB，并且接地。", "漏电保护加接地", ["30mA ELCB"]),
# K17
("K17", "狭窄空间入口旁有空白气体检测仪图标",
 "A narrow congested area between pipes with a blank gas detector icon at its entrance. No people.",
 "狭窄拥挤的区域，先做气体检测。", "通风不良处先测气体"),
# K18
("K18", "老李戴焊接面罩，阿杰在旁也戴面罩递工具",
 "The facility engineer wears a welding helmet while the young male student beside him also wears a welding helmet and hands him a tool.",
 "焊工戴面罩，助手也要戴。", "焊工和助手都戴面罩"),
# K19
("K19", "灭火器标志下有灭火器和灭火毯",
 "A fire extinguisher sign above a fire extinguisher and a folded fire blanket next to the work spot. No people.",
 "备好灭火毯和灭火器，", "灭火器材和看火人"),
("K19", "小研拿着灭火器站在作业点旁看护",
 "The female graduate student stands watch near the work spot holding a fire extinguisher.",
 "再安排一名看火人。"),
# K20
("K20", "作业点四周围上防火挡板",
 "Flame resistant screens set up around the work spot, sparks stopped inside. No people.",
 "火花百分之百封闭，不让飞出。", "火花封闭，焊接隔间", ["100%封闭"]),
("K20", "带挡帘的焊接棚",
 "An empty welding booth with flame resistant curtains in a workshop. No people.",
 "焊接放在焊接棚里做。"),
("K20", "作业区周围空无可燃物，打绿勾",
 "A top view of the work spot surrounded by a clear empty zone, with a green check mark. No people.",
 "再强调：作业区不留可燃易燃物。"),
# K21
("K21", "砂轮机护罩完好，打绿勾",
 "An angle grinder with its wheel guard properly in place, green check mark. No people.",
 "打磨：砂轮机要有护罩。", "砂轮要有护罩"),
# K22
("K22", "手松开开关，砂轮停转",
 "An icon of a hand releasing the switch of a grinder, and the wheel stops. No people.",
 "要有松手即停开关，", "松手即停开关要好用"),
("K22", "阿杰试按开关，打绿勾",
 "The young male student tests the grinder switch before work, and a green check appears.",
 "并确认它工作正常。"),
# K23
("K23", "砂轮片和机器标签比大小",
 "Icons of a grinding disc with a blank rating label and a grinder with a blank rating label, greater-than symbol between them. No people.",
 "砂轮片转速要高于机器转速。", "砂轮片转速要够", ["片转速 > 机器转速"]),
# K24
("K24", "耳塞图标",
 "An icon of a pair of foam ear plugs next to loud sound waves. No people.",
 "噪声大时，戴耳塞。", "噪声大戴耳塞"),
# K25
("K25", "老李护目镜外加焊接面罩",
 "The facility engineer wears safety goggles under his welding helmet.",
 "焊接：护目镜加焊接面罩。", "双重眼部防护", ["焊接：加焊接面罩"]),
("K25", "阿杰护目镜外加面屏打磨",
 "The young male student wears safety goggles under a clear face shield while grinding, with gloves on.",
 "打磨：护目镜加面屏。", "", ["打磨：加面屏"]),
# 小结
("小结", "欣欣身旁浮现火焰和许可单图标",
 "The panda mascot stands beside floating icons of a flame and a blank permit form.",
 "动火作业，先办PTW。", "小结"),
("小结", "火、火花、电、烟、烫、光六个危害图标",
 "Six hazard icons: a flame, sparks, a lightning bolt, fumes, a hot surface and a bright light. No people.",
 "火、火花、电、烟、烫、强光都是危害。"),
("小结", "移走、盖毯、清扫三个打勾图标",
 "Three icons with green checks: boxes moved away, a cabinet under a fire blanket and a swept floor. No people.",
 "移走、盖严、扫净，现场先清理。"),
("小结", "面罩、手套、漏电保护器、气体检测仪图标",
 "Icons of a welding helmet, leather gloves, a residual current breaker and a gas detector. No people.",
 "全套防护，漏保接地，先测气体。"),
("小结", "挡板、灭火器、看火人、护罩图标",
 "Icons of a flame resistant screen, a fire extinguisher, a person pictogram watching and a wheel guard. No people.",
 "封闭火花，备好器材，专人看火。"),
# 结尾
("结尾", "欣欣戴着护目镜挥手道别",
 "The panda mascot wearing safety goggles waves goodbye at the camera in front of the whiteboard.",
 "动火守规矩，平安每一天，下次见！"),
]
