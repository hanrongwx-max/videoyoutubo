# 09 气瓶阀 原著版卡通剧本作者源
# 完全照原片：经销商栏目第一期，员工在仓库里单人介绍一个气瓶阀品牌，K1–K6（俄亥俄州生产、美国制造、100%测试、
# 统一化设计降低泄漏、三个部件按正确工序装配、符合美国压缩气体协会的气瓶阀标准、自动化测试确认关闭力矩、
# 打电话当天发货），无补充知识点；原片没有使用、搬运和应急内容，剧本同样不加；品牌、主持人姓名、电话不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "气瓶阀解析",
    "edition": "原著版",
    "points": {
        "K1": "气瓶阀是气瓶上控制气体进出的关键安全部件，出厂应逐只测试",
        "K2": "统一、规范的结构设计保证正确装配，可降低泄漏",
        "K3": "气瓶阀由多个部件组成，必须按正确工序装配才能正常工作——装配和维修只能由专业单位进行",
        "K4": "气瓶阀要符合气瓶阀的设计和运行标准",
        "K5": "关闭要可靠：出厂测试确认关闭力矩，防止阀门意外打开",
        "K6": "设备从正规渠道采购",
    },
    "avoid": ["EquiTips", "Equi-Tips", "EquiTip", "EquiGas", "Equigas", "Sherwood", "Sherwood Valves", "Ava Krosper",
              "Ava Casper", "Ohio", "CGA", "V9", "V-9", "336", "790-3915", "Made in USA", "Made in the USA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在仓库货架前，向镜头招手",
 "The panda mascot stands in front of warehouse shelves of parts bins and waves at the camera.",
 "欢迎来到设备小课堂第一期！", "气瓶阀解析"),
("开场", "一只黄铜气瓶阀图标，旁边一张地图上标出一个州",
 "A brass gas cylinder valve icon next to a simple map with one state highlighted. No people.",
 "今天介绍一家俄亥俄州的气瓶阀厂家。", "", ["美国制造"]),
# 情景
("情景", "阿杰站在一排气瓶前，盯着瓶顶的黄铜阀门",
 "The young male student stands in front of a row of gas cylinders, staring at the brass valves on top.",
 "阿杰每天开关气瓶阀，却没细想过它。"),
("情景", "阿杰挠头，头顶冒出一个问号",
 "The young male student scratches his head with a question mark above him.",
 "一个好的气瓶阀，要做到什么？"),
# K1
("K1", "气瓶顶部的阀门特写，气体进出的箭头",
 "Close-up of the valve on top of a gas cylinder with arrows showing gas flowing in and out. No people.",
 "气瓶阀管着气体的进和出。", "出厂逐只测试"),
("K1", "一排阀门依次通过测试台，每只都打绿勾",
 "A row of cylinder valves passing one by one over a test bench, each getting a green check mark. No people.",
 "这家的阀门百分之百都经过测试，", "", ["100%测试"]),
("K1", "盾牌图标罩住一只气瓶阀",
 "A shield icon covering a cylinder valve. No people.",
 "用来保证安全。"),
# K2
("K2", "几只阀门外形和接口完全一致，拼成一套",
 "Several valves with identical shapes and matching ports fitting together into one unified set. No people.",
 "阀门按统一化的体系设计，", "统一设计，降低泄漏"),
("K2", "零件严丝合缝装在一起，泄漏气流图标被划掉",
 "Parts fitting together snugly while a small gas leak puff icon is crossed out. No people.",
 "保证装配正确，降低泄漏率。"),
# K3
("K3", "阀体、阀杆、手轮三个部件分开摆放",
 "Three valve parts laid out separately: a valve body, a stem and a handwheel. No people.",
 "阀门由三个部件组成，", "按正确工序装配", ["阀体", "阀杆", "手轮"]),
("K3", "三个部件按一二三的顺序依次装到一起",
 "The three parts are assembled in order one, two, three with numbered arrows. No people.",
 "必须在正确的时机按工序装配，"),
("K3", "装好的阀门安装到气瓶上，开关自如",
 "The assembled valve is fitted onto a cylinder and its handwheel turns smoothly. No people.",
 "才能正确安装、正常工作。"),
# K4
("K4", "一本空白标准手册，带星条小旗图标",
 "A blank standard book with a small striped flag icon. No people.",
 "阀门符合美国压缩气体协会的阀门标准。", "符合气瓶阀标准"),
("K4", "设计图纸和运行齿轮两个图标，都打绿勾",
 "A blueprint icon and a turning gear icon, both with green check marks. No people.",
 "这对设计和运行要求都极其重要。", "", ["设计要求", "运行要求"]),
# K5
("K5", "自动化测试设备拧紧阀门手轮，旁边是力矩表图标",
 "An automated test machine turns a valve handwheel closed, with a torque gauge icon beside it. No people.",
 "还有自动化测试来确认关闭力矩，", "关闭可靠，防意外打开"),
("K5", "关紧的阀门上，气流箭头被挡住",
 "A tightly closed valve with a gas flow arrow blocked at the seat. No people.",
 "确保阀门关得严，"),
("K5", "阀门意外打开的图标被红叉划掉",
 "An icon of a valve accidentally opening by itself, crossed out with a red X. No people.",
 "防止意外打开，品质过硬。"),
# K6
("K6", "欣欣指向下方的空白电话条",
 "The panda mascot points down to a blank bar with a telephone icon.",
 "想订购，就拨打下方的电话。", "从正规渠道采购"),
("K6", "电话图标和一辆当天出发的送货车",
 "A telephone icon next to a delivery truck leaving with a sun icon above it. No people.",
 "我们接电话，当天就发货。", "", ["当天发货"]),
# 小结
("小结", "测试台、统一设计、三部件三个图标",
 "Three icons: a test bench with a check mark, a unified valve set and three valve parts.",
 "逐只测试，统一设计，按工序装配。", "小结"),
("小结", "标准手册和关紧的阀门两个图标",
 "Two icons: a blank standard book and a tightly closed valve. No people.",
 "符合阀门标准，关得严不意外打开。"),
("小结", "阿杰拍拍气瓶阀，点头微笑",
 "The young male student pats a cylinder valve and nods with a smile.",
 "阿杰说：小小瓶阀，学问不少。"),
("小结", "欣欣挥手，旁边日历翻页",
 "The panda mascot waves next to a calendar flipping a page.",
 "这就是第一期的内容。"),
# 结尾
("结尾", "欣欣在仓库货架前挥手道别",
 "The panda mascot waves goodbye in front of the warehouse shelves.",
 "今天的设备小课堂就到这里，下次见！"),
]
