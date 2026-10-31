# 22_Replace the DC Power Supply for the xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换直流电源，无旁白、只有字幕），K1–K15，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、激光电源至少等 5 分钟、全程戴绝缘手套）、工具规格（3 mm / 5 mm 十字、5 mm 内六角）、
# 8 颗把手螺钉、4 颗电源螺钉、托住电源防掉落、接线与参考图一致，以及原片画面（操作者徒手拆接端子线、先装防护罩再提示核对接线）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊接机更换直流电源",
    "edition": "原著版",
    "points": {
        "K1": "仅限专业人员，内有高压和强激光",
        "K2": "残余高压，等够时间再碰",
        "K3": "全程戴绝缘手套",
        "K4": "准备工具和新电源",
        "K5": "关机并拔掉全部线缆",
        "K6": "锁定四个脚轮",
        "K7": "拆下前后把手",
        "K8": "拆下左侧盖板",
        "K9": "拆透明防护罩和接线",
        "K10": "拆最后一颗螺丝要托住",
        "K11": "装新电源，拧紧四颗螺丝",
        "K12": "装回透明防护罩",
        "K13": "接线与参考图完全一致",
        "K14": "挂钩对销钉，装回左盖",
        "K15": "两侧把手装回",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带脚轮的激光焊接机旁招手",
 "The panda mascot stands beside a blank gray wheeled handheld laser welding machine in a workshop and waves at the camera.",
 "这一课讲激光焊接机怎样更换直流电源。", "激光焊接机更换直流电源"),
("开场", "四个图标排成一行：把手、侧盖、电源模块、透明罩",
 "Four icons in a row: a machine handle, a side cover, a power supply module and a clear plastic shield. No people.",
 "拆把手、开左盖、换电源、装回。", "", ["拆把手", "开左盖", "换电源", "装回"]),
# 情景
("情景", "阿杰按下开关，焊接机没有反应",
 "The young male student presses the switch but the laser welding machine does not respond.",
 "焊接机的直流电源坏了。"),
