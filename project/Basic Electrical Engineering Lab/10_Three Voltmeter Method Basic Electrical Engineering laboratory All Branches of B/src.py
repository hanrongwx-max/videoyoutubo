# 10_Three Voltmeter Method Basic Electrical Engineering laboratory All Branches of B 卡通剧本作者源
# 原著版：完全照原片（三电压表法测扼流线圈的电阻和电感：器材、电路、接线顺序、步骤、读数、回零断电、计算公式），K1–K16，
# 不加补充知识点、不做本土化和更正（保留器材表 0–1 A、50 Ω/3 A 与电路图 0–5 A、100 Ω/3 A 的不一致，“调压器电压随意取”，通电时单手转调压器）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '电工实验：三电压表法测线圈',
    "edition": "原著版",
    "points": {
        'K1': '三电压表法测什么',
        'K2': '要准备的器材',
        'K3': '导线先测通断',
        'K4': '电路怎么连',
        'K5': '交流电路用交流表',
        'K6': '先接串联，后并电压表',
        'K7': '实验四步走',
        'K8': '认识实验台，四个读数',
        'K9': '调电压，读一组记一组',
        'K10': '多测几组，各自计算',
        'K11': '先回零，再断电',
        'K12': '数据表格',
        'K13': '功率因数公式',
        'K14': '阻抗三角形求电阻感抗',
        'K15': '由感抗求电感',
        'K16': '参考教材，有疑问就问',
    },
    "avoid": ['VTU', 'Simplified EEE', 'EEE Studies', 'KINEMASTER', 'KineMaster', 'BANDICAM', 'Kulshreshtha', 'Kulasreshta'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台前，台上有一个铁心线圈和三块电压表', 'The panda mascot stands at an electrical lab bench with an iron-core coil and three analog voltmeters with blank dials, waving at the camera.', '今天用三块电压表，摸清一个线圈！', '电工实验：三电压表法测线圈'),
('开场', '线圈图标旁有两个问号：电阻和电感', 'An iron-core coil icon with two question mark bubbles beside it. No people.', '它的电阻多大？电感多大？', '', ['电阻？', '电感？']),
# 情景
('情景', '阿杰拿着一个扼流线圈翻看，一脸疑惑', 'The young male student turns an iron-core choke coil over in his hands, looking puzzled.', '阿杰拿着线圈：这东西怎么量？'),
('情景', '小研指着桌上三块电压表微笑', 'The female graduate student smiles and points at three voltmeters on the bench.', '小研说：三块电压表就能算出来。'),
# K1
('K1', '王老师在空白黑板前，旁边是线圈图标', 'The safety administrator stands at a blank blackboard next to a large coil icon.', '三电压表法，专门测线圈的电阻和电感。', '三电压表法测什么'),
('K1', '线圈内部画成一个电阻加一个电感串联', 'A coil icon opened up to show a small resistor and an inductor symbol in series inside. No people.', '线圈可以看成电阻和电感串在一起。', '', ['电阻 r', '电感 L']),
# K2
('K2', '台上摆着线圈、三块电压表、一块电流表', 'A choke coil, three AC voltmeters and one AC ammeter laid out on a bench. No people.', '准备线圈、三块交流电压表、一块电流表。', '要准备的器材'),
('K2', '滑线变阻器和一捆导线，旁边空白铭牌', 'A slide-wire rheostat with a blank nameplate and a bundle of connecting wires. No people.', '器材表写：电流表一安，变阻器五十欧三安。', '', ['0–1 A', '50 Ω 3 A']),
('K2', '电表表盘特写，指针式动铁结构图标', 'A meter dial close-up with a moving iron mechanism icon. No people.', '电表都用交流动铁式，变阻器作限流电阻。'),
# K3
('K3', '小研用万用表通断档逐根测导线，屏幕空白', 'The female graduate student tests each unconnected wire with a multimeter set to continuity; the display is blank.', '导线先用万用表通断档测一遍。', '导线先测通断'),
# K4
('K4', '简化电路图：电源、熔断器、调压器', 'A simple circuit diagram icon: AC supply, fuse and single-phase variable autotransformer. No people.', '单相交流电源经熔断器，接到调压器上。', '电路怎么连', ['电源', '熔断器', '调压器']),
('K4', '调压器后面，电流表、电阻、线圈串成一串，旁边标数', 'After the autotransformer, an ammeter, a resistor and a coil connected in series, with small rating tags. No people.', '电流表、电阻、线圈串成一路。', '', ['0–5 A', '100 Ω 3 A']),
('K4', '三个电压表图标分别跨在总电压、电阻、线圈上', 'Three voltmeter icons connected across the total supply, the resistor and the coil. No people.', '三块电压表：测总电压、电阻、线圈。', '', ['V1 总电压', 'V2 电阻', 'V3 线圈']),
('K4', '箭头沿串联回路流过，电流处处相同', 'Arrows flow around the series loop, equal everywhere. No people.', '串联回路里，电流处处一样大。'),
# K5
('K5', '表盘上画波浪符号的电表打勾，画直线符号的打叉', 'Two meter icons: one with a wave symbol and a green check, one with a straight-line symbol crossed out with a red X. No people.', '交流电路，要用交流电表。', '交流电路用交流表'),
('K5', '老周在电路图里给电表符号旁加一个波浪号', 'The older man draws a small wave symbol next to a meter circle on a blank circuit diagram.', '画图时，交流表要标上交流符号。'),
# K6
('K6', '阿杰先把串联的一路连好，电压表还放在一边', 'The young male student first connects the series chain on the bench while the three voltmeters still sit unconnected aside.', '接线先接串联的那一路。', '先接串联，后并电压表'),
('K6', '最后把电压表一块块并上去', 'The young male student then connects the voltmeters one by one across the parts of the circuit.', '最后再把电压表一块块并上去。', '', ['① 串联', '② 并联']),
# K7
('K7', '四个步骤图标排成一行', 'Four step icons in a row: wiring, switch on, adjust and read, switch off. No people.', '实验步骤：接线、合闸、调压读数、断电。', '实验四步走', ['接线', '合闸', '读数', '断电']),
('K7', '阿杰合上电源开关', 'The young male student closes the supply switch.', '按图接好线，合上电源开关。'),
('K7', '小研转动调压器，在空白记录表上写下读数', 'The female graduate student turns the autotransformer and writes readings in a blank record sheet.', '用调压器改变电压，记下各表读数。'),
('K7', '阿杰拉下电源开关', 'The young male student switches off the supply.', '读完数，断开电源开关。'),
# K8
('K8', '实验台全景，五件器材旁各有编号小旗', 'A wide view of the bench: autotransformer, multimeter, ammeter and two voltmeters, each with a small numbered flag. No people.', '认清调压器、电流表和三块电压表。', '认识实验台，四个读数'),
('K8', '万用表拨到交流电压档，当第一块电压表', 'A multimeter with its dial set to the AC voltage position, connected as the first voltmeter; the display is blank. No people.', '第一块电压表可以用万用表交流档。'),
('K8', '四个空白读数框', 'Four blank reading boxes in a row. No people.', '每次要读四个数。', '', ['V1', 'V2', 'V3', 'I']),
# K9
('K9', '老周通电后单手转动调压器旋钮，镜头贴近接线端子', 'With the circuit powered, the older man turns the autotransformer knob with one hand; the view is close to the exposed terminals.', '合上电源，用调压器加一个电压。', '调电压，读一组记一组'),
('K9', '小研依次看电流表、两块电压表，在空白表格上记录', 'The female graduate student reads the ammeter and two voltmeters in turn and writes in a blank table.', '依次读电流、V2、V3，记下来。'),
('K9', '调压器旋钮再转一点，重复读数', 'The autotransformer knob turns a little further and the readings are taken again. No people.', '再换一个电压，重复一遍。'),
('K9', '老周摊手微笑，旋钮停在任意位置', 'The older man shrugs with a smile; the knob rests at an arbitrary position.', '讲解里说：电压随意取，没有限制。'),
# K10
('K10', '小组四五个人围着表格，每人一行', 'A small group of students around a blank data table, each pointing at a different row.', '多测几组，组里每人各算一组。', '多测几组，各自计算'),
# K11
('K11', '阿杰把调压器旋钮转回零位', 'The young male student turns the autotransformer knob all the way back to the zero position.', '做完了，先把调压器转回零。', '先回零，再断电'),
('K11', '随后拉下电源开关', 'Then he switches off the bench power switch.', '然后再断开电源。', '', ['① 回零', '② 断电']),
# K12
('K12', '一张空白宽表格，表头只有图标', 'A wide blank data table with many columns whose headers are only small icons. No people.', '表格里记电压、电流和计算结果。', '数据表格', ['三个电压', '电流', '功率因数', '阻抗电阻感抗', '电感']),
# K13
('K13', '老周在白板上写分数式，只有字母符号', 'The older man writes a fraction with letter symbols on a whiteboard, no words.', '先算功率因数。', '功率因数公式', ['分子：平方差', '分母：2V2V3']),
('K13', '欣欣比出记住的手势', 'The panda mascot taps its head with a paw as if memorizing.', '公式记住会用，不必现场推导。'),
('K13', '计算器图标显示空白，旁边角度符号', 'A calculator icon with a blank display next to an angle symbol. No people.', '再求出相角和它的正弦。', '', ['φ', 'sinφ']),
# K14
('K14', '直角三角形：斜边阻抗，底边电阻，竖边感抗', 'A right triangle diagram: the long side for impedance, the base for resistance, the vertical side for reactance, with an angle at the corner. No people.', '画出阻抗三角形。', '阻抗三角形求电阻感抗', ['Z', 'r', 'XL']),
('K14', '第三块电压表读数除以电流表读数', 'The third voltmeter icon divided by the ammeter icon, with an equals sign. No people.', '阻抗等于V3除以电流。', '', ['Z=V3÷I']),
('K14', '三角形里的角度标记为相角', 'The angle at the corner of the right triangle highlights. No people.', '三角形里的这个角，就是相角。'),
('K14', '三角形底边和竖边分别高亮', 'The base of the triangle highlights, then the vertical side highlights. No people.', '电阻乘余弦，感抗乘正弦。', '', ['r=Z·cosφ', 'XL=Z·sinφ']),
# K15
('K15', '感抗图标除以一个旋转的圆圈符号', 'A reactance icon divided by a spinning circle symbol for angular frequency. No people.', '电感等于感抗除以角频率。', '由感抗求电感', ['L=XL÷(2πf)']),
('K15', '小研在表格最后一栏填好数字，打勾', 'The female graduate student fills in the last column of a blank table and adds a green check mark.', '频率用电源频率，电感就求出来了。'),
# K16
('K16', '空白封面教材和一只举起的手', 'A textbook with a blank cover next to a raised hand icon. No people.', '课后对照教材复习，有疑问就问。', '参考教材，有疑问就问'),
# 小结
('小结', '线圈、三块电压表、电流表图标', 'Icons of a choke coil, three voltmeters and an ammeter. No people.', '三块电压表加电流表，测出线圈参数。', '小结'),
('小结', '公式卡片和三角形图标', 'A formula card icon and an impedance triangle icon. No people.', '先算功率因数，再用三角形求解。'),
('小结', '调压器旋钮回零和断开的开关两个图标', 'Two icons: an autotransformer knob back at zero and an open supply switch. No people.', '做完先回零，再断电。'),
# 结尾
('结尾', '欣欣在调压器回零的实验台前挥手', 'The panda mascot waves in front of a lab bench with the autotransformer knob at zero.', '线圈参数算出来了，下次见！'),
]
