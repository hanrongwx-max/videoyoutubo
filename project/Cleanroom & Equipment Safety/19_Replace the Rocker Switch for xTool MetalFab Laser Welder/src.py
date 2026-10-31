# 19_Replace the Rocker Switch for xTool MetalFab Laser Welder 卡通剧本作者源
# 原片为激光焊接设备厂家的售后维修教程（无旁白，只有字幕）：更换带把手机型后盖上的船形开关（与第 14 集同部件、不同机型）。
# 保留全部操作知识点 K1–K16，设备统称“手持式激光焊接机”；
# 审查补充 S1–S4（停电后先关开关、机壳发麻立即停用、开机前点检、操作规程和应急电话上墙）；
# 开关符号、异常停用、关机顺序、湿手、监护、照明已在第 14 集补充，不重复
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "带把手机型电源开关的规范更换",
    "points": {
        "K1": "只限专业人员，先断电",
        "K2": "高压和强激光的伤害",
        "K3": "断电后仍有残余高压",
        "K4": "全程戴绝缘手套",
        "K5": "准备工具和备件",
        "K6": "拔掉所有线缆",
        "K7": "锁住四个脚轮",
        "K8": "拆后把手，扶住防掉落",
        "K9": "拆后盖四颗螺钉",
        "K10": "拔下开关的四根线",
        "K11": "认清锁定卡舌",
        "K12": "交替按卡舌，推出开关",
        "K13": "新开关外侧插入，O朝下",
        "K14": "短线接上，长线接下",
        "K15": "装回后盖，拧紧螺钉",
        "K16": "装回后把手",
        "S1": "停电后先关开关",
        "S2": "机壳发麻，立即停用",
        "S3": "开机前点检",
        "S4": "规程和应急电话上墙",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带把手的激光焊接机背面，指着后盖上的红色开关，向镜头招手",
 "The panda mascot stands at the back of a gray wheeled laser welding machine with handles, points at the red rocker switch on its rear cover, and waves at the camera.",
 "这一课，换另一款焊机的电源开关。", "带把手机型电源开关的规范更换"),
("开场", "四个图标：闪电恢复的灯泡、手摸机壳、点检表、墙上的告示板",
 "Four icons in a row: a light bulb with a returning lightning bolt, a hand touching a machine case, a checklist and a notice board on a wall. No people.",
 "换好开关，用电习惯也要跟上。", "", ["停电先关", "发麻停用", "开机点检", "规程上墙"]),
# 情景
("情景", "实验室灯突然熄灭，阿杰的焊机也停了",
 "The lab lights suddenly go out and the young male student's laser welding machine stops.",
 "实验楼突然停电，焊机也停了。"),
("情景", "来电后焊机突然自己启动，风扇呼呼转，阿杰吓一跳",
 "When power returns, the machine suddenly starts by itself with its fan whirring, and the young male student jumps back in surprise.",
 "来电那一刻，焊机自己又启动了。"),
("情景", "小研关掉开关，开关一按就松垮，老李来看",
 "The female graduate student switches it off; the rocker switch feels loose and wobbly, and the facility engineer comes to check.",
 "开关也松了，老李决定换开关。"),
# S1
("S1", "欣欣举起一根手指，旁边灯泡熄灭的图标",
 "The panda mascot raises one finger next to an icon of a light bulb going dark.",
 "停电或跳闸，先把设备开关关掉。", "停电后先关开关"),
("S1", "来电时机器突然启动、人在旁边吓到的图标被打叉",
 "An icon of a machine suddenly starting when power returns while a person stands next to it, crossed out with a red X. No people.",
 "不然来电时机器突然动作，很危险。"),
("S1", "小研关掉开关，查明原因后再开",
 "The female graduate student keeps the switch off and checks a blank notice before switching on again.",
 "查明原因、确认安全，再重新开机。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换开关要拆机，只限专业人员。", "只限专业人员，先断电"),
# K2
("K2", "机箱剖面示意：一边闪电图标，一边激光束图标",
 "A simple cutaway diagram of a machine cabinet with a lightning bolt icon on one side and a red laser beam icon on the other side. No people.",
 "机内高压和强激光，会触电、烧伤。", "高压和强激光的伤害", ["高电压", "强激光"]),
# K3
("K3", "拔掉插头的焊机内部，一个模块上闪电图标，旁边沙漏",
 "Inside an unplugged machine cabinet, one module shows a glowing lightning bolt icon, with an hourglass beside it. No people.",
 "断电后仍有残余高压，按说明书等待。", "断电后仍有残余高压"),
# K4
("K4", "老李戴上厚绝缘手套",
 "The facility engineer pulls on thick insulated gloves.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "木板上摆着一把内六角扳手、一把一字螺丝刀、一把十字螺丝刀和一个红色船形开关",
 "On a wooden board lie a hex key, a flat-head screwdriver, a cross-head screwdriver and a new red rocker switch. No people.",
 "内六角、一字刀、十字刀和新开关。", "准备工具和备件", ["内六角", "一字刀", "十字刀", "新开关"]),
