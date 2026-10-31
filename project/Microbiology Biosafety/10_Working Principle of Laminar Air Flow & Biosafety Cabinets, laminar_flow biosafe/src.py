# 10_Working Principle of Laminar Air Flow & Biosafety Cabinets, laminar_flow biosafe 原著版卡通剧本作者源
# 完全照原片：K1–K13（层流与生物安全柜的定义、作用、目标、气流、过滤、围护、应用对比与小结），无补充知识点；
# 不加超净台吹向人的警示、安全柜选型和个人防护
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "层流台 VS 生物安全柜：别选错",
    "edition": "原著版",
    "points": {
        "K1": "两种设备：层流台与生物安全柜",
        "K2": "层流：平行单向、少湍流的气流",
        "K3": "层流的用处：营造洁净环境",
        "K4": "层流首要目标：减少颗粒和微生物",
        "K5": "生物安全柜：处理危险生物材料",
        "K6": "安全柜保护操作者和环境",
        "K7": "安全柜靠气流、过滤、围护防护",
        "K8": "目标区别：洁净 VS 围护",
        "K9": "气流方向不同",
        "K10": "两者都用高效过滤",
        "K11": "围护结构不同",
        "K12": "各自的应用场景",
        "K13": "都受控，但目的不同",
    },
    "avoid": ["raqbamicrohub", "Ragba Micro Hub", "Ragba", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在两台外形相似的设备中间，向镜头招手",
 "The panda mascot stands between two similar-looking lab cabinets and waves at the camera. Blank panels.",
 "这一课比较两种实验室设备。", "层流台 VS 生物安全柜：别选错"),
("开场", "欣欣指向左右两个空白设备图标",
 "The panda mascot points to a left and a right blank cabinet icon. No text on them.",
 "层流台和生物安全柜，别搞混。", "", ["层流台", "安全柜"]),
# 情景
("情景", "阿杰站在两台机器前，一脸犯难",
 "The young male student stands in front of the two cabinets looking confused.",
 "阿杰分不清这两台机器。"),
("情景", "阿杰转身问小研，小研指着两台设备",
 "The young male student asks a question; the female graduate student points at the two cabinets.",
 "小研说：它们的目的不一样。"),
("情景", "欣欣出现在两人身旁",
 "The panda mascot appears beside the two students.",
 "先弄清它俩差在哪。"),
# K1
("K1", "两台空白柜子的剖面轮廓并排",
 "Two blank cabinet cutaway outlines side by side. No people.",
 "今天比层流台和生物安全柜。", "两种设备"),
# K2
("K2", "一组平行、同向的气流箭头",
 "A set of parallel arrows all pointing the same direction, evenly spaced. No people.",
 "层流：平行、单向的气流。", "什么是层流"),
("K2", "顺滑的流线，几乎没有漩涡",
 "Smooth straight streamlines with almost no swirls. No people.",
 "气流很稳，几乎没有乱流。"),
# K3
("K3", "一个闪着洁净光点的工作区图标",
 "A work-area icon with clean sparkle dots. No people.",
 "它的用处是营造洁净环境。", "层流做什么"),
# K4
("K4", "空气里的尘点被箭头带走",
 "Airborne dust dots being carried away by an arrow. No people.",
 "首要目标：减少空气里的颗粒。", "减少污染"),
("K4", "一个微生物图标旁边有向下的箭头",
 "A microbe icon next to a downward arrow. No people.",
 "把微生物和污染物降下来。"),
# K5
("K5", "一台生物安全柜轮廓，角上有生物危害图标",
 "A biosafety cabinet outline with a biohazard pictogram in the corner. No people.",
 "生物安全柜处理危险材料。", "什么是生物安全柜"),
("K5", "柜内一个烧瓶贴着生物危害图标",
 "Inside the cabinet, a flask marked with a biohazard pictogram. No people.",
 "尤其是有生物危害的材料。"),
