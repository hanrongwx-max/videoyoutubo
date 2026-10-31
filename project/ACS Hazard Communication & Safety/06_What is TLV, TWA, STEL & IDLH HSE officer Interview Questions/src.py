# 06_What is TLV, TWA, STEL & IDLH HSE officer Interview Questions 卡通剧本作者源（原著版）
# 原片为四个职业接触限值术语的面试题讲解（幻灯片）：完全照原片，保留 K1–K5 的定义和硫化氢示例数值
# （TWA 10 ppm、STEL 15 ppm、IDLH 100 ppm）及“在此浓度下可工作多久 / 不能工作”的说法；不本土化、不加补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "TLV、TWA、STEL与IDLH是什么",
    "edition": "原著版",
    "points": {
        "K1": "阈限值TLV",
        "K2": "时间加权平均浓度TWA",
        "K3": "短时间接触限值STEL",
        "K4": "立即威胁生命和健康浓度IDLH",
        "K5": "四个术语一组浓度界限",
    },
    "avoid": ["Safety Management Study", "SAFETY MGMT STUDY", "SAFETY MGMT", "ACGIH", "NIOSH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在问答台后，身边四张空白卡片",
 "The panda mascot stands behind a quiz podium with four blank cards fanned out beside it and waves at the camera.",
 "今天的面试题：四个接触限值。", "安全知识问答：读懂职业接触限值"),
# 情景
("情景", "阿杰对着四个英文缩写卡皱眉",
 "The young male student frowns at four blank cards with simple letter-shaped icons on a desk.",
 "阿杰面试安全员，最怕这四个缩写。"),
("情景", "欣欣把四张卡排成一列",
 "The panda mascot lines up the four cards in a column on the podium.",
 "我们一个一个来讲。"),
# K5 目录
("K5", "四张卡片依次亮起，旁边一个火焰图标",
 "Four cards light up one by one next to a flame icon. No people.",
 "TLV、TWA、STEL、IDLH。", "四个术语一组浓度界限", ["TLV", "TWA", "STEL", "IDLH"]),
("K5", "一条从长期到立即危险的箭头",
 "A long arrow running from a calendar icon through a clock and an hourglass to a skull pictogram. No people.",
 "从长期、每天、短时到立即危险。"),
# K1
("K1", "空气中漂浮的分子点，旁边一个小人图标",
 "Small floating molecule dots in the air next to a worker pictogram. No people.",
 "TLV，阈限值：空气中有害物浓度。", "阈限值TLV"),
("K1", "小人图标沿一条长时间线从年轻走到年老",
 "A worker pictogram walks along a long timeline from young to old, a calendar flipping beside it. No people.",
 "日复一日，接触整个职业生涯。"),
("K1", "长期和短期两个健康图标都打绿勾",
 "A long-term health icon and a short-term health icon, both with green checks. No people.",
 "都不会产生长期或短期的不良影响。"),
# K2
("K2", "时钟显示八小时，日历一周五天",
 "A clock icon showing a full working day and a calendar with five weekdays highlighted. No people.",
 "TWA：空气中污染物的浓度。", "时间加权平均浓度TWA", ["8小时/天", "40小时/周"]),
("K2", "工人图标在波动浓度线旁，下方一条平均线",
 "A worker pictogram beside a wavy concentration line with a flat average line under it. No people.",
 "每天8小时、每周40小时接触。"),
("K2", "长短期健康图标打绿勾",
 "A long-term health icon and a short-term health icon with green checks. No people.",
 "不产生长期或短期的不良影响。"),
("K2", "硫化氢气团图标旁一个大号数字牌",
 "A gas cloud icon next to a large blank number card. No people.",
 "比如硫化氢，TWA是10ppm。", "", ["H2S", "10ppm"]),
("K2", "工人图标在厂门口按时上下班",
 "A worker pictogram clocks in and out at a plant gate next to a clock showing a full shift. No people.",
 "在这个浓度下，可以正常干8小时。"),
# K3
("K3", "沙漏图标旁一个浓度尖峰",
 "An hourglass icon next to a short sharp peak on a concentration line. No people.",
 "STEL：化学品的最高浓度。", "短时间接触限值STEL"),
("K3", "沙漏流完一刻钟",
 "An hourglass runs through a quarter of an hour, with a green check. No people.",
 "最多接触15分钟，不伤健康。", "", ["15分钟"]),
("K3", "硫化氢气团图标旁一个数字牌",
 "A gas cloud icon next to a large blank number card with an hourglass. No people.",
 "硫化氢的STEL是15ppm。", "", ["H2S", "15ppm"]),
("K3", "工人图标工作片刻，沙漏流完后离开",
 "A worker pictogram works briefly then steps out as the hourglass empties. No people.",
 "在这个浓度下，只能干15分钟。"),
# K4
("K4", "红色警示区里的骷髅图标",
 "A red danger zone with a skull pictogram and a gas cloud. No people.",
 "IDLH：立即威胁生命和健康的浓度。", "立即威胁生命和健康浓度IDLH"),
("K4", "小人图标碰到红区边缘，红色闪光",
 "A worker pictogram touches the edge of the red zone and a red flash appears. No people.",
 "一旦接触，直接威胁生命，甚至致死。"),
("K4", "硫化氢气团图标旁一个红色数字牌",
 "A gas cloud icon next to a large red blank number card. No people.",
 "硫化氢的IDLH是100ppm。", "", ["H2S", "100ppm"]),
("K4", "红区门口一个停止手势",
 "A stop hand icon at the entrance of the red zone. No people.",
 "这样的环境里，不能作业。"),
# 小结
("小结", "欣欣身旁四张卡片排成阶梯",
 "The panda mascot stands beside the four cards arranged as rising steps.",
 "TLV管一辈子，TWA管每天8小时。", "小结"),
("小结", "沙漏和骷髅图标",
 "An hourglass icon and a skull pictogram side by side. No people.",
 "STEL管15分钟，IDLH立即危险。"),
("小结", "三个数字牌并排",
 "Three blank number cards side by side, growing larger and turning from yellow to red. No people.",
 "硫化氢：10、15、100ppm。", "", ["TWA 10", "STEL 15", "IDLH 100"]),
# 结尾
("结尾", "欣欣竖起大拇指挥手",
 "The panda mascot gives a thumbs up and waves goodbye.",
 "记住这四个词，下期见！"),
]
