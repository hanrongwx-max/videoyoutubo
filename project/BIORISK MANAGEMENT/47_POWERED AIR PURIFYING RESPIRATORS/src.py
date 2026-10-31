# 47_POWERED AIR PURIFYING RESPIRATORS 卡通剧本作者源（原著版）
# 原片是 3 分钟操作演示：头盔式电动送风过滤式呼吸器（PAPR）的组成、原理、穿戴（腰带—电池—头罩—头箍—先通电—灯全亮—系带）、
# 脱卸（风机运转时摘下再断电）、表面去污与充电。
# 原著版：完全照原片，保留全部知识点 K1–K14，不补充知识点、不做本土化；
# 照原片保留：演示者（老李）穿短袖 T 恤、不戴手套、不穿防护服在自己身上演示，不打叉不提示；电池续航“约 6 小时”。
# 品牌不出现（入 avoid）。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "电动送风过滤式呼吸器",
    "edition": "原著版",
    "points": {
        "K1": "送风头罩由什么组成",
        "K2": "头罩可以更换",
        "K3": "空气怎么流",
        "K4": "靠电池供电",
        "K5": "先系腰带",
        "K6": "电池充满，装牢",
        "K7": "溢洒后换头罩",
        "K8": "调好头箍",
        "K9": "先通电，再戴上",
        "K10": "开机看灯，留意续航",
        "K11": "戴上、系紧、查一圈",
        "K12": "脱下：风机转着摘，再断电",
        "K13": "用后表面去污",
        "K14": "用完就充电",
    },
    "avoid": ["MAXAIR", "MaxAir", "Max Air", "TouchNTuff", "UMS", "Universiti Malaysia Sabah", "Kenneth", "Rodrigues", "MOOC"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验室更衣间，手捧一个白色送风头盔，向镜头招手",
 "The panda mascot stands in a laboratory changing room holding a white powered air hood helmet and waves at the camera.",
 "今天学穿送风式呼吸头罩。", "送风头罩，一步步穿对"),
("开场", "欣欣指着头盔、电池、腰带三样东西",
 "The panda mascot points at a helmet, a battery pack and a belt laid on a bench.",
 "顺序错一步，都可能出危险。"),
# 情景
("情景", "小研拿着空白通知，第一次要进高等级实验室",
 "The female graduate student holds a blank notice, preparing to enter a high containment laboratory for the first time.",
 "小研第一次要用送风头罩。"),
("情景", "小研拿起头盔左看右看，一脸疑惑",
 "The female graduate student turns the helmet around with a puzzled look.",
 "这么多部件，先装哪个？"),
("情景", "穿短袖T恤的老李推着设备车进来，要亲自示范",
 "The facility engineer in a short-sleeved T-shirt and no gloves wheels an equipment cart in, ready to demonstrate on himself.",
 "老李穿上身，给她示范一遍。"),
# K1
("K1", "老李手指头盔顶部的过滤器",
 "The facility engineer points to the filter mounted on top of the helmet.",
 "头盔里装着过滤器，能挡住病原。", "送风头罩由什么组成"),
("K1", "头盔、头罩、电池、腰带四个部件摆开",
 "Four parts laid out on a bench: a helmet, a soft shroud, a battery pack and a belt. No people.",
 "头盔、头罩、电池、腰带，一整套。", "", ["头盔", "头罩", "电池", "腰带"]),
# K2
("K2", "老李把白色披肩头罩从头盔上取下又装回",
 "The facility engineer detaches the white shroud from the helmet and attaches it again.",
 "外面这层披肩头罩，可以更换。", "头罩可以更换"),
# K3
("K3", "示意图：空气从头盔侧面吸入，经过滤器，向下吹过面部",
 "A diagram of air drawn in from the side of the helmet, passing a filter and flowing downward over the face. No people.",
 "空气从侧面吸进，过滤后吹向脸部。", "空气怎么流"),
("K3", "头罩内气流箭头向下、向外",
 "Arrows inside the hood flowing down and out under the shroud. No people.",
 "向下的气流，把脏空气挡在外面。"),
# K4
("K4", "电池组和连接线图标",
 "A battery pack icon with a connecting cable. No people.",
 "风机靠电池带动。", "靠电池供电"),
# K5
("K5", "老李把腰带系在自己腰上，调好松紧，小研在旁看",
 "The facility engineer in a short-sleeved T-shirt and no gloves fastens a belt around his own waist and adjusts it while the female graduate student watches.",
 "第一步，先系好腰带。", "先系腰带"),
("K5", "穿上防护服后手够不到腰带的示意，问号",
 "A diagram of a person in a protective suit unable to reach the belt underneath, with a question mark. No people.",
 "穿上防护服，就够不着了。"),
# K6
("K6", "电池放在充电座上，指示灯满格",
 "A battery pack on a charging dock showing a full charge indicator. No people.",
 "每次实验前，电池要充满。", "电池充满，装牢"),
