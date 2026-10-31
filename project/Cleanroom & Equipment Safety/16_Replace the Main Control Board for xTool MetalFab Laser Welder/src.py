# 16_Replace the Main Control Board for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机主控板，无旁白、只有字幕），K1–K19，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、静置 10 分钟、5 / 3 mm 十字刀、14 / 8 颗螺钉，
# 以及原片画面（操作者徒手拿主控板）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换主控板",
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
        "K13": "拔下主控板所有插头",
        "K14": "拆主控板固定螺钉",
        "K15": "取下主控板",
        "K16": "新主控板装到原位",
        "K17": "八颗螺钉固定",
        "K18": "插头按形状对应插回",
        "K19": "装回左侧面板",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys"],
}

SHOTS = [
# 开场
("开场", "欣欣站在侧门打开的激光焊接机旁，指着机内一块长条电路板，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine with its side open, points at a long blank circuit board inside, and waves at the camera.",
 "这一课，看焊机的主控板怎样更换。", "激光焊机：更换主控板"),
("开场", "四个图标：警示卡、插头、旧电路板、新电路板",
 "Four icons in a row: a warning card, a cable connector, an old circuit board and a new circuit board. No people.",
 "拔插头、拆旧板、装新板、插回。", "", ["拔插头", "拆旧板", "装新板", "插回"]),
# 情景
("情景", "阿杰开机，屏幕显示空白报警图标，焊枪不动作",
 "The young male student powers on the machine; its screen shows a blank warning icon and the welding gun does nothing.",
 "阿杰发现焊机一开机就报警。"),
("情景", "老李提着工具箱和新板盒走来",
 "The facility engineer walks in with a toolbox and a boxed new circuit board.",
 "专业技术人员老李来换主控板。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换主控板只限专业人员。", "只限专业人员，先断电"),
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
("K5", "工作台上摆着两把十字螺丝刀、一把镊子和一块新电路板",
 "On a workbench lie two cross-head screwdrivers, a pair of tweezers and a new blank circuit board. No people.",
 "5、3毫米十字刀，镊子和新主控板。", "准备工具和备件", ["5mm十字刀", "3mm十字刀", "镊子", "新主控板"]),
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
 "用5毫米十字刀拆14颗螺钉。", "拆送丝安装板螺钉"),
# K11
("K11", "老李拆黄绿色接地线的螺钉",
 "The facility engineer removes the screw of the yellow-green earth wire.",
 "用3毫米十字刀拆接地线螺钉。", "拆下接地线"),
# K12
("K12", "安装板放平，露出机内右侧一块长条电路板",
 "The mounting plate is laid outward, revealing a long circuit board on the right side of the cabinet.",
 "放平安装板，主控板就在右边。", "放平安装板"),
# K13
("K13", "画面一角是全景图，几个插头被虚线圈出，老李逐个拔下",
 "A small inset shows the whole board with several connectors circled in dotted lines, while the facility engineer unplugs them one by one.",
 "对照位置图，逐个拔下所有插头。", "拔下主控板所有插头"),
("K13", "插头上有一点胶，镊子先剥掉",
 "Close view of tweezers peeling a small blob of glue off a connector before it is unplugged.",
 "插头有固定胶，先用镊子剥掉。"),
# K14
("K14", "老李用十字刀拧下电路板四周的螺钉",
 "The facility engineer removes the screws around the edge of the circuit board with a cross-head screwdriver.",
 "拆下主控板的固定螺钉。", "拆主控板固定螺钉"),
# K15
("K15", "老李握住电路板边缘，把整块板取出",
 "The facility engineer holds the circuit board by its edges and lifts it out of the cabinet.",
 "捏住板边，取下旧主控板。", "取下主控板"),
# K16
("K16", "老李从袋里取出新主控板，放到原位",
 "The facility engineer takes the new circuit board out of its bag and places it in position in the cabinet.",
 "取出新主控板，装到原位。", "新主控板装到原位"),
# K17
("K17", "八颗螺钉逐一拧紧",
 "Eight screws are tightened one by one around the new board.",
 "用八颗螺钉固定。", "八颗螺钉固定"),
# K18
("K18", "画面一角是位置图，老李按形状把插头插回",
 "A small inset shows connector positions while the facility engineer plugs each connector back by matching its shape.",
 "每个插头按形状，对准插回。", "插头按形状对应插回"),
("K18", "插头和插座形状一一对应的示意",
 "Diagram of several connectors with different shapes, each matched to a socket of the same shape by dotted lines. No people.",
 "形状对应，避免插错口。"),
# K19
("K19", "老李抬回安装板，接送丝电机线和接地线",
 "The facility engineer lifts the mounting plate back and reconnects the wire feeder motor cable and the earth wire.",
 "接回电机线和接地线。", "装回左侧面板"),
("K19", "螺钉装回，关上左侧门板",
 "All screws are refitted and the left side door is closed.",
 "装回螺钉，关好门板。"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, an hourglass, a screwdriver and a circuit board.",
 "专业人员操作，断电静置，拔插头拆板。", "小结", ["专业人员", "断电静置", "换主控板"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "八颗螺钉固定，插头按形状插回。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye in front of the laser welding machine.",
 "主控板换好了，下次见！"),
]