# K6
("K6", "一个操作者图标和一个环境图标，都被盾牌护住",
 "An operator icon and an environment icon, both covered by a shield. No people shown in detail.",
 "它保护操作者，也保护环境。", "保护谁"),
("K6", "一个感染微生物图标被挡在外面",
 "An infectious-microbe icon blocked by a barrier. No people.",
 "挡住感染微生物和毒素。"),
# K7
("K7", "定向气流箭头、过滤器和围护框三个图标",
 "Three icons: directional airflow arrows, a filter, and an enclosure frame. No people.",
 "靠定向气流加高效过滤。", "靠什么防护"),
("K7", "一个围护外壳把柜子包起来",
 "An enclosure shell wrapping around the cabinet. No people.",
 "再加上围护结构挡一挡。"),
# K8
("K8", "画面一分为二：左边洁净光点，右边围护框",
 "A split frame: clean sparkle dots on the left, an enclosure frame on the right. No people.",
 "关键区别：洁净还是围护。", "目标不一样"),
("K8", "左边层流图标标着洁净符号",
 "Left-side laminar-flow icon tagged with a clean symbol. No people.",
 "层流重在洁净，不管围护。"),
("K8", "右边安全柜图标标着围护符号",
 "Right-side cabinet icon tagged with a containment symbol. No people.",
 "安全柜重在围住危险。"),
# K9
("K9", "平行箭头水平和垂直吹过工作台",
 "Parallel arrows sweeping horizontally and vertically across a workbench. No people.",
 "层流的风，平行吹过工作区。", "气流方向"),
("K9", "安全柜前窗处的箭头向内吸",
 "Arrows curving inward at the cabinet front window. No people.",
 "安全柜把风往里吸，护住人。"),
# K10
("K10", "两台设备顶部都画着高效过滤器",
 "Both cabinets shown with a HEPA filter block on top. No people.",
 "两者都用高效过滤器。", "都要过滤"),
("K10", "安全柜的过滤器图标上拦住一个微生物",
 "The cabinet's filter icon catching a microbe. No people.",
 "安全柜的过滤还要拦住病原。"),
# K11
("K11", "层流台前面是敞开的，没有屏障",
 "A laminar bench with an open front and no barrier. No people.",
 "层流台没有专门围护。", "围护结构"),
("K11", "安全柜画出前窗、屏障和排风管",
 "A biosafety cabinet drawn with a front window, a barrier, and an exhaust duct. No people.",
 "安全柜有前窗、屏障和排风。"),
# K12
("K12", "层流一侧出现药片、芯片、培养皿图标",
 "Beside the laminar bench appear icons of a pill, a microchip, and a culture dish. No people.",
 "层流用于制药、电子装配、组织培养。", "各自用在哪"),
("K12", "安全柜一侧出现毒素瓶、检测和微生物图标",
 "Beside the cabinet appear a toxin flask icon, a diagnostic-test icon and a microbe icon. No people.",
 "安全柜用于毒素、诊断和感染因子。"),
# K13
("K13", "两台设备都被一个受控环境框圈住",
 "Both cabinets enclosed by a single controlled-environment frame. No people.",
 "两者都给受控环境。", "记住区别"),
("K13", "欣欣左右手各指一台设备",
 "The panda mascot points to each cabinet with a different paw.",
 "但一个重洁净，一个重围护。"),
# 小结
("小结", "欣欣站在两台设备中间，各指一台",
 "The panda mascot stands between the two cabinets, pointing to each.",
 "层流重洁净，安全柜重围护。"),
("小结", "欣欣竖起一根手指提醒",
 "The panda mascot raises one finger as a reminder.",
 "都受控，但首要目的不同。"),
# 结尾
("结尾", "欣欣在实验室里向镜头挥手告别",
 "The panda mascot waves goodbye in the lab.",
 "分清目的，认准设备，下次见！"),
]
