# 12_Laser System Emergency Shut Down Innovative Laser Maintenance Laser Safety 卡通剧本作者源
# 原著版：完全照原片（1 分 12 秒：激光切割机的三种紧急停机——安全地垫、进给保持/急停、总隔离开关），K1–K9，不加补充知识点、不做更正；
# 保留原片说法：地垫一踩整台机器立即停；操作台和机器末端都有进给保持，只中断运动；急停驱动、高压全部断开；
# 事故时、新操作员不知所措就拉总闸，激光器、冷水机和全部辅助设备一起断电；“如果还得想一想，就拉闸”
# 原片没讲拉闸后的报告复位、装置定期测试和演练，本版也不加；讲解人姓名、公司名、网址和联系方式不出现，讲解人改为老李
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光设备的紧急停机",
    "edition": "原著版",
    "points": {
        "K1": "欢迎参观，更要照看",
        "K2": "人人都想凑近看",
        "K3": "安全地垫：一踩全停",
        "K4": "两种停机按钮",
        "K5": "进给保持：只停运动",
        "K6": "急停：驱动高压全断",
        "K7": "出了事拿不准，拉总闸",
        "K8": "总闸一拉，全部断电",
        "K9": "还要犹豫，就拉闸",
    },
    "avoid": ["Scott Kiser", "Kiser", "Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "LaserServiceGuy", "Laser Maintenance Group", "LMG"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光切割机旁，指着一个红色大按钮",
 "The panda mascot stands beside a laser cutting machine and points at a big red button.",
 "激光设备怎么紧急停机？", "激光设备的紧急停机"),
("开场", "地垫、按钮、闸刀开关三个图标",
 "Three icons in a row: a floor safety mat, a stop button and a wall knife switch. No people.",
 "三种办法：地垫、按钮、总闸。", "", ["安全地垫", "停机按钮", "总闸"]),
# 情景
("情景", "办公区门口，老李对着镜头讲话",
 "At an office door, the facility engineer talks to the camera.",
 "老李带客户参观激光车间。"),
("情景", "老李推门，带大家走向大型激光切割机",
 "The facility engineer opens the door and leads the visitors toward a large laser cutting machine.",
 "边走边讲紧急停机。"),
# K1
("K1", "访客们好奇地看着车间里正在工作的机器",
 "Visitors look curiously at the working machines in the workshop.",
 "客户来了，都想看看我们在做什么。", "欢迎参观，更要照看"),
("K1", "老李笑着张开手臂欢迎",
 "The facility engineer smiles and opens his arms in welcome.",
 "我们也乐意展示给他们看。"),
# K2
("K2", "几位访客弯腰凑到激光机前往里看",
 "Several visitors bend over and lean close to the front of the laser machine to look inside.",
 "走到激光机前，人人第一件事——", "人人都想凑近看"),
("K2", "访客的脸几乎贴到机器前面",
 "A visitor's face is almost pressed to the front of the machine.",
 "就是凑到跟前去看。"),
# K3
("K3", "激光机前铺着一条长长的黑色安全地垫",
 "A long black safety mat lies on the floor in front of the laser cutting machine. No people.",
 "机器前面铺着这条安全地垫。", "安全地垫：一踩全停"),
("K3", "老李沿着地垫走，然后站上去",
 "The facility engineer walks along the mat and then steps onto it.",
 "只要一踩上去，"),
("K3", "示意图：脚踩上地垫，机器所有运动图标停止",
 "A diagram: a foot steps on the mat and all the machine's motion icons stop. No people.",
 "整台机器立刻停止。"),
("K3", "地垫图标和盾牌图标连在一起",
 "A floor mat icon connected to a shield icon. No people.",
 "这是机器上最重要的保护之一。"),
# K4
("K4", "操作台上并排一个红色急停按钮和一个黄色快停按钮",
 "On the operator console, a red emergency stop button sits next to a yellow quick stop button. No people.",
 "停机按钮有两种：急停和进给保持。", "两种停机按钮", ["急停", "进给保持"]),
("K4", "老李走到机器末端，指着另一个按钮",
 "The facility engineer walks to the far end of the machine and points at another button.",
 "操作台上有，机器末端也有。"),
# K5
("K5", "按下快停，龙门架停住，电源指示灯仍亮",
 "The quick stop button is pressed; the gantry freezes while the power indicator lights stay on. No people.",
 "进给保持是快停，", "进给保持：只停运动"),
("K5", "运动箭头被暂停符号挡住",
 "A motion arrow blocked by a pause symbol. No people.",
 "只中断机器的运动。"),
# K6
("K6", "老李手按操作台上的红色急停按钮",
 "The facility engineer presses the red emergency stop button on the console.",
 "急停就不一样了。", "急停：驱动高压全断"),
("K6", "驱动、高压等图标一起熄灭",
 "Icons for motor drives, high voltage and everything else switch off together. No people.",
 "驱动、高压，全部断开。", "", ["驱动", "高压", "全部"]),
# K7
("K7", "老李转身穿过门边，经过储罐和冷水机",
 "The facility engineer turns and walks past a cryogenic tank and a chiller.",
 "要是出了事故，", "出了事拿不准，拉总闸"),
("K7", "一个新操作员图标头顶冒出问号",
 "An icon of a new operator with question marks above his head. No people.",
 "新操作员又不知道该怎么办，"),
("K7", "老李走到墙边的闸刀开关前，伸手指着",
 "The facility engineer reaches a big knife disconnect switch on the wall and points at it.",
 "那就拉下这个总隔离开关。"),
# K8
("K8", "闸刀被拉下",
 "The knife switch handle is pulled down. No people.",
 "总闸一拉，", "总闸一拉，全部断电"),
("K8", "激光器、冷水机、辅助设备图标一起熄灭",
 "Icons of the laser, the chiller and all support equipment go dark together. No people.",
 "激光器、冷水机和辅助设备全断电。", "", ["激光器", "冷水机", "辅助设备"]),
# K9
("K9", "老李站在总闸旁，对镜头竖起一根手指",
 "The facility engineer stands beside the disconnect switch and raises one finger to the camera.",
 "如果你还要花时间想一想，", "还要犹豫，就拉闸"),
("K9", "思考气泡被划掉，箭头指向闸刀开关",
 "A thinking bubble is crossed out and an arrow points to the knife switch. No people.",
 "那就直接拉闸。"),
# 小结
("小结", "欣欣身旁浮现地垫、两个按钮、闸刀开关图标",
 "The panda mascot stands beside icons of a safety mat, two stop buttons and a knife switch.",
 "地垫一踩全停，进给保持停运动。", "小结"),
("小结", "红色急停按钮和闸刀开关",
 "A red emergency stop button and a knife switch side by side. No people.",
 "急停全断，拿不准就拉总闸。"),
# 结尾
("结尾", "欣欣站在总闸旁挥手告别",
 "The panda mascot waves goodbye beside the wall disconnect switch.",
 "紧急停机就讲到这里，下次见！"),
]
