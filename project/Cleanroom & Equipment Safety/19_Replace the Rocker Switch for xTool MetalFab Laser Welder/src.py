# 19_Replace the Rocker Switch for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：带把手机型更换后盖上的船形开关，无旁白、只有字幕），K1–K16，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、工具规格（5 mm 内六角、3 mm 一字、3 mm 十字）、
# 2 / 4 颗螺钉、4 个卡舌、“O”朝下、短线接上长线接下，以及原片画面（操作者徒手、本片无静置字幕）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换船形开关（带把手机型）",
    "edition": "原著版",
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
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带把手的激光焊接机背面，指着后盖上的红色开关，向镜头招手",
 "The panda mascot stands at the back of a gray wheeled laser welding machine with handles, points at the red rocker switch on its rear cover, and waves at the camera.",
 "这一课，换另一款焊机的电源开关。", "带把手机型电源开关的规范更换"),
("开场", "四个图标：把手、后盖、船形开关、插片线",
 "Four icons in a row: a machine handle, a rear cover, a rocker switch and a wire connector. No people.",
 "拆把手、开后盖、换开关、装回。", "", ["拆把手", "开后盖", "换开关", "装回"]),
# 情景
("情景", "阿杰按焊机后盖上的红色开关，开关松垮按不住",
 "The young male student presses the red rocker switch on the machine's rear cover, but it feels loose and wobbly.",
 "阿杰发现焊机开关松了。"),
("情景", "老李提着工具箱和新开关走来",
 "The facility engineer comes over carrying a toolbox and a new red rocker switch.",
 "专业技术人员老李来换开关。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
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
 "可能残留高压，至少等5分钟再碰。", "断电后仍有残余高压", ["≥5分钟"]),
# K4
("K4", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "木板上摆着一把内六角扳手、一把一字螺丝刀、一把十字螺丝刀和一个红色船形开关",
 "On a wooden board lie a hex key, a flat-head screwdriver, a cross-head screwdriver and a new red rocker switch. No people.",
 "5毫米内六角、3毫米一字和十字刀。", "准备工具和备件", ["5mm内六角", "3mm一字", "3mm十字", "新开关"]),
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
 "用5毫米内六角，松开一侧2颗螺钉。", "拆后把手，扶住防掉落"),
("K8", "拆最后一颗螺钉时，老李另一只手托住把手",
 "While removing the last screw, the facility engineer supports the handle with his other hand.",
 "拆最后一颗时扶住把手，别让它砸下。"),
# K9
("K9", "老李用十字刀拆下后盖的四颗螺钉",
 "The facility engineer removes the four screws of the rear cover with a cross-head screwdriver.",
 "十字刀拆下后盖4颗螺钉，翻开后盖。", "拆后盖四颗螺钉"),
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
# K14
("K14", "两根短线插到开关上方端子，两根长线插到下方端子",
 "Two shorter wires are pushed onto the top terminals of the switch and two longer wires onto the bottom terminals.",
 "短线接上方，长线接下方。", "短线接上，长线接下"),
# K15
("K15", "后盖合上，四颗螺钉拧紧",
 "The rear cover is closed and its four screws are tightened.",
 "装回后盖，拧紧全部螺钉。", "装回后盖，拧紧螺钉"),
# K16
("K16", "后把手装回，内六角拧紧",
 "The rear handle is refitted and tightened with a hex key.",
 "装回后把手。", "装回后把手"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, a handle, a rocker switch and a wire connector.",
 "专业人员操作，扶住把手，按卡舌。", "小结", ["专业人员", "扶住把手", "按卡舌", "O朝下"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "O朝下，短线接上，长线接下。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the laser welding machine.",
 "开关换好了，下次见！"),
]
