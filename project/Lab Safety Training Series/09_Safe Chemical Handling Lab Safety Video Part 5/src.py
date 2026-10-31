# 09_Safe Chemical Handling Lab Safety Video Part 5 卡通剧本作者源（原著版）
# 原片为实验室安全系列第 5 集（安全操作化学品）：完全照原片，知识点 K1–K24，保留原片拨打 911、Z87.1 护目镜标识、接地储存柜等，不本土化、不补充
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室安全（五）：化学品的安全操作",
    "edition": "原著版",
    "points": {
        "K1": "凡事预则立",
        "K2": "动手前先判断风险",
        "K3": "穿好防护，想好应急",
        "K4": "稀释酸碱：酸入水",
        "K5": "化学品不出实验室",
        "K6": "转运用防破碎二次容器",
        "K7": "三条暴露途径",
        "K8": "防飞溅要戴护目镜",
        "K9": "护目镜要有合格标识",
        "K10": "近视眼镜不能代替防护",
        "K11": "防腐蚀：实验服、手套和围裙",
        "K12": "强腐蚀品戴长臂橡胶手套",
        "K13": "看不见的吸入危害",
        "K14": "不闻、进通风柜、随手盖紧",
        "K15": "大量溢洒：撤离、封闭、报告",
        "K16": "专业人员清理，许可后返回",
        "K17": "易燃品：先了解易燃易爆性",
        "K18": "易燃品远离火源",
        "K19": "易燃品放专用储存柜",
        "K20": "按规定处置化学品和废物",
        "K21": "废物用耐腐蚀容器",
        "K22": "不得靠通风柜蒸发“处置”溶剂",
        "K23": "清理溢洒的材料也是危险废物",
        "K24": "准备是安全的关键",
    },
    "avoid": ["BioNetwork", "NC Community Colleges", "Community Colleges", "Learning Solutions", "LSTeam", "Aldrich", "Fisher", "Pyrex", "Franklin", "NFPA", "Ciocalteu", "Folin"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台旁，向镜头招手",
 "The panda mascot stands beside a clean lab bench with a few reagent bottles and waves at the camera.",
 "这一课讲怎样安全地操作化学品。", "实验室安全（五）：化学品的安全操作"),
("开场", "护目镜、通风柜、易燃品柜、废液桶四个图标",
 "Four icons in a row: safety goggles, a fume hood, a yellow flammable storage cabinet and a waste container. No people.",
 "防护、通风、储存、废弃，一样不落。", "", ["防护", "通风", "储存", "废弃"]),
# 情景
("情景", "阿杰端着一瓶液体往门外走",
 "The young male student walks toward the lab door carrying an open bottle of liquid in one hand.",
 "阿杰想把一瓶试剂拿到隔壁实验室。"),
("情景", "小研拦住他，递上一只带盖的塑料提篮",
 "The female graduate student stops him and hands him a sturdy plastic carrier bucket with a lid.",
 "小研拦下他：这样拿太危险了。"),
# K1
("K1", "欣欣翻开一本空白计划本",
 "The panda mascot opens a blank planning notebook on the lab bench.",
 "凡事预则立，每次实验前都要准备。", "凡事预则立"),
# K2
("K2", "放大镜照着试剂瓶和仪器，冒出警示三角",
 "A magnifying glass over a reagent bottle and a hot plate, with a yellow warning triangle appearing. No people.",
 "动手之前，先想清楚有哪些风险。", "动手前先判断风险"),
# K3
("K3", "小研穿实验服、戴护目镜和手套",
 "The female graduate student puts on a lab coat, safety goggles and gloves at the lab entrance.",
 "穿戴合适的个人防护装备。", "穿好防护，想好应急"),
("K3", "洗眼器、冲淋器、灭火器图标",
 "Icons of an eyewash station, a safety shower and a fire extinguisher, each with a small location pin. No people.",
 "想好这种化学品出了事怎么应急。"),
# K4
("K4", "烧杯里装水，箭头表示把酸慢慢加入水中，打绿勾",
 "An icon of a beaker of water with an arrow showing a small bottle of acid being added slowly into it, with a green check. No people.",
 "稀释酸碱，要把酸碱加进水里。", "稀释酸碱：酸入水", ["酸入水 ✓"]),
