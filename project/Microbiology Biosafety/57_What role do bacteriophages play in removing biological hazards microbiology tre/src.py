# 57_What role do bacteriophages play in removing biological hazards microbiology tre 卡通剧本作者源
# 原片为无讲解的文字幻灯片问答：噬菌体清除致病菌、微生物间接中和酸碱废水、生物滤池去除有毒气体（与安全相关度低）。保留全部知识点 K1–K7
# 原著版：完全照原片，K1–K7，无补充知识点；K4 照原片说嗜酸菌“把硫酸转化为单质硫”（原片说法，不更正）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "噬菌体在清除生物危害中的作用",
    "edition": "原著版",
    "points": {
        "K1": "噬菌体：专杀特定细菌的病毒",
        "K2": "精准清除污水和医院里的致病菌",
        "K3": "微生物能间接中和强酸强碱",
        "K4": "嗜酸菌：把硫酸变成单质硫",
        "K5": "嗜碱菌：产有机酸，把碱降下来",
        "K6": "生物滤池：微生物把有毒气体当食物",
        "K7": "去氨、去硫化氢的两种菌",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "ARH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在污水处理池模型旁，身旁浮着一个噬菌体图标",
 "The panda mascot stands beside a model of a wastewater treatment tank, a floating bacteriophage icon with a head and spider-like legs beside it, and waves at the camera.",
 "有一种病毒，专门帮我们杀细菌。", "噬菌体在清除生物危害中的作用"),
("开场", "欣欣指向三个图标：噬菌体、酸碱试纸、烟囱",
 "The panda mascot points to three floating icons: a bacteriophage, a pH test strip, and a chimney with fumes.",
 "还有微生物能对付酸碱和臭气。", "", ["噬菌体", "酸碱废水", "有毒气体"]),
# 情景
("情景", "阿杰拿着一瓶浑浊的污水样，准备倒进培养瓶",
 "The young male student holds a bottle of murky wastewater sample with a blank label at an open bench, about to pour it.",
 "阿杰想从污水里分离噬菌体。"),
("情景", "阿杰看着污水样，头顶冒出问号",
 "The young male student looks at the cloudy water sample with a question mark above his head.",
 "他问：病毒也能帮忙治污？"),
("情景", "欣欣在空白白板前点头",
 "The panda mascot nods in front of a blank whiteboard.",
 "分三道题，一起看看。"),
# K1
("K1", "噬菌体落在一个杆菌表面，把尾巴扎进去",
 "A bacteriophage lands on the surface of a rod-shaped bacterium and pushes its tail into it. No people.",
 "噬菌体，是感染细菌的病毒。", "噬菌体：专杀特定细菌的病毒"),
("K1", "细菌里冒出许多小噬菌体，细菌破裂",
 "Many small bacteriophages form inside the bacterium, which then bursts open. No people.",
 "它在细菌里复制，再把细菌撑破。"),
("K1", "噬菌体只停在一种颜色的细菌上，别的颜色不碰",
 "Bacteriophages land only on bacteria of one color and ignore bacteria of other colors. No people.",
 "而且只认特定的细菌。"),
# K2
("K2", "污水池里，噬菌体围住带红色警示的致病菌",
 "In a wastewater tank, bacteriophages surround bacteria marked with small red warning dots. No people.",
 "在污水里，它能盯住致病菌，", "精准清除污水和医院里的致病菌"),
("K2", "医院建筑图标旁，带红点的细菌被噬菌体消灭",
 "Beside a hospital building icon, bacteria with red warning dots are destroyed by bacteriophages. No people.",
 "医院环境里，也能派上用场。", "", ["污水", "医院"]),
("K2", "绿色的有益菌安然无恙，旁边绿色对勾",
 "Green beneficial bacteria remain untouched, with a green check mark beside them. No people.",
 "有益的微生物，它不伤害。"),
# K3
("K3", "工厂排水管流出两股水，一股带酸象形图，一股带碱",
 "A factory drain releases two streams, each marked with a corrosive pictogram. No people.",
 "工业废水，常常酸碱很强。", "微生物能间接中和强酸强碱", ["强酸", "强碱"]),
