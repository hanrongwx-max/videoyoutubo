# 09_Replace the Switched-Mode Power Supply for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机内的开关电源，无旁白、只有字幕），K1–K20，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、静置 10 分钟、5 / 3 mm 螺丝刀、14 颗螺钉、4 根线，
# 以及原片画面（操作者徒手、无验电和试机）；元件品牌型号不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换开关电源",
    "edition": "原著版",
    "points": {
        "K1": "只限专业人员，先断电",
        "K2": "高压和强激光的伤害",
        "K3": "断电后仍有残余高压",
        "K4": "全程戴绝缘手套",
        "K5": "准备工具和备件",
        "K6": "断开所有连接",
        "K7": "锁住四个脚轮",
        "K8": "静置放电和冷却",
        "K9": "打开左侧门板",
        "K10": "拆送丝安装板螺钉",
        "K11": "拆下接地线",
        "K12": "放平安装板",
        "K13": "拔下主控板供电线",
        "K14": "拆螺钉，撬出电源",
        "K15": "拆下旧电源的接线",
        "K16": "新电源接线拧紧",
        "K17": "接线顺序对照参考图",
        "K18": "轻拉导线查牢固",
        "K19": "装上导轨，接回固定",
        "K20": "装回面板和接地线",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys", "Mean Well", "MEANWELL", "SMPS", "HDR", "MDR"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实训车间里一台带轮子的激光焊接机旁，向镜头招手",
 "The panda mascot stands in a university workshop next to a gray wheeled cabinet-type laser welding machine with a handheld welding gun, and waves at the camera.",
 "这一课，看焊机里的电源怎样规范更换。", "激光焊接机开关电源的规范更换"),
("开场", "四个图标：警示卡、断电插头、旧模块、新模块",
 "Four icons in a row: a warning card, an unplugged power plug, an old module and a new module. No people.",
 "看警示、做准备、拆旧件、装新件。", "", ["警示", "准备", "拆旧", "装新"]),
# 情景
("情景", "阿杰按下焊机开关，屏幕不亮，他皱眉",
 "The young male student presses the power switch of the laser welding machine; its blank display stays dark and he frowns.",
 "阿杰发现焊机里的电源坏了。"),
