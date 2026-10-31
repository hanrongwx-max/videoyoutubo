# 18_Replace the Pneumatic Assembly for xTool MetalFab Laser Welder 卡通剧本作者源
# 原片为激光焊接设备厂家的售后维修教程（无旁白，只有字幕）：更换带把手机型的气动组件（与第 10 集同部件、不同机型）。
# 保留全部操作知识点 K1–K23，设备统称“手持式激光焊接机”；
# 审查补充 S1–S5（气源要干燥洁净、气管插接要到位、压缩空气不对人吹、先通气后出光、保护气按说明书选用）；
# 关气泄压、两人放倒、光纤防弯折、检漏已在第 10 集补充，不重复
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "带把手机型气动组件的规范更换",
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
        "S1": "气源要干燥洁净",
        "S2": "气管插接要到位",
        "S3": "压缩空气不对人吹",
        "S4": "先通气，后出光",
        "S5": "保护气按说明书选用",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台带前后把手的激光焊接机旁，机旁有一个小型空压机和过滤器，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine with front and back handles, next to a small air compressor with a filter, and waves at the camera.",
 "这一课，换另一款焊机的气动组件。", "带把手机型气动组件的规范更换"),
("开场", "四个图标：水滴打叉的过滤器、气管接头、人脸前的气流打叉、气流箭头再激光",
 "Four icons in a row: a filter with a crossed-out water drop, a push-fit tube connector, an air jet aimed at a face crossed out, and an air arrow followed by a laser beam. No people.",
 "气要干净，管要插牢，用气有规矩。", "", ["气源干净", "插接到位", "不对人吹", "先气后光"]),
# 情景
("情景", "阿杰焊出的焊缝发黑、有气孔，焊枪喷出一点水雾",
 "The young male student looks at a dark porous weld seam while a little water mist sputters from the welding gun nozzle.",
 "阿杰发现焊缝发黑，焊枪还喷出水雾。"),
("情景", "老李打开空压机下方的过滤器，里面积着一层水",
 "The facility engineer opens the filter bowl under the air compressor and shows a layer of water collected inside.",
 "老李一查：气源进了水，电磁阀也坏了。"),
("情景", "老李拿出新的气动组件，小研站在一旁记录",
 "The facility engineer takes out a new air valve assembly while the female graduate student takes notes beside him.",
 "先换组件，再把气源管起来。"),
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
 "断电后仍有残余高压，按说明书等待。", "断电后仍有残余高压"),
# K4
("K4", "老李戴上厚绝缘手套",
 "The facility engineer pulls on thick insulated gloves.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "工作台上摆着两把十字螺丝刀、一把内六角扳手和一个带蓝色气管的新气动组件",
 "On a workbench lie two cross-head screwdrivers, a hex key and a new air valve assembly with a solenoid, a small sensor and blue tubes. No people.",
 "两把十字刀、内六角和新气动组件。", "准备工具和备件", ["十字刀", "内六角", "新组件"]),
# K6
("K6", "老李关机，拔下背面所有线缆和气管",
 "The facility engineer switches off the machine and unplugs all cables and the air supply hose from the back.",
 "关机，拔掉所有线缆。", "关机，拔掉所有线缆"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "老李用内六角松开前后把手的螺钉",
 "The facility engineer loosens the screws of the front and back handles with a hex key.",
 "松开前后把手八颗螺钉。", "松开把手螺钉"),
# K9
("K9", "老李拆右侧盖螺钉，从挂架取下焊枪，线缆在台面盘成大圈",
 "The facility engineer removes the right cover screws, lifts the welding gun off its holder and lays the cable in wide loops on the bench.",
 "取下焊枪，线缆盘大圈不急弯。", "取下焊枪，线缆不急弯"),
# K10
("K10", "老李拆下挂架和线缆夹的螺钉",
 "The facility engineer removes the screws of the gun holder and the cable clamp.",
 "拆挂架三颗、线缆夹两颗螺钉。", "拆挂架线缆夹，抬下右侧盖"),
("K10", "右侧盖向上抬起取下，露出黄色光纤",
 "The right cover is lifted upward and off, revealing a yellow fiber cable looped inside.",
 "把右侧盖向上抬下来。"),
# K11
("K11", "台面上铺泡沫，两人把机器侧放上去",
 "A foam pad is placed on the bench and two people lay the machine on its side on top of it.",
 "机器侧放，左侧下面垫泡沫。", "侧放机器，垫好泡沫"),
# K12
("K12", "老李拆下机器底部的两颗螺钉",
 "The facility engineer removes two screws from the bottom of the machine.",
 "拆下底部两颗螺钉。", "拆底部两颗螺钉"),
# K13
("K13", "细十字刀松开固定黄色光纤的小夹子",
 "A fine cross-head screwdriver loosens the two screws of a small clamp holding the yellow fiber.",
 "松开光纤夹的两颗螺钉。", "松开光纤夹"),
