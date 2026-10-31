# 18_Radiological Emergencies Get Your Lab Safety Now Training Course 原著版卡通剧本作者源
# 完全照原片：K1–K9（隔离—屏蔽（铅为首选）—铅围裙手套剂量计—脱装备去污—盖革计数器检测—
# 美国核管理委员会指南与 ALARA—不走捷径），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "放射性物质洒漏怎么办",
    "edition": "原著版",
    "points": {
        "K1": "少见，但同样严重",
        "K2": "第一步：隔离现场",
        "K3": "设屏障、拉警示带、人远离",
        "K4": "用屏蔽，铅是首选",
        "K5": "防护穿戴齐全，佩戴剂量计",
        "K6": "控制住了，再去污",
        "K7": "检测确认安全",
        "K8": "依法规，守ALARA原则",
        "K9": "不走捷径，尽量少受照",
    },
    "avoid": ["Atlantic", "Atlantic Training", "NRC", "Nuclear Regulatory Commission", "Geiger"],
}

SHOTS = [
# 开场
("开场", "欣欣站在贴有电离辐射警告标志的实验室门外，向镜头招手",
 "The panda mascot stands outside a lab door marked with an ionizing radiation warning sign and waves at the camera.",
 "这一课讲放射性应急怎么处理。", "放射性物质洒漏怎么办"),
# 情景
("情景", "同位素实验室里，一个小瓶倒在台面上，液体洒开",
 "In a radioisotope lab, a small vial lies tipped over on the bench with liquid spreading out. No people.",
 "实验室里，放射性溶液洒了。"),
("情景", "阿杰愣在原地，小研快步走来",
 "The young male student freezes in place while the female graduate student hurries over.",
 "阿杰一时不知道该怎么办。"),
# K1
("K1", "欣欣严肃地站在电离辐射警告标志旁",
 "The panda mascot stands beside an ionizing radiation warning sign with a serious face.",
 "放射性事故不常见，但同样严重。", "少见，但同样严重"),
("K1", "隔离、防护、去污三个图标",
 "Three icons in a row: a barrier, a shield and a cleaning cloth. No people.",
 "一定要知道该怎么做。", "", ["隔离", "防护", "去污"]),
# K2
("K2", "洒漏处周围画出一个红色圆圈，透明塑料帘挡住",
 "A small spill on a bench with a red circle around it and a clear plastic curtain drawn across. No people.",
 "洒漏或泄漏，第一件事是隔离现场。", "第一步：隔离现场"),
# K3
("K3", "戴蓝手套的手拉开红白警示带，立起辐射警告标志",
 "A hand in a blue glove stretches red and white warning tape across the doorway, beside an ionizing radiation warning sign.",
 "设屏障，拉上辐射警示带，", "设屏障、拉警示带、人远离"),
("K3", "人群图标沿箭头远离隔离区",
 "Person pictograms move far away from a taped-off area along arrows. No people.",
 "让人员离得越远越好。"),
# K4
("K4", "射线源图标与人之间立起一块灰色铅屏蔽板",
 "A radiation source icon with a thick grey lead shielding block between it and a person pictogram. No people.",
 "用辐射屏蔽降低照射水平，", "用屏蔽，铅是首选"),
("K4", "铅砖图标打勾",
 "A stack of grey lead bricks with a green check mark. No people.",
 "铅是首选的屏蔽材料。", "", ["铅"]),
# K5
("K5", "王老师、小研、阿杰互相帮忙穿白色防护服、戴口罩",
 "The safety administrator, the female graduate student and the young male student help each other into white protective coveralls and masks.",
 "穿戴合适的个人防护装备，", "防护穿戴齐全，佩戴剂量计"),
("K5", "铅围裙、手套、剂量计三个图标",
 "Three icons in a row: a lead apron, a pair of gloves and a dosimeter badge. No people.",
 "铅围裙、手套，还有剂量计。", "", ["铅围裙", "手套", "剂量计"]),
("K5", "剂量计图标旁有空白记录本",
 "A dosimeter badge icon next to a blank record book. No people.",
 "剂量计用来监测受照剂量。"),
("K5", "小研穿戴齐全站在警示带前",
 "The female graduate student, fully suited with apron, gloves and dosimeter, stands at the warning tape.",
 "处理时，一定要穿戴齐全。"),
# K6
("K6", "洒漏处被吸水材料围住，箭头显示不再扩散",
 "The spill is ringed with absorbent material and arrows show it no longer spreading. No people.",
 "污染控制住之后，开始去污。", "控制住了，再去污"),
("K6", "小研小心脱下外层手套和防护用品，放进专用袋",
 "The female graduate student carefully removes her outer gloves and gear and places them into a bag marked with a radiation warning sign.",
 "小心脱下受污染的防护用品，"),
("K6", "戴黄手套的手用蓝布和去污剂擦台面、水槽边",
 "A hand in a yellow glove wipes the bench and sink edge with a blue cloth and a decontamination spray bottle with a blank label.",
 "用合适的去污剂，清洁受影响的表面。"),
# K7
("K7", "黄色辐射检测仪表盘特写，指针刻度",
 "Close view of a yellow radiation survey meter with a needle dial and a blank scale.",
 "用盖革计数器检测，", "检测确认安全"),
("K7", "指针回落，绿勾出现",
 "The meter needle drops back down and a green check mark appears. No people.",
 "确认区域已经安全。"),
# K8
("K8", "空白指南手册，封面有星条旗和原子图标",
 "A blank guideline handbook with a stars-and-stripes flag icon and an atom icon on the cover. No people.",
 "以美国核管理委员会的辐射安全指南，", "依法规，守ALARA原则"),
("K8", "向下的箭头和尽量低的刻度图标",
 "A downward arrow beside a dose gauge kept near the lowest mark. No people.",
 "和ALARA原则为准：合理可行尽量低。", "", ["ALARA", "合理可行尽量低"]),
# K9
("K9", "抄近路的箭头被打叉，按规范路线的箭头打勾",
 "A shortcut arrow crossed out with a red X, and a proper route arrow with a green check. No people.",
 "千万不要走捷径。", "不走捷径，尽量少受照"),
("K9", "两人隔着黑黄警示带站立，旁边日历时钟图标",
 "Two people in dark protective suits stand behind black and yellow warning tape, beside a calendar and clock icon.",
 "辐射照射可能有长期影响，"),
("K9", "剂量表指针压到最低",
 "A dose gauge with its needle pushed down to the minimum. No people.",
 "要尽可能把它降到最低。"),
# 小结
("小结", "欣欣身旁浮现隔离、屏蔽、去污图标",
 "The panda mascot stands beside floating icons of a barrier, a lead shield and a cleaning cloth.",
 "先隔离，再屏蔽防护，然后去污。", "小结"),
("小结", "检测仪、剂量计、ALARA图标",
 "Icons of a survey meter, a dosimeter badge and a downward arrow. No people.",
 "检测确认，照射合理可行尽量低。"),
# 结尾
("结尾", "欣欣在辐射实验室门外挥手道别",
 "The panda mascot waves goodbye outside a lab door with an ionizing radiation warning sign.",
 "敬畏射线，不走捷径，下次见！"),
]
