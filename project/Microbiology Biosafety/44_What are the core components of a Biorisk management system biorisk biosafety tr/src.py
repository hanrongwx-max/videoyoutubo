# 44_What are the core components of a Biorisk management system biorisk biosafety tr 卡通剧本作者源
# 原片（无语音的单页文字幻灯片）列出生物风险管理体系的六个核心组成：保留 K1–K7，
# 原著版：完全照原片，K1–K7，无补充知识点（六个组成：评估、缓解、监测、培训与能力、事件报告、持续改进）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "生物风险管理体系的核心组成",
    "edition": "原著版",
    "points": {
        "K1": "完善的体系，由六部分组成",
        "K2": "风险评估：找出并评价风险",
        "K3": "风险缓解：安全和安保措施落地",
        "K4": "绩效监测：检查、审核、演练",
        "K5": "培训与能力：持续学习",
        "K6": "事件报告：发现了就报，报了就处理",
        "K7": "持续改进：定期修订制度和规程",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "ABM"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一座六根柱子撑起的小房子前",
 "The panda mascot stands in front of a small house held up by six pillars, a biohazard symbol on its roof, and waves at the camera.",
 "这一课讲生物风险管理体系的六根支柱。", "生物风险管理体系的六根支柱"),
# 情景
("情景", "王老师通知：下月学院要检查各实验室的管理体系",
 "The safety administrator hands a blank notice to the older man in the lab office.",
 "学院下月要检查实验室的生物安全管理体系。"),
("情景", "老周把小研和阿杰叫来，桌上一堆零散的纸",
 "The older man calls over the female graduate student and the young male student; a messy pile of blank papers lies on the desk.",
 "老周发现，各种材料东一张西一张。"),
("情景", "小研拿出一张空白白板，画出六个格子",
 "The female graduate student draws six empty boxes on a whiteboard.",
 "小研说：按六个组成来理，一项项对。"),
# K1
("K1", "六根柱子依次亮起",
 "The six pillars of the small house light up one after another. No people.",
 "完善的体系，由六个部分撑起来。", "完善的体系，由六部分组成",
 ["评估", "缓解", "监测", "培训", "报告"]),
("K1", "第六根柱子亮起，上面一个循环箭头",
 "The sixth pillar lights up with a circular arrow icon. No people.",
 "缺一根，房子就不稳。", "", ["改进"]),
# K2
("K2", "第一根柱子上放大镜图标",
 "The first pillar shows a magnifying glass icon. No people.",
 "第一，风险评估。", "风险评估：找出并评价风险"),
("K2", "小研和阿杰对着空白评估表讨论",
 "The female graduate student and the young male student discuss a blank risk assessment form.",
 "找出实验里有哪些生物风险，评价大小。"),
# K3
("K3", "第二根柱子上盾牌和锁两个图标",
 "The second pillar shows a shield icon and a padlock icon. No people.",
 "第二，风险缓解。", "风险缓解：安全和安保措施落地", ["生物安全", "生物安保"]),
("K3", "小研在安全柜里操作，戴手套",
 "The female graduate student works in a biosafety cabinet wearing gloves and a lab coat.",
 "生物安全措施，防止人员意外暴露；"),
("K3", "上锁的样本冰箱和登记本",
 "A locked sample freezer with a blank sign-out logbook beside it. No people.",
 "生物安保措施，防止样本丢失、被盗。"),
# K4
("K4", "第三根柱子上仪表图标",
 "The third pillar shows a gauge icon. No people.",
 "第三，绩效监测。", "绩效监测：检查、审核、演练"),
("K4", "王老师拿着空白检查表巡查",
 "The safety administrator walks through the lab with a blank checklist on a clipboard.",
 "定期检查，看措施是否真的落实，"),
("K4", "王老师和老周翻看空白记录本",
 "The safety administrator and the older man review blank record books at a desk.",
 "审核记录，看体系是否按规定运行，"),
("K4", "小研和阿杰进行溢洒处置演练，用空白道具",
 "The female graduate student and the young male student practice a spill drill with a spill kit and a blank prop bottle.",
 "还要搞安全演练，看大家会不会处置。"),
# K5
("K5", "第四根柱子上讲台图标",
 "The fourth pillar shows a small lecture podium icon. No people.",
 "第四，培训与能力。", "培训与能力：持续学习"),
("K5", "阿杰在课堂听课，小研在旁指导操作",
 "The young male student attends a class, then practices at a bench while the female graduate student coaches him.",
 "培训不是一次了事，要持续学习，"),
("K5", "阿杰独立完成操作，小研竖起大拇指",
 "The young male student completes a task on his own and the female graduate student gives a thumbs up.",
 "确认真的会做，才算有能力。"),
# K6
("K6", "第五根柱子上警示三角和电话图标",
 "The fifth pillar shows a warning triangle and a telephone icon. No people.",
 "第五，事件报告。", "事件报告：发现了就报，报了就处理"),
("K6", "两个图标：打翻的培养皿、空了一格的样本盒",
 "Two icons: a tipped culture plate and a sample rack with one empty slot. No people.",
 "不管是意外事故，还是安保事件，", "", ["意外事故", "安保事件"]),
("K6", "小研打电话报告，老周赶来",
 "The female graduate student makes a phone call while the older man hurries over.",
 "都要有渠道及时发现、报告、处理。"),
# K7
("K7", "第六根柱子上循环箭头",
 "The sixth pillar shows a circular arrow icon. No people.",
 "第六，持续改进。", "持续改进：定期修订制度和规程"),
("K7", "老周和王老师在桌前修改空白制度文件",
 "The older man and the safety administrator revise a blank policy document together at a desk.",
 "定期回顾，把程序和制度改得更好。"),
# 小结
("小结", "欣欣站在六根柱子房子前",
 "The panda mascot stands in front of the six-pillar house.",
 "评估、缓解、监测、培训、报告、改进。", "小结"),
# 结尾
("结尾", "欣欣和老周、小研、阿杰站在稳固的房子前挥手",
 "The panda mascot, the older man, the female graduate student and the young male student wave goodbye in front of the sturdy six-pillar house.",
 "支柱立稳，安全才牢，下次见！"),
]
