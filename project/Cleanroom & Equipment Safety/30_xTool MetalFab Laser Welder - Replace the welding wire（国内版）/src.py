# 30_xTool MetalFab Laser Welder - Replace the welding wire 卡通剧本作者源
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字
# 原片为厂家教程片段（第 26 集“更换焊丝”）；设备统称“手持式激光焊接机”“送丝机”，品牌与规格数值不出现
# 补充 S 点避开本剧集 01–29 已用的

META = {
    "title": "激光焊接机更换焊丝",
    "points": {
        "K1": "换成更粗的焊丝",
        "K2": "开门，拧盖取套筒",
        "K3": "打开两个压紧器",
        "K4": "倒转焊丝盘，退出焊丝",
        "K5": "丝头弯折插进盘孔",
        "K6": "拆下当前送丝轮",
        "K7": "取出上方备用送丝轮",
        "K8": "核对送丝轮尺寸",
        "K9": "装新送丝轮，旧轮存好",
        "K10": "换对应规格的导嘴",
        "K11": "装新焊丝盘、套筒和盖子",
        "K12": "引出丝头，剪掉弯头",
        "K13": "穿丝，轻压穿过",
        "K14": "合压紧器，按表调压力",
        "K15": "按送丝键送到导嘴",
        "S1": "先看焊丝的安全数据单",
        "S2": "焊丝干燥存放，标签清楚",
        "S3": "换丝径后屏幕参数同步改",
        "S4": "空盘废丝分类回收",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣抱着一卷焊丝，站在打开的送丝机旁",
 "The panda mascot holds a wire spool and stands beside an open blank wire feeder box.",
 "这一课讲：怎样换成另一种直径的焊丝。", "激光焊接机更换焊丝"),
# 情景
("情景", "阿杰从柜子里翻出一卷没有标签、有点生锈的焊丝",
 "The young male student pulls a rusty wire spool with no label out of a cluttered cabinet.",
 "阿杰找来一卷焊丝，标签掉了，还有点锈。"),
("情景", "阿杰拿着焊丝就往送丝机上装",
 "The young male student is about to mount the unlabeled spool onto the wire feeder.",
 "他也不知道是什么材质，就想装上。"),
("情景", "小研拦住他，拿出一卷包装完好的新焊丝",
 "The female graduate student stops him and holds up a new, sealed wire spool with a blank label.",
 "小研说：先弄清楚焊丝，再动手换。"),
# S1
("S1", "欣欣举起一份空白的安全数据单",
 "The panda mascot holds up a blank safety data sheet with a few pictogram boxes.",
 "每种焊丝都有安全数据单。", "先看焊丝的安全数据单"),
("S1", "焊丝冒出的烟里，浮现几个不同的元素小方块",
 "Fumes rising from a weld seam contain a few small blank element squares. No people.",
 "材质不同，焊接烟尘的成分也不同。"),
("S1", "小研对照数据单，打开排风、拿出呼吸防护",
 "The female graduate student reads the blank data sheet, switches on the fume extractor and takes out a respirator.",
 "按数据单的要求配好排风和防护。"),
# S2
("S2", "干燥柜里整齐码放着带标签的焊丝盘",
 "A dry storage cabinet with neatly stacked wire spools, each in its original packaging with a blank label. No people.",
 "焊丝放在干燥处，原包装保存。", "焊丝干燥存放，标签清楚"),
("S2", "生锈、没标签的焊丝盘被红叉划掉",
 "A rusty wire spool with no label is crossed out with a red X. No people.",
 "受潮生锈、标签不清的，不要用。"),
# K1
("K1", "一细一粗两卷焊丝，中间一个箭头",
 "Two wire spools, one thinner and one thicker, with an arrow from the first to the second. No people.",
 "这次把细焊丝换成粗一号的。", "换成更粗的焊丝"),
# K2
("K2", "老李打开送丝机门，拧下盖子取下套筒",
 "The facility engineer opens the wire feeder door, unscrews the cap and slides off the sleeve.",
 "打开送丝机门，拧下盖子，取下套筒。", "开门，拧盖取套筒"),
# K3
("K3", "老李扳开两个红色压紧器",
 "The facility engineer flips open the two red tensioners on the drive unit.",
 "打开两个压紧器。", "打开两个压紧器"),
# K4
("K4", "老李顺时针转动焊丝盘，焊丝从送丝驱动里退出来",
 "The facility engineer turns the spool clockwise and the wire slides back out of the drive unit.",
 "顺时针转焊丝盘，把丝从驱动里退出来。", "倒转焊丝盘，退出焊丝"),
("K4", "老李把焊丝盘从转轴上取下",
 "The facility engineer lifts the old spool off the spindle.",
 "取下旧焊丝盘。"),
# K5
("K5", "焊丝端头弯折，插进盘边的小孔",
 "Close view: the wire end is bent and tucked into a small hole on the rim of the spool. No people.",
 "丝头弯一下，插进盘边小孔，不会散开。", "丝头弯折插进盘孔"),
# K6
("K6", "老李拧下螺丝，取下送丝轮",
 "The facility engineer removes the screws and takes the drive rollers off the drive unit.",
 "拆下螺丝，取下现在的送丝轮。", "拆下当前送丝轮"),
# K7
("K7", "老李从上方存放位取出另一对送丝轮",
 "The facility engineer unscrews the storage pegs above and takes out the spare pair of rollers.",
 "从上方存放位取出另一对送丝轮。", "取出上方备用送丝轮"),
# K8
("K8", "送丝轮外侧刻印被放大，旁边是新焊丝盘",
 "A magnified view of the blank size mark on the outer side of a drive roller, next to the new wire spool. No people.",
 "核对：送丝轮外侧的尺寸和新焊丝一致。", "核对送丝轮尺寸"),
# K9
("K9", "老李装上新送丝轮，拧回螺丝",
 "The facility engineer fits the matching rollers and refastens the screws.",
 "装上新的一对，拧回螺丝。", "装新送丝轮，旧轮存好"),
("K9", "换下的送丝轮放回上方存放位",
 "The removed pair of rollers is stored on the pegs above the drive unit. No people.",
 "换下的那对，存到上方。"),
# K10
("K10", "老李拧下送丝管末端的导嘴，换上另一规格",
 "The facility engineer unscrews the nozzle at the end of the feeding tube and fits a nozzle of the other size.",
 "送丝导嘴也换成对应规格的。", "换对应规格的导嘴"),
# K11
("K11", "老李把新焊丝盘套上转轴，装回套筒和盖子",
 "The facility engineer slides the new spool onto the spindle, then refits the sleeve and screws on the cap.",
 "装新焊丝盘，装回套筒，拧好盖子。", "装新焊丝盘、套筒和盖子"),
# K12
("K12", "老李捏住丝头，用钳子剪掉弯头",
 "Wearing safety goggles, the facility engineer pinches the wire end and snips off the bent tip with pliers.",
 "捏住丝头引出来，剪掉弯曲的一段。", "引出丝头，剪掉弯头"),
# K13
("K13", "老李把焊丝穿进送丝驱动",
 "The facility engineer threads the wire into the drive unit.",
 "焊丝穿进送丝驱动，", "穿丝，轻压穿过"),
("K13", "手指轻压焊丝，穿过送丝轮",
 "A finger lightly presses the wire so it passes between the rollers into the tube. No people.",
 "轻轻压一下，让它穿过送丝轮。"),
# K14
("K14", "老李合上压紧器，转动旋钮",
 "The facility engineer closes the tensioners and turns their knobs.",
 "合上压紧器，转旋钮调压力。", "合压紧器，按表调压力"),
("K14", "一张空白表格",
 "A blank adjustment table made of empty rows and columns with dots. No people.",
 "换了丝径，压力也按表格重新调。"),
# K15
("K15", "老李按住送丝键，焊丝从导嘴伸出",
 "The facility engineer holds the feed button and the new wire comes out of the brass nozzle.",
 "按住送丝键，送到丝从导嘴伸出。", "按送丝键送到导嘴"),
# S3
("S3", "屏幕上焊丝直径选项框被放大",
 "The touch screen with the wire diameter option box magnified by a circle. No people.",
 "换了焊丝，屏幕上的丝径也要改。", "换丝径后屏幕参数同步改"),
("S3", "参数不对，焊缝没熔透、光散射出去的示意图",
 "Diagram: with wrong settings the metal does not melt through and the beam scatters outward. No people.",
 "参数不匹配，可能熔不透，激光散射。"),
("S3", "老李选好丝径，先在废料上试焊",
 "The facility engineer selects the new wire size on the screen, then test-welds on a scrap piece while wearing a face shield.",
 "改好参数，先在废料上试一下。"),
# S4
("S4", "空焊丝盘和剪下的废丝，分别放进两个回收箱",
 "An empty plastic spool and snipped wire scraps go into two separate recycling boxes. No people.",
 "空焊丝盘和废丝，分开回收。", "空盘废丝分类回收"),
("S4", "地上散落的废丝被红叉划掉",
 "Scattered wire scraps on the floor crossed out with a red X. No people.",
 "废丝不留在地上和台面上。"),
# 小结
("小结", "欣欣身后浮现几个步骤图标",
 "The panda mascot stands beside the wire feeder with icons behind: a spool out, rollers, a nozzle, a spool in.",
 "退旧丝，换轮换嘴，装新丝，送到位。", "", ["退旧丝", "换轮换嘴", "装新丝", "送到位"]),
("小结", "图标：数据单、干燥柜、屏幕、回收箱",
 "Icons in a row: a safety data sheet, a dry cabinet, a touch screen and a recycling box. No people.",
 "看数据单，存得干，改参数，分类收。", "", ["看数据单", "干燥存放", "改参数", "分类回收"]),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye at the camera.",
 "焊丝换得对，焊缝才可靠。下次见！"),
]
