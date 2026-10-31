# 12_Demonstration of Verification of KVL and KCL for a given DC Circuit Basic Electr 卡通剧本作者源
# 原著版：完全照原片（双路稳压电源的使用、三只灯一串两并电路的接线与实测，验证 KVL、KCL），K1–K15，
# 不加补充知识点、不做本土化和更正（保留“电压旋钮最小、电流旋钮最大”“两路可串联升压”、3 V 设定电压，实测约 1.9 V + 1.08 V ≈ 2.98 V、I1 约 0.138 A 与支路各约 0.06 A）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '电工实验：基尔霍夫定律（实测演示）',
    "edition": "原著版",
    "points": {
        'K1': '先看图，先串后并',
        'K2': '双路稳压电源',
        'K3': '粗调、细调和电流旋钮',
        'K4': '开机前旋钮放好',
        'K5': '显示切换拨钮',
        'K6': '正负不接反，开关先关',
        'K7': '三只灯：一串两并',
        'K8': '一只万用表测电压',
        'K9': '三只电流表',
        'K10': '从正极出发，回到负极',
        'K11': '通电调到设定电压',
        'K12': '实测验证KVL',
        'K13': '实测验证KCL',
        'K14': '有误差是正常的',
        'K15': '换电压重复，有疑问就问',
    },
    "avoid": ['VTU', 'Simplified EEE', 'EEE Studies', "Winner's Capsule", "WINNER'S CAPSULE", 'Kulshreshtha', 'Kulasreshta', 'Automatic Electric', 'BANDICAM', 'McGraw', 'Mcgraw'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台前，台上有稳压电源、三只小灯和电表', 'The panda mascot stands at a lab bench with a dual regulated DC power supply, three small lamps and DC meters, waving at the camera.', '上次算好了，今天动手测一测！', '电工实验：基尔霍夫定律（实测演示）'),
# 情景
('情景', '阿杰拿着上次的计算纸，对着实验台跃跃欲试', "The young male student holds last lesson's calculation sheet, eager in front of the lab bench.", '阿杰带着计算结果，来实验室对答案。'),
('情景', '小研指着电源面板上一排旋钮', 'The female graduate student points at a row of knobs on the power supply panel.', '小研说：先把电源认清楚。'),
# K1
('K1', '电路图图标：先亮起串联部分，再亮起电压表', 'A circuit diagram icon where the series path lights up first, then the voltmeters light up. No people.', '看懂电路，先接串联，最后并电压表。', '先看图，先串后并'),
('K1', '万用表拨到直流电压档，代替三只电压表', 'A multimeter set to DC voltage replaces three small voltmeter icons that fade out. No people.', '这次用一只万用表直流档代替电压表。'),
# K2
('K2', '双路稳压电源，两组输出端各有一个空白标签', 'A dual-channel regulated DC power supply with two output terminal groups, each with a blank tag. No people.', '这台电源有两路输出，任用一路。', '双路稳压电源', ['第一路', '第二路']),
('K2', '老周指着两路输出讲解', 'The older man points at the two output channels while explaining.', '要更高电压，可以两路串联，这次用不到。'),
# K3
('K3', '电压粗调旋钮和细调旋钮特写', 'Close-up of two voltage knobs on the supply, one large for coarse and one small for fine adjustment. No people.', '粗调旋钮大步调，细调旋钮微调。', '粗调、细调和电流旋钮', ['粗调', '细调']),
('K3', '旁边的电流旋钮特写', 'Close-up of the current knob beside the voltage knobs. No people.', '旁边这个是电流旋钮。'),
# K4
('K4', '手把两个电压旋钮都转到最小', 'A hand turns both voltage knobs to minimum. No people.', '开机前，两个电压旋钮放到最小。', '开机前旋钮放好', ['电压：最小']),
('K4', '电流旋钮被转到最大', 'The current knob turned fully to maximum. No people.', '电流旋钮放到最大。', '', ['电流：最大']),
# K5
('K5', '拨钮拨动，显示窗在电压和电流图标间切换', 'A small toggle switch is flipped and the display window changes between a voltage icon and a current icon. No people.', '这个拨钮切换显示电压还是电流。', '显示切换拨钮'),
# K6
('K6', '红色正端子和黑色负端子特写', 'Close-up of a red positive output terminal and a black negative output terminal on the supply. No people.', '输出端分正负，直流不能接反。', '正负不接反，开关先关', ['＋', '－']),
('K6', '电源总开关处于关闭位置', 'The main power switch of the supply in the off position. No people.', '接线时，电源总开关一定是关的。'),
# K7
('K7', '透明面板上三只小灯，两只并排一只在前', 'Three small lamps on a clear panel: one in front, two side by side behind it. No people.', '灯2灯3并联，再和灯1串联。', '三只灯：一串两并', ['灯1', '灯2', '灯3']),
# K8
('K8', '万用表表笔跨在第一盏灯两端', 'Multimeter probes placed across the two ends of the first lamp icon. No people.', '万用表测灯1两端，就是V2。', '一只万用表测电压'),
('K8', '表笔跨在并联两灯两端', 'Multimeter probes placed across the pair of parallel lamps. No people.', '测并联部分两端，就是V3。'),
('K8', '电源显示窗亮着电压图标', 'The power supply display window lit with a voltage icon. No people.', '电源电压V1，直接看电源显示。'),
# K9
('K9', '三只直流电流表一字排开', 'Three DC ammeters with blank dials lined up on the bench. No people.', '三只直流电流表测三路电流。', '三只电流表', ['I1', 'I2', 'I3']),
# K10
('K10', '箭头从电源正极出发，进入第一只电流表正端', "An arrow leaves the supply's positive terminal and enters the positive terminal of the first ammeter. No people.", '从电源正极出发，先进电流表正端。', '从正极出发，回到负极'),
('K10', '箭头经过灯1后分成两路，各进一只电流表', 'The arrow passes lamp one, then splits into two branches, each through an ammeter. No people.', '过了灯1分两路，各串一只电流表。'),
('K10', '两路分别经过灯2、灯3后汇合，回到负极', 'The two branches pass lamps two and three, join, and return to the negative terminal. No people.', '两灯另一端接在一起，回到负极。'),
('K10', '阿杰对照电路图接完最后一根线，回路闭合', 'The young male student connects the last wire following the circuit diagram, closing the loop.', '这样就形成了一个闭合回路。'),
# K11
('K11', '阿杰打开电源，转粗调再转细调', 'The young male student switches on the supply and turns the coarse knob, then the fine knob.', '打开电源，粗调细调到三伏，四伏也行。', '通电调到设定电压', ['3 V']),
('K11', '万用表旋钮停在直流档，交流档图标打叉', "A multimeter's switch rests on the DC voltage range; an AC range icon is crossed out. No people.", '万用表一定拨直流档，别拨交流档。'),
# K12
('K12', '小研测灯1两端电压，阿杰记录', 'The female graduate student measures across lamp one with the multimeter while the young male student writes.', '先测灯1两端，V2约一点九伏。', '实测验证KVL', ['V2≈1.9 V']),
('K12', '小研再测并联部分电压', 'She then measures across the two parallel lamps.', '再测并联部分，V3约一点零八伏。', '', ['V3≈1.08 V']),
('K12', '两段电压柱叠起来，和电源电压柱几乎一样高', 'Two stacked voltage bars almost as tall as the supply voltage bar. No people.', '相加约二点九八伏，和三伏基本相等。', '', ['≈2.98 V', 'V1=3 V']),
# K13
('K13', '阿杰慢慢转电源旋钮，眼睛盯着第一只电流表', 'The young male student slowly turns the supply knob, watching the first ammeter.', '调电源，让干路电流约零点一三八安。', '实测验证KCL', ['I1≈0.138 A']),
('K13', '表盘下排刻度高亮', 'The lower scale on a meter dial highlighted. No people.', '用小量程，就读下排刻度。'),
('K13', '两只支路电流表读数被记下', 'The readings of the two branch ammeters are written down.', '两条支路电流，各约零点零六安。', '', ['I2≈0.06 A', 'I3≈0.06 A']),
('K13', '两个支路箭头合起来约等于干路箭头', 'Two branch arrows combining to roughly equal the main arrow. No people.', '两路相加，约等于干路电流。', '', ['I2+I3≈I1']),
# K14
('K14', '天平稍微倾斜，旁边一个放大镜', 'A balance scale tilted very slightly, with a magnifying glass beside it. No people.', '元件和电表都有误差，差一点正常。', '有误差是正常的'),
# K15
('K15', '电压旋钮转到另一位置，再测一组', 'The voltage knob is turned to another position and the group takes another set of readings.', '换几个电压，重复测几组。', '换电压重复，有疑问就问'),
('K15', '两张表格并排：理论值和实测值', 'Two blank tables side by side, one with a calculator icon and one with a meter icon, both checked. No people.', '理论和实测都做完，才算完成。'),
('K15', '阿杰举手提问，老周回答', 'The young male student raises his hand and the older man answers.', '对照教材复习，有疑问就问。'),
# 小结
('小结', '电源旋钮、正负端子、闭合回路三个图标', 'Three icons: supply knobs, positive and negative terminals, and a closed loop. No people.', '旋钮放好，正负分清，接成闭合回路。', '小结'),
('小结', '两个约等式都打勾', 'Two approximate equation icons, both with green checks. No people.', '实测电压电流，两条定律都成立。'),
# 结尾
('结尾', '欣欣在关好电源的实验台前挥手', 'The panda mascot waves in front of the lab bench with the supply switched off.', '定律验证成功，下次见！'),
]
