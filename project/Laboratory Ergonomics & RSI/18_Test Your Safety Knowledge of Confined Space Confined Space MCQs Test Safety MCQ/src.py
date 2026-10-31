# 18_Test Your Safety Knowledge of Confined Space Confined Space MCQs Test Safety MCQ 卡通剧本作者源
# 原著版：完全照原片（10 道有限空间选择题和判断题，读题后给答案），K1–K10，不加补充知识点、不做更正；
# 保留原片答案和数值：定义（D a 和 b）、第 2 题原片未给答案（照录为“未报答案”）、三类检测（D）、空化学品罐也算（错误）、
# 监护人不随同进入（错误）、氧含量低于 19.5% 和高于 23.5% 都可能致命（D）、须有能力经培训者才能进入、先测氧含量（A）、
# IDLH 立即危及生命或健康（B）、无人接替时监护人不能进入施救（错误）
# 频道名和美国机构名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "受限空间安全知识自测",
    "edition": "原著版",
    "points": {
        "K1": "什么是有限空间",
        "K2": "都要办许可吗",
        "K3": "检测三类危害",
        "K4": "空罐也是有限空间",
        "K5": "监护人守在外面",
        "K6": "氧太少太多都致命",
        "K7": "不是谁都能进",
        "K8": "先测氧含量",
        "K9": "IDLH：立即危及生命",
        "K10": "监护人不能独自进去救",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "OSHA", "NIOSH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一个盖着盖板的检修井旁，向镜头招手",
 "The panda mascot stands beside a covered maintenance hatch with a warning sign and waves at the camera.",
 "今天十道题，讲讲有限空间。", "有限空间安全十问"),
("开场", "一行图标：井口、储罐、气体检测仪、监护人",
 "A row of icons: a manhole, a storage tank, a gas detector and an attendant with a radio. No people.",
 "定义、检测、监护、救援，都在题里。", "", ["定义", "检测", "监护", "救援"]),
# 情景
("情景", "厂区地下污水池的检修口打开着",
 "At a plant site, the hatch of an underground wastewater pit is open.",
 "厂区地下的污水池要清理。"),
("情景", "老李拿着工具，准备直接下去",
 "The facility engineer holds tools and leans toward the hatch as if to climb in.",
 "老李想着下去看一眼就上来。"),
("情景", "王老师拦住他，手里拿着气体检测仪",
 "The safety administrator stops him, holding a gas detector.",
 "王老师拦住：这是有限空间，先答十题。"),
# K1
("K1", "井、罐、管道、地下池四个图标",
 "Four icons: a manhole, a tank, a large pipe and an underground pit, each with a narrow opening. No people.",
 "第一题：什么是有限空间？", "什么是有限空间", ["出入口受限", "不宜长期停留"]),
("K1", "狭窄的出入口，一个人形图标侧身才能通过",
 "A narrow opening that a person icon can only pass sideways. No people.",
 "进出口受限，不是给人长期待的地方。"),
("K1", "开阔的房间图标打叉",
 "An icon of a wide open room crossed out with a red X. No people.",
 "开放空间不算，答案D，a和b。", "", ["D a和b"]),
# K2
("K2", "作业许可和印章图标",
 "A blank permit form and a stamp icon. No people.",
 "第二题：所有有限空间都要办许可吗？", "都要办许可吗"),
("K2", "欣欣摊手，旁边一个问号",
 "The panda mascot shrugs with a question mark icon beside it.",
 "这一题，原片只读了题，没报答案。"),
# K3
("K3", "检测仪屏幕上三个图标：氧气、火焰、骷髅",
 "A gas detector display showing three icons: an oxygen symbol, a flame and a skull. No people.",
 "第三题：必须检测哪几类？", "检测三类危害", ["氧含量", "可燃气体", "有毒气体"]),
("K3", "王老师把检测仪探头伸进井口",
 "The safety administrator lowers a gas detector probe into the hatch.",
 "氧含量、可燃气、有毒气，答案D。", "", ["D 以上都是"]),
