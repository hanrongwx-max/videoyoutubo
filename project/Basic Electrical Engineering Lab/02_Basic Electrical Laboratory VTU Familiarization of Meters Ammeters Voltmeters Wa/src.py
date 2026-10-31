# 02_Basic Electrical Laboratory VTU Familiarization of Meters Ammeters Voltmeters Wa 卡通剧本作者源
# 原著版：完全照原片（电流表、电压表、功率表、万用表的用途、接法、读数），K1–K22，
# 不加补充知识点、不做本土化和更正（保留电流表导线“幻灯片写粗线、讲解说细线”、LED/节能灯用低功率因数表的举例、10 A 插孔）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '认识电工实验室的四种仪表',
    "edition": "原著版",
    "points": {
        'K1': '先熟悉四种仪表',
        'K2': '电流表：测电流',
        'K3': '电流表要串联',
        'K4': '电流表内阻很小',
        'K5': '交流表与直流表',
        'K6': '双量程：读对刻度',
        'K7': '电流表的连接导线',
        'K8': '电压表：测电压，内阻大',
        'K9': '电压表要并联',
        'K10': '电压表的分类',
        'K11': '动圈式与动铁式电压表',
        'K12': '功率表测有功功率',
        'K13': '电流线圈串、电压线圈并',
        'K14': '四个接线端：M、L、C、V',
        'K15': '功率表常数',
        'K16': '单位功率因数表与低功率因数表',
        'K17': '万用表：一表多用',
        'K18': '模拟式与数字式',
        'K19': '万用表的挡位和插孔',
        'K20': '有效值与峰值',
        'K21': '用表笔接入电路',
        'K22': '做实验前回顾本讲',
    },
    "avoid": ['VTU', 'Visvesvaraya', 'Simplified EEE Studies', 'Simplified EEE', 'rupees', 'AE'],
}

