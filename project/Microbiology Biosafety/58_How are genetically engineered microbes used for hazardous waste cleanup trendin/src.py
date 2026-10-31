# 58_How are genetically engineered microbes used for hazardous waste cleanup trendin 卡通剧本作者源
# 原片为无讲解的文字幻灯片问答：基因工程微生物清理危险废物（三个改造方向、遇砷发光的工程大肠杆菌，与安全相关度低）。保留全部知识点 K1–K6，
# 原著版：完全照原片，K1–K6，无补充知识点（三个改造方向、遇砷发光的工程大肠杆菌、配图中的风险与伦理监管）；硬性底线：不讲任何构建方法和基因细节
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "基因工程微生物如何用于危险废物治理？",
    "edition": "原著版",
    "points": {
        "K1": "改造细菌，清理危险废物",
        "K2": "多产降解酶，分解更快",
        "K3": "耐得住高浓度毒物",
        "K4": "当生物传感器：发现污染就报信",
        "K5": "例子：遇砷发光的工程大肠杆菌",
        "K6": "工程菌的风险：生态、伦理与监管",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "ARH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台前，身旁浮着一个DNA双螺旋和细菌图标",
 "The panda mascot stands at a lab bench beside a floating DNA double helix icon and a bacterium icon, and waves at the camera.",
 "改造过基因的细菌，能帮忙治污。", "工程菌治污：本事大，规矩更大"),
("开场", "欣欣指向一个细菌图标和一个盾牌图标",
 "The panda mascot points to a bacterium icon and a shield icon side by side.",
 "今天讲它的本事，也看它的风险。", "", ["本事", "风险"]),
# 情景
("情景", "阿杰在组会上兴奋地展示一张空白示意图",
 "The young male student excitedly presents a blank diagram at a group meeting.",
 "阿杰读到工程菌治污，很兴奋。"),
("情景", "阿杰头顶冒出一个问号气泡，里面是细菌和废物桶",
 "A thought bubble above the young male student shows a bacterium next to a hazardous waste drum, with a question mark.",
 "他问：细菌到底是怎么改的？"),
("情景", "老周笑着拿起白板笔",
 "The older man smiles and picks up a whiteboard marker.",
 "老周说：主要有三个方向。"),
("情景", "欣欣在空白白板前点头",
 "The panda mascot nods in front of a blank whiteboard.",
 "先看工程菌能做什么。"),
# K1
("K1", "一个细菌图标里，一段DNA被剪刀剪开换上新片段",
 "Inside a bacterium icon, a piece of DNA is snipped by small scissors and a new colored segment is inserted. No people.",
 "科学家改造细菌的基因，", "改造细菌，清理危险废物"),
("K1", "改造后的细菌朝一堆带骷髅象形图的废物桶前进",
 "The modified bacteria move toward a pile of waste drums with skull pictograms. No people.",
 "让它们专门对付危险废物。"),
("K1", "三个空白方框依次出现：剪刀、盾牌、灯泡图标",
 "Three blank boxes appear one by one with icons: scissors, a shield, and a light bulb. No people.",
 "主要往三个方向改。", "", ["降解更快", "耐受毒物", "报信"]),
# K2
("K2", "细菌内部的小工厂图标加速运转，冒出很多酶图标",
 "A tiny factory icon inside a bacterium speeds up and releases many small enzyme icons. No people.",
 "一是让它多产降解酶，", "多产降解酶，分解更快"),
("K2", "污染物分子被大量酶图标快速剪碎，旁边一个快进的时钟",
 "Pollutant molecules are quickly cut apart by many enzyme icons, with a fast-forward clock beside them. No people.",
 "污染物分解得更快。"),
# K3
("K3", "普通细菌在深色毒物液体中萎缩",
 "An ordinary bacterium shrinks and fades in a dark toxic liquid. No people.",
 "二是让它耐得住毒。", "耐得住高浓度毒物"),
("K3", "工程菌在同样的深色液体中依旧精神，外围有盾牌",
 "An engineered bacterium with a small shield around it stays healthy in the same dark toxic liquid. No people.",
 "毒物浓度高，也能活下来干活。"),
# K4
("K4", "细菌图标遇到污染物分子，身上亮起一盏小灯",
 "A bacterium icon touches a pollutant molecule and a small light switches on inside it. No people.",
 "三是把它变成生物传感器，", "当生物传感器：发现污染就报信"),
("K4", "一管水样里亮起点点光，旁边一个铃铛图标",
 "A tube of water sample glows with small dots of light, a bell icon ringing beside it. No people.",
 "一碰到污染物，就发出信号。"),
# K5
("K5", "试管里一团细菌，旁边一个带骷髅象形图的小瓶",
 "A test tube of bacteria next to a small vial with a skull pictogram. No people.",
 "举个例子：工程大肠杆菌，", "例子：遇砷发光的工程大肠杆菌", ["工程大肠杆菌", "砷"]),
("K5", "试管在暗处发出绿色荧光",
 "The test tube glows with green fluorescence in a dark room. No people.",
 "水里有砷，它就发出荧光。"),
("K5", "两支试管对比：一支发光一支不发光",
 "Two test tubes side by side: one glowing green, one dark. No people.",
 "一看亮不亮，就知道有没有砷。"),
# K6
("K6", "一个放大镜照着一株工程菌，旁边三个警示图标",
 "A magnifying glass over an engineered bacterium, with three warning icons nearby. No people.",
 "但工程菌也有风险。", "工程菌的风险：生态、伦理与监管", ["生态破坏", "生物多样性", "环境污染"]),
("K6", "工程菌进入河流，与当地小生物混在一起，打问号",
 "Engineered bacteria drift into a river and mix with local tiny creatures, with question marks above them. No people.",
 "放到野外，可能打乱原有的生态。"),
("K6", "盾牌和天平图标并排",
 "A shield icon and a balance scale icon side by side. No people.",
 "所以必须考虑伦理，接受监管。"),
# 小结
("小结", "欣欣站在三个图标前：酶、盾牌、发光灯泡",
 "The panda mascot stands in front of three icons: an enzyme, a shield and a glowing light bulb.",
 "一起回顾一下。", "小结", ["降解更快", "耐受毒物", "报信"]),
("小结", "发光的试管",
 "A test tube glowing green in the dark. No people.",
 "工程菌还能当传感器，遇砷发光。"),
("小结", "放大镜下的工程菌和三个警示图标，旁边盾牌和天平",
 "A magnifying glass over an engineered bacterium with three warning icons, next to a shield and a balance scale. No people.",
 "也要看风险，考虑伦理和监管。"),
# 结尾
("结尾", "欣欣和阿杰、小研一起挥手告别",
 "The panda mascot waves goodbye together with the young male student and the female graduate student.",
 "本事要用好，风险要看清，下次见！"),
]
