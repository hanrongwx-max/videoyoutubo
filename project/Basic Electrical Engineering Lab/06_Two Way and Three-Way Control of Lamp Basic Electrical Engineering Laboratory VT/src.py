# 06_Two Way and Three-Way Control of Lamp Basic Electrical Engineering Laboratory VT 卡通剧本作者源
# 原著版：完全照原片（双控与三地控制照明：目的、器材、电路接法、实际接线、中间开关直连与交叉、4 种与 8 种状态真值表、结论），K1–K15，
# 不加补充知识点、不做本土化和更正（保留“花园布线”的叫法、5 A/230 V 开关、230 V/40 W 灯而电路图标 100 W、230 V 50 Hz 电源、演示者戴腕表徒手接线）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '双控与三地控制照明实验',
    "edition": "原著版",
    "points": {
        'K1': '双控：两地控一灯',
        'K2': '三地控制：加中间开关',
        'K3': '实验目的',
        'K4': '所需器材',
        'K5': '双控电路的接法',
        'K6': '按图接线',
        'K7': '扳动开关，观察灯',
        'K8': '双控真值表',
        'K9': '中间开关：直连与交叉',
        'K10': '三地控制电路的接法',
        'K11': '三地控制接线',
        'K12': '两种状态分别测',
        'K13': '三地控制真值表',
        'K14': '三地控制用在哪',
        'K15': '实验结论',
    },
    "avoid": ['VTU', 'Visvesvaraya', '18EEL27', 'BEELAB', 'Screencast', 'SCREENCAST-O-MATIC', 'garden wiring', 'go-down'],
}

