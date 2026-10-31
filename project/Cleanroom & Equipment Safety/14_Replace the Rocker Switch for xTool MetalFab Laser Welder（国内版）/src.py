# 14_Replace the Rocker Switch for xTool MetalFab Laser Welder 卡通剧本作者源
# 原片为激光焊接设备厂家的售后维修教程（无旁白，只有字幕）：更换焊机背面的船形电源开关。
# 保留全部操作知识点 K1–K18，设备统称“手持式激光焊接机”；
# 审查补充 S1–S6（认读开关 I/O 符号、开关异常信号、正确关机顺序、湿手不碰开关、维修有人监护、工位照明与整理）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊接机电源开关的规范更换",
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
        "S1": "认读开关上的 I 和 O",
        "S2": "开关异常，马上停用",
        "S3": "关机顺序：先停光，再关电",
        "S4": "湿手油手不碰开关",
        "S5": "维修有人监护",
        "S6": "工位照明与工具摆放",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Schneider", "TeSys"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机背面，指着一个红色船形开关，向镜头招手",
 "The panda mascot stands at the back of a gray wheeled laser welding machine, points at a red illuminated rocker switch, and waves at the camera.",
 "这一课，看焊机的电源开关怎样更换。", "激光焊接机电源开关的规范更换"),
("开场", "四个图标：开关、火花、手掌、两个人",
 "Four icons in a row: a rocker switch, a spark, a hand and two people side by side. No people.",
 "开关天天用，坏了也要按规矩换。", "", ["认符号", "看异常", "关机顺序", "有人监护"]),
# 情景
("情景", "阿杰按下船形开关，开关里闪了一下火花，有一缕烟",
 "The young male student presses the red rocker switch; a small spark flashes inside it and a wisp of smoke rises.",
 "阿杰一按开关，里面啪地闪了一下。"),
("情景", "阿杰想再按几下试试，小研抓住他的手",
 "The young male student reaches to press the switch again, but the female graduate student holds his hand back.",
 "他还想多按几下，被小研拦住了。"),
("情景", "小研拔下插头，老李走过来查看",
 "The female graduate student unplugs the machine and the facility engineer comes over to look.",
 "小研先拔掉插头，请老李来换开关。"),
# S2
("S2", "开关打火、发烫、冒焦烟、指示灯不亮四个图标",
 "Four warning icons in a row: a switch with a spark, a switch with heat waves, a switch with dark smoke and a switch with a dark indicator light. No people.",
 "打火、发烫、焦味、灯不亮，都是故障。", "开关异常，马上停用", ["打火", "发烫", "焦味", "灯不亮"]),
("S2", "反复按开关试的手被打叉，旁边空白停用牌",
 "An icon of a finger pressing a faulty switch again and again, crossed out with a red X, next to a blank out-of-service tag. No people.",
 "别反复试，拔插头、挂牌、报修。"),
# S1
("S1", "红色船形开关特写，一端印着竖线，一端印着圆圈",
 "Close view of a red rocker switch with a vertical line symbol on one end and a circle symbol on the other end. No people.",
 "开关上的竖线表示通，圆圈表示断。", "认读开关上的 I 和 O", ["通", "断"]),
("S1", "欣欣按到圆圈一侧，开关灯熄灭",
 "The panda mascot presses the circle side of the switch and its light goes out.",
 "按到圆圈一侧，灯灭，才算关了。"),
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
 "断电后仍有残余高压，要等待。", "断电后仍有残余高压"),
# K4
("K4", "老李戴上厚绝缘手套",
 "The facility engineer pulls on thick insulated gloves.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# S5
("S5", "小研站在老李旁边，手边就是墙上的配电开关",
 "The female graduate student stands next to the facility engineer, within reach of the wall circuit breaker.",
 "维修时旁边要有人监护。", "维修有人监护"),
("S5", "一个人独自在机器里操作的图标被打叉",
 "An icon of a single person working alone inside an open machine, crossed out with a red X. No people.",
 "出了意外，监护人能马上断电呼救。"),
# K5
("K5", "工作台上摆着两把十字螺丝刀、一把一字螺丝刀和一个新的红色船形开关",
 "On a workbench lie two cross-head screwdrivers, one flat-head screwdriver and a new red rocker switch. No people.",
 "两把十字刀、一字刀和新开关。", "准备工具和备件", ["十字刀", "一字刀", "新开关"]),
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
 "静置一段时间，放电、冷却。", "静置放电和冷却"),
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
# S6
("S6", "老李打开头灯，机内深处被照亮",
 "The facility engineer switches on a headlamp and the deep corner of the cabinet lights up.",
 "开关在机身深处，先把光线照亮。", "工位照明与工具摆放"),
("S6", "工具整齐摆在托盘里，另一边工具散落在机器里的图标被打叉",
 "Tools arranged neatly in a tray, next to an icon of tools scattered inside a machine crossed out with a red X. No people.",
 "工具放托盘，不往机器里随手搁。"),
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
("K17", "两根线插反、开关冒火花的图标被打叉",
 "An icon of two swapped wires on a switch with a spark, crossed out with a red X. No people.",
 "插反了，开关可能断不开电。"),
# K18
("K18", "老李抬回安装板，接送丝电机线，装回接地线和螺钉",
 "The facility engineer lifts the mounting plate back, plugs in the wire feeder motor cable, refits the earth wire and screws.",
 "接回电机线、接地线，装回螺钉。", "装回左侧面板"),
("K18", "关上左侧门板",
 "The left side door is closed.",
 "关好左侧门板。"),
# S3
("S3", "关机步骤：松开焊枪扳机、焊枪挂回、按开关圆圈侧",
 "A three-step diagram joined by arrows: a hand releasing the welding gun trigger, the gun hung on its holder, and a finger pressing the circle side of the rocker switch. No people.",
 "关机先停出光，挂好焊枪，再关开关。", "关机顺序：先停光，再关电", ["停出光", "挂焊枪", "关开关"]),
("S3", "焊接时直接拍开关断电的图标被打叉",
 "An icon of a hand slapping the power switch off in the middle of welding, crossed out with a red X. No people.",
 "不要在焊接中途直接拍开关。"),
("S3", "红色急停按钮特写，旁边闪电图标",
 "Close view of the red emergency stop button next to a lightning bolt icon. No people.",
 "真有危险，按的是急停按钮。"),
# S4
("S4", "湿手按开关的图标被打叉",
 "An icon of a wet dripping hand pressing a rocker switch, crossed out with a red X. No people.",
 "湿手、油手，不碰开关。", "湿手油手不碰开关"),
("S4", "阿杰擦干手，再按开关",
 "The young male student dries his hands on a towel, then presses the switch.",
 "擦干再操作，开关周围不放水杯。"),
# 小结
("小结", "欣欣站在焊机背面，身后浮现四个图标",
 "The panda mascot stands at the back of the laser welding machine with four icons behind: a switch with line and circle symbols, a spark, a gun on a holder and two people.",
 "认得通和断，异常就停用。", "小结", ["认符号", "看异常", "关机顺序", "有人监护"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "先停光再关电，维修要有人陪。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手，开关指示灯亮着",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the machine with its switch light glowing.",
 "小开关，大责任。下次见！"),
]
