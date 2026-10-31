# 17_Replace the Welding Torch Communication Cable for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊枪通讯线，无旁白、只有字幕），K1–K27，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、工具规格（3 mm / PH0 十字、5 mm 内六角、T6 梅花）、
# 8 / 3 / 2 / 9 颗螺钉、4 个线卡、回形针作记号，以及原片画面（操作者徒手、本片无静置字幕）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换焊枪通讯线",
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
        "K9": "拆左侧盖螺钉",
        "K10": "取下焊枪，线缆不急弯",
        "K11": "拆挂架和线缆夹",
        "K12": "抬下右侧盖",
        "K13": "拆焊枪外壳螺钉",
        "K14": "拔下通讯线，拆底壳螺钉",
        "K15": "拆线缆支架，别剪错线",
        "K16": "松开线卡，回形针作记号",
        "K17": "从弹簧和护套抽出旧线",
        "K18": "转动机器，拔主板端",
        "K19": "新线穿弹簧，接焊枪主板",
        "K20": "线塞进护套，完全包住",
        "K21": "穿过右侧盖，接主板",
        "K22": "按记号紧固线卡，取回形针",
        "K23": "装底壳，接线，轻拉检查",
        "K24": "装顶盖，弹簧到位，拧紧",
        "K25": "装右侧盖，焊枪归位",
        "K26": "装左侧盖：挂钩对销钉",
        "K27": "装回把手",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带前后把手的激光焊接机旁，手里举着焊枪，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine with handles at the front and back, holding up its handheld welding gun, and waves at the camera.",
 "这一课，看焊枪通讯线怎样更换。", "激光焊机：更换焊枪通讯线"),
("开场", "焊枪、长线缆、主机三个图标用虚线连起",
 "Three icons joined by a dotted line: a handheld welding gun, a long coiled cable and a machine cabinet. No people.",
 "拆侧盖、开焊枪、换线、装回。", "", ["拆侧盖", "开焊枪", "换线", "装回"]),
# 情景
("情景", "阿杰按焊枪上的按键，屏幕时有时无地跳出报警图标",
 "The young male student presses the buttons on the welding gun while a warning icon flickers on and off on the machine screen.",
 "阿杰发现焊枪按键时灵时不灵。"),
("情景", "老李提着工具箱和一卷新线走来",
 "The facility engineer comes over carrying a toolbox and a new coiled cable.",
 "专业技术人员老李来换通讯线。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看具体步骤。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换线要拆机，只限专业人员。", "只限专业人员，先断电"),
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
("K5", "工作台上摆着几把粗细不同的螺丝刀、内六角、剪刀、扎带、回形针和一卷新线",
 "On a workbench lie several screwdrivers of different sizes, a hex driver, scissors, cable ties, paper clips and a new coiled cable. No people.",
 "3毫米和PH0十字、5毫米内六角、T6梅花。", "准备工具和备件", ["3mm/PH0十字", "5mm内六角", "T6梅花", "回形针", "新线"]),
("K5", "老李举起一枚回形针",
 "The facility engineer holds up a single paper clip and smiles.",
 "还有回形针，待会儿做记号用。"),
# K6
("K6", "老李关机，拔下背面所有线缆",
 "The facility engineer switches off the machine and unplugs all cables from the back.",
 "关机，拔掉所有线缆。", "关机，拔掉所有线缆"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "机器两端的把手连接处被虚线圈出，老李用内六角松螺钉",
 "The joints of the front and back handles are circled with dotted lines while the facility engineer loosens the screws with a hex driver.",
 "用5毫米内六角，松开把手8颗螺钉。", "松开把手螺钉"),
# K9
("K9", "老李拆下左侧盖上的螺钉",
 "The facility engineer removes the screw on the left side cover.",
 "用3毫米十字刀拆左侧盖螺钉。", "拆左侧盖螺钉"),
# K10
("K10", "老李拆右侧盖螺钉，再从挂架上取下焊枪",
 "The facility engineer removes the screws on the right side cover, then lifts the welding gun off its holder.",
 "拆右侧盖螺钉，取下焊枪。", "取下焊枪，线缆不急弯"),
("K10", "焊枪线缆在台面上盘成大弧度",
 "The welding gun cable is laid on the bench in wide gentle curves. No people.",
 "线缆别打急弯，保持挂着时的弧度。"),
# K11
("K11", "老李拆下焊枪挂架的三颗螺钉，取下挂架",
 "The facility engineer removes three screws from the gun holder and takes it off.",
 "拆下挂架三颗螺钉，取下挂架。", "拆挂架和线缆夹"),
("K11", "画面一角红箭头标出线缆夹的两颗螺钉",
 "A small inset with red arrows marks the two screws of the cable clamp as they are removed.",
 "再拆线缆夹的两颗螺钉。"),
# K12
("K12", "老李把右侧盖向上抬起，整块取下",
 "The facility engineer lifts the right side cover upward and takes it off completely.",
 "右侧盖向上抬，完全取下来。", "抬下右侧盖"),
# K13
("K13", "老李手持焊枪，用细梅花螺丝刀拆外壳螺钉，焊枪头部有激光警告标志",
 "The facility engineer holds the welding gun and removes its shell screws with a fine star-tip screwdriver; a laser warning sign is on the gun head.",
 "用T6梅花刀，拆下外壳9颗螺钉。", "拆焊枪外壳螺钉"),
