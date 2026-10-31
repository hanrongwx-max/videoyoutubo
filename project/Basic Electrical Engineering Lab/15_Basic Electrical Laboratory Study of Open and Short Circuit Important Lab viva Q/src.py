# 15_Basic Electrical Laboratory Study of Open and Short Circuit Important Lab viva Q 卡通剧本作者源
# 原著版：完全照原片（“开路与短路”实验的口试问答：开路、短路、串并联、熔断器、SPST/DPST），K1–K15，
# 不加补充知识点、不做本土化和更正（保留“开路电压变为无穷大”“短路电流无穷大”的说法、雷雨天电线杆导线相碰的例子、
# 熔断器规格举例 5 A、32 A、64 A）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "开路与短路实验口试问答",
    "edition": "原著版",
    "points": {
        "K1": "本集考什么",
        "K2": "什么是开路",
        "K3": "什么是短路",
        "K4": "电阻的三种连接",
        "K5": "什么是串联",
        "K6": "串联的特点",
        "K7": "一两句话答清楚",
        "K8": "什么是并联",
        "K9": "并联的特点",
        "K10": "熔断器保护设备",
        "K11": "熔断器接相线、串在电路里",
        "K12": "按负载选熔断器规格",
        "K13": "单刀单掷开关",
        "K14": "双刀单掷开关",
        "K15": "小结，复习上一集",
    },
    "avoid": ["VTU", "Simplified EEE", "EEE Studies"],
}

