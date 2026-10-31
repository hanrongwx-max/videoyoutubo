# 17_Safe Working Distance From Overhead Electrical Transmission Line 卡通剧本作者源
# 原著版：完全照原片（高压输电线分级、与架空线的安全作业距离表，两分多钟），K1–K6，不加补充知识点、不做本土化和更正
# （保留原片的 HV 100–230 kV、EHV 230–1000 kV、UHV 1000 kV 以上，以及五档距离 1.40/3.60/4.70/5.70/6.50 m，
#  含板书的“132–273 kV”“273–400 kV”档）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "离高压线远一点",
    "edition": "原著版",
    "points": {
        "K1": "高压：100到230千伏",
        "K2": "超高压：230到1000千伏",
        "K3": "特高压：1000千伏以上",
        "K4": "必须保持安全距离",
        "K5": "五档安全距离",
        "K6": "吊臂碰线最危险",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSC Study Guide", "O-RAID"],
}

SHOTS = [
# 开场
("开场", "欣欣站在工地空地上，远处是输电铁塔和架空线，向镜头招手",
 "The panda mascot stands on an open work site with transmission towers and overhead power lines in the distance and waves at the camera.",
 "你好！今天聊聊头顶上的高压线。", "离高压线远一点"),
("开场", "铁塔、闪电、距离箭头三个图标",
 "Three icons in a row: a transmission tower, a lightning bolt and a double-headed distance arrow. No people.",
 "它有多危险，要离多远？"),
# 情景
("情景", "阿杰扛着一根长长的铝合金杆走在工地边，上方有电线",
 "The young male student carries a long aluminum pole on his shoulder along the edge of a work site, with power lines overhead.",
 "阿杰扛着长铝杆穿过工地。"),
("情景", "杆子一头慢慢翘起，接近头顶电线",
 "The end of the long pole tilts upward and gets close to the overhead power line.",
 "杆子一翘，离电线越来越近。"),
("情景", "小研大喊着跑来，阿杰赶紧放平杆子",
 "The female graduate student shouts and runs over, and the young male student quickly lowers the pole flat.",
 "小研一声喊，阿杰赶紧放平。"),
("情景", "欣欣出现，指着上方的电线",
 "The panda mascot appears and points up at the overhead lines.",
 "欣欣说：高压线，离远一点！"),
# K1
("K1", "欣欣站在三座不同高度的铁塔图标前",
 "The panda mascot stands in front of three transmission tower icons of increasing height.",
 "高压输电线按电压分三级。", "高压：100到230千伏", ["HV", "EHV", "UHV"]),
("K1", "较矮的铁塔图标亮起",
 "The shortest transmission tower icon lights up. No people.",
 "高压线路，100到230千伏。", "", ["HV", "100–230kV"]),
# K2
("K2", "中等高度的铁塔图标亮起，闪电变大",
 "The middle transmission tower icon lights up and its lightning bolt grows bigger. No people.",
 "超高压线路，230到1000千伏。", "超高压：230到1000千伏", ["EHV", "230–1000"]),
# K3
("K3", "最高的铁塔图标亮起，闪电最大",
 "The tallest transmission tower icon lights up with the biggest lightning bolt. No people.",
 "特高压线路，1000千伏以上。", "特高压：1000千伏以上", ["UHV", "＞1000kV"]),
# K4
("K4", "架空线下画出一圈半透明的禁入区",
 "A translucent keep-out zone drawn around an overhead power line. No people.",
 "架空线周围，有一圈不能进的范围。", "必须保持安全距离"),
("K4", "人形图标停在禁入区边界外",
 "A person pictogram stops outside the boundary of the keep-out zone. No people.",
 "人和工具，都要留在圈外。"),
# K5
("K5", "五条线路图标，禁入区一圈比一圈大",
 "Five power line icons whose keep-out zones grow larger with each one. No people.",
 "电压越高，要离得越远，共五档。", "五档安全距离"),
("K5", "第一、二条线路图标亮起，旁边距离箭头",
 "The first and second power line icons light up with distance arrows beside them. No people.",
 "11千伏以下1.4米，11到33千伏3.6米。", "", ["≤11kV", "1.40m", "11–33kV", "3.60m"]),
("K5", "第三条线路图标亮起",
 "The third power line icon lights up with a longer distance arrow. No people.",
 "33到132千伏，4.7米。", "", ["33–132kV", "4.70m"]),
("K5", "第四条线路图标亮起",
 "The fourth power line icon lights up with a long distance arrow. No people.",
 "132到273千伏，5.7米。", "", ["132–273kV", "5.70m"]),
("K5", "第五条线路图标亮起，距离箭头最长",
 "The fifth power line icon lights up with the longest distance arrow. No people.",
 "273到400千伏，6.5米。", "", ["273–400kV", "6.50m"]),
("K5", "距离箭头旁出现米和英尺两种刻度",
 "The distance arrows show two scales side by side, meters and feet. No people.",
 "折合约4.6到21.3英尺。", "", ["4.59ft", "21.32ft"]),
# K6
("K6", "起重机吊臂伸向架空线的图标打红叉",
 "An icon of a crane boom reaching toward an overhead power line, crossed out with a red X. No people.",
 "最常见的事故：吊臂碰到电线。", "吊臂碰线最危险"),
("K6", "电流沿吊臂传到车身，地面出现一圈圈波纹",
 "Current runs down the crane boom into the vehicle body, and ripples spread on the ground around it. No people.",
 "电会沿着机械传下来，"),
("K6", "周围站着的人形图标都被闪电波及",
 "Person pictograms standing around the crane are reached by lightning symbols. No people.",
 "旁边站着的人也会受伤。"),
# 小结
("小结", "欣欣站在铁塔图标前",
 "The panda mascot stands in front of a transmission tower icon.",
 "高压线分等级，电压越高越危险。", "小结"),
("小结", "禁入区和距离箭头图标",
 "A keep-out zone icon with a distance arrow around a power line. No people.",
 "人、工具、机械，都要离得够远。"),
("小结", "吊臂碰线图标打红叉",
 "An icon of a crane boom touching an overhead line, crossed out with a red X. No people.",
 "吊臂别靠近，周围人也要远离。"),
# 结尾
("结尾", "欣欣、小研和放平长杆的阿杰一起挥手",
 "The panda mascot waves goodbye with the female graduate student and the young male student, who holds the pole flat.",
 "抬头看一眼，安全多一分，下次见！"),
]
