# 29_xTool MetalFab Laser Welder - Replace the wire feeding nozzle 卡通剧本作者源
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字
# 原片为 20 秒的厂家教程片段（第 26 集“更换送丝导嘴”）；设备统称“手持式激光焊接机”，品牌与规格数值不出现
# 补充 S 点避开本剧集 01–28 已用的

META = {
    "title": "激光焊接机更换送丝导嘴",
    "points": {
        "K1": "送丝管卡扣端装可换导嘴",
        "K2": "导嘴分两种规格",
        "K3": "按焊丝直径换导嘴",
        "S1": "换前回抽焊丝，关送丝",
        "S2": "导嘴磨损要及时换",
        "S3": "导嘴装正，防光打铜嘴",
        "S4": "耗材领用要登记",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一个小小的铜色导嘴，向镜头招手",
 "The panda mascot holds up a tiny knurled brass wire feeding nozzle and waves at the camera.",
 "这一课讲送丝导嘴怎样更换。", "激光焊接机更换送丝导嘴"),
# 情景
("情景", "阿杰换了一卷粗焊丝，焊丝卡在导嘴里出不来",
 "The young male student has loaded a thicker wire spool, but the wire jams at the small brass nozzle.",
 "阿杰换了粗焊丝，送丝却老是卡住。"),
("情景", "小研拿起导嘴看了看，摇摇头",
 "The female graduate student picks up the nozzle end of the feeding tube, looks at it and shakes her head.",
 "小研一看：导嘴没跟着换。"),
# K1
("K1", "送丝管两端：一端普通，一端带卡扣和铜导嘴",
 "A wire feeding tube laid out on the bench: one plain end, and one end with a clamp and a brass nozzle. No people.",
 "送丝管带卡扣的这一头，", "送丝管卡扣端装可换导嘴"),
("K1", "铜导嘴特写，旁边一个旋转箭头",
 "Close view of the brass nozzle with a circular arrow showing it can be unscrewed. No people.",
 "装着一个可以拆换的导嘴。"),
# K2
("K2", "两个铜导嘴并排，一个孔小一个孔大",
 "Two brass nozzles side by side, one with a small hole and one with a larger hole, each with a blank tag. No people.",
 "导嘴有两种规格，孔径不一样。", "导嘴分两种规格", ["细丝导嘴", "粗丝导嘴"]),
("K2", "细导嘴连着两卷细焊丝，粗导嘴连着两卷粗焊丝",
 "Lines link the small-hole nozzle to two thin wire spools and the large-hole nozzle to two thick wire spools. No people.",
 "每种规格对应两种焊丝直径。"),
# S1
("S1", "老李按住回抽键，焊丝退回导嘴里",
 "The facility engineer presses the retract button and the wire tip withdraws into the nozzle.",
 "换导嘴之前，先把焊丝回抽进去，", "换前回抽焊丝，关送丝"),
("S1", "老李关掉焊枪上的送丝使能开关",
 "The facility engineer flips the wire feeding enable switch on the welding gun to off.",
 "再关掉送丝使能。"),
("S1", "换导嘴时焊丝突然送出扎到手的图标，被红叉划掉",
 "Icon of wire suddenly shooting out and poking a hand during a nozzle change, crossed out with a red X. No people.",
 "免得焊丝突然送出来扎手。"),
# K3
("K3", "老李看焊丝盘上的空白标签，再看导嘴",
 "The facility engineer checks the blank label on the wire spool, then looks at the nozzles.",
 "先看清焊丝的直径，", "按焊丝直径换导嘴"),
("K3", "老李拧下旧导嘴，拧上对应规格的导嘴",
 "The facility engineer unscrews the old nozzle from the tube end and screws on the matching one.",
 "拧下旧导嘴，换上对应规格的。"),
("K3", "欣欣指着空白说明书上的一张小表",
 "The panda mascot points at a small blank table in the manual.",
 "规格对应关系，查说明书的对照表。"),
("K3", "焊丝顺畅地从新导嘴伸出，打勾",
 "The wire comes out smoothly from the new nozzle, with a green check mark. No people.",
 "规格对了，送丝就顺畅。"),
# S2
("S2", "新导嘴的圆孔和磨损导嘴的椭圆孔对比",
 "Close-up comparison: a new nozzle with a round hole and a worn nozzle with an enlarged oval hole. No people.",
 "导嘴用久了，孔会被焊丝磨大。", "导嘴磨损要及时换"),
("S2", "焊丝在磨损的导嘴里晃动，偏离红点",
 "Diagram: the wire wobbles in a worn nozzle and drifts away from the red dot. No people.",
 "送丝会晃，丝也对不准光点。"),
("S2", "老李把磨损的导嘴放进废件盒，换新的",
 "The facility engineer drops the worn nozzle into a scrap parts box and takes out a new one.",
 "发现磨损变形，就及时换新。"),
# S3
("S3", "导嘴装歪，激光打在铜导嘴上反射出去的示意图",
 "Diagram: a crooked nozzle puts the wire off center, the beam hits the brass nozzle and reflects away. No people.",
 "导嘴装歪，光可能打到铜导嘴上。", "导嘴装正，防光打铜嘴"),
("S3", "铜表面像镜子一样反光的图标",
 "Icon of a shiny copper surface reflecting light like a mirror. No people.",
 "铜很反光，反射的激光同样伤人。"),
("S3", "老李把导嘴拧正拧紧，丝尖正对红点",
 "The facility engineer screws the nozzle straight and tight; the wire tip lines up with the red dot.",
 "导嘴拧正拧紧，丝尖对准红点。"),
("S3", "欣欣指着封面有激光标志的空白小册子",
 "The panda mascot points at a blank booklet with a laser warning pictogram on the cover.",
 "激光防护以现行国家标准为准。"),
# S4
("S4", "小研在空白耗材登记本上写字，旁边一盒导嘴",
 "The female graduate student writes in a blank consumables logbook beside a box of nozzles.",
 "导嘴、焊丝这些耗材，领用要登记。", "耗材领用要登记"),
("S4", "登记本旁浮现日期、数量、签名三个图标",
 "Beside the logbook float three icons: a calendar, a number counter and a signature line. No people.",
 "记下日期、数量和领用人。"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands with icons behind: a retract arrow, two nozzles, a worn hole and a straight nozzle with a red dot.",
 "先回抽，对规格，看磨损，装端正。", "", ["先回抽", "对规格", "看磨损", "装端正"]),
("小结", "阿杰的焊丝顺利送出，他竖起大拇指",
 "The wire now feeds smoothly through the new nozzle and the young male student gives a thumbs up.",
 "阿杰换对导嘴，送丝顺畅了。"),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye at the camera.",
 "小零件，大讲究。下次见！"),
]
