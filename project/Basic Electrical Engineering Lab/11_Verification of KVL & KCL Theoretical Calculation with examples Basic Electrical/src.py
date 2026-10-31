# 11_Verification of KVL & KCL Theoretical Calculation with examples Basic Electrical 卡通剧本作者源
# 原著版：完全照原片（直流电路 KVL、KCL 验证的理论计算：目的、器材、RPS 注意事项、电路、步骤、两套表、四步计算），K1–K14，
# 不加补充知识点、不做本土化和更正（保留“RPS 电压旋钮最小、电流旋钮最大”、磁电式表、12 V/10 W 灯 14.4 Ω、Req 21.6 Ω、4 V 时 0.185 A 等算例）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '电工实验：基尔霍夫定律（理论计算）',
    "edition": "原著版",
    "points": {
        'K1': '先学理论，再做验证',
        'K2': '实验目的：算一算，测一测',
        'K3': '要准备的器材',
        'K4': '稳压电源的旋钮先放好',
        'K5': '看懂电路：一串两并',
        'K6': '直流表标明正负',
        'K7': '实验六步',
        'K8': '组员各测一组',
        'K9': '先画两套表',
        'K10': '第一步：求灯的电阻',
        'K11': '第二步：求等效电阻',
        'K12': '第三步：求电流，验证KCL',
        'K13': '第四步：求电压，验证KVL',
        'K14': '填好理论值，下次实测',
    },
    "avoid": ['VTU', 'Simplified EEE', 'EEE Studies', 'BANDICAM', 'CamScanner'],
}

