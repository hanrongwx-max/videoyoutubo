# 08_Sublimation 卡通剧本作者源（原著版）
# 原著版：完全照原片（培养皿常压升华纯化演示），K1–K23，不本土化、不纠正、不补充
# 保留原片两处“注意”（过热毁样品、皿盖粘住丢晶体）与开放台面上的电热板操作；参数只用原片的“铺层不超过 5 mm”“低热”
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "升华",
    "edition": "原著版",
    "points": {
        "K1": "什么是升华",
        "K2": "能升华的固体可用来纯化",
        "K3": "本课演示常压升华",
        "K4": "条件一：不分解",
        "K5": "条件二：杂质不升华",
        "K6": "装置很简单",
        "K7": "转移粗样",
        "K8": "铺薄，不超过5毫米",
        "K9": "放上热板，盖好皿盖",
        "K10": "盖上放冰浴",
        "K11": "低温加热，要有耐心",
        "K12": "过热会毁掉样品",
        "K13": "皿盖上长出晶体",
        "K14": "长成一层就关热",
        "K15": "先稍冷却",
        "K16": "轻轻滑开冰浴",
        "K17": "小心皿盖粘住",
        "K18": "揭盖见晶体",
        "K19": "刮到表面皿上",
        "K20": "和粗样对比",
        "K21": "再收一批",
        "K22": "重复到全部纯化",
        "K23": "演示不能代替讲义",
    },
    "avoid": ["Digital Lab Techniques Manual", "Massachusetts Institute", "OpenCourseWare", "Sarah Tabacco", "Tabacco", "Aayesha Siddiqui", "Siddiqui", "Class of", "Pyrex", "KIMAX", "Kimble", "VWR"],
}

