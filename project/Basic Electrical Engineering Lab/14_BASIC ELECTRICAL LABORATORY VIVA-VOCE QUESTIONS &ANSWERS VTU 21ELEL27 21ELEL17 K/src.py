# 14_BASIC ELECTRICAL LABORATORY VIVA-VOCE QUESTIONS &ANSWERS VTU 21ELEL27 21ELEL17 K 卡通剧本作者源
# 原著版：完全照原片（基尔霍夫定律实验的口试问答辅导：18 个常见问题与口试技巧），K1–K21，
# 不加补充知识点、不做本土化和更正（保留“电是电子的运动”、直流应用举电池、电子管、直流电动机、电影放映机，
# 欧姆定律“温度和压力不变”，“动铁式用于交流、磁电式用于直流”的说法）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "KVL与KCL实验口试问答",
    "edition": "原著版",
    "points": {
        "K1": "口试前先回想实验",
        "K2": "什么是电",
        "K3": "电的两类",
        "K4": "电流的两类",
        "K5": "直流和交流的区别",
        "K6": "直流用在哪里",
        "K7": "交流用在哪里",
        "K8": "影响电阻的因素",
        "K9": "认真对待口试",
        "K10": "欧姆定律",
        "K11": "欧姆定律的局限",
        "K12": "基尔霍夫电流定律",
        "K13": "基尔霍夫电压定律",
        "K14": "分流用于并联，分压用于串联",
        "K15": "电压表并联，电流表串联",
        "K16": "RPS是什么",
        "K17": "动铁式和磁电式仪表",
        "K18": "什么是电功率",
        "K19": "答题简短清楚",
        "K20": "直流电路标极性",
        "K21": "认真准备，有疑问就问",
    },
    "avoid": ["VTU", "Simplified EEE", "EEE Studies", "21ELEL17", "21ELEL27"],
}

