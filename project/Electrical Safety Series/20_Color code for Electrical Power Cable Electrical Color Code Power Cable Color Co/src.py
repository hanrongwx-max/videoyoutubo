# 20_Color code for Electrical Power Cable Electrical Color Code Power Cable Color Co 卡通剧本作者源
# 原著版：完全照原片（电力电缆基本色标：红黄蓝相线、黑色中性线、黄绿地线），K1–K6，
# 不加补充知识点、不做本土化和更正（不加“国内色标”“颜色不能代替验电”等说明）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "电力电缆的颜色代码",
    "edition": "原著版",
    "points": {
        "K1": "认识电线颜色很重要",
        "K2": "三类导线",
        "K3": "单相相线：红黄蓝之一",
        "K4": "三相相线：红黄蓝",
        "K5": "中性线：黑色",
        "K6": "保护导体：黄绿双色",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSE study guide"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一束各种颜色的电线",
 "The panda mascot holds up a bundle of insulated wires in many colors and smiles at the camera.",
 "这一课认识电线的颜色。", "电力电缆的颜色代码"),
("开场", "相线、零线、地线三个图标",
 "Three icons in a row: a lightning bolt, a returning arrow and a ground symbol. No people.",
 "火线、零线、地线，各有颜色。", "", ["相线", "中性线", "保护导体"]),
# 情景
("情景", "阿杰看着打开的配电箱里颜色不同的导线",
 "The young male student looks into an open distribution box at wires of several different colors.",
 "阿杰看着配电箱里五颜六色的线。"),
("情景", "阿杰挠头，一脸不解",
 "The young male student scratches his head with a puzzled look.",
 "这么多颜色，各代表什么？"),
("情景", "欣欣在白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "来认识电力电缆的基本色标。"),
# K1
("K1", "一束彩色电线特写",
 "Close-up of a bundle of wires with red, yellow, blue, black, brown and green-yellow insulation. No people.",
 "电线外皮的颜色，是一种标识。", "认识电线颜色很重要"),
("K1", "老李看着配电箱里的导线点头",
 "The facility engineer looks into an open distribution box at neatly colored wires and nods.",
 "看颜色，就能大致分出导线的用途。"),
("K1", "欣欣指着白板上的空白表格",
 "The panda mascot points at a blank chart with three rows on the whiteboard.",
 "所以，基本色标一定要知道。"),
# K2
("K2", "三根导线并排，分别配闪电、回流箭头、接地符号",
 "Three wires side by side, each labeled with an icon: a lightning bolt, a returning arrow and a ground symbol. No people.",
 "导线分三类。", "三类导线", ["相线", "中性线", "保护导体"]),
("K2", "电流从相线流向灯泡，再从中性线流回",
 "A simple circuit: current flows from the live wire to a light bulb and returns along the neutral wire. No people.",
 "相线送电，中性线让电流流回。"),
("K2", "仪器金属外壳连着一根接地线",
 "The metal case of a lab instrument connected by a wire to a ground symbol. No people.",
 "保护导体连着外壳，就是地线。"),
# K3
("K3", "一张空白表格，单相栏里红、黄、蓝三段导线",
 "A blank chart with a single-phase column showing a red wire, a yellow wire and a blue wire with an or sign between them. No people.",
 "单相线路，相线用红、黄、蓝之一。", "单相相线：红黄蓝之一", ["红", "黄", "蓝"]),
("K3", "单相线路示意：一根红色相线连到灯泡",
 "A single-phase circuit icon with one red live wire running to a light bulb. No people.",
 "三种颜色任选一种都可以。"),
# K4
("K4", "三相栏：第一根红、第二根黄、第三根蓝",
 "A three-phase column with three wires labeled one, two, three in red, yellow and blue. No people.",
 "三相线依次是红、黄、蓝。", "三相相线：红黄蓝", ["L1 红", "L2 黄", "L3 蓝"]),
("K4", "三根线首字母组成简称",
 "The three colored wires gather into a neat bundle with a small shorthand tag. No people.",
 "简称RYB。", "", ["RYB"]),
("K4", "三根红黄蓝导线连到一台三相电动机",
 "Three wires in red, yellow and blue connect to a three-phase electric motor. No people.",
 "三相电动机，就接这三根相线。"),
# K5
("K5", "中性线栏：一根黑色导线",
 "A neutral row in the chart showing a single black wire. No people.",
 "中性线用黑色。", "中性线：黑色", ["黑"]),
("K5", "电流从灯泡沿黑色导线流回",
 "Current flows back from a light bulb along a black wire. No people.",
 "电流沿黑色的中性线流回去。"),
# K6
("K6", "保护导体栏：一根黄绿条纹导线",
 "A protective conductor row showing a wire with green and yellow stripes. No people.",
 "地线用黄绿双色。", "保护导体：黄绿双色", ["黄绿双色"]),
("K6", "黄绿线连到接地符号，打绿勾",
 "The green and yellow striped wire connects to a ground symbol with a green check. No people.",
 "黄绿线，就是保护导体。"),
("K6", "仪器金属外壳上接着黄绿线",
 "A green and yellow striped wire attached to the metal case of a machine. No people.",
 "它连着设备的金属外壳。"),
# 小结
("小结", "欣欣身旁浮现三根导线图标",
 "The panda mascot stands beside floating icons of three wires: live, neutral and ground.",
 "相线、中性线、地线，颜色各不同。", "小结"),
("小结", "色标表：红黄蓝相线、黑色中性线、黄绿地线",
 "A color chart with red, yellow and blue phase wires, a black neutral wire and a green-yellow ground wire. No people.",
 "相线红黄蓝，中性线黑，地线黄绿。"),
("小结", "阿杰对着色标表点头，指向配电箱里的线",
 "The young male student nods at the color chart and points to the matching wires in the distribution box.",
 "记住色标，一眼认出导线。"),
# 结尾
("结尾", "欣欣把一束整理好的电线放进盒子，挥手道别",
 "The panda mascot puts a neat bundle of colored wires into a box and waves goodbye at the camera.",
 "认清颜色，用电安心，下次见！"),
]
