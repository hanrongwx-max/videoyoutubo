# 03_Power Tools Safety in hindi Power Tools Hazards & Precautions in hindi 卡通剧本作者源（原著版）
# 完全照原片：电动工具危害与预防清单，知识点 K1–K20，不加补充知识点、不做本土化
# （保留原片的 110 V 供电配 30 mA ELCB、松手即停开关、笼统的皮手套要求、焊接棚与看火人，场景为工地）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "电动工具的危害与预防措施",
    "edition": "原著版",
    "points": {
        "K1": "什么是电动工具",
        "K2": "危害：触电",
        "K3": "危害：火灾和爆炸",
        "K4": "危害：火花",
        "K5": "危害：割伤",
        "K6": "危害：烧伤",
        "K7": "危害：噪声",
        "K8": "危害：振动",
        "K9": "电源要有漏电保护",
        "K10": "松手即停的开关",
        "K11": "防护罩不能拆",
        "K12": "清走可燃易燃物",
        "K13": "砂轮片转速要够",
        "K14": "火花要挡住",
        "K15": "焊接设隔离区",
        "K16": "灭火器材和看火人",
        "K17": "护目镜加面罩",
        "K18": "皮手套和围裙",
        "K19": "耳塞或耳罩",
        "K20": "长时间作业要轮换",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "Samsung", "SAMSUNG"],
}