# K14
("K14", "焊枪外壳打开，老李抬起接线插座拔下线",
 "The gun shell is opened and the facility engineer lifts a small connector latch and unplugs the cable.",
 "抬起插座，拔下通讯线。", "拔下通讯线，拆底壳螺钉"),
("K14", "细十字刀拆下底壳螺钉",
 "A fine cross-head screwdriver removes the screw on the bottom shell of the gun.",
 "用PH0十字刀拆底壳螺钉。"),
# K15
("K15", "侧盖打开的机身里，老李用梅花刀拆线缆支架",
 "Inside the open machine side, the facility engineer removes a small cable bracket with a star-tip screwdriver.",
 "用T6梅花刀拆下线缆支架。", "拆线缆支架，别剪错线"),
("K15", "剪刀靠近一束线，只剪扎带不碰导线",
 "Scissors snip only a cable tie next to a bundle of wires without touching the wires.",
 "剪扎带时小心，别剪到其他线。"),
# K16
("K16", "黑色线缆护套上四个线卡，老李逐个拧松",
 "Four clamps hold a black cable sleeve inside the machine; the facility engineer loosens them one by one.",
 "3毫米十字刀逐个松开4个线卡。", "松开线卡，回形针作记号"),
("K16", "每个线卡位置插上一枚回形针",
 "A paper clip is inserted at each clamp position on the sleeve as a marker. No people.",
 "每个位置插一枚回形针作记号。"),
# K17
("K17", "通讯线从弹簧和黑色护套里被抽出",
 "The communication cable is pulled out from inside a spring and the black sleeve.",
 "把旧线从弹簧和护套里抽出来。", "从弹簧和护套抽出旧线"),
# K18
("K18", "老李转动机器，从主板上拔下线的另一端",
 "The facility engineer turns the machine around and unplugs the other end of the cable from the main board.",
 "转动机器，拔下主板上的另一端。", "转动机器，拔主板端"),
# K19
("K19", "新线穿过弹簧，接到焊枪内的小电路板",
 "The new cable is threaded through the spring and plugged into a small circuit board inside the gun end.",
 "新线穿过弹簧，接到焊枪主板。", "新线穿弹簧，接焊枪主板"),
("K19", "线缆支架拧紧",
 "The cable bracket is screwed back in place.",
 "装回线缆支架。"),
# K20
("K20", "线缆被慢慢塞进黑色护套，直到看不见",
 "The cable is gradually pushed into the black sleeve until it is fully covered.",
 "线塞进黑色护套，直到完全包住。", "线塞进护套，完全包住"),
# K21
("K21", "线头穿过右侧盖的过孔，转到机器另一侧插到主板",
 "The cable end is routed through a hole in the right cover and plugged into the main board on the other side of the machine.",
 "穿过右侧盖，另一端插回主板。", "穿过右侧盖，接主板"),
# K22
("K22", "老李对着回形针的位置拧紧线卡",
 "The facility engineer tightens each clamp exactly where a paper clip marks the position.",
 "对着回形针记号，逐个拧紧线卡。", "按记号紧固线卡，取回形针"),
("K22", "回形针全部取下放回盒里",
 "All the paper clips are removed and dropped back into a small box.",
 "拧好后，回形针一个不落取下来。"),
# K23
("K23", "焊枪底壳螺钉装回，线接回原位",
 "The bottom shell screw of the gun is refitted and the wire is reconnected to its original position.",
 "装回底壳螺钉，线接回原位。", "装底壳，接线，轻拉检查"),
("K23", "老李轻拉导线",
 "The facility engineer gently tugs the wire to check it.",
 "轻拉一下，确认接牢。"),
# K24
("K24", "顶盖合上前，手指把护套里的弹簧推到位",
 "Before closing the top cover, a finger pushes the spring inside the black sleeve into its seat.",
 "装顶盖前，确认护套里的弹簧到位。", "装顶盖，弹簧到位，拧紧"),
("K24", "上下壳螺钉逐颗拧紧",
 "All screws on the top and bottom shells of the gun are tightened one by one.",
 "上下壳的螺钉全部拧紧。"),
# K25
("K25", "右侧盖装回，线缆夹和挂架螺钉拧紧",
 "The right cover is refitted, and the screws of the cable clamp and the gun holder are tightened.",
 "装回右侧盖、线缆夹和挂架。", "装右侧盖，焊枪归位"),
("K25", "焊枪放回挂架，侧盖螺钉装回",
 "The welding gun is placed back into its holder and the right cover screw is refitted.",
 "焊枪放回挂架，装好螺钉。"),
# K26
("K26", "左侧盖两边的挂钩对准机架上的销钉，推进去",
 "The hooks on both sides of the left cover are aligned with pegs on the frame and the cover is pushed in.",
 "左侧盖挂钩对准销钉，推进去。", "装左侧盖：挂钩对销钉"),
("K26", "拧紧左侧盖螺钉",
 "The screw securing the left cover is tightened.",
 "拧紧螺钉固定。"),
# K27
("K27", "两端把手装回，每侧四颗螺钉",
 "The front and back handles are refitted with four screws on each side.",
 "装回把手，两侧各四颗螺钉。", "装回把手"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, a side cover, a welding gun and a paper clip.",
 "专业人员操作，拆侧盖，开焊枪。", "小结", ["专业人员", "拆侧盖", "开焊枪", "回形针"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "线不急弯，按记号紧线卡，弹簧到位。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手，焊枪挂在挂架上",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye beside the machine with its gun hung on the holder.",
 "通讯线换好了，下次见！"),
]
