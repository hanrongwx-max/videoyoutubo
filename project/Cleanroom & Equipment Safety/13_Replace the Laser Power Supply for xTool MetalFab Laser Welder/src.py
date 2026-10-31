# 13_Replace the Laser Power Supply for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机激光电源，无旁白、只有字幕），K1–K24，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、静置 10 分钟、5 / 3 mm 十字刀、6 mm 一字刀、
# 4 根扎带、4 / 5 根线、6 颗 / 每侧 4 颗螺钉，以及原片画面（操作者徒手、未测电、单手取电源）；品牌型号不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换激光电源",
    "edition": "原著版",
    "points": {
        "K1": "只限专业人员，先断电",
        "K2": "高压和强激光的伤害",
        "K3": "激光电源的残余高压",
        "K4": "全程戴绝缘手套",
        "K5": "准备工具和备件",
        "K6": "断开所有连接",
        "K7": "锁住四个脚轮",
        "K8": "静置放电和冷却",
        "K9": "打开左侧门板",
        "K10": "拆送丝安装板螺钉",
        "K11": "拆下接地线",
        "K12": "放平安装板",
        "K13": "剪扎带，不伤线缆",
        "K14": "断开船形开关的四根线",
        "K15": "断开电源的五根线",
        "K16": "拆电源支架螺钉",
        "K17": "拔黑色端子，取出电源",
        "K18": "撕膜拆螺钉，卸下支架",
        "K19": "支架装上新电源，贴回膜",
        "K20": "放回主机，插端子，拧螺钉",
        "K21": "五根线接回，线色对端子",
        "K22": "四根线接回船形开关",
        "K23": "扎带固定，别扎太紧",
        "K24": "装回左侧面板",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机旁，机内露出一个银色长方形电源模块，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine whose side is open, showing a long silver power supply module inside, and waves at the camera.",
 "这一课，看焊机的激光电源怎样更换。", "激光焊机：更换激光电源"),
("开场", "四个图标：警示卡、扎带、银色电源模块、船形开关",
 "Four icons in a row: a warning card, a cable tie, a silver power supply module and a rocker switch. No people.",
 "拆线、换电源、接线、扎线。", "", ["拆线", "换电源", "接线", "扎线"]),
# 情景
("情景", "阿杰按下焊枪扳机，焊机报警灯闪，没有出光",
 "The young male student presses the welding gun trigger; a red warning light flashes on the machine and nothing happens.",
 "阿杰发现焊机报警，焊枪不出光了。"),
("情景", "老李检查后，指着机内的银色电源模块",
 "The facility engineer finishes checking and points at the silver power supply module inside the machine.",
 "老李判断：要更换激光电源。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "专业技术人员老李来更换。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "激光电源维修，只限专业人员。", "只限专业人员，先断电"),
("K1", "老李把焊机电源开关拨到关",
 "The facility engineer switches the main power switch of the laser welding machine to off.",
 "动手之前，先关机断电。"),
# K2
("K2", "机箱剖面示意：一边闪电图标，一边激光束图标",
 "A simple cutaway diagram of a machine cabinet with a lightning bolt icon on one side and a red laser beam icon on the other side. No people.",
 "机内高压和强激光，会触电、烧伤。", "高压和强激光的伤害", ["高电压", "强激光"]),
# K3
("K3", "银色电源模块示意，内部亮着闪电图标，旁边沙漏",
 "A simple diagram of the silver power supply module with a glowing lightning bolt icon inside and an hourglass beside it. No people.",
 "残余高压，说的就是这个激光电源。", "激光电源的残余高压"),
("K3", "沙漏放在焊机旁",
 "An hourglass stands on the floor beside the closed laser welding machine. No people.",
 "至少等5分钟，才能触碰。", "", ["≥5分钟"]),
# K4
("K4", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "工作台上摆着两把十字螺丝刀、一把一字螺丝刀、剪刀、四根扎带和新电源模块",
 "On a workbench lie two cross-head screwdrivers, one flat-head screwdriver, a pair of scissors, four cable ties and a new silver power supply module. No people.",
 "5、3毫米十字刀，6毫米一字刀等。", "准备工具和备件", ["5/3mm十字刀", "6mm一字刀", "剪刀", "4根扎带", "新电源"]),
# K6
("K6", "焊机背面接口全部空着",
 "The back of the laser welding machine with all sockets empty and the unplugged cables coiled on the floor. No people.",
 "确认所有连接都已断开。", "断开所有连接"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "焊机静静放着，墙上时钟指针转动",
 "The closed laser welding machine stands still while a wall clock shows time passing. No people.",
 "静置10分钟，放电、冷却。", "静置放电和冷却", ["10分钟"]),
# K9
("K9", "老李打开焊机左侧门板",
 "The facility engineer opens the hinged left side door of the machine.",
 "打开左侧门板。", "打开左侧门板"),
# K10
("K10", "老李拆送丝安装板周边螺钉",
 "The facility engineer removes the screws around the wire feeder mounting plate.",
 "拆下安装板十四颗螺钉。", "拆送丝安装板螺钉"),
