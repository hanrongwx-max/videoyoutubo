# 17_Safety Objective Type Q A Safety Quiz Questions & Answers Safety Quiz Safety MCQ 卡通剧本作者源
# 原著版：完全照原片（15 道安全客观题，读题后给答案），K1–K15，不加补充知识点、不做更正；
# 保留原片答案：间接成本只答损失工时（B）、直接成本医疗费和赔偿金（D）、检查表四项为工作区域 / 材料 / 机器 / 工具（A）、
# 标志颜色红禁止和危险报警 / 黄警告 / 蓝指令 / 绿应急急救、辐射危害用紫色（D）、事故三方责任、靠自己的注意力和态度、
# 火灾时首先关注自身安全（A）、正确使用防护用品靠自己（A）
# 频道名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "安全常识十五问",
    "edition": "原著版",
    "points": {
        "K1": "安全管理：减少、控制、消除危害",
        "K2": "事故的间接成本",
        "K3": "事故的直接成本",
        "K4": "危害分析检查表",
        "K5": "安全信息怎么表达",
        "K6": "安全标志的种类",
        "K7": "红色：禁止和危险",
        "K8": "黄色：警告",
        "K9": "蓝色：指令",
        "K10": "绿色：疏散和急救",
        "K11": "辐射危害用紫色",
        "K12": "事故责任三方面",
        "K13": "始终保安全靠态度",
        "K14": "火灾时先保自己",
        "K15": "防护用品自己负责",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSC StudyGuide"],
}

