# 07 高压阀门与接头 原著版卡通剧本作者源
# 完全照原片：经销商员工在仓库里单人介绍一个高压阀门品牌，K1–K8（1915年创立于宾夕法尼亚州、服役30年以上、
# 美国航天机构和海军在用、按美国压缩气体协会和材料试验标准清洗测试包装、氧气冲击测试、手柄高压下易转、
# 最高工作压力惰性气体7800磅/平方英寸与氧气6000磅/平方英寸（旁白用中文数字）、管螺纹O形圈和焊接连接、邮箱电话联系），
# 无补充知识点；品牌、主持人姓名、联系方式不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "高压阀门与接头解析",
    "edition": "原著版",
    "points": {
        "K1": "高压阀门和接头用于高压气瓶、汇流排和高压气体管路，必须使用专门的高压产品",
        "K2": "质量可靠的阀门可以长期服役，但仍需定期检查",
        "K3": "阀门出厂要经过清洗、测试和包装，特别是氧气用阀门必须达到禁油清洁要求",
        "K4": "氧气用阀门的设计要经过氧气冲击（绝热压缩）测试，因为高压氧快速冲入会发热引燃",
        "K5": "手柄设计要便于在高压下平稳转动，操作时不需要也不应借助加力工具",
        "K6": "阀门有额定工作压力，同一阀门用于氧气时的允许压力低于惰性气体，必须按介质和额定值使用",
        "K7": "连接方式（管螺纹、O 形圈密封、焊接）要与系统匹配",
        "K8": "设备从正规渠道采购，有疑问咨询供应商",
    },
    "avoid": ["EquiTips", "Equi-Tips", "Equi-tip", "EquiGas", "Equigas", "CPV", "CPV Manufacturing", "Ava Casper",
              "Casper", "Kennett Square", "Kennon Square", "NASA", "Navy", "CGA", "ASTM", "PSI", "7800", "6000",
              "Made in USA", "Made in the USA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在仓库货架通道里，手按胸口对镜头打招呼",
 "The panda mascot stands in a warehouse aisle between shelves of parts bins, hand on chest, greeting the camera.",
 "欢迎来到设备小课堂，我是欣欣。", "高压阀门与接头解析"),
("开场", "一只黄铜高压主阀，黑色十字手柄",
 "A brass high-pressure master valve with a black cross-shaped handle on a plain background. No people.",
 "今天介绍一家高压阀门和接头厂家。"),
# 情景
("情景", "阿杰站在气瓶汇流排前，看着墙上一排黄铜高压阀门",
 "The young male student stands in front of a gas cylinder manifold, looking at a row of brass high-pressure valves on the wall.",
 "阿杰第一次见到这么多高压阀门。"),
("情景", "阿杰挠头，头顶冒出一个问号",
 "The young male student scratches his head with a question mark above him.",
 "高压阀门有什么讲究？听欣欣说。"),
# K1
("K1", "老式工厂图标和日历图标，旁边一张地图上标出一个州",
 "An old factory icon, a calendar icon and a simple map with one state highlighted. No people.",
 "这家公司1915年创立于宾夕法尼亚州。", "高压阀门和接头", ["1915年"]),
("K1", "高压气瓶、汇流排、高压管路三个图标",
 "Three icons: a high-pressure gas cylinder, a cylinder manifold and a high-pressure gas line. No people.",
 "是高压阀门和接头的主要厂商之一。"),
# K2
("K2", "一只阀门旁日历翻过三十多页",
 "A valve icon beside a calendar flipping through more than thirty pages. No people.",
 "他们多数阀门和接头已服役三十多年。", "可以长期服役", ["30年以上"]),
("K2", "火箭图标和军舰图标",
 "A rocket icon and a gray warship icon side by side. No people.",
 "部分产品用于美国航天机构和海军。"),
# K3
("K3", "阀门在清洗槽中冲洗，随后放到测试台上",
 "A valve is rinsed in a cleaning bath, then placed on a pressure test bench. No people.",
 "所有阀门都经过清洗、测试和包装，", "出厂清洗、测试、包装", ["清洗", "测试", "包装"]),
("K3", "两本空白标准手册，带星条小旗图标",
 "Two blank standard books, each with a small striped flag icon. No people.",
 "按美国压缩气体协会和材料试验标准。"),
("K3", "密封袋包好的洁净阀门",
 "A clean valve sealed in a clear plastic bag with a blank tag. No people.",
 "包装好再出厂，保持洁净。"),
# K4
("K4", "氧气冲入阀门的箭头示意，测试仪在旁监测",
 "A diagram of oxygen surging rapidly into a valve while a test rig monitors it. No people.",
 "每一种设计，都通过了氧气冲击测试。", "氧气冲击测试"),
("K4", "测试台上的阀门旁打绿勾",
 "A valve on a test bench with a green check mark beside it. No people.",
 "经过测试认可，才拿来用在氧气上。"),
# K5
("K5", "人体工学手柄特写，握把贴合手掌",
 "Close-up of an ergonomic valve handle shaped to fit a hand. No people.",
 "阀门配人体工学手柄，", "手柄高压下平稳转动"),
("K5", "老李在汇流排前轻松转动阀门手柄",
 "The facility engineer easily turns a valve handle on the cylinder manifold.",
 "就算在高压下，也非常容易转动。"),
# K6
("K6", "压力表图标和两个气体图标：惰性气体和氧气",
 "A blank pressure gauge icon next to two gas icons, one for inert gas and one for oxygen. No people.",
 "最高工作压力，看用的是什么气体。", "按介质和额定压力使用"),
("K6", "惰性气体图标旁一根较高的柱子",
 "An inert gas icon beside a tall pressure bar. No people.",
 "惰性气体是七千八百磅每平方英寸。", "", ["惰性气体"]),
("K6", "氧气图标旁一根稍矮的柱子",
 "An oxygen icon beside a shorter pressure bar. No people.",
 "氧气是六千磅每平方英寸。", "", ["氧气"]),
# K7
("K7", "管螺纹、O形圈、焊缝三种连接图标",
 "Three connection icons: a pipe thread, an O-ring seal and a weld seam. No people.",
 "连接方式有管螺纹、O形圈密封和焊接。", "连接方式要与系统匹配", ["管螺纹", "O形圈", "焊接"]),
# K8
("K8", "欣欣站在货架前竖起大拇指",
 "The panda mascot stands in front of the shelves and gives a thumbs up.",
 "这就是这家厂家安全又与众不同之处。", "从正规渠道采购"),
("K8", "欣欣指向下方的空白信息条，有信封和电话图标",
 "The panda mascot points down to a blank info bar with an envelope icon and a telephone icon.",
 "想了解更多，发邮件或打电话联系我们。"),
("K8", "欣欣挥手，旁边日历翻到下个月",
 "The panda mascot waves, with a calendar beside it flipping to the next month.",
 "我们下个月再见。"),
# 小结
("小结", "高压阀门、三十年日历、清洗测试包装三个图标",
 "Three icons: a high-pressure valve, a calendar marked thirty years and a sealed clean package.",
 "高压阀门耐用，出厂清洗测试包装。", "小结"),
("小结", "氧气冲击、手柄、压力柱、连接方式四个图标",
 "Four icons: an oxygen surge arrow, an ergonomic handle, two pressure bars and connection types. No people.",
 "氧气冲击测试，手柄好转，按气体限压。"),
# 结尾
("结尾", "欣欣在仓库货架前挥手道别",
 "The panda mascot waves goodbye in front of the warehouse shelves.",
 "今天的设备小课堂就到这里，下次见！"),
]