SHOTS = [
# 开场
("开场", "欣欣坐在考官桌后，桌上放着空白题卡",
 "The panda mascot sits behind an examiner's desk with a stack of blank question cards, waving at the camera.",
 "实验口试来了，一起来练一练！", "电工实验口试：基尔霍夫定律篇"),
# 情景
("情景", "阿杰在走廊里紧张地翻实验报告",
 "The young male student nervously flips through a blank lab report in a corridor outside a lab.",
 "阿杰明天口试，心里直打鼓。"),
("情景", "小研拍拍他的肩，递上一张空白问题清单",
 "The female graduate student pats his shoulder and hands him a blank list of questions.",
 "小研说：常考的题，其实就这些。"),
# K1
("K1", "阿杰闭眼回想实验台和电路",
 "The young male student closes his eyes; a thought bubble shows a lab bench with a power supply, lamps and meters.",
 "进考场前，先回想实验做了什么。", "口试前先回想实验"),
("K1", "实验台上的稳压电源、灯和电表图标",
 "Icons of a regulated power supply, three small lamps and DC meters. No people.",
 "用了哪些器材，电路怎么接。"),
# K2
("K2", "导线里一串小圆点向前移动",
 "Inside a wire, a row of small dots moves forward in one direction. No people.",
 "什么是电？电子的运动。", "什么是电"),
# K3
("K3", "梳子吸纸屑和灯泡通电两个图标",
 "Two icons: a comb attracting bits of paper, and a lit bulb connected to a battery. No people.",
 "电分两类：静电和电流。", "电的两类", ["静电", "电流"]),
# K4
("K4", "直线箭头和波浪箭头两个图标",
 "Two icons: a straight arrow and a wavy arrow. No people.",
 "电流又分直流和交流。", "电流的两类", ["直流", "交流"]),
# K5
("K5", "坐标图上一条水平直线",
 "A simple graph with a flat horizontal line over time. No people.",
 "直流的大小方向不随时间变。", "直流和交流的区别"),
("K5", "坐标图上一条正弦波",
 "A simple graph with a sine wave over time. No people.",
 "交流随时间来回变化。"),
("K5", "阿杰在空白纸上画两条曲线给考官看",
 "The young male student sketches a flat line and a wave on a blank sheet and shows the older man.",
 "口试带上纸笔，画个图更清楚。"),
# K6
("K6", "电池、电子管、直流电动机、放映机四个图标",
 "Four icons: a battery, a vacuum tube, a small DC motor and an old film projector. No people.",
 "电池、电子管、直流电机、放映机用直流。", "直流用在哪里"),
# K7
("K7", "输电塔和墙上插座图标",
 "Icons of a power transmission tower and a wall socket. No people.",
 "电力系统和日常供电用交流。", "交流用在哪里"),
# K8
("K8", "一长一短两根导线，长的电阻符号更大",
 "Two wires of different lengths; the longer one has a larger resistor symbol. No people.",
 "导线越长，电阻越大。", "影响电阻的因素"),
("K8", "一粗一细两根导线，细的电阻符号更大",
 "A thick wire and a thin wire; the thin one has a larger resistor symbol. No people.",
 "截面越大，电阻越小。"),
("K8", "白板上的公式",
 "A whiteboard showing a simple resistance formula with letter symbols. No people.",
 "电阻等于电阻率乘长度除以截面积。", "", ["R=ρL÷A"]),
("K8", "电阻率符号旁边标着单位",
 "A rho symbol next to a unit label. No people.",
 "电阻率的单位是欧姆米。", "", ["ρ：Ω·m"]),
# K9
("K9", "欣欣严肃地竖起手指",
 "The panda mascot raises a finger with a serious face.",
 "口试别轻视，这些要点要记牢。", "认真对待口试"),
# K10
("K10", "电压和电流两条柱同步变高",
 "Two bars, voltage and current, rise together in proportion, with a thermometer and a pressure gauge both showing steady levels. No people.",
 "温度压力不变，电压电流成正比。", "欧姆定律", ["U∝I"]),
# K11
("K11", "绝缘体和半导体芯片图标旁打叉",
 "Icons of an insulator and a semiconductor chip, each with a small red X. No people.",
 "绝缘体、半导体不遵守欧姆定律。", "欧姆定律的局限"),
# K12
("K12", "节点处三个箭头：两进一出",
 "A junction with two arrows flowing in and one arrow flowing out. No people.",
 "节点上，流进的电流等于流出的。", "基尔霍夫电流定律"),
# K13
("K13", "闭合回路上电源和电阻的电压箭头",
 "A closed loop with a source and resistors, voltage arrows going around the loop. No people.",
 "闭合回路里，电压代数和为零。", "基尔霍夫电压定律"),
# K14
("K14", "两个并联电阻，电流分成两路",
 "Two resistors in parallel with current splitting into two arrows. No people.",
 "分流公式，用在并联电路。", "分流用于并联，分压用于串联"),
("K14", "两个串联电阻，电压分成两段",
 "Two resistors in series with the voltage divided into two segments. No people.",
 "分压公式，用在串联电路。"),
# K15
("K15", "电压表跨在灯两端，电流表串在线路里",
 "Circuit icon: a voltmeter connected across a lamp and an ammeter connected in line. No people.",
 "电压表并联，电流表串联。", "电压表并联，电流表串联"),
# K16
("K16", "稳压直流电源图标",
 "An icon of a regulated DC power supply with blank display. No people.",
 "RPS就是稳压直流电源。", "RPS是什么"),
# K17
("K17", "两只电表，一只表盘画波浪号，一只画直线",
 "Two meters, one with a wave symbol on its dial, one with a straight-line symbol. No people.",
 "动铁式仪表用于交流测量。", "动铁式和磁电式仪表", ["动铁式 MI", "磁电式 MC"]),
("K17", "磁电式电表连在电池上",
 "The meter with the straight-line symbol is connected to a battery. No people.",
 "磁电式，也叫动圈式，用于直流。"),
# K18
("K18", "做功图标除以时钟图标",
 "A work icon divided by a clock icon equals a power icon. No people.",
 "电功率，就是单位时间做的功。", "什么是电功率"),
# K19
("K19", "阿杰站直，简短回答，老周点头",
 "The young male student stands straight and answers briefly; the older man nods.",
 "回答要简短清楚，大方自信。", "答题简短清楚"),
("K19", "阿杰想起自己接线的情景",
 "A thought bubble above the young male student shows him wiring a circuit in the lab.",
 "联系自己做过的实验来答。"),
# K20
("K20", "直流电路图上电源和电表都标正负号",
 "A DC circuit diagram with plus and minus signs at the source and the meters. No people.",
 "画直流电路，记得标正负极。", "直流电路标极性"),
("K20", "交流电路图上没有正负号",
 "An AC circuit diagram with a sine wave source symbol and no polarity marks. No people.",
 "交流电路不用标极性。"),
# K21
("K21", "阿杰举手提问，老周微笑回答",
 "The young male student raises his hand and the older man smiles and answers.",
 "好好准备，有疑问就问。", "认真准备，有疑问就问"),
# 小结
("小结", "一叠空白题卡，最上面一张打勾",
 "A stack of blank question cards with a green check on the top card. No people.",
 "概念、定律、仪表，答题要点记牢。", "小结"),
("小结", "直流交流、串联并联、电压表电流表图标",
 "Icons: DC and AC graphs, series and parallel resistors, a voltmeter and an ammeter. No people.",
 "分清直交流、串并联、表的接法。"),
# 结尾
("结尾", "阿杰走出考场，和欣欣击掌",
 "The young male student walks out of the exam room smiling and gives the panda mascot a high five.",
 "口试顺利通过，下次见！"),
]
