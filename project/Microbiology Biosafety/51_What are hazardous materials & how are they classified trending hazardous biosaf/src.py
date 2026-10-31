# 51_What are hazardous materials & how are they classified trending hazardous biosaf 卡通剧本作者源
# 原片是无人声的文字幻灯片（6 分钟）：危险物品定义、按理化危险分组、联合国危险货物九大类，右侧配 GHS 象形图
# 原著版：完全照原片，K1–K13，无补充知识点；九类照原片为联合国运输类别（第4类只说易燃固体、第9类杂项危险物品），配图照原片为红框象形图，不区分两套体系、不加国内标准
# 审查补充 S1–S3（运输标志与 GHS 象形图是两套体系；一物多险，象形图都要看；分类不明，按最危险对待）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "什么是危险物品？如何分类？",
    "edition": "原著版",
    "points": {
        "K1": "危险物品：伤人、毁物、污染环境",
        "K2": "按理化危险分组",
        "K3": "联合国规定：运输分九类",
        "K4": "第 1 类：爆炸品",
        "K5": "第 2 类：气体",
        "K6": "第 3 类：易燃液体",
        "K7": "第 4 类：易燃固体",
        "K8": "第 5 类：氧化性物质和有机过氧化物",
        "K9": "第 6 类：毒性物质和感染性物质",
        "K10": "第 7 类：放射性物质",
        "K11": "第 8 类：腐蚀性物质",
        "K12": "第 9 类：杂项危险物品",
        "K13": "象形图：通用的危害图形语言",
    },
    "avoid": ["Ragba Micro Hub", "Ragba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一面贴满红框菱形象形图的墙前，向镜头招手",
 "The panda mascot stands in front of a wall covered with GHS hazard pictograms and waves at the camera.",
 "危险物品这么多，怎么分门别类？", "危险物品怎么分类：九大类与象形图"),
("开场", "九个空白格子排成三行三列，依次亮起",
 "Nine blank boxes arranged in three rows of three light up one by one. No people.",
 "今天认识九大类和它们的标志。"),
# 情景
("情景", "阿杰面对满柜贴着菱形标志的试剂瓶",
 "The young male student stands before a cabinet full of reagent bottles with red-bordered diamond symbols.",
 "阿杰看着满柜子的菱形标志。"),
("情景", "阿杰挠头，头顶几个问号",
 "The young male student scratches his head with several question marks above him.",
 "他问：危险物品到底怎么分类？"),
("情景", "欣欣出现，拿着两张卡片",
 "The panda mascot appears holding two blank cards.",
 "欣欣说：先从分类讲起。"),
# K1
("K1", "人体、房屋、河流三个图标，各连一个警示三角",
 "Three icons, a human figure, a house and a river, each linked to a warning triangle. No people.",
 "危险物品，会伤人、毁物、污染环境。", "危险物品：伤人、毁物、污染环境", ["人体健康", "财产", "环境"]),
# K2
("K2", "七个圆形图标依次出现：火焰、腐蚀、骷髅、爆炸、辐射、生物危害、气瓶",
 "Seven round icons appear one by one: flame, corrosion, skull, explosion, radiation trefoil, biohazard, gas cylinder. No people.",
 "按物理和化学危险，分成几组。", "按理化危险分组"),
("K2", "七个图标下方出现中文标签",
 "The seven icons line up in a row with blank label strips beneath them. No people.",
 "易燃、腐蚀、有毒、反应、放射。", None, ["易燃", "腐蚀", "有毒", "反应性", "放射性"]),
("K2", "最后两个图标放大",
 "The biohazard icon and the gas cylinder icon enlarge. No people.",
 "还有生物危害和压缩气体。", None, ["生物危害", "压缩气体"]),
# K3
("K3", "卡车、轮船、飞机图标并排，货箱上贴菱形标签",
 "Icons of a truck, a ship and a plane side by side, each carrying a crate with dangerous goods labels. No people.",
 "为了安全运输，联合国规定了九类。", "联合国规定：运输分九类"),
("K3", "九个格子编号一到九依次亮起",
 "Nine boxes numbered one to nine light up in order. No people.",
 "我们按编号，一类一类看。"),
# K4
("K4", "数字一的格子亮起，里面是爆炸图形的菱形标签",
 "Box number one lights up showing an exploding bomb dangerous goods label. No people.",
 "第 1 类：爆炸品。", "第 1 类：爆炸品", ["第1类 爆炸品"]),
