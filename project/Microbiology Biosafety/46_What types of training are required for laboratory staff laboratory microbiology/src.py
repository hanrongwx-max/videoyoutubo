# 46_What types of training are required for laboratory staff laboratory microbiology 卡通剧本作者源
# 原片（无语音的单页文字幻灯片）列出实验室人员六类必备培训：保留 K1–K7，
# 原著版：完全照原片，K1–K7，无补充知识点（六类必备培训）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室人员需要哪些培训？",
    "edition": "原著版",
    "points": {
        "K1": "六类必备培训",
        "K2": "生物安全操作：操作、隔离、废物",
        "K3": "生物安保意识：防止未经授权接触",
        "K4": "个人防护：会选、会穿、会脱",
        "K5": "应急程序：溢洒、撤离、暴露处理",
        "K6": "设备使用：安全柜、灭菌器",
        "K7": "事件报告：怎么报，何时报",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在培训教室门口，手里拿着一本空白手册",
 "The panda mascot stands at the door of a small training classroom holding a blank handbook and waves at the camera.",
 "这一课讲：进生物实验室要学什么。", "进生物实验室要学什么"),
# 情景
("情景", "阿杰拿着准入考试合格的空白证书，兴奋地走向实验室",
 "The young male student happily walks toward the lab holding a blank certificate card.",
 "阿杰通过了学校的安全考试，想直接上手。"),
("情景", "小研笑着拦住，翻开一张六格清单",
 "The female graduate student smiles, stops him and opens a blank checklist with six boxes.",
 "小研说：要做微生物实验，还有六门课。"),
# K1
("K1", "六个图标排成两行",
 "Six icons in two rows: a petri dish, a padlock, gloves, a warning triangle, a biosafety cabinet and a telephone. No people.",
 "实验室人员的必备培训，有六类。", "六类必备培训", ["安全操作", "安保意识", "个人防护", "应急", "设备"]),
("K1", "第六个电话图标亮起",
 "The telephone icon lights up. No people.",
 "最后一类，是事件报告。", "", ["事件报告"]),
# K2
("K2", "培养皿图标亮起，小研戴手套演示",
 "The female graduate student, wearing gloves and a lab coat, demonstrates careful handling of a culture plate.",
 "第一，生物安全操作。", "生物安全操作：操作、隔离、废物"),
("K2", "小研在安全柜里操作，阿杰在旁观看",
 "The female graduate student works inside a biosafety cabinet while the young male student watches.",
 "学会规范操作，在防护设施里做实验，"),
("K2", "废弃培养物装袋，放入灭菌器",
 "Used culture plates go into a biohazard bag and then into an autoclave. No people.",
 "还要学会废物怎样灭活、怎样处置。"),
# K3
("K3", "带锁的样本冰箱和门禁读卡器",
 "A locked sample freezer and a door access card reader. No people.",
 "第二，生物安保意识。", "生物安保意识：防止未经授权接触"),
("K3", "一个陌生人形图标在门外，被门禁挡住",
 "An unfamiliar person silhouette icon is stopped at a locked lab door. No people.",
 "能认出未经授权的进入和接触，"),
# K4
("K4", "手套、护目镜、实验服、口罩图标",
 "Icons of gloves, goggles, a lab coat and a respirator mask. No people.",
 "第三，个人防护装备。", "个人防护：会选、会穿、会脱", ["选择", "穿戴", "脱卸"]),
("K4", "小研对照空白清单挑选合适尺码的手套",
 "The female graduate student picks gloves of the right size from a shelf, checking a blank list.",
 "学会怎样选对防护用品，"),
("K4", "阿杰按顺序穿上实验服、戴手套",
 "The young male student puts on a lab coat and then gloves in front of a mirror.",
 "按顺序穿戴，检查是否完好，"),
("K4", "阿杰摘手套时外面朝里翻",
 "The young male student removes his gloves by turning them inside out.",
 "脱的时候外面当污染，别碰到皮肤。"),
# K5
("K5", "警示三角图标亮起",
 "A warning triangle icon lights up. No people.",
 "第四，应急程序。", "应急程序：溢洒、撤离、暴露处理", ["溢洒", "撤离", "暴露"]),
("K5", "小研和阿杰用空白溢洒处理箱演练",
 "The female graduate student and the young male student practice with a spill kit around a blank prop spill.",
 "溢洒了怎么处理，"),
("K5", "绿色疏散指示标志和向外走的箭头",
 "An emergency exit sign with green arrows pointing toward the door. No people.",
 "什么情况要撤离，"),
("K5", "洗眼器和急救箱图标",
 "Icons of an eyewash station and a first aid kit. No people.",
 "被扎伤、溅到了，第一时间怎么做。"),
# K6
("K6", "安全柜和高压灭菌器并排",
 "A biosafety cabinet and an autoclave side by side. No people.",
 "第五，设备使用。", "设备使用：安全柜、灭菌器"),
("K6", "老李给阿杰讲安全柜面板，面板只有图标",
 "The facility engineer explains the icon-only control panel of a biosafety cabinet to the young male student.",
 "安全柜怎么开、怎么用、怎么判断正常，"),
("K6", "老李在灭菌器前演示关门锁紧",
 "The facility engineer demonstrates closing and locking the autoclave door.",
 "灭菌器怎么装载、怎么防烫伤。"),
# K7
("K7", "电话图标亮起",
 "A telephone icon lights up. No people.",
 "第六，事件报告。", "事件报告：怎么报，何时报"),
("K7", "电话和空白报告单两个图标",
 "A phone icon next to a blank report form. No people.",
 "要学会怎么报：找谁、填什么。"),
("K7", "时钟图标，指针刚走一点",
 "A clock icon with the hand just moving forward. No people.",
 "事故和暴露，发生后立即报告，"),
("K7", "小研在空白事件记录表上如实填写",
 "The female graduate student fills in a blank incident record form.",
 "如实记录下来。"),
# 小结
("小结", "欣欣站在六个图标旁",
 "The panda mascot stands beside the six training icons.",
 "安全操作、安保、防护、应急、设备、报告。", "小结"),
# 结尾
("结尾", "欣欣和阿杰站在实验室门口挥手",
 "The panda mascot and the young male student wave goodbye at the lab door with a biohazard warning sign.",
 "学到位，再上手，下次见！"),
]
