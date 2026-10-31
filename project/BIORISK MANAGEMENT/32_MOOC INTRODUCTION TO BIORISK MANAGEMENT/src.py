# 32_MOOC INTRODUCTION TO BIORISK MANAGEMENT 卡通剧本作者源
# 原片为 1 分钟无声招生短片：生物风险管理在线课程、职业方向、生物安保与生物安全管理、三条口号，
# 素材画面有采血管、注射器与利器盒、移液。
# 原著版：完全照原片，只有知识点 K1–K7；素材画面照原片作背景，不加针头处置、转运和国内法规补充。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "生物风险管理导论",
    "edition": "原著版",
    "points": {
        "K1": "欢迎来到生物风险管理",
        "K2": "新的职业：生物风险管理者",
        "K3": "五周在线课程，系统学习",
        "K4": "既管安全，也管安保",
        "K5": "身边的风险源",
        "K6": "报名，积极参与",
        "K7": "了解、警觉、安全",
    },
    "avoid": ["UMS", "Universiti Malaysia Sabah", "University Malaysia Sabah", "Malaysia Sabah", "Commonwealth of Learning",
              "COL", "MOOC4DEV", "mooc4dev", "MOOC", "Rodrigues", "Kenneth", "Ainatul", "Ramlie", "Zulfadlee", "Nasyir",
              "Norazzaleza", "Bertly", "FEELject", "FEEL ject"],
}

SHOTS = [
# 开场
("开场", "欣欣站在电脑屏幕旁，屏幕上是空白的课程页面",
 "The panda mascot stands beside a computer screen showing a blank online course page and waves at the camera.",
 "这一课，带你走进生物风险管理。", "走进生物风险管理"),
# 情景
("情景", "阿杰在宿舍用笔记本电脑浏览，屏幕上一个空白招生横幅",
 "The young male student browses on a laptop in a dorm; the screen shows a blank course banner with a microbe pictogram.",
 "阿杰刷到一门在线课，很感兴趣。"),
("情景", "阿杰转头问小研，头上冒出问号",
 "The young male student turns to ask the female graduate student, with a question mark above his head.",
 "生物风险管理，到底管些什么？"),
("情景", "小研笑着在白板上画一个大圆圈",
 "The female graduate student smiles and draws a big circle on a whiteboard.",
 "小研说：咱们一起来看看。"),
# K1
("K1", "一扇门打开，门内是整洁的实验室和各种安全图标",
 "A door opens to reveal a tidy lab with floating safety icons: gloves, a cabinet, a checklist. No people.",
 "生物风险管理，是一个专门的领域，", "欢迎来到生物风险管理"),
("K1", "人、样本、实验室三个图标被一个圆环围住",
 "Icons of a person, a sample tube and a lab building enclosed by one protective ring. No people.",
 "目标是让人、样本和环境都安全。"),
# K2
("K2", "王老师胸前挂着空白工牌，在实验室巡查",
 "The safety administrator wearing a blank badge walks through the lab with a blank checklist.",
 "这个领域，正需要专门的管理者。", "新的职业：生物风险管理者"),
("K2", "评估表、盾牌、培训课堂三个图标连成一排",
 "Three icons in a row: a risk assessment form, a shield and a small classroom. No people.",
 "他们做评估、定措施、搞培训。", "", ["评估", "措施", "培训"]),
("K2", "阿杰眼睛一亮，头上冒出一个灯泡",
 "The young male student's eyes light up with a light bulb above his head.",
 "这也可以是一条职业道路。"),
# K3
("K3", "一张五格日历，每格一个书本图标",
 "A calendar with five weekly boxes, each with a book icon. No people.",
 "这门在线课共五周，免费开放，", "五周在线课程，系统学习", ["五周", "在线", "免费"]),
("K3", "阿杰戴耳机在电脑前做笔记",
 "The young male student wears headphones and takes notes in front of a laptop.",
 "可以一步步系统地学。"),
# K4
("K4", "两格对比：打翻的试管图标和上锁的样品柜",
 "Two panels: a tipped-over tube icon on the left, a locked sample cabinet on the right. No people.",
 "课程讲两样：生物安全和生物安保。", "既管安全，也管安保", ["生物安全", "生物安保"]),
("K4", "左格试管加上防护盾",
 "A shield appears over the tipped-over tube icon. No people.",
 "安全，是防止意外暴露和泄漏；"),
("K4", "右格样品柜加上门禁和登记本",
 "An access card reader and a logbook appear next to the locked sample cabinet. No people.",
 "安保，是防止丢失、被盗和滥用。"),
# K5
("K5", "欣欣指着桌上的样本管、针筒和利器盒图标",
 "The panda mascot points at a table with icons of a capped sample tube, a syringe and a yellow sharps container.",
 "实验室里，风险源就在手边：", "身边的风险源", ["样本管", "针筒", "利器盒"]),
("K5", "戴手套的手稳稳拿着一支盖紧的样本管",
 "A gloved hand holds a tightly capped blank sample tube steadily. No people.",
 "血液等样本，可能带有病原；"),
("K5", "针头图标和一个小红色警示",
 "A syringe needle icon with a small red warning sign. No people.",
 "针头锐器，可能刺伤皮肤；"),
("K5", "小研在实验台上向孔板加样",
 "The female graduate student pipettes into a multi-well plate at a laboratory bench.",
 "移液加样，可能产生气溶胶。"),
# K6
("K6", "阿杰在空白报名页面点击提交按钮",
 "The young male student clicks a blank submit button on a laptop screen.",
 "感兴趣，就报名，", "报名，积极参与"),
("K6", "阿杰和其他学员在空白讨论区交流图标",
 "Chat bubble icons on a blank forum page, the young male student typing a question.",
 "跟着课程积极参与讨论。"),
# K7
("K7", "欣欣举起三块空白牌子，上面分别是书、眼睛、盾牌图标",
 "The panda mascot holds up three blank signs with a book icon, an eye icon and a shield icon.",
 "最后记住三句话：", "了解、警觉、安全", ["保持了解", "保持警觉", "保持安全"]),
("K7", "书本图标发亮",
 "The book icon glows brightly. No people.",
 "持续了解新知识和新规定，"),
("K7", "眼睛图标和盾牌图标依次发亮",
 "The eye icon and then the shield icon glow brightly. No people.",
 "对异常保持警觉，守住生物安全。"),
# 小结
("小结", "欣欣身旁是课程页、样本管、针筒和利器盒图标",
 "The panda mascot beside icons of a course page, a sample tube, a syringe and a sharps container.",
 "生物风险管理，既管安全也管安保。", "小结"),
("小结", "五格日历和书、眼睛、盾牌三个图标",
 "A five-week calendar next to a book icon, an eye icon and a shield icon. No people.",
 "五周课程，保持了解、警觉和安全。"),
# 结尾
("结尾", "欣欣和小研、阿杰、王老师一起挥手",
 "The panda mascot waves goodbye with the female graduate student, the young male student and the safety administrator.",
 "学起来，用起来，下次见！"),
]