("情景", "老李提着工具箱和新电源模块走来",
 "The facility engineer comes over carrying a toolbox and a new power supply module.",
 "专业技术人员老李来更换。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "先看片头的安全警示。"),
# K1
("K1", "黄黑条纹的警示卡，中间是闪电和激光三角标志",
 "A warning card with yellow and black stripes, showing an electric shock warning sign and a laser warning sign side by side. No people.",
 "这台设备内部有高压，还有强激光。", "仅限专业人员，内有高压和强激光"),
("K1", "触电和烧伤图标并排，下面一个惊叹号",
 "Icons of an electric shock and a burned hand side by side with a large exclamation mark below. No people.",
 "处理不当，可能触电、烧伤。"),
("K1", "阿杰拿螺丝刀伸向机箱的图标，被红叉划掉",
 "An icon of a student reaching toward a machine cabinet with a screwdriver, crossed out with a red X. No people.",
 "非专业人员，严禁擅自拆机。"),
("K1", "欣欣举着黄黑边框警示卡，卡面只有扳手和人形图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a wrench icon and a worker icon.",
 "这项维修只供专业技术人员。"),
("K1", "老李关闭焊接机电源开关",
 "The facility engineer turns off the main power switch of the laser welding machine.",
 "动手前，一定先断电。"),
# K2
("K2", "电源模块图标里闪着电，旁边一个沙漏",
 "An icon of a power supply module with a small lightning symbol inside and an hourglass beside it. No people.",
 "激光电源里可能残留高压。", "残余高压，等够时间再碰"),
("K2", "沙漏旁边一个时钟图标",
 "An hourglass next to a clock icon with its hand sweeping round. No people.",
 "至少等5分钟，再去触碰。", "", ["≥5分钟"]),
# K3
("K3", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "所有操作全程戴绝缘手套。", "全程戴绝缘手套"),
# K4
("K4", "台面上两把十字螺丝刀、一把内六角扳手和新电源",
 "Top view of a workbench with two cross-head screwdrivers, a hex wrench and a new metal-cased power supply module with a honeycomb vent. No people.",
 "3和5毫米十字刀、5毫米内六角、新电源。", "准备工具和新电源", ["3mm十字", "5mm十字", "5mm内六角", "新电源"]),
# K5
("K5", "老李关机，拔下电源插头和其他线缆",
 "The facility engineer switches off the machine, pulls out the power plug and disconnects the other cables.",
 "关机，拔掉全部线缆。", "关机并拔掉全部线缆"),
# K6
("K6", "老李把四个脚轮的锁扣依次踩下",
 "The facility engineer presses down the brake levers of all four caster wheels one by one.",
 "锁住四个脚轮，机器不会滑动。", "锁定四个脚轮"),
# K7
("K7", "老李用内六角扳手松开把手螺丝，取下把手",
 "The facility engineer loosens the handle screws with the hex wrench and lifts the handles off.",
 "5毫米内六角松开把手8颗螺丝。", "拆下前后把手"),
# K8
("K8", "老李拆下左盖顶部螺丝，取下盖板",
 "The facility engineer removes the top screw of the left side cover and lifts the cover away.",
 "3毫米十字刀拆左盖螺丝，取下左盖。", "拆下左侧盖板"),
# K9
("K9", "机内一块透明塑料罩盖着电源接线端子",
 "Inside the opened machine, a clear plastic shield covers the terminal block of a power supply module. No people.",
 "电源接线端子前，有一块透明防护罩。", "拆透明防护罩和接线"),
("K9", "老李徒手取下透明罩，逐根拆下端子线",
 "With bare hands, the facility engineer removes the clear shield and unscrews the wire terminals one by one.",
 "取下防护罩，再拆电源左侧的接线。"),
# K10
("K10", "老李一只手托住电源底部，另一只手拧最后一颗螺丝",
 "The facility engineer supports the bottom of the power supply with one hand while removing the last screw with the other.",
 "拆最后一颗螺丝时，用手托住电源。", "拆最后一颗螺丝要托住"),
("K10", "电源掉落的图标，被红叉划掉",
 "An icon of a power supply module falling, crossed out with a red X. No people.",
 "防止电源掉下来。"),
# K11
("K11", "老李把新电源放进机内，对准螺丝孔",
 "The facility engineer places the new power supply into the machine and lines it up with the screw holes.",
 "把新电源放到原来的位置。", "装新电源，拧紧四颗螺丝"),
("K11", "老李拧紧四颗固定螺丝",
 "The facility engineer tightens four mounting screws on the new power supply.",
 "拧紧4颗固定螺丝。"),
# K12
("K12", "老李徒手接好端子线，把透明防护罩装回端子前方",
 "With bare hands, the facility engineer reconnects the terminal wires and fits the clear plastic shield back over the terminal block.",
 "接好线，装回透明防护罩。", "装回透明防护罩"),
# K13
("K13", "平板上的空白接线示意图，旁边是机内的端子",
 "A simple wiring diagram on a tablet made only of lines and colored dots, next to the terminal block inside the machine.",
 "接线必须和参考图完全一致。", "接线与参考图完全一致"),
("K13", "颜色和位置对应的线头图标打勾，接反的打叉",
 "Two icons: wires matched to terminals by color with a green check, and swapped wires with a red X. No people.",
 "位置、颜色一根都不能错。"),
# K14
("K14", "盖板挂钩对准机架销钉，老李推入并拧螺丝",
 "The facility engineer aligns three hooks on the side cover with three pegs on the frame, pushes it in and tightens the screw.",
 "三个挂钩对准三个销钉，推入左盖拧紧。", "挂钩对销钉，装回左盖"),
# K15
("K15", "老李装回两侧把手，用内六角扳手拧紧",
 "The facility engineer refits the handles on both sides and tightens them with the hex wrench.",
 "两侧把手装回，螺丝全部拧紧。", "两侧把手装回"),
# 小结
("小结", "欣欣身后浮现几个步骤图标",
 "The panda mascot stands beside the closed machine with step icons floating behind: a warning card, an hourglass, a power supply module and a wiring diagram.",
 "专业人员，断电，等5分钟，戴手套。", "小结", ["专业人员", "等5分钟", "托住电源", "对图接线"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "托住电源拆螺丝，接线对照参考图。"),
# 结尾
("结尾", "欣欣、老李和阿杰在焊接机前挥手",
 "The panda mascot, the facility engineer and the young male student wave goodbye in front of the laser welding machine.",
 "直流电源换好了，下次见！"),
]
