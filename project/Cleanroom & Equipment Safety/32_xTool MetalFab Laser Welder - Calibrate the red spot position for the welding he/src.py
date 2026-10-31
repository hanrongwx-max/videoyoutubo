# 32_xTool MetalFab Laser Welder - Calibrate the red spot position for the welding he 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：校准焊枪红点的左右 / 上下偏移，画外音讲解），K1–K6，不加补充知识点、不做更正；
# 保留原片步骤（管理员设置调左右偏移，仍不行归零后用内六角插孔一或孔二调上下）和画面（演示者手持焊枪调校）；
# 原片公开的管理员密码不转录；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：校准焊接头的红光定位点",
    "edition": "原著版",
    "points": {
        "K1": "红点偏离焊丝左右时校准",
        "K2": "进入管理员设置",
        "K3": "左右箭头调偏移，对准焊丝",
        "K4": "切割嘴光打内壁，先调左右",
        "K5": "仍不行：偏移归零再调上下",
        "K6": "内六角慢慢拧，红点清晰即停",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣指着焊嘴下方的一个小红点",
 "The panda mascot points at a small red dot on the work surface below a welding gun nozzle.",
 "这一课讲焊枪红色定位点的校准。", "激光焊机：校准焊接头的红光定位点"),
("开场", "两个图标：左右箭头、上下箭头",
 "Two icons side by side: a left-right arrow and an up-down arrow around a red dot. No people.",
 "分左右偏移和上下偏移两种。", "", ["左右偏移", "上下偏移"]),
# 情景
("情景", "阿杰对准焊缝，发现红点偏在焊丝一边",
 "The young male student aims the welding gun at a seam and notices the red dot falls to one side of the wire.",
 "阿杰发现，红点没落在焊丝上。"),
("情景", "阿杰换了几个角度，红点还是偏",
 "He tilts the gun at different angles, but the red dot is still off to the side.",
 "怎么摆焊枪，红点都偏在一边。"),
("情景", "老李走过来，看了看焊枪头",
 "The facility engineer walks over and looks closely at the welding gun head.",
 "老李说：这要校准红点位置。"),
("情景", "欣欣在空白白板前竖起一根手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "先调左右，再调上下。"),
# K1
("K1", "焊嘴下，红点偏在焊丝的一侧",
 "Close view: below the nozzle the red dot falls to one side of the welding wire tip. No people.",
 "喷嘴装好了，红点仍偏在焊丝左边或右边，", "红点偏离焊丝左右时校准"),
("K1", "原装焊接嘴特写，旁边打勾",
 "Close view of the original welding nozzle properly fitted, with a green check mark. No people.",
 "用的是原装焊接嘴，就做左右校准。"),
# K2
("K2", "老李在屏幕上依次点开设置菜单",
 "The facility engineer taps through blank menu items on the touch screen: settings, machine settings, administrator.",
 "在屏幕上进入系统设置、机器设置，", "进入管理员设置"),
("K2", "密码键盘，输入的数字显示为圆点",
 "A numeric keypad on the touch screen with the entered digits shown only as dots. No people.",
 "再进管理员设置，输入管理员密码。"),
# K3
("K3", "老李点红点偏移右边的开始按钮",
 "The facility engineer taps the start button next to the red dot offset item on the settings page.",
 "点红点偏移旁边的开始，", "左右箭头调偏移，对准焊丝"),
("K3", "分屏：点左箭头红点左移，点右箭头红点右移",
 "Split view: tapping a left arrow moves the red dot left, tapping a right arrow moves it right. No people.",
 "左箭头红点左移，右箭头红点右移。"),
("K3", "红点中心正好落在焊丝上，老李点完成",
 "The red dot center lands exactly on the wire; the facility engineer taps a completed button.",
 "红点中心落在焊丝上，点完成。"),
# K4
("K4", "切割嘴剖面：光束打在喷嘴内壁上",
 "Cutaway diagram of a narrow cutting nozzle: the beam strikes the inner wall instead of passing through the center. No people.",
 "用切割嘴时，光可能打到喷嘴内壁，", "切割嘴光打内壁，先调左右"),
("K4", "内壁处出现堵塞和反射的小图标",
 "Small icons of a blockage and a reflected arrow appear at the nozzle's inner wall. No people.",
 "造成堵塞或反射，先做左右校准。"),
# K5
("K5", "屏幕上偏移数值框归零",
 "The offset value box on the settings screen is reset to zero. No people.",
 "还是不行，就把红点偏移归零，", "仍不行：偏移归零再调上下"),
("K5", "焊接嘴和清洗嘴的大孔径特写，旁边打勾",
 "Close views of a welding nozzle and a cleaning nozzle with wide openings, with a green check mark. No people.",
 "再调上下；焊接嘴清洗嘴孔大，一般不用。"),
# K6
("K6", "老李手持焊枪，把小内六角插进焊枪上的调节孔",
 "Holding the welding gun in his hand, the facility engineer inserts a small hex key into an adjustment hole on the gun.",
 "内六角插进焊枪上的孔一或孔二，", "内六角慢慢拧，红点清晰即停", ["孔1", "孔2"]),
("K6", "分屏：一边慢慢拧，一边散乱的红光逐渐汇成一点",
 "Split view: a hex key turns slowly while a scattered red glow gradually gathers into one dot. No people.",
 "一边慢慢拧，一边看喷嘴射出的红光。"),
("K6", "一个清晰的圆形红点，老李停手",
 "A sharp round red dot appears on the bench and the facility engineer stops turning.",
 "出现清晰的红点，就停。"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands with icons behind: a settings gear, a left-right arrow, a nozzle and a hex key.",
 "红点偏左右，进管理员设置调偏移。", "小结", ["管理员设置", "左右偏移", "归零", "调上下"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "切割嘴还不行，归零后用内六角调上下。"),
("小结", "红点正好落在焊丝尖上",
 "Close view: the red dot sits exactly on the tip of the welding wire. No people.",
 "红点对准焊丝，清晰就好。"),
# 结尾
("结尾", "欣欣、老李和阿杰挥手告别",
 "The panda mascot, the facility engineer and the young male student wave goodbye at the camera.",
 "红点校准好了，下次见！"),
]
