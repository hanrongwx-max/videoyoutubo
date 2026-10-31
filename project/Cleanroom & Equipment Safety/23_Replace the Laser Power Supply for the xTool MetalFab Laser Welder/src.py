# 23_Replace the Laser Power Supply for the xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换激光电源，无旁白、只有字幕），K1–K19，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、工具规格（3 / 5 mm 十字、3 mm 一字、镊子、5 / 2.5 mm 内六角）、
# 8 颗把手螺钉、5 根电源线、黄色固定胶、8 颗支架螺钉、挂钩朝外，以及原片画面（操作者徒手拆接电源线、未设维修区）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换激光电源（带把手机型）",
    "edition": "原著版",
    "points": {
        "K1": "仅限专业人员，内有高压和强激光",
        "K2": "残余高压，等够时间再碰",
        "K3": "全程戴绝缘手套",
        "K4": "准备工具和新激光电源",
        "K5": "关机并拔掉全部线缆",
        "K6": "锁定四个脚轮",
        "K7": "拆把手，最后一颗扶住把手",
        "K8": "拆下左侧盖板",
        "K9": "拆五根电源线，黄胶用镊子剥",
        "K10": "拆下电源固定螺丝",
        "K11": "向右滑出，先抬左侧",
        "K12": "拆下电源支架",
        "K13": "支架装到新电源，挂钩朝外",
        "K14": "新电源装回原位",
        "K15": "理线，逐根固定电源线",
        "K16": "复核接线顺序",
        "K17": "拧回固定螺丝",
        "K18": "挂钩对销钉，装回左盖",
        "K19": "两侧把手装回",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带脚轮的激光焊接机旁招手",
 "The panda mascot stands beside a blank gray wheeled handheld laser welding machine in a workshop and waves at the camera.",
 "这一课讲激光焊接机怎样更换激光电源。", "激光焊接机更换激光电源"),
("开场", "四个图标排成一行：把手、侧盖、长条电源、支架",
 "Four icons in a row: a machine handle, a side cover, a long power supply module and a metal bracket. No people.",
 "拆把手左盖、换电源、装支架、装回。", "", ["拆把手", "开左盖", "换电源", "装回"]),
# 情景
("情景", "阿杰按下焊枪扳机，焊枪不出光，他皱眉",
 "The young male student presses the trigger of the welding gun but nothing happens, and he frowns.",
 "焊接机的激光电源坏了。"),