# K4
("K4", "一个空储罐，罐口敞开",
 "An empty chemical storage tank with its top hatch open. No people.",
 "第四题：空的化学品罐，算不算？", "空罐也是有限空间"),
("K4", "空罐图标打勾",
 "The empty tank icon gets a green check as a confined space. No people.",
 "说不算是错误的，空罐也是有限空间。", "", ["错误"]),
# K5
("K5", "阿杰站在井口外，手拿对讲机，盯着下面",
 "The young male student stands outside the hatch holding a radio, watching inside.",
 "第五题：监护人要跟着下去吗？", "监护人守在外面"),
("K5", "两个人都下去、上面没人的图标打红叉",
 "An icon of two people inside a pit with nobody outside, crossed out with a red X. No people.",
 "答案：错误，监护人不随同进入。", "", ["错误"]),
# K6
("K6", "氧气瓶图标的刻度条，两端都是红色",
 "A gauge bar for oxygen level with red zones at both the low end and the high end and green in the middle. No people.",
 "第六题：氧含量怎样会致命？", "氧太少太多都致命"),
("K6", "低端红区：人形图标晕倒",
 "In the low red zone, a person icon collapses. No people.",
 "低于19.5%，进去可能致命；", "", ["＜19.5%"]),
("K6", "高端红区亮起",
 "The high red zone of the gauge bar lights up. No people.",
 "高于23.5%，同样有问题。答案D。", "", ["＞23.5%", "D"]),
# K7
("K7", "一名路过的人想下井，被拦住",
 "A passer-by icon tries to climb into the hatch and is stopped by a barrier. No people.",
 "第七题：谁都能进去维修吗？", "不是谁都能进"),
("K7", "老李出示培训合格卡",
 "The facility engineer shows a blank training certificate card.",
 "错误，进入者要有能力、经过培训。", "", ["错误"]),
# K8
("K8", "检测仪上氧气图标先亮起",
 "On the gas detector, the oxygen icon lights up first. No people.",
 "第八题：先测什么？", "先测氧含量"),
("K8", "欣欣竖起一根手指",
 "The panda mascot raises one finger.",
 "答案A，进入前首先检测氧含量。", "", ["A 氧含量"]),
# K9
("K9", "检测仪屏幕上出现红色警报",
 "A gas detector screen flashes a red alarm. No people.",
 "第九题：IDLH是什么意思？", "IDLH：立即危及生命"),
("K9", "警示三角和心跳线",
 "A warning triangle next to a heartbeat line that drops. No people.",
 "答案B，立即危及生命或健康。", "", ["B"]),
# K10
("K10", "井下的人倒下，阿杰想往下冲",
 "An icon of a person collapsed inside a pit while the attendant leans to jump in. No people.",
 "第十题：监护人能独自进去救人吗？", "监护人不能独自进去救"),
("K10", "欣欣摇头",
 "The panda mascot shakes its head firmly.",
 "答案：错误，没人接替就不能进去。", "", ["错误"]),
# 小结
("小结", "欣欣站在井口旁的白板前",
 "The panda mascot stands at a whiteboard beside the hatch.",
 "出入受限、不为久留，就是有限空间。", "小结"),
("小结", "检测仪：氧气、火焰、骷髅图标",
 "A gas detector showing an oxygen symbol, a flame and a skull. No people.",
 "测氧、可燃、有毒，先测氧含量。"),
("小结", "氧含量刻度条两端红区",
 "The oxygen gauge bar with red zones at both ends. No people.",
 "低于19.5%或高于23.5%都危险。", "", ["19.5%", "23.5%"]),
("小结", "阿杰守在井口",
 "The young male student stands guard at the hatch with a radio.",
 "监护人不随同进入，没人接替不下去。"),
# 结尾
("结尾", "欣欣在盖好的井口旁挥手告别",
 "The panda mascot waves goodbye beside the closed hatch.",
 "有限空间十问到这里，下次见！"),
]
