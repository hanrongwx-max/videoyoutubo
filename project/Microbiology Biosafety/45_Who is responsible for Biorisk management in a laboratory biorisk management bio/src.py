# 45_Who is responsible for Biorisk management in a laboratory biorisk management bio 卡通剧本作者源
# 原片（无语音的单页文字幻灯片）讲生物风险管理的四类责任主体：保留 K1–K5，
# 原著版：完全照原片，K1–K5，无补充知识点；四方照原片：实验室主任/课题负责人、生物安全官、实验人员、机构生物安全委员会
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室生物风险管理由谁负责？",
    "edition": "原著版",
    "points": {
        "K1": "责任共担：四方一起扛",
        "K2": "实验室主任、课题负责人：抓落实",
        "K3": "生物安全官：监督与指导",
        "K4": "实验人员：守规程，报问题",
        "K5": "机构生物安全委员会：审查和批准",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "BSO", "IBC"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一条由几个人形图标连成的链条前",
 "The panda mascot stands in front of a chain of linked person icons and waves at the camera.",
 "这一课讲：实验室生物安全，到底谁负责。", "生物安全，谁来负责"),
# 情景
("情景", "生物安全柜报警灯亮着，阿杰站在旁边",
 "A biosafety cabinet shows a red alarm light while the young male student stands beside it looking unsure.",
 "安全柜报警了，阿杰心想：这不归我管。"),
("情景", "阿杰转身要走，小研叫住他",
 "The young male student turns to leave; the female graduate student calls him back.",
 "小研叫住他：发现问题，人人有责。"),
("情景", "老周走过来，三人看向墙上空白的职责图",
 "The older man walks over; the three of them look at a blank responsibility chart on the wall.",
 "老周说：咱们把责任链从头捋一遍。"),
# K1
("K1", "四个人形图标手拉手围成一圈",
 "Four person icons holding hands in a circle around a biohazard sign. No people.",
 "责任不是一个人扛，而是多方共担。", "责任共担：四方一起扛", ["负责人", "安全官", "实验人员", "委员会"]),
("K1", "每层旁边各一个人形图标亮起",
 "A person icon lights up beside each of the three levels. No people.",
 "每一方，都有自己的职责。"),
# K2
("K2", "老周站在实验室门口，胸前一个盾牌徽章",
 "The older man stands at the lab door wearing a small shield badge.",
 "先说实验室主任和课题负责人。", "实验室主任、课题负责人：抓落实"),
("K2", "老周把空白制度贴到墙上",
 "The older man pins a blank policy sheet to the lab wall.",
 "要确保安全政策在实验室落实。"),
("K2", "老周在实验室里巡看，大家都按墙上的制度操作",
 "The older man walks through the lab watching everyone follow the posted rules.",
 "政策是不是真做到了，他要盯着。"),
# K3
("K3", "王老师戴着生物安全官胸牌，拿着空白检查表巡查",
 "The safety administrator, wearing a biosafety officer badge, inspects the lab with a blank checklist.",
 "第二，生物安全官。", "生物安全官：监督与指导"),
("K3", "王老师给老周和小研讲解空白文件",
 "The safety administrator explains a blank document to the older man and the female graduate student.",
 "监督整个生物安全计划，给大家指导。"),
("K3", "王老师在白板上画出整个生物安全计划的流程图",
 "The safety administrator draws a flow chart of the whole biosafety program on a whiteboard.",
 "整个计划怎么运转，他心里有数。"),
# K4
("K4", "阿杰穿戴整齐，对照空白规程操作",
 "The young male student, fully dressed in lab coat and gloves, follows a blank procedure binder at the bench.",
 "第三，实验室里的每个工作人员。", "实验人员：守规程，报问题"),
("K4", "规程本上一行行打勾",
 "A blank procedure binder with a column of green check marks. No people.",
 "严格按规程操作，不图省事。"),
("K4", "阿杰回到报警的安全柜前，拿起电话",
 "The young male student returns to the alarming biosafety cabinet, stops work and picks up a phone.",
 "发现异常，先停下来，再报告。"),
("K4", "老李赶来检修安全柜",
 "The facility engineer arrives and inspects the biosafety cabinet.",
 "报告了，问题才能被及时处理。"),
# K5
("K5", "会议桌旁一圈人形图标，桌上空白文件",
 "A round meeting table with several person icons around it and a stack of blank documents. No people.",
 "第四，机构生物安全委员会。", "机构生物安全委员会：审查和批准"),
("K5", "空白课题书从实验室流向委员会，再回到实验室，盖章图标",
 "A blank project proposal moves by arrows from a lab door to the meeting table and back with a stamp icon. No people.",
 "涉及危险因子的研究，要经它审查，"),
("K5", "王老师把盖章的文件交给老周",
 "The safety administrator hands a stamped blank document to the older man.",
 "批准了才能开展。"),
# 小结
("小结", "欣欣站在四人手拉手的图标前",
 "The panda mascot stands in front of the four person icons holding hands.",
 "四方共担，各尽其责。", "小结"),
("小结", "老周、王老师、阿杰三个人形图标",
 "Three person icons in a row: one with a shield badge, one with a clipboard, one with gloves. No people.",
 "负责人抓落实，安全官监督，人人守规。"),
("小结", "会议桌和盖章图标",
 "A round meeting table with a stamp icon. No people.",
 "机构生物安全委员会审查批准。"),
("小结", "阿杰拿起电话报告安全柜报警",
 "The young male student picks up the phone to report the biosafety cabinet alarm.",
 "阿杰说：发现问题，我也要报告！"),
# 结尾
("结尾", "欣欣和课题组站成一排挥手",
 "The panda mascot, the older man, the female graduate student and the young male student stand in a row and wave goodbye.",
 "安全链条，人人一环，下次见！"),
]
