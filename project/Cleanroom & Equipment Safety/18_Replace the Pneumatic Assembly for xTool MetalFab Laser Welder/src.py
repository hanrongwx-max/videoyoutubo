# 18_Replace the Pneumatic Assembly for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：带把手机型更换气动组件，无旁白、只有字幕），K1–K23，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、工具规格（3 mm / 5 mm / 2.5 mm 十字、5 mm 内六角）、
# 8 / 3 / 2 / 2 / 2 颗螺钉、侧放垫泡沫，以及原片画面（操作者徒手、一人侧放和扶正、本片无静置字幕、拆气管前未讲关气泄压）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换气动组件（带把手机型）",
    "edition": "原著版",
    "points": {
        "K1": "只限专业人员，先断电",
        "K2": "高压和强激光的伤害",
        "K3": "断电后仍有残余高压",
        "K4": "全程戴绝缘手套",
        "K5": "准备工具和备件",
        "K6": "关机，拔掉所有线缆",
        "K7": "锁住四个脚轮",
        "K8": "松开把手螺钉",
        "K9": "取下焊枪，线缆不急弯",
        "K10": "拆挂架线缆夹，抬下右侧盖",
        "K11": "侧放机器，垫好泡沫",
        "K12": "拆底部两颗螺钉",
        "K13": "松开光纤夹",
        "K14": "按释放环拔气管，扶正",
        "K15": "黄色光纤保持原弧度",
        "K16": "拔下传感器和电磁阀线",
        "K17": "取出整个气动组件",
        "K18": "新组件穿线接主板",
        "K19": "装左侧盖：挂钩对销钉",
        "K20": "接回气管，固定光纤",
        "K21": "侧放装回底部螺钉",
        "K22": "装右侧盖，焊枪归位",
        "K23": "装回把手",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带前后把手的激光焊接机旁，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine with front and back handles and waves at the camera.",
 "这一课，换另一款焊机的气动组件。", "带把手机型气动组件的规范更换"),
("开场", "四个图标：把手、右侧盖、气动组件、左侧盖",
 "Four icons in a row: a machine handle, a side cover, an air valve block and a second side cover. No people.",
 "拆把手侧盖、换组件、装回。", "", ["拆把手", "拆侧盖", "换组件", "装回"]),
# 情景
("情景", "阿杰按下焊枪开关，焊枪没有出气，他皱眉看着",
 "The young male student presses the trigger of the welding gun but no gas flows, and he frowns at it.",
 "阿杰发现焊枪不出气了。"),
