# 03_Basic Electrical Engg Laboratory VTU Familiarization of Autotransformer Wires, C 卡通剧本作者源
# 原著版：完全照原片（导体与绝缘体、铜铝铁导线、导线结构与规格、R=ρL/A、自耦调压器），K1–K22，
# 不加补充知识点、不做本土化和更正（保留原片的截面规格、股数与线径、铝约为铜 60%、调压器铭牌 0–270 V/10 A 与约 470 V/10 A、电压回路用细线的举例）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '导线、导体与自耦调压器',
    "edition": "原著版",
    "points": {
        'K1': '本课内容',
        'K2': '导体：自由电子多',
        'K3': '电导是电阻的倒数',
        'K4': '铜导线',
        'K5': '铝导线',
        'K6': '按载流量选截面',
        'K7': '镀锌铁线',
        'K8': '良导体、不良导体、非导体',
        'K9': '常用绝缘材料',
        'K10': '实心线、绞合线、多股线、软线',
        'K11': '单芯与双芯',
        'K12': '粗线电阻小',
        'K13': '导线等于导体加绝缘层',
        'K14': '绝缘层的作用',
        'K15': '按电路选导线',
        'K16': '自耦调压器：一个绕组',
        'K17': '原副边相连，不隔离',
        'K18': '调节线路电压',
        'K19': '单相调压器的接法',
        'K20': '单相与三相调压器',
        'K21': '调压器的别名',
        'K22': '本课回顾',
    },
    "avoid": ['VTU', 'Visvesvaraya', 'Simplified EEE Studies', 'Simplified EEE', 'HELUKABEL', 'dimmerstat', 'Dimmer Stat'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台边，台上有一卷卷彩色导线和一台带旋钮的圆形调压器，向镜头招手', 'The panda mascot stands beside a lab bench with coils of colored wire and a round variable autotransformer with a big knob, waving at the camera.', '这一课认识导线、导体和自耦调压器。', '导线、导体与自耦调压器'),
('开场', '导体、绝缘层、导线、调压器四个图标', 'Four icons in a row: a copper strand, an insulating sleeve, a coiled wire and a round voltage regulator with a knob. No people.', '导体、绝缘、导线、调压器。', '', ['导体', '绝缘', '导线', '调压器']),
# 情景
('情景', '阿杰面对一桌粗细不同的彩色导线，拿起一根又放下', 'The young male student faces a bench full of colored wires of different thicknesses, picking one up and putting it down, unsure.', '阿杰看着一桌导线，不知道该用哪根。'),
('情景', '阿杰指着圆形调压器的旋钮，一脸疑问', 'The young male student points at the knob of a round variable autotransformer with a puzzled look.', '旁边这个带旋钮的圆盒子，又是什么？'),
('情景', '小研拿起两根导线比较粗细', 'The female graduate student holds up two wires side by side to compare their thickness.', '小研说：先弄懂导体、导线和调压器。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '导线和调压器，看着简单，学问不少。'),
# K1
('K1', '欣欣依次指向四个图标', 'The panda mascot points one by one at four icons: a conductor, an insulator, a wire and an autotransformer.', '先讲导体和绝缘，再讲导线和调压器。', '本课内容'),
# K2
('K2', '金属里很多自由移动的小圆点', 'An icon of a metal block with many small free-moving dots inside, arrows showing them drifting. No people.', '导体里的自由电子多，容易导电。', '导体：自由电子多'),
('K2', '左边圆点密集标绿勾，右边圆点稀少标黄色', 'Two blocks side by side: left packed with free dots and a green check, right with few dots and a yellow mark. No people.', '电子多，电阻小；电子少，电阻大。', '', ['良导体', '不良导体']),
# K3
('K3', '电阻符号和倒数箭头指向电导符号', 'A resistor symbol with a flip arrow pointing to a conductance symbol. No people.', '电导是电阻的倒数。', '电导是电阻的倒数'),
('K3', '一张空白卡片上有单位图示', 'A blank card with a unit icon. No people.', '单位是西门子，旧称姆欧。', '', ['西门子 S']),
# K4
('K4', '一卷闪亮的铜线', 'A shiny coil of copper wire on a bench. No people.', '铜线导电好，好焊接。', '铜导线'),
('K4', '铜线卷放在天平一侧较重，旁边有钱币图标', 'A copper coil on a balance scale tipping down, next to a coin stack icon. No people.', '缺点是重一些、贵一些。'),
('K4', '房屋图标里的墙内布线', 'A house icon with wiring routes drawn inside the walls. No people.', '家里布线常用铜线。'),
# K5
('K5', '一卷银灰色铝线，轻轻浮在天平上', 'A coil of silver-grey aluminum wire on a balance scale tipping up, lighter. No people.', '铝线便宜又轻。', '铝导线'),
('K5', '铜和铝两根导电柱，铝的约为铜的六成', 'Two conductivity bars: a copper bar full height and an aluminum bar about sixty percent as tall. No people.', '导电率大约是铜的六成。', '', ['铝≈铜的60%']),
# K6
('K6', '粗细不同的四根导线截面圆，从小到大排开', 'Four wire cross-section circles of increasing size in a row. No people.', '截面有 1、1.5、4、6 平方毫米等规格。', '按载流量选截面', ['1', '1.5', '4', '6 mm²']),
('K6', '电流箭头穿过导线，粗电流配粗线', 'Current arrows passing through wires; the thick arrow goes through the thick wire. No people.', '电流大，就选截面大的导线。'),
('K6', '电压表回路接细线，电流回路接粗线', 'A circuit icon: thin wires leading to a voltmeter, thick wires in the main current loop with an ammeter. No people.', '比如测电压的回路用细线，电流回路用粗线。'),
# K7
('K7', '一卷灰色镀锌铁线', 'A coil of dull grey galvanized iron wire. No people.', '镀锌铁线：重，导电最差。', '镀锌铁线'),
('K7', '架空线和接地极两个图标', 'Two icons: overhead line poles with wires, and an earth rod in the ground. No people.', '多用在架空线和接地。'),
# K8
('K8', '铜铝导线图标打绿勾', 'Icons of copper and aluminum wires with a green check. No people.', '铜、铝是良导体，电阻小，用来输电。', '良导体、不良导体、非导体'),
('K8', '发光的灯丝和发红的电热丝', 'Icons of a glowing lamp filament and a red-hot heating coil. No people.', '钨丝、镍铬丝电阻较大，用来发热发光。'),
('K8', '塑料管和玻璃瓶图标', 'Icons of plastic pipes and a glass bottle. No people.', '塑料、玻璃几乎不导电，用来绝缘。'),
('K8', '导线剖面：中间铜芯，外面塑料皮', 'A cutaway icon of a wire: copper core in the middle, plastic sleeve outside. No people.', '电线把导体和绝缘体组合起来。'),
# K9
('K9', 'PVC、橡胶两种绝缘层样品，天然橡胶打黄色问号', 'Samples of PVC insulation and vulcanized rubber insulation with green checks, and natural rubber with a yellow question mark. No people.', '绝缘层常用塑料和硫化橡胶。', '常用绝缘材料'),
('K9', '天然橡胶样品打叉', 'A natural rubber sample crossed out with a red X. No people.', '天然橡胶不宜作导线绝缘。'),
# K10
('K10', '一根粗实心铜芯的剖面', 'A cross-section of a wire with one solid copper core. No people.', '实心导线，一根铜芯，常用在电缆里。', '实心线、绞合线、多股线、软线'),
('K10', '几股铜丝绞在一起的导线，轻松弯曲', 'A wire made of several copper strands twisted together, bending easily. No people.', '绞合导线有 1、7、19、37 股，最常用。', '', ['1/7/19/37 股']),
('K10', '绞合导线旁边一把卡尺图标', 'A stranded wire next to a caliper icon. No people.', '整根直径大约 1.13 到 3.73 毫米，比单根软。', '', ['1.13–3.73mm']),
('K10', '很多细铜丝组成的多股线', 'A wire made of many fine copper strands. No people.', '多股导线单丝约零点二到零点三毫米，载流更好。', '', ['单丝0.2–0.3mm']),
('K10', '极细铜丝组成的软线，可绕成圈', 'A flexible cord of very fine copper strands, coiled into a loop. No people.', '软线有 14、23、40 股，单丝更细。', '', ['14/23/40 股', '单丝<0.2 mm']),
('K10', '小研在空白订货单上写股数', 'The female graduate student writes on a blank order form next to a coil of flexible cord.', '订购软线时，要说明股数。'),
# K11
('K11', '三根导线：单芯单股、单芯多股、双芯多股', 'Three wire icons: single core single strand, single core multi-strand, and two-core multi-strand. No people.', '还有单芯单股、单芯多股、双芯多股。', '单芯与双芯'),
# K12
('K12', '公式卡：电阻等于电阻率乘长度除以截面', 'A blank card with a formula icon showing resistance proportional to length over area. No people.', '电阻跟长度成正比，跟截面成反比。', '粗线电阻小', ['R=ρL/A']),
('K12', '大截面圆打绿勾标低电阻，小截面圆标高电阻', 'Two cross-section circles: a large one labeled low resistance, a small one labeled high resistance. No people.', '截面大，电阻小；截面小，电阻大。', '', ['粗→电阻小', '细→电阻大']),
('K12', '长导线和短导线对比', 'A long wire and a short wire side by side, the long one with a bigger resistance symbol. No people.', '导线越长，电阻越大。'),
# K13
('K13', '导线剖面：铜芯 + 外皮，加号连接', 'An icon equation: a copper core plus an insulating sleeve equals a finished wire. No people.', '导线，就是导体加绝缘层。', '导线等于导体加绝缘层', ['导体', '绝缘层']),
('K13', '铝芯和铜芯两根导线对比', 'Two wires: one with an aluminum core and a coin icon, one with a copper core and a lightning icon. No people.', '图省钱选铝，要导电好选铜。'),
# K14
('K14', '电流箭头只在铜芯里流动，外皮挡住', 'Current arrows flowing only inside the copper core while the insulation sheath blocks them. No people.', '绝缘层让电流只在导体里走，保证安全。', '绝缘层的作用'),
('K14', '小研捏着导线绝缘外皮插入接线孔', 'The female graduate student holds a wire by its insulation and plugs it into a terminal.', '也方便用手拿取和接线。'),
# K15
('K15', '实验台上一排不同颜色、长短的连接导线', 'A rack of connecting leads in different colors and lengths on a lab bench. No people.', '连接导线种类多，按电路选用。', '按电路选导线'),
# K16
('K16', '圆形调压器剖面：一个线圈绕在铁心上，有滑动触点', 'A cutaway of a round variable autotransformer: a single coil wound on a laminated iron core with a sliding contact. No people.', '自耦调压器只有一个绕组。', '自耦调压器：一个绕组'),
('K16', '转动旋钮，输出电压条平滑上升', 'An icon of a knob turning and an output bar rising smoothly. No people.', '转动旋钮，交流电压平滑可调。'),
# K17
('K17', '单个绕组上，输入和输出共用一部分线圈', 'A single winding icon where input and output share part of the same coil. No people.', '它和普通变压器相似，但原副边绕组相连。', '原副边相连，不隔离'),
('K17', '普通变压器两个独立线圈 vs 自耦变压器一个线圈', 'Comparison icons: a two-winding transformer with two separate coils, and an autotransformer with one coil. No people.', '缺点是很难做到隔离。', '', ['双绕组', '自耦']),
('K17', '铜线卷变小、钱币图标', 'A smaller copper coil icon next to a coin icon. No people.', '好处是省铜、经济。'),
# K18
('K18', '电压指针在设定线附近保持稳定', 'A voltage gauge needle holding steady at a set line while input arrows vary. No people.', '它用来调整电压，或让电压保持稳定。', '调节线路电压'),
# K19
('K19', '单相调压器正面：输入插头、两个输出接线柱、旋钮和刻度', 'The front of a single-phase variable autotransformer: a power cord with plug, two output terminals, a big knob and a blank dial scale. No people.', '单相调压器：插头接电源输入。', '单相调压器的接法'),
('K19', '输入端标相线和中性线两个空白标签', 'The input side of the autotransformer with two blank tags for line and neutral. No people.', '输入端分相线和中性线。', '', ['相线 L', '中性线 N']),
('K19', '旋钮转动，输出端电压随刻度变化', 'The knob turning and the dial pointer moving, an arrow from the output terminals. No people.', '转旋钮，输出端电压随之改变。'),
# K20
('K20', '一台圆形单相调压器和一台高大的三相调压器并排', 'A round single-phase variable autotransformer next to a tall three-phase one. No people.', '调压器有单相和三相两种。', '单相与三相调压器', ['单相', '三相']),
('K20', '三相电路图标连到三相调压器', 'A three-phase circuit icon linked to the three-phase variable autotransformer. No people.', '测三相功率，就要用三相调压器。'),
('K20', '单相调压器的空白铭牌，旁边是电压和电流图标', 'The single-phase unit with a blank nameplate, voltage and current icons beside it. No people.', '单相的举例：零到二百七十伏，十安。', '', ['0–270 V', '10 A']),
('K20', '三相调压器的空白铭牌，旁边是电压和电流图标', 'The three-phase unit with a blank nameplate, voltage and current icons beside it. No people.', '三相的约四百七十伏、十安，容量各不同。', '', ['约470 V', '10 A']),
# K21
('K21', '欣欣拿着调压器的空白名牌', 'The panda mascot holds a blank name tag beside a variable autotransformer.', '自耦调压器，实验室常简称调压器。', '调压器的别名'),
# K22
('K22', '导体、导线、调压器三个图标依次亮起', 'Three icons light up one by one: a conductor, a wire and an autotransformer. No people.', '导体、绝缘、导线规格和调压器，都讲了。', '本课回顾'),
# 小结
('小结', '铜、铝、铁三种导线和截面圆', 'Three coils of copper, aluminium and galvanized iron wire with cross-section circles. No people.', '按材料和载流量选导线，粗线电阻小。', '小结'),
('小结', '导线剖面：导体加绝缘层，旁边几种结构', 'A wire cross-section of conductor plus insulation, beside solid, stranded and flexible wire icons. No people.', '导线是导体加绝缘，结构规格各不同。'),
('小结', '调压器旋钮和单相、三相两个图标', 'A variable autotransformer knob with single-phase and three-phase icons. No people.', '调压器一个绕组，平滑调电压。'),
# 结尾
('结尾', '欣欣在整齐的导线架和调压器旁挥手道别', 'The panda mascot waves goodbye beside a tidy wire rack and a variable autotransformer.', '认识了导线和调压器，下次见！'),
]