("K3", "微生物不直接碰酸碱，而是放出小分子改变水质",
 "Microbes in the water release small molecules that slowly change the water color toward neutral green. No people.",
 "微生物能帮忙，但是间接的。"),
# K4
("K4", "酸性的红色水里，一群细菌照样活跃",
 "In red acidic water, a group of bacteria stays lively and active. No people.",
 "嗜酸菌，比如酸硫杆菌，", "嗜酸菌：把硫酸变成单质硫", ["嗜酸菌", "酸硫杆菌"]),
("K4", "细菌周围的酸性液体里析出黄色的硫颗粒",
 "Yellow sulfur particles appear and change around the bacteria. No people.",
 "在酸性废物里生长，把硫酸变成单质硫。"),
# K5
("K5", "蓝紫色的碱性水里，杆菌活跃",
 "In blue-purple alkaline water, rod-shaped bacteria are active. No people.",
 "嗜碱菌，比如耐盐芽孢杆菌，", "嗜碱菌：产有机酸，把碱降下来", ["嗜碱菌", "耐盐芽孢杆菌"]),
("K5", "细菌放出小酸滴，水色从蓝紫变成绿色",
 "The bacteria release small acid droplets and the water color changes from blue-purple to green. No people.",
 "会产生有机酸，把碱性废水的pH降下来。"),
# K6
("K6", "生物滤池剖面：一层层滤料，表面长满细菌膜",
 "A cutaway of a biofilter tower: layers of packing material whose surfaces are covered with bacterial film. No people.",
 "生物滤池和生物反应器，", "生物滤池：微生物把有毒气体当食物"),
("K6", "带骷髅象形图的臭气从底部进入，向上穿过滤料",
 "Smelly gas with a skull pictogram enters from the bottom and rises through the packing layers. No people.",
 "让有毒气体从滤料中间穿过，", "", ["氨", "硫化氢", "挥发性有机物"]),
("K6", "细菌把气体分子吃掉，顶部出来的是干净空气",
 "The bacteria absorb the gas molecules, and clean air comes out of the top. No people.",
 "长在表面的微生物，把气体当食物吃掉。"),
# K7
("K7", "一种细菌抓住氨分子，变成另一个分子",
 "One kind of bacterium grabs an ammonia molecule icon and turns it into a different molecule icon. No people.",
 "亚硝化单胞菌，把氨氧化成亚硝酸盐。", "去氨、去硫化氢的两种菌", ["亚硝化单胞菌", "氨→亚硝酸盐"]),
("K7", "另一种细菌抓住硫化氢分子，变成硫酸盐",
 "Another kind of bacterium grabs a hydrogen sulfide molecule icon and turns it into a sulfate icon. No people.",
 "硫杆菌，把硫化氢氧化成硫酸盐。", "", ["硫杆菌", "硫化氢→硫酸盐"]),
# 小结
("小结", "欣欣站在三个图标前：噬菌体、酸碱试纸、生物滤池",
 "The panda mascot stands in front of three icons: a bacteriophage, a pH strip and a biofilter tower.",
 "一起回顾一下。", "小结", ["噬菌体", "酸碱废水", "生物滤池"]),
("小结", "噬菌体攻击带红点的细菌，绿色细菌无恙",
 "Bacteriophages attack bacteria with red dots while green bacteria stay unharmed. No people.",
 "噬菌体精准杀致病菌，不伤有益菌。"),
("小结", "水色由红、蓝变成绿色，滤池顶部出干净空气",
 "Red and blue water turn green, and clean air comes out of a biofilter tower. No people.",
 "微生物间接调酸碱，滤池吃掉臭气。"),
# 结尾
("结尾", "欣欣和阿杰、小研一起挥手告别",
 "The panda mascot waves goodbye together with the young male student and the female graduate student.",
 "小小微生物，治污大本事，下次见！"),
]
