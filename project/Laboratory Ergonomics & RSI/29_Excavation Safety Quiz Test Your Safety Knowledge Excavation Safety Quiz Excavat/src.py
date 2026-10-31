# 29_Excavation Safety Quiz Test Your Safety Knowledge Excavation Safety Quiz Excavat 卡通剧本作者源
# 原著版：完全照原片（在线计时开挖测验的演示：10 题限时 10 分钟、80% 通过，演示者快速作答得 50%，
# 结果页显示正确答案），K1–K7，不加补充知识点、不做更正；保留网页要点（证书一般在不同工地都认可）、
# 题目和选项：深基坑支护由专业工程师审批、“1.5 比 1 规则”四个英尺选项（正确答案录屏中看不清，不报）、
# 常见危害土体失稳、进场前现场检查、穿钢头安全鞋；录屏中不可辨认的第 3、4、5、8、9 题不写
# 网站、链接和频道名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "开挖安全测验",
    "edition": "原著版",
    "points": {
        "K1": "测验规则：十题八对才过",
        "K2": "培训、安全会、装备、证书",
        "K3": "深基坑支护由专业工程师审批",
        "K4": "1.5比1规则",
        "K5": "最常见的危害：土体失稳",
        "K6": "进场前先检查",
        "K7": "穿安全鞋，不穿拖鞋",
    },
    "avoid": ["HSE Study Guide", "HSE StudyGuide", "HSE STUDY GUIDE", "hsestudyguide"],
}

SHOTS = [
# 开场
("开场", "欣欣戴安全帽站在沟槽围挡外，向镜头招手",
 "The panda mascot wearing a safety helmet stands outside a trench fence and waves at the camera.",
 "开挖安全小测验，来试一试！", "开挖安全测验"),
# 情景
("情景", "工地办公室里，阿杰坐在电脑前，屏幕空白",
 "In a site office, the young male student sits at a computer with a blank screen.",
 "阿杰要准备公司的开挖安全考试。"),
("情景", "老李站在他身后指着屏幕",
 "The facility engineer stands behind him and points at the screen.",
 "老李说：先读要点，再开始答题。"),
# K2
("K2", "培训课堂、班前会、安全装备图标",
 "Icons of a training class, a toolbox meeting and safety equipment. No people.",
 "开挖作业要培训，开班前安全会。", "培训、安全会、装备、证书"),
("K2", "安全帽、反光背心、法规书图标",
 "Icons of a hard hat, a reflective vest and a rule book. No people.",
 "配好安全装备，跟进最新法规。"),
("K2", "一张空白证书和几处工地图标",
 "A blank certificate next to icons of several different work sites. No people.",
 "网页说，开挖安全证书一般各工地都认。"),
# K1
("K1", "屏幕上十格进度条和倒计时",
 "A screen with a ten-segment progress bar and a countdown timer. No people.",
 "测验十题，限时十分钟，一题约一分钟。", "测验规则：十题八对才过", ["10题", "10分钟"]),
("K1", "上一题按钮亮起",
 "A back button lights up on the screen. No people.",
 "觉得选错了，可以返回去修改。"),
("K1", "倒计时归零，屏幕停住",
 "The countdown reaches zero and the screen freezes. No people.",
 "十分钟一到，测验自动结束。"),
("K1", "阿杰飞快点完，结果页五绿五红",
 "The young male student clicks through quickly; the result screen shows five green and five red boxes.",
 "阿杰快速答完，只得了50%。", "", ["50%"]),
("K1", "进度条在八成处插一面小旗",
 "A progress bar with a flag at four fifths. No people.",
 "要答对八题、达到80%才能过。", "", ["80%通过"]),
("K1", "结果页逐题红绿，旁边重做按钮",
 "The result screen shows each question in red or green, with a restart button. No people.",
 "往下翻能看到每题正确答案，还能重做。"),
# K3
("K3", "深基坑和支护结构剖面",
 "A cross-section of a deep pit with shoring. No people.",
 "第一题：深基坑支护设计谁来审批？", "深基坑支护由专业工程师审批"),
("K3", "工程师、路人、业主家属、工人四个图标",
 "Four icons: an engineer with a helmet, a passerby, a family member and workers. No people.",
 "工程师、路人、业主家属、现场工人。", "", ["专业工程师", "路人", "业主家属", "现场工人"]),
("K3", "工程师图标亮绿",
 "The engineer icon lights up green. No people.",
 "答案：专业工程师。"),
# K4
("K4", "沟槽剖面，旁边量尺",
 "A trench cross-section with a measuring rule beside it. No people.",
 "第二题：“1.5比1规则”是什么意思？", "1.5比1规则"),
("K4", "四张选项卡片",
 "Four option cards with trench and arrow icons. No people.",
 "1.5英尺内免支护？每深1英尺宽1.5英尺？", "", ["1.5英尺内免支护", "深1宽1.5", "宽为深1.5倍", "深不超1.5英尺"]),
("K4", "选项卡片轮流亮起，答案处模糊",
 "The option cards light up in turn; the answer area stays blurred. No people.",
 "宽是深的1.5倍？不超1.5英尺深？"),
("K4", "欣欣摊手，旁边一个问号",
 "The panda mascot shrugs with a question mark icon beside it.",
 "这一题的正确答案，画面上看不清。"),
# K5
("K5", "太阳、咖啡杯、静音、塌方四个图标",
 "Four icons: a hot sun, a coffee cup, a quiet speaker and a collapsing trench wall. No people.",
 "第六题：哪个是开挖的常见危害？", "最常见的危害：土体失稳", ["日晒过多", "缺咖啡", "噪声低", "土体失稳"]),
("K5", "塌方图标亮绿",
 "The collapsing wall icon lights up green. No people.",
 "答案：土体失稳。"),
# K6
("K6", "工地入口",
 "The entrance to an excavation site. No people.",
 "第七题：进入开挖现场前该做什么？", "进场前先检查"),
("K6", "媒体、茶点、闲聊会议、检查四个图标",
 "Four icons: a camera crew, refreshments, a chatting meeting and an inspector with a magnifier. No people.",
 "通知媒体、备茶点、开会聊私事、查隐患。", "", ["通知媒体", "备茶点", "聊私事", "现场检查"]),
("K6", "检查图标亮绿",
 "The inspector icon lights up green. No people.",
 "答案：做现场检查，找出潜在危害。"),
# K7
("K7", "四双鞋：人字拖、运动鞋、钢头鞋、凉鞋",
 "Four pairs of shoes: flip-flops, sneakers, steel-toed boots and sandals. No people.",
 "第十题：开挖工人推荐穿什么鞋？", "穿安全鞋，不穿拖鞋", ["人字拖", "运动鞋", "钢头鞋", "凉鞋"]),
("K7", "钢头鞋亮绿",
 "The steel-toed boots light up green. No people.",
 "答案：钢头安全鞋。"),
# 小结
("小结", "欣欣站在白板前",
 "The panda mascot stands at a whiteboard.",
 "十题十分钟，答对八题才算过。", "小结"),
("小结", "工程师和塌方图标",
 "Icons of an engineer and a collapsing wall. No people.",
 "支护设计找专业工程师，常见危害是失稳。"),
("小结", "检查和钢头鞋图标",
 "Icons of an inspector and steel-toed boots. No people.",
 "进场先检查，脚上穿安全鞋。"),
("小结", "阿杰点下重做按钮",
 "The young male student clicks the restart button.",
 "没过就看答案，再做一遍。"),
# 结尾
("结尾", "欣欣挥手告别",
 "The panda mascot waves goodbye.",
 "开挖小测验到这里，下次见！"),
]
