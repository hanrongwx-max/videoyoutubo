# 03_Fundamentals of Laboratory Safety Safety Resources Scenario 卡通剧本作者源
# 原片为情景思考题（只提问不作答）：保留 K1–K4，审查补出答案 S1–S5
# （防护用品不出实验区、安全手册·SOP·SDS、实验室安全员与负责人、学院安全管理员与学校主管部门、友善提醒与反映）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "安全问题找谁问",
    "points": {
        "K1": "办公区里的实验服",
        "K2": "担心暴露：这样做允许吗",
        "K3": "有哪些安全资源可以求助",
        "K4": "本课不能代替本实验室规程",
        "S1": "实验服不出实验区",
        "S2": "查手册、规程和SDS",
        "S3": "找实验室安全员和负责人",
        "S4": "找学院和学校安全管理部门",
        "S5": "友善提醒，及时反映",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验室和办公区之间的走廊上，向镜头招手",
 "The panda mascot stands in a corridor between a laboratory door and an office area, waving at the camera.",
 "这一课：遇到安全问题，找谁问？", "安全问题找谁问"),
# 情景
("情景", "小研抱着电脑走进办公区，准备开组会",
 "The female graduate student carries a laptop into a bright open office area with desks and a meeting table.",
 "小研来到办公区，准备开组会。"),
# K1
("K1", "阿杰穿着实验服、戴着护目镜，坐在办公桌前吃零食",
 "The young male student, still wearing a lab coat and safety goggles, sits at an office desk eating a snack.",
 "她看见阿杰穿着实验服，坐在办公桌前。", "办公区里的实验服"),
("K1", "阿杰的实验服袖口有一小块污渍，旁边是会议桌",
 "Close-up of the lab coat sleeve with a small stain, resting on a shared meeting table next to papers. No people.",
 "实验服上的沾染，可能跟着进了办公区。"),
# K2
("K2", "小研皱眉思考，头顶浮现问号",
 "The female graduate student frowns thoughtfully, a question mark icon floating above her head.",
 "这会不会造成暴露？办公区允许这样吗？", "担心暴露：这样做允许吗"),
("K2", "污渍小点从实验服扩散到桌面、门把手、杯子的箭头示意",
 "Arrows showing small dots spreading from a lab coat icon to a desk, a door handle and a coffee cup icon. No people.",
 "污染会沾到桌面、门把手和水杯上。"),
# K3
("K3", "欣欣站到小研身边，伸出手掌数指头",
 "The panda mascot stands next to the female graduate student and counts on its paw.",
 "拿不准时，有哪些资源可以求助？", "有哪些安全资源可以求助"),
# S1
("S1", "实验室门内有挂衣钩，挂着实验服，门外是办公区",
 "A coat hook just inside a laboratory door with a lab coat hanging on it; the office area is visible outside the door. No people.",
 "先说规矩：实验服不出实验区。", "实验服不出实验区"),
("S1", "办公室、会议室、食堂三个图标，各有实验服图标被红叉划掉",
 "Three icons each with a crossed-out lab coat inside: an office, a meeting room, and a canteen. No people.",
 "办公室、会议室、食堂都不能穿。", "", ["办公室", "会议室", "食堂"]),
("S1", "小研在门口脱下手套，扔进废物桶，再挂好实验服",
 "The female graduate student removes her gloves at the lab door, drops them in a waste bin and hangs her lab coat on the hook.",
 "离开前脱手套、脱实验服，再洗手。"),
# S2
("S2", "书架上空白的安全手册和规程文件夹",
 "A shelf with a blank laboratory safety manual and blank procedure binders. No people.",
 "资源一：本实验室的安全手册和规程。", "查手册、规程和SDS"),
("S2", "小研翻到手册中画着实验服和护目镜的一页",
 "The female graduate student opens the manual to a page showing only icons of a lab coat, goggles and gloves.",
 "防护用品怎么穿、在哪脱，里面都有。"),
("S2", "空白SDS页面上高亮一个护目镜和手套图标",
 "A blank safety data sheet with a highlighted section showing goggles and gloves icons. No people.",
 "具体化学品的防护，查SDS的防护部分。"),
# S3
("S3", "小研胸前戴着空白的安全员袖标",
 "The female graduate student wears a blank armband marking her as the lab safety officer.",
 "资源二：实验室安全员，就在身边。", "找实验室安全员和负责人"),
("S3", "老周坐在办公室，阿杰敲门进来请教",
 "The older man sits in his office; the young male student knocks and comes in to ask a question.",
 "实验室负责人，对本室安全负总责。"),
# S4
("S4", "王老师在学院办公室，桌上摆着空白的检查表",
 "The safety administrator sits in a school office with blank inspection checklists on the desk.",
 "资源三：学院实验室安全管理员。", "找学院和学校安全管理部门"),
("S4", "学校实验室安全管理部门的楼宇图标，旁边是电话和邮件图标",
 "An icon of a university administration building with telephone and email icons beside it. No people.",
 "还有学校的实验室安全管理部门。"),
("S4", "王老师在培训室讲解防护用品，学生们认真听",
 "The safety administrator explains protective equipment to a group of students in a training room.",
 "安全培训和咨询，都可以找他们。"),
# S5
("S5", "小研微笑着走到阿杰桌边，轻声提醒",
 "The female graduate student smiles and walks over to the young male student's desk to remind him quietly.",
 "看到问题，先友善地当面提醒。", "友善提醒，及时反映"),
("S5", "阿杰不好意思地挠头，起身回实验室",
 "The young male student scratches his head sheepishly and stands up to walk back to the laboratory.",
 "阿杰马上回去，把实验服脱在室内。"),
("S5", "阿杰用湿巾擦拭刚才坐过的桌面",
 "The young male student wipes the office desk he used with a disinfectant wipe.",
 "刚才碰过的桌面，也擦拭干净。"),
("S5", "小研在空白的反映单上填写，交给王老师",
 "The female graduate student fills in a blank feedback form and hands it to the safety administrator.",
 "反复出现的问题，向安全管理员反映。"),
("S5", "王老师在组会上用空白挂图讲规定，大家点头",
 "The safety administrator speaks at a group meeting with a blank flip chart; everyone nods.",
 "提醒的是问题，不是针对人。"),
# K4
("K4", "一张空白课程卡片和一本更大的空白规程手册",
 "A small blank course card next to a larger blank procedure binder with a check mark. No people.",
 "这门课不能代替本实验室的规程。", "本课不能代替本实验室规程"),
# 小结
("小结", "欣欣身旁浮现挂起的实验服和打叉的办公桌图标",
 "The panda mascot stands beside icons of a lab coat on a hook and a crossed-out office desk.",
 "实验服、手套不出实验区。", "小结"),
("小结", "手册、SDS、安全员、管理部门四个图标排成一排",
 "Four icons in a row: a manual, a data sheet, a person with an armband, and an office building. No people.",
 "手册SDS，安全员，学院和学校。", "", ["手册", "SDS", "安全员", "管理部门"]),
("小结", "两人握手图标",
 "A handshake icon above a small speech bubble. No people.",
 "友善提醒，及时反映，大家都安全。"),
# 结尾
("结尾", "欣欣和小研、阿杰在实验室门口挥手",
 "The panda mascot, the female graduate student and the young male student wave goodbye at the laboratory door.",
 "有疑问就问，安全没小事，下次见！"),
]
