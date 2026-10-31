# 21_Replace the Motherboard for the xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换主控板，无旁白、只有字幕），K1–K11，不加补充知识点、不做更正；
# 保留原片工具规格（5 mm / 3 mm 十字、5 mm 内六角、镊子）、8 颗把手螺钉、7 颗主板螺钉、三挂钩对三销钉、每侧 4 颗螺钉，
# 以及原片画面（本片无警示页、只写关机拔线、操作者徒手拿主板、拔线前未做记号）；品牌口号不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换主板",
    "edition": "原著版",
    "points": {
        "K1": "准备工具和新主板",
        "K2": "关机并拔掉全部线缆",
        "K3": "锁定四个脚轮",
        "K4": "拆下前后把手",
        "K5": "拆下左侧盖板",
        "K6": "拔下主板插头，有胶先去胶",
        "K7": "拆下固定螺丝，取出旧主板",
        "K8": "装新主板，插头插回原位",
        "K9": "整理左侧线缆",
        "K10": "挂钩对销钉，装回左盖",
        "K11": "两侧把手装回",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab", "We Inspire Creation"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带脚轮的激光焊接机旁，向镜头招手",
 "The panda mascot stands beside a blank gray wheeled handheld laser welding machine in a workshop and waves at the camera.",
 "这一课讲激光焊接机怎样更换主控板。", "激光焊机：更换主板"),
("开场", "四个图标排成一行：把手、侧盖、电路板、挂钩",
 "Four icons in a row: a machine handle, a side cover, a circuit board and a small hook. No people.",
 "拆把手、开左盖、换主板、装回。", "", ["拆把手", "开左盖", "换主板", "装回"]),
# 情景
("情景", "焊接机屏幕不亮，阿杰皱眉看着",
 "The young male student frowns at a laser welding machine whose screen stays dark.",
 "焊接机的主板坏了，需要更换。"),
("情景", "老李提着工具箱和一块新电路板走来",
 "The facility engineer comes over carrying a toolbox and a new circuit board.",
 "老李带着工具和新主板来了。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "台面上摆着两把十字螺丝刀、一把内六角扳手、一把镊子",
 "Top view of a workbench with two cross-head screwdrivers of different sizes, a hex wrench and a pair of tweezers neatly laid out. No people.",
 "工具：5毫米和3毫米十字螺丝刀，", "准备工具和新主板", ["5mm十字", "3mm十字"]),
("K1", "工具旁放着一块新电路板",
 "A new circuit board lies next to the tools on the workbench. No people.",
 "5毫米内六角、镊子，还有新主板。", "", ["5mm内六角", "镊子", "新主板"]),
# K2
("K2", "老李按下焊接机开关，然后拔下电源插头",
 "The facility engineer switches off the laser welding machine and pulls the power plug out of the wall socket.",
 "第一步：关机，", "关机并拔掉全部线缆"),
("K2", "老李把机器上的线缆依次拔下",
 "The facility engineer disconnects all the cables from the back of the machine one by one.",
 "拔掉所有线缆。"),
# K3
("K3", "老李蹲下，把机器底部的脚轮锁扣按下",
 "The facility engineer crouches and presses down the brake lever on a caster wheel under the machine.",
 "把机器底部四个脚轮全部锁住。", "锁定四个脚轮"),
("K3", "四个脚轮图标都带锁，机器稳稳停在地上",
 "Icon of a wheeled machine with all four casters showing small lock symbols, standing still. No people.",
 "四个脚轮都锁住，机器不会移动。"),
# K4
("K4", "机器侧面，把手两端的螺丝被圆圈标出",
 "Side view of the laser welding machine with green circles marking the screws at both ends of the top handles. No people.",
 "用5毫米内六角，松开前后把手螺丝。", "拆下前后把手"),
("K4", "老李把松开的把手取下，放在一旁",
 "The facility engineer lifts the loosened handle off the machine and places it on the bench.",
 "两个把手一共8颗螺丝，取下把手。"),
# K5
("K5", "老李用小号十字螺丝刀拧下侧盖顶部的螺丝",
 "The facility engineer uses a small cross-head screwdriver to remove a screw at the top of the left side cover.",
 "用3毫米十字刀，拆下左盖的螺丝。", "拆下左侧盖板"),
