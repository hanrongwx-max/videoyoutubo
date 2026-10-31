# 21_Fundamentals of Handling Compressed Gas Cylinders Safely – Setting Regulator Pre 原著版卡通剧本作者源
# 完全照原片：开启瓶阀、设定减压器输出压力的操作演示（1 分 46 秒），K1–K10（出口背向身体、手不放阀门正上方、
# 用手慢开除非供应商要求专用工具、压力低联系实验室主管、满刻度不是安全压力、出口阀管流量调压阀管压力、通气后复核）；
# 原片气瓶未见固定，照原片呈现，无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "开瓶阀与调压力",
    "edition": "原著版",
    "points": {
        "K1": "出口朝外，侧身站",
        "K2": "手别放在阀门正上方",
        "K3": "用手慢慢开阀",
        "K4": "看进口压力表",
        "K5": "压力偏低，要报告",
        "K6": "慢慢调到所需压力",
        "K7": "满刻度不是安全压力",
        "K8": "慢慢打开出口阀",
        "K9": "出口阀管流量，调压阀管压力",
        "K10": "通气后再复核",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣站在装好减压器的气瓶旁，双表朝向镜头",
 "The panda mascot stands beside a gas cylinder standing upright, fitted with a two-gauge pressure regulator, and waves at the camera.",
 "这一课讲开瓶阀和调节输出压力。", "开瓶阀与调压力"),
("开场", "两只压力表图标，一只标进口、一只标出口",
 "Two round pressure gauge icons side by side with blank dials, connected by a short pipe. No people.",
 "一只表看瓶里，一只表看输出。", "", ["进口压力表", "输出压力表"]),
# 情景
("情景", "阿杰正对着减压器出口，伸手猛拧瓶阀",
 "The young male student stands directly in front of the regulator outlet and grabs the cylinder valve handwheel, about to twist it hard.",
 "阿杰站在表的正前方，想一把拧开瓶阀。"),
("情景", "正对出口站立、猛拧阀门的图标被打叉",
 "An icon of a person standing in front of a regulator outlet and twisting a valve fast, crossed out with a red X. No people.",
 "出口对着自己，这样很不安全。"),
("情景", "小研把阿杰拉到气瓶侧面",
 "The female graduate student gently moves the young male student to the side of the cylinder.",
 "小研让他换个位置，慢慢来。"),
# K1
("K1", "小研站在气瓶侧面，减压器出口指向另一边",
 "The female graduate student, wearing a lab coat, safety goggles and gloves, stands at the side of the cylinder; the regulator outlet points away from her.",
 "开阀时侧身站，出口不对着自己。", "出口朝外，侧身站"),
# K2
("K2", "手掌盖在阀门顶上的图标被打叉",
 "An icon of a palm placed flat over the top of a cylinder valve, crossed out with a red X. No people.",
 "手也别放在阀门正上方。", "手别放在阀门正上方"),
# K3
("K3", "小研用手握住瓶阀手轮慢慢转动",
 "The female graduate student slowly turns the cylinder valve handwheel by hand.",
 "用手慢慢打开瓶阀。", "用手慢慢开阀"),
("K3", "一把专用阀门扳手配供应商图标",
 "A special cylinder valve key next to a delivery truck icon representing the gas supplier. No people.",
 "供应商规定用专用工具时，才用工具。"),
# K4
("K4", "进口压力表指针上升，旁边一个虚线目标框",
 "The inlet pressure gauge needle rises and stops inside a dotted target zone on a blank dial. No people.",
 "看进口压力表，读数应在预期之内。", "看进口压力表"),
# K5
("K5", "指针停在很低的位置，旁边问号",
 "The inlet gauge needle stops far below the dotted target zone, with a question mark beside it. No people.",
 "压力比预期低？先别急着用。", "压力偏低，要报告"),
("K5", "快空的气瓶图标和冒气的瓶阀图标",
 "Two icons: a nearly empty cylinder and a cylinder valve with a small gas puff escaping. No people.",
 "可能快用空了，也可能瓶阀漏气。"),
("K5", "小研向老周报告，老周皱眉点头",
 "The female graduate student reports to the older man next to the cylinder; he frowns and nods.",
 "瓶阀漏气是严重问题，要找实验室主管。"),
# K6
("K6", "小研缓慢顺时针转动调压手轮",
 "The female graduate student slowly turns the large regulator adjusting knob clockwise while watching the gauge.",
 "慢慢转调压手轮，边转边看表。", "慢慢调到所需压力"),
("K6", "输出表指针停在空白规程卡上标的位置",
 "The delivery gauge needle settles on a mark that matches a blank procedure card beside it. No people.",
 "调到仪器和规程要求的压力。"),
# K7
("K7", "表盘满刻度处亮红光，旁边红叉",
 "A gauge dial with its maximum scale end glowing red and a red X beside it. No people.",
 "表的满刻度，不是安全工作压力。", "满刻度不是安全压力"),
# K8
("K8", "小研慢慢打开减压器出口小阀，气流箭头流向仪器",
 "The female graduate student slowly opens the small outlet valve; a gentle arrow shows gas flowing to an instrument.",
 "再慢慢打开出口阀，向系统供气。", "慢慢打开出口阀"),
# K9
("K9", "出口阀旁是流量箭头，调压手轮旁是压力表",
 "Split icon: the outlet valve paired with a flow arrow, the adjusting knob paired with a pressure gauge. No people.",
 "出口阀只管流量，不管压力。", "出口阀管流量，调压阀管压力", ["出口阀：流量", "调压阀：压力"]),
("K9", "用出口阀调压力的图标被打叉",
 "An icon of a hand turning the outlet valve while staring at the pressure gauge, crossed out with a red X. No people.",
 "要改压力，只能用调压手轮。"),
# K10
("K10", "通气后输出表指针稍稍下滑",
 "After gas starts flowing, the delivery gauge needle drops slightly below the mark. No people.",
 "通气后，输出压力会略有下降。", "通气后再复核"),
("K10", "小研看表，轻轻微调手轮",
 "The female graduate student watches the delivery gauge and makes a small adjustment to the knob.",
 "复核一下，需要时再微调。"),
# 小结
("小结", "欣欣身旁浮现侧身站和慢转手轮图标",
 "The panda mascot stands beside floating icons of a person standing sideways and a slowly turning handwheel.",
 "出口朝外，手不压阀，慢慢开。", "小结"),
("小结", "进口表、调压手轮、出口阀三个图标",
 "Three icons: an inlet gauge with a question mark, an adjusting knob and an outlet valve with a flow arrow. No people.",
 "压力低要报告，调压阀管压力。"),
("小结", "出口阀慢开、输出表复核两个打勾图标",
 "Two icons with green checks: an outlet valve opening slowly and a delivery gauge being rechecked. No people.",
 "出口阀慢开，通气后复核压力。"),
# 结尾
("结尾", "欣欣在调好压力的气瓶旁挥手道别",
 "The panda mascot waves goodbye at the camera beside a gas cylinder with its regulator set.",
 "稳稳开阀，准准调压，下次见！"),
]
