# 33_xTool MetalFab Laser Welder - Calibrate the Welding Gun Focus 卡通剧本作者源
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字
# 原片为 14 秒无声片段（第 26 集“校准焦距”）；设备统称“手持式激光焊接机”，品牌、序列号、参数值不出现
# 补充 S 点避开本剧集 01–32 已用的

META = {
    "title": "激光焊接机焊枪焦距的校准",
    "points": {
        "K1": "在系统设置里查参考值",
        "K2": "调整前关闭电源",
        "K3": "开卡扣，推拉刻度管到参考值",
        "S1": "焦点不准，风险变大",
        "S2": "卡扣锁紧再使用",
        "S3": "焊枪摔碰后，先查再用",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣举着焊枪，指着枪管上的一圈刻度",
 "The panda mascot holds a handheld laser welding gun and points at the graduated scale on its barrel.",
 "这一课讲焊枪焦距怎样校准。", "激光焊接机焊枪焦距的校准"),
# 情景
("情景", "焊枪从台面边缘掉到地上",
 "A welding gun slips off the edge of the bench and falls onto the floor.",
 "阿杰不小心，把焊枪碰到了地上。"),
("情景", "阿杰捡起焊枪，看看没坏，就想接着焊",
 "The young male student picks up the welding gun, glances at it and is about to start welding again.",
 "他看看外表没坏，就想接着用。"),
("情景", "老李伸手接过焊枪，摇摇头",
 "The facility engineer takes the welding gun from him and shakes his head.",
 "老李说：摔过的焊枪，要先检查。"),
# S3
("S3", "焊枪剖面示意：里面的镜片和光路",
 "Cutaway diagram of the welding gun showing lenses and the dashed beam path inside. No people.",
 "焊枪里有镜片和光路，", "焊枪摔碰后，先查再用"),
("S3", "镜片出现裂纹、光路歪斜的图标",
 "Icons of a cracked lens and a tilted beam path inside a gun outline. No people.",
 "摔一下，镜片可能裂，焦点可能偏。"),
("S3", "老李检查焊枪外壳和镜片，在本子上记录",
 "The facility engineer inspects the gun housing and lens holder, then writes in a blank logbook.",
 "检查外壳镜片，校准焦距，记录报告。"),
# S1
("S1", "焦点准时光斑小而集中，焦点偏时光斑散开",
 "Diagram: a focused beam makes a small tight spot; an off-focus beam spreads into a wider blurred spot. No people.",
 "焦点不准，光斑就会散开。", "焦点不准，风险变大"),
("S1", "熔不透、飞溅、散射三个图标",
 "Three icons: an unmelted weld, scattered spatter dots and scattered beam arrows. No people.",
 "焊不透、飞溅多，散射反射也会增加。"),
# K1
("K1", "老李在触摸屏上点开系统设置",
 "The facility engineer taps the system settings item on the touch screen of the main unit.",
 "先在屏幕的系统设置里，", "在系统设置里查参考值"),
("K1", "信息列表最后一行被放大圈出",
 "A blank information list on the screen, with its last line magnified by a circle. No people.",
 "找到焦距刻度参考值。"),
("K1", "老李把参考值抄在小本子上",
 "The facility engineer copies the value into a small blank notebook.",
 "把它记下来。"),
# K2
("K2", "老李按下背面电源开关到关闭",
 "The facility engineer presses the rocker switch on the back of the main unit to off.",
 "调整之前，关闭设备电源。", "调整前关闭电源"),
("K2", "屏幕熄灭，旁边打勾",
 "The touch screen goes dark, with a green check mark. No people.",
 "确认屏幕熄灭。"),
# K3
("K3", "焊枪刻度管与参考值对照，数字一致打勾",
 "Close view of the gun's graduated tube beside a note card; matching marks with a green check. No people.",
 "刻度管和参考值一致，就不用调。", "开卡扣，推拉刻度管到参考值"),
("K3", "老李打开刻度管上的卡扣",
 "The facility engineer opens the clamp on the graduated tube of the welding gun.",
 "不一致，就打开卡扣，"),
("K3", "老李推拉刻度管，对准参考刻度",
 "The facility engineer slides the graduated tube in or out until the mark matches the reference.",
 "推拉刻度管，对准参考值。"),
# S2
("S2", "老李合上卡扣，用力确认不松动",
 "The facility engineer closes the clamp and gently tugs the tube to confirm it does not move.",
 "调好后，卡扣一定要合紧。", "卡扣锁紧再使用"),
("S2", "使用中刻度管悄悄滑动的图标，被红叉划掉",
 "Icon of the graduated tube slipping during use, crossed out with a red X. No people.",
 "不然用着用着，焦点就悄悄变了。"),
("S2", "老李开机后看定位红光，再戴面罩试焊",
 "The facility engineer switches the machine on, checks the red aiming dot, then test-welds wearing a face shield.",
 "开机先看红光，再按规程试焊。"),
("S2", "欣欣指着封面有激光标志的空白小册子",
 "The panda mascot points at a blank booklet with a laser warning pictogram on the cover.",
 "激光防护以现行国家标准为准。"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands with icons behind: a settings screen, a power switch off, a graduated tube and a locked clamp.",
 "查参考值，先关机，对刻度，锁卡扣。", "", ["查参考值", "先关机", "对刻度", "锁卡扣"]),
("小结", "阿杰向老李点头，把焊枪挂回支架",
 "The young male student nods to the facility engineer and hangs the welding gun back on its holder.",
 "阿杰记住了：摔过的焊枪先检查。"),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye at the camera.",
 "焦点对准，焊得安全。下次见！"),
]
