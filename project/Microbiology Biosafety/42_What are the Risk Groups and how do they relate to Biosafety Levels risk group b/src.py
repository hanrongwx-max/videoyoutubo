# 42_What are the Risk Groups and how do they relate to Biosafety Levels risk group b 卡通剧本作者源
# 原片（无语音的文字幻灯片）讲国际危害组 RG1–4 与防护级别 BSL-1–4 的对应：保留 K1–K10，
# 原著版：完全照原片，K1–K10，无补充知识点；危害组照原片 RG1→RG4 递增并与 BSL-1～4 一一对应，示例菌种照原片，不加国内分类方向说明
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "风险组是什么？与生物安全等级有何关系",
    "edition": "原著版",
    "points": {
        "K1": "危害组：按对人的风险分",
        "K2": "第1组：个体低、群体低",
        "K3": "第2组：个体中、群体低",
        "K4": "第3组：个体高、群体低到中",
        "K5": "第4组：个体高、群体高",
        "K6": "防护级别：规定怎么防",
        "K7": "一级：对应第1组，基本防护",
        "K8": "二级：准入、防护用品、安全柜",
        "K9": "三级：受控进入、负压房间",
        "K10": "四级：全身防护服、专门设施、高效过滤",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在四把彩色锁和四扇实验室门之间，向镜头招手",
 "The panda mascot stands between four colored locks and four lab doors, and waves at the camera.",
 "这一课讲危害组和防护级别。", "危害组与防护级别：别把顺序记反"),
# 情景
("情景", "阿杰看着几张空白的菌种资料卡，皱眉",
 "The young male student frowns at several blank strain info cards.",
 "阿杰：资料上写着第几组，啥意思？"),
("情景", "阿杰挠头，头顶两个箭头打架",
 "The young male student scratches his head; two arrows above him point in opposite directions.",
 "又说要在几级实验室做，怎么对应？"),
("情景", "小研拿着两张卡片走过来",
 "The female graduate student walks over holding two blank cards, one with a globe icon and one with a shield icon.",
 "小研：先看危害组，再看防护级别。"),
# K1
("K1", "四把彩色锁排成一排，旁边一个微生物图标",
 "Four colored padlocks in a row, numbered only by one to four dots, next to a microbe icon. No people.",
 "危害组，是按生物因子对人的风险来分的。", "危害组：按对人的风险分"),
("K1", "一个人形和一群人形图标",
 "One person outline on the left and a crowd of person outlines on the right. No people.",
 "看两头：对个人的风险，对人群的风险。", "", ["个体风险", "群体风险"]),
# K2
("K2", "第一把锁亮起绿色，人与人群都打绿勾",
 "The first padlock lights up green; one person and a crowd icon both have green check marks. No people.",
 "第1组：个人和人群的风险都低。", "第1组：个体低、群体低", ["第1组"]),
("K2", "培养皿里一株普通实验室菌株",
 "A petri dish with a plain non-harmful laboratory strain colony. No people.",
 "比如常用的大肠杆菌实验株。"),
# K3
("K3", "第二把锁亮起黄色，个人图标带黄色感叹号",
 "The second padlock lights up yellow; a single person icon has a yellow exclamation mark, the crowd icon a green check. No people.",
 "第2组：个人风险中等，人群风险低。", "第2组：个体中、群体低", ["第2组"]),
("K3", "一个杆状细菌图标，旁边肠胃图标",
 "A rod-shaped bacterium icon next to a simple stomach icon. No people.",
 "比如沙门菌，会致病，但不易大范围传播。"),
# K4
("K4", "第三把锁亮起橙色，个人图标带橙色三角",
 "The third padlock lights up orange; a person icon has an orange warning triangle, the crowd icon a small yellow mark. No people.",
 "第3组：个人风险高，人群风险低到中。", "第3组：个体高、群体低到中", ["第3组"]),
("K4", "肺部图标旁一个杆菌图标",
 "A lung icon next to a slender rod bacterium icon. No people.",
 "比如结核分枝杆菌。"),
# K5
("K5", "第四把锁亮起红色，个人和人群都带红色三角",
 "The fourth padlock lights up red; both the person icon and the crowd icon have red warning triangles. No people.",
 "第4组：个人和人群的风险都高。", "第4组：个体高、群体高", ["第4组"]),
("K5", "一个丝状病毒剪影图标，周围红框",
 "A simple thread-shaped virus silhouette icon inside a red frame. No people.",
 "比如埃博拉病毒，风险最高。"),
# K6
("K6", "戴手套的手举着生物危害警示牌",
 "A gloved hand holds up a biohazard warning sign. No people.",
 "防护级别，规定操作这些因子要怎么防。", "防护级别：规定怎么防"),
("K6", "四扇实验室门，门上盾牌一到四个",
 "Four lab doors in a row, with one, two, three and four shield icons on them. No people.",
 "从一级到四级，一级比一级严。", "", ["一级", "二级", "三级", "四级"]),
# K7
("K7", "第一扇门打开，里面是普通台面和洗手池",
 "The first door opens onto a simple open lab bench with a hand-washing sink. No people.",
 "一级，对应第1组。", "一级：对应第1组，基本防护"),
("K7", "实验服、手套、洗手图标",
 "Icons of a lab coat, gloves and hand washing. No people.",
 "做好基本防护和良好操作就可以。"),
# K8
("K8", "第二扇门，门上生物危害标志，门禁闪绿灯",
 "The second door with a biohazard warning sign and an access card reader with a green light. No people.",
 "二级，对应第2组。", "二级：准入、防护用品、安全柜"),
("K8", "小研刷卡进入，穿实验服戴手套护目镜",
 "The female graduate student swipes her card and enters, wearing a lab coat, gloves and safety goggles.",
 "限制进入，穿戴好个人防护，"),
("K8", "小研在生物安全柜里操作",
 "The female graduate student works inside a biosafety cabinet with the sash at working height.",
 "可能产生气溶胶的操作，进安全柜。"),
# K9
("K9", "第三扇门，缓冲间两道门，压差表图标",
 "The third door leads into an anteroom with two doors and a pressure gauge icon. No people.",
 "三级，对应第3组。", "三级：受控进入、负压房间"),
("K9", "气流箭头从走廊流向实验室内",
 "Blue airflow arrows flow from the corridor into the lab room through the anteroom. No people.",
 "严格控制进入，房间保持负压，空气只进不出。"),
# K10
("K10", "第四扇门，厚重密封门",
 "The fourth door is a heavy sealed door with a red light above it. No people.",
 "四级，对应第4组。", "四级：全身防护服、专门设施、高效过滤"),
("K10", "全身防护服图标、专门建筑、过滤器图标",
 "Icons of a full-body protective suit with an air hose, a separate building and a HEPA filter. No people.",
 "全身防护服、专门实验室、高效过滤。", "", ["全身防护服", "专门设施", "高效过滤"]),
# 小结
("小结", "欣欣身旁浮现四把锁和四扇门",
 "The panda mascot stands beside four floating padlocks and four lab doors.",
 "危害组看风险，防护级别管措施。", "小结"),
("小结", "四把锁从绿到红依次亮起",
 "Four colored locks light up from green to red. No people.",
 "第1组最低，第4组最高。"),
("小结", "四把锁和四扇门一一连线",
 "Lines connect each of the four locks to one of the four lab doors. No people.",
 "第几组，就对应几级防护。"),
# 结尾
("结尾", "欣欣和阿杰在二级实验室门口挥手",
 "The panda mascot and the young male student wave goodbye at a lab door with a biohazard warning sign.",
 "分清方向，选对级别，下次见！"),
]
