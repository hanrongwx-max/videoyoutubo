# 52_What are the main risks of hazardous materials for humans and the environment tr 卡通剧本作者源
# 原片是无人声的文字幻灯片（4.5 分钟）：危险物品对人（烧伤、中毒、呼吸损伤、癌症、感染、死亡）和环境（水土污染、生物蓄积、
# 生态破坏、多样性丧失）的危害，以及安全运输和标识（统一分类标签、菱形标志、包装封装、SDS、培训人员）
# 原著版：完全照原片，K1–K15，无补充知识点；运输与标识照原片“遵循 GHS 和美国职业安全卫生管理局的危害告知标准”、联合国危险类别菱形标志
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "危险物品对人和环境的主要风险",
    "edition": "原著版",
    "points": {
        "K1": "人和环境，都会受伤",
        "K2": "对人：烧伤",
        "K3": "对人：中毒",
        "K4": "对人：伤呼吸道和肺",
        "K5": "对人：致癌等长期危害",
        "K6": "对人：感染",
        "K7": "对人：严重时致命",
        "K8": "对环境：污染水和土壤",
        "K9": "对环境：毒素层层蓄积",
        "K10": "对环境：破坏生态，物种减少",
        "K11": "统一的分类和标签制度",
        "K12": "菱形危险类别标志",
        "K13": "规范包装，可靠封装",
        "K14": "随货附上安全技术说明书",
        "K15": "培训合格的人来操作和应急",
    },
    "avoid": ["Ragba Micro Hub", "Ragba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub",
              "Occupational Safety and Health Administration", "OSHA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一半是实验室、一半是河流草地的背景前，向镜头招手",
 "The panda mascot stands in front of a background that is half laboratory and half river and meadow, waving at the camera.",
 "危险物品伤的不只是人。", "危险物品对人和环境的主要风险"),
("开场", "一个天平，一边是人形图标，一边是地球图标",
 "A balance with a human figure icon on one side and a globe icon on the other. No people.",
 "今天看看，它对人和环境的危害。"),
# 情景
("情景", "阿杰洗完器皿，准备把一烧杯废液倒进水池",
 "The young male student finishes washing glassware and is about to pour a beaker of waste liquid into the sink.",
 "阿杰想把一点废液倒进水池。"),
("情景", "阿杰说话的样子，旁边一个“就一点点”的小手势",
 "The young male student shrugs and pinches his fingers to show a tiny amount.",
 "他说：就一点点，又没碰到手。"),
("情景", "小研拦住阿杰，把烧杯拿开",
 "The female graduate student stops the young male student and takes the beaker away.",
 "小研拦住他：一点点，也会伤人伤环境。"),
# K1
("K1", "两条箭头从一个危险品瓶分别指向人形和河流",
 "Two arrows lead from a hazardous material bottle to a human figure and to a river. No people.",
 "危险物品，对人和环境都有风险。", "人和环境，都会受伤", ["人", "环境"]),
# K2
("K2", "手臂图标上出现红色烫伤痕迹，旁边火焰和腐蚀象形图",
 "A forearm icon with a red burn mark, next to flame and corrosion pictograms. No people.",
 "对人，首先是烧伤。", "对人：烧伤", ["烧伤"]),
# K3
("K3", "骷髅象形图，人形图标脸色发青",
 "The skull pictogram beside a human figure icon looking ill and pale. No people.",
 "第二是中毒。", "对人：中毒", ["中毒"]),
("K3", "鼻子、嘴巴、皮肤三个入口图标",
 "Three entry route icons: a nose, a mouth, and skin on a hand. No people.",
 "毒物经呼吸、嘴巴和皮肤进入身体。", None, ["吸入", "误食", "皮肤"]),
# K4
("K4", "肺部图标里飘进灰色雾气",
 "Grey fumes drift into a lung icon. No people.",
 "第三是伤呼吸道和肺。", "对人：伤呼吸道和肺", ["呼吸损伤"]),
# K5
("K5", "细胞图标慢慢变色，旁边日历翻过很多页",
 "A cell icon slowly changes color as calendar pages flip by. No people.",
 "第四是致癌等长期危害。", "对人：致癌等长期危害", ["致癌"]),
("K5", "人体轮廓上，内部器官图标闪着淡淡的警示色",
 "A human body outline with internal organ icons glowing in a faint warning color. No people.",
 "伤害可能多年后才显现。"),
# K6
("K6", "生物危害标志，微生物图标飘向人形",
 "The biohazard warning sign, with microbe icons drifting toward a human figure. No people.",
 "第五是感染。", "对人：感染", ["感染"]),
