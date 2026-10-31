# 30_xTool MetalFab Laser Welder - Replace the welding wire 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：更换不同直径的焊丝，画外音讲解），K1–K15，不加补充知识点、不做更正；
# 保留原片示例和规格（1 mm 换 1.2 mm 焊丝、0.8/1.0 导嘴换成随附的 1.2/1.6 导嘴、按表调压力）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊接机更换焊丝",
    "edition": "原著版",
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
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣抱着一卷焊丝，站在打开的送丝机旁",
 "The panda mascot holds a wire spool and stands beside an open blank wire feeder box.",
 "这一课讲：怎样换成另一种直径的焊丝。", "激光焊接机更换焊丝"),
# 情景
("情景", "阿杰拿着一卷较粗的新焊丝走到送丝机旁",
 "The young male student walks to the wire feeder holding a new, thicker wire spool.",
 "阿杰要换一卷更粗的焊丝。"),
("情景", "送丝机里装着一卷细焊丝",
 "Inside the open wire feeder sits a spool of thinner wire. No people.",
 "可送丝机里还装着细的那卷。"),
("情景", "老李走过来，打开送丝机门",
 "The facility engineer comes over and opens the wire feeder door.",
 "老李说：换丝径，轮和嘴都要换。"),
# K1
("K1", "一细一粗两卷焊丝，中间一个箭头",
 "Two wire spools, one thinner and one thicker, with an arrow from the first to the second. No people.",
 "以1毫米换1.2毫米焊丝为例。", "换成更粗的焊丝", ["1mm→1.2mm"]),
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
 "核对：送丝轮外侧的尺寸和新焊丝一致。", "核对送丝轮尺寸", ["1.2"]),
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
 "0.8/1.0导嘴换成随附的1.2/1.6。", "换对应规格的导嘴", ["0.8/1.0→1.2/1.6"]),
# K11
("K11", "老李把新焊丝盘套上转轴，装回套筒和盖子",
 "The facility engineer slides the new spool onto the spindle, then refits the sleeve and screws on the cap.",
 "装新焊丝盘，装回套筒，拧好盖子。", "装新焊丝盘、套筒和盖子"),
# K12
("K12", "老李捏住丝头，用钳子剪掉弯头",
 "The facility engineer pinches the wire end and snips off the bent tip with pliers.",
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
 "压力按表格来调。"),
# K15
("K15", "老李按住送丝键，焊丝从导嘴伸出",
 "The facility engineer holds the feed button and the new wire comes out of the brass nozzle.",
 "按住送丝键，送到丝从导嘴伸出。", "按送丝键送到导嘴"),
# 小结
("小结", "欣欣身后浮现几个步骤图标",
 "The panda mascot stands beside the wire feeder with icons behind: a spool out, rollers, a nozzle, a spool in.",
 "退旧丝，换轮换嘴，装新丝，送到位。", "小结", ["退旧丝", "换轮换嘴", "装新丝", "送到位"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "丝头插盘孔，轮的尺寸对丝径。"),
# 结尾
("结尾", "欣欣、老李和阿杰在送丝机旁挥手",
 "The panda mascot, the facility engineer and the young male student wave goodbye beside the wire feeder.",
 "焊丝换好了，下次见！"),
]