# K14
("K14", "手指按下快插接头的释放环，拔出气管",
 "Fingers press the release ring of a push-fit air fitting and pull the tube out.",
 "按下释放环，拔出两根气管。", "按释放环拔气管，扶正"),
("K14", "两人小心把机器扶正",
 "Two people carefully stand the machine upright again.",
 "再小心把机器扶正。"),
# K15
("K15", "机内黄色光纤顺着原来的大弧度盘着",
 "Inside the machine, the yellow fiber stays in its original wide curve. No people.",
 "黄色光纤别弯折，保持原来的弧度。", "黄色光纤保持原弧度"),
# K16
("K16", "老李拆左侧盖螺钉，从主板拔下两根线",
 "The facility engineer removes the left cover screw and unplugs two cables from the main board.",
 "拔下传感器线和电磁阀线。", "拔下传感器和电磁阀线"),
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
# S2
("S2", "气管管口切平、无划痕，插到底的示意",
 "A diagram: a tube end cut square without scratches, pushed fully into a fitting up to a marked line. No people.",
 "插管前看管口：切平、无划痕。", "气管插接要到位"),
("S2", "管口斜切、只插一半两个图标被打叉",
 "Two icons crossed out with red X marks: a tube end cut at a slant and a tube inserted only halfway. No people.",
 "插到底再轻拉一下，拉不出才算好。"),
# K21
("K21", "机器再次侧放在泡沫上，装回底部两颗螺钉",
 "The machine is laid on the foam again and the two bottom screws are refitted.",
 "侧放装回底部两颗螺钉。", "侧放装回底部螺钉"),
# K22
("K22", "右侧盖装回，线缆夹、挂架拧紧，焊枪挂回",
 "The right cover is refitted, the cable clamp and gun holder are screwed in place, and the welding gun is hung back.",
 "装右侧盖、线缆夹和挂架。", "装右侧盖，焊枪归位"),
("K22", "侧盖螺钉装回",
 "The screw on the right cover is refitted.",
 "焊枪归位，装好侧盖螺钉。"),
# K23
("K23", "把手装回，内六角拧紧",
 "The front and back handles are refitted and tightened with a hex key.",
 "装回前后把手。", "装回把手"),
# S1
("S1", "空压机后接着干燥器和过滤器，箭头表示气流",
 "An air compressor connected to an air dryer and a filter, with arrows showing the airflow to the welding machine. No people.",
 "压缩空气要经过干燥和过滤。", "气源要干燥洁净"),
("S1", "小研按下过滤器底部阀门，排出积水",
 "The female graduate student presses the drain valve at the bottom of the filter bowl and water drips out.",
 "过滤器的积水，按规定定期排掉。"),
("S1", "带油带水的气流进入焊枪、镜片起雾的图标被打叉",
 "An icon of oily, wet air flowing into a welding gun and fogging its lens, crossed out with a red X. No people.",
 "含油含水，会污染镜片、卡住阀门。"),
# S3
("S3", "气枪对着人脸和衣服吹的图标被打叉",
 "An icon of an air blow gun aimed at a person's face and clothes, crossed out with a red X. No people.",
 "压缩空气不对人吹，不吹身上的灰。", "压缩空气不对人吹"),
("S3", "气流冲进皮肤、眼睛的示意图",
 "A simple diagram of a sharp air jet hitting skin and an eye with warning marks. No people.",
 "高速气流会伤眼睛、钻进皮肤。"),
# S4
("S4", "开机顺序：打开气源，看空白压力表，再开机出光",
 "A three-step diagram joined by arrows: opening the air supply valve, checking a blank pressure gauge, then switching on the laser. No people.",
 "先开气、看气压，再开机出光。", "先通气，后出光", ["开气源", "看气压", "再出光"]),
("S4", "没有保护气就出光、焊点冒火星的图标被打叉",
 "An icon of a laser firing without shielding gas and a weld spot throwing sparks, crossed out with a red X. No people.",
 "没气就焊，焊不好还容易伤镜片。"),
# S5
("S5", "老李翻开空白说明书，对照几种不同颜色的气瓶图标",
 "The facility engineer opens a blank manual and compares several gas cylinder icons of different colors.",
 "保护气用哪种，看说明书和材料。", "保护气按说明书选用"),
("S5", "两个不同气瓶接在同一根管上的图标被打叉",
 "An icon of two different gas cylinders connected to the same hose, crossed out with a red X. No people.",
 "不随意换气、不混接。"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a clean filter, a push-fit connector, a crossed-out air jet and an air-then-laser arrow.",
 "气源干又净，气管插到底。", "小结", ["气源干净", "插接到位", "不对人吹", "先气后光"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "不对人吹，先气后光，气种照说明书。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在焊机前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye in front of the laser welding machine.",
 "气顺了，焊缝才亮。下次见！"),
]