("情景", "老李提着工具箱走来",
 "The facility engineer walks in carrying a toolbox and a boxed spare module.",
 "专业技术人员老李来更换。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "一起看看怎么拆、怎么装。"),
# K1
("K1", "欣欣举着一张黄黑边框的警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "厂家写明：这类维修只限专业人员。", "只限专业人员，先断电"),
("K1", "学生拿螺丝刀拆机箱的图标被打叉",
 "An icon of a student opening a machine cabinet with a screwdriver, crossed out with a red X. No people.",
 "非专业人员，严禁擅自拆机。"),
("K1", "老李把焊机电源开关拨到关",
 "The facility engineer switches the main power switch of the laser welding machine to off.",
 "动手之前，第一步永远是断电。"),
# K2
("K2", "机箱剖面示意：一边闪电图标，一边激光束图标",
 "A simple cutaway diagram of a machine cabinet with a lightning bolt icon on one side and a red laser beam icon on the other side. No people.",
 "机器里有高电压，也有强激光。", "高压和强激光的伤害", ["高电压", "强激光"]),
("K2", "手部触电和烧伤的图标",
 "Two warning icons side by side: a hand with a lightning bolt and a hand with a flame burn mark. No people.",
 "处理不当，会触电、烧伤，甚至更严重。", "", ["触电", "烧伤"]),
# K3
("K3", "拔掉插头的焊机内部，一个电源模块上还闪着闪电图标",
 "Inside an unplugged machine cabinet, one power module still shows a glowing lightning bolt icon above it. No people.",
 "注意：拔了电，电源里还可能有高压。", "断电后仍有残余高压"),
("K3", "沙漏放在焊机旁",
 "An hourglass stands on the floor beside the closed laser welding machine. No people.",
 "至少等5分钟，才能碰内部。", "", ["≥5分钟"]),
# K4
("K4", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "整个维修过程，都要戴绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "工作台上摆着两把十字螺丝刀、一把一字螺丝刀和一个新电源模块",
 "On a workbench lie two cross-head screwdrivers of different sizes, one flat-head screwdriver and a new blank gray rail-mounted power supply module. No people.",
 "5、3毫米十字刀，3毫米一字刀。", "准备工具和备件", ["5mm十字刀", "3mm十字刀", "3mm一字刀", "新电源"]),
# K6
("K6", "焊机背面接口全部空着，电源线和焊枪线放在一边",
 "The back of the laser welding machine with all sockets empty; the unplugged power cable and the welding gun cable lie coiled on the floor. No people.",
 "确认电源线、焊枪线等全部断开。", "断开所有连接"),
# K7
("K7", "老李戴手套踩下焊机脚轮的刹车",
 "The facility engineer presses down the brake on a caster wheel of the laser welding machine with his foot.",
 "四个脚轮全部锁住，机器不会滑动。", "锁住四个脚轮"),
# K8
("K8", "焊机静静放着，旁边时钟指针转动",
 "The closed laser welding machine stands still while a wall clock beside it shows time passing. No people.",
 "静置10分钟，让机器放电、冷却。", "静置放电和冷却", ["10分钟"]),
# K9
("K9", "老李打开焊机左侧的门板",
 "The facility engineer opens the hinged left side door of the laser welding machine.",
 "打开机器左侧的门板。", "打开左侧门板"),
# K10
("K10", "门内是送丝机安装板，老李用十字螺丝刀拧螺钉",
 "Inside the door is a black wire feeder mounting plate; the facility engineer removes its screws one by one with a cross-head screwdriver.",
 "用5毫米十字刀拆安装板周边螺钉。", "拆送丝安装板螺钉"),
("K10", "一个小盒子里装着拆下的螺钉",
 "A small parts tray on the workbench holding the removed screws. No people.",
 "一共十四颗，放进零件盒别弄丢。"),
# K11
("K11", "老李用小十字刀拆黄绿色接地线的螺钉",
 "The facility engineer uses a small cross-head screwdriver to remove the screw holding a yellow-green earth wire on the plate.",
 "再用3毫米十字刀拆接地线螺钉。", "拆下接地线"),
# K12
("K12", "老李把安装板向外放平，露出机内的接线和模块",
 "The facility engineer carefully lays the mounting plate outward, revealing neat wiring and blank electrical modules inside the cabinet.",
 "把安装板轻轻放平，露出里面的电气区。", "放平安装板"),
# K13
("K13", "老李从主控板上拔下红黑两色的供电线",
 "The facility engineer unplugs a red and black power cable connector from the main control board.",
 "从主控板上拔下电源的供电线。", "拔下主控板供电线"),
# K14
("K14", "导轨上的灰色电源模块，老李拧下固定螺钉",
 "A gray power supply module on a silver mounting rail; the facility engineer removes its fixing screw with a cross-head screwdriver.",
 "拧下电源模块的固定螺钉。", "拆螺钉，撬出电源"),
("K14", "一字螺丝刀插进模块底部卡扣，轻轻撬起",
 "Close view of a flat-head screwdriver inserted into the clip at the bottom of the module, gently levering it off the rail.",
 "用一字刀撬开卡扣，从导轨上取下。"),
# K15
("K15", "老李手持旧电源，拧松端子螺丝",
 "The facility engineer holds the old power supply module and loosens its terminal screws.",
 "拧松四个端子螺丝。", "拆下旧电源的接线"),
("K15", "四根线拔出，旧模块放到一边",
 "Four wires are pulled out of the terminals and the old module is set aside on the workbench.",
 "拔下四根线，取下旧电源。"),
# K16
("K16", "老李从包装中取出新的电源模块",
 "The facility engineer takes a new blank gray power supply module out of its box.",
 "取出新电源。", "新电源接线拧紧"),
("K16", "四根线插入新模块端子，螺丝刀拧紧",
 "Four wires are inserted into the terminals of the new module and tightened with a small screwdriver.",
 "四根线插回对应端子，逐个拧紧。"),
# K17
("K17", "小研拿着一张参考图，图上四个端子用不同颜色圆点标出",
 "The female graduate student holds a reference diagram showing four terminals marked with colored dots beside the new module.",
 "接线顺序，必须和参考图一模一样。", "接线顺序对照参考图"),
# K18
("K18", "老李逐根轻拉导线",
 "The facility engineer gently tugs each wire at the terminals one by one.",
 "每根线轻轻一拉，确认没有松动。", "轻拉导线查牢固"),
# K19
("K19", "新模块底部卡进银色导轨",
 "The new module's bottom clip is hooked onto the silver mounting rail and pressed into place.",
 "把新电源底部卡进银色导轨。", "装上导轨，接回固定"),
("K19", "插回主控板供电线，再拧紧固定螺钉",
 "The facility engineer plugs the power cable back into the main control board, then tightens the fixing screw of the module.",
 "接回主控板供电线，拧紧固定螺钉。"),
# K20
("K20", "老李抬起安装板，把送丝电机线插回主控板",
 "The facility engineer lifts the mounting plate back up and plugs the wire feeder motor cable into the main control board.",
 "抬回安装板，接好送丝电机线。", "装回面板和接地线"),
("K20", "接地线螺钉拧紧，周边螺钉逐一装回",
 "The yellow-green earth wire screw is tightened, then the screws around the plate are refitted one by one.",
 "接地线一定装回，螺钉全部拧上。"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons floating behind: a warning card, an unplugged plug, an hourglass and a screwdriver.",
 "专业人员维修，断电，静置放电。", "小结", ["专业人员", "断电", "静置", "螺丝刀"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "按参考图接线，轻拉查牢，装回接地。"),
# 结尾
("结尾", "欣欣和老李、阿杰在焊机前挥手",
 "The panda mascot, the facility engineer and the young male student wave goodbye in front of the laser welding machine.",
 "电源换好了，下次见！"),
]