SHOTS = [
# 开场
("开场", "欣欣站在电热板旁，板上是盖着皿盖的培养皿，皿盖上放着一杯冰水，向镜头招手",
 "The panda mascot stands beside a hot plate holding a covered glass dish topped with a beaker of ice water, and waves at the camera.",
 "这一课讲升华纯化。", "升华"),
("开场", "固体直接变成气体、再在冷处结晶的示意",
 "A diagram: a solid turning directly into vapor, then forming crystals on a cold surface above. No people.",
 "固体变气体，遇冷再结晶。", "", ["固体", "气体", "晶体"]),
# 情景
("情景", "阿杰把电热板旋钮拧到最大，培养皿里的样品冒烟发黑",
 "The young male student turns the hot plate knob all the way up and the sample in the petri dish smokes and turns black.",
 "阿杰想快点，把热板开到最大。"),
("情景", "烧黑的样品图标被红叉划掉",
 "An icon of a blackened sample in a dish, crossed out with a red X. No people.",
 "样品烧焦了，白忙一场。"),
("情景", "小研把旋钮调到很低",
 "The female graduate student turns the hot plate knob down to a very low setting.",
 "小研说：升华要小火、要耐心。"),
# K1
("K1", "冰块化成水和固体直接冒出气体两个对比图标",
 "Two icons compared: an ice cube melting into water, and a solid giving off vapor directly with no liquid. No people.",
 "固体不经熔化，直接变成气体。", "什么是升华"),
("K1", "欣欣指着冒出蒸气的固体图标",
 "The panda mascot points at an icon of a solid releasing vapor.",
 "这就叫升华。"),
# K2
("K2", "温度计上熔点线下方，固体已有蒸气冒出",
 "A thermometer with a melting point line; below the line the solid already gives off vapor. No people.",
 "熔点以下就有明显蒸气压的固体，", "能升华的固体可用来纯化"),
("K2", "粗样变成纯晶体的箭头",
 "A crude brownish powder turning into bright pure crystals with an arrow. No people.",
 "才能升华，可以用来纯化。"),
# K3
("K3", "常压升华装置图，旁边一个减压装置小图标",
 "A diagram of an open sublimation setup at normal pressure, with a small vacuum setup icon beside it. No people.",
 "本课演示常压升华。", "本课演示常压升华"),
("K3", "两种装置之间一个等号",
 "The two setups with an equal sign between them. No people.",
 "减压升华，原理和步骤也一样。"),
# K4
("K4", "分子变成气体再变回晶体，结构不变",
 "A molecule icon becomes vapor and then a crystal again, keeping the same shape, with a green check. No people.",
 "条件一：升华和凝结时不分解。", "条件一：不分解"),
# K5
("K5", "目标分子飞上去，杂质颗粒留在原处",
 "Target molecule icons rise up while impurity particles stay behind at the bottom. No people.",
 "条件二：杂质在同样条件下不升华。", "条件二：杂质不升华"),
# K6
("K6", "电热板、培养皿底、培养皿盖、冰水烧杯四个部件",
 "Four parts laid out: a hot plate, a glass dish bottom, a glass dish lid, and a beaker of ice water. No people.",
 "电热板、培养皿、皿盖、冰浴。", "装置很简单", ["电热板", "培养皿", "皿盖", "冰浴"]),
("K6", "欣欣竖起大拇指",
 "The panda mascot gives a thumbs up beside the simple setup.",
 "就这么简单。"),
# K7
("K7", "小研戴手套，用刮刀把棕色粗样转进培养皿",
 "The female graduate student, wearing gloves, uses a spatula to transfer brownish crude powder into a glass dish.",
 "先把粗样转进培养皿。", "转移粗样"),
# K8
("K8", "刮刀把粉末摊平，旁边一个厚度标尺",
 "A spatula spreads the powder evenly, with a small thickness ruler beside it. No people.",
 "摊开摊平，哪里都不超过5毫米。", "铺薄，不超过5毫米", ["≤5毫米"]),
# K9
("K9", "培养皿放到电热板上，盖上皿盖",
 "The dish is set on the hot plate and covered with its glass lid. No people.",
 "放到电热板上，盖上皿盖。", "放上热板，盖好皿盖"),
# K10
("K10", "一杯冰水放在皿盖上",
 "A beaker of ice water is placed on top of the dish lid. No people.",
 "皿盖上放一杯冰水当冰浴。", "盖上放冰浴"),
# K11
("K11", "手指把旋钮调到很低的位置",
 "A finger turns the hot plate knob to a very low mark. No people.",
 "加热开到很低。", "低温加热，要有耐心"),
("K11", "沙漏图标旁的装置",
 "The setup next to an hourglass icon. No people.",
 "耐心等着。"),
# K12
("K12", "旋钮开到最大、样品发黑的图标被打叉",
 "An icon of a knob at maximum and a blackened sample, crossed out with a red X. No people.",
 "加热过头，样品就毁了。", "过热会毁掉样品"),
# K13
("K13", "皿盖下表面出现亮黄色晶体",
 "Bright yellow-orange crystals form on the underside of the dish lid below the ice beaker. No people.",
 "条件合适，皿盖上很快长出晶体。", "皿盖上长出晶体"),
# K14
("K14", "晶体长成一层，手指关闭加热",
 "A layer of crystals has grown; a finger switches off the heat. No people.",
 "长成一层，就关掉加热。", "长成一层就关热"),
# K15
("K15", "温度计图标指针下降",
 "A thermometer icon beside the setup with its level dropping. No people.",
 "先让装置稍微冷一冷。", "先稍冷却"),
# K16
("K16", "冰水烧杯被轻轻从皿盖上滑开",
 "The ice water beaker is gently slid sideways off the dish lid. No people.",
 "再把冰浴轻轻滑开。", "轻轻滑开冰浴"),
# K17
("K17", "皿盖粘在烧杯底被一起提起、晶体掉落的图标被打叉",
 "An icon of the lid stuck to the beaker bottom being lifted together, crystals falling off, crossed out with a red X. No people.",
 "小心，皿盖可能粘在烧杯底上。", "小心皿盖粘住"),
("K17", "手按住皿盖，烧杯平移离开",
 "A hand holds the lid down while the beaker slides away. No people.",
 "一不小心，晶体就全掉了。"),
# K18
("K18", "小研轻轻揭开皿盖，盖下一层闪亮晶体",
 "The female graduate student carefully lifts the lid to show a layer of shiny crystals underneath.",
 "小心揭盖，纯净的晶体出现了。", "揭盖见晶体"),
# K19
("K19", "刮刀把晶体刮到干净表面皿上",
 "A spatula scrapes the crystals from the lid onto a clean watch glass. No people.",
 "把晶体刮到干净的表面皿上。", "刮到表面皿上"),
# K20
("K20", "左边棕色带黑点的粗样，右边亮橙色晶体",
 "Left: a brownish crude powder with dark specks. Right: bright orange crystals, with a green check. No people.",
 "和粗样比一比，干净多了。", "和粗样对比", ["粗样", "纯品"]),
# K21
("K21", "表面皿上只有少量晶体",
 "Only a small amount of crystals on the watch glass. No people.",
 "第一批不多，别着急。", "再收一批"),
("K21", "盖回皿盖、放上冰浴、重新开低热",
 "The lid goes back on, the ice beaker on top, and the heat is turned back on low. No people.",
 "盖好、放冰浴、重新加热收下一批。"),
# K22
("K22", "循环箭头图标，表面皿上的晶体越来越多",
 "A cycle arrow icon while the pile of crystals on the watch glass grows. No people.",
 "重复几次，直到全部纯化。", "重复到全部纯化"),
# K23
("K23", "欣欣手捧空白讲义",
 "The panda mascot holds a thick blank lab manual.",
 "演示只是预习，讲义一定要读。", "演示不能代替讲义"),
# 小结
("小结", "欣欣身旁浮现不分解、杂质不升华两个图标",
 "The panda mascot stands beside two floating icons: an intact molecule and impurities staying behind.",
 "不分解、杂质不升华，才能用升华。", "小结"),
("小结", "铺薄的粗样、皿盖、冰浴、低温旋钮图标",
 "Icons of a thin layer of crude solid, a dish lid, a beaker of ice water and a low heat knob. No people.",
 "铺薄、盖好、放冰浴、小火慢热。"),
("小结", "冷却、滑开、揭盖、刮晶体四个图标",
 "Four icons: cooling, sliding the beaker away, lifting the lid and scraping crystals. No people.",
 "先冷却，再滑开冰浴，小心揭盖。"),
("小结", "循环箭头和越来越多的晶体图标",
 "A circular arrow icon next to a watch glass with a growing pile of crystals. No people.",
 "一批一批收，直到全部纯化。"),
# 结尾
("结尾", "欣欣举起盛着橙色晶体的表面皿，挥手道别",
 "The panda mascot holds up a watch glass of bright orange crystals and waves goodbye at the camera.",
 "小火慢慢来，晶体自然来，下次见！"),
]