("K5", "老李把左侧盖板向外取下，露出内部电路",
 "The facility engineer lifts the left side cover away, revealing power modules, wiring and a circuit board inside.",
 "取下左侧盖板，就能看到主控板了。"),
# K6
("K6", "老李捏住插头本体，把它从主板上拔下",
 "The facility engineer grips a connector body and pulls it straight out of the circuit board.",
 "依次拔下主板上的所有插头。", "拔下主板插头，有胶先去胶"),
("K6", "老李用镊子轻轻剥掉插头上的固定胶",
 "The facility engineer uses tweezers to gently peel away a dab of glue holding a connector in place.",
 "插头上有固定胶的，先用镊子去胶。"),
# K7
("K7", "主板特写，七个螺丝孔位被圆圈标出",
 "Close view of the circuit board inside the machine with seven green circles marking its mounting screws. No people.",
 "主板由7颗螺丝固定在机架上。", "拆下固定螺丝，取出旧主板"),
("K7", "老李用大号十字螺丝刀逐颗拧下螺丝",
 "The facility engineer removes the board's mounting screws one by one with a larger cross-head screwdriver.",
 "用5毫米十字刀，逐颗拆下。"),
("K7", "老李徒手拿着旧主板取出，放到一旁",
 "The facility engineer lifts the old circuit board out with bare hands and sets it aside on the bench.",
 "取出旧主板。"),
# K8
("K8", "老李把新主板对准螺丝孔放好",
 "The facility engineer lines up the new circuit board with the mounting holes inside the cabinet.",
 "新主板对准孔位，放回原来的位置。", "装新主板，插头插回原位"),
("K8", "老李拧上七颗螺丝固定新主板",
 "The facility engineer fastens the new board with its seven screws using the cross-head screwdriver.",
 "拧上7颗螺丝，固定牢靠。"),
("K8", "老李把插头逐个插回原来的插座",
 "The facility engineer plugs each connector back into its original socket on the new board.",
 "插头逐个插回原位，插到底。"),
# K9
("K9", "老李把机器下方垂落的线缆理顺，收回机内",
 "The facility engineer gathers the loose cables hanging below the open side and tucks them neatly inside.",
 "整理好左侧的线缆，收回机内。", "整理左侧线缆"),
("K9", "整齐的线束图标打勾，被盖板压住的线图标打叉",
 "Two icons side by side: a neat cable bundle with a green check mark, and a cable pinched under a cover edge with a red X. No people.",
 "线缆不能被盖板压住。"),
# K10
("K10", "盖板边缘的挂钩和机架上的销钉，用箭头对应",
 "Diagram of the side cover edge with three hooks and the machine frame with three pegs, arrows matching each hook to a peg. No people.",
 "左盖两侧有三个挂钩，对准三个销钉。", "挂钩对销钉，装回左盖"),
("K10", "老李把盖板推入机器，再拧紧顶部螺丝",
 "The facility engineer pushes the side cover into place and tightens the screw at its top.",
 "把盖板推进去，再拧紧螺丝固定。"),
# K11
("K11", "老李把把手放回原位，用内六角扳手拧紧",
 "The facility engineer sets a handle back on top of the machine and tightens its screws with the hex wrench.",
 "最后装回把手，拧紧螺丝。", "两侧把手装回"),
("K11", "老李走到另一侧，同样装好把手",
 "The facility engineer walks to the other side of the machine and fits the second handle the same way.",
 "另一侧也一样，用4颗螺丝固定。"),
# 小结
("小结", "欣欣站在焊接机旁，身后浮现几个步骤图标",
 "The panda mascot stands beside the closed laser welding machine with a row of step icons floating behind: a plug, a handle, a circuit board and a side cover.",
 "关机拔线锁脚轮，拆把手和左盖。", "小结", ["关机拔线", "锁脚轮", "换主板", "装回"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "有胶先去胶，7颗螺丝，插头回原位。"),
# 结尾
("结尾", "欣欣、老李和阿杰在焊接机前挥手",
 "The panda mascot, the facility engineer and the young male student wave goodbye in front of the laser welding machine.",
 "主板换好了，下次见！"),
]
