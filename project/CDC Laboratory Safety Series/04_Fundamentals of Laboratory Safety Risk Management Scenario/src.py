# 04_Fundamentals of Laboratory Safety Risk Management Scenario 卡通剧本作者源
# 原片为情景思考题（只提问不作答）：保留 K1–K5，审查补出答案 S1–S5
# （先停下并报告、书面风险评估、修订 SOP 与审批、培训后在指导下首次操作、变更再评估）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "新实验，先评估",
    "points": {
        "K1": "接到一项新操作",
        "K2": "先查现有风险评估和规程",
        "K3": "担心还有新的风险",
        "K4": "这时该怎么做",
        "K5": "本课不能代替本实验室规程",
        "S1": "先停下，报告负责人",
        "S2": "做书面风险评估",
        "S3": "修订规程，审批后再做",
        "S4": "培训到位，指导下首做",
        "S5": "情况变了，重新评估",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台前，举着一块空白写字板",
 "The panda mascot stands at a lab bench holding up a blank clipboard with a magnifier icon.",
 "这一课：接到新实验，第一步做什么？", "新实验，先评估"),
# K1
("K1", "老周把一张空白任务卡交给小研",
 "The older man hands a blank task card to the female graduate student in his office.",
 "老周交给小研一项新的实验操作。", "接到一项新操作"),
("K1", "小研戴紫色手套，托着一只培养皿，若有所思",
 "The female graduate student in a lab coat, goggles and purple gloves holds a closed culture dish and looks thoughtful.",
 "这是课题组以前没做过的步骤。"),
# K2
("K2", "小研翻开空白的风险评估表和规程文件夹",
 "The female graduate student opens a blank risk assessment form and a blank procedure binder on her desk.",
 "她先翻出现有的风险评估表和规程。", "先查现有风险评估和规程"),
("K2", "表格上几行打勾，最后一行是空白",
 "A blank checklist with several rows checked in green and the last row empty with a question mark. No people.",
 "可是新步骤，表上并没有写到。"),
# K3
("K3", "小研眉头紧锁，身旁浮现飞溅、气溶胶、锐器三个小图标",
 "The female graduate student frowns; small icons of a splash, a mist cloud and a needle float beside her.",
 "会不会多了溅洒、气溶胶或锐器风险？", "担心还有新的风险"),
# K4 / 情景
("K4", "阿杰凑过来，摆手说“先做了再说”，被打叉",
 "The young male student leans over and waves his hand casually; an icon of a rushing runner beside him is crossed out with a red X.",
 "阿杰说：先做了再说。这样不行。", "这时该怎么做"),
("K4", "欣欣站在小研身边，竖起手掌示意停下",
 "The panda mascot stands next to the female graduate student and raises a paw in a stop gesture.",
 "拿不准的风险，要先评估再动手。"),
# S1
("S1", "小研合上文件夹，放下培养皿",
 "The female graduate student closes the binder and puts the closed culture dish back on the bench.",
 "第一步：先停下，不擅自开始。", "先停下，报告负责人"),
("S1", "小研敲门走进老周办公室，指着空白任务卡",
 "The female graduate student knocks on the older man's office door and points to the blank task card.",
 "把担心的风险告诉实验室负责人。"),
# S2
("S2", "老周和小研对着一张空白的风险评估表讨论",
 "The older man and the female graduate student sit together and discuss a blank risk assessment form.",
 "第二步：一起做书面风险评估。", "做书面风险评估"),
("S2", "三个图标依次出现：放大镜、天平秤、盾牌",
 "Three icons appear one by one: a magnifier, a balance scale, and a shield. No people.",
 "找出危害，估计后果，定下控制措施。", "", ["识别危害", "评估风险", "控制措施"]),
("S2", "控制措施金字塔：替代、工程控制、管理、个人防护",
 "A pyramid icon with four layers: a swap arrow, a fume hood, a checklist, and goggles with gloves. No people.",
 "先替代和工程控制，再管理和个人防护。", "", ["替代", "工程控制", "管理措施", "个人防护"]),
("S2", "表格最后一栏是应急图标：洗眼器、急救箱",
 "The bottom of a blank form shows icons of an eyewash station and a first aid kit. No people.",
 "万一出事怎么处理，也要写进去。"),
# S3
("S3", "小研在电脑上修改空白规程文档",
 "The female graduate student edits a blank procedure document on a computer with a pencil icon on screen.",
 "第三步：根据评估，修订操作规程。", "修订规程，审批后再做"),
("S3", "老周在空白规程上签字",
 "The older man signs the blank procedure document with a pen.",
 "实验室负责人审核签字，才能执行。"),
("S3", "王老师在学院办公室翻看空白备案表",
 "The safety administrator reviews a blank registration form in the school office.",
 "涉及病原、危化品的，按规定报审备案。"),
# S4
("S4", "小研在王老师指导下练习，空白培训记录上打勾",
 "The female graduate student practices with a closed container under the guidance of the safety administrator; a blank training record gets a check mark.",
 "第四步：培训到位，防护和应急备好。", "培训到位，指导下首做"),
("S4", "老周站在小研身旁，看她第一次正式操作",
 "The older man stands beside the female graduate student as she performs the new procedure for the first time at a biological safety cabinet.",
 "第一次操作，请有经验的人在旁指导。"),
# S5
("S5", "循环箭头：评估、执行、复查、改进",
 "A circular arrow icon with four segments: a checklist, a hand at work, a magnifier, and a wrench. No people.",
 "第五步：做完复查，发现问题就改进。", "情况变了，重新评估", ["评估", "执行", "复查", "改进"]),
("S5", "试剂量放大、换了仪器、换了人三个图标，各带感叹号",
 "Three icons each with an exclamation mark: a larger flask, a new instrument, and a new person. No people.",
 "用量、设备、人员变了，都要重新评估。"),
("S5", "日历图标上圈出一个日期，旁边是评估表",
 "A calendar icon with one date circled next to a blank assessment form. No people.",
 "就算没变，也要定期复审。"),
# K5
("K5", "一张空白课程卡片和一本更大的空白规程手册",
 "A small blank course card next to a larger blank procedure binder with a check mark. No people.",
 "这门课不能代替本实验室的规程。", "本课不能代替本实验室规程"),
# 小结
("小结", "欣欣身旁浮现停止手掌和评估表图标",
 "The panda mascot stands beside floating icons of a raised stop hand and a blank assessment form.",
 "新操作有疑问，先停下来报告。", "小结"),
("小结", "评估表、签字笔、培训记录三个图标打勾",
 "Three icons with green checks: an assessment form, a signing pen, and a training record. No people.",
 "评估、修订、审批、培训，再动手。"),
("小结", "循环箭头图标",
 "A circular arrow icon around a small flask. No people.",
 "情况一变，重新评估。"),
# 结尾
("结尾", "欣欣和小研站在生物安全柜旁挥手",
 "The panda mascot and the female graduate student wave goodbye beside a biological safety cabinet.",
 "先评估，再动手，下次见！"),
]