# K6
("K6", "老李拔下机器背面所有线缆",
 "The facility engineer unplugs all cables from the back of the machine.",
 "拔掉设备上的所有线缆。", "拔掉所有线缆"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "老李用内六角松开后把手一侧的两颗螺钉",
 "The facility engineer loosens two screws on one side of the rear handle with a hex key.",
 "松开后把手一侧的两颗螺钉。", "拆后把手，扶住防掉落"),
("K8", "拆最后一颗螺钉时，老李另一只手托住把手",
 "While removing the last screw, the facility engineer supports the handle with his other hand.",
 "拆最后一颗时扶住把手，别让它砸下。"),
# K9
("K9", "老李用十字刀拆下后盖的四颗螺钉",
 "The facility engineer removes the four screws of the rear cover with a cross-head screwdriver.",
 "拆下后盖四颗螺钉，翻开后盖。", "拆后盖四颗螺钉"),
# K10
("K10", "后盖翻开，开关背面四根线的插片被逐个拔下",
 "The rear cover is tilted open and the four wire connectors on the back of the switch are pulled off one by one.",
 "拔下开关背面的四根线。", "拔下开关的四根线"),
# K11
("K11", "画面一角红箭头指着开关侧面的小卡舌",
 "A small inset with red arrows points at the small locking tabs on the sides of the rocker switch. No people.",
 "开关四边各有一个锁定卡舌。", "认清锁定卡舌"),
# K12
("K12", "一字刀轮流按压卡舌，另一只手从内侧推开关",
 "A flat-head screwdriver presses the tabs one after another while the other hand pushes the switch out from the inside.",
 "一字刀交替按卡舌，从里往外推。", "交替按卡舌，推出开关"),
# K13
("K13", "新开关从后盖外侧插入，圆圈一端朝下",
 "The new rocker switch is inserted into the rear cover from the outside, with its circle symbol end facing down.",
 "新开关从外侧插入，圆圈朝下。", "新开关外侧插入，O朝下"),
("K13", "两台机器的开关都是按下端为关",
 "Two machines side by side, both switches with the circle end at the bottom. No people.",
 "方向统一，大家按开关才不会弄反。"),
# K14
("K14", "两根短线插到开关上方端子，两根长线插到下方端子",
 "Two shorter wires are pushed onto the top terminals of the switch and two longer wires onto the bottom terminals.",
 "短线接上方，长线接下方。", "短线接上，长线接下"),
("K14", "老李轻拉每根插片线",
 "The facility engineer gently tugs each wire connector.",
 "插到底，轻拉不脱。"),
# K15
("K15", "后盖合上，四颗螺钉拧紧",
 "The rear cover is closed and its four screws are tightened.",
 "装回后盖，拧紧全部螺钉。", "装回后盖，拧紧螺钉"),
# K16
("K16", "后把手装回，内六角拧紧",
 "The rear handle is refitted and tightened with a hex key.",
 "装回后把手。", "装回后把手"),
# S2
("S2", "阿杰手背碰到机壳，手上出现麻电的波纹图标",
 "The young male student's hand touches the machine case and a tingling wave icon appears on his hand.",
 "碰到机壳手发麻，说明可能漏电。", "机壳发麻，立即停用"),
("S2", "小研立即拉下墙上开关，挂上空白停用牌",
 "The female graduate student immediately switches off the wall breaker and hangs a blank out-of-service tag.",
 "马上断电，挂牌停用，报修。"),
("S2", "再摸一次试试的手被打叉",
 "An icon of a hand reaching to touch the case again to test, crossed out with a red X. No people.",
 "不要再去摸着试。"),
# S3
("S3", "阿杰拿着空白点检卡站在焊机前",
 "The young male student stands in front of the machine holding a blank pre-use checklist card.",
 "每次开机前，按点检卡看一遍。", "开机前点检"),
("S3", "点检项目图标：开关、急停、线缆、外壳、气源",
 "Checklist icons in a row: a rocker switch, an emergency stop button, a cable, a machine case and a gas valve. No people.",
 "开关、急停、线缆、外壳、气源。", "", ["开关", "急停", "线缆", "外壳", "气源"]),
("S3", "阿杰在点检卡上打勾，有一项画问号便停下",
 "The young male student ticks items on the card; at one item he draws a question mark and stops.",
 "有一项不对，就先不开机。"),
# S4
("S4", "焊机旁墙上贴着空白的操作规程和电话卡",
 "On the wall beside the machine hang a blank operating procedure sheet and a blank emergency contact card.",
 "设备旁贴好操作规程和应急电话。", "规程和应急电话上墙"),
("S4", "电话卡上只有电话图标、数字119和120",
 "A close view of the contact card showing a phone icon and the numbers 119 and 120. No people.",
 "火警119，急救120，再报告负责人。", "", ["119", "120"]),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a dark light bulb, a tingling hand, a checklist and a wall notice.",
 "停电先关开关，发麻立即停用。", "小结", ["停电先关", "发麻停用", "开机点检", "规程上墙"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "开机前点检，规程电话贴在旁边。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手，墙上贴着告示",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the machine, with notices on the wall.",
 "开关在手，安全在心。下次见！"),
]
