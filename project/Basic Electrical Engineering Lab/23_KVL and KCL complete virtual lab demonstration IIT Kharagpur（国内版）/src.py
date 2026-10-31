# 23_KVL and KCL complete virtual lab demonstration IIT Kharagpur 卡通剧本作者源
# 原片为 15 秒竖屏预告短片（KVL/KCL 仿真演示封面），非安全专题：保留全部知识点 K1–K4，审查补充 S1–S3
# （拔插头握插头本体、电源线不压不折不穿门缝、散热口不遮挡）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "基尔霍夫两定律速记",
    "points": {
        "K1": "电压定律：串联电压相加等于电源",
        "K2": "电流定律：流入等于流出",
        "K3": "用仿真实验来验证",
        "K4": "完整步骤看完整演示",
        "S1": "拔插头，握住插头本体",
        "S2": "电源线不压、不折、不穿门缝",
        "S3": "散热口不遮挡",
    },
    "avoid": ["IIT", "Kharagpur", "Virtual Labs", "Vineeth", "Simplified EEE Studies", "Simplified EEE", "VTU"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一块空白卡片，卡片上只有回路和节点两个图标",
 "The panda mascot holds up a blank card showing only a loop icon and a junction icon, waving at the camera.",
 "两条定律，一起速记！", "基尔霍夫两定律速记"),
# 情景
("情景", "阿杰考前在台灯下翻空白笔记，皱眉",
 "The young male student flips through a blank notebook under a desk lamp before an exam, frowning.",
 "考前，阿杰又把两条定律记混了。"),
("情景", "小研拿出两张卡片，一张画回路，一张画节点",
 "The female graduate student holds up two cards, one with a loop icon and one with a junction icon.",
 "小研说：一个看回路，一个看节点。"),
# K1
("K1", "电源与两个电阻串联成回路，一个环形箭头绕回路一圈",
 "A circuit icon: a battery in series with two resistors forming a loop, with a circular arrow going around. No people.",
 "电压定律看回路。", "电压定律：串联电压相加等于电源", ["R1", "R2"]),
("K1", "两个电阻上的电压条叠起来，和电源电压条一样高",
 "Two voltage bars for the two resistors stacked together, exactly as tall as the battery's voltage bar. No people.",
 "两个电阻的电压，叠起来一样高。", "", ["V1+V2=Vs"]),
("K1", "叠起的电压条与电源条之间一个等号",
 "An equals sign between the stacked voltage bars and the battery voltage bar. No people.",
 "所以电阻电压之和等于电源电压。"),
("K1", "欣欣沿着回路走一圈，回到起点",
 "The panda mascot walks around a large loop drawn on the floor and returns to the start point.",
 "绕回路一圈，电压升降正好抵消。"),
# K2
("K2", "一个节点，一支粗箭头流入，两支细箭头流出",
 "A junction icon with one thick arrow flowing in and two thinner arrows flowing out. No people.",
 "电流定律看节点。", "电流定律：流入等于流出", ["I", "I1", "I2"]),
("K2", "水管三通，一股水流分成两股",
 "A water pipe T-junction icon where one stream splits into two streams. No people.",
 "就像水管分岔，水不会凭空变多变少。"),
("K2", "节点公式卡片",
 "A card with a junction formula in symbols only. No people.",
 "流进的电流，等于流出的电流之和。", "", ["I=I1+I2"]),
# K3
("K3", "笔记本电脑屏幕上是空白的仿真电路图标",
 "A laptop screen showing a blank simulated circuit icon with small meters. No people.",
 "这两条定律，可以用仿真实验验证。", "用仿真实验来验证"),
("K3", "靶心、阶梯、对勾三个图标",
 "Three icons in a row: a target, a staircase, and a check mark. No people.",
 "好懂、分步，实验和考试都用得上。", "", ["好懂", "分步", "备考"]),
# K4
("K4", "欣欣指向一部播放按钮图标的屏幕",
 "The panda mascot points at a screen showing only a large play button icon.",
 "完整步骤，请看上一集的完整演示。", "完整步骤看完整演示"),
("K4", "阿杰在电脑前跟着做，旁边空白笔记本",
 "The young male student follows along on a laptop with a blank notebook beside him.",
 "边看边做，记下每一步。"),
# S1
("S1", "阿杰在实验台旁拔笔记本电源，手握插头本体",
 "At the lab bench, the young male student unplugs a laptop power cord by gripping the plug body.",
 "用完拔插头，要握住插头本体。", "拔插头，握住插头本体"),
("S1", "拽着电线拔插头的图标被红叉划掉",
 "An icon of a hand yanking a power cord to pull out a plug, crossed out with a red X. No people.",
 "别拽电线，容易拉断、拉松。"),
("S1", "湿手拔插头的图标被红叉划掉",
 "An icon of a wet hand reaching for a plug, crossed out with a red X. No people.",
 "手湿时，更不要碰插头。"),
# S2
("S2", "电源线被椅子腿压住的图标被红叉划掉",
 "An icon of a power cord pinched under a chair leg, crossed out with a red X. No people.",
 "电源线别被椅子、重物压住。", "电源线不压、不折、不穿门缝"),
("S2", "电源线穿过门缝被门夹住的图标被红叉划掉",
 "An icon of a power cord running through a door gap and pinched by the door, crossed out with a red X. No people.",
 "不穿门缝、不被门夹。"),
("S2", "老李把破皮的电源线换成新的",
 "The facility engineer replaces a power cord with cracked insulation with a new one.",
 "线皮磨破了，停用并更换。"),
# S3
("S3", "笔记本电脑放在被子上、散热口被堵的图标被红叉划掉",
 "An icon of a laptop on a soft blanket with its air vents blocked, crossed out with a red X. No people.",
 "电脑别放在被子、软垫上用。", "散热口不遮挡"),
("S3", "仪器背面散热口前堆着书本的图标被红叉划掉",
 "An icon of books piled against the rear air vents of a lab instrument, crossed out with a red X. No people.",
 "仪器的散热口，不能堆东西挡住。"),
("S3", "小研把电源适配器放在通风的桌面上",
 "The female graduate student places a power adapter on an open, well-ventilated desk.",
 "适配器放在通风处，发烫就停用。"),
# 小结
("小结", "回路图标和节点图标并排",
 "A loop icon and a junction icon side by side. No people.",
 "回路看电压，节点看电流。", "小结", ["V1+V2=Vs", "I=I1+I2"]),
("小结", "握插头、理顺电线、通风三个打勾图标",
 "Three icons with green checks: a hand gripping a plug, a neatly routed cord, and an air vent with airflow lines. No people.",
 "握插头拔，线不压，口不挡。"),
# 结尾
("结尾", "欣欣合上笔记本电脑，挥手告别",
 "The panda mascot closes a laptop and waves goodbye.",
 "下次见，安全用电！"),
]
