# 39_BIOSAFETY LEVEL 3 LABORATORY 卡通剧本作者源（原著版）
# 原片为竖屏设施走访（3 分 50 秒）：封闭/三级生物实验室如何用定向气流把病原控制在限定空间——
# 气闸正压、负压区、高效空气过滤、顶部排风、负压递减套间、洁净/污染分区、更衣与警示标识。
# 原著版：完全照原片，保留全部知识点 K1–K15，不补充知识点、不做本土化；
# 原片口播的"0.22 微米"过滤器说法照原片保留，不更正。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "三级生物安全实验室",
    "edition": "原著版",
    "points": {
        "K1": "定向气流控住病原",
        "K2": "封闭的基本概念",
        "K3": "气闸间是正压",
        "K4": "正压像一道风幕",
        "K5": "里面一区是负压",
        "K6": "排风先过高效过滤",
        "K7": "过滤器把病原截住",
        "K8": "气流导向顶部排出",
        "K9": "定向气流是工程控制",
        "K10": "越往里负压越低",
        "K11": "涉病原都在负压间做",
        "K12": "洁净区与污染区分开",
        "K13": "进出要走更衣流程",
        "K14": "门口有危害与禁入标识",
        "K15": "病原被关在各自工作区",
    },
    "avoid": ["UMS", "Universiti Malaysia Sabah", "Malaysia", "Siemens", "BSL", "HEPA", "WHO"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一扇封闭实验室的门前",
 "The panda mascot stands in front of a sealed laboratory door.",
 "今天带你看，三级室怎么封住病原。", "三级室怎么封"),
("开场", "欣欣指向门上的生物危害标志",
 "The panda mascot points at a biohazard sign on the door.",
 "靠的不是锁，是气流。"),
# 情景
("情景", "阿杰隔着玻璃好奇地往里看",
 "The young male student peers curiously through a glass window.",
 "阿杰问：空气不会把病原带出来吗？"),
("情景", "老李穿着设施工服指着通风口",
 "The facility engineer in work clothes points at an air vent.",
 "老李说：看气往哪个方向走。"),
# K1
("K1", "一条蓝色气流箭头把病原图标往里压",
 "A blue airflow arrow pushes a pathogen icon inward. No people.",
 "定向气流，把病原控在屋里。", "定向气流控住病原"),
# K2
("K2", "一间屋子被一圈气流包住",
 "A room wrapped in a ring of airflow. No people.",
 "这就是封闭的基本思路。", "封闭的基本概念"),
# K3
("K3", "一间气闸间，两侧箭头向外推",
 "An airlock room with arrows pushing outward on both sides. No people.",
 "气闸间是正压，把空气挡在外。", "气闸间是正压"),
# K4
("K4", "一道向下的风幕像超市门口",
 "A downward air curtain like a supermarket entrance. No people.",
 "正压像一道风幕，往下压。", "正压像一道风幕"),
("K4", "风幕把病原图标压在门内一侧",
 "The air curtain keeps a pathogen icon on the inner side of the door. No people.",
 "病原就被锁在封闭区里。"),
# K5
("K5", "里面一区，箭头全部向内",
 "An inner zone with all arrows pointing inward. No people.",
 "再往里是负压，空气只进不出。", "里面一区是负压"),
# K6
("K6", "排风口前装一层高效过滤网",
 "An exhaust vent fitted with a high-efficiency filter. No people.",
 "排风先过高效过滤，再出门。", "排风先过高效过滤"),
# K7
("K7", "过滤网把病原颗粒拦在网里",
 "The filter traps pathogen particles in its mesh. No people.",
 "过滤器把病原截在滤材里。", "过滤器把病原截住"),
("K7", "放大的滤材纤维，旁边一个微米刻度尺",
 "A magnified filter fibre mat beside a small micrometre scale bar. No people.",
 "这道过滤器是0.22微米的。", "", ["0.22微米"]),
# K8
("K8", "气流沿墙升到天花板的过滤器",
 "Airflow rises along the wall to a ceiling filter. No people.",
 "气流被导到顶部，过滤后排出。", "气流导向顶部排出"),
# K9
("K9", "一个齿轮图标压在气流箭头上",
 "A gear icon over an airflow arrow. No people.",
 "定向气流，是一种工程控制。", "定向气流是工程控制"),
("K9", "多间实验室都画着同样的气流",
 "Several labs all drawn with the same airflow pattern. No people.",
 "各类生物实验室都用它。"),
# K10
("K10", "一排套间，负压数字一间比一间低",
 "A row of suites with pressure getting more negative inward. No people.",
 "越往里走，负压越低。", "越往里负压越低"),
# K11
("K11", "负压套间里放着诊断和实验图标",
 "A negative-pressure suite holding diagnostic and experiment icons. No people.",
 "涉病原的活，都在负压间做。", "涉病原都在负压间做"),
# K12
("K12", "一张平面图，洁净区绿、污染区红",
 "A floor plan: clean zone in green, dirty zone in red. No people.",
 "平面分区：洁净和污染分开。", "洁净区与污染区分开", ["洁净区", "污染区"]),
# K13
("K13", "一扇更衣间门，挂着工服图标",
 "A change-room door with a gown icon. No people.",
 "进出要走更衣流程。", "进出要走更衣流程"),
# K14
("K14", "门口贴着生物危害标志和禁入标志",
 "A biohazard sign and a no-entry sign at the door. No people.",
 "门口有危害和禁止擅入标识。", "门口有危害与禁入标识"),
# K15
("K15", "病原图标被圈在各自的工作区里",
 "Pathogen icons enclosed within their own work zones. No people.",
 "病原被关在各自的工作区。", "病原被关在各自工作区"),
# 小结
("小结", "欣欣身旁：正压风幕、负压箭头、顶部过滤",
 "The panda mascot beside an air curtain, inward arrows and a ceiling filter.",
 "正压挡、负压收、过滤排。", "封闭的基本概念"),
("小结", "洁净区、污染区和门口标识三个图标",
 "Three icons: a clean zone, a contaminated zone and a door warning sign. No people.",
 "分区、更衣、标识，各管一段。"),
# 结尾
("结尾", "欣欣在门前挥手，气流箭头环绕",
 "The panda mascot waves in front of the door with airflow arrows around.",
 "气流守得住，我们下次见！"),
]