("K4", "反向操作的图标被红叉划掉",
 "The reverse icon, water being poured into a bottle of acid, crossed out with a red X. No people.",
 "反过来倒，可能剧烈反应、溅出伤人。", "", ["水入酸 ✗"]),
# K5
("K5", "门口图标，化学瓶被红叉挡住",
 "A lab door icon with a chemical bottle icon crossed out by a red X at the threshold. No people.",
 "化学品不得带出实验室。", "化学品不出实验室"),
# K6
("K6", "阿杰把试剂瓶放进带盖的二次容器里提着走",
 "The young male student places a capped bottle into a sturdy lidded plastic carrier and carries it with both hands down a corridor.",
 "实验室之间转运，装进防破碎的二次容器。", "转运用防破碎二次容器"),
# K7
("K7", "人体轮廓，眼睛、皮肤、鼻子三处高亮",
 "A simple human outline with three highlighted spots: the eyes, the skin of the hands, and the nose. No people.",
 "化学品伤人，走眼睛、皮肤、呼吸三条路。", "三条暴露途径", ["眼睛", "皮肤", "吸入"]),
# K8
("K8", "带侧护的安全眼镜旁有飞溅水滴越过边缘",
 "A pair of safety glasses with side shields, with splash droplets flying around the edges toward the eye. No people.",
 "安全眼镜挡得住碎屑，挡不住飞溅。", "防飞溅要戴护目镜"),
("K8", "小研戴上贴合脸部的化学防溅护目镜",
 "The female graduate student puts on snug-fitting chemical splash goggles that seal around her eyes.",
 "有飞溅危险，换成防溅护目镜。"),
# K9
("K9", "护目镜镜框上的空白标识和合格对勾",
 "A close-up of a goggle frame with a blank embossed mark and a green check badge beside it. No people.",
 "护目镜要刻有防护标准的标识。", "护目镜要有合格标识", ["Z87.1"]),
# K10
("K10", "老周戴着近视眼镜，再在外面戴上面屏",
 "The older man wearing his ordinary prescription glasses puts a full face shield on over them.",
 "近视眼镜不防护，外面要加护目镜或面屏。", "近视眼镜不能代替防护"),
# K11
("K11", "腐蚀象形图，液滴落在手上",
 "A GHS corrosion hazard pictogram next to an icon of a droplet landing on a hand. No people.",
 "腐蚀品溅到皮肤，会造成灼伤。", "防腐蚀：实验服、手套和围裙"),
("K11", "阿杰穿实验服、戴手套，再系上全长的耐化学品围裙",
 "The young male student in a lab coat and gloves ties on a full-length chemical-resistant apron.",
 "飞溅风险大，再加一条耐化学品围裙。", "", ["实验服", "手套", "围裙"]),
# K12
("K12", "普通丁腈手套和长臂橡胶手套并排",
 "A short thin nitrile glove next to a thick rubber glove that reaches up to the elbow, with a green check on the long one. No people.",
 "强腐蚀品，换上长到手臂的橡胶手套。", "强腐蚀品戴长臂橡胶手套"),
# K13
("K13", "试剂瓶上方飘出看不见的淡色蒸气飘向人头图标",
 "A faint transparent vapor drifting from an open bottle toward a human head icon. No people.",
 "有些化学品，不碰也会伤人。", "看不见的吸入危害"),
# K14
("K14", "用鼻子凑近瓶口闻的图标被红叉划掉",
 "An icon of a nose sniffing an open bottle, crossed out with a red X. No people.",
 "不要用鼻子闻化学品。", "不闻、进通风柜、随手盖紧"),
("K14", "小研在通风柜里操作，拉门拉低",
 "The female graduate student works inside a fume hood with the sash pulled low, wearing goggles and gloves.",
 "有毒化学品，一律在通风柜里操作。"),
("K14", "手拧紧瓶盖",
 "A gloved hand tightens the cap on a reagent bottle. No people.",
 "用完随手把盖子盖紧。"),
# K15
("K15", "地上一只碎瓶和一大片液体，冒出蒸气",
 "A large puddle of liquid spreading from a broken bottle on the lab floor with vapor rising, drawn as a simple illustration. No people.",
 "要是发生大量溢洒，", "大量溢洒：撤离、封闭、报告"),