SHOTS = [
# 开场
("开场", "欣欣站在白板前，白板旁画着电钻和角磨机，向镜头招手",
 "The panda mascot stands in front of a whiteboard with drawings of an electric drill and an angle grinder, waving at the camera.",
 "这一课讲电动工具。", "电动工具的危害与预防措施"),
("开场", "警示三角和盾牌两个图标",
 "Two icons in a row: a yellow warning triangle and a shield with a check mark. No people.",
 "它有哪些危害，又该怎么预防。", "", ["危害", "预防"]),
# 情景
("情景", "工地上，老李把一台角磨机交给阿杰",
 "At a construction site, the facility engineer hands an angle grinder to the young male student.",
 "阿杰今天要在工地上打磨钢件。"),
("情景", "阿杰看着角磨机，头顶冒出问号",
 "The young male student looks at the angle grinder in his hands with a question mark bubble above him.",
 "他问：用这个，要注意什么？"),
("情景", "欣欣在白板前竖起手指",
 "The panda mascot stands in front of the whiteboard and raises one finger.",
 "先认识它，再列危害和预防。"),
# K1
("K1", "手锯和电锯并排，电锯旁有插头",
 "A hand saw and an electric saw side by side, the electric saw with a power cord and plug. No people.",
 "不靠人力、靠别的动力驱动的，", "什么是电动工具"),
("K1", "角磨机、钻床、木工切割机、电焊机四个图标",
 "Four icons in a row: an angle grinder, a drill press, a wood cutting saw and a welding machine. No people.",
 "就是电动工具，比如这几种。", "", ["砂轮机", "钻床", "木工切割机", "电焊机"]),
# K2
("K2", "电钻电源线冒出小闪电",
 "An icon of an electric drill with its cord sparking, with an electric shock warning sign. No people.",
 "工具接着电源，首要危害是触电。", "危害：触电"),
# K3
("K3", "火焰和爆炸图标",
 "A flame icon and an explosion burst icon side by side. No people.",
 "第二，火灾和爆炸。", "危害：火灾和爆炸"),
# K4
("K4", "砂轮边缘飞出一串火花",
 "Bright sparks flying from the edge of a grinding wheel icon. No people.",
 "第三，火花。", "危害：火花"),
# K5
("K5", "锯片和一只手形图标，旁边警示三角",
 "An icon of a saw blade near a hand pictogram with a yellow warning triangle. No people.",
 "第四，割伤，机会可不小。", "危害：割伤"),
# K6
("K6", "火花落在手臂图标上留下红点",
 "An icon of sparks landing on an arm pictogram leaving small red burn marks. No people.",
 "第五，打磨火花落身上会烧伤。", "危害：烧伤"),
# K7
("K7", "耳朵图标旁边很大的声波",
 "An ear icon with large loud sound waves coming at it. No people.",
 "第六，噪声大，影响听力。", "危害：噪声"),
# K8
("K8", "握着工具的双手图标，旁边有抖动线",
 "An icon of two hands gripping a vibrating power tool with shaking lines around them. No people.",
 "第七，振动。", "危害：振动"),
("K8", "七个危害图标逐个打勾",
 "Seven small hazard icons in two columns, each getting a check mark one by one: shock, flame, sparks, blade, burn, ear, vibration. No people.",
 "七种危害，再过一遍。", "", ["触电", "火灾爆炸", "火花", "割伤", "烧伤"]),
# K9
("K9", "工具插在带漏电保护器的插座箱上",
 "A power tool plugged into a site socket box equipped with a residual current breaker with a test button. No people.",
 "预防一：用110伏降压供电，", "电源要有漏电保护", ["110V"]),
("K9", "插座箱上的漏电保护器特写",
 "A close view of the residual current breaker on the site socket box. No people.",
 "并配30毫安的ELCB。", "", ["30mA ELCB"]),
# K10
("K10", "手松开开关，工具停转",
 "An icon of a hand releasing the trigger of a drill, and the drill bit stops spinning. No people.",
 "预防二：开关要松手即停。", "松手即停的开关"),
# K11
("K11", "角磨机带着完好的护罩，打绿勾",
 "An angle grinder with its wheel guard properly in place, green check mark. No people.",
 "预防三：机器要有防护罩。", "防护罩不能拆"),
# K12
("K12", "阿杰把纸箱和油桶搬离作业区",
 "The young male student moves cardboard boxes and a closed oil drum away from the work area.",
 "预防四：作业区没有可燃易燃物。", "清走可燃易燃物"),
# K13
("K13", "砂轮片和机器各有空白标签，中间大于号",
 "Icons of a grinding disc with a blank rating label and a grinder with a blank rating label, with a greater-than symbol between them. No people.",
 "预防五：砂轮片额定转速，", "砂轮片转速要够", ["片转速 > 机器转速"]),
("K13", "砂轮片高速旋转，打绿勾",
 "A grinding disc spinning at speed on a grinder, green check mark. No people.",
 "必须高于机器的转速。"),
# K14
("K14", "作业区用挡板全部围起，火花被挡住",
 "A work area completely surrounded by fire resistant screens, sparks stopped inside. No people.",
 "预防六：火花百分之百遮挡，", "火花要挡住", ["100%遮挡"]),
("K14", "挡板外干净，没有火花",
 "Outside the fire resistant screens the area is clean, no sparks escape. No people.",
 "作业区围好，火花飞不出来。"),
# K15
("K15", "带挡帘的焊接棚",
 "A welding booth with flame resistant curtains around it, empty. No people.",
 "预防七：电焊要设焊接棚。", "焊接设隔离区"),
("K15", "焊接棚内闪光被挡帘挡住",
 "Bright welding light inside the booth is blocked by the curtains. No people.",
 "把火花挡在棚里面。"),
# K16
("K16", "灭火器标志下有灭火器和灭火毯",
 "A fire extinguisher sign above a fire extinguisher and a folded fire blanket. No people.",
 "预防八：备好灭火器和灭火毯，", "灭火器材和看火人"),
("K16", "老李站在作业区旁看护，手边有灭火器",
 "The facility engineer stands watch beside a work area with a fire extinguisher at hand.",
 "还要有受过培训的看火人。"),
# K17
("K17", "阿杰戴护目镜，再放下面罩",
 "The young male student puts on safety goggles and then lowers a clear face shield over them.",
 "预防九：护目镜加面罩，双重护眼。", "护目镜加面罩"),
# K18
("K18", "皮手套和围裙图标",
 "Icons of a pair of leather work gloves and a flame resistant apron. No people.",
 "预防十：戴皮手套、穿围裙。", "皮手套和围裙"),
# K19
("K19", "耳塞和耳罩图标",
 "Icons of a pair of foam ear plugs and a pair of ear muffs. No people.",
 "预防十一：戴耳塞或耳罩。", "耳塞或耳罩"),
# K20
("K20", "时钟图标和两个人形图标交替",
 "A clock icon with two person pictograms swapping places with circular arrows. No people.",
 "预防十二：长时间作业要轮岗。", "长时间作业要轮换"),
("K20", "老李拍拍阿杰肩膀，换小研接手",
 "The facility engineer taps the young male student on the shoulder, and the female graduate student takes over.",
 "减少每个人的噪声和振动。"),
# 小结
("小结", "欣欣身旁浮现七个危害图标",
 "The panda mascot stands beside seven floating hazard icons.",
 "七种危害：电、火、火花、割烧、噪振。", "小结"),
("小结", "漏电保护器、松手开关、防护罩三个打勾图标",
 "Three icons with green checks: a residual current breaker, a trigger switch and a wheel guard. No people.",
 "降压漏保、松手即停、护罩装好。"),
("小结", "清场、挡板、焊接棚、灭火器四个图标",
 "Four icons: an empty clean area, a fire resistant screen, a welding booth and a fire extinguisher. No people.",
 "清走易燃物、挡火花、备灭火器。"),
("小结", "护目镜、面罩、手套、耳罩四个图标",
 "Four icons: safety goggles, a face shield, leather gloves and ear muffs. No people.",
 "眼、脸、手、耳防护，再加轮岗。"),
# 结尾
("结尾", "欣欣戴着护目镜挥手道别",
 "The panda mascot wearing safety goggles waves goodbye at the camera in front of the whiteboard.",
 "工具用得对，危害少一半，下次见！"),
]
