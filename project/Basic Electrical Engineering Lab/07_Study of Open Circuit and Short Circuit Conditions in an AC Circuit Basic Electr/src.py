# 07_Study of Open Circuit and Short Circuit Conditions in an AC Circuit Basic Electr 卡通剧本作者源
# 原著版：完全照原片（两灯串联、电流表加开关短接灯 1 的开路与短路实验：器材、电源、接线、读数、口试题、结论），K1–K15，
# 不加补充知识点、不做本土化和更正（保留 100 W/230 V 灯、230 V 50 Hz 与 5 A 熔断器、0–300 V 与 0–1/0–2 A 量程、实测约 112–114 V 和 0.41–0.42 A、口试题“短路时为什么一盏灯变暗”、讲者戴腕表徒手扳开关）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '交流电路的开路与短路',
    "edition": "原著版",
    "points": {
        'K1': '实验目的',
        'K2': '所需器材',
        'K3': '电源与熔断器',
        'K4': '用带插头的导线',
        'K5': '两灯串联的主回路',
        'K6': '电流表和开关组成短路支路',
        'K7': '电压表并在灯 1 两端',
        'K8': '先串联，后并联',
        'K9': '认识实物',
        'K10': '通电时开关先断开',
        'K11': '先看量程再读数',
        'K12': '开路：电压高，电流零',
        'K13': '短路：电流大，电压零',
        'K14': '口试常问',
        'K15': '结果与结论',
    },
    "avoid": ['VTU', 'Visvesvaraya', '18ELEL27', 'BEE LAB', 'Screencast', 'SCREENCAST-O-MATIC', 'Automatic Electric'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台旁，台上两盏灯泡、一只电流表、一只电压表，向镜头招手', 'The panda mascot stands beside a lab bench with two light bulbs on a wiring board, an analog ammeter and an analog voltmeter, waving at the camera.', '这一课做交流电路的开路与短路实验。', '交流电路的开路与短路'),
('开场', '断开的电路和被短接的电路两个图标', 'Two icons: a circuit with a gap, and a circuit with a wire bridging across a lamp. No people.', '开路和短路，到底有什么不同？', '', ['开路', '短路']),
# 情景
('情景', '阿杰翻着空白课本，指着开路和短路两个词发愁', 'The young male student flips through a blank textbook, frowning at two circuit icons: an open gap and a bridged load.', '阿杰总分不清开路和短路。'),
('情景', '小研指向实验台上的两盏灯和两只表', 'The female graduate student points to two lamps and two meters on the lab bench.', '小研说：做一遍实验，看看表就明白。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '一起来研究开路和短路的影响。'),
# K1
('K1', '欣欣指着开路、短路两个图标', 'The panda mascot points at the open circuit icon and the short circuit icon.', '目的：观察开路和短路时电压电流的变化。', '实验目的'),
# K2
('K2', '实验台上：交流电流表、交流电压表、两盏白炽灯、一个单极开关', 'On the bench: an AC ammeter, an AC voltmeter, two incandescent bulbs and a single-pole switch. No people.', '器材：交流电流表、电压表，都是动铁式。', '所需器材', ['交流电流表', '交流电压表', '白炽灯×2', '单极开关']),
('K2', '两盏灯泡旁空白铭牌', 'Two incandescent bulbs with blank nameplates beside them. No people.', '白炽灯两只，一百瓦、二百三十伏。', '', ['100 W', '230 V']),
('K2', '电压表旁边一只万用表打问号', 'A voltmeter next to a multimeter with a small question mark. No people.', '没有电压表，可以用万用表代替。'),
# K3
('K3', '接线板上的电源区：一个双极开关和一个熔断器', 'The supply section of a patch board: a double-pole switch and a fuse. No people.', '单相交流电，二百三十伏、五十赫兹。', '电源与熔断器', ['230 V 50 Hz']),
('K3', '相线和中性线从熔断器和开关后引出到插孔', 'Live and neutral lines lead out from the fuse and switch to two sockets on the board. No people.', '经双极开关和五安熔断器引出相线、中性线。', '', ['5 A 熔断器', '相线', '中性线']),
# K4
('K4', '两端带插头的连接导线打绿勾，两根裸线头打红叉', 'Two icons: a connecting lead with proper plugs on both ends with a green check, and two bare wire ends crossed out with a red X. No people.', '连接导线要带合适的插头，不用裸线头。', '用带插头的导线'),
# K5
('K5', '电路图：相线接灯 1，灯 1 接灯 2，灯 2 接中性线', 'A circuit diagram icon: the line wire goes to lamp one, lamp one to lamp two, and lamp two to the neutral wire. No people.', '相线接灯一，灯一接灯二，灯二接零线。', '两灯串联的主回路', ['灯1', '灯2']),
('K5', '两盏灯首尾相连成一串', 'Two lamp icons connected end to end in a single series loop. No people.', '两盏灯串联，构成主回路。'),
# K6
('K6', '从灯 1 前端引线到电流表，再到开关，回到灯 1 后端', 'The diagram highlights a branch: from the front of lamp one through an ammeter and a switch back to the back of lamp one. No people.', '电流表和开关串起来，跨接在灯一两端。', '电流表和开关组成短路支路', ['电流表', '开关S1']),
('K6', '支路导线画得比主回路粗', 'The branch wire drawn thicker than the main loop wires. No people.', '这条支路用粗一点的导线。'),
('K6', '开关后端接到灯 1 后端或灯 2 前端，两点用同色圆点标出', 'The diagram marks the back of lamp one and the front of lamp two with the same colored dot. No people.', '接灯一后端或灯二前端，都是同一点。'),
# K7
('K7', '电压表用细导线并接在灯 1 两端', 'A voltmeter connected with thin wires across lamp one. No people.', '电压表用细线，并在灯一两端。', '电压表并在灯 1 两端'),
('K7', '电压表和电流表的量程旋钮各指向一个挡', 'Range terminals on the voltmeter and ammeter highlighted. No people.', '电压表选三百伏，电流表选一安或两安。', '', ['0–300 V', '0–1 A / 0–2 A']),
# K8
('K8', '先画出串联回路，再加上并联支路的两步图', 'Two step icons: first the series loop drawn, then the parallel branch added. No people.', '接线顺序：先接串联，后接并联。', '先串联，后并联', ['第1步 串联', '第2步 并联']),
# K9
('K9', '接线板上两盏灯、开关、两只表的实物', 'The real setup on the bench: two bulbs, a switch, an ammeter and a voltmeter connected with plug leads. No people.', '实物就是这样：两盏灯，一开关，两只表。', '认识实物'),
# K10
('K10', '开关 S1 处于断开位置，打绿勾', 'A close-up of switch S1 in the off position with a green check. No people.', '通电时，开关 S1 必须先断开。', '通电时开关先断开', ['S1 断开']),
# K11
('K11', '电压表接线柱被圈出，箭头指向下刻度', "The voltmeter's connected terminal circled, an arrow pointing to the lower scale on the dial. No people.", '先看表接在哪个量程，读对应刻度。', '先看量程再读数'),
('K11', '表盘一段放大，数小格', 'A magnified section of the dial showing small divisions between two numbered marks. No people.', '再数小格，算出读数。'),
# K12
('K12', 'S1 断开，灯 1 发亮', 'Switch S1 open; lamp one glows. No people.', 'S1 断开，这就是开路状态，灯一亮着。', '开路：电压高，电流零'),
('K12', '电压表指针偏转较大', 'The voltmeter needle deflects well up the scale. No people.', '电压表读数约一百一十二到一百一十四伏。', '', ['约112–114 V']),
('K12', '电流表指针停在零', 'The ammeter needle stays at zero. No people.', '电流表读数为零。', '', ['0 A']),
('K12', '欣欣举着开路卡片：电压高，电流零', 'The panda mascot holds up a card with an open circuit icon.', '开路：电压高，电流为零。', '', ['电压 高', '电流 零']),
# K13
('K13', '老周戴着腕表，徒手扳下开关 S1，灯 1 熄灭', 'The older man, wearing a metal wristwatch, flips switch S1 on the patch board bare-handed; lamp one goes dark.', '闭合 S1，灯一被短接，熄灭了。', '短路：电流大，电压零'),
('K13', '电流表指针偏转', 'The ammeter needle deflects. No people.', '电流表读数约零点四一到零点四二安。', '', ['约0.41–0.42 A']),
('K13', '电压表指针回到零', 'The voltmeter needle drops back to zero. No people.', '灯一两端电压变成零。', '', ['0 V']),
('K13', '欣欣举着短路卡片：电流大，电压零', 'The panda mascot holds up a card with a short circuit icon.', '短路：电流大，电压为零。', '', ['电流 大', '电压 零']),
# K14
('K14', '王老师拿着三张空白问题卡', 'The safety administrator holds three blank question cards.', '口试常问三个问题。', '口试常问'),
('K14', '开路和短路两个图标之间一个问号', 'An open circuit icon and a short circuit icon with a question mark between them. No people.', '一问：开路和短路有什么区别？'),
('K14', '两盏灯，其中一盏变暗，旁边问号', 'Two lamps, one dimmer than the other, with a question mark. No people.', '二问：短路时，为什么一盏灯变暗？'),
('K14', '动铁式和动圈式表芯剖面', 'Cutaway icons of a moving iron and a moving coil meter movement. No people.', '三问：动铁式和动圈式仪表有何不同？'),
# K15
('K15', '空白结果表，只有开关、亮灯、灭灯图标', 'A blank results table with only switch icons and lamp-on and lamp-off icons in the cells. No people.', '把开关状态、电压、电流、灯的状态填进表。', '结果与结论'),
('K15', '开路和短路两张卡片并排', 'The open circuit card and the short circuit card side by side. No people.', '开路电压大电流零，短路电流大电压零。'),
# 小结
('小结', '开路和短路两张卡片', 'Two cards: an open circuit icon and a short circuit icon. No people.', '开路电压大电流零，短路电流大电压零。', '小结'),
('小结', '串联主回路和并联支路的接线顺序图标', 'Icons showing the wiring order: series main loop first, then the parallel branch. No people.', '带插头导线，先串后并，S1 先断开。'),
('小结', '表盘上下两条刻度和一个放大镜', 'A meter dial with upper and lower scales and a magnifying glass. No people.', '看清量程再读数，记好结果表。'),
# 结尾
('结尾', '欣欣在实验台前挥手道别', 'The panda mascot waves goodbye in front of a lab bench with two lamps and two meters.', '分清开路和短路，下次见！'),
]
