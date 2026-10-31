# 05 空温式汽化器 原著版卡通剧本作者源
# 完全照原片：汽化器工厂露天堆场的一分钟推广访谈，K1–K5（领先的空温式汽化器、约20个型号可定制、医院到充装站、
# 氮氧氩二氧化碳液化天然气专用、经销商购买），无补充知识点；两人只戴安全帽照原片；品牌、人名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "空温式汽化器与储罐站安全",
    "edition": "原著版",
    "points": {
        "K1": "空温式汽化器利用环境空气的热量，通过铝翅片管把低温液体（液氮、液氧等）汽化成常温气体供用户使用",
        "K2": "汽化器有多种型号，应按用气量和工况由专业人员选型，必要时定制",
        "K3": "应用场所广泛：医院、气体充装站、工厂、学校的供气站等",
        "K4": "不同介质有专用设备：氮气、氧气、氩气、二氧化碳、液化天然气等，氧气设备有特殊要求",
        "K5": "设备应从正规渠道采购",
    },
    "avoid": ["EquiTips", "Equi-Tips", "Acme Tips", "EquiGas", "Equigas", "echo gas", "FinnCo", "Finco", "FIBA",
              "FIBA Technologies", "Ethan Houston", "Houston", "Niko Avelo", "Nico Arvelo", "Arvelo", "844"],
}

SHOTS = [
# 开场
("开场", "欣欣戴着红色安全帽，站在露天堆场里成排横放的铝翅片汽化器前，向镜头招手",
 "The panda mascot wearing a red hard hat stands in an outdoor yard in front of rows of aluminum finned vaporizers lying on their sides, and waves at the camera.",
 "欢迎来到设备小课堂，今天在汽化器厂。", "空温式汽化器与储罐站安全"),
("开场", "老李戴着白色安全帽走进画面，和欣欣并肩站立",
 "The facility engineer wearing a white hard hat walks into the frame and stands beside the panda mascot.",
 "嘉宾老李，是这家工厂的厂长。"),
# 情景
("情景", "阿杰路过校园储罐站，看见立式储罐旁一排银色翅片柱子",
 "The young male student walks past a campus gas storage station and sees tall silver finned columns beside a vertical tank.",
 "阿杰常在储罐站看到这些银色翅片柱。"),
("情景", "阿杰挠头，头顶冒出一个问号",
 "The young male student scratches his head with a question mark above him.",
 "它们是干什么用的？一起来问问。"),
# K1
("K1", "老李拍拍身后的翅片汽化器，旁边浮现奖杯图标",
 "The facility engineer pats a finned vaporizer behind him, with a trophy icon floating beside him.",
 "老李说，他们是空温式汽化器的领先厂家。", "空温式汽化器"),
("K1", "星形铝翅片管的截面示意图",
 "A cross-section diagram of a star-shaped aluminum finned tube. No people.",
 "汽化器由一根根铝翅片管组成。"),
("K1", "低温液体从底部进入，周围空气的热量箭头传入翅片",
 "A diagram: cold liquid enters the finned tubes at the bottom while heat arrows from the surrounding air flow into the fins. No people.",
 "靠周围空气的热量，加热管里的低温液体。"),
("K1", "液体在管内逐渐变成气体，从顶部出口流出",
 "A diagram of liquid gradually turning into gas inside the tubes and flowing out of the top outlet. No people.",
 "液体变成常温气体，再送给用户。", "", ["低温液体", "常温气体"]),
# K2
("K2", "一排大小不同的汽化器图标，上方浮现数字二十",
 "A row of vaporizer icons of different sizes, with a large number twenty floating above. No people.",
 "他们大约有二十个型号。", "多种型号，可以定制", ["约20个型号"]),
("K2", "工程师在图纸上调整汽化器的尺寸",
 "An engineer adjusts the size of a vaporizer on a blank blueprint at a drafting desk.",
 "工程部门很专业，"),
("K2", "图纸上的汽化器按需求拉长、加宽",
 "A vaporizer drawing on a blueprint stretches taller and wider to fit a customer request. No people.",
 "任何机组都能按你的需要定制。"),
# K3
("K3", "欣欣问哪里会用到，老李张开双手",
 "The panda mascot asks where they are used, and the facility engineer spreads his arms wide.",
 "哪里能看到它们？到处都有。", "应用场所广泛"),
("K3", "医院图标和带红十字的储罐",
 "A hospital icon next to a storage tank with a red cross. No people.",
 "小到医院，", "", ["医院"]),
("K3", "气瓶充装站图标，成排气瓶",
 "A cylinder filling station icon with rows of gas cylinders. No people.",
 "大到气体充装站。", "", ["充装站"]),
# K4
("K4", "老李竖起两根手指",
 "The facility engineer raises two fingers while explaining.",
 "有氮气专用的，也有氧气专用的。", "不同介质有专用设备"),
("K4", "五个储罐图标，各带一个分子图标",
 "Five storage tank icons, each with a different simple molecule icon above. No people.",
 "氧、氮、氩、二氧化碳、液化天然气。", "", ["氧气", "氮气", "氩气", "二氧化碳", "液化天然气"]),
("K4", "五台汽化器各连一个对应颜色的储罐",
 "Five vaporizers, each connected by a line to a matching colored storage tank. No people.",
 "不同的气体，配不同的机型。"),
# K5
("K5", "欣欣问去哪里买，老李指向一个空白经销商标牌",
 "The panda mascot asks where to buy, and the facility engineer points to a blank distributor sign.",
 "想要汽化器，去哪里买？", "从正规渠道采购"),
("K5", "老李笑着点头，电话图标和空白号码条",
 "The facility engineer smiles and nods next to a telephone icon and a blank number bar.",
 "老李说：联系我们合作的经销商。"),
# 小结
("小结", "翅片管、空气热量箭头、气体出口三个图标",
 "Three icons: a finned tube, air heat arrows and a gas outlet.",
 "空温式汽化器，用空气把液体变成气。", "小结"),
("小结", "二十个型号、定制图纸两个图标",
 "Two icons: a row of vaporizer models and a blank blueprint. No people.",
 "约二十个型号，还能按需定制。"),
("小结", "医院、充装站和五种气体图标",
 "Icons of a hospital, a filling station and five gas molecules. No people.",
 "医院到充装站，多种气体都有专用。"),
("小结", "欣欣指向电话图标",
 "The panda mascot points to a telephone icon.",
 "需要的话，找经销商就行。"),
# 结尾
("结尾", "欣欣和老李戴着安全帽在汽化器堆场挥手道别",
 "The panda mascot and the facility engineer, both in hard hats, wave goodbye in the vaporizer yard.",
 "今天的设备小课堂就到这里，下次见！"),
]