("K6", "老李把电池卡进自己腰带上",
 "The facility engineer in a short-sleeved T-shirt and no gloves clips the battery pack firmly onto his belt.",
 "把电池牢牢装在腰带上。"),
# K7
("K7", "头罩上一滩液体溢洒的图标",
 "A shroud with a liquid spill mark on it. No people.",
 "头罩去污后可以再用。", "溢洒后换头罩"),
("K7", "沾了溢洒的头罩放进生物危害废物袋，新头罩换上",
 "A spill-stained shroud goes into a biohazard waste bag and a fresh shroud is fitted. No people.",
 "可一旦沾上溢洒，就换新的。"),
# K8
("K8", "老李转动头盔内的头箍旋钮",
 "The facility engineer in a short-sleeved T-shirt and no gloves turns the headband adjustment knob inside the helmet.",
 "调节头箍，让它稳稳贴住额头。", "调好头箍"),
# K9
("K9", "老李把电源线插到电池和头盔上",
 "The facility engineer in a short-sleeved T-shirt and no gloves plugs the cable into the battery and the helmet.",
 "戴上之前，先插好电源线。", "先通电，再戴上"),
("K9", "不通电就戴上头罩的图标被打叉，旁边红色警示",
 "An icon of a person wearing an unpowered hood, crossed out with a red X and a red warning sign. No people.",
 "不送风戴着头罩，会喘不上气！"),
# K10
("K10", "电池上三个指示灯全部亮起",
 "Three indicator lights all turn on on the battery pack. No people.",
 "开机，看指示灯是不是全亮。", "开机看灯，留意续航"),
("K10", "电池图标和时钟",
 "A battery icon beside a clock. No people.",
 "这款电池约用六小时，再充电。"),
# K11
("K11", "老李双手戴上头盔，披肩垂到T恤上",
 "The facility engineer in a short-sleeved T-shirt and no gloves puts the helmet on with both hands and the shroud drapes over his shirt.",
 "风机转着，戴上头盔。", "戴上、系紧、查一圈"),
("K11", "老李系紧颈部的带子",
 "The facility engineer in a short-sleeved T-shirt and no gloves tightens the straps around his neck.",
 "系紧带子，披肩盖住肩膀。"),
("K11", "老李慢慢转一圈，小研帮他看前后",
 "The facility engineer in a short-sleeved T-shirt and no gloves turns around slowly while the female graduate student checks front and back.",
 "转一圈，前后都检查到位。"),
# K12
("K12", "老李站着，头盔里风机仍在转",
 "The facility engineer in a short-sleeved T-shirt and no gloves stands still with the helmet fan still running.",
 "脱的时候，风机先别关。", "脱下：风机转着摘，再断电"),
("K12", "老李双手托住头盔后部，向上向前摘下",
 "The facility engineer in a short-sleeved T-shirt and no gloves lifts the helmet off from the back with both hands",
 "先把头盔摘下来。"),
("K12", "摘下后，才拔下电源线",
 "After the helmet is off, the power cable is unplugged. No people.",
 "摘下来以后，再断开电池。"),
# K13
("K13", "头盔放在托盘上，用消毒湿巾擦拭表面",
 "A helmet on a tray being wiped with disinfectant wipes by a bare hand.",
 "每次用完，表面去污。", "用后表面去污"),
("K13", "老李空手用消毒湿巾擦头盔表面",
 "The facility engineer in a short-sleeved T-shirt and no gloves wipes the helmet surface with disinfectant wipes.",
 "用推荐的消毒剂擦表面。"),
("K13", "旧头罩放进废物袋，换上新头罩",
 "An old shroud goes into a waste bag and a new shroud is fitted. No people.",
 "需要时，换上新头罩。"),
# K14
("K14", "电池放回充电座，日历上打勾",
 "The battery pack is placed back on the charging dock with a calendar tick. No people.",
 "用完马上充电，下次才放心。", "用完就充电"),
# 小结
("小结", "欣欣身旁一排步骤图标：腰带、电池、头箍、插电、灯亮、系带",
 "The panda mascot stands beside a row of step icons: belt, battery, headband, plug, lights and straps.",
 "腰带、电池、头箍、先插电，再戴上。", "小结"),
("小结", "电池三灯全亮和时钟图标",
 "Three battery lights on beside a clock icon. No people.",
 "开机看灯全亮，续航约六小时。"),
("小结", "风机转着摘头盔、再断电的两格图",
 "Two panels: removing the helmet with the fan on, then unplugging the cable. No people.",
 "脱时风机先转着，摘下再断电。"),
("小结", "擦拭头盔和充电座两个图标",
 "Two icons: wiping a helmet and a charging dock. No people.",
 "用后表面去污，然后充电。"),
# 结尾
("结尾", "欣欣和小研、老李一起挥手",
 "The panda mascot waves goodbye together with the female graduate student and the facility engineer.",
 "一步步穿对，安全才有保障，再见！"),
]