("情景", "老李提着工具箱和装着新组件的盒子走来",
 "The facility engineer comes over carrying a toolbox and a boxed new air valve assembly.",
 "专业技术人员老李来换气动组件。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "拆机维修，只限专业人员。", "只限专业人员，先断电"),
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
("K5", "工作台上摆着两把十字螺丝刀、一把内六角扳手和一个带蓝色气管的新气动组件",
 "On a workbench lie two cross-head screwdrivers, a hex key and a new air valve assembly with a solenoid, a small sensor and blue tubes. No people.",
 "3和5毫米十字刀、5毫米内六角、新组件。", "准备工具和备件", ["3mm十字", "5mm十字", "5mm内六角", "新组件"]),
# K6
("K6", "老李关机，拔下背面所有线缆",
 "The facility engineer switches off the machine and unplugs all cables from the back.",
 "关机，拔掉所有线缆。", "关机，拔掉所有线缆"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "老李用内六角松开前后把手的螺钉",
 "The facility engineer loosens the screws of the front and back handles with a hex key.",
 "用5毫米内六角，松开把手8颗螺钉。", "松开把手螺钉"),
# K9
("K9", "老李拆右侧盖螺钉，从挂架取下焊枪，线缆在台面盘成大圈",
 "The facility engineer removes the right cover screws, lifts the welding gun off its holder and lays the cable in wide loops on the bench.",
 "取下焊枪，线缆盘大圈不急弯。", "取下焊枪，线缆不急弯"),
# K10
("K10", "老李拆下挂架和线缆夹的螺钉",
 "The facility engineer removes the screws of the gun holder and the cable clamp.",
 "拆挂架3颗、线缆夹2颗螺钉。", "拆挂架线缆夹，抬下右侧盖"),
("K10", "右侧盖向上抬起取下，露出黄色光纤",
 "The right cover is lifted upward and off, revealing a yellow fiber cable looped inside.",
 "把右侧盖向上抬下来。"),
# K11
("K11", "台面上铺泡沫，老李把机器侧放上去",
 "A foam pad is placed on the bench and the facility engineer lays the machine on its side on top of it.",
 "机器侧放，左侧下面垫泡沫。", "侧放机器，垫好泡沫"),
# K12
("K12", "老李拆下机器底部的两颗螺钉",
 "The facility engineer removes two screws from the bottom of the machine.",
 "用5毫米十字刀拆底部2颗螺钉。", "拆底部两颗螺钉"),
# K13
("K13", "细十字刀松开固定黄色光纤的小夹子",
 "A fine cross-head screwdriver loosens the two screws of a small clamp holding the yellow fiber.",
 "用2.5毫米十字刀松光纤夹2颗螺钉。", "松开光纤夹"),
# K14
("K14", "手指按下快插接头的释放环，拔出气管",
 "Fingers press the release ring of a push-fit air fitting and pull the tube out.",
 "按下释放环，拔出两根气管。", "按释放环拔气管，扶正"),
("K14", "老李小心把机器扶正",
 "The facility engineer carefully stands the machine upright again.",
 "再小心把机器扶正。"),
# K15
("K15", "机内黄色光纤顺着原来的大弧度盘着",
 "Inside the machine, the yellow fiber stays in its original wide curve. No people.",
 "黄色光纤别弯折，保持原来的弧度。", "黄色光纤保持原弧度"),
# K16
("K16", "老李拆左侧盖螺钉，从主板拔下两根线",
 "The facility engineer removes the left cover screw and unplugs two cables from the main board.",
 "3毫米十字刀拆左盖螺钉，拔两根线。", "拔下传感器和电磁阀线"),
# K17
("K17", "老李把旧气动组件整个取出",
 "The facility engineer pulls the whole old air valve assembly out of the machine.",
 "把整个旧组件取出来。", "取出整个气动组件"),
# K18
("K18", "新组件的两根线从右侧穿到左侧，插回主板",
 "The two cables of the new air valve assembly are fed from the right side to the left side and plugged into the main board.",
 "新组件两根线右穿左，接回主板。", "新组件穿线接主板"),
# K19
("K19", "左侧盖两边挂钩对准机架销钉推入，拧紧螺钉",
 "The hooks on both sides of the left cover are aligned with pegs on the frame, the cover is pushed in and its screw is tightened.",
 "左侧盖挂钩对销钉推入，拧紧。", "装左侧盖：挂钩对销钉"),
# K20
("K20", "两根蓝色气管插回接头",
 "Two blue air tubes are pushed back into their fittings.",
 "接回两根气管。", "接回气管，固定光纤"),
("K20", "光纤夹拧紧，气管卡好",
 "The fiber clamp is tightened and the air tubes are clipped in place.",
 "把光纤和气管固定到位。"),
# K21
("K21", "机器再次侧放在泡沫上，装回底部两颗螺钉",
 "The machine is laid on the foam again and the two bottom screws are refitted.",
 "侧放装回底部2颗螺钉。", "侧放装回底部螺钉"),
# K22
("K22", "右侧盖装回，线缆夹、挂架拧紧，焊枪挂回",
 "The right cover is refitted, the cable clamp and gun holder are screwed in place, and the welding gun is hung back.",
 "装右侧盖，线缆夹2颗、挂架3颗螺钉。", "装右侧盖，焊枪归位"),
("K22", "侧盖螺钉装回",
 "The screw on the right cover is refitted.",
 "焊枪归位，装好侧盖螺钉。"),
# K23
("K23", "把手装回，内六角拧紧",
 "The front and back handles are refitted and tightened with a hex key.",
 "装回前后把手。", "装回把手"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, a foam pad, an air valve block and a yellow fiber loop.",
 "专业人员操作，侧放垫泡沫，换组件。", "小结", ["专业人员", "垫泡沫", "换组件", "光纤弧度"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "线缆不急弯，光纤保持原弧度。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手，焊枪挂在挂架上",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the machine with its gun hung on the holder.",
 "气动组件换好了，下次见！"),
]
