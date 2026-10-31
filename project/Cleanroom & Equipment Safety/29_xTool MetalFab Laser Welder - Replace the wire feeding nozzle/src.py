# 29_xTool MetalFab Laser Welder - Replace the wire feeding nozzle 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：按焊丝直径更换送丝导嘴，两句旁白加字幕），K1–K3，不加补充知识点、不做更正；
# 保留原片的规格对照（0.8/1.0 导嘴配 0.8、1.0 mm 焊丝，1.2/1.6 导嘴配 1.2、1.6 mm 焊丝）；
# 原片只有 20 秒，剧本按原片内容放慢分解到 2 分钟，不添加原片没有的要求；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换送丝嘴",
    "edition": "原著版",
    "points": {
        "K1": "送丝管卡扣端装可换导嘴",
        "K2": "导嘴分两种规格",
        "K3": "按焊丝直径换导嘴",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一个小小的铜色导嘴，向镜头招手",
 "The panda mascot holds up a tiny knurled brass wire feeding nozzle and waves at the camera.",
 "这一课讲送丝导嘴怎样更换。", "激光焊接机更换送丝导嘴"),
("开场", "送丝机、送丝管、焊枪连成一线的示意图",
 "Diagram: a wire feeder, a long wire feeding tube and a handheld welding gun joined in a line. No people.",
 "导嘴装在送丝管的末端。"),
# 情景
("情景", "阿杰换上了一卷粗焊丝",
 "The young male student mounts a thicker wire spool in the wire feeder.",
 "阿杰把焊丝换成了1.2毫米的。"),
("情景", "焊丝卡在送丝管末端的小导嘴前",
 "The wire jams at the small brass nozzle at the end of the feeding tube. No people.",
 "可送丝时，焊丝卡在导嘴前。"),
("情景", "小研拿起送丝管末端看了看，摇摇头",
 "The female graduate student picks up the nozzle end of the feeding tube, looks at it and shakes her head.",
 "小研一看：导嘴还是细丝用的。"),
("情景", "欣欣在空白白板前竖起一根手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们来看导嘴怎么换。"),
# K1
("K1", "送丝管两端：一端普通，一端带卡扣和铜导嘴",
 "A wire feeding tube laid out on the bench: one plain end, and one end with a clamp and a brass nozzle. No people.",
 "送丝管有一头带卡扣，", "送丝管卡扣端装可换导嘴"),
("K1", "卡扣端特写，铜导嘴被圆圈标出",
 "Close view of the clamp end of the tube with the brass nozzle marked by a green circle. No people.",
 "这一头装着送丝导嘴。"),
("K1", "铜导嘴特写，旁边一个旋转箭头",
 "Close view of the brass nozzle with a circular arrow showing it can be unscrewed. No people.",
 "导嘴可以拧下来更换。"),
# K2
("K2", "两个铜导嘴并排，一个孔小一个孔大",
 "Two brass nozzles side by side, one with a small hole and one with a larger hole, each with a blank tag. No people.",
 "导嘴有两种规格。", "导嘴分两种规格", ["0.8/1.0", "1.2/1.6"]),
("K2", "小孔导嘴放大，刻印处空白",
 "A magnified view of the small-hole nozzle with a blank engraved band. No people.",
 "一种是0.8/1.0的，", "", ["0.8/1.0"]),
("K2", "大孔导嘴放大，刻印处空白",
 "A magnified view of the large-hole nozzle with a blank engraved band. No people.",
 "另一种是1.2/1.6的。", "", ["1.2/1.6"]),
("K2", "小孔导嘴用线连着两卷细焊丝",
 "Lines link the small-hole nozzle to two thin wire spools. No people.",
 "0.8/1.0导嘴配0.8和1.0毫米焊丝。", "", ["0.8mm", "1.0mm"]),
("K2", "大孔导嘴用线连着两卷粗焊丝",
 "Lines link the large-hole nozzle to two thick wire spools. No people.",
 "1.2/1.6导嘴配1.2和1.6毫米焊丝。", "", ["1.2mm", "1.6mm"]),
# K3
("K3", "老李看焊丝盘上的空白标签",
 "The facility engineer checks the blank label on the wire spool.",
 "先看清焊丝的直径，", "按焊丝直径换导嘴"),
("K3", "老李在送丝机旁手持送丝管末端，拧下旧导嘴",
 "Standing beside the wire feeder, the facility engineer holds the end of the feeding tube and unscrews the old nozzle.",
 "拧下送丝管末端的旧导嘴，"),
("K3", "老李拧上另一种规格的导嘴",
 "The facility engineer screws the nozzle of the other size onto the tube end.",
 "换上和焊丝对应的导嘴。"),
("K3", "一张两行的对照表，左边导嘴图标，右边焊丝图标",
 "A two-row matching chart: nozzle icons on the left, wire spool icons on the right. No people.",
 "丝径和导嘴，照对照表来配。", "", ["0.8/1.0→0.8、1.0", "1.2/1.6→1.2、1.6"]),
("K3", "焊丝从新导嘴伸出，打勾",
 "The wire comes out of the new nozzle, with a green check mark. No people.",
 "导嘴和焊丝对上了。"),
# 小结
("小结", "欣欣身后浮现送丝管和两个导嘴图标",
 "The panda mascot stands with icons behind: a feeding tube with a clamp end and two nozzles.",
 "送丝管卡扣端，装着可换的导嘴。", "小结", ["卡扣端", "可换导嘴"]),
("小结", "两个导嘴各连两卷焊丝",
 "Two nozzles, each linked by lines to two wire spools. No people.",
 "两种规格，各配两种丝径。", "", ["0.8/1.0", "1.2/1.6"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "按焊丝直径，换对应的导嘴。"),
("小结", "阿杰的焊丝顺利送出，他竖起大拇指",
 "The wire now feeds smoothly through the new nozzle and the young male student gives a thumbs up.",
 "阿杰换对导嘴，送丝顺畅了。"),
# 结尾
("结尾", "欣欣、小研和阿杰挥手告别",
 "The panda mascot, the female graduate student and the young male student wave goodbye at the camera.",
 "导嘴换好了，下次见！"),
]
