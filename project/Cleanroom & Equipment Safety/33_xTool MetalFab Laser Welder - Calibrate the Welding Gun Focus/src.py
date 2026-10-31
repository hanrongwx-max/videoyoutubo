# 33_xTool MetalFab Laser Welder - Calibrate the Welding Gun Focus 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：校准焊枪焦距刻度，无旁白无字幕，三个镜头），K1–K3，不加补充知识点、不做更正；
# 保留原片三步顺序（系统设置查焦距刻度参考值、关闭电源、开卡扣推拉刻度管对准参考值），判断标准按本剧集第 26 集同段旁白；
# 原片只有 14 秒，剧本按原片三步放慢分解到 2 分钟，不添加原片没有的要求；屏幕上的序列号等识别信息和品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：校准焊枪焦点",
    "edition": "原著版",
    "points": {
        "K1": "在系统设置里查参考值",
        "K2": "调整前关闭电源",
        "K3": "开卡扣，推拉刻度管到参考值",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着焊枪，指着枪管上的一圈刻度",
 "The panda mascot holds a handheld laser welding gun and points at the graduated scale on its barrel.",
 "这一课讲焊枪焦距怎样校准。", "激光焊机：校准焊枪焦点"),
("开场", "三个步骤图标：设置屏幕、电源开关、刻度管",
 "Three icons in a row: a settings screen, a power switch turned off and a graduated tube. No people.",
 "一共三步：查、关、调。", "", ["查参考值", "关电源", "调刻度管"]),
# 情景
("情景", "阿杰拿着焊枪，看着枪管上的刻度",
 "The young male student holds the welding gun and looks at the graduated scale on its barrel.",
 "阿杰注意到焊枪上有一圈刻度。"),
("情景", "阿杰挠头，看看屏幕又看看焊枪",
 "He scratches his head, looking from the touch screen to the gun and back.",
 "这刻度该放在哪儿呢？"),
("情景", "老李走过来，指了指触摸屏",
 "The facility engineer walks over and points at the touch screen.",
 "老李说：要和屏幕上的参考值对上。"),
("情景", "触摸屏和焊枪刻度管之间画着一个问号",
 "A question mark floats between the touch screen of the main unit and the graduated tube of the welding gun. No people.",
 "参考值在哪儿看？怎么调？"),
("情景", "欣欣在空白白板前竖起一根手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看怎么校准。"),
# K1
("K1", "主机触摸屏亮着，显示空白主界面",
 "The touch screen of the main unit is on, showing a blank home page. No people.",
 "第一步，在主机屏幕上查参考值。", "在系统设置里查参考值"),
("K1", "老李在触摸屏上点开系统设置",
 "The facility engineer taps the system settings item on the touch screen of the main unit.",
 "点开系统设置，"),
("K1", "机器信息列表，最后一行被放大圈出",
 "A blank machine information list on the screen, with its last line magnified by a circle. No people.",
 "机器信息的最后一行，"),
("K1", "放大的最后一行，只有一个空白数值框",
 "The magnified last line shows a single blank value box. No people.",
 "就是焦距刻度参考值。"),
# K2
("K2", "老李走到主机背面",
 "The facility engineer walks around to the back of the main unit.",
 "第二步，关闭设备电源。", "调整前关闭电源"),
("K2", "老李按下背面电源开关到关闭",
 "The facility engineer presses the rocker switch on the back of the main unit to off.",
 "按下背面的电源开关。"),
# K3
("K3", "老李手持焊枪，刻度管特写",
 "The facility engineer holds the welding gun in his hand; close view of its graduated tube.",
 "第三步，看焊枪上的刻度管。", "开卡扣，推拉刻度管到参考值"),
("K3", "焊枪刻度管与参考值对照，数字一致打勾",
 "Close view of the gun's graduated tube beside a note card; matching marks with a green check. No people.",
 "刻度和参考值一致，就不用调。"),
("K3", "老李打开刻度管上的卡扣",
 "The facility engineer opens the clamp on the graduated tube of the welding gun.",
 "不一致，就打开卡扣，"),
("K3", "刻度管上的卡扣打开的特写",
 "Close view of the opened clamp on the graduated tube of the welding gun. No people.",
 "卡扣打开，刻度管就能动了。"),
("K3", "老李推拉刻度管",
 "The facility engineer slides the graduated tube in and out.",
 "推拉刻度管，"),
("K3", "刻度管上的刻度对准参考标记",
 "Close view: the mark on the graduated tube lines up with the reference mark. No people.",
 "直到刻度和参考值一致。"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands with icons behind: a settings screen, a power switch off and a graduated tube.",
 "系统设置里，查焦距刻度参考值。", "小结", ["查参考值", "关电源", "调刻度管"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "调整之前，先关电源。"),
("小结", "欣欣指着焊枪的刻度管",
 "The panda mascot points at the graduated tube on the welding gun.",
 "一致不用调，不一致就推拉对准。"),
("小结", "阿杰拿着焊枪，刻度与参考值一致，他点头",
 "The young male student holds the welding gun with its scale matching the reference and nods.",
 "阿杰学会了校准焦距。"),
# 结尾
("结尾", "欣欣、老李和阿杰挥手告别",
 "The panda mascot, the facility engineer and the young male student wave goodbye at the camera.",
 "焦距校准好了，下次见！"),
]
