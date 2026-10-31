# 28_xTool MetalFab Laser Welder – How to change different nozzle 卡通剧本作者源
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字
# 原片为 15 秒的厂家教程片段（第 26 集“激光清洗”开头）；设备统称“手持式激光焊接机”，品牌不出现
# 补充 S 点避开本剧集 01–27 已用的

META = {
    "title": "激光焊接机更换清洗嘴",
    "points": {
        "K1": "先关闭设备电源",
        "K2": "拆下送丝管",
        "K3": "拆下焊接嘴",
        "K4": "换上清洗嘴",
        "S1": "等焊嘴凉了再换",
        "S2": "喷嘴装前查损伤",
        "S3": "嘴和模式要对应",
        "S4": "激光清洗同样要防护",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一把焊枪，旁边摆着两种不同形状的喷嘴",
 "The panda mascot holds a handheld laser welding gun beside two differently shaped brass nozzles on the bench.",
 "这一课讲：焊接嘴怎样换成清洗嘴。", "激光焊接机更换清洗嘴"),
# 情景
("情景", "阿杰刚焊完，伸手就去拧焊嘴",
 "The young male student has just finished welding and reaches with a bare hand to unscrew the nozzle.",
 "阿杰刚焊完，想马上换嘴去清洗焊缝。"),
("情景", "焊嘴冒着热气，阿杰缩回手",
 "Heat waves rise from the nozzle and the young male student pulls his hand back quickly.",
 "焊嘴还烫着，机器也没关。"),
("情景", "老李走过来，示意他先等一等",
 "The facility engineer walks over and gestures for him to wait.",
 "老李说：换嘴有顺序，别急。"),
# K1
("K1", "老李按下主机背面的电源开关到关闭",
 "The facility engineer presses the rocker switch on the back of the main unit to off.",
 "第一步，关闭设备电源。", "先关闭设备电源"),
("K1", "屏幕熄灭、指示灯熄灭，旁边打勾",
 "The touch screen and indicator light go dark, with a green check mark. No people.",
 "确认屏幕和指示灯都灭了。"),
# S1
("S1", "焊嘴旁的热浪图标和高温警示",
 "Icon of heat waves rising from a welding nozzle with a hot surface warning sign. No people.",
 "刚用完的焊嘴很烫，", "等焊嘴凉了再换"),
("S1", "焊枪挂在支架上，旁边一个沙漏",
 "The welding gun rests on its cradle with an hourglass beside it. No people.",
 "先挂回支架，等它冷却。"),
("S1", "老李戴上皮革耐热手套",
 "The facility engineer puts on thick leather heat-resistant gloves.",
 "动手时戴好耐热手套。"),
# K2
("K2", "老李从焊枪头上取下送丝管",
 "Wearing heat-resistant gloves, the facility engineer opens the clamp and removes the wire feeding tube from the gun.",
 "第二步，拆下送丝管。", "拆下送丝管"),
("K2", "送丝管放在一旁，焊丝头朝下",
 "The wire feeding tube is set aside on the bench with its wire tip pointing down. No people.",
 "清洗用不到送丝，送丝管先放好。"),
# K3
("K3", "老李拧下焊枪头上的铜色焊接嘴",
 "The facility engineer unscrews the copper welding nozzle from the tip of the welding gun.",
 "第三步，拆下焊接嘴。", "拆下焊接嘴"),
("K3", "焊接嘴放进一个分格的喷嘴盒",
 "The welding nozzle is placed into a compartment of a small nozzle storage box. No people.",
 "拆下的焊嘴放进喷嘴盒，不随手乱放。"),
# S2
("S2", "老李拿起清洗嘴，对着灯检查",
 "The facility engineer holds a cleaning nozzle up to the light and inspects it.",
 "装之前，先看看清洗嘴。", "喷嘴装前查损伤"),
("S2", "变形、烧蚀、堵塞的喷嘴图标，都被红叉划掉",
 "Icons of a bent nozzle, a burned nozzle and a clogged nozzle, all crossed out with red X marks. No people.",
 "变形、烧蚀、堵塞的，不能用。"),
# K4
("K4", "老李把清洗嘴拧到焊枪头上",
 "The facility engineer screws the cleaning nozzle onto the welding gun tip.",
 "第四步，换上清洗嘴。", "换上清洗嘴"),
("K4", "清洗嘴拧到位，旁边打勾",
 "Close view: the cleaning nozzle is fully seated on the gun tip, with a green check mark. No people.",
 "拧紧到位，不松不歪。"),
# S3
("S3", "清洗嘴图标和屏幕清洗模式图标用线连起来",
 "A line links a cleaning nozzle icon to a cleaning mode icon on a touch screen; a welding nozzle links to a welding mode icon. No people.",
 "换了清洗嘴，屏幕上就要选清洗模式。", "嘴和模式要对应"),
("S3", "嘴和模式错配，喷嘴冒烟的图标，被红叉划掉",
 "Icon of a mismatched nozzle and mode with smoke coming from the nozzle, crossed out with a red X. No people.",
 "嘴和模式不对应，可能烧坏喷嘴。"),
("S3", "老李开机后核对屏幕上的模式",
 "The facility engineer switches the machine back on and checks the selected mode on the touch screen.",
 "开机后先核对模式，再开出光。"),
# S4
("S4", "清洗时光斑在锈面上来回扫的示意图",
 "Diagram: a laser spot sweeps back and forth over a rusty metal surface, sending up a cloud of particles. No people.",
 "激光清洗的光在表面来回扫，", "激光清洗同样要防护"),
("S4", "扫描光反射到四周的示意图",
 "Diagram: reflected beams scatter in several directions from the swept surface. No people.",
 "反射方向更难预料，还会扬起锈和涂层粉尘。"),
("S4", "老李戴面罩、呼吸防护，排风罩对着工件",
 "The facility engineer wears a laser face shield and a respirator while a fume extraction hood points at the workpiece.",
 "防护眼镜、呼吸防护、排风，一样不少。"),
("S4", "欣欣指着封面有激光标志的空白小册子",
 "The panda mascot points at a blank booklet with a laser warning pictogram on the cover.",
 "要求以现行国家标准和本校规定为准。"),
# 小结
("小结", "欣欣身后四个步骤图标",
 "The panda mascot stands beside the welding gun with four step icons behind: a power switch off, a tube, a nozzle out and a nozzle in.",
 "关机、拆管、拆焊嘴、装清洗嘴。", "", ["关机", "拆送丝管", "拆焊嘴", "装清洗嘴"]),
("小结", "图标：冷却、检查、对模式、防护",
 "Icons in a row: an hourglass, a magnifier on a nozzle, a nozzle linked to a mode, and a face shield. No people.",
 "等冷却，查喷嘴，对模式，做防护。", "", ["等冷却", "查喷嘴", "对模式", "做防护"]),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye at the camera.",
 "换嘴虽小，规矩不少。下次见！"),
]
