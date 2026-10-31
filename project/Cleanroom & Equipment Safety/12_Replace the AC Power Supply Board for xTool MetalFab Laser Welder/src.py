# 12_Replace the AC Power Supply Board for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机交流电源板，无旁白、只有字幕），K1–K19，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、静置 10 分钟、5 / 3 mm 十字刀、14 颗 / 4 颗螺钉，
# 以及原片画面（操作者徒手）；品牌和元件厂商不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换交流电源板",
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
        "K13": "拆下电源板上的导线",
        "K14": "拔下直流电源线",
        "K15": "拆四角螺钉，取下旧板",
        "K16": "新板四颗螺钉固定",
        "K17": "对照参考图接回导线",
        "K18": "插回直流电源线",
        "K19": "装回面板和接地线",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys", "VIIP"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机旁，身后墙上是一个插座和配电箱，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine, with a wall socket and a small distribution box behind it, and waves at the camera.",
 "这一课，看焊机的交流电源板怎样更换。", "激光焊接机交流电源板的规范更换"),
("开场", "电网输电线、插头、电路板、焊机四个图标用箭头连起",
 "Four icons joined by arrows: a power line tower, a plug, a circuit board and a laser welding machine. No people.",
 "市电进机器，第一站就是这块板。", "", ["市电", "插头", "电源板", "焊机"]),
# 情景
("情景", "阿杰按下焊机开关，焊机没有反应",
 "The young male student presses the power switch of the laser welding machine; nothing lights up.",
 "阿杰发现焊机通不上电了。"),
("情景", "老李检查后，拿出一块新的电源板",
 "The facility engineer checks the machine and takes out a new blank power supply board from a box.",
 "专业技术人员老李要换交流电源板。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换电源板只限专业人员动手。", "只限专业人员，先断电"),
("K1", "老李把焊机电源开关拨到关",
 "The facility engineer switches the main power switch of the laser welding machine to off.",
 "先关机、断电。"),
# K2
("K2", "机箱剖面示意：一边闪电图标，一边激光束图标",
 "A simple cutaway diagram of a machine cabinet with a lightning bolt icon on one side and a red laser beam icon on the other side. No people.",
 "机内高压和强激光，会触电、烧伤。", "高压和强激光的伤害", ["高电压", "强激光"]),
# K3
("K3", "拔掉插头的焊机内部，一个模块上闪电图标，旁边沙漏",
 "Inside an unplugged machine cabinet, one module shows a glowing lightning bolt icon, with an hourglass beside it. No people.",
 "可能残留高压，至少等5分钟再碰。", "断电后仍有残余高压", ["≥5分钟"]),
# K4
("K4", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "工作台上摆着大小两把十字螺丝刀和一块新的黑色电源板",
 "On a workbench lie two cross-head screwdrivers of different sizes and a new blank black power supply circuit board. No people.",
 "备好5毫米、3毫米十字刀和新电源板。", "准备工具和备件", ["5mm十字刀", "3mm十字刀", "新电源板"]),
# K6
("K6", "焊机背面接口全部空着，电源线放在一边",
 "The back of the laser welding machine with all sockets empty; the unplugged power cable lies coiled on the floor. No people.",
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
 "The facility engineer opens the hinged left side door of the laser welding machine.",
 "打开左侧门板。", "打开左侧门板"),
# K10
("K10", "老李用十字刀拆送丝安装板周边螺钉，零件盒里螺钉渐多",
 "The facility engineer removes the screws around the wire feeder mounting plate; a parts tray beside him fills with screws.",
 "用5毫米十字刀拆安装板14颗螺钉。", "拆送丝安装板螺钉"),
# K11
("K11", "老李用小十字刀拆黄绿色接地线的螺钉",
 "The facility engineer uses a small cross-head screwdriver to remove the screw of the yellow-green earth wire.",
 "用3毫米十字刀拆接地线螺钉。", "拆下接地线"),
# K12
("K12", "安装板放平，露出机内电气区",
 "The mounting plate is laid outward, revealing neat wiring and blank modules inside the cabinet.",
 "放平安装板，露出电气区。", "放平安装板"),
# K13
("K13", "老李逐个拧下电源板端子螺丝",
 "The facility engineer unscrews the wires from the power supply board terminals one by one.",
 "拆下电源板端子上的各根导线。", "拆下电源板上的导线"),
# K14
("K14", "老李拔下电源板上的直流电源线插头",
 "The facility engineer unplugs the DC power cable connector from the board.",
 "拔下直流电源线。", "拔下直流电源线"),
# K15
("K15", "老李拆下电路板四个角的螺钉",
 "The facility engineer removes the four corner screws of the circuit board.",
 "拆下四个角的螺钉。", "拆四角螺钉，取下旧板"),
("K15", "旧电源板被取出",
 "The old power supply board is lifted out of the cabinet.",
 "取下旧电源板。"),
# K16
("K16", "新电源板放进原位，四颗螺钉拧紧",
 "The new power supply board is placed in position and its four corner screws are tightened.",
 "新板放回原位，四颗螺钉固定。", "新板四颗螺钉固定"),
# K17
("K17", "画面一角是接线参考图，老李逐根把导线接回端子",
 "A small reference wiring picture in the corner while the facility engineer reconnects each wire to the board terminals.",
 "对照参考图，一根一根接回导线。", "对照参考图接回导线"),
("K17", "参考图和实物端子用虚线一一对应",
 "Split view: a blank reference wiring picture and the real terminals, with matching dotted lines between them. No people.",
 "位置、颜色都要和参考图一致。"),
# K18
("K18", "直流电源线插回电源板",
 "The DC power cable connector is plugged back into the new board.",
 "插回直流电源线。", "插回直流电源线"),
# K19
("K19", "老李抬回安装板，插回送丝电机线",
 "The facility engineer lifts the mounting plate back and plugs the wire feeder motor cable into the main board.",
 "抬回安装板，接回送丝电机线。", "装回面板和接地线"),
("K19", "接地线螺钉拧紧，周边螺钉装回，关上门板",
 "The earth wire screw is tightened, the screws around the plate are refitted and the side door is closed.",
 "装回接地线和螺钉，关好门板。"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, an unplugged plug, an hourglass and a screwdriver.",
 "专业人员操作，断开连接，静置放电。", "小结", ["专业人员", "断电", "静置"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "拆线换板，对照参考图接回。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the repaired laser welding machine.",
 "电源板换好了，下次见！"),
]