SHOTS = [
# 开场
("开场", "欣欣坐在考官桌后，举起一张空白题卡",
 "The panda mascot sits behind an examiner's desk holding up a blank question card, waving at the camera.",
 "口试第二关：开路和短路！", "电工实验口试：开路与短路篇"),
# 情景
("情景", "阿杰和小研在实验室门口复习",
 "The young male student and the female graduate student review notes together at the lab door.",
 "阿杰和小研一起准备第二次口试。"),
# K1
("K1", "断开的电路和被导线短接的电路两个图标",
 "Two circuit icons: one with a gap in the wire, one with a wire bridging across the lamp. No people.",
 "这次考开路、短路和相关器件。", "本集考什么", ["开路", "短路"]),
# K2
("K2", "电路导线中间断开一个缺口，灯不亮",
 "A circuit icon with a gap in the wire; the lamp is dark. No people.",
 "开路：电路某处断开了。", "什么是开路"),
("K2", "电流箭头在缺口处停住，旁边写零",
 "A current arrow stops at the gap, with a zero beside it. No people.",
 "断开了，电流就是零。", "", ["I=0"]),
("K2", "缺口两端电压箭头拉得很长，旁边一个无穷大符号",
 "Across the gap, a very long voltage arrow with an infinity symbol beside it. No people.",
 "原片说：开路时电压变为无穷大。", "", ["U→∞"]),
# K3
("K3", "两根导线直接碰在一起，冒出火花",
 "Two bare conductors touching each other directly, with a spark at the contact point. No people.",
 "短路：两根导线直接碰在一起。", "什么是短路"),
("K3", "电流箭头变得很粗，负载两端电压为零",
 "A very thick current arrow bypasses the load; a zero sign beside the load. No people.",
 "短路时电压为零，电流非常大。", "", ["U=0", "I→∞"]),
("K3", "老周比划电流冲向无穷大",
 "The older man spreads his arms wide beside a huge current arrow with an infinity symbol.",
 "原片说：短路电流是无穷大。"),
("K3", "雷雨中电线杆上两根导线被风吹到一起",
 "In a thunderstorm, two overhead wires on a utility pole swing together and spark. No people.",
 "雷雨大风时，电线相碰就会短路。"),
("K3", "欣欣对比两个图标：开路和短路相反",
 "The panda mascot points at the open circuit and short circuit icons side by side.",
 "开路和短路，特点正好相反。"),
# K4
("K4", "串联、并联、串并联三个电阻组合图标",
 "Three resistor combination icons: series, parallel, and series-parallel. No people.",
 "电阻有串联、并联、串并联三种接法。", "电阻的三种连接", ["串联", "并联", "串并联"]),
# K5
("K5", "两个电阻首尾相接",
 "Two resistors connected end to start in a line. No people.",
 "串联：前一个的尾接后一个的头。", "什么是串联"),
# K6
("K6", "串联电阻上同样粗的电流箭头",
 "Two series resistors with equal-thickness current arrows through both. No people.",
 "串联电流处处相同。", "串联的特点"),
("K6", "两个电阻上方电压柱高低不同",
 "Two series resistors with voltage bars of different heights above them. No people.",
 "各个电阻的电压不同。"),
("K6", "分压公式卡片",
 "A blank formula card with a voltage divider icon. No people.",
 "求各段电压，用分压公式。"),
# K7
("K7", "阿杰简短作答，老周点头",
 "The young male student answers in one short sentence; the older man nods approvingly.",
 "回答一两句话，把要点说清就行。", "一两句话答清楚"),
# K8
("K8", "两个电阻并排，头接头、尾接尾",
 "Two resistors side by side, their starting ends joined and their finishing ends joined. No people.",
 "并联：头接头，尾接尾。", "什么是并联"),
# K9
("K9", "并联电阻上方电压柱一样高",
 "Two parallel resistors with voltage bars of equal height. No people.",
 "并联各支路电压相同。", "并联的特点"),
("K9", "电流箭头在节点分成两路",
 "A current arrow splits into two at the junction before the parallel resistors. No people.",
 "电流分流，用分流公式求。"),
# K10
("K10", "人形图标和设备图标并排",
 "Two icons side by side: a person silhouette and a piece of equipment. No people.",
 "安全分人身安全和设备安全。", "熔断器保护设备", ["人身安全", "设备安全"]),
("K10", "熔断器图标，过大电流时熔丝熔断",
 "A fuse icon whose wire melts open when a very thick current arrow passes. No people.",
 "熔断器防过电流，保护线路和设备。"),
# K11
("K11", "熔断器画在相线上打勾，画在零线上打叉",
 "Two circuit icons: a fuse on the phase line with a green check, a fuse on the neutral line with a red X. No people.",
 "熔断器要接在相线上，不接零线。", "熔断器接相线、串在电路里", ["相线 √", "零线 ×"]),
("K11", "熔断器串在电路中",
 "A fuse connected in series in a simple circuit with a lamp. No people.",
 "熔断器和负载串联。"),
# K12
("K12", "不同大小的熔断器排成一排",
 "A row of fuses of different sizes. No people.",
 "熔断器规格很多，五安、三十二安、六十四安。", "按负载选熔断器规格", ["5 A", "32 A", "64 A"]),
("K12", "老李对照负载的空白铭牌挑熔断器",
 "The facility engineer compares a load's blank rating plate with fuse sizes and picks one.",
 "按负载的额定电流来选。"),
# K13
("K13", "单刀单掷开关符号",
 "A single pole single throw switch symbol: one moving blade and one contact. No people.",
 "单刀单掷：一个刀片，一个触点。", "单刀单掷开关", ["SPST"]),
# K14
("K14", "双刀单掷开关符号，两刀用虚线联动",
 "A double pole single throw switch symbol: two blades linked by a dashed line, two contacts. No people.",
 "双刀单掷：两个刀片一起动作。", "双刀单掷开关", ["DPST"]),
("K14", "两刀分别接相线和零线",
 "The double pole switch symbol with one blade on the phase line and one on the neutral line. No people.",
 "一刀接相线，一刀接零线。", "", ["相线", "零线"]),
# K15
("K15", "两张题卡都打勾",
 "Two blank question cards with green check marks. No people.",
 "开路短路、串并联、熔断器、开关。", "小结，复习上一集"),
("K15", "阿杰翻出上次的口试笔记",
 "The young male student takes out his notes from the previous oral exam.",
 "再复习上次的题，祝考试顺利。"),
# 小结
("小结", "开路、短路、串联、并联四个图标",
 "Four icons: open circuit, short circuit, series and parallel resistors. No people.",
 "开路电流为零，短路电流极大。", "小结"),
("小结", "熔断器和两种开关图标",
 "Icons of a fuse and two switch symbols. No people.",
 "熔断器接相线，开关分单刀双刀。"),
# 结尾
("结尾", "阿杰和小研走出考场，和欣欣挥手",
 "The young male student and the female graduate student walk out of the exam room and wave with the panda mascot.",
 "口试加油，下次见！"),
]
