# 07_Fundamentals of Laboratory Safety Emergency Procedures and Reporting Scenario 卡通剧本作者源
# 原片为情景思考题（只提问不作答）：保留 K1–K3，审查补出答案 S1–S5
# （刺破手套后的即时处置、未遂也要报告、逐级报告流程、紧急电话 119/120 与保卫处、应急预案与演练）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "手套破了，要不要说",
    "points": {
        "K1": "针头刺破手套，皮肤没伤",
        "K2": "这样的未遂要不要报告",
        "K3": "本课不能代替本实验室规程",
        "S1": "先停下，换手套，查皮肤",
        "S2": "未遂事件也要报告",
        "S3": "逐级报告：负责人、学院、学校",
        "S4": "紧急情况：119、120和保卫处",
        "S5": "应急预案和演练",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣举着一只有小破洞的手套，向镜头歪头",
 "The panda mascot holds up a blue nitrile glove with a tiny hole and tilts its head at the camera.",
 "这一课：手套破了，要不要告诉别人？", "手套破了，要不要说"),
# 情景
("情景", "阿杰戴蓝手套，在生物安全柜前做实验",
 "The young male student in a lab coat, goggles and blue nitrile gloves works at a biological safety cabinet.",
 "阿杰正在生物安全柜里做实验。"),
# K1
("K1", "针头图标擦过手套图标，手套上出现一个小破口",
 "An icon of a needle tip grazing a gloved finger, leaving a tiny tear in the glove. No people.",
 "一不小心，针头刺破了手套。", "针头刺破手套，皮肤没伤"),
("K1", "阿杰看看手指，松了口气",
 "The young male student looks at his gloved finger and lets out a sigh of relief.",
 "还好，好像没扎到皮肤。"),
# K2
("K2", "阿杰把手指藏到身后，想当作没发生",
 "The young male student hides his hand behind his back and looks around, pretending nothing happened.",
 "没受伤，要不要告诉别人？", "这样的未遂要不要报告"),
("K2", "欣欣从旁边探出头，用力点头",
 "The panda mascot pops out from the side and nods firmly.",
 "答案是：要说，而且要马上说。", "", ["要报告"]),
# S1
("S1", "阿杰把注射器放进锐器盒，双手离开操作区",
 "The young male student places the syringe into a sharps container and steps his hands back from the work area.",
 "先停下，把锐器安全放好。", "先停下，换手套，查皮肤"),
("S1", "阿杰脱下手套，对着灯光仔细看手指",
 "The young male student removes his gloves and carefully inspects his finger under the light.",
 "脱下手套，仔细检查皮肤有没有伤口。"),
("S1", "阿杰在水槽边洗手，然后戴上新手套",
 "The young male student washes his hands at a sink and then puts on a fresh pair of gloves.",
 "洗手，换上新手套。"),
("S1", "手指图标上有红点，箭头指向冲洗和医院图标",
 "A finger icon with a small red dot, with arrows pointing to a running faucet icon and a hospital icon. No people.",
 "一旦发现破皮，就按暴露处置。"),
# S2
("S2", "冰山图标：水面上一小块，水面下一大块",
 "An iceberg icon with a small tip above the water line and a much larger part below. No people.",
 "未遂事件，是水面下的冰山。", "未遂事件也要报告", ["事故", "未遂", "隐患"]),
("S2", "针头朝向自己的图标被红叉划掉",
 "An icon of a needle pointing toward the user's own hand, crossed out with a red X. No people.",
 "这次没伤到，下次可能就扎进去。"),
("S2", "小研和阿杰一起看着空白流程图，找出问题环节",
 "The female graduate student and the young male student look at a blank flow chart and circle one step.",
 "说出来，大家才能找到原因、改掉它。"),
("S2", "举手的小人图标旁是盾牌",
 "A person pictogram raising a hand, next to a shield icon. No people.",
 "报告不是挨批评，是保护大家。"),
# S3
("S3", "阿杰走进老周办公室，比划刚才的情况",
 "The young male student walks into the older man's office and explains what happened with gestures.",
 "第一时间报告实验室负责人。", "逐级报告：负责人、学院、学校"),
("S3", "三层台阶图标：实验室、学院、学校，箭头向上",
 "A three-level step icon with upward arrows: a lab room, a school building, and a university building. No people.",
 "需要时，再报学院和学校管理部门。", "", ["实验室", "学院", "学校"]),
("S3", "王老师在空白登记表上记录",
 "The safety administrator writes the details on a blank incident report form.",
 "如实登记时间、经过和处理情况。"),
# S4
("S4", "实验室门边张贴着应急电话卡，只有电话图标和数字",
 "An emergency contact card on the wall by the lab door, showing phone icons and large digits only. No people.",
 "门口张贴的应急电话，要记牢。", "紧急情况：119、120和保卫处", ["119", "120", "保卫处"]),
("S4", "火焰图标旁是电话和119",
 "A flame icon next to a telephone icon. No people.",
 "着火爆炸，拨打119。", "", ["119"]),
("S4", "红十字图标旁是电话和120",
 "A red cross icon next to a telephone icon. No people.",
 "有人受伤，拨打120。", "", ["120"]),
("S4", "保卫处值班员接起电话，迅速记录",
 "The security officer answers the phone at the duty desk and quickly takes notes.",
 "同时通知学校保卫处，引导救援。"),
# S5
("S5", "老周把一本空白的应急预案放到架子上",
 "The older man places a blank emergency plan binder on the shelf near the lab door.",
 "实验室要有应急预案，人人知道。", "应急预案和演练"),
("S5", "全组人员在王老师带领下练习疏散和使用洗眼器",
 "Led by the safety administrator, the team practices an evacuation drill and using an eyewash station.",
 "定期演练，出事时才不慌。"),
# K3
("K3", "一张空白课程卡片和一本更大的空白规程手册",
 "A small blank course card next to a larger blank procedure binder with a check mark. No people.",
 "这门课不能代替本实验室的规程。", "本课不能代替本实验室规程"),
# 小结
("小结", "欣欣身旁浮现破手套、锐器盒、洗手图标",
 "The panda mascot stands beside floating icons of a torn glove, a sharps container and hand washing.",
 "停下操作，查皮肤，换手套。", "小结"),
("小结", "冰山和三层台阶图标",
 "Icons of an iceberg and a three-level step with upward arrows. No people.",
 "未遂也报告，负责人、学院、学校。"),
("小结", "119、120和保卫处三个电话图标",
 "Three telephone icons side by side. No people.",
 "紧急情况，119、120、保卫处。", "", ["119", "120", "保卫处"]),
# 结尾
("结尾", "欣欣和阿杰在应急电话卡前挥手",
 "The panda mascot and the young male student wave goodbye in front of the emergency contact card by the lab door.",
 "说出来，就是保护大家，下次见！"),
]
