# 04_What are Biosafety cabinets , biosafety cabinet in microbiology laboratory biosa 原著版卡通剧本作者源
# 完全照原片：K1–K14（生物安全柜定义，I、II、III 级的防护对象、气流、适用范围），无补充知识点；
# 保留原片说法：I 级“不适合挥发性化学品或放射性核素”，II 级“A1、A2、B2 三个防护等级”，III 级“通常嵌入实验室建造”；
# 原片在 III 级处点名的具体病毒不出现，只说“最危险的生物因子”
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "什么是生物安全柜？",
    "edition": "原著版",
    "points": {
        "K1": "生物安全柜：护人、护环境、护样品",
        "K2": "按防护水平分三级",
        "K3": "一级柜：护人和环境",
        "K4": "一级柜：不护样品",
        "K5": "一级柜：前面敞开，向里吸风",
        "K6": "一级柜：低到中度风险",
        "K7": "二级柜：最常用，三方面都护",
        "K8": "二级柜：A1、A2、B2",
        "K9": "二级柜：过滤加气流，保持无菌",
        "K10": "二级柜：中到高风险",
        "K11": "三级柜：最高防护",
        "K12": "三级柜：完全隔离",
        "K13": "三级柜：手套口和传递气锁",
        "K14": "三级柜：废物处理后才出柜",
    },
    "avoid": ["ARHMicroHub", "ARH Micro Hub", "ARH", "raqbamicrohub", "PRO-LAB", "Prolab", "Ebola"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台生物安全柜旁，向镜头招手",
 "The panda mascot stands beside a biological safety cabinet and waves at the camera.",
 "这一课专讲生物安全柜。", "生物安全柜的三个级别"),
("开场", "一、二、三级三台柜子图标排成一行",
 "Three cabinet icons in a row: an open-front cabinet, a cabinet with a front window, and a sealed glove-box style cabinet. No people.",
 "它分一、二、三级，各不相同。", "", ["一级", "二级", "三级"]),
# 情景
("情景", "阿杰看着实验室里两台外形不同的安全柜",
 "The young male student looks at two different biological safety cabinets in the lab, puzzled.",
 "阿杰发现，实验室里的安全柜不一样。"),
("情景", "阿杰问小研，小研笑着拿出空白说明书",
 "The young male student asks a question; the female graduate student smiles and takes out a blank cabinet manual.",
 "小研说：级别不同，护的东西也不同。"),
# K1
("K1", "生物安全柜正面，前窗半开",
 "Front view of a biological safety cabinet with its window at the marked height and a biohazard warning sign. No people.",
 "生物安全柜，是一种生物防护设备。", "生物安全柜：护人、护环境、护样品"),
("K1", "三个盾牌：人、地球、样品管",
 "Three shields protecting a person icon, a globe icon and a sample tube icon. No people.",
 "它保护人员、环境，还有样品。", "", ["人员", "环境", "样品"]),
# K2
("K2", "三台柜子按密闭程度从开放到全封闭排列",
 "Three cabinet icons arranged from fully open front to fully sealed. No people.",
 "按提供的防护水平，分成三级。", "按防护水平分三级", ["一级", "二级", "三级"]),
# K3
("K3", "一级柜：前面敞开",
 "A simple class one cabinet with an open front, beside a lab coat, gloves and goggles icon. No people.",
 "先看一级柜。", "一级柜：护人和环境"),
("K3", "盾牌挡在人形图标前和地球图标前",
 "Shields in front of a person outline and a globe icon. No people.",
 "它保护使用者和环境，免受有害材料伤害。"),
# K4
("K4", "柜内样品旁飘进室内的灰尘点",
 "Dust dots from room air drift into the cabinet and land near an open culture dish. No people.",
 "但它不保护操作的材料，", "一级柜：不护样品"),
("K4", "样品管图标上出现污染点，旁边一个叉",
 "A sample tube icon with contamination dots and a red X beside it. No people.",
 "材料可能被污染。"),
# K5
("K5", "剖面图：空气从前面开口被吸进柜内",
 "A cutaway diagram of a class one cabinet: room air flows in through the open front, away from the user. No people.",
 "一级柜前面敞开，把空气从人这边吸走，", "一级柜：前面敞开，向里吸风"),
("K5", "空气经过顶部过滤器后排出",
 "The air passes through a filter at the top before being exhausted. No people.",
 "经过过滤后再排出去。"),
# K6
("K6", "风险刻度上低到中段被点亮",
 "A risk scale from low to high with the low-to-middle section highlighted. No people.",
 "一级柜一般用于低到中度风险的因子。", "一级柜：低到中度风险"),
