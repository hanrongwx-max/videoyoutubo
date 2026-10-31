# 04 低温截止阀 原著版卡通剧本作者源
# 完全照原片：阀门厂车间里的推广访谈，K1–K7（低温截止阀与三处工厂、十多年系列和最大3英寸口径及多种端部连接、
# 弹簧加载冷密封填料、锥形阀座、一体式阀座、人体工学手轮、经销商购买），无补充知识点；
# 车间内两人戴护目镜、装配工戴手套照原片；品牌、工厂所在地、人名、电话不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "低温截止阀解析",
    "edition": "原著版",
    "points": {
        "K1": "低温截止阀是液氮、液氧、液氩等低温储罐和管路上用来开关、调节液体或气体的阀门，专门工厂制造",
        "K2": "低温阀门有多种口径和端部连接方式，要按管路选用",
        "K3": "填料（阀杆密封）在低温下容易收缩泄漏，弹簧加载的冷密封填料能自动补偿，保持密封",
        "K4": "锥形阀座等设计减少维护、减少停机",
        "K5": "阀门需要维护；结构简单、便于拆装的阀座可以让维修更快、更少出错",
        "K6": "手轮要便于操作人员转动，避免用力过猛或借助加力工具",
        "K7": "阀门应通过正规渠道采购",
    },
    "avoid": ["EquiTips", "Equi-Tips", "EquiGas", "Equigas", "Ecogas", "RegO", "Rego", "REGO", "SK Series",
              "SK Advantage", "OPW", "Dover", "Emily Harrel", "Harrel", "Harrell", "Nico Arvelo", "Arvelo",
              "Allentown", "Tampa", "Elon", "Elan", "North Carolina", "844"],
}

SHOTS = [
# 开场
("开场", "欣欣戴着护目镜站在阀门厂车间的货架前，向镜头招手",
 "The panda mascot wearing safety glasses stands in front of shelves in a valve factory workshop and waves at the camera.",
 "欢迎来到设备小课堂，今天在阀门厂。", "低温截止阀解析"),
("开场", "小研戴着护目镜走进画面，和欣欣并肩站立",
 "The female graduate student wearing safety glasses walks into the frame and stands beside the panda mascot.",
 "嘉宾小研，是厂家的产品管理总监。"),
# 情景
("情景", "阿杰站在一个白色低温储罐下，看着管路上的蓝色手轮阀门",
 "The young male student stands below a white cryogenic storage tank, looking up at blue handwheel valves on its piping.",
 "阿杰常看见储罐管路上的蓝手轮阀门。"),
("情景", "阿杰挠头，头顶冒出一个问号",
 "The young male student scratches his head with a question mark above him.",
 "这些阀门有什么门道？一起来听听。"),
# K1
("K1", "小研指向身后车间，旁边浮现三个工厂图标",
 "The female graduate student points to the workshop behind her, with three small factory icons floating beside her.",
 "小研说，他们有三处低温产品工厂。", "低温截止阀"),
("K1", "欣欣双手举起一只蓝色手轮的不锈钢截止阀",
 "The panda mascot holds up a stainless steel globe valve with a blue handwheel in both hands.",
 "欣欣手里这只，就是低温截止阀。"),
("K1", "低温储罐和管路示意图，截止阀装在出液管上",
 "A diagram of a cryogenic storage tank and its piping, with globe valves on the liquid and gas lines. No people.",
 "用在液氮、液氧、液氩储罐和管路上。", "", ["液氮", "液氧", "液氩"]),
("K1", "阀门打开和关闭两个状态的图标",
 "Two icons of the same valve, one open with flow arrows and one closed with no flow. No people.",
 "用来开关和调节液体或气体。"),
("K1", "小研竖起大拇指，阀门旁浮现一枚奖章图标",
 "The female graduate student gives a thumbs up, with a medal icon floating next to the valve.",
 "她说这个系列是市场上最好的。"),
# K2
("K2", "日历图标翻过十几页",
 "A calendar icon flipping through more than ten pages. No people.",
 "这个系列已经做了十多年。", "多种口径和端部连接"),
("K2", "从小到大一排截止阀，最大的标着三英寸",
 "A row of globe valves from small to large, the largest marked with a size arrow. No people.",
 "现在新增了大口径，最大到三英寸。", "", ["最大3英寸"]),
("K2", "焊接、螺纹、法兰三种端部连接图标",
 "Three icons of valve end connections: a welded end, a threaded end and a flanged end. No people.",
 "还有不同的端部连接方式可选。"),
# K3
("K3", "装配线上戴蓝手套的手在夹具上组装一排阀体",
 "On an assembly line, hands in blue gloves assemble a row of brass valve bodies on fixtures, with a red parts bag nearby.",
 "第一个优点：弹簧加载的冷密封填料。", "弹簧加载的冷密封填料"),
("K3", "阀杆填料剖面示意：低温收缩，弹簧把填料压紧",
 "A cutaway diagram of a valve stem packing: packing shrinks in the cold and a spring pushes it tight again. No people.",
 "低温下填料收缩，弹簧会把它压紧。", "", ["填料", "弹簧"]),
# K4
("K4", "锥形阀座剖面示意，阀芯严丝合缝落在锥面上",
 "A cutaway diagram of a conical valve seat with the plug fitting snugly into the cone. No people.",
 "第二个优点：锥形阀座设计。", "锥形阀座减少维护"),
("K4", "扳手图标变小，时钟图标变大",
 "A wrench icon shrinking while a running clock icon grows larger. No people.",
 "维护少了，运行时间就长了。", "", ["少维护", "多运行"]),
# K5
("K5", "老李在工作台上拆开一只截止阀，取出阀座",
 "The facility engineer opens a globe valve on a workbench and lifts out its seat in one piece.",
 "真要维护时，一体式阀座拆装方便。", "便于拆装的阀座"),
("K5", "秒表图标和一个整块阀座图标",
 "A stopwatch icon next to a one-piece valve seat icon. No people.",
 "维修又简单又快。"),
# K6
("K6", "老李在储罐旁轻松转动蓝色手轮",
 "The facility engineer easily turns a blue handwheel on a valve beside a cryogenic tank.",
 "第三个优点：人体工学手轮。", "手轮便于操作人员转动"),
("K6", "手轮特写，握把弧度贴合手掌",
 "Close-up of an ergonomic handwheel with grips shaped to fit a hand. No people.",
 "现场操作人员转起来很轻松。"),
# K7
("K7", "欣欣问去哪里买，小研指向一个空白经销商标牌",
 "The panda mascot asks where to buy, and the female graduate student points to a blank distributor sign.",
 "去哪里买？找当地的经销商。", "从正规渠道采购"),
("K7", "电话图标和空白号码条",
 "A telephone icon next to a blank number bar. No people.",
 "欣欣报出了经销商的订购电话。"),
# 小结
("小结", "截止阀、口径、连接方式三个图标",
 "Three icons: a globe valve, a size arrow and three end connection types.",
 "低温截止阀，口径连接多样可选。", "小结"),
("小结", "填料弹簧、锥形阀座、一体阀座、手轮四个图标",
 "Four icons: a spring-loaded packing, a conical seat, a one-piece seat and an ergonomic handwheel. No people.",
 "冷密封填料、锥形阀座、好拆、好转。"),
# 结尾
("结尾", "欣欣和小研戴着护目镜在车间里挥手道别",
 "The panda mascot and the female graduate student, both wearing safety glasses, wave goodbye in the workshop.",
 "今天的设备小课堂就到这里，下次见！"),
]
