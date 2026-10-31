# 38_BIORISK ASSESSMENT 卡通剧本作者源（原著版）
# 原片为 MOOC 第六讲（16 分 28 秒，CC-BY）：已知病原的微生物风险评估——评估判据、两套是/否问卷、
# 病原安全数据资料九节模板，冰山类比说明评估范围。
# 原著版：完全照原片，保留全部知识点 K1–K29，不补充知识点、不做本土化；
# 病原保持匿名，不补充病原特性，基因改造只作中性提示、不列任何性状；
# 在线病原资料为原片所述的国外在线资源，按原片中性转述（具体名称入 avoid）。
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字。

META = {
    "title": "风险评估怎么做",
    "edition": "原著版",
    "points": {
        "K1": "只评已知病原",
        "K2": "本讲三个目标",
        "K3": "学完能做到的事",
        "K4": "评估有范围：冰山",
        "K5": "评估看哪些判据",
        "K6": "致病性与感染剂量",
        "K7": "暴露后果有多重",
        "K8": "感染途径有哪些",
        "K9": "在环境里能活多久",
        "K10": "浓度与培养量",
        "K11": "有没有宿主或媒介",
        "K12": "先查别人的研究",
        "K13": "哪些操作易暴露",
        "K14": "有没有做过改造",
        "K15": "有没有预防或治疗",
        "K16": "一病原一评估",
        "K17": "病原特性问卷",
        "K18": "设施与管理问卷",
        "K19": "病原资料可查可用",
        "K20": "资料第一节：是谁",
        "K21": "第二节：危害识别",
        "K22": "第三节：怎么传播",
        "K23": "第四节：能不能杀灭",
        "K24": "第五节：急救与医学",
        "K25": "第六节：实验室危害",
        "K26": "第七节：防护级别",
        "K27": "第八节：操作与储存",
        "K28": "第九节：法规信息",
        "K29": "小结回顾",
    },
    "avoid": ["UMS", "Universiti Malaysia Sabah", "Malaysia", "Kenneth", "Rodrigues",
              "Commonwealth of Learning", "COL", "Biotechnology Research Institute", "BRI", "MOOC",
              "OHSAS", "Canada", "PSDS", "WHO"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一张空白评估表前",
 "The panda mascot stands in front of a blank assessment form.",
 "这一课，学会给病原做评估。", "风险评估怎么做"),
("开场", "欣欣举起一张问卷和一本资料册",
 "The panda mascot holds up a questionnaire and a data booklet. No people.",
 "一张问卷，一本资料，就够用。"),
# 情景
("情景", "阿杰拿着一支不明样本发愁",
 "The young male student looks puzzled at an unlabelled sample tube.",
 "阿杰问：这管样本怎么评估？"),
("情景", "小研摇头，指着样本上的问号",
 "The female graduate student shakes her head, pointing at a question mark on the tube.",
 "小研说：不认识，就评不了。"),
("情景", "王老师递来一份已知病原的资料卡",
 "The safety administrator hands over a known-pathogen data card.",
 "王老师：先弄清它是谁。"),
# K1
("K1", "欣欣把已知样本放进评估框，未知的挡在外面",
 "The panda mascot puts a known sample into an assessment box; an unknown one stays outside.",
 "风险评估，只评已知病原。", "只评已知病原"),
("K1", "未知样本旁边一个大问号",
 "An unknown sample beside a large question mark. No people.",
 "不知道是谁，风险就看不清。"),
# K2
("K2", "三个目标图标竖排点亮",
 "Three objective icons light up in a column. No people.",
 "本讲三个目标：", "本讲三个目标", ["会评估流程", "抓住要点", "会查资料"]),
# K3
("K3", "三个对勾方框依次打勾",
 "Three check boxes get ticked one by one. No people.",
 "学完能编问卷、本地化、用资料。", "学完能做到的事"),
# K4
("K4", "一座冰山，水上一角水下一大块",
 "An iceberg with a small tip above water and a large mass below. No people.",
 "评估有范围：看得见的在水上。", "评估有范围：冰山"),
("K4", "水下部分标着看不见的风险",
 "The underwater part marked as unseen risk. No people.",
 "看不见的风险，在水面之下。"),
# K5
("K5", "欣欣展开一张判据清单",
 "The panda mascot unfolds a criteria checklist.",
 "评估要看一串判据。", "评估看哪些判据"),
# K6
("K6", "一个病原图标配一支小剂量滴管",
 "A pathogen icon beside a small-dose dropper. No people.",
 "一看致病性，二看感染剂量。", "致病性与感染剂量"),
# K7
("K7", "一个从轻到重的后果刻度条",
 "A severity scale bar from light to heavy. No people.",
 "暴露后果有多重，要掂量。", "暴露后果有多重"),
# K8
("K8", "鼻、口、手三个途径图标",
 "Three route icons: nose, mouth, hand. No people.",
 "自然途径加操作途径，都要查。", "感染途径有哪些"),
# K9
("K9", "一个病原图标配一个时钟",
 "A pathogen icon beside a clock. No people.",
 "它在环境里能活多久？", "在环境里能活多久"),
# K10
("K10", "一支小试管旁边一个大培养瓶",
 "A small tube beside a large culture flask. No people.",
 "浓度高、量大，风险也涨。", "浓度与培养量"),
# K11
("K11", "一个动物图标和一个昆虫图标",
 "An animal icon and an insect icon. No people.",
 "有没有宿主或媒介帮它传？", "有没有宿主或媒介"),
# K12
("K12", "一摞打开的文献和报告",
 "A stack of open papers and reports. No people.",
 "先查别人的研究，拿到依据。", "先查别人的研究"),
# K13
("K13", "移液、离心、提取三个操作图标",
 "Three operation icons: pipetting, a centrifuge, an extraction tube. No people.",
 "哪些操作易产生暴露，标出来。", "哪些操作易暴露", ["移液", "离心", "提取"]),
# K14
("K14", "一个病原图标旁打一个问号标签",
 "A pathogen icon with a question-mark tag. No people.",
 "有没有做过基因改造？要问。", "有没有做过改造"),
# K15
("K15", "一个疫苗瓶和一盒药，旁边问号",
 "A vaccine vial and a medicine box with a question mark. No people.",
 "当地有没有预防或治疗？", "有没有预防或治疗"),
# K16
("K16", "两个不同病原图标，各配一张表",
 "Two different pathogen icons, each with its own form. No people.",
 "一个病原，一份评估，不能套。", "一病原一评估"),
# K17
("K17", "一张是非问卷，右边两列打勾叉",
 "A yes-no questionnaire with two tick-cross columns. No people.",
 "病原问卷：是或否，逐条答。", "病原特性问卷", ["是否致病", "是否发病", "是否可治"]),
# K18
("K18", "另一张问卷，列着设施与管理项",
 "Another questionnaire listing facility and management items. No people.",
 "再问设施与管理：", "设施与管理问卷", ["培训", "应急", "设施", "防护"]),
("K18", "问卷后两项打勾：处置、安保",
 "The last items ticked: disposal and security. No people.",
 "还有废物处置、安保和规程。", "", ["处置", "安保", "规程"]),
# K19
("K19", "一台平板和一部手机显示空白资料页",
 "A tablet and a phone showing blank data pages. No people.",
 "病原资料网上可查，有手机版。", "病原资料可查可用"),
# K20
("K20", "资料封面第一节：一个身份图标",
 "The data sheet cover, section one: an identity icon. No people.",
 "第一节：这病原是谁。", "资料第一节：是谁"),
# K21
("K21", "第二节：危害识别图标",
 "Section two: a hazard-identification icon. No people.",
 "第二节：危害识别，有多凶。", "第二节：危害识别"),
# K22
("K22", "第三节：传播箭头图标",
 "Section three: a transmission-arrow icon. No people.",
 "第三节：怎么传，谁来传。", "第三节：怎么传播"),
# K23
("K23", "第四节：消毒与加热灭活图标",
 "Section four: a disinfectant and heat-inactivation icon. No people.",
 "第四节：能不能杀灭，会不会耐药。", "第四节：能不能杀灭"),
# K24
("K24", "第五节：急救与听诊器图标",
 "Section five: a first-aid and stethoscope icon. No people.",
 "第五节：急救、疫苗、用药。", "第五节：急救与医学"),
# K25
("K25", "第六节：实验室危害标志",
 "Section six: a laboratory-hazard sign. No people.",
 "第六节：实验室里的危害。", "第六节：实验室危害"),
# K26
("K26", "第七节：防护服与危害组标尺",
 "Section seven: protective clothing beside a risk-group scale. No people.",
 "第七节：按危害组定防护级别。", "第七节：防护级别"),
# K27
("K27", "第八节：溢洒、处置、冷藏三图标",
 "Section eight: a spill, a disposal bin, a fridge. No people.",
 "第八节：溢洒、处置、储存。", "第八节：操作与储存", ["溢洒", "处置", "储存"]),
# K28
("K28", "第九节：法规卷宗与对勾清单",
 "Section nine: a regulations folder and a checklist. No people.",
 "第九节：法规和编写信息。", "第九节：法规信息"),
# 小结
("小结", "欣欣身旁：冰山、问卷、资料册",
 "The panda mascot beside an iceberg, a questionnaire and a data booklet.",
 "评估分范围，问卷加资料。", "小结回顾"),
("小结", "问卷九节、一病原一评估两图标",
 "Two icons: a nine-section booklet and one form per pathogen. No people.",
 "一病原一评估，九节问一遍。"),
# K29
("K29", "小研照着问卷给一份样本逐项打钩",
 "The female graduate student ticks a questionnaire for a sample item by item.",
 "照着九节问一遍，评估就成形。", "小结回顾"),
# 结尾
("结尾", "欣欣挥手，身后资料册发亮",
 "The panda mascot waves goodbye with a glowing data booklet behind.",
 "评估做扎实，我们下次见！"),
]