SHOTS = [
# 开场
('开场', '欣欣站在楼梯口，楼梯上下各有一个开关，向镜头招手', 'The panda mascot stands at the foot of a staircase with a light switch at the bottom and another at the top, waving at the camera.', '这一课做双控和三地控制照明实验。', '双控与三地控制照明实验'),
('开场', '一盏灯连着两个开关和三个开关的两组图标', 'Two icons: one lamp linked to two switches, and one lamp linked to three switches. No people.', '一盏灯，两处、三处都能开关。', '', ['两地控制', '三地控制']),
# 情景
('情景', '阿杰走到楼梯顶，回头发现楼下的灯关不了', 'The young male student reaches the top of a staircase and looks back at a lamp he cannot switch off from downstairs.', '阿杰上了楼，楼下的灯却关不掉。'),
('情景', '小研在楼上按开关，灯灭了', 'The female graduate student presses a wall switch upstairs and the staircase lamp goes off.', '小研在楼上一按，灯就灭了。'),
('情景', '阿杰惊讶地挠头，欣欣在旁边竖起手指', 'The young male student scratches his head in surprise while the panda mascot raises one finger beside him.', '秘密就在开关的接法里。'),
# K1
('K1', '楼梯上下两个开关控制同一盏灯的示意', 'A staircase icon with a switch at the bottom and the top, both linked to one ceiling lamp. No people.', '双控：两个地点控制同一盏灯。', '双控：两地控一灯'),
('K1', '卧室门口和床头各一个开关控制吊灯', 'A bedroom icon with one switch by the door and one by the bed, both linked to the ceiling lamp. No people.', '楼梯常用，卧室也能用。'),
# K2
('K2', '两只双控开关之间加了一只中间开关', 'An intermediate switch added between two two-way switches, all controlling one lamp. No people.', '再加一只中间开关，三个地点控一盏灯。', '三地控制：加中间开关', ['双控开关', '中间开关', '双控开关']),
('K2', '花园里三条小路口各有一个开关，控制同一盏灯', 'A garden icon with three path entrances, each with a switch, all linked to one garden lamp. No people.', '讲解里把它叫作花园布线。'),
# K3
('K3', '空白实验记录本上画着两张空表', 'A blank lab notebook showing two empty table grids. No people.', '目的：实现两地、三地控灯，列出真值表。', '实验目的'),
# K4
('K4', '实验台上摆着两只双控开关、一只中间开关、一个灯泡和导线', 'Two two-way switches, one intermediate switch, an incandescent bulb and connecting wires laid out on a bench. No people.', '器材：两只双控开关，一只中间开关。', '所需器材', ['双控开关×2', '中间开关×1', '白炽灯×1', '连接导线']),
('K4', '开关旁空白铭牌，旁边是电流和电压图标', 'The switches with blank nameplates, current and voltage icons beside them. No people.', '开关都是五安、二百三十伏。', '', ['5 A', '230 V']),
('K4', '白炽灯旁空白铭牌和一卷导线', 'An incandescent bulb with a blank nameplate next to a coil of connecting wire. No people.', '白炽灯二百三十伏、四十瓦，再加导线。', '', ['230 V', '40 W']),
# K5
('K5', '电路图：交流电源的相线经熔断器接到第一只开关的公共端', 'A circuit diagram icon: the live line of an AC supply passes through a fuse to the common terminal of the first switch. No people.', '单相交流电源，相线先经熔断器。', '双控电路的接法', ['230 V 50 Hz', '相线', '熔断器']),
('K5', '相线接到开关一的公共端 A', 'The live line reaching the common terminal of switch one. No people.', '接到开关一的公共端 A。', '', ['S1：A']),
('K5', '两只开关之间两根导线对应相连', 'Two wires linking the two contacts of switch one to the two contacts of switch two. No people.', 'B 接 E，C 接 F。', '', ['B–E', 'C–F']),
('K5', '开关二的公共端接灯，灯另一端接中性线，灯旁标 100 W', "The common terminal of switch two goes to the lamp, and the lamp's other end goes to the neutral line. No people.", '开关二公共端 D 接灯，灯再接中性线。', '', ['D', '中性线', '灯 100 W']),
# K6
('K6', '小研在透明接线板上按图插线', 'The female graduate student plugs wires into a transparent patch board following a circuit diagram.', '备齐器材，在接线板上按图接线。', '按图接线'),
('K6', '接好的导线逐根打勾', 'Each connected wire on the board gets a green check one by one. No people.', '先连 B–E、C–F，再从 D 接灯和中性线。'),
# K7
('K7', '小研扳动开关一，灯亮', 'The female graduate student flips switch one by its handle and the bulb lights up.', '扳动开关一，灯亮了。', '扳动开关，观察灯'),
('K7', '阿杰扳动开关二，灯灭', 'The young male student flips switch two by its handle and the bulb goes out.', '再扳开关二，灯又灭了。'),
# K8
('K8', '一张 4 行真值表，只有亮灯和灭灯图标', 'A four-row truth table grid with only lamp-on and lamp-off icons. No people.', '把四种开关状态记成真值表。', '双控真值表', ['AB–DE 亮', 'AB–DF 灭', 'AC–DE 灭', 'AC–DF 亮']),
('K8', '两开关同侧时灯亮，异侧时灯灭', 'Two switch icons on the same side with a lit lamp, and on opposite sides with a dark lamp. No people.', '两开关位置对应，灯亮；错开，灯灭。'),
# K9
('K9', '中间开关内部两条平行连线', 'An intermediate switch with two parallel internal links. No people.', '中间开关第一种状态：直连。', '中间开关：直连与交叉', ['P–Q', 'R–S']),
('K9', '中间开关内部两条交叉连线', 'An intermediate switch with two crossed internal links. No people.', '第二种状态：交叉连接。', '', ['P–S', 'Q–R']),
('K9', '直连和交叉同时出现的图标被红叉划掉', 'An icon showing both parallel and crossed links at once, crossed out with a red X. No people.', '两种状态，不能同时成立。'),
# K10
('K10', '电路图：相线接 A，开关一的 B、C 接到中间开关一侧', 'A circuit diagram icon: the live line to switch one, whose two contacts go to one side of the intermediate switch. No people.', '相线接 A，B 接 P，C 接 R。', '三地控制电路的接法', ['A', 'B–P', 'C–R']),
('K10', '中间开关另一侧连到开关二，开关二接灯', 'The other side of the intermediate switch links to switch two, which goes to the lamp and neutral. No people.', 'Q 接 E，S 接 F，D 接灯再接中性线。', '', ['Q–E', 'S–F', 'D']),
# K11
('K11', '老周戴着腕表，徒手在接线板上加装中间开关并插线', 'The older man, wearing a metal wristwatch, plugs wires bare-handed into a patch board to add an intermediate switch.', '先连开关一到中间开关，再连到开关二。', '三地控制接线'),
('K11', '老周接上灯和中性线', 'The older man connects the lamp and the neutral wire on the patch board.', '再接灯和中性线。'),
('K11', '中间开关扳上、扳下两个图标', 'Two icons of the intermediate switch lever: up and down. No people.', '扳上是直连，扳下是交叉。', '', ['上 直连', '下 交叉']),
# K12
('K12', '中间开关扳上，阿杰轮流扳动两只双控开关', 'With the intermediate switch up, the young male student flips the two two-way switches in turn by their handles.', '先在直连状态下，扳动两只开关。', '两种状态分别测'),
('K12', '中间开关扳下，再轮流扳动', 'With the intermediate switch down, the young male student flips the two switches again while the female graduate student records.', '再换成交叉状态，重复一遍。'),
# K13
('K13', '一张 8 行真值表，上半与下半用颜色区分', 'An eight-row table with the top half shaded one color and the bottom half another, only lamp icons in the last column. No people.', '三地控制，一共八种状态。', '三地控制真值表', ['直连 4 种', '交叉 4 种']),
('K13', '上半表亮灭顺序与双控相同，下半表完全相反', 'The top half shows lamp on, off, off, on; the bottom half shows off, on, on, off. No people.', '直连和双控一样，交叉正好相反。'),
('K13', '亮灯图标旁是 1，灭灯旁是 0', 'A lit lamp icon next to the digit one and a dark lamp icon next to the digit zero. No people.', '亮记 1，灭记 0，逻辑一目了然。'),
# K14
('K14', '大仓库里三个门口各有一个开关', 'A large warehouse icon with a switch at each of three doors, all linked to the hall lights. No people.', '大仓库、粮库，多处都要能开关灯。', '三地控制用在哪'),
# K15
('K15', '欣欣指着两地和三地控制的两张图', 'The panda mascot points at the two-way and three-way control diagrams on a board.', '双控两地控灯，加中间开关三地控灯。', '实验结论'),
('K15', '房屋图标里的楼梯灯', 'A house icon with a staircase lamp highlighted. No people.', '弄懂开关逻辑，家里布线也明白了。'),
# 小结
('小结', '双控和三地控制两张电路图', 'Two circuit diagram icons: two-way control and three-place control. No people.', '双控两只开关，三地再加中间开关。', '小结'),
('小结', '4 行和 8 行两张真值表', 'A four-row truth table and an eight-row truth table with lamp icons. No people.', '真值表：双控四种，三地八种。'),
('小结', '房屋图标里的楼梯灯和开关逻辑图标', 'A house icon with a staircase lamp and a small switch logic icon. No people.', '理解开关逻辑，家庭布线也用得上。'),
# 结尾
('结尾', '欣欣站在楼梯中间，按下开关，灯亮，挥手道别', 'The panda mascot stands halfway up a staircase, presses a switch, the lamp lights up, and she waves goodbye.', '哪里都能开关灯，下次见！'),
]