SHOTS = [
# 开场
('开场', '欣欣站在仪表柜前，柜里摆着几只指针式电表和一只万用表，向镜头招手', 'The panda mascot stands in front of an instrument cabinet holding several analog meters with blank dials and a multimeter, waving at the camera.', '这一课认识电工实验室的四种仪表。', '认识电工实验室的四种仪表'),
('开场', '电流表、电压表、功率表、万用表四个图标排成一行', 'Four icons in a row: an ammeter, a voltmeter, a wattmeter and a multimeter, all with blank dials. No people.', '电流表、电压表、功率表、万用表。', '', ['电流表', '电压表', '功率表', '万用表']),
# 情景
('情景', '阿杰面对桌上四只仪表，拿起又放下，不知道先用哪只', 'The young male student faces four meters on the bench, picking one up and putting it down, unsure which to use.', '阿杰看着一桌仪表，不知从哪下手。'),
('情景', '小研拿起电流表和电压表各一只，放在他面前', 'The female graduate student picks up an ammeter and a voltmeter and sets them in front of him.', '小研说：每种表测什么、怎么接，先弄清。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '表接对了，读数才准。'),
# K1
('K1', '王老师把四只仪表依次摆在实验台上', 'The safety administrator places four meters one by one on the lab bench.', '做实验之前，先熟悉这四种仪表。', '先熟悉四种仪表'),
('K1', '四只仪表图标连到一块电路板，每只旁边有问号', 'Four meter icons linked to a circuit board icon, each with a small question mark. No people.', '每种表测什么、怎么接，都要弄清。'),
# K2
('K2', '圆圈里一个字母 A 的电流表符号，旁边是指针式电流表', 'A circuit symbol of a circle with the letter A inside, next to an analog ammeter with a blank dial. No people.', '电流表，用来测电路里的电流。', '电流表：测电流', ['A']),
('K2', '导线里流动的小箭头，汇入电流表', 'Small arrows flowing along a wire into an ammeter icon. No people.', '单位是安培，所以也叫安培表。'),
# K3
('K3', '电池、电流表、负载首尾相连成一圈', 'A circuit icon: a battery, an ammeter and a load connected end to end in a single loop. No people.', '电流表要串联在电路里。', '电流表要串联'),
('K3', '箭头依次穿过电池、电流表、负载', 'Arrows passing in turn through the battery, the ammeter and the load in a single loop. No people.', '被测电流全部从表里流过。'),
# K4
('K4', '电流表内部一个很小的电阻图标', 'An ammeter icon with a cutaway showing a very small resistor inside. No people.', '所以电流表的内阻做得很小。', '电流表内阻很小'),
('K4', '电流表两端只有很小的电压降，负载上电压基本不变', 'An icon showing a tiny voltage drop arrow across the ammeter and a large one across the load. No people.', '表上压降小，才不影响原电路。'),
# K5
('K5', '两只电流表并排：一只表盘有直线符号，一只有波浪符号', 'Two analog ammeters side by side: one marked with a straight line symbol, the other with a wave symbol. No people.', '电流表分直流和交流两种。', '交流表与直流表', ['直流', '交流']),
('K5', '直流表内部是可动线圈，交流表内部是铁片', 'Two cutaway icons: a moving coil inside one meter, a moving iron vane inside the other. No people.', '直流用动圈式，交流用动铁式。', '', ['动圈式', '动铁式']),
('K5', '欣欣指着直线和波浪两个符号', 'The panda mascot points at a straight line symbol and a wave symbol on a blank card.', '直线是直流，波浪是交流。'),
# K6
('K6', '一只电流表上三个接线柱，其中一个标为公共端', 'An analog ammeter with three terminals on top, one of them highlighted as the common terminal. No people.', '双量程表：公共端固定，另一端选量程。', '双量程：读对刻度'),
('K6', '表盘上有上下两条刻度，大量程连到上刻度', 'A meter dial with an upper scale and a lower scale; an arrow links the higher range terminal to the upper scale. No people.', '接大量程，看上刻度。', '', ['大量程→上刻度']),
('K6', '小量程接线柱连到下刻度', 'The same dial; an arrow links the lower range terminal to the lower scale. No people.', '接小量程，看下刻度。', '', ['小量程→下刻度']),
('K6', '阿杰盯着表盘皱眉，小研指向正确的刻度', 'The young male student frowns at a meter dial; the female graduate student points to the correct scale.', '很多人读错刻度，现在就要分清。'),
# K7
('K7', '一根粗导线接到电流表，旁边一张空白幻灯片卡片', 'A thick wire connected to an ammeter, next to a blank presentation slide card. No people.', '接电流表的导线，幻灯片上写用粗线。', '电流表的连接导线', ['用粗导线']),
('K7', '王老师拿起一根细导线讲解', 'The safety administrator holds up a thin connecting wire while explaining at the bench.', '讲解时说的是，用细线接上去。'),
# K8
('K8', '圆圈里一个字母 V 的电压表符号，旁边是电压表', 'A circuit symbol of a circle with the letter V inside, next to an analog voltmeter with a blank dial. No people.', '电压表，测的是两点间的电压。', '电压表：测电压，内阻大', ['V']),
('K8', '电压表内部一个很大的电阻图标', 'A voltmeter icon with a cutaway showing a very large resistor inside. No people.', '它的内阻做得很大。'),
('K8', '流过电压表的电流箭头极细', 'An icon of a voltmeter with only a hair-thin current arrow flowing through it. No people.', '这样几乎不分走电流，不改变电路。'),
# K9
('K9', '电压表的两根线跨接在电阻两端', 'A circuit icon: a battery, a resistor and a load in a loop, with a voltmeter connected across the two ends of the resistor. No people.', '电压表要并联在被测元件两端。', '电压表要并联'),
('K9', '小研把电压表并接在电阻两端', 'The female graduate student connects a voltmeter across a resistor on a circuit board.', '比如测电阻两端的电压降。'),
('K9', '两张对照卡：电流表串联、电压表并联', 'Two comparison cards: an ammeter in series in a loop, and a voltmeter connected in parallel across a resistor. No people.', '记住：电流表串，电压表并。', '', ['电流表 串联', '电压表 并联']),
# K10
('K10', '一棵分类树图标，分出三根枝', 'A tree diagram icon branching into three blank boxes. No people.', '电压表可以从三个角度分类。', '电压表的分类'),
('K10', '指针表和数字表并排', 'An analog voltmeter with a needle next to a digital voltmeter with a blank display. No people.', '按显示，分模拟式和数字式。', '', ['模拟式', '数字式']),
('K10', '五个不同结构的表芯小图标', 'Five small cutaway icons of different meter movements in a row. No people.', '按结构，有整流式、动铁式、动圈式等。', '', ['整流式', '动铁式', '永磁动圈式', '感应式', '电动式']),
('K10', '直线和波浪两个符号被高亮', 'A straight line symbol and a wave symbol highlighted with a glow. No people.', '实验中最常用的是分交流、直流。'),
# K11
('K11', '直流电压表和交流电压表并排', 'A DC voltmeter and an AC voltmeter side by side, dials blank except for the line and wave symbols. No people.', '直流电压表是动圈式，交流是动铁式。', '动圈式与动铁式电压表'),
('K11', '电压表的两个量程接线柱分别连向上、下刻度', 'A voltmeter with two range terminals, arrows linking each terminal to the upper or lower scale. No people.', '电压表也要按所接量程读刻度。'),
# K12
('K12', '功率表实物和一个灯泡', 'An analog wattmeter with a blank dial next to a glowing light bulb. No people.', '功率表测的是有功功率。', '功率表测有功功率'),
('K12', '有功功率的柱子亮起，无功功率的柱子变灰', 'Two bars: one labeled with a lit bulb icon glowing, the other with a coil icon greyed out. No people.', '无功功率，它不测。', '', ['有功 √', '无功 ×']),
# K13
('K13', '功率表内部两个线圈：一个粗线圈、一个细线圈', 'A cutaway icon of a wattmeter with two coils inside: a thick current coil and a fine voltage coil. No people.', '功率表里有两个线圈。', '电流线圈串、电压线圈并', ['电流线圈', '电压线圈']),
('K13', '电流线圈串在负载回路，电压线圈跨接负载两端', 'A circuit icon: the current coil in series with the load, the voltage coil connected across the load. No people.', '电流线圈串联，电压线圈并联。'),
('K13', '电流符号乘电压符号等于功率符号', 'An icon equation: a current arrow times a voltage arrow equals a light bulb with rays. No people.', '电流乘电压，就得到功率。'),
# K14
('K14', '功率表顶部四个接线柱，旁边四个字母', 'The top of an analog wattmeter with four terminals, each with a small blank tag. No people.', '功率表有四个接线端。', '四个接线端：M、L、C、V', ['M 电源侧', 'L 负载侧', 'C 公共端', 'V 电压端']),
('K14', 'M 和 C 两个接线柱之间连一根短线', 'A short jumper wire connecting two of the four wattmeter terminals. No people.', 'M 和 C 两端要用短线连起来。', '', ['M—C 短接']),
('K14', '旋钮和接线柱分别对应电压量程和电流量程', "The wattmeter's range terminals highlighted: one group for voltage range, one group for current range. No people.", '电压、电流量程，按实验需要选。'),
# K15
('K15', '一张空白卡片上写着 K 的公式图示', 'A blank card showing a fraction icon: voltage times current times power factor over a full dial. No people.', '用功率表，先算功率表常数 K。', '功率表常数', ['电压×电流×功率因数', '÷满偏格数']),
('K15', '表盘读数乘以 K 得到功率', 'An icon: a meter dial reading arrow, a multiply sign, the letter K, an equals sign and a light bulb. No people.', '读到的格数乘 K，才是实际功率。'),
# K16
('K16', '两只功率表并排，一只贴绿色标签，一只贴橙色标签', 'Two analog wattmeters side by side, one with a blank green tag and one with a blank orange tag. No people.', '功率表有两种：单位功率因数和低功率因数。', '单位功率因数表与低功率因数表', ['UPF', 'LPF']),
('K16', '电阻负载连绿色表，LED 灯和节能灯连橙色表', 'An icon of a resistor heater linked to the green-tagged meter, and an LED bulb and a compact fluorescent bulb linked to the orange-tagged meter. No people.', '电阻负载用单位功率因数表。'),
('K16', 'LED 灯和节能灯图标旁是橙色标签的功率表', 'An LED bulb icon and a compact fluorescent bulb icon beside the orange-tagged wattmeter. No people.', 'LED 灯、节能灯，用低功率因数表。'),
('K16', '选错表时表盘指针只偏一点点的图标', 'A wattmeter dial whose needle barely moves from zero, with a question mark. No people.', '选错了，读数就不准。'),
# K17
('K17', '欣欣举着一只数字万用表', 'The panda mascot holds up a digital multimeter with a blank display.', '万用表，一只表能测好几样。', '万用表：一表多用'),
('K17', '电压、电流、电阻、温度、晶体管五个图标围着万用表', 'Five icons around a multimeter: a voltage arrow, a current arrow, a resistor, a thermometer and a transistor. No people.', '电压、电流、电阻，有的还能测更多。'),
# K18
('K18', '指针式万用表和数字万用表并排', 'An analog multimeter with a needle and a digital multimeter with a blank display side by side. No people.', '万用表分指针式和数字式两种。', '模拟式与数字式', ['指针式', '数字式']),
# K19
('K19', '数字万用表正面特写：屏幕、按键、旋钮', 'A close-up of a digital multimeter front: blank display, two small buttons and a big rotary switch. No people.', '上面是显示屏、保持键和电源键。', '万用表的挡位和插孔'),
('K19', '旋钮周围一圈挡位图标', 'A rotary switch surrounded by small icons: straight line, wave, resistor, sound wave for continuity, and a transistor. No people.', '旋钮选挡：电压、电流、电阻、通断。'),
('K19', '表笔测一根导线两端，万用表发出提示音', "A multimeter's probes touching both ends of a disconnected wire, with a sound wave icon from the meter. No people.", '通断挡能查导线是否导通。'),
('K19', '表身下方几个插孔，大电流插孔单独一个', 'The bottom of a multimeter with several jacks; one separate jack highlighted for high current. No people.', '大电流用单独的 10A 插孔，其余用普通插孔。', '', ['10A 插孔', '普通插孔']),
# K20
('K20', '一条正弦波，峰值和有效值两条横线', 'A sine wave icon with two horizontal lines: one at the peak, one lower at the effective value. No people.', '仪表读到的是有效值。', '有效值与峰值'),
('K20', '有效值乘根号二箭头指向峰值', 'An icon: the lower line, a multiply sign with a square root of two symbol, and an arrow up to the peak line. No people.', '正弦量的峰值，是有效值乘根号二。', '', ['峰值=有效值×√2']),
# K21
('K21', '一红一黑两根表笔插在万用表上', 'A red and a black test lead plugged into a multimeter, laid neatly on the bench. No people.', '万用表通过两根表笔接入电路。', '用表笔接入电路'),
# K22
('K22', '阿杰翻着空白笔记本复习仪表图标', 'The young male student reviews a blank notebook with meter icons drawn on it.', '做实验时，回头看看这一课。', '做实验前回顾本讲'),
('K22', '阿杰举手提问，王老师回应', 'The young male student raises his hand and the safety administrator answers him.', '有疑问，及时问老师。'),
# 小结
('小结', '四只仪表图标，各标串联或并联', 'Four meter icons: ammeter with a series loop, voltmeter with a parallel link, wattmeter with two coils, multimeter with a rotary switch. No people.', '电流表串，电压表并，功率表两样都有。', '小结'),
('小结', '量程、刻度、常数 K 三个打勾图标', 'Three icons with green checks: a range selector, an upper and lower scale, and the letter K. No people.', '选对量程，读对刻度，别忘乘 K。'),
('小结', '两种功率表和一只万用表图标', 'Icons of a green-tagged wattmeter, an orange-tagged wattmeter and a multimeter with probes. No people.', '按负载选功率表，万用表一表多用。'),
# 结尾
('结尾', '欣欣在整齐的仪表柜前挥手道别', 'The panda mascot waves goodbye in front of a tidy instrument cabinet with meters lined up.', '认识了仪表，下次动手做实验，再见！'),
]