("情景", "老李提着工具箱，和小研抬着长条形新电源走来",
 "The facility engineer carries a toolbox while the female graduate student brings a long new power supply module.",
 "专业技术人员老李来更换。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "先看片头的安全警示。"),
# K1
("K1", "当心触电和当心激光两个警告标志并排",
 "An electric shock warning sign and a laser warning sign side by side on a yellow background. No people.",
 "激光焊接机里有高压，也有强激光。", "仅限专业人员，内有高压和强激光"),
("K1", "触电和烧伤图标并排，下面一个惊叹号",
 "Icons of an electric shock and a burned hand side by side with a large exclamation mark below. No people.",
 "处理不当，会触电、烧伤。"),
("K1", "学生拿螺丝刀伸向机箱的图标，被红叉划掉",
 "An icon of a student reaching toward a machine cabinet with a screwdriver, crossed out with a red X. No people.",
 "非专业人员严禁拆机，动手前必须断电。"),
# K2
("K2", "长条形电源图标里闪着电，旁边一个沙漏",
 "An icon of a long power supply module with a small lightning symbol inside and an hourglass beside it. No people.",
 "激光电源断电后，还可能残留高压。", "残余高压，等够时间再碰"),
("K2", "沙漏旁边一个时钟图标",
 "An hourglass next to a clock icon with its hand sweeping round. No people.",
 "至少等5分钟，再去触碰。", "", ["≥5分钟"]),
# K3
("K3", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "全过程戴绝缘手套。", "全程戴绝缘手套"),
# K4
("K4", "木纹台面上一个长条形银色电源和一排工具",
 "Top view of a wooden workbench with a long silver power supply module, several screwdrivers, two hex wrenches and tweezers. No people.",
 "新激光电源，3和5毫米十字刀，3毫米一字刀，", "准备工具和新激光电源", ["3mm十字", "5mm十字", "3mm一字"]),
("K4", "两把大小不同的内六角扳手和一把镊子特写",
 "Close view of two hex wrenches of different sizes and a pair of tweezers on the bench. No people.",
 "5和2.5毫米内六角，还有镊子。", "", ["5mm内六角", "2.5mm内六角", "镊子"]),
# K5
("K5", "老李拔下电源插头和其他线缆",
 "The facility engineer pulls out the power plug and disconnects the other cables from the machine.",
 "关机，拔掉全部线缆。", "关机并拔掉全部线缆"),
# K6
("K6", "老李把四个脚轮锁扣依次踩下",
 "The facility engineer presses down the brake levers of all four caster wheels one by one.",
 "锁好四个脚轮。", "锁定四个脚轮"),
# K7
("K7", "老李用内六角扳手松把手螺丝",
 "The facility engineer loosens the handle screws with a hex wrench.",
 "5毫米内六角松开把手8颗螺丝。", "拆把手，最后一颗扶住把手"),
("K7", "老李一只手扶住把手，另一只手拧最后一颗螺丝",
 "The facility engineer holds the handle with one hand while removing the last screw with the other.",
 "拆最后一颗时扶住把手，防止掉落。"),
# K8
("K8", "老李拆下左盖螺丝，取下盖板",
 "The facility engineer removes the left cover screw and lifts the side cover away.",
 "3毫米十字刀拆左盖螺丝，取下左盖。", "拆下左侧盖板"),
# K9
("K9", "机内长条电源一端，五根线接在端子上",
 "Inside the machine, one end of a long power supply module shows five wires connected to a terminal strip. No people.",
 "激光电源一端接着五根电源线。", "拆五根电源线，黄胶用镊子剥"),
("K9", "老李徒手用十字螺丝刀逐根拆下端子线",
 "With bare hands, the facility engineer unscrews the terminal wires one by one with a cross-head screwdriver.",
 "用5毫米十字刀，逐根拆下来。"),
("K9", "老李用镊子剥掉端子上的黄色固定胶",
 "The facility engineer uses tweezers to peel yellow fixing glue off a terminal.",
 "端子上有黄色固定胶，用镊子剥掉。"),
# K10
("K10", "主板旁边一颗被圆圈标出的螺丝，螺丝刀拧下",
 "A screw near the circuit board is marked with a green circle and removed with a screwdriver.",
 "再用5毫米十字刀拆电源固定螺丝。", "拆下电源固定螺丝"),
# K11
("K11", "老李双手把长条电源从左向右滑动",
 "The facility engineer slides the long power supply from left to right with both hands.",
 "把电源从左往右滑。", "向右滑出，先抬左侧"),
("K11", "老李先抬起电源左端，再慢慢取出右端",
 "The facility engineer lifts the left end of the power supply out first, then slowly pulls out the right end.",
 "先抬出左侧，再慢慢取出右侧。"),
# K12
("K12", "电源放在台面上，老李用小号内六角扳手拆支架",
 "The power supply lies on the bench; the facility engineer removes the bracket screws with a small hex wrench.",
 "2.5毫米内六角拆支架8颗螺丝。", "拆下电源支架"),
# K13
("K13", "新电源和支架并排，支架上的挂钩被圆圈标出",
 "The new power supply lies next to the metal bracket, its hooks marked with green circles. No people.",
 "把支架装到新电源上。", "支架装到新电源，挂钩朝外"),
("K13", "挂钩朝外的支架打勾，朝内的打叉",
 "Two icons: a bracket with hooks facing outward with a green check, and hooks facing inward with a red X. No people.",
 "注意方向：挂钩要朝外。"),
("K13", "老李拧紧支架螺丝",
 "The facility engineer tightens the bracket screws on the new power supply.",
 "8颗螺丝拧紧。"),
# K14
("K14", "老李把新电源放回机内原位",
 "The facility engineer slides the new power supply back into its place inside the machine.",
 "把新电源装回原来的位置。", "新电源装回原位"),
# K15
("K15", "老李把线缆理顺，逐根拧紧端子",
 "The facility engineer tidies the cables and tightens each terminal screw one by one with bare hands.",
 "理顺线缆，5根电源线逐根固定。", "理线，逐根固定电源线"),
# K16
("K16", "老李对照平板上的空白接线示意图检查",
 "The facility engineer compares the terminals with a simple wiring diagram of lines and colored dots on a tablet.",
 "对照参考图，再核对一遍接线顺序。", "复核接线顺序"),
("K16", "端子和导线颜色一一对应，打勾",
 "Icon of terminals and wires matched one to one by color with a green check mark. No people.",
 "一根都不能接错。"),
# K17
("K17", "老李拧回主板旁的固定螺丝",
 "The facility engineer refastens the screw near the circuit board that secures the power supply.",
 "拧回固定电源的螺丝。", "拧回固定螺丝"),
# K18
("K18", "盖板挂钩对准销钉，老李推入并拧紧",
 "The facility engineer aligns the side cover's three hooks with three pegs on the frame, pushes it in and tightens the screw.",
 "三个挂钩对准三个销钉，装回左盖。", "挂钩对销钉，装回左盖"),
# K19
("K19", "老李装回两侧把手",
 "The facility engineer refits the handles on both sides and tightens them with the hex wrench.",
 "两侧把手装回拧紧。", "两侧把手装回"),
# 小结
("小结", "欣欣身后浮现几个步骤图标",
 "The panda mascot stands beside the closed machine with step icons floating behind: a warning card, an hourglass, a long power supply and a bracket.",
 "专业人员，断电，等5分钟，戴手套。", "小结", ["专业人员", "等5分钟", "5根电源线", "挂钩朝外"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "黄胶镊子剥，先抬左侧再取右侧。"),
("小结", "欣欣指着焊接机",
 "The panda mascot points at the closed laser welding machine.",
 "支架挂钩朝外，接线对照参考图。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊接机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye in front of the laser welding machine.",
 "激光电源换好了，下次见！"),
]
