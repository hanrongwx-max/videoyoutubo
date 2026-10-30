# 08_Fundamentals of Laboratory Safety Near Miss Scenario 卡通剧本作者源
# 原片为情景思考题（只提问不作答）：保留 K1–K4，审查补出答案 S1–S5
# （定向气流为什么要向内、不进入并关门挂牌、报告负责人和设施人员、修复验证后再恢复、未遂登记与整改闭环）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "飘带向外飘了",
    "points": {
        "K1": "清晨，飘带向外飘",
        "K2": "气流本该流进实验室",
        "K3": "这时你该怎么做",
        "K4": "本课不能代替本实验室规程",
        "S1": "定向气流为什么要向内",
        "S2": "不进入，关好门，挂牌",
        "S3": "报告负责人和设施人员",
        "S4": "修好验证，再恢复工作",
        "S5": "未遂登记，整改闭环",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验室门外，门框上一根小飘带",
 "The panda mascot stands outside a laboratory door with a small ribbon tape hanging from the top of the door frame.",
 "这一课：门口的小飘带，在提醒什么？", "飘带向外飘了"),
# 情景
("情景", "清晨，小研拎着包走到实验室门口",
 "Early morning light in a corridor; the female graduate student carrying a bag walks up to the laboratory door.",
 "一天早上，小研来实验室做实验。"),
# K1
("K1", "门一开，门框上的飘带向走廊方向飘出",
 "As the lab door opens, the ribbon tape on the door frame blows outward into the corridor. No people.",
 "一开门，飘带却朝走廊外面飘。", "清晨，飘带向外飘"),
("K1", "从实验室指向走廊的蓝色气流箭头，带感叹号",
 "Blue airflow arrows pointing from the lab out into the corridor, with a red exclamation mark. No people.",
 "这说明空气正从实验室往外流。"),
# K2
("K2", "正常情况：气流箭头从走廊流进实验室，飘带向内飘，打绿勾",
 "Normal situation icon: blue airflow arrows flowing from the corridor into the lab, the ribbon tape bending inward, with a green check. No people.",
 "可正常情况下，气流应该流进实验室。", "气流本该流进实验室"),
# K3
("K3", "小研停在门口，手扶门把，皱眉",
 "The female graduate student stops at the doorway with her hand on the handle, frowning.",
 "这时，该怎么办？", "这时你该怎么做"),
("K3", "阿杰从后面走来，想直接进门，被红叉图标挡住",
 "The young male student walks up behind her and tries to walk straight in; a red X icon appears in front of him.",
 "阿杰说：先进去干活吧。不行！"),
# S1
("S1", "欣欣站在剖面示意图前，走廊、门、实验室，箭头向内",
 "The panda mascot stands beside a cutaway diagram of a corridor, a door and a lab, with airflow arrows pointing into the lab.",
 "定向气流，让空气从清洁区流向实验区。", "定向气流为什么要向内"),
("S1", "实验室内的小雾点被向内的箭头挡在室内",
 "Tiny mist dots inside the lab are held back by inward-pointing airflow arrows at the door. No people.",
 "这样，室内的气溶胶就不会跑出来。"),
("S1", "箭头反向，雾点飘向走廊，警示三角",
 "The arrows reverse and the mist dots drift out into the corridor, with a yellow warning triangle. No people.",
 "飘带外飘，说明这道屏障失效了。"),
# S2
("S2", "小研退出门外，轻轻把门关上",
 "The female graduate student steps back into the corridor and gently closes the laboratory door.",
 "不进入，不开展任何实验，关好门。", "不进入，关好门，挂牌"),
("S2", "门上挂起一块空白的暂停使用提示牌，带禁止进入图标",
 "A blank notice board with a no entry pictogram hangs on the laboratory door. No people.",
 "门口挂牌，提醒别人也别进。"),
("S2", "如果已在室内：小人图标放下手中工作、盖好容器、离开",
 "Icon sequence: a person pictogram closes a container, steps away from the bench and exits through a door. No people.",
 "已经在里面，就收好材料，撤出关门。"),
# S3
("S3", "小研打电话给老周",
 "The female graduate student calls the older man on her phone in the corridor.",
 "马上报告实验室负责人。", "报告负责人和设施人员"),
("S3", "老李提着工具箱赶来，查看通风控制面板",
 "The facility engineer arrives with a toolbox and checks a ventilation control panel with blank displays.",
 "通知设施人员，检查通风系统。"),
("S3", "老李在空白记录本上写下发现时间",
 "The facility engineer writes the time of discovery in a blank maintenance logbook.",
 "说清发现时间、现象和位置。"),
# S4
("S4", "老李修好后，飘带重新向内飘",
 "After the repair, the ribbon tape on the door frame bends inward again while the facility engineer watches.",
 "修好后，先确认气流恢复向内。", "修好验证，再恢复工作"),
("S4", "老周看过检查结果，摘下提示牌",
 "The older man reviews the check results with the facility engineer and removes the notice from the door.",
 "负责人确认后，才能恢复实验。"),
("S4", "小研每次进门前抬头看一眼飘带",
 "The female graduate student glances up at the ribbon tape before entering the lab.",
 "以后每次进门，先看一眼飘带。"),
# S5
("S5", "欣欣举着一张空白的未遂事件登记表",
 "The panda mascot holds up a blank near miss report form.",
 "没人受伤，这是一起未遂事件。", "未遂登记，整改闭环"),
("S5", "王老师在空白登记表上记录，小研在旁说明",
 "The safety administrator fills in the blank report form while the female graduate student explains.",
 "也要登记上报，不能修好就算。"),
("S5", "闭环箭头：登记、查原因、整改、复查、分享",
 "A closed loop of five arrows with icons: a form, a magnifier, a wrench, a check mark, and a speech bubble. No people.",
 "查原因、定措施、复查、全组分享。", "", ["登记", "查原因", "整改", "复查", "分享"]),
("S5", "老李在通风设备上加装一个报警灯",
 "The facility engineer installs a small warning light on the ventilation control panel.",
 "比如加装报警，下次早发现。"),
# K4
("K4", "一张空白课程卡片和一本更大的空白规程手册",
 "A small blank course card next to a larger blank procedure binder with a check mark. No people.",
 "这门课不能代替本实验室的规程。", "本课不能代替本实验室规程"),
# 小结
("小结", "欣欣身旁浮现向内的气流箭头和飘带",
 "The panda mascot stands beside floating icons of inward airflow arrows and a ribbon tape.",
 "气流应向内，飘带外飘就是异常。", "小结"),
("小结", "关门、挂牌、电话三个图标",
 "Three icons: a closed door, a no entry notice, and a telephone. No people.",
 "不进入，关门挂牌，报告负责人。"),
("小结", "扳手、对勾、闭环箭头三个图标",
 "Three icons: a wrench, a green check, and a closed loop arrow. No people.",
 "修好验证再开工，未遂整改要闭环。"),
# 结尾
("结尾", "欣欣和小研、老李在实验室门口挥手，飘带向内",
 "The panda mascot, the female graduate student and the facility engineer wave goodbye at the lab door, the ribbon tape bending inward.",
 "小飘带，大提醒，下次见！"),
]