SHOTS = [
# 开场
("开场", "欣欣举着写有15的牌子，向镜头招手",
 "The panda mascot holds up a blank sign with a large number-shaped badge and waves at the camera.",
 "今天十五道安全常识题，一起来答。", "安全常识十五问"),
("开场", "一行图标：盾牌、钱袋、标志牌、心形",
 "A row of icons: a shield, a money bag, a safety sign and a heart. No people.",
 "管理、成本、标志、态度，一个不落。", "", ["管理", "成本", "标志", "态度"]),
# 情景
("情景", "王老师带着阿杰和小研在走廊巡查",
 "The safety administrator leads the young male student and the female graduate student on an inspection walk in a corridor.",
 "王老师带新同事巡查。"),
("情景", "阿杰看着各色标志",
 "The young male student looks at colorful safety signs on the wall.",
 "边走边问，十五道题边看边答。"),
# K1
("K1", "危险图标依次变小、被框住、消失",
 "A hazard icon shrinks, then is boxed in, then disappears. No people.",
 "第一题：安全管理管什么？", "安全管理：减少、控制、消除危害", ["减少", "控制", "消除"]),
("K1", "欣欣举起三个勾",
 "The panda mascot holds up a card with three check marks.",
 "减少、控制、消除危害，答案D。", "", ["D 以上都是"]),
# K2
("K2", "冰山图标，水下部分很大",
 "An iceberg icon with a small tip above water and a huge part below. No people.",
 "第二题：哪些是事故的间接成本？", "事故的间接成本"),
("K2", "水下部分出现时钟图标",
 "Below the water a clock icon with lost hours lights up. No people.",
 "答案B，受伤人员损失工时的成本。", "", ["B 损失工时"]),
# K3
("K3", "冰山露出水面的部分：药箱和钱袋",
 "The tip of the iceberg shows a first aid kit and a money bag. No people.",
 "第三题：直接成本呢？", "事故的直接成本"),
("K3", "欣欣指着冰山顶",
 "The panda mascot points at the tip of the iceberg.",
 "答案D，医疗费和赔偿金。", "", ["D 医疗费和赔偿"]),
# K4
("K4", "检查表四格：工作区、材料、机器、工具",
 "A blank checklist with four boxes showing icons of a work area, materials, a machine and tools. No people.",
 "第四题：危害分析检查表查什么？", "危害分析检查表", ["工作区域", "材料", "机器", "工具"]),
("K4", "四格一起打勾，人形图标那张卡打叉",
 "The four checklist boxes get green checks, while an option card with a person icon is crossed out. No people.",
 "答案A，工作区域、材料、机器、工具。", "", ["A"]),
# K5
("K5", "标志牌、彩色条纹、喇叭三个图标",
 "Three icons: a sign board, colored stripes and a loudspeaker. No people.",
 "第五题：安全信息用什么表达？", "安全信息怎么表达", ["标志牌", "颜色", "声信号"]),
("K5", "欣欣点头",
 "The panda mascot nods.",
 "标志牌、颜色、声信号，答案D都是。", "", ["D 以上都是"]),
# K6
("K6", "三类标志排成一排",
 "Three kinds of safety signs in a row: prohibition and warning, emergency and first aid, and mandatory. No people.",
 "第六题：安全标志牌有哪几种？", "安全标志的种类", ["禁止和警告", "应急和急救", "指令"]),
("K6", "三类标志一起打勾",
 "All three kinds of signs get green check marks. No people.",
 "答案D，以上都是。", "", ["D 以上都是"]),
# K7
("K7", "红圈斜杠的禁止标志：禁止烟火",
 "A red circular no-smoking prohibition sign. No people.",
 "第七题：禁止和危险用什么色？", "红色：禁止和危险"),
("K7", "红色禁止标志和红色报警器",
 "A red prohibition sign and a red danger alarm beacon. No people.",
 "答案A，红色：禁止和危险报警。", "", ["A 红色"]),
# K8
("K8", "黄色三角警告标志：当心腐蚀",
 "A yellow triangular corrosive warning sign. No people.",
 "第八题：警告用什么色？", "黄色：警告"),
("K8", "阿杰在黄色标志前放慢脚步",
 "The young male student slows down in front of a yellow warning sign.",
 "答案B，警告用黄色，也叫琥珀色。", "", ["B 黄色"]),
# K9
("K9", "蓝色圆形指令标志：必须戴护目镜",
 "A blue circular mandatory sign for eye protection. No people.",
 "第九题：指令用什么色？", "蓝色：指令"),
("K9", "阿杰戴上护目镜",
 "The young male student puts on safety goggles under the blue sign.",
 "答案C，指令用蓝色。", "", ["C 蓝色"]),
# K10
("K10", "绿色紧急出口和急救标志",
 "Green emergency exit and first aid signs. No people.",
 "第十题：疏散和急救用什么色？", "绿色：疏散和急救"),
("K10", "小研指着绿色箭头",
 "The female graduate student points along a green exit arrow.",
 "答案D，疏散和急救用绿色。", "", ["D 绿色"]),
# K11
("K11", "辐射标志旁四张颜色卡：红、橙、绿、紫",
 "A radiation hazard symbol beside four color cards: red, orange, green and purple. No people.",
 "第十一题：辐射危害用什么颜色？", "辐射危害用紫色", ["红", "橙", "绿", "紫"]),
("K11", "紫色卡片亮起打勾",
 "The purple color card lights up with a green check. No people.",
 "答案D，紫色。", "", ["D 紫色"]),
# K12
("K12", "三个图标：管理者、员工、工作环境",
 "Three icons: a manager figure, a worker figure and a workplace building. No people.",
 "第十二题：事故谁有责任？", "事故责任三方面"),
("K12", "三个图标连成三角",
 "The three icons connect into a triangle. No people.",
 "管理者、员工、环境条件，答案D。", "", ["D 以上都是"]),
# K13
("K13", "防护用品、安全员、警示牌三张卡片淡出",
 "Cards of protective gear, a safety officer badge and a warning sign fade out. No people.",
 "第十三题：什么能让你始终安全？", "始终保安全靠态度"),
("K13", "阿杰头顶亮起一颗心和一只眼睛",
 "A heart and an eye icon glow above the young male student's head.",
 "答案D，自己的注意力和安全态度。", "", ["D 注意力和态度"]),
# K14
("K14", "走廊冒烟，小研往出口走",
 "Smoke drifts in a corridor and the female graduate student walks toward the exit.",
 "第十四题：火灾时首先关注什么？", "火灾时先保自己"),
("K14", "自身安全的卡片亮起，同事和财产卡片淡出",
 "A card with a person and a shield lights up, while cards for coworkers and company property fade. No people.",
 "答案A，自身安全，不是同事或财产。", "", ["A 自身安全"]),
# K15
("K15", "阿杰对着镜子调整护目镜",
 "The young male student checks his safety goggles in a mirror.",
 "第十五题：谁确保你戴对防护用品？", "防护用品自己负责"),
("K15", "同事、安全部门、企业主卡片淡出，阿杰亮起",
 "Cards for a coworker, a safety department and a business owner fade, while the young male student is highlighted.",
 "答案A，你自己，不是同事或老板。", "", ["A 你自己"]),
# 小结
("小结", "欣欣站在标志墙前",
 "The panda mascot stands in front of a wall of colored safety signs.",
 "红禁止、黄警告、蓝指令、绿急救。", "小结"),
("小结", "紫色卡片和辐射标志",
 "A purple color card beside a radiation hazard symbol. No people.",
 "原题：辐射危害用紫色。", "", ["紫色"]),
("小结", "冰山图标",
 "The iceberg icon again. No people.",
 "间接成本是损失工时，直接是医药赔偿。"),
("小结", "心形和护目镜图标",
 "A heart icon and a pair of goggles. No people.",
 "安全靠态度，火灾先保自己，防护自己戴。"),
# 结尾
("结尾", "欣欣和三人在走廊挥手告别",
 "The panda mascot waves goodbye with the safety administrator and two colleagues in the corridor.",
 "十五问到这里，下次见！"),
]