# K7
("K7", "心电图线由起伏变成一条直线的图标，红色警示",
 "A heartbeat line icon that flattens into a straight line, with a red alert. No people.",
 "最严重时，会危及生命。", "对人：严重时致命", ["致命"]),
# K8
("K8", "水池下水管通向河流，河水变色",
 "A sink drain pipe leads to a river, and the river water changes color. No people.",
 "对环境：污染水体。", "对环境：污染水和土壤", ["水污染"]),
("K8", "地面渗下的液滴把土壤染色，植物枯黄",
 "Drops seeping into the ground stain the soil and plants turn yellow. No people.",
 "渗进土壤，也很难清除。", None, ["土壤污染"]),
# K9
("K9", "小鱼吃了小点，大鱼吃了小鱼，小点越来越多",
 "A small fish eats tiny dots, a bigger fish eats the small fish, and the dots pile up inside it. No people.",
 "有些毒素，会在生物体内蓄积。", "对环境：毒素层层蓄积", ["生物蓄积"]),
("K9", "食物链最上方是一个人形，体内的小点最多",
 "At the top of the food chain stands a human figure icon holding the most dots. No people.",
 "顺着食物链，最后回到人身上。"),
# K10
("K10", "一片湿地由绿变灰，水鸟飞走",
 "A wetland fades from green to grey as water birds fly away. No people.",
 "生态系统会被破坏。", "对环境：破坏生态，物种减少", ["生态破坏"]),
("K10", "一排动植物图标逐个变淡消失",
 "A row of plant and animal icons fades out one by one. No people.",
 "物种减少，生物多样性下降。", None, ["多样性丧失"]),
# K11
("K11", "地球图标和一本空白标准书，箭头相连",
 "A globe icon connected by an arrow to a blank standard booklet. No people.",
 "怎样安全运输和标识？有统一规则。", "统一的分类和标签制度"),
("K11", "标准书封面上一个红框菱形，旁边一本外文规章书",
 "A blank standard booklet with a red diamond pictogram on the cover next to a blank regulations book. No people.",
 "遵循GHS和美国职安署的危害告知标准。", None, ["GHS", "危害告知标准"]),
# K12
("K12", "货箱上贴着彩色菱形运输标志",
 "A shipping crate with colored dangerous goods labels. No people.",
 "货包贴联合国危险类别菱形标志。", "菱形危险类别标志"),
("K12", "保卫处值班员看到货箱标志，示意绕行",
 "The security officer sees the labels on the crate and gestures others to keep clear.",
 "一眼就知道里面是哪类危险。"),
# K13
("K13", "瓶子装进内层密封袋、吸附垫，再放进坚固外箱",
 "A bottle is sealed in an inner bag with absorbent padding and placed into a sturdy outer box. No people.",
 "包装要合规，封装要可靠。", "规范包装，可靠封装"),
# K14
("K14", "货箱上插着一份空白说明书",
 "A blank safety data sheet is attached to the crate. No people.",
 "随货附上安全技术说明书。", "随货附上安全技术说明书", ["SDS"]),
# K15
("K15", "王老师培训，小研和阿杰听课",
 "The safety administrator leads a training session; the female graduate student and the young male student listen.",
 "操作和搬运，要由培训合格的人来做。", "培训合格的人来操作和应急"),
("K15", "老李拿着溢洒处置箱演示，阿杰跟着做",
 "The facility engineer demonstrates with a spill kit while the young male student practices.",
 "出了状况，懂得怎么应急。"),
# 回到情景
# 小结
("小结", "欣欣站在白板前，左边人形图标周围亮起几个小图标",
 "The panda mascot stands at a whiteboard; small icons light up around a human figure on the left.",
 "对人：烧伤、中毒、伤肺、致癌、感染。", "小结", ["烧伤", "中毒", "伤肺", "致癌", "感染"]),
("小结", "右边地球图标周围亮起几个小图标",
 "Small icons light up around a globe on the right.",
 "对环境：污染、蓄积、破坏生态。", None, ["水土污染", "生物蓄积", "生态破坏"]),
("小结", "标志、包装、说明书、培训四个图标排成一行",
 "Four icons in a row: a diamond label, a package, a document, a trainer.",
 "标志、包装、说明书、培训，缺一不可。", None, ["标志", "包装", "SDS", "培训"]),
# 结尾
("结尾", "欣欣站在清澈的河边，向镜头挥手",
 "The panda mascot stands beside a clear river and waves goodbye to the camera.",
 "护好自己，也护好环境，再见！"),
]
