# 21_Basic Electrical Engineering Laboratory Viva Questions & Answers -Two Wattmeter 卡通剧本作者源
# 原著版：完全照原片（“二瓦特表法测三相功率”实验的口试问答），K1–K9，
# 不加补充知识点、不做本土化和更正（保留星形连接、线电压 400 V 的三相电源，
# tanφ = √3(W2 − W1)/(W1 + W2) 的板书写法，不讲功率表反偏的处理）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "二瓦特表法口试问答",
    "edition": "原著版",
    "points": {
        "K1": "三相功率怎么测",
        "K2": "什么是二瓦特表法",
        "K3": "三相有功功率公式",
        "K4": "三相无功功率公式",
        "K5": "由两表读数算功率因数",
        "K6": "三相电源和三相负载举例",
        "K7": "还会问到电机",
        "K8": "功率表的两个线圈",
        "K9": "有疑问就提出",
    },
    "avoid": ["VTU", "Visvesvaraya", "Simplified EEE Studies", "Simplified EEE", "21ELEL17", "21ELEL27", "BE/BTech",
              "Experiment 7"],
}

SHOTS = [
# 开场
("开场", "欣欣站在三相实验台前，台上两块功率表和一台小电动机",
 "The panda mascot stands at a three-phase lab bench with two wattmeters with blank dials and a small motor, waving at the camera.",
 "大家好！今天复习二瓦特表法。", "二瓦特表法口试问答"),
("开场", "两块功率表、三相线、电动机三个图标",
 "Three icons in a row: two wattmeters, three supply lines, and an induction motor. No people.",
 "两块表，测出三相总功率。", "", ["两块表", "三相", "功率"]),
# 情景
("情景", "阿杰对着两块功率表挠头",
 "The young male student scratches his head in front of two wattmeters with blank dials.",
 "阿杰纳闷：三相功率，两块表就够？"),
("情景", "小研拿出空白题卡",
 "The female graduate student holds up a stack of blank question cards.",
 "小研说：口试题一道道过，就明白了。"),
# K1
("K1", "三相线路上接着两块功率表的图标",
 "An icon of a three-phase line with two wattmeters connected. No people.",
 "第一题：三相功率怎么测？", "三相功率怎么测", ["二瓦特表法"]),
("K1", "平衡天平和不平衡天平都打勾",
 "Two icons, a balanced scale and an unbalanced scale, both with green checks. No people.",
 "用二瓦特表法，负载对称不对称都能测。"),
# K2
("K2", "两块功率表分别串在两根相线上，第三根线作公共参考",
 "An icon of two wattmeters placed on two of the three lines, with the third line as the common reference. No people.",
 "第二题：两块功率表接在任意两根相线上。", "什么是二瓦特表法", ["W1", "W2"]),
("K2", "星形连接的三相电源图标，线间标着电压",
 "A star-connected three-phase source icon with a voltage arrow between two lines. No people.",
 "三相电源星形连接，线电压四百伏。", "", ["400 V"]),
("K2", "两块表的读数相加得到总功率",
 "Two meter icons with a plus sign between them and an equals sign leading to a total power icon. No people.",
 "总功率等于两块表读数相加。", "", ["P=W1+W2"]),
("K2", "功率表旁一个有功功率灯泡图标",
 "A wattmeter icon beside a glowing lamp icon representing real power. No people.",
 "测出来的是有功功率。"),
# K3
("K3", "白板上写着三相有功功率公式",
 "A whiteboard with a three-phase real power formula in symbols only. No people.",
 "第三题：有功功率可以用线量写。", "三相有功功率公式", ["P=√3·VL·IL", "×cosφ"]),
("K3", "白板上写着用相量表示的公式",
 "A whiteboard with the same formula written using phase quantities. No people.",
 "也可以用相量写，cosφ 是功率因数。", "", ["P=3·Vph·Iph", "×cosφ"]),
# K4
("K4", "白板上把 cos 换成 sin",
 "A whiteboard where a cosine symbol is replaced by a sine symbol. No people.",
 "无功功率：把余弦换成正弦。", "三相无功功率公式", ["Q=√3·VL·IL", "×sinφ"]),
# K5
("K5", "两块表的读数卡片和一个计算器",
 "Two blank reading cards for two meters next to a calculator. No people.",
 "第四题：功率因数怎么算？", "由两表读数算功率因数"),
("K5", "白板上写着正切公式",
 "A whiteboard with a tangent formula in symbols only. No people.",
 "先由两表读数算出正切值。", "", ["tanφ=√3×", "(W2−W1)", "÷(W1+W2)"]),
("K5", "小研用计算器先求角度，再求余弦",
 "The female graduate student uses a calculator, first finding an angle, then its cosine.",
 "反求出角度，再取余弦，就是功率因数。"),
# K6
("K6", "发电机图标引出三根线",
 "A generator icon with three output lines. No people.",
 "第五题：三相电源，比如交流发电机。", "三相电源和三相负载举例"),
("K6", "三相异步电动机图标",
 "A three-phase induction motor icon. No people.",
 "三相负载，最典型的是异步电动机。"),
# K7
("K7", "电动机和发电机图标旁各一个问号",
 "A motor icon and a generator icon, each with a question mark. No people.",
 "口试也可能问电机的原理。", "还会问到电机"),
# K8
("K8", "功率表内部两个线圈示意：一个粗一个细",
 "A cutaway icon of a wattmeter showing two coils, one thick and one thin. No people.",
 "补充：功率表里有两个线圈。", "功率表的两个线圈"),
("K8", "粗线圈串在线路里",
 "The thick coil connected in series with the line. No people.",
 "电流线圈串在线路里。", "", ["电流线圈", "M", "L"]),
("K8", "细线圈并在两根线之间",
 "The thin coil connected across two lines. No people.",
 "电压线圈并在线路两端。", "", ["电压线圈", "C", "V"]),
# K9
("K9", "阿杰举手，王老师走过来",
 "The young male student raises his hand and the safety administrator walks over.",
 "复习有疑问，及时问老师。", "有疑问就提出"),
# 小结
("小结", "两块功率表相加的图标",
 "Two wattmeter icons with a plus sign and an equals sign. No people.",
 "二瓦特表法：两表相加是总功率。", "小结", ["P=W1+W2"]),
("小结", "余弦和正弦两张公式卡片",
 "Two formula cards, one with a cosine symbol and one with a sine symbol. No people.",
 "有功用余弦，无功用正弦。"),
("小结", "发电机和电动机图标",
 "A generator icon and a motor icon side by side. No people.",
 "电源如发电机，负载如电动机。"),
("小结", "功率表两个线圈图标",
 "A wattmeter icon showing its thick current coil and thin voltage coil. No people.",
 "功率表：电流线圈串，电压线圈并。"),
# 结尾
("结尾", "欣欣在三相实验台前挥手",
 "The panda mascot waves goodbye at the three-phase lab bench with two wattmeters.",
 "祝口试顺利，下次见！"),
]