("K6", "挥发性试剂瓶和放射标志旁打叉",
 "A volatile chemical bottle and a radiation warning sign, each with a red X beside a class one cabinet. No people.",
 "它不适合挥发性化学品和放射性核素。", "", ["挥发性化学品", "放射性核素"]),
# K7
("K7", "二级柜特写，前窗有标记线",
 "Close-up of a class two biological safety cabinet with a front window at a marked height. No people.",
 "二级柜是最常用的安全柜。", "二级柜：最常用，三方面都护"),
("K7", "三个盾牌同时亮起",
 "Shields over a person icon, a globe icon and a sample tube icon light up together. No people.",
 "使用者、环境、样品，它都能保护。"),
# K8
("K8", "三台二级柜图标，排风箭头各不相同",
 "Three class two cabinet icons with different exhaust arrows: some return air to the room, one ducted to the roof. No people.",
 "二级柜有三个防护等级：", "二级柜：A1、A2、B2", ["A1", "A2", "B2"]),
("K8", "气流方向、排风管、盾牌三个图标",
 "Three icons: airflow arrows, an exhaust duct going outside, and a shield. No people.",
 "按气流、排风系统和防护水平来分。", "", ["气流方式", "排风系统", "防护水平"]),
# K9
("K9", "剖面图：过滤后的空气从上往下吹",
 "A cutaway diagram of a class two cabinet: filtered air flows down over the work surface. No people.",
 "二级柜把高效过滤和气流结合起来，", "二级柜：过滤加气流，保持无菌"),
("K9", "小研在二级柜里操作培养物",
 "The female graduate student, in a lab coat, goggles and gloves, works with cultures in a class two cabinet.",
 "提供一个无菌的工作环境。"),
# K10
("K10", "风险刻度中到高段被点亮",
 "A risk scale with the middle-to-high section highlighted next to a class two cabinet. No people.",
 "二级柜适用于中到高风险的因子。", "二级柜：中到高风险"),
# K11
("K11", "三级柜：全封闭的手套箱式柜",
 "A fully sealed glove-box style class three cabinet with two glove ports. No people.",
 "三级柜是最安全的一种，", "三级柜：最高防护"),
("K11", "三个盾牌最大最亮",
 "Large glowing shields over a person icon, a globe icon and a sample tube icon. No people.",
 "对人、环境和样品，防护都最高。"),
# K12
("K12", "柜子被一圈厚墙完全包围",
 "A diagram of the sealed cabinet surrounded by a thick wall, no air arrows escaping. No people.",
 "它用于最危险的生物因子，", "三级柜：完全隔离"),
("K12", "柜内和柜外之间一道实线分隔",
 "A solid line separating inside the cabinet from the room outside. No people.",
 "与外界环境完全隔离。"),
# K13
("K13", "柜子嵌在实验室墙体中的示意",
 "A diagram of the sealed cabinet built into the wall of a lab room. No people.",
 "三级柜通常嵌在实验室里建造。", "三级柜：手套口和传递气锁"),
("K13", "手伸进手套口的示意",
 "A diagram of hands inserted into the glove ports of a sealed cabinet. No people.",
 "操作时，手伸进手套口，"),
("K13", "侧面传递气锁，一道门关、一道门开",
 "A pass-through airlock box on the side of the cabinet with two doors, one closed while the other opens. No people.",
 "物品经传递气锁进出工作区。"),
# K14
("K14", "废物袋在柜内封好，再进入灭菌器",
 "A sealed waste bag inside the cabinet moving into an attached autoclave. No people.",
 "柜里的所有材料和废物，", "三级柜：废物处理后才出柜"),
("K14", "处理后的废物从柜子另一侧出来，绿色对勾",
 "Treated waste comes out the other side with a green check mark. No people.",
 "都要在柜内封装处理后才能移出。"),
# 小结
("小结", "欣欣身旁三台柜子图标依次亮起",
 "The panda mascot stands beside three cabinet icons that light up one by one.",
 "一级护人和环境，不护样品；", "小结"),
("小结", "二级柜和三个盾牌",
 "A class two cabinet icon with three shields. No people.",
 "二级最常用，三方面都护；"),
("小结", "三级柜和手套口",
 "A sealed class three cabinet icon with glove ports. No people.",
 "三级完全隔离，防护最高。"),
# 结尾
("结尾", "欣欣和阿杰在二级柜前挥手",
 "The panda mascot and the young male student wave goodbye in front of a class two biological safety cabinet.",
 "认清级别再使用，下次见！"),
]