("K15", "小研和阿杰快步离开实验室，带上门",
 "The female graduate student and the young male student walk quickly out of the lab and close the door behind them.",
 "立即撤离，关门封闭实验室。"),
("K15", "小研用手机拨号，屏幕显示911",
 "The female graduate student dials on her mobile phone in the corridor; the screen shows the digits 9 1 1.",
 "通知有关部门，拨打911。", "", ["911"]),
# K16
("K16", "小研在门上贴警示牌，穿防护服的专业人员走来",
 "The female graduate student sticks a blank warning sign on the lab door while a response crew in protective suits approaches down the corridor.",
 "大量溢洒蒸气多，交给专业人员处理。", "专业人员清理，许可后返回"),
("K16", "阿杰在门外等待，老周点头示意",
 "The young male student waits outside the closed door; the older man arrives and gives a nod.",
 "负责人确认安全之前，不能回去。"),
# K17
("K17", "火焰象形图和爆炸弹象形图",
 "A GHS flame hazard pictogram and a GHS exploding bomb hazard pictogram side by side. No people.",
 "易燃品，先弄清它的易燃易爆性。", "易燃品：先了解易燃易爆性"),
# K18
("K18", "易燃溶剂瓶和酒精灯、加热板之间画红叉",
 "A flammable solvent bottle icon with a red X line separating it from a burner flame icon and a hot plate icon. No people.",
 "远离明火、加热板等一切火源。", "易燃品远离火源"),
# K19
("K19", "阿杰把溶剂瓶放进黄色的易燃品储存柜",
 "The young male student places a solvent bottle into a yellow flammable storage cabinet and closes the door.",
 "放回专用、接地的易燃品储存柜。", "易燃品放专用储存柜"),
# K20
("K20", "小研把废液倒入带漏斗的废液桶",
 "The female graduate student pours waste liquid through a funnel into a labeled waste container inside a fume hood.",
 "按国家、地方和本单位要求处置废物。", "按规定处置化学品和废物"),
# K21
("K21", "塑料桶和金属桶图标，打绿勾",
 "Icons of a chemical-resistant plastic carboy and a metal can, each with a green check. No people.",
 "废物用耐化学品的塑料或金属容器装。", "废物用耐腐蚀容器"),
# K22
("K22", "通风柜里敞口烧杯冒蒸气，被红叉划掉",
 "An open beaker of solvent evaporating inside a fume hood, crossed out with a red X. No people.",
 "不能把溶剂放通风柜里挥发掉了事。", "不得靠通风柜蒸发“处置”溶剂"),
("K22", "阿杰向老周请教",
 "The young male student asks the older man a question beside a fume hood.",
 "需要蒸发溶剂，先问负责人怎么做。"),
# K23
("K23", "用过的纸巾装进危险废物袋",
 "Used paper towels being placed into a hazardous waste bag with a blank label. No people.",
 "擦过溢洒的纸巾，也是危险废物。", "清理溢洒的材料也是危险废物"),
# K24
("K24", "欣欣举着三张卡片",
 "The panda mascot holds up three blank cards one after another.",
 "准备，是安全操作化学品的关键。", "准备是安全的关键", ["用的是什么", "怎么操作", "出事怎么办"]),
# 小结
("小结", "欣欣身旁浮现护目镜、围裙、通风柜图标",
 "The panda mascot stands beside floating icons of splash goggles, an apron and a fume hood.",
 "酸入水，护目镜，通风柜里操作。", "小结"),
("小结", "门、电话和警示牌图标",
 "Icons of a closed door, a telephone and a warning sign. No people.",
 "大量溢洒：撤离、封闭、通知。"),
("小结", "易燃品柜和废液桶图标",
 "Icons of a flammable storage cabinet and a lidded chemical waste container. No people.",
 "易燃品进专柜，废物按规定处置。"),
# 结尾
("结尾", "欣欣在整洁的通风柜旁挥手道别",
 "The panda mascot waves goodbye beside a tidy fume hood with the sash closed.",
 "做好准备，安全实验，下次见！"),
]