SHOTS = [
# 开场
('开场', '欣欣站在白板前，白板上画着一个节点和一个回路', 'The panda mascot stands in front of a whiteboard with a simple junction and a loop drawn on it, waving at the camera.', '今天先动笔，算一算基尔霍夫定律！', '电工实验：基尔霍夫定律（理论计算）'),
('开场', '节点处箭头汇合、回路上箭头绕圈两个图标', 'Two icons: arrows meeting at a junction, and arrows circling around a closed loop. No people.', '一个管电流，一个管电压。', '', ['KCL 电流', 'KVL 电压']),
# 情景
('情景', '阿杰拿着三只小灯泡，急着要接线', 'The young male student holds three small bulbs, eager to start wiring.', '阿杰拿起灯泡就想接线。'),
('情景', '小研递上一张空白计算纸', 'The female graduate student hands him a blank sheet of calculation paper.', '小研说：先把理论值算出来，再去测。'),
# K1
('K1', '一本空白理论书和一块实验板，箭头从书指向实验板', 'A blank textbook icon with an arrow pointing to a lab circuit board icon. No people.', '先弄懂两条定律，再动手验证。', '先学理论，再做验证'),
# K2
('K2', '天平一边是计算纸，一边是电表', 'A balance scale icon with a calculation sheet on one side and a meter on the other, level. No people.', '对同一个直流电路，算一遍，测一遍。', '实验目的：算一算，测一测', ['理论值', '实测值']),
('K2', '王老师指着两边相等的天平', 'The safety administrator points at the level balance scale on a board.', '看看两条定律是不是都成立。'),
# K3
('K3', '稳压直流电源和三只相同的小灯泡', 'A regulated DC power supply and three identical small DC bulbs. No people.', '准备稳压直流电源和三只同规格的灯。', '要准备的器材'),
('K3', '三只直流电流表和三只直流电压表，表芯为可动线圈', 'Three DC ammeters and three DC voltmeters with moving coil mechanism icons. No people.', '三只磁电式电流表，三只磁电式电压表。', '', ['MC 电流表×3', 'MC 电压表×3']),
('K3', '万用表旋钮拨到直流电压档', "A multimeter's rotary switch turned to the DC voltage range. No people.", '没有电压表，就用万用表直流档。'),
# K4
('K4', '稳压电源电压旋钮被转到最左边', 'The voltage knob of a regulated DC power supply turned fully to the left. No people.', '接通前，电压旋钮放到最小。', '稳压电源的旋钮先放好', ['电压：最小']),
('K4', '电流旋钮被转到最右边', 'The current knob of the same supply turned fully to the right. No people.', '电流旋钮放到最大。', '', ['电流：最大']),
('K4', '冒烟的电源图标被红叉划掉', 'An icon of a smoking power supply crossed out with a red X. No people.', '不这样放，电源可能损坏。'),
# K5
('K5', '简化电路图：电源、一盏灯串联，后面两盏灯并联', 'A simple circuit diagram icon: a DC source, one lamp in series, followed by two lamps in parallel. No people.', '电路是一盏灯串联，两盏灯并联。', '看懂电路：一串两并', ['灯1 串联', '灯2 灯3 并联']),
('K5', '三个电流表分别在干路和两条支路上', 'Circuit icon with three ammeters: one in the main line and one in each parallel branch. No people.', '三只电流表测干路和两条支路电流。', '', ['I1', 'I2', 'I3']),
('K5', '三个电压表分别跨在电源、灯1、并联部分', 'Circuit icon with three voltmeters: across the source, across the first lamp, and across the parallel pair. No people.', '三只电压表测电源、灯1和并联部分。', '', ['V1', 'V2', 'V3']),
('K5', '并联的两盏灯上方一个等号', 'Two lamps in parallel with an equals sign above them. No people.', '并联的两盏灯，电压一样。'),
# K6
('K6', '电表符号里写着可动线圈图标，旁边标着加号和减号', 'Meter symbols with a moving coil icon inside, marked with plus and minus signs. No people.', '直流表画图时标明磁电式和正负极。', '直流表标明正负', ['MC', '+', '−']),
# K7
('K7', '六个步骤图标排成两行', 'Six step icons in two rows: wiring, switch on, set voltage, read meters, repeat, switch off. No people.', '接线、合闸、调电压、读数、重复、断电。', '实验六步'),
('K7', '阿杰按图接线后合上电源开关，在电源上设一个电压', 'The young male student finishes wiring, switches on the regulated supply and sets a voltage.', '按图接好线，合闸，设定一个电压。'),
('K7', '小研记下读数，再换一个电压', 'The female graduate student writes down the meter readings, then turns the voltage knob to a new value.', '记下各表读数，再换几个电压。'),
('K7', '阿杰关掉电源，拔下插头', 'The young male student switches off the supply and pulls out the plug.', '做完关电源，拔下插头。'),
# K8
('K8', '五个同学每人手里一张写着不同电压的空白卡', 'Five students each hold a blank card with a different small battery icon, standing in a row.', '组里每人选一个电压，各测一组。', '组员各测一组'),
# K9
('K9', '两张空白表格并排，一张画计算器，一张画电表', 'Two blank tables side by side, one headed by a calculator icon and one by a meter icon. No people.', '测量前先画两套表：理论和实测。', '先画两套表', ['理论值', '实测值']),
('K9', '电压表格最后一栏是等式', 'A blank voltage table whose last column holds an equation icon. No people.', '电压表格验证V1等于V2加V3。', '', ['V1=V2+V3']),
('K9', '电流表格最后一栏是等式', 'A blank current table whose last column holds an equation icon. No people.', '电流表格验证I1等于I2加I3。', '', ['I1=I2+I3']),
# K10
('K10', '灯泡图标上贴着额定电压和功率的空白铭牌', 'A bulb icon with a blank rating tag beside it. No people.', '第一步，用灯的额定值求电阻。', '第一步：求灯的电阻', ['12 V', '10 W']),
('K10', '白板上的公式：电压平方除以功率', 'A whiteboard showing a formula icon: voltage squared over power. No people.', '十二伏、十瓦，电阻是十四点四欧。', '', ['R=U²÷P', 'R=14.4Ω']),
('K10', '三只灯泡下面都标着相同的电阻符号', 'Three bulbs, each with the same resistor symbol below. No people.', '三只灯一样，电阻也一样。'),
# K11
('K11', '两盏并联灯合成一个电阻，再和第一个电阻相加', 'Diagram: two parallel resistors merge into one, then add to the series resistor to form a single equivalent resistor. No people.', '第二步，并联部分合起来，再加串联。', '第二步：求等效电阻', ['R1+R2∥R3', 'Req=21.6Ω']),
# K12
('K12', '电源电压除以等效电阻得到总电流', 'Diagram: a source voltage icon divided by the equivalent resistor icon gives a current arrow. No people.', '第三步，电压除以等效电阻，得总电流。', '第三步：求电流，验证KCL', ['4V÷21.6Ω', '≈0.185A']),
('K12', '总电流箭头在节点分成两路', 'A main current arrow splits into two branch arrows at a junction. No people.', '再用分流公式求两条支路的电流。'),
('K12', '两条支路电阻相同，箭头一样粗', 'Two parallel branches with equal resistors carry two arrows of equal thickness. No people.', '两路电阻相同，电流各占一半。', '', ['I2≈0.0925A', 'I3≈0.0925A']),
('K12', '两支路电流加起来等于总电流，打勾', 'Two branch arrows add up to equal the main arrow, with a green check mark. No people.', '两路相加等于总电流，KCL成立。'),
# K13
('K13', '总电流乘第一盏灯电阻得到灯1电压', 'Diagram: the main current icon multiplied by the first resistor gives a voltage icon. No people.', '第四步，欧姆定律求灯1的电压。', '第四步：求电压，验证KVL', ['V2=I1×R1', '≈2.664V']),
('K13', '电源电压减去灯1电压得到并联电压', 'Diagram: the source voltage minus the first lamp voltage gives the parallel voltage. No people.', '电源电压减去它，是并联部分电压。', '', ['V3=V1-V2', '≈1.336V']),
('K13', '两段电压加起来等于电源电压，打勾', 'Two voltage bars stacked equal the source voltage bar, with a green check mark. No people.', '两段电压相加等于电源，KVL成立。'),
# K14
('K14', '小研把算好的数填进理论值表', 'The female graduate student fills calculated numbers into the blank theoretical table.', '先把理论值填好，下次实测对照。', '填好理论值，下次实测'),
('K14', '串联、并联、分压、分流四个小图标', 'Four small icons: series resistors, parallel resistors, a voltage divider and a current divider. No people.', '复习串并联和分压分流公式。'),
# 小结
('小结', '电阻、等效电阻、电流、电压四步图标', 'Four step icons: resistance, equivalent resistance, current, voltage. No people.', '四步计算：电阻、等效、电流、电压。', '小结'),
('小结', '两个等式都打勾', 'Two equation icons, both with green checks. No people.', '电流相加、电压相加，两条定律成立。'),
('小结', '电压旋钮最小、电流旋钮最大两个图标', 'Two knob icons: voltage at minimum, current at maximum. No people.', '通电前：电压最小，电流最大。'),
# 结尾
('结尾', '欣欣举着写满计算的空白纸挥手', 'The panda mascot waves, holding up a sheet of calculation paper.', '下次实测见分晓，再见！'),
]
