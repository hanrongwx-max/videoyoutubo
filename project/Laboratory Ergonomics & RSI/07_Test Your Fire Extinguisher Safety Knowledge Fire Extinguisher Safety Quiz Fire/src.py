# 07_Test Your Fire Extinguisher Safety Knowledge Fire Extinguisher Safety Quiz Fire 卡通剧本作者源
# 原著版：完全照原片（10 道灭火器选择题，读题后口述答案），K1–K11，不加补充知识点、不做更正；
# 保留原片的美国火灾分类（A 普通可燃物、B 易燃液体、C 电气、D 可燃金属）、二氧化碳灭火器适用 B 和 C 类、
# ABC 三类干粉、水型靠冷却、最常见的是干粉；哈龙只作为选项出现
# 频道名和美国标准机构名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "灭火器安全知识自测",
    "edition": "原著版",
    "points": {
        "K1": "灭火器十题",
        "K2": "发现火情先报警",
        "K3": "四步口诀",
        "K4": "对准火焰根部",
        "K5": "二氧化碳灭火器灭哪类火",
        "K6": "出口留在身后",
        "K7": "火三角",
        "K8": "A类火：普通固体",
        "K9": "ABC干粉灭火器",
        "K10": "水型灭火器靠冷却",
        "K11": "最常见的是干粉",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "NFPA"],
}

