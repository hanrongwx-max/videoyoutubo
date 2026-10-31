# 18_Earthing Why Earthing Is Important What Is The Use of Earthing What Is The Need 卡通剧本作者源
# 原著版：完全照原片（白板动画：接地的定义与做法、五个作用、有无接地的对比示意图），K1–K11，
# 不加补充知识点、不做本土化和更正（保留原片的镀锌铁、“零电位的大地”、不区分保护接地与系统接地、
#  “有接地时人碰外壳不会触电”的说法）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "接地为什么重要",
    "edition": "原著版",
    "points": {
        "K1": "什么是接地",
        "K2": "接哪里：金属外壳与中性点",
        "K3": "接地材料",
        "K4": "漏电和短路电流有处去",
        "K5": "作用一：给漏电流开条路",
        "K6": "作用二：保护人身安全",
        "K7": "作用三：建筑防雷",
        "K8": "作用四：泄放雷电和短路电流",
        "K9": "作用五：电子设备工作更稳",
        "K10": "没有接地：电流走人身",
        "K11": "有接地：电流走接地线",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSI study guide", "HSI Study Guide"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验室配电箱旁，手里拿着一段黄绿色导线，向镜头招手",
 "The panda mascot stands beside a lab distribution box holding a short green and yellow wire and waves at the camera.",
 "你好！今天讲讲接地。", "接地，给漏电找条路"),
("开场", "接地符号、闪电、盾牌三个图标",
 "Three icons in a row: a ground symbol, a lightning bolt and a shield. No people.",
 "它是什么，为什么非要不可？"),
# 情景
("情景", "阿杰摸了一下烘箱的金属外壳，皱眉缩手",
 "The young male student touches the metal case of a lab oven, frowns and pulls his hand back.",
 "阿杰碰烘箱外壳，手有点发麻。"),
("情景", "老李检查烘箱后面，发现接地线松脱",
 "The facility engineer checks the back of the oven and finds a loose green and yellow ground wire.",
 "老李一查：接地线松了。"),
("情景", "老李贴上空白停用牌，欣欣走过来",
 "The facility engineer attaches a blank out of service tag to the oven as the panda mascot walks over.",
 "先停用修好。欣欣来讲讲为什么。"),
# K1
("K1", "设备外壳经一根导线连到地下接地极",
 "A metal equipment case connected by a wire to a ground rod buried in the earth. No people.",
 "接地，就是用电阻很小的导线，", "什么是接地"),
("K1", "漏出的电沿导线快速流入大地",
 "Stray current flows quickly along the wire down into the earth. No people.",
 "把不该有的电，直接引进大地。"),
# K2
("K2", "仪器金属外壳上的接地端子亮起",
 "The ground terminal on the metal case of a lab instrument lights up. No people.",
 "把设备不带电的金属部分接地，", "接哪里：金属外壳与中性点"),
("K2", "变压器中性点连到接地极的示意图标",
 "An icon of a transformer whose neutral point is connected to a ground rod. No people.",
 "或把供电系统的中性点接地。"),
# K3
("K3", "镀锌铁接地极和扁铁图标",
 "Icons of a galvanized iron ground rod and a flat galvanized iron strip. No people.",
 "接地材料，多用镀锌铁。", "接地材料", ["镀锌铁"]),
# K4
("K4", "设备漏电，电流沿接地线顺利流走",
 "Leakage current from an instrument flows smoothly away through the ground wire. No people.",
 "有了接地，漏电流有路可走。", "漏电和短路电流有处去"),
("K4", "短路瞬间大电流沿接地线入地，设备完好",
 "At the moment of a short circuit, a large current runs through the ground wire into the earth and the instrument stays intact. No people.",
 "短路时电流流进零电位的大地，"),
("K4", "盾牌护住设备和线路图标",
 "A shield protecting an instrument and its wiring. No people.",
 "保护系统和设备不被损坏。"),
# K5
("K5", "欣欣举起写着五个点的空白卡",
 "The panda mascot holds up a blank card with five dots.",
 "接地有五个作用。", "作用一：给漏电流开条路", ["五个作用"]),
("K5", "两条路：一条经人形，一条经接地线，电流选了接地线",
 "Two paths for leakage current: one through a person pictogram and one through a ground wire; the current takes the ground wire. No people.",
 "第一，给漏电流另开一条入地的路。"),
# K6
("K6", "人形图标触碰仪器外壳，安然无恙，打绿勾",
 "A person pictogram touches an instrument case and stays safe, with a green check. No people.",
 "第二，减少触电，保护人的生命。", "作用二：保护人身安全"),
# K7
("K7", "高楼顶上的避雷针，闪电击中后沿引下线入地",
 "A lightning rod on top of a tall building; lightning strikes it and travels down a conductor into the ground. No people.",
 "第三，高楼防雷也要靠接地。", "作用三：建筑防雷"),
# K8
("K8", "雷电流和短路电流两个箭头都流向接地极",
 "Two arrows, one from lightning and one from a short circuit, both flow into a ground rod. No people.",
 "第四，雷电流、短路电流安全泄放。", "作用四：泄放雷电和短路电流"),
# K9
("K9", "精密仪器屏幕上的杂乱波形变得平稳",
 "A noisy waveform on a precision instrument screen becomes smooth and stable. No people.",
 "第五，让精密电子设备工作更稳。", "作用五：电子设备工作更稳"),
# K10
("K10", "示意图：变压器经相线给设备供电，设备外壳漏电",
 "A diagram: a transformer supplies an instrument through a live wire, and the instrument case leaks current. No people.",
 "看对比：设备没接地，外壳漏电，", "没有接地：电流走人身"),
("K10", "人形图标摸外壳，红色电流穿过身体到地面",
 "A person pictogram touches the case, and red current arrows pass through the body down to the ground. No people.",
 "人一碰，电流就从人身上走。"),
("K10", "人形图标周围闪电，打红叉",
 "Lightning bolts around the person pictogram, with a red X. No people.",
 "这就是触电。"),
# K11
("K11", "同样的示意图，外壳多了一根接地线",
 "The same diagram, but the instrument case now has a ground wire to a ground rod. No people.",
 "设备接了地，外壳照样漏电，", "有接地：电流走接地线"),
("K11", "电流沿接地线流走，人形图标安全",
 "Current arrows flow away through the ground wire, and the person pictogram touching the case stays safe. No people.",
 "电流沿接地线走，人就安全得多。"),
("K11", "人形图标摸着外壳，旁边盾牌打绿勾",
 "A person pictogram touching the instrument case with a shield and a green check beside it. No people.",
 "人碰外壳，也不会触电。"),
# 小结
("小结", "欣欣站在接地示意图前",
 "The panda mascot stands in front of a diagram of an instrument connected to a ground rod.",
 "接地，就是给漏电找条安全的路。", "小结"),
("小结", "人形、楼房避雷针、精密仪器三个图标",
 "Three icons: a safe person pictogram, a building with a lightning rod and a precision instrument. No people.",
 "护人、防雷、护设备，都离不开它。"),
("小结", "没接地触电与接地后安全的两幅对比图标",
 "Two side-by-side icons: an ungrounded case shocking a person pictogram with a red X, and a grounded case with a safe person and a green check. No people.",
 "没接地电走人身，有接地电走地线。"),
# 结尾
("结尾", "欣欣、老李和阿杰站在修好的烘箱旁一起挥手",
 "The panda mascot, the facility engineer and the young male student wave goodbye beside the repaired oven.",
 "接好地，用好电，下次见！"),
]
