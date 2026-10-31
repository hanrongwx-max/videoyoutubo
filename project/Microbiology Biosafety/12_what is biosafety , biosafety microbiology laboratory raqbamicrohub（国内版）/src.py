# 12_what is biosafety , biosafety microbiology laboratory raqbamicrohub 卡通剧本作者源
# 原片为单页无配音定义幻灯片：生物安全 = 用规范操作 + 安全设备 + 专门设施，保护工作人员、社区和环境，
# 免受感染因子、毒素等的意外暴露与无意释放。保留全部知识点 K1–K4，
# 审查补充 S1–S3（生物安全 vs 生物安保；三要素配套；守住环境+病原分级方向）。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "什么是生物安全",
    "points": {
        "K1": "生物安全：操作+设备+设施",
        "K2": "保护工作人员、社区和环境",
        "K3": "防意外暴露与无意释放",
        "K4": "三要素合成一套防护体系",
        "S1": "生物安全防意外，生物安保防人为",
        "S2": "三要素配套，防护才有效",
        "S3": "守住环境：病原不外泄",
    },
    "avoid": ["raqbamicrohub", "Ragba Micro Hub", "Ragba", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在微生物实验室门口，向镜头招手",
 "The panda mascot stands at the door of a microbiology lab and waves at the camera.",
 "这一课讲：什么是生物安全。", "什么是生物安全"),
("开场", "欣欣身旁出现一个生物危害警示图标",
 "The panda mascot beside a biohazard warning sign. No text.",
 "一句话，弄懂这个词。"),
# 情景
("情景", "阿杰第一天走进微生物实验室，有点紧张",
 "The young male student enters a microbiology lab for the first time, looking a bit nervous.",
 "阿杰第一天进微生物实验室。"),
("情景", "小研迎上来，欣欣也出现",
 "The female graduate student greets him; the panda mascot appears too.",
 "小研说：先懂生物安全是什么。"),
# K1
("K1", "三个并排的空白图标：操作手册、安全柜、实验楼",
 "Three blank icons in a row: a manual, a safety cabinet, and a lab building. No people.",
 "生物安全靠三样东西。", "什么是生物安全", ["操作", "设备", "设施"]),
("K1", "一本操作手册图标",
 "A procedure-manual icon. No people.",
 "规范的操作方法，"),
("K1", "一台安全设备图标",
 "A safety-equipment icon. No people.",
 "专门的安全设备，"),
("K1", "一栋专门设计的实验楼图标",
 "A specially designed lab-building icon. No people.",
 "和专门设计的实验室。"),
# K2
("K2", "工作人员、人群、环境三个图标",
 "Three icons: a worker, a community, and the environment. No people shown in detail.",
 "目的是保护三方。", "保护谁"),
("K2", "一个工作人员图标被盾牌护住",
 "A worker icon covered by a shield. No people shown in detail.",
 "保护工作人员，"),
("K2", "人群和环境图标被盾牌护住",
 "A community icon and an environment icon covered by a shield. No people shown in detail.",
 "也保护社区和环境。"),
# K3
("K3", "一个意外暴露的图标被打叉",
 "An accidental-exposure icon marked with a red cross. No people.",
 "防意外暴露。", "防什么"),
("K3", "一滴病原意外泄漏的图标被打叉",
 "An unintentional-release droplet icon marked with a red cross. No people.",
 "防病原意外泄漏。"),
("K3", "感染因子和毒素图标被挡住",
 "Infectious-agent and toxin icons blocked by a barrier. No people.",
 "挡住感染因子、毒素等危害。"),
# K4
("K4", "三个要素图标合成一面盾牌",
 "Three element icons merging into one shield. No people.",
 "三要素合起来，是一套防护。", "一套体系"),
("K4", "欣欣竖起一根手指提醒",
 "The panda mascot raises one finger as a reminder.",
 "少一样，防护就有漏洞。"),
# S1
("S1", "左边一个意外跌倒图标，右边一个小偷图标",
 "Left: an accident icon. Right: a thief icon. No people shown in detail.",
 "生物安全，防的是意外。", "安全与安保"),
("S1", "一把锁和一个被打叉的小偷",
 "A padlock next to a thief icon marked with a red cross. No people shown in detail.",
 "防人为盗用，那是生物安保。"),
# S2
("S2", "三个环扣成一条链",
 "Three links joined into one chain. No people.",
 "三要素要配套使用。", "配套才有效"),
("S2", "链子缺了一环，断开了",
 "A chain with one link missing, broken apart. No people.",
 "缺一环，就可能出事。"),
# S3
("S3", "一个高压灭菌器把废物处理后再出门",
 "An autoclave treating waste before it leaves the lab. No people.",
 "病原不能随意排放。", "守住环境"),
("S3", "感染性废物袋经灭菌后打上对勾",
 "An infectious-waste bag with a green check after sterilization. No people.",
 "感染性废物，先灭菌再处理。"),
("S3", "欣欣举起一张分级卡",
 "The panda mascot holds up a blank classification card.",
 "按危害分级，国内第一类最危险。"),
# 小结
("小结", "欣欣身旁排开操作、设备、设施三个图标",
 "The panda mascot stands beside three icons: a manual, equipment, and a building. No text.",
 "操作、设备、设施，护人护环境。"),
("小结", "欣欣对镜头点头",
 "The panda mascot nods at the camera.",
 "这就是生物安全。"),
# 结尾
("结尾", "欣欣在实验室门口向镜头挥手告别",
 "The panda mascot waves goodbye at the lab door.",
 "守好第一课，平安做实验。"),
]
