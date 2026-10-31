# 28_xTool MetalFab Laser Welder – How to change different nozzle 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：焊接嘴换成清洗嘴，一句旁白加字幕），K1–K4，不加补充知识点、不做更正；
# 保留原片四步顺序（关机、拆送丝管、拆焊接嘴、装清洗嘴）和画面（操作者穿白色工作服、戴皮革耐热手套）；
# 原片只有 16 秒，剧本按原片四步放慢分解到 2 分钟，不添加原片没有的要求；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：如何更换不同喷嘴",
    "edition": "原著版",
    "points": {
        "K1": "先关闭设备电源",
        "K2": "拆下送丝管",
        "K3": "拆下焊接嘴",
        "K4": "换上清洗嘴",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一把焊枪，旁边摆着两种不同形状的喷嘴",
 "The panda mascot holds a handheld laser welding gun beside two differently shaped brass nozzles on the bench.",
 "这一课讲：焊接嘴怎样换成清洗嘴。", "激光焊机：如何更换不同喷嘴"),
("开场", "四个步骤图标排成一行：电源开关、送丝管、焊接嘴、清洗嘴",
 "Four icons in a row: a power switch turned off, a wire feeding tube, a welding nozzle and a cleaning nozzle. No people.",
 "一共四步，很快就能换好。", "", ["关机", "拆送丝管", "拆焊接嘴", "装清洗嘴"]),
# 情景
("情景", "阿杰看着一条发黑的焊缝，想把它清洗干净",
 "The young male student looks at a dark weld seam on a metal plate and wants to clean it.",
 "阿杰焊完了，想清洗一下焊缝。"),
("情景", "焊枪头上装着送丝管和焊接嘴",
 "Close view of the welding gun tip still fitted with the wire feeding tube and the welding nozzle. No people.",
 "可焊枪上装的还是焊接嘴。"),
("情景", "老李穿着白色工作服、戴着皮革耐热手套走过来",
 "The facility engineer walks over in a white work suit and leather heat-resistant gloves.",
 "老李说：清洗要换清洗嘴。"),
("情景", "欣欣在空白白板前竖起一根手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看怎么换。"),
# K1
("K1", "穿白色工作服、戴皮革耐热手套的老李走到主机背面",
 "The facility engineer in a white work suit and leather heat-resistant gloves walks to the back of the main unit.",
 "第一步，关闭设备电源。", "先关闭设备电源"),
("K1", "老李按下主机背面的电源开关到关闭",
 "The facility engineer presses the rocker switch on the back of the main unit to off.",
 "按下背面的电源开关。"),
("K1", "主机屏幕熄灭",
 "The touch screen on the main unit goes dark. No people.",
 "设备关机后，再动焊枪。"),
# K2
("K2", "焊枪头上卡着送丝管，卡扣被圆圈标出",
 "Close view of the welding gun tip with the wire feeding tube clamped on, the clamp marked with a green circle. No people.",
 "第二步，拆下送丝管。", "拆下送丝管"),
("K2", "老李戴着耐热手套打开卡扣",
 "Wearing leather heat-resistant gloves, the facility engineer opens the clamp on the gun tip.",
 "打开焊枪头上的卡扣，"),
("K2", "老李把送丝管从焊枪头上滑下来",
 "The facility engineer slides the wire feeding tube off the welding gun tip.",
 "把送丝管从焊枪上取下来。"),
("K2", "送丝管放在台面一旁",
 "The wire feeding tube is laid aside on the bench. No people.",
 "送丝管放到一旁。"),
# K3
("K3", "焊枪头上的铜色焊接嘴特写",
 "Close view of the copper welding nozzle on the tip of the welding gun. No people.",
 "第三步，拆下焊接嘴。", "拆下焊接嘴"),
("K3", "老李戴手套握住焊接嘴，逆时针拧",
 "The gloved facility engineer grips the copper welding nozzle and turns it counterclockwise.",
 "握住焊接嘴，拧下来。"),
("K3", "焊枪头上的焊接嘴已取下，老李手里拿着它",
 "The welding gun tip is now bare and the facility engineer holds the removed welding nozzle in his gloved hand.",
 "焊接嘴取下了。"),
# K4
("K4", "老李拿起一个形状不同的清洗嘴",
 "The facility engineer picks up a differently shaped brass cleaning nozzle.",
 "第四步，拿出清洗嘴。", "换上清洗嘴"),
("K4", "老李把清洗嘴拧到焊枪头上",
 "The facility engineer screws the cleaning nozzle onto the welding gun tip.",
 "把清洗嘴拧到焊枪头上。"),
("K4", "装着清洗嘴的焊枪特写",
 "Close view of the welding gun now fitted with the cleaning nozzle. No people.",
 "清洗嘴换好了。"),
# 小结
("小结", "欣欣身后四个步骤图标",
 "The panda mascot stands beside the welding gun with four step icons behind: a power switch off, a tube, a nozzle out and a nozzle in.",
 "关机、拆管、拆焊嘴、装清洗嘴。", "小结", ["关机", "拆送丝管", "拆焊接嘴", "装清洗嘴"]),
("小结", "欣欣指着第一个图标：电源开关",
 "The panda mascot points at the first icon, a power switch turned off.",
 "第一步永远是关机。"),
("小结", "两个喷嘴并排：焊接嘴和清洗嘴",
 "Two brass nozzles side by side: a welding nozzle and a differently shaped cleaning nozzle. No people.",
 "焊接用焊接嘴，清洗换清洗嘴。"),
("小结", "阿杰拿着装好清洗嘴的焊枪点头",
 "The young male student holds the welding gun fitted with the cleaning nozzle and nods.",
 "阿杰记住了这四步。"),
# 结尾
("结尾", "欣欣、老李和阿杰挥手告别",
 "The panda mascot, the facility engineer and the young male student wave goodbye at the camera.",
 "清洗嘴换好了，下次见！"),
]
