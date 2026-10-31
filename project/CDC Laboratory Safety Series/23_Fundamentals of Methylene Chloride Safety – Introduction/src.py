# 23_Fundamentals of Methylene Chloride Safety – Introduction 原著版卡通剧本作者源
# 完全照原片：二氯甲烷安全课程的导引短片（1 分 31 秒），K1–K6（为什么要专门培训、长期或反复高水平接触伤心肝脑、
# 增加致癌风险、美国职业安全监管机构发布二氯甲烷专项标准、标准针对工业大量使用、实验室用量小但该法规同样适用），无补充知识点
# 画面沿用原片的示范：通风柜内取液、加样，废液倒入二次容器中的有机废液瓶
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "二氯甲烷安全基础：导论",
    "edition": "原著版",
    "points": {
        "K1": "为什么要专门培训",
        "K2": "伤心、伤肝、伤脑",
        "K3": "增加致癌风险",
        "K4": "有专门的职业接触标准",
        "K5": "标准源于大量使用",
        "K6": "用量小，规矩不减",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services", "OSHA", "1910.1052", "29 CFR",
              "Mott Manufacturing", "Mott", "J.T.Baker", "J. T. Baker", "Baker"],
}

SHOTS = [
# 开场
("开场", "欣欣站在通风柜旁，柜里有一瓶空白标签的溶剂",
 "The panda mascot stands beside a chemical fume hood with a brown solvent bottle with a blank label inside, and waves at the camera.",
 "这一课讲二氯甲烷的安全使用。", "二氯甲烷安全基础：导论"),
("开场", "溶剂瓶旁浮现健康危害和感叹号象形图",
 "A solvent bottle with a blank label next to a health hazard pictogram and an exclamation mark pictogram. No people.",
 "先说说，它为什么值得专门学。"),
# 情景
("情景", "阿杰拿到一瓶空白标签的溶剂，准备做萃取",
 "The young male student picks up a brown solvent bottle with a blank label from a shelf, ready for an extraction experiment.",
 "阿杰要用二氯甲烷做萃取。"),
("情景", "小研递给他一张空白的培训通知",
 "The female graduate student hands the young male student a blank training notice.",
 "小研说：用之前，先参加专门培训。"),
("情景", "阿杰一脸不解地看着通知",
 "The young male student looks at the blank notice with a puzzled face.",
 "阿杰有点不明白。"),
# K1
("K1", "阿杰挠头，头顶一个大问号",
 "The young male student scratches his head with a big question mark above him, next to a solvent bottle with a blank label.",
 "在实验室用它，为什么要专门培训？", "为什么要专门培训"),
("K1", "小研穿一次性防护服、戴护目镜和手套，在通风柜里用瓶口分液器取液",
 "The female graduate student, in a disposable protective gown, goggles and blue gloves, dispenses solvent with a bottle-top dispenser inside a fume hood.",
 "这是个好问题，我们来看看。"),
# K2
("K2", "小研用移液管向几支编号空白的样品管里加液",
 "Inside the fume hood, the female graduate student pipettes liquid into a row of sample tubes with blank labels.",
 "长期或反复的高水平接触，", "伤心、伤肝、伤脑"),
("K2", "人体示意图，心脏、肝脏、大脑依次亮起红色",
 "A simple human body diagram with the heart, the liver and the brain lighting up red one after another. No people.",
 "会严重伤害心脏、肝脏和大脑。", "", ["心脏", "肝脏", "大脑"]),
("K2", "日历上一页页翻过，人形图标逐渐变灰",
 "Calendar pages flip by while a person pictogram slowly turns gray. No people.",
 "这是长期、反复接触带来的影响。"),
# K3
("K3", "手持一只空白标签的烧杯，移液管伸进去取液",
 "A gloved hand holds a beaker with a blank label while a pipette draws liquid from it inside the fume hood. No people.",
 "不仅如此，", "增加致癌风险"),
("K3", "人形图标胸前出现健康危害象形图",
 "A person silhouette icon with a health hazard pictogram on its chest. No people.",
 "还可能增加患癌的风险。", "", ["可能致癌"]),
# K4
("K4", "一本空白标准文本，封面上是天平图标和美国地图轮廓",
 "A blank standard document with a scales of justice icon and an outline map of the United States on its cover. No people.",
 "正因为这些危害，", "有专门的职业接触标准"),
("K4", "小研在通风柜前操作，画面旁浮现空白的情况说明书",
 "The female graduate student works at the fume hood, slightly blurred, while a blank fact sheet floats beside her.",
 "美国职业安全监管机构发布了专门标准。", "", ["二氯甲烷标准"]),
# K5
("K5", "手从试管架上取下一支样品管",
 "A gloved hand takes a sample tube from a tube rack inside the fume hood. No people.",
 "这个标准是专门针对它的危害，", "标准源于大量使用"),
("K5", "仓库里一排排化学品桶和吨桶",
 "Rows of large blue chemical drums and big bulk containers on warehouse shelves with blank labels. No people.",
 "以及它在工业上的大量使用而定的。"),
# K6
("K6", "大桶缩小成实验室的小瓶，盾牌图标不变",
 "A large drum shrinks into a small lab bottle, while a shield icon beside it stays the same size. No people.",
 "实验室里用量小得多，", "用量小，规矩不减"),
("K6", "空白法规文本上打绿勾，旁边是实验室小瓶",
 "A blank regulation document with a green check next to a small lab solvent bottle. No people.",
 "但这项法规同样适用。"),
("K6", "小研把棕色瓶里的液体倒进二次容器中的废液瓶",
 "The female graduate student pours liquid from a brown bottle into a waste bottle standing in a secondary container inside the fume hood.",
 "重视它的危害，"),
("K6", "通风柜、护目镜、手套、废液瓶四个打勾图标",
 "Four icons with green checks: a fume hood, goggles, gloves and a waste bottle in a tray. No people.",
 "确保控制措施真正有效。"),
# 小结
("小结", "欣欣身旁浮现心脏、肝脏、大脑图标",
 "The panda mascot stands beside floating icons of a heart, a liver and a brain.",
 "伤心伤肝伤脑，还可能致癌。", "小结"),
("小结", "空白标准文本和实验室小瓶并排",
 "A blank standard document next to a small lab solvent bottle. No people.",
 "专门标准，实验室同样适用。"),
("小结", "欣欣举着空白的本实验室规程",
 "The panda mascot holds up a blank laboratory procedure binder.",
 "本课不替代本实验室的操作规程。"),
("小结", "阿杰点头，拿起培训通知走向培训室",
 "The young male student nods and walks toward a training room holding the blank notice.",
 "阿杰明白了，先去参加培训。"),
# 结尾
("结尾", "欣欣在关好的通风柜旁挥手道别",
 "The panda mascot waves goodbye at the camera beside a tidy fume hood with its sash closed.",
 "用量再小也认真，下次见！"),
]