SHOTS = [
# 开场
("开场", "欣欣抱着一具灭火器，向镜头招手",
 "The panda mascot holds a red fire extinguisher and waves at the camera.",
 "灭火器十问，选对、拿稳、用好！", "灭火器安全知识自测"),
# 情景
("情景", "阿杰在走廊里看着墙上的灭火器，挠头",
 "The young male student looks at a fire extinguisher hanging on a corridor wall and scratches his head.",
 "阿杰看着灭火器：真着火了我会用吗？"),
("情景", "王老师走来，拿起题卡",
 "The safety administrator walks over holding a stack of blank quiz cards.",
 "王老师说：来，十道题测一测。"),
# K1
("K1", "十张空白题卡，灭火器图标",
 "Ten blank quiz cards with a small fire extinguisher icon. No people.",
 "十道题，一题一题来。", "灭火器十题", ["10道题"]),
# K2
("K2", "四个选项图标：跑开的人、拿灭火器的新手、留在屋里的人、报警按钮和电话",
 "Four option icons: a person running away alone, a beginner grabbing an extinguisher, a person staying inside, and an alarm button with a phone. No people.",
 "第一题：发现火情，第一步做什么？", "发现火情先报警"),
("K2", "报警按钮和电话图标亮起打勾，其他三个打叉",
 "The alarm button and phone icon glows with a green check; the other three are crossed out. No people.",
 "答案D，拉响火警，呼叫消防队。", "", ["D 报警", "呼叫消防队"]),
("K2", "一个人独自跑开、别人没察觉的图标打叉",
 "An icon of a person running off while others remain unaware, crossed out. No people.",
 "不能自己跑掉，不提醒别人。"),
("K2", "从没用过灭火器的人硬上，图标打叉",
 "An icon of an untrained person nervously holding an extinguisher upside down, crossed out. No people.",
 "没学过就别硬上，更别留在屋里琢磨。"),
# K3
("K3", "四个手势：拔销、对准、压把、扫射",
 "Four step icons: pulling a pin, aiming a nozzle, squeezing a handle and sweeping. No people.",
 "第二题：四步口诀是什么？", "四步口诀", ["拔销", "对准", "压把", "扫射"]),
("K3", "小研在培训场依次完成四步",
 "The female graduate student performs the four steps in order at a fire training ground.",
 "答案C：拔销、对准、压把、扫射。", "", ["C"]),
# K4
("K4", "火焰分顶部、中部、根部三段，喷嘴对准根部",
 "A flame divided into top, middle and base sections, with a nozzle aimed at the base. No people.",
 "第三题：喷嘴对准哪里？", "对准火焰根部"),
("K4", "对准火苗顶部、中部和远处的图标打叉",
 "Icons of spraying away from the fire, at the top and at the center of the flames, each crossed out with a red X. No people.",
 "不对着远处、顶部、中部，答案D根部。", "", ["D 火焰根部"]),
# K5
("K5", "二氧化碳灭火器，长喇叭筒",
 "A carbon dioxide fire extinguisher with a long horn-shaped nozzle. No people.",
 "第四题：二氧化碳灭火器灭哪类火？", "二氧化碳灭火器灭哪类火"),
("K5", "易燃液体和带电设备两个图标打勾",
 "Two icons with green checks: a burning liquid and an electrical panel. No people.",
 "答案D，B类和C类火。", "", ["B类 易燃液体", "C类 电气", "D B和C"]),
# K6
("K6", "小研灭火，身后是安全出口",
 "The female graduate student fights a small fire with the emergency exit behind her.",
 "第五题：出口要留在身后，对吗？", "出口留在身后"),
("K6", "对勾图标",
 "A large green check mark beside the exit icon. No people.",
 "答案A，正确。", "", ["A 正确"]),
# K7
("K7", "火三角：氧气、可燃物、热源",
 "A red triangle with an oxygen icon, a fuel icon and a heat icon on its sides. No people.",
 "第六题：火三角是哪三样？", "火三角", ["氧气", "可燃物", "热源"]),
("K7", "水和土的图标打叉",
 "A water drop icon and a soil icon crossed out. No people.",
 "答案C，氧气、可燃物、热源。", "", ["C"]),
# K8
("K8", "木头、纸张、布料、液体、电器、金属图标",
 "Icons of wood, paper and cloth beside icons of a burning liquid, an electrical plug and a metal ingot. No people.",
 "第七题：A类火涉及什么？", "A类火：普通固体"),
("K8", "三样东西放进A类框",
 "The three items drop into one box with a solid block icon. No people.",
 "答案A，普通可燃物。", "", ["A 普通可燃物"]),
# K9
("K9", "一具干粉灭火器，铭牌上三个空白方块",
 "A dry powder extinguisher with three blank squares on its label. No people.",
 "第八题：ABC干粉能灭哪些火？", "ABC干粉灭火器"),
("K9", "A、B、C三个图标打勾",
 "Icons of a wooden block, a burning liquid and an electrical plug, each with a green check. No people.",
 "A、B、C类都能用，答案D全部。", "", ["A", "B", "C", "D 以上皆是"]),
# K10
("K10", "水型灭火器喷水，温度计下降",
 "A water fire extinguisher spraying with a thermometer dropping beside it. No people.",
 "第九题：水型灭火器靠什么灭火？", "水型灭火器靠冷却"),
("K10", "冷却图标亮起，其他三个打叉",
 "The cooling icon lights up; icons for oxygen exclusion, fuel removal and chain breaking are crossed out. No people.",
 "答案A，冷却。", "", ["A 冷却"]),
# K11
("K11", "四种灭火器图标：水型、干粉、哈龙、泡沫",
 "Four extinguisher icons: water, dry powder, halon and foam. No people.",
 "第十题：最常见的灭火器是哪种？", "最常见的是干粉"),
("K11", "干粉灭火器亮起打勾",
 "The dry powder extinguisher glows with a green check. No people.",
 "答案B，干粉灭火器。", "", ["B 干粉"]),
# 小结
("小结", "欣欣在白板前",
 "The panda mascot stands in front of a whiteboard with extinguisher icons.",
 "十题答完，回顾一下。", "小结"),
("小结", "图标：报警、四步、火焰根部",
 "Icons: an alarm button, four step icons and a flame base target. No people.",
 "先报警，PASS四步，对准根部。"),
("小结", "图标：二氧化碳灭火器配B、C，干粉配A、B、C",
 "Icons: a carbon dioxide extinguisher paired with two category boxes, and a dry powder extinguisher paired with three. No people.",
 "二氧化碳灭B、C，三类干粉灭ABC。", "", ["CO2→B C", "干粉→A B C"]),
("小结", "图标：出口在身后、水滴温度计",
 "Icons: a person with an exit behind and a water drop with a falling thermometer. No people.",
 "出口在身后，水型靠冷却。"),
("小结", "阿杰提起灭火器，竖起大拇指",
 "The young male student lifts the extinguisher from the wall bracket and gives a thumbs up.",
 "阿杰说：这回我会用了。"),
# 结尾
("结尾", "欣欣把灭火器挂回墙上，挥手",
 "The panda mascot hangs the extinguisher back on the wall and waves goodbye.",
 "灭火器十问到这里，下次见！"),
]
