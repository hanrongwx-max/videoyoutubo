# 06 减压阀与背压阀 原著版卡通剧本作者源
# 完全照原片：经销商员工在仓库里单人介绍一个阀门品牌，K1–K6（十九世纪末创立于美国中西部、减压阀与背压阀主要生产商、
# 大流量、低温系列液气两用、内置过滤网易清洁、1/4到2英寸口径和多种弹簧范围、邮箱电话联系），无补充知识点；
# 原片没有产品画面、没有使用和应急内容，剧本同样不加；集团名、品牌名、城市名、联系方式不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "减压阀与背压阀解析",
    "edition": "原著版",
    "points": {
        "K1": "减压阀（调压阀）把上游较高的压力降到下游需要的稳定压力；背压阀则保持上游压力不超过设定值，起稳压、泄压作用",
        "K2": "调压阀要按所需流量选型，流量能力不足会导致下游压力不稳",
        "K3": "低温系统用的调压阀要适用于低温液体或气体工况，不能随便用普通阀代替",
        "K4": "内置过滤网能挡住杂质、保护阀内部件，要定期清洁",
        "K5": "口径和弹簧范围要与应用匹配，选型由专业人员确认",
        "K6": "设备从正规渠道采购，有疑问咨询供应商",
    },
    "avoid": ["EquiTips", "Equi-Tips", "EquiGas", "Equigas", "equigas.net", "Emerson", "Cash Valve", "Ava Kasper",
              "Kasper", "St. Louis", "Missouri", "336", "790-3915"],
}

SHOTS = [
# 开场
("开场", "欣欣站在仓库货架通道里，对着镜头招手",
 "The panda mascot stands in a warehouse aisle between shelves of blue parts bins and waves at the camera.",
 "欢迎来到设备小课堂，我是欣欣。", "减压阀与背压阀的安全使用"),
("开场", "欣欣身旁浮现一只阀门图标和一个盾牌图标",
 "The panda mascot stands beside a floating valve icon and a shield icon.",
 "今天介绍一个调压阀门品牌。"),
# 情景
("情景", "阿杰在仓库里对着货架上一盒盒阀门发愣",
 "The young male student stands in the warehouse staring at boxes of valves on the shelves, looking confused.",
 "阿杰要给实验室订阀门，看花了眼。"),
("情景", "欣欣朝阿杰招手",
 "The panda mascot waves at the young male student to come closer.",
 "别急，听欣欣说说这家有什么特点。"),
# K1
("K1", "老式工厂图标和日历图标，日历停在十九世纪",
 "An old-fashioned factory icon next to a calendar icon showing an old century. No people.",
 "这家集团十九世纪末创立于美国中西部。", "减压阀与背压阀", ["19世纪末创立"]),
("K1", "小工厂图标长成一座大工厂",
 "A small workshop icon growing into a large modern factory icon. No people.",
 "如今已是减压阀和背压阀的主要生产商。"),
("K1", "减压阀示意：高压箭头进、低压稳定箭头出",
 "A diagram of a pressure regulator: a thick high-pressure arrow goes in and a thin steady low-pressure arrow comes out. No people.",
 "减压阀把高压降成稳定的低压。", "", ["高压", "稳定低压"]),
("K1", "背压阀示意：上游压力超过设定值时阀门打开泄出",
 "A diagram of a back pressure valve opening to release flow when upstream pressure rises above a set line. No people.",
 "背压阀让上游压力不超过设定值。", "", ["设定值"]),
# K2
("K2", "欣欣竖起一根手指，身旁浮现粗大的流量箭头",
 "The panda mascot raises one finger, with a thick flow arrow floating beside it.",
 "第一个特点：流量大。", "按流量选调压阀"),
("K2", "两只阀门对比，一只流出粗箭头，另一只流出细箭头",
 "Two valves side by side: one sends out a thick flow arrow, the other only a thin one. No people.",
 "能通过的流量远超其他产品的极限。"),
# K3
("K3", "低温储罐图标旁，一只阀门同时连着液滴和气体云图标",
 "A cryogenic tank icon beside a valve connected to both a liquid drop icon and a gas cloud icon. No people.",
 "第二，多数低温系列液体气体都能用。", "低温工况专用调压阀", ["低温液体", "低温气体"]),
("K3", "雪花图标贴在阀门上，打绿勾",
 "A snowflake icon on a valve body with a green check mark. No people.",
 "低温液体和低温气体工况都适用。"),
# K4
("K4", "调压阀剖面示意，入口处有一片网状过滤网挡住杂质颗粒",
 "A cutaway diagram of a regulator with a mesh strainer at the inlet catching small debris particles. No people.",
 "第三，部分调压阀带内置过滤网。", "内置过滤网保护阀门"),
("K4", "过滤网挡住颗粒，内部弹簧和阀芯完好",
 "The strainer blocks particles while the inner spring and valve plug stay clean and intact. No people.",
 "它能保护阀里的工作部件。"),
("K4", "取出的过滤网被刷子刷干净",
 "A removed mesh strainer being cleaned with a small brush, sparkling afterward. No people.",
 "而且过滤网很容易清洁。"),
# K5
("K5", "一排从小到大的阀门，最小和最大分别标着尺寸",
 "A row of valves from small to large, the smallest and largest marked with size arrows. No people.",
 "第四，口径范围宽。", "口径和弹簧范围要匹配", ["1/4英寸", "2英寸"]),
("K5", "欣欣指着从小到大的阀门",
 "The panda mascot points along the row of valves from small to large.",
 "从四分之一英寸到两英寸都有。"),
("K5", "几根粗细不同的弹簧排成一排",
 "Several springs of different thickness lined up in a row. No people.",
 "还配有多种弹簧范围，"),
("K5", "不同阀门对应实验室、工厂、储罐三个场景",
 "Different valves matched by lines to three scenes: a laboratory, a factory and a storage tank. No people.",
 "能适应各种不同的应用。"),
# K6
("K6", "欣欣指向下方的空白信息条，有信封和电话图标",
 "The panda mascot points down to a blank info bar with an envelope icon and a telephone icon.",
 "想了解更多，发邮件或打电话联系我们。", "从正规渠道采购"),
("K6", "欣欣挥手，旁边日历翻到下个月",
 "The panda mascot waves, with a calendar beside it flipping to the next month.",
 "我们下个月再见。"),
# 小结
("小结", "减压阀和背压阀两个图标",
 "Icons of a pressure regulator and a back pressure valve side by side.",
 "减压阀降压稳压，背压阀守住上游。", "小结"),
("小结", "大流量、雪花、过滤网、弹簧四个图标",
 "Four icons: a thick flow arrow, a snowflake, a mesh strainer and a spring. No people.",
 "大流量、液气两用、过滤网、口径多。"),
("小结", "阿杰对照清单在货架上挑出阀门",
 "The young male student checks a blank list and picks a valve from the shelf.",
 "阿杰心里有数，挑好了阀门。"),
# 结尾
("结尾", "欣欣在仓库货架前挥手道别",
 "The panda mascot waves goodbye in front of the warehouse shelves.",
 "今天的设备小课堂就到这里，下次见！"),
]
