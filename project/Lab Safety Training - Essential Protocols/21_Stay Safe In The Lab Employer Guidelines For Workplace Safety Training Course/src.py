# 21_Stay Safe In The Lab Employer Guidelines For Workplace Safety Training Course 原著版卡通剧本作者源
# 完全照原片：K1–K11，保留原片“雇主—员工”的责任框架（雇主：应急预案、培训演练、维护安全设备、更新规程；
# 员工：熟悉应急程序、认真培训演练、维护防护装备、报告隐患、保持警觉），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室安全，人人有责",
    "edition": "原著版",
    "points": {
        "K1": "安全，雇主也有责任",
        "K2": "针对本实验室制定应急预案",
        "K3": "定期培训，组织演练",
        "K4": "安全设备随手可取、状态完好",
        "K5": "规程要跟着更新",
        "K6": "安全是双向的，员工也有责任",
        "K7": "熟悉应急程序和自己的角色",
        "K8": "认真培训，用心演练",
        "K9": "防护用品勤清洁、勤检查",
        "K10": "发现隐患马上报告",
        "K11": "保持警觉，心中有数",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA"],
}

SHOTS = [
# 开场
("开场", "欣欣站在明亮的实验室里，向镜头招手",
 "The panda mascot stands in a bright busy lab and waves at the camera.",
 "这一课讲：实验室安全，人人有责。", "实验室安全，人人有责"),
("开场", "一边是公司大楼图标，一边是员工图标，中间双向箭头",
 "A company building icon on one side and a group of worker pictograms on the other, joined by a two-way arrow. No people.",
 "雇主有雇主的责任，员工有员工的。", "", ["雇主", "员工"]),
# 情景
("情景", "小研和王老师在玻璃温室旁交谈",
 "The female graduate student and the safety administrator, both in lab coats, talk beside a glass greenhouse.",
 "大家聊起：安全到底是谁的事？"),
# K1
("K1", "明亮实验室里多人工作，王老师在巡视",
 "Several people work in a bright lab while the safety administrator walks around observing.",
 "别忘了，雇主在这里也有责任。", "安全，雇主也有责任"),
# K2
("K2", "王老师对着空白应急预案文件，旁边浮现本实验室的危害图标",
 "The safety administrator works on a blank emergency plan binder, with this lab's hazard pictograms floating beside it.",
 "营造安全环境，针对具体危害定预案。", "针对本实验室制定应急预案"),
("K2", "火灾、溢洒、受伤图标连到预案本",
 "Icons of a fire, a spill and an injury, each linked by a line to a blank plan binder. No people.",
 "预案要全面。"),
# K3
("K3", "王老师在培训室给员工上课",
 "The safety administrator teaches a group of lab staff in a training room in front of a blank screen.",
 "定期培训员工，", "定期培训，组织演练"),
("K3", "大家沿疏散箭头有序走出实验室",
 "Lab staff walk out in an orderly line along an evacuation arrow during a drill.",
 "组织演练，让人人都知道该做什么。"),
# K4
("K4", "灭火器、洗眼器、溢洒处理箱三个图标",
 "Three icons in a row: a fire extinguisher, an eyewash station and a spill kit box. No people.",
 "维护安全设备：灭火器、洗眼器、溢洒包，", "安全设备随手可取、状态完好", ["灭火器", "洗眼器", "溢洒处理包"]),
("K4", "老李检查灭火器压力表，打勾",
 "The facility engineer checks the pressure gauge of a fire extinguisher, and a green check appears.",
 "样样随手可取，状态完好。"),
# K5
("K5", "旧规程本换成新规程本，旁边新危害图标和法规本",
 "An old blank procedure binder is swapped for a new one, next to a new hazard icon and an updated regulation booklet. No people.",
 "跟上新危害和新法规，审查更新规程。", "规程要跟着更新"),
# K6
("K6", "小研、阿杰、老周围在实验台前讨论",
 "The female graduate student, the young male student and the older man gather around a lab bench in discussion.",
 "安全不是单行道，", "安全是双向的，员工也有责任"),
("K6", "双向箭头图标",
 "A large two-way arrow icon. No people.",
 "员工也有自己的责任。"),
# K7
("K7", "阿杰戴好手套，调整袖口",
 "The young male student pulls on gloves and adjusts the cuffs.",
 "熟悉应急程序：", "熟悉应急程序和自己的角色"),
("K7", "走廊里的红色灭火器和安全出口标志",
 "A red fire extinguisher in a corridor and an emergency exit sign above a door. No people.",
 "知道出口和灭火器在哪，"),
("K7", "阿杰胸前别着空白角色牌",
 "The young male student wears a blank role badge on his chest.",
 "明白自己在应急中的角色。"),
# K8
("K8", "小研和老李拿平板在设备间巡看",
 "The female graduate student and the facility engineer walk through an equipment room holding tablets.",
 "认真对待培训，这不是做样子。", "认真培训，用心演练"),
("K8", "穿蓝色防护服戴面屏的阿杰低头工作，演练图标",
 "The young male student in a blue protective gown and face shield works with his head down, beside a drill evacuation icon.",
 "积极参加演练，把学到的记在心里。"),
# K9
("K9", "小研戴护目镜和口罩，整理发帽",
 "The female graduate student in safety goggles and a respirator mask adjusts her hair cap.",
 "维护个人防护装备：", "防护用品勤清洁、勤检查"),
("K9", "擦拭护目镜、对光检查手套",
 "Hands wipe a pair of goggles clean and hold a glove up to the light to inspect it. No people.",
 "保持清洁，定期检查，用前确认完好。", "", ["清洁", "检查", "用前确认"]),
# K10
("K10", "阿杰戴护目镜口罩，查看试剂瓶标签",
 "The young male student in goggles, mask and hair cap examines the blank label of a reagent bottle and frowns.",
 "一发现隐患，就马上报告。", "发现隐患马上报告"),
("K10", "阿杰向老周报告",
 "The young male student reports the problem bottle to the older man.",
 "别等出了事再说，要主动。"),
# K11
("K11", "小研戴护目镜，抬头环顾四周",
 "The female graduate student in safety goggles looks up and around the lab attentively.",
 "保持警觉，对周围情况心中有数，", "保持警觉，心中有数"),
("K11", "两名穿防护服的人在实验台并肩操作",
 "The young male student and the female graduate student in protective coats work side by side at a bench.",
 "护好自己，也护好同事。"),
# 小结
("小结", "欣欣身旁浮现预案、培训、设备、规程图标",
 "The panda mascot stands beside floating icons of a plan binder, a classroom, an extinguisher and a procedure book.",
 "雇主：预案、培训、设备、规程。", "小结"),
("小结", "出口、护目镜、电话、眼睛图标",
 "Icons of an exit sign, safety goggles, a telephone and an open eye. No people.",
 "员工：懂程序、护装备、报隐患、要警觉。"),
# 结尾
("结尾", "欣欣在实验室门口挥手道别",
 "The panda mascot waves goodbye at the lab doorway.",
 "安全靠大家，下次见！"),
]
