# 04_VTU Basic Electrical Engg Laboratory Familiarization of Switches and Rheostats G 卡通剧本作者源
# 原著版：完全照原片（变阻器的结构、铭牌、切入切出位置、符号；SPST/SPDT/DPST/DPDT/TPST/TPDT 六种开关），K1–K18，
# 不加补充知识点、不做本土化和更正（保留铭牌 200 Ω、1.5 A，三相 R、Y、B，TPDT 用于感应发电机并网的举例）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '变阻器与开关',
    "edition": "原著版",
    "points": {
        'K1': '本课内容',
        'K2': '变阻器：可变电阻',
        'K3': '变阻器的结构',
        'K4': '看铭牌：阻值和额定电流',
        'K5': '接入越长，电阻越大',
        'K6': '切入位置：电阻最大',
        'K7': '切出位置：电阻最小',
        'K8': '变阻器的符号',
        'K9': '任取两端：一固定一滑动',
        'K10': '先认识开关',
        'K11': '单极单掷开关',
        'K12': '单极双掷开关',
        'K13': '双极单掷开关',
        'K14': '双极双掷开关',
        'K15': '数极、数掷',
        'K16': '三极单掷开关',
        'K17': '三极双掷：三相转换',
        'K18': '本课回顾',
    },
    "avoid": ['VTU', 'Visvesvaraya', 'Simplified EEE Studies', 'Simplified EEE', 'India Mart', 'IndiaMART', 'Amazon'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台旁，台上有一根长长的滑线变阻器和几个开关，向镜头招手', 'The panda mascot stands beside a lab bench with a long tubular sliding rheostat and several switches, waving at the camera.', '这一课认识变阻器和各种开关。', '变阻器与开关'),
('开场', '变阻器、船形开关、闸刀开关三个图标', 'Three icons in a row: a tubular sliding rheostat, a rocker switch and a knife-blade changeover switch. No people.', '一个调电阻，一个管通断。', '', ['变阻器', '开关']),
# 情景
('情景', '阿杰拿起一根长长的滑线变阻器，左看右看', 'The young male student picks up a long slide-wire rheostat and turns it around, looking puzzled.', '阿杰拿着变阻器，不知道怎么接。'),
('情景', '台上摆着几种外形不同的开关，阿杰挠头', 'Several switches of different shapes lie on the bench; the young male student scratches his head.', '开关也有好几种，长得都不一样。'),
('情景', '小研拿起一个开关，指着上面的触点', 'The female graduate student picks up a switch and points to its contacts.', '小研说：做实验前，这些都得认清。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '一个调电阻，一个管通断，一起来看。'),
# K1
('K1', '欣欣指着变阻器和一排开关', 'The panda mascot points at a rheostat and a row of different switches.', '做实验前，先把它们认清楚。', '本课内容'),
# K2
('K2', '电阻符号上加一个斜箭头', 'A resistor symbol with a diagonal arrow across it. No people.', '变阻器，就是阻值可以调的电阻。', '变阻器：可变电阻'),
# K3
('K3', '变阻器特写：瓷管上密绕电阻丝，上方有滑块', 'A close-up of a tubular rheostat: resistance wire tightly wound on a ceramic tube, with a slider on a bar above it. No people.', '瓷管上绕着电阻丝，上面有个滑块。', '变阻器的结构'),
('K3', '两端和滑块处三个接线柱被高亮', 'The two end terminals and the slider terminal of the rheostat highlighted. No people.', '两头是固定端，滑块是滑动端。', '', ['固定端 A', '固定端 B', '滑动端 C']),
# K4
('K4', '变阻器侧面的空白铭牌，旁边是电阻和电流图标', 'The side of a rheostat with a blank nameplate, a resistor icon and a current icon beside it. No people.', '铭牌上标着阻值和额定电流。', '看铭牌：阻值和额定电流', ['200 Ω', '1.5 A']),
('K4', '欣欣举起写着电流图标的空白卡', 'The panda mascot holds up a blank card with a current arrow icon.', '比如这台二百欧、一点五安，两个数一样重要。'),
# K5
('K5', '长段电阻丝和短段电阻丝对比', 'Two icons: a long section of resistance wire with a big resistance bar, a short section with a small bar. No people.', '接入的电阻丝越长，电阻越大。', '接入越长，电阻越大'),
# K6
('K6', '滑块位置使整根电阻丝都接入，电流箭头走完全程', 'A rheostat icon with the slider positioned so that current arrows travel the entire length of the wire. No people.', '电阻丝全长接入，电阻最大。', '切入位置：电阻最大', ['切入位置', '最大']),
# K7
('K7', '滑块位置使电流只走一小段', 'A rheostat icon with the slider positioned so that current arrows travel only a short section of wire. No people.', '只接入一小段，电阻最小。', '切出位置：电阻最小', ['切出位置', '最小']),
('K7', '老周指着三电压表电路图里的变阻器', 'The older man points at the rheostat in a three-voltmeter circuit diagram on a board.', '后面三电压表法实验，要用到它。'),
# K8
('K8', '两种变阻器符号并排', 'Two rheostat circuit symbols side by side: a zigzag resistor with a diagonal arrow, and a box resistor with a sliding arrow. No people.', '画电路图时，用这两种符号。', '变阻器的符号'),
('K8', '符号一端标固定，箭头端标可变', 'One rheostat symbol with one end marked by a fixed pin icon and the arrow marked by a slider icon. No people.', '一端固定，箭头那端可变。'),
# K9
('K9', '小研把导线接到一个固定端和滑动端', 'The female graduate student connects leads to one fixed terminal and the sliding terminal of a rheostat.', '任取两个端子：一个固定端，一个滑动端。', '任取两端：一固定一滑动'),
('K9', '滑块左右移动，电阻条变长变短', 'The slider moves left and right while a resistance bar grows and shrinks. No people.', '滑块位置，决定是切入还是切出。'),
# K10
('K10', '楼梯两头的开关控制同一盏灯', 'A staircase icon with a switch at the bottom and top controlling one lamp. No people.', '双控、多地控制照明，都要用到开关。', '先认识开关'),
('K10', '一个开关图标，标出“极”和“掷”', 'A switch symbol with its moving blade and its contact points highlighted in different colors. No people.', '开关看两样：几个极，几个掷。', '', ['极：动触头', '掷：接通位置']),
# K11
('K11', '单极单掷开关符号和一个船形开关', 'A single pole single throw switch symbol next to a black rocker switch. No people.', '单极单掷：一个极，一个位置。', '单极单掷开关'),
('K11', '电池、开关、灯泡电路：开关断开灯灭，闭合灯亮', 'Two circuit icons: battery, open switch and dark bulb; battery, closed switch and lit bulb. No people.', '断开就断电，闭合就接通。'),
# K12
('K12', '单极双掷开关符号：一个刀片可拨到两个位置', 'A single pole double throw switch symbol: one blade that can swing to position one or position two. No people.', '单极双掷：一个极，两个位置。', '单极双掷开关', ['位置1', '位置2']),
('K12', '刀片先接位置一，再接位置二', 'The blade connected to position one, then switching over to position two. No people.', '同一时刻只接一个位置。'),
('K12', '两只单极双掷开关控制楼梯灯', 'Two single pole double throw switches at both ends of a staircase controlling one lamp. No people.', '双控照明，就靠它。'),
# K13
('K13', '双极单掷开关符号：两个刀片用虚线连在一起', 'A double pole single throw switch symbol: two blades linked by a dashed line. No people.', '双极单掷：两个极一起动作。', '双极单掷开关'),
('K13', '一只开关同时接通两路电路', 'An icon of one double pole switch connecting two separate circuits to their loads at the same time. No people.', '一扳，两路电路同时接通。'),
# K14
('K14', '双极双掷开关符号和一个方形开关', 'A double pole double throw switch symbol next to a square rocker switch. No people.', '双极双掷：两个极，两个位置。', '双极双掷开关'),
('K14', '触点示意：常开和常闭', 'A contact diagram icon showing a normally open pair and a normally closed pair. No people.', '触点分常开和常闭，用在复杂电路。', '', ['常开 NO', '常闭 NC']),
# K15
('K15', '四种开关符号排成两行两列', 'Four switch symbols arranged in a two by two grid: single pole single throw, single pole double throw, double pole single throw, double pole double throw. No people.', '单极还是双极，单掷还是双掷？', '数极、数掷'),
('K15', '阿杰对着图数手指，小研点头', 'The young male student counts on his fingers in front of the grid; the female graduate student nods.', '数一数极和掷，就分清了。'),
# K16
('K16', '三极单掷开关符号：三个刀片连动', 'A switch symbol with three blades linked by a dashed line, one throw position. No people.', '三极单掷：三个极，一个掷。', '三极单掷开关'),
('K16', '三相电源三根线经开关接到负载', 'Three supply lines passing through the three-pole switch to a load. No people.', '三个极分别接三相 R、Y、B。', '', ['R', 'Y', 'B']),
('K16', '开关一扳，电源侧和负载侧三相同时亮起', 'The switch is thrown and all three lines on the supply side and load side light up together. No people.', '电源和负载三相，同时通、同时断。', '', ['电源侧', '负载侧']),
# K17
('K17', '实验室的三相转换开关板：三个刀闸、两排接线柱', 'A three-phase changeover switch board in a lab: three linked blades and two rows of terminals. No people.', '三极双掷：三个极，可拨到位置一或位置二。', '三极双掷：三相转换', ['位置1', '位置2']),
('K17', '电机图标和电网图标之间一个转换开关', 'A changeover switch icon between an induction machine icon and a power grid icon. No people.', '它常用作三相转换开关。'),
('K17', '发电机和电网的两条波形逐渐对齐', 'Two sine waves, one from a generator icon and one from a grid icon, gradually lining up. No people.', '比如感应发电机与电网同步并网的实验。'),
# K18
('K18', '变阻器和六种开关图标依次亮起', 'A rheostat icon and six switch symbols light up one by one. No people.', '变阻器和开关，是电工实验的基础。', '本课回顾'),
# 小结
('小结', '变阻器滑块在两端的两个图标', 'Two rheostat icons with the slider at opposite ends. No people.', '切入最大，切出最小，看铭牌额定值。', '小结'),
('小结', '六种开关符号排成一行', 'Six switch symbols in a row. No people.', '数极数掷，认清六种开关。'),
# 结尾
('结尾', '欣欣在整齐的实验台前挥手道别', 'The panda mascot waves goodbye in front of a tidy lab bench with a rheostat and switches.', '认识了变阻器和开关，下次见！'),
]
