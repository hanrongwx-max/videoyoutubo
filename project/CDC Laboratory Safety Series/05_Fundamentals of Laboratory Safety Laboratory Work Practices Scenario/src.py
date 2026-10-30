# 05_Fundamentals of Laboratory Safety Laboratory Work Practices Scenario 卡通剧本作者源
# 原片为事故情景思考题（只提问不作答）：保留 K1–K6，审查补出答案 S1–S5
# （规范用电不拉线、通道和门口畅通、容器必须有标签、加热不离人、烫伤处置与事故报告）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "一根电线引发的烫伤",
    "points": {
        "K1": "在仪器旁用加热板",
        "K2": "附近没插座，拉了延长线",
        "K3": "无标签溶液，无人看管",
        "K4": "同事绊倒，手被烫伤",
        "K5": "事故原因与避免办法",
        "K6": "本课不能代替本实验室规程",
        "S1": "规范用电，不乱拉线",
        "S2": "通道和门口保持畅通",
        "S3": "容器必须贴标签",
        "S4": "加热不离人",
        "S5": "烫伤处置与事故报告",
    },
    "avoid": ["Centers for Disease Control", "Division of Laboratory Systems", "reach.cdc.gov",
              "Public Health Service", "Health and Human Services"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台加热板旁，指着地上的一根电线",
 "The panda mascot stands beside a hot plate on a bench and points down at a power cord on the floor.",
 "这一课：一根电线，怎么引发了烫伤？", "一根电线引发的烫伤"),
# K1
("K1", "阿杰把加热搅拌器搬到另一台仪器旁，放上一只烧杯",
 "The young male student places a stirring hot plate next to another instrument and sets a beaker of clear liquid on it.",
 "阿杰要在一台仪器旁边用加热板。", "在仪器旁用加热板"),
# K2
("K2", "阿杰四处找插座，墙上附近没有",
 "The young male student looks around the bench for a wall outlet, but there is none nearby.",
 "可附近没有插座。", "附近没插座，拉了延长线"),
("K2", "阿杰拉出一根长延长线，从台边一直拖过地面",
 "The young male student unrolls a long extension cord from the bench across the floor of the lab.",
 "他拉了根延长线，一直拖过地面。"),
("K2", "延长线横穿门前通道，插在门边的插座上",
 "The extension cord lies across the walkway right in front of the laboratory door, plugged into an outlet by the door. No people.",
 "插头接到了实验室另一头的门口。"),
# K3
("K3", "烧杯里液体在搅拌，杯身没有任何标签",
 "A beaker of clear liquid stirring on the hot plate, with no label on the beaker. No people.",
 "烧杯里的溶液，没贴任何标签。", "无标签溶液，无人看管"),
("K3", "阿杰看看手表，转身离开实验台",
 "The young male student glances at his watch and walks away from the bench, leaving the hot plate on.",
 "他想：就走开一小会儿。"),
# K4
("K4", "老周抱着一摞空白文件夹进门，没看见地上的电线",
 "The older man walks through the door carrying a stack of blank binders and does not see the cord on the floor.",
 "这时，老周抱着资料走进门。", "同事绊倒，手被烫伤"),
("K4", "被电线绊倒的小人图标和发烫的加热板图标",
 "Icons: a person pictogram tripping over a cord, and a hot plate icon with red heat waves and a hand icon. No people.",
 "他被电线绊倒，手按在了加热板上。"),
# K5
("K5", "欣欣举着放大镜，身后浮现四个问号",
 "The panda mascot holds a big magnifier, with four question mark icons floating behind it.",
 "哪些情形导致了事故？怎样能避免？", "事故原因与避免办法"),
("K5", "四个图标：延长线、门口、无标签烧杯、空人位，各带红叉",
 "Four icons each with a red X: an extension cord on the floor, a blocked doorway, an unlabeled beaker, and an empty bench with a hot plate on. No people.",
 "乱拉线、堵门口、没标签、没人看。", "", ["乱拉线", "堵通道", "无标签", "无人看管"]),
