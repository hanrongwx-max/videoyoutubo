# 14_Replace the Rocker Switch for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机船形电源开关，无旁白、只有字幕），K1–K18，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、静置 10 分钟、5 / 3 mm 十字刀、6 mm 一字刀、
# 14 颗螺钉、4 根线、“咔嗒”声确认，以及原片画面（操作者徒手、单人操作）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换船形开关",
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
        "K13": "压弹片，逐根拔线",
        "K14": "压卡扣，推出旧开关",
        "K15": "按入新开关，听咔嗒声",
        "K16": "插回四根线，咔嗒到位",
        "K17": "线色对应端子",
        "K18": "装回左侧面板",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机背面，指着一个红色船形开关，向镜头招手",
 "The panda mascot stands at the back of a gray wheeled laser welding machine, points at a red illuminated rocker switch, and waves at the camera.",
 "这一课，看焊机的电源开关怎样更换。", "激光焊接机电源开关的规范更换"),
("开场", "四个图标：警示卡、螺丝刀、旧开关、新开关",
 "Four icons in a row: a warning card, a flat-head screwdriver, an old rocker switch and a new rocker switch. No people.",
 "看警示、拆旧开关、装新开关。", "", ["警示", "拆旧", "装新"]),
# 情景
("情景", "阿杰按下船形开关，开关没有反应",
 "The young male student presses the red rocker switch; its light stays off and nothing happens.",
 "阿杰发现焊机的电源开关坏了。"),
("情景", "老李提着工具箱和新开关走来",
 "The facility engineer comes over carrying a toolbox and a new red rocker switch.",
 "专业技术人员老李来换开关。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换开关也要拆机，只限专业人员。", "只限专业人员，先断电"),
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
("K5", "工作台上摆着两把十字螺丝刀、一把一字螺丝刀和一个新的红色船形开关",
 "On a workbench lie two cross-head screwdrivers, one flat-head screwdriver and a new red rocker switch. No people.",
 "5、3毫米十字刀，6毫米一字刀，新开关。", "准备工具和备件", ["5/3mm十字刀", "6mm一字刀", "新开关"]),
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
("K12", "安装板放平，露出机内电气区",
 "The mounting plate is laid outward, revealing the wiring inside the cabinet.",
 "放平安装板。", "放平安装板"),
# K13
("K13", "一字刀压住端子上的弹片，另一只手同时把导线拔出",
 "Close view: a flat-head screwdriver presses the spring clip on a push-in terminal while the other hand pulls the wire out at the same time.",
 "一字刀压住端子弹片，同时拔线。", "压弹片，逐根拔线"),
("K13", "四根线逐根拆下",
 "The four wires are removed from the switch terminals one by one.",
 "四根线一根一根拆下来。"),
# K14
("K14", "示意图：一字刀压下开关角上的凸起卡扣",
 "A simple diagram: a flat-head screwdriver presses down a raised latch at the corner of the rocker switch body. No people.",
 "一字刀压下开关角上的卡扣。", "压卡扣，推出旧开关"),
("K14", "开关从面板另一侧被推出，取下",
 "The rocker switch is pushed out through the panel from the other side and removed.",
 "从面板另一侧把开关推出来。"),
# K15
("K15", "老李在机身背面把新开关按进安装孔",
 "At the back of the machine, the facility engineer presses the new rocker switch into its mounting hole.",
 "新开关从外侧按进安装孔。", "按入新开关，听咔嗒声"),
("K15", "按入的瞬间出现咔嗒音符图标",
 "As the switch snaps into place, a small click sound icon appears beside it. No people.",
 "听到咔嗒一声，说明装牢了。"),
# K16
("K16", "导线插进端子，出现咔嗒音符图标",
 "A wire is pushed into a push-in terminal on the back of the switch and a small click sound icon appears.",
 "四根线逐根插回，咔嗒一声到位。", "插回四根线，咔嗒到位"),
# K17
("K17", "四根不同颜色的线和参考图用虚线对应",
 "Split view: a blank reference wiring picture and the four colored wires on the switch, with matching dotted lines. No people.",
 "每根线的颜色，都要对上端子。", "线色对应端子"),
# K18
("K18", "老李抬回安装板，接送丝电机线，装回接地线和螺钉",
 "The facility engineer lifts the mounting plate back, plugs in the wire feeder motor cable, refits the earth wire and screws.",
 "接回电机线、接地线，装回螺钉。", "装回左侧面板"),
("K18", "关上左侧门板",
 "The left side door is closed.",
 "关好左侧门板。"),
# 小结
("小结", "欣欣站在焊机背面，身后浮现四个图标",
 "The panda mascot stands at the back of the laser welding machine with four icons behind: a warning card, an hourglass, a flat-head screwdriver and a rocker switch.",
 "专业人员操作，断电静置，压弹片拔线。", "小结", ["专业人员", "断电静置", "压弹片"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "听到咔嗒才到位，线色对端子。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手，开关指示灯亮着",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the machine with its switch light glowing.",
 "开关换好了，下次见！"),
]
