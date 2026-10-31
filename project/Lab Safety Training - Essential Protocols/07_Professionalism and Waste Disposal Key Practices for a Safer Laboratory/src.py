# 07_Professionalism and Waste Disposal Key Practices for a Safer Laboratory 原著版卡通剧本作者源
# 完全照原片：K1–K9（不恶作剧不打闹、护目镜戴在眼睛上、别把什么都倒下水道、
# 有些物质可以进入市政污水和污水处理厂但要查 SDS 和当地要求确认、全流程靠素养条理沟通），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "职业素养与废物处置：实验室安全要点",
    "edition": "原著版",
    "points": {
        "K1": "安全文化差，多因不专业",
        "K2": "人人负责，行事审慎",
        "K3": "不恶作剧、不打闹、守伦理",
        "K4": "护目镜戴在眼睛上",
        "K5": "手套、口罩、呼吸器、面屏按需戴",
        "K6": "防护不到位，最不专业",
        "K7": "别什么都往下水道倒",
        "K8": "能不能排，查说明书和当地规定",
        "K9": "全流程靠素养、条理和沟通",
    },
    "avoid": ["Atlantic", "Atlantic Training"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一排贴着空白标签的废液桶旁",
 "The panda mascot stands beside a neat row of waste containers with blank labels in a lab corner and waves at the camera.",
 "这一课讲职业素养和废物处置。", "职业素养与废物处置"),
("开场", "握手、护目镜、废液桶、对话气泡四个图标",
 "Four icons in a row: a handshake, safety goggles, a waste container and a speech bubble. No people.",
 "守规矩、戴防护、管废物、多沟通。", "", ["守规矩", "戴防护", "管废物", "多沟通"]),
# 情景
("情景", "阿杰安静地听欣欣讲课，认真点头",
 "The young male student listens attentively to the panda mascot and nods seriously.",
 "阿杰听得很认真。"),
("情景", "欣欣竖起大拇指",
 "The panda mascot gives the young male student a thumbs up.",
 "欣欣说：你是个好听众，这很难得。"),
# K1
("K1", "欣欣站在杂乱的实验台旁皱眉",
 "The panda mascot frowns beside a messy lab bench with scattered bottles.",
 "安全文化差的地方，常见的就是不专业。", "安全文化差，多因不专业"),
("K1", "欣欣对阿杰微笑",
 "The panda mascot smiles at the young male student.",
 "很高兴，你不是那样的人。"),
# K2
("K2", "实验室成员围在一起，每人头上一个盾牌图标",
 "Lab members including the older man, the female graduate student and the young male student stand together, each with a small shield icon above.",
 "每个人都要出一份力，建设安全文化。", "人人负责，行事审慎"),
("K2", "小研动手前认真核对步骤",
 "The female graduate student carefully checks a blank procedure sheet before starting work.",
 "人人负责，凡事审慎。"),
# K3
("K3", "两人在实验室追逐打闹的图标，打叉",
 "An icon of two people chasing and playing pranks in a lab, crossed out with a big red X. No people.",
 "不搞恶作剧，不打闹嬉戏。", "不恶作剧、不打闹、守伦理"),
("K3", "天平图标，代表伦理",
 "A balance scale icon with a green check, standing for ethics. No people.",
 "一切按伦理规范来，这个以后细讲。"),
# K4
("K4", "欣欣举起一副护目镜",
 "The panda mascot holds up a pair of safety goggles seriously.",
 "再强调一次个体防护。", "护目镜戴在眼睛上"),
("K4", "阿杰把额头上的护目镜拉下来戴好",
 "The young male student pulls his safety goggles down from his forehead to properly cover his eyes.",
 "护目镜戴在眼睛上，不是额头上。"),
# K5
("K5", "手套、口罩、呼吸器、面屏四个图标",
 "Four icons: protective gloves, a face mask, a half-face respirator and a face shield. No people.",
 "戴合适的手套，戴口罩、呼吸器和面屏。", "手套、口罩、呼吸器、面屏按需戴"),
# K6
("K6", "没戴防护的小人图标，打叉",
 "A pictogram of a person without goggles or gloves, crossed out with a red X. No people.",
 "防护缺失、不合适、用得不对，", "防护不到位，最不专业"),
("K6", "空白评分表上打了低分图标",
 "A blank evaluation sheet with a thumbs-down icon. No people.",
 "最能看出一个人不专业。"),
# K7
("K7", "欣欣竖起一根手指",
 "The panda mascot raises one finger.",
 "最后一件事：废物处置。", "别什么都往下水道倒"),
("K7", "阿杰端着烧杯走向水槽，被打叉",
 "The young male student carries a beaker of used solution toward a lab sink; the scene is crossed out with a red X.",
 "拜托，别什么都往下水道里倒。"),
# K8
("K8", "下水管连到城市污水处理厂的图标",
 "A drain pipe icon leading to a municipal wastewater treatment plant icon. No people.",
 "有些东西，确实可以进市政污水处理。", "能不能排，查说明书和当地规定"),
("K8", "小研查看空白说明书的废弃处置部分",
 "The female graduate student reads the disposal section of a blank safety data sheet.",
 "但要查安全技术说明书，", "", ["说明书", "当地规定"]),
("K8", "小研对照一本空白的当地规定手册",
 "The female graduate student checks a blank local regulations booklet next to the sink.",
 "还要查当地要求，确认了才行。"),
# K9
("K9", "订购、使用、处置、消毒四个图标连成一圈",
 "Four icons connected in a loop: a shopping cart, a hand with a flask, a waste container and a spray bottle. No people.",
 "从订购、操作、使用，到处置、消毒，", "全流程靠素养、条理和沟通"),
("K9", "小研、阿杰、老周在实验室里交流",
 "The female graduate student, the young male student and the older man talk together in a tidy lab.",
 "素养、条理和沟通，决定实验室行为。", "", ["素养", "条理", "沟通"]),
("K9", "拼图块拼合在一起",
 "Puzzle pieces with a handshake, goggles and a waste container icon snapping together. No people.",
 "看，这些是不是都连起来了？"),
# 小结
("小结", "欣欣身旁浮现握手和护目镜图标",
 "The panda mascot stands beside floating icons of a handshake and safety goggles.",
 "不打闹，守伦理，防护戴到位。", "小结"),
("小结", "说明书和当地规定两个图标",
 "Two icons: a blank data sheet and a blank local rule booklet beside a drain. No people.",
 "倒之前先查说明书和当地规定。"),
# 结尾
("结尾", "欣欣在整洁的实验室里挥手道别",
 "The panda mascot waves goodbye at the camera in a clean, tidy lab.",
 "专业做事，安全实验，下次见！"),
]