# S1
("S1", "老李在实验台边安装一个新的固定插座",
 "The facility engineer installs a new fixed wall outlet next to the lab bench.",
 "设备放在有插座的位置，不够就报修加装。", "规范用电，不乱拉线"),
("S1", "拖地的延长线、插排串插排两个图标被红叉划掉",
 "Two icons crossed out with red X marks: an extension cord lying across a floor, and power strips plugged into each other. No people.",
 "不拖地拉线，不串接插排。", "", ["不拖地", "不串接"]),
("S1", "老李检查插座和电线，竖起大拇指",
 "The facility engineer checks the outlet and the hot plate cord, then gives a thumbs-up.",
 "大功率设备用电，请设施人员评估。"),
# S2
("S2", "实验室门口和通道空无一物，地面干净",
 "A clear laboratory doorway and walkway with nothing on the floor, and a green emergency exit sign above the door. No people.",
 "通道和门口，任何时候都要畅通。", "通道和门口保持畅通"),
("S2", "门口的箱子和电线被挪开",
 "The female graduate student moves a box and a cable away from the doorway.",
 "出了事，这里是撤离的路。"),
# S3
("S3", "小研给烧杯贴上标签，标签上只有图标",
 "The female graduate student sticks a label with only simple icons onto the beaker.",
 "所有容器，都要贴上标签。", "容器必须贴标签"),
("S3", "标签放大，四个小图标：瓶子、百分比、日历、人像",
 "Close-up of a label showing four small icons: a bottle, a percent sign, a calendar, and a person. No people.",
 "写明名称、浓度、日期和使用人。", "", ["名称", "浓度", "日期", "使用人"]),
# S4
("S4", "阿杰守在加热板旁，看着搅拌",
 "The young male student stands beside the stirring hot plate and watches it carefully.",
 "加热时不离人。", "加热不离人"),
("S4", "加热板旋钮转到关，旁边放着一块空白的加热中提示牌",
 "A hand turns the hot plate knob to off; a blank hot surface warning sign stands next to it.",
 "要离开，先关加热，或请人看护挂牌。"),
("S4", "加热板周围的纸张和溶剂瓶被移开",
 "Paper towels and a solvent bottle are moved away from the hot plate on the bench. No people.",
 "加热板周边，不放纸张和易燃物。"),
# S5
("S5", "老周把手放在水龙头下冲洗",
 "The older man holds his hand under cool running water at a lab sink.",
 "烫伤了，立即用流动冷水冲洗。", "烫伤处置与事故报告"),
("S5", "电话图标旁有红十字和120",
 "A telephone icon with a red cross icon beside it. No people.",
 "伤得重，及时就医，紧急拨打120。", "", ["120"]),
("S5", "阿杰向老周和王老师说明经过，王老师在空白记录本上记录",
 "The young male student explains what happened to the older man and the safety administrator, who writes in a blank logbook.",
 "报告负责人，如实记录，整改到位。"),
# K6
("K6", "一张空白课程卡片和一本更大的空白规程手册",
 "A small blank course card next to a larger blank procedure binder with a check mark. No people.",
 "这门课不能代替本实验室的规程。", "本课不能代替本实验室规程"),
# 小结
("小结", "欣欣身旁浮现插座和畅通门口两个图标",
 "The panda mascot stands beside floating icons of a wall outlet and a clear doorway.",
 "用固定插座，通道门口不拉线。", "小结"),
("小结", "贴标签的烧杯和守在旁边的小人图标",
 "Icons of a labeled beaker and a person standing next to a hot plate. No people.",
 "容器有标签，加热不离人。"),
("小结", "水龙头和报告单图标",
 "Icons of a running faucet and a blank report form. No people.",
 "烫伤先冲水，事后要报告。"),
# 结尾
("结尾", "欣欣和阿杰在整洁的实验台旁挥手",
 "The panda mascot and the young male student wave goodbye beside a tidy bench with a labeled beaker on a hot plate.",
 "小习惯，防大事故，下次见！"),
]