# K11
("K11", "老李拆黄绿色接地线的螺钉",
 "The facility engineer removes the screw of the yellow-green earth wire.",
 "拆下接地线螺钉。", "拆下接地线"),
# K12
("K12", "安装板放平，露出机内电气区和上方的电源模块",
 "The mounting plate is laid outward, revealing the wiring and the silver power supply module at the top of the cabinet.",
 "放平安装板。", "放平安装板"),
# K13
("K13", "剪刀小心剪断捆线的扎带",
 "Scissors carefully snip a cable tie holding a bundle of wires, leaving the wires intact.",
 "剪断四根扎带，别剪到线。", "剪扎带，不伤线缆"),
# K14
("K14", "一字螺丝刀松开船形开关背面的端子，四根线依次取下",
 "A flat-head screwdriver loosens the terminals on the back of a rocker switch and four wires are removed one by one.",
 "用6毫米一字刀断开开关4根线。", "断开船形开关的四根线"),
# K15
("K15", "十字刀拧松电源模块端子，五根线取下",
 "A cross-head screwdriver loosens the terminal screws on the power supply module and five wires are removed.",
 "用5毫米十字刀断开电源5根线。", "断开电源的五根线"),
# K16
("K16", "老李拧下电源支架的固定螺钉",
 "The facility engineer removes the screws fixing the power supply bracket to the cabinet.",
 "用3毫米十字刀拆支架6颗螺钉。", "拆电源支架螺钉"),
# K17
("K17", "老李拔下电源上的黑色插头",
 "The facility engineer unplugs a black connector from the power supply module.",
 "拔下电源上的黑色端子。", "拔黑色端子，取出电源"),
("K17", "老李单手拎着电源组件取出",
 "The facility engineer lifts the power supply assembly out of the cabinet with one hand.",
 "把整个电源组件取出来。"),
# K18
("K18", "电源放在台面，撕开侧面保护膜",
 "On the bench, the protective film on the side of the bracket is peeled back.",
 "撕开两侧的保护膜。", "撕膜拆螺钉，卸下支架"),
("K18", "每侧拧下四颗螺钉，支架和旧电源分开",
 "Four screws are removed from each side and the black bracket is separated from the old power supply.",
 "每侧拆四颗螺钉，卸下支架。"),
# K19
("K19", "支架装到新电源上，每侧四颗螺钉",
 "The black bracket is fitted onto the new power supply and four screws are tightened on each side.",
 "支架装上新电源，每侧四颗螺钉。", "支架装上新电源，贴回膜"),
("K19", "手指按压，把两侧保护膜贴平",
 "Fingers press the protective films flat on both sides of the bracket.",
 "压平两侧保护膜。"),
# K20
("K20", "新电源组件放回机内，插上黑色端子",
 "The new power supply assembly is placed back into the cabinet and the black connector is plugged in.",
 "放回主机，插上黑色端子。", "放回主机，插端子，拧螺钉"),
("K20", "六颗螺钉拧紧",
 "Six screws are tightened to secure the power supply assembly.",
 "装上六颗螺钉固定。"),
# K21
("K21", "画面一角接线参考图，五根不同颜色的线穿过黑色磁环接到端子",
 "A small reference picture in the corner while five wires of different colors pass through a black ferrite ring and are connected to blank terminals on the power supply.",
 "五根线照原样穿过磁环，接回电源。", "五根线接回，线色对端子"),
("K21", "参考图和实物端子用虚线一一对应",
 "Split view: a blank reference wiring picture and the real terminals with matching dotted lines between same-colored wires. No people.",
 "每根线的颜色，必须对上端子。"),
# K22
("K22", "四根线接回船形开关背面端子",
 "Four wires are reconnected to the terminals on the back of the rocker switch.",
 "四根线接回船形开关。", "四根线接回船形开关"),
# K23
("K23", "老李用四根扎带把线缆捆好",
 "The facility engineer bundles the cables neatly with four cable ties.",
 "用四根扎带把线缆固定好。", "扎带固定，别扎太紧"),
("K23", "扎带勒进线皮的图标被打叉",
 "An icon of a cable tie biting deep into a cable jacket, crossed out with a red X. No people.",
 "扎得太紧，会勒伤线皮。"),
# K24
("K24", "老李抬回安装板，接送丝电机线，装回接地线",
 "The facility engineer lifts the mounting plate back, plugs in the wire feeder motor cable and refits the earth wire.",
 "接回电机线和接地线。", "装回左侧面板"),
("K24", "螺钉全部装回，关上门板",
 "All screws are refitted and the side door is closed.",
 "装回螺钉，关好门板。"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, an hourglass, a rocker switch and a power supply module.",
 "专业人员操作，断电静置，拆线取电源。", "小结", ["专业人员", "断电静置", "换电源"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "线色对端子，扎带别太紧。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye in front of the laser welding machine.",
 "激光电源换好了，下次见！"),
]
