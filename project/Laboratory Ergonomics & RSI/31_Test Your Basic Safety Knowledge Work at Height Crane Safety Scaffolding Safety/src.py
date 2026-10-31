# 31_Test Your Basic Safety Knowledge Work at Height Crane Safety Scaffolding Safety 卡通剧本作者源
# 原著版：完全照原片（网站在线考试栏目录屏，选高处作业测验，主讲人随手作答得 20% 未通过），
# K1–K6，不加补充知识点、不做本土化；保留原片的考试规则（10 题、10 分钟、80% 通过、首次通过仅 18 人）、
# 主题清单、录屏中能辨认的 4 道题及其答案，和“首次答题前先读文章”的建议
# 网站名、频道名、广告和“请点链接”不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "基础安全测验：高处作业、起重、脚手架与消防",
    "edition": "原著版",
    "points": {
        "K1": "考试形式：先学再考",
        "K2": "高处作业有哪些风险",
        "K3": "有坠落风险就要防护",
        "K4": "选梯子看四样",
        "K5": "防坠落装备用前必查",
        "K6": "救援计划为了尽快救人",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "hsestudyguide"],
}

SHOTS = [
# 开场
("开场", "欣欣站在梯子旁，举起一张空白答卷",
 "The panda mascot stands next to a step ladder holding up a blank answer sheet and waves at the camera.",
 "高处作业小测验，看看能不能一次过关！", "高处作业：争取一次过关"),
# 情景
("情景", "阿杰坐在电脑前，屏幕上一排空白主题卡片",
 "The young male student sits at a computer whose screen shows a row of blank topic cards.",
 "阿杰打开安全知识在线考试。"),
("情景", "阿杰挑中梯子图标的卡片",
 "The young male student clicks a card with a ladder icon on the screen.",
 "他选了高处作业这一套。"),
# K1
("K1", "一排主题卡片：射线、水压、化学品、脚手架、施工、电气",
 "A row of topic cards: a radiation trefoil, a pressure gauge, a chemical bottle, scaffolding, a crane hook and a lightning bolt. No people.",
 "射线、水压、化学品、脚手架、施工、电气。", "考试形式：先学再考"),
("K1", "第二排卡片：工作场所、梯子、起重机、受限空间、火焰、土坑",
 "A second row of topic cards: a factory, a ladder, a crane, a manhole, a flame and a trench. No people.",
 "还有工作场所、高处、起重、受限空间、消防、开挖。"),
("K1", "空白测验框：十格进度条和计时器",
 "A blank quiz panel with ten progress segments and a countdown timer. No people.",
 "每套十题十分钟，答对八题才算过。", "", ["10题", "10分钟", "80%过关"]),
("K1", "一大群人只有少数打勾",
 "A crowd of small person icons where only a few have green checks above them. No people.",
 "几百人考过，第一次就过的只有18人。", "", ["首次通过18人"]),
# K2
("K2", "测验框上方一页空白文章，阿杰直接往下拉",
 "Above the quiz panel there is a blank article page, and the young male student scrolls past it.",
 "测验上面有一篇文章，阿杰没看。", "高处作业有哪些风险"),
("K2", "三个图标：坠落的人、断裂的挂钩、风雨云",
 "Three icons: a falling person, a broken hook and a wind and rain cloud. No people.",
 "文章讲高处作业的风险。", "", ["坠落", "设备失效", "环境因素"]),
("K2", "老李站在梯子上，窗外刮风",
 "The facility engineer stands on a ladder indoors while strong wind blows outside the window.",
 "人会坠落，设备会失效，环境也会添乱。"),
# K3
("K3", "四张卡片：高楼、夜晚月亮、警示三角、雨伞",
 "Four cards: a tall building, a night moon, a warning triangle and an umbrella. No people.",
 "第一题：什么时候要防坠落保护？", "有坠落风险就要防护"),
("K3", "高楼、月亮、雨伞三张卡片打叉",
 "The tall building, night moon and umbrella cards are crossed out with red X marks. No people.",
 "不是只在高楼、夜里或下雨才要。"),
("K3", "人站在平台边缘，旁边护栏和安全带图标",
 "A person icon near a platform edge, with a guardrail icon and a harness icon beside it. No people.",
 "只要有从高处坠落的风险，就要防护。"),
# K4
("K4", "价格标签、颜色色卡、卷尺图标打叉",
 "A price tag icon, a color swatch icon and a tape measure icon, all crossed out with red X marks. No people.",
 "第二题：选梯子要考虑什么？", "选梯子看四样"),
("K4", "四个图标：高度尺、砝码、材质块、任务卡",
 "Four icons: a height ruler, a weight, a material sample block and a task card. No people.",
 "高度、承重、材质，还有干什么活。", "", ["高度", "承重", "材质", "任务"]),
("K4", "老李对着梯子比划要干的活",
 "The facility engineer looks at a ladder and points up at the task he needs to do.",
 "不是只看价钱、颜色或者长短。"),
# K5
("K5", "老李检查安全带的织带和挂钩",
 "The facility engineer inspects the webbing and hook of a full body harness.",
 "第三题：防坠落装备多久查一次？", "防坠落装备用前必查"),
("K5", "一年、半年、坏了才查的日历图标打叉",
 "Calendar icons for yearly and half-yearly checks and a broken icon, all crossed out. No people.",
 "不是一年、半年，也不是坏了才查。"),
("K5", "空白说明书和带勾的检查记录",
 "A blank manufacturer manual and a blank inspection record with a check mark. No people.",
 "每次用前查，再按厂家建议定期查。"),
# K6
("K6", "老李挂在安全带上，悬在半空",
 "The facility engineer hangs from his harness lanyard below a beam after a fall, holding still.",
 "第四题：为什么要有救援计划？", "救援计划为了尽快救人"),
("K6", "炫耀、盖章、多加小心三个图标打叉",
 "Three icons crossed out with red X marks: a person showing off, a stamp on a form and a caution hand. No people.",
 "不是做给领导看，也不只为合规。"),
("K6", "保卫处值班员推来移动平台把老李接下",
 "The security officer brings a mobile platform and helps the facility engineer down safely.",
 "是为了出事时迅速、安全地把人救下。"),
# K1
("K1", "阿杰的屏幕显示一个大大的20%和红叉",
 "The young male student looks at his screen showing a large red cross and a low score bar.",
 "阿杰随手乱选，只得了20%。", "", ["20%", "未通过"]),
("K1", "结果页逐题显示正确选项",
 "A result page lists each question with the correct option highlighted in green. No people.",
 "结果页会告诉你每题的正确答案。"),
("K1", "阿杰认真翻看那篇文章",
 "The young male student scrolls back up and reads the article carefully.",
 "第一次答题前，先把文章读一遍。"),
# 小结
("小结", "欣欣站在白板前，一排图标：文章、护栏、梯子",
 "The panda mascot stands at a whiteboard with icons of an article, a guardrail and a ladder.",
 "先读材料；有坠落风险就防护；选梯看四样。", "小结"),
("小结", "检查表和救援平台图标",
 "Icons of a checklist and a mobile rescue platform. No people.",
 "装备用前查，救援计划为救人。"),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye next to the ladder.",
 "先学再考，争取一次过关，下次见！"),
]
