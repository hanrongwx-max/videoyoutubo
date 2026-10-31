# 24_Replace the Display Screen for the xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换顶部触摸显示屏，无旁白、只有字幕），K1–K13，不加补充知识点、不做更正；
# 保留原片工具规格（5 mm / 3 mm 十字、撬棒、镊子）、8 + 8 颗螺钉、黄色软排线对缺口，
# 以及原片画面（本片无警示页、螺钉和屏幕组件直接放在机器顶面）；品牌和贴膜字样不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊接机更换显示屏",
    "edition": "原著版",
    "points": {
        "K1": "准备工具、新屏和贴膜",
        "K2": "关机并拔掉全部线缆",
        "K3": "锁定四个脚轮",
        "K4": "撬起四角，揭下保护膜",
        "K5": "必要时清除支架残胶",
        "K6": "拆下支架八颗螺丝",
        "K7": "抬起屏幕，拔下背面排线",
        "K8": "再拆八颗螺丝，取下旧屏",
        "K9": "新屏入支架，排线对缺口",
        "K10": "拧紧八颗螺丝",
        "K11": "接回排线",
        "K12": "拧紧其余八颗螺丝",
        "K13": "贴新保护膜，对齐抹平",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab", "Designed by xTool"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机旁，指着机器顶上的显示屏",
 "The panda mascot stands beside a blank gray wheeled handheld laser welding machine and points at the touch screen on its top.",
 "这一课讲激光焊接机怎样更换显示屏。", "激光焊接机更换显示屏"),
("开场", "四个图标：撬棒、螺丝刀、显示屏、贴膜",
 "Four icons in a row: a pry tool, a screwdriver, a display panel and a screen protector sticker. No people.",
 "揭膜、拆屏、换屏、贴新膜。", "", ["揭膜", "拆屏", "换屏", "贴膜"]),
# 情景
("情景", "阿杰点着焊接机顶上的触摸屏，屏幕没有反应",
 "The young male student taps the touch screen on top of the laser welding machine, but it does not respond.",
 "焊接机的显示屏坏了。"),
("情景", "老李提着工具箱和新显示屏走来",
 "The facility engineer comes over carrying a toolbox and a new display panel.",
 "老李带着新屏来更换。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "台面上两把十字螺丝刀、黑色撬棒、镊子",
 "Top view of a wooden bench with two cross-head screwdrivers, a black plastic pry tool and tweezers. No people.",
 "5毫米和3毫米十字刀、撬棒和镊子，", "准备工具、新屏和贴膜"),
("K1", "一块新显示屏和一张黑框空白贴膜",
 "A new display panel with a green circuit board back and a blank black-framed screen protector sticker on the bench. No people.",
 "还有新显示屏和新保护膜。", "", ["5mm十字", "3mm十字", "撬棒", "镊子", "新屏和贴膜"]),
# K2
("K2", "老李关机，拔下电源插头和其他线缆",
 "The facility engineer switches off the machine and unplugs the power cord and other cables.",
 "关机，拔掉全部线缆。", "关机并拔掉全部线缆"),
# K3
("K3", "老李把四个脚轮锁扣踩下",
 "The facility engineer presses down the brake levers of all four caster wheels.",
 "锁好底座四个脚轮。", "锁定四个脚轮"),
# K4
("K4", "老李用撬棒撬起保护膜的一个角",
 "The facility engineer lifts one corner of the screen protector with the plastic pry tool.",
 "用撬棒把保护膜四个角撬起来，", "撬起四角，揭下保护膜"),
("K4", "老李用手把保护膜整张揭下",
 "The facility engineer peels the whole screen protector off by hand.",
 "再整张揭下来。"),
# K5
("K5", "露出的金属支架边缘有一些残胶",
 "Close view of the metal screen bracket with small spots of leftover glue along its edge. No people.",
 "支架上有残胶的，清理干净。", "必要时清除支架残胶"),
# K6
("K6", "老李用小号十字螺丝刀拆下支架螺丝，放在机器顶面上",
 "The facility engineer removes the bracket screws with a small cross-head screwdriver and leaves them on top of the machine.",
 "用3毫米十字刀，拆下8颗螺丝。", "拆下支架八颗螺丝"),
# K7
("K7", "老李双手抬起屏幕组件",
 "The facility engineer lifts the screen assembly up from the top of the machine with both hands.",
 "抬起屏幕，背面连着一根排线。", "抬起屏幕，拔下背面排线"),
("K7", "老李用镊子剥掉排线上的胶，再拔下排线",
 "The facility engineer peels glue off the ribbon cable with tweezers, then unplugs the cable.",
 "排线上有胶，先用镊子剥掉再拔。"),
# K8
("K8", "屏幕放在台面上，老李拆背面螺丝",
 "The screen assembly lies face down on the bench; the facility engineer removes the screws on the back.",
 "用5毫米十字刀，再拆8颗螺丝。", "再拆八颗螺丝，取下旧屏"),
("K8", "旧屏和金属支架分开放在台面上",
 "The old screen and the empty metal bracket lie separately on the bench with the screws beside them. No people.",
 "旧屏从支架上取下来。"),
# K9
("K9", "新屏放进支架，黄色软排线对准支架缺口",
 "The new screen is placed into the bracket; a yellow flexible cable lines up with a notch in the bracket. No people.",
 "新屏放进支架，黄色软排线对准缺口。", "新屏入支架，排线对缺口"),
# K10
("K10", "老李拧紧屏幕背面的螺丝",
 "The facility engineer tightens the screws on the back of the new screen.",
 "拧紧8颗螺丝。", "拧紧八颗螺丝"),
# K11
("K11", "老李把排线插回屏幕背面",
 "The facility engineer plugs the ribbon cable back into the back of the new screen above the machine.",
 "回到机器上，接回排线。", "接回排线"),
# K12
("K12", "屏幕放回机顶，老李拧紧支架螺丝",
 "The screen assembly sits back on the machine top; the facility engineer tightens the bracket screws.",
 "放回屏幕，拧紧其余8颗螺丝。", "拧紧其余八颗螺丝"),
# K13
("K13", "老李揭开新贴膜背纸，对准屏幕四角",
 "The facility engineer peels the backing off a new blank screen protector and lines up its corners with the screen.",
 "贴新保护膜，先对齐四个角，", "贴新保护膜，对齐抹平"),
("K13", "老李用手掌把贴膜均匀抹平",
 "The facility engineer smooths the protector evenly with his palm.",
 "再均匀地抹平。"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands beside the machine with icons floating behind: a plug, a pry tool, a display panel and a sticker.",
 "关机拔线锁脚轮，撬四角揭旧膜。", "小结", ["关机拔线", "揭膜", "8+8颗螺丝", "贴新膜"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "排线有胶先剥，黄排线对准缺口。"),
# 结尾
("结尾", "欣欣、老李和阿杰在焊接机前挥手，屏幕亮起",
 "The panda mascot, the facility engineer and the young male student wave goodbye beside the laser welding machine with its screen lit.",
 "显示屏换好了，下次见！"),
]
