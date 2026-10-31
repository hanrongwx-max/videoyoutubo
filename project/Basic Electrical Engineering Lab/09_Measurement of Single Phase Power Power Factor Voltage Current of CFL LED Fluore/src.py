# 09_Measurement of Single Phase Power Power Factor Voltage Current of CFL LED Fluore 卡通剧本作者源
# 原著版：完全照原片（荧光灯、CFL、LED、白炽灯的电流、电压、功率和功率因数测量：器材、两种功率表、电路、功率表常数、步骤、读数、结论），K1–K17，
# 不加补充知识点、不做本土化和更正（保留“LED 和 CFL 用低功率因数表、白炽灯和荧光灯用单位功率因数表”、红线相线黑线零线、通电时贴近接线柱用手指点读数）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '电工实验：测灯具的功率与功率因数',
    "edition": "原著版",
    "points": {
        'K1': '实验目的：四种灯的电流功率',
        'K2': '要准备的器材',
        'K3': '按功率因数高低选功率表',
        'K4': '导线先测通断',
        'K5': '看懂电路图',
        'K6': '功率表的四个端子',
        'K7': '功率表常数',
        'K8': '记录数据，算功率因数',
        'K9': '认清台上的灯和表',
        'K10': '万用表拨到交流电压档',
        'K11': '电流回路粗线，电压回路细线',
        'K12': '测量步骤',
        'K13': '读数不歪看，量程对刻度',
        'K14': '测LED灯和节能灯',
        'K15': '分清相线和零线',
        'K16': '结论：哪种灯最省电',
        'K17': '参考教材，有疑问就问',
    },
    "avoid": ['VTU', 'Simplified EEE', 'EEE Studies', "Winner's Capsule", "WINNER'S CAPSULE", 'Kulshreshtha', 'Kulasreshta', 'Automatic Electric', 'BANDICAM', 'McGraw', 'Mc graw'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台前，台上并排放着四盏不同的灯', 'The panda mascot stands in front of an electrical lab bench with four different lamps in a row, waving at the camera.', '今天做电工实验：给四种灯测功率！', '电工实验：测灯具的功率与功率因数'),
('开场', '白炽灯、荧光灯管、节能灯、LED 灯四个图标排成一行', 'Four icons in a row: an incandescent bulb, a straight fluorescent tube, a spiral compact fluorescent bulb and an LED bulb. No people.', '看看哪种灯最费电，哪种最省电。', '', ['白炽灯', '荧光灯', '节能灯', 'LED灯']),
# 情景
('情景', '阿杰在宿舍台灯前犹豫，手里拿着两只不同的灯泡', 'The young male student hesitates in front of a desk lamp in his dorm, holding two different bulbs.', '阿杰想换台灯灯泡，不知道选哪种。'),
('情景', '小研笑着指向实验室里的灯具实验台', 'The female graduate student smiles and points to a lamp test bench in the lab.', '小研说：做个实验，用数据说话。'),
# K1
('K1', '王老师站在实验台旁，四盏灯各连着电表', 'The safety administrator stands beside a bench where four lamps are each connected to analog meters with blank dials.', '本实验要测四种灯的电流和电压。', '实验目的：四种灯的电流功率'),
('K1', '电流、电压、功率、功率因数四个图标', 'Four simple icons: a current arrow, a voltage symbol, a power meter dial and a triangle diagram. No people.', '还要测功率，算出功率因数。', '', ['电流', '电压', '功率', '功率因数']),
# K2
('K2', '器材柜里取出电流表、电压表、功率表', 'An open equipment cabinet with an AC ammeter, an AC voltmeter and a wattmeter, all with blank dials. No people.', '准备交流电流表、电压表和功率表。', '要准备的器材'),
('K2', '数字万用表图标代替电压表，旁边打勾', 'A digital multimeter icon with a blank display placed beside a voltmeter icon, with a green check mark. No people.', '没有电压表，可以用万用表代替。'),
('K2', '四盏灯和一捆连接导线摆在台面上', 'Four lamps and a bundle of connecting wires laid out on a bench. No people.', '再备好四种灯和足够的连接导线。'),
# K3
('K3', '两只外观相同的功率表，一只贴蓝色标签一只贴橙色标签', 'Two identical-looking wattmeters, one with a blank blue tag and one with a blank orange tag. No people.', '功率表有两种，要按灯来选。', '按功率因数高低选功率表', ['UPF', 'LPF']),
('K3', 'LED 灯和节能灯图标连向橙色标签功率表', 'An LED bulb icon and a compact fluorescent bulb icon linked to the orange-tagged wattmeter. No people.', 'LED和节能灯功率因数低，用低功率因数表。'),
('K3', '白炽灯和荧光灯管图标连向蓝色标签功率表', 'An incandescent bulb icon and a fluorescent tube icon linked to the blue-tagged wattmeter. No people.', '白炽灯和荧光灯，用单位功率因数表。'),
# K4
('K4', '小研用万用表两支表笔碰一根未接入电路的导线两端', 'The female graduate student touches the two probes of a multimeter to both ends of an unconnected wire on the bench.', '导线用前，先用万用表测通断。', '导线先测通断'),
('K4', '断线图标打叉，通的导线打勾', 'Two icons: a wire broken inside with a red X, and an intact wire with a green check. No people.', '内部断了的线，挑出来不用。'),
# K5
('K5', '简化电路图：电源、开关、电流表、功率表、灯', 'A simple circuit diagram icon: an AC source, a switch, an ammeter, a wattmeter and a lamp in a loop, with a voltmeter across the lamp. No people.', '接线前，先把电路图看懂。', '看懂电路图'),
('K5', '箭头从电源出发，依次经过开关、电流表、功率表到灯', 'An arrow travels from the AC source through the switch, the ammeter and the wattmeter to the lamp. No people.', '电源经开关，串过电流表和功率表。'),
('K5', '电压表图标并在灯的两端', 'A voltmeter icon connected across the two ends of a lamp icon. No people.', '电压表并在灯两端，测灯的电压。'),
# K6
('K6', '功率表放大图，四个接线柱旁各有一个空白小牌', 'A close-up icon of a wattmeter with four terminals, each marked by a small blank tag. No people.', '功率表有四个接线端。', '功率表的四个端子', ['M 电源端', 'L 负载端', 'C 公共端', 'V 电压端']),
('K6', '电流线圈串在回路里，电压线圈跨在负载上', 'An icon showing a thick current coil placed in series in the loop and a thin voltage coil connected across the load. No people.', '电流线圈串进回路，电压线圈跨在负载上。'),
# K7
('K7', '老周在空白白板前画分数线，只有符号没有文字', 'The older man stands at a blank whiteboard drawing a fraction line with simple symbols, no words.', '用功率表前，先算功率表常数。', '功率表常数', ['电压量程×电流量程', '×功率因数÷满格数']),
('K7', '表盘指针指在一格刻度上，旁边一个乘号和数字 2', 'A wattmeter dial icon with the needle on a mark, next to a multiplication sign and the number 2. No people.', '读数乘常数，才是真实功率。', '', ['10格×2=20瓦']),
('K7', '欣欣竖起手指提醒', 'The panda mascot raises one finger as a reminder.', '换了量程，常数也要重新算。'),
# K8
('K8', '一张空白记录表，四行四种灯的图标', 'A blank data table with four rows, each row starting with a lamp icon, and empty columns. No people.', '每种灯的电压、电流、功率都记下来。', '记录数据，算功率因数', ['电压', '电流', '功率', '功率因数']),
('K8', '功率除以电压乘电流的图示', 'A simple diagram: a power icon divided by a voltage icon multiplied by a current icon. No people.', '功率因数等于功率除以电压乘电流。', '', ['P÷(U×I)']),
('K8', '有功功率与视在功率两根长短不同的柱', 'Two bars side by side, a shorter one for real power and a taller one for apparent power. No people.', '就是有功功率和视在功率之比。', '', ['有功', '视在']),
('K8', '刻度尺最高处标着 1', 'A vertical scale with its top mark highlighted as 1. No people.', '功率因数最大就是一。'),
# K9
('K9', '实验台全景，灯和表旁各插一面编号小旗', 'A wide view of the lab bench with four lamps and three meters, each with a small numbered flag from 1 to 7. No people.', '先认清台上的四盏灯和三块表。', '认清台上的灯和表', ['1-4 灯', '5 电流表', '6 功率表', '7 电压表']),
# K10
('K10', '手把万用表旋钮拨到交流电压档，屏幕空白', "A hand turns a multimeter's rotary switch to the AC voltage range; the display is blank. No people.", '万用表当电压表，一定先拨到交流电压档。', '万用表拨到交流电压档'),
('K10', '万用表并在灯两端', 'A multimeter connected across a lamp holder in place of a voltmeter. No people.', '再把它并在灯的两端。'),
# K11
('K11', '一粗一细两根导线并排', 'A thick connecting wire and a thin connecting wire side by side. No people.', '电流回路用粗线，电压回路用细线。', '电流回路粗线，电压回路细线', ['电流回路：粗', '电压回路：细']),
# K12
('K12', '阿杰对照电路图在灯具面板上接线', 'The young male student connects wires on an open lamp panel following a circuit diagram.', '按电路图接好线，选好要测的那盏灯。', '测量步骤'),
('K12', '阿杰合上电源，白炽灯亮起', 'The young male student switches on the supply and the incandescent bulb lights up.', '合上电源，灯亮了。'),
('K12', '小研依次看电压表、功率表、电流表，并在空白表格上记录', 'The female graduate student reads the voltmeter, wattmeter and ammeter in turn and writes in a blank table.', '依次读电压、功率、电流，记进表格。'),
('K12', '阿杰拉下电源开关，灯熄灭', 'The young male student switches off the supply and the bulb goes dark.', '读完断开电源，再测下一盏灯。'),
# K13
('K13', '侧面歪着看表盘的眼睛图标打叉，正对表盘的打勾', 'Two icons: an eye viewing a meter dial from the side with a red X, and an eye directly in front with a green check. No people.', '读指针表要正对表盘，避免视差。', '读数不歪看，量程对刻度'),
('K13', '老周通电时用手指贴近功率表接线柱，指着表盘读数', 'With the circuit powered, the older man points his finger close to the wattmeter terminals while reading the dial.', '选哪个量程，就读哪排刻度。', '', ['小量程→下排', '大量程→上排']),
# K14
('K14', 'LED 灯亮起，旁边接的是低功率因数功率表', 'An LED bulb is lit on the bench, connected to the wattmeter with the orange label.', '测LED灯，换上低功率因数功率表。', '测LED灯和节能灯'),
('K14', '电流表指针只偏转一点点', 'An ammeter dial with the needle moved only slightly from zero. No people.', 'LED的电流很小，读数要仔细。'),
('K14', '节能灯亮起，小研记录读数', 'A spiral compact fluorescent bulb is lit; the female graduate student records readings on a blank sheet.', '节能灯同样步骤，读完断电。'),
# K15
('K15', '电源引线两根，一根红线一根黑线', 'Two supply leads on the bench, one red and one black. No people.', '电源两根线，要分清相线和零线。', '分清相线和零线', ['红：相线', '黑：零线']),
('K15', '老周指着红线和黑线说明', 'The older man points at the red lead and then the black lead while explaining.', '演示里，红线接相线，黑线接零线。'),
# K16
('K16', '四盏灯下方柱形：白炽灯最高，LED 最低', 'Four lamp icons with bars beneath them: the incandescent bar is tallest and the LED bar is shortest. No people.', '结果：白炽灯最费电，LED最省电。', '结论：哪种灯最省电'),
('K16', '白炽灯冒出热浪图标，只有少量光线', 'An incandescent bulb icon radiating large heat waves and only a few light rays. No people.', '白炽灯的电能大多变成了热。'),
('K16', '阿杰在宿舍台灯里装上 LED 灯泡，满意地笑', 'The young male student screws an LED bulb into his desk lamp in the dormitory and smiles.', '阿杰决定：台灯换成LED灯。'),
# K17
('K17', '一本空白封面的电工教材和一只举起的手', 'A textbook with a blank cover next to a raised hand icon. No people.', '课后对照教材复习，有疑问就问。', '参考教材，有疑问就问'),
# 小结
('小结', '四盏灯和两种功率表图标', 'Icons of four lamps and two wattmeters with blue and orange tags. No people.', '按灯选功率表，读数乘常数。', '小结'),
('小结', '记录表和柱状图图标', 'A blank record table icon and a bar chart icon. No people.', '算出功率因数，LED最省电。'),
# 结尾
('结尾', '欣欣在实验台前挥手', 'The panda mascot waves in front of the lamp test bench.', '家里照明选LED，下个实验见！'),
]