# K5
("K5", "数字二的格子亮起，里面是气瓶和火焰的菱形标签",
 "Box number two lights up showing gas cylinder and flame dangerous goods labels. No people.",
 "第 2 类：气体。", "第 2 类：气体", ["第2类 气体"]),
# K6
("K6", "数字三的格子亮起，里面是火焰菱形标签和溶剂瓶",
 "Box number three lights up showing a flame dangerous goods label and a solvent bottle. No people.",
 "第 3 类：易燃液体。", "第 3 类：易燃液体", ["第3类 易燃液体"]),
# K7
("K7", "数字四的格子亮起，里面是红白条纹火焰标签",
 "Box number four lights up showing a red and white striped flame dangerous goods label. No people.",
 "第 4 类：易燃固体。", "第 4 类：易燃固体", ["第4类"]),
# K8
("K8", "数字五的格子亮起，里面是圆圈上火焰的黄色菱形标签",
 "Box number five lights up showing a yellow flame-over-circle dangerous goods label. No people.",
 "第 5 类：氧化性物质和有机过氧化物。", "第 5 类：氧化性物质和有机过氧化物", ["第5类"]),
# K9
("K9", "数字六的格子亮起，里面是骷髅标签和生物危害标签",
 "Box number six lights up showing a skull dangerous goods label and a biohazard label. No people.",
 "第 6 类：毒性物质和感染性物质。", "第 6 类：毒性物质和感染性物质", ["第6类"]),
("K9", "骷髅图标一侧，生物危害标志一侧",
 "A skull icon on one side and a biohazard symbol on the other. No people.",
 "有毒的化学品，和感染性物质。", None, ["毒性物质", "感染性物质"]),
# K10
("K10", "数字七的格子亮起，里面是三叶形辐射标签",
 "Box number seven lights up showing a radiation trefoil dangerous goods label. No people.",
 "第 7 类：放射性物质。", "第 7 类：放射性物质", ["第7类 放射性"]),
# K11
("K11", "数字八的格子亮起，里面是液滴滴在手和金属上的黑白标签",
 "Box number eight lights up showing a black and white corrosion dangerous goods label with drops on a hand and a metal bar. No people.",
 "第 8 类：腐蚀性物质。", "第 8 类：腐蚀性物质", ["第8类 腐蚀性"]),
# K12
("K12", "数字九的格子亮起，里面是上半黑色竖条的标签",
 "Box number nine lights up showing a dangerous goods label with black vertical stripes on the upper half. No people.",
 "第 9 类：杂项危险物品。", "第 9 类：杂项危险物品", ["第9类 杂项"]),
# K13
("K13", "九个红框菱形象形图排成一圈",
 "Nine GHS hazard pictograms arranged in a circle. No people.",
 "红框菱形象形图，是通用的危害语言。", "象形图：通用的危害图形语言"),
("K13", "象形图分三组：物理、健康、环境",
 "The hazard pictograms are sorted into three groups with a flask icon, a human body icon and a tree icon. No people.",
 "分物理、健康、环境三方面危害。", None, ["物理危险", "健康危害", "环境危害"]),
# 回到情景
# 小结
("小结", "欣欣站在白板前，九个格子依次亮起前四个",
 "The panda mascot stands at a whiteboard where the first four of nine boxes light up.",
 "爆炸品、气体、易燃液体、易燃固体。", "小结", ["1 爆炸品", "2 气体", "3 易燃液体", "4 易燃固体"]),
("小结", "后五个格子亮起",
 "The remaining five boxes light up.",
 "氧化、毒性感染、放射、腐蚀、杂项。", None, ["5 氧化", "6 毒性感染", "7 放射", "8 腐蚀", "9 杂项"]),
("小结", "九个红框象形图排成一圈",
 "Nine red-bordered diamond pictograms arranged in a circle. No people.",
 "红框象形图，一看就懂。"),
("小结", "阿杰对着试剂柜一一认出象形图，小研竖起大拇指",
 "The young male student points to each pictogram on the reagent bottles while the female graduate student gives a thumbs up.",
 "阿杰说：九类加象形图，我记住了！"),
# 结尾
("结尾", "欣欣举起一张象形图卡片，向镜头挥手",
 "The panda mascot holds up a pictogram card and waves goodbye to the camera.",
 "认准标志，分类不乱，再见！"),
]
