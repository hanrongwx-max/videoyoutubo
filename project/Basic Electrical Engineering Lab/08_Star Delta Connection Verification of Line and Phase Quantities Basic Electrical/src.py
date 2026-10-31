# 08_Star Delta Connection Verification of Line and Phase Quantities Basic Electrical 卡通剧本作者源
# 原著版：完全照原片（三盏灯作三相负载的星形、三角形连接，验证线量与相量关系：接线、调压器升压、读数、回零断闸、结论），K1–K24，
# 不加补充知识点、不做本土化和更正（保留 R、Y、B 相标，415 V 50 Hz、15 A 熔断器、470 V 10 A 调压器、100 W 灯，星形升到约 400 V、三角形约 230 V，讲者对星形/三角形用途的说法）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '三相星形与三角形连接实验',
    "edition": "原著版",
    "points": {
        'K1': '实验目的',
        'K2': '星形：同名端接成星点',
        'K3': '星形的用途',
        'K4': '三盏灯代表三相负载',
        'K5': '三相电源与保护',
        'K6': '三相调压器',
        'K7': '星形接线',
        'K8': '线电压：两线之间',
        'K9': '相电压：一线与中性点之间',
        'K10': '星形：线电流等于相电流',
        'K11': '电路图要标额定值',
        'K12': '认识实物',
        'K13': '先断开、先回零，再合闸升压',
        'K14': '读数并记录',
        'K15': '先回零，再断闸',
        'K16': '三角形：首尾相连成闭环',
        'K17': '三角形的用途',
        'K18': '三角形接线',
        'K19': '测相电流，线电压即相电压',
        'K20': '三相电，安全措施要做足',
        'K21': '三角形只升到较低电压',
        'K22': '三角形的读数',
        'K23': '实验结论',
        'K24': '理解为什么这样接',
    },
    "avoid": ['VTU', 'Visvesvaraya', 'legrand', 'DIMMERSTAT', 'Automatic Electric', 'AE', 'R Y B'],
}

SHOTS = [
# 开场
('开场', '欣欣站在实验台旁，台上三盏灯泡、一台高大的三相调压器、几只电表，向镜头招手', 'The panda mascot stands beside a lab bench with three light bulbs on a board, a tall three-phase variable autotransformer and several analog meters, waving at the camera.', '这一课做三相星形和三角形连接实验。', '三相星形与三角形连接实验'),
('开场', '星形和三角形两个连接图标', 'Two icons: three loads joined at a center point in a star shape, and three loads joined end to end in a triangle. No people.', '看看线电压、相电压，线电流、相电流。', '', ['星形 Y', '三角形 Δ']),
# 情景
('情景', '阿杰看着课本上的星形和三角形两个图，挠头', 'The young male student looks at star and triangle connection icons in a blank textbook and scratches his head.', '阿杰背不住星形三角形的电压电流关系。'),
('情景', '小研指向实验台上的三盏灯和三相调压器', 'The female graduate student points to three lamps and a tall three-phase variable autotransformer on the bench.', '小研说：到实验室亲手测一测。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '理论课学的关系，今天来验证。'),
# K1
('K1', '一本空白理论书和一块实验板用箭头连起来', 'A blank textbook and a three-lamp experiment board linked by an arrow. No people.', '目的：在实验室验证星形三角形的关系。', '实验目的'),
# K2
('K2', '三个线圈的末端连在同一点', 'A diagram of three coils whose ending terminals are all joined at one center point. No people.', '星形：三个线圈的同名端接在一起。', '星形：同名端接成星点'),
('K2', '中心点被圈出并发光', 'The center joining point of the star diagram circled and glowing. No people.', '这一点叫中性点，也叫星点。', '', ['中性点', '星点']),
# K3
('K3', '星形图标旁，电压箭头长、电流箭头短', 'A star connection icon with a long voltage arrow and a short current arrow beside it. No people.', '星形用在需要高电压、小电流的负载。', '星形的用途'),
# K4
('K4', '透明板上三盏灯，每盏灯两端标首端和末端', 'Three incandescent lamps on a transparent board, each with two terminals. No people.', '用三盏一百瓦的灯代表三相负载。', '三盏灯代表三相负载', ['100 W ×3', 'A1-A2', 'B1-B2', 'C1-C2']),
('K4', '三盏灯的末端用导线连在一起', 'The far ends of the three lamps joined together with wires. No people.', 'A2、B2、C2 连起来，就是中性点。'),
# K5
('K5', '墙上配电箱：三极开关和熔断器，三根线引出', 'A wall distribution box with a three-pole switch and fuses; three supply lines lead out. No people.', '三相电源 R、Y、B，四百一十五伏、五十赫兹。', '三相电源与保护', ['R', 'Y', 'B', '415 V 50 Hz']),
('K5', '熔断器和三极开关被高亮', 'The fuses and the three-pole single-throw switch highlighted in the box. No people.', '经十五安熔断器和三极开关引出。', '', ['15 A 熔断器', '三极开关']),
# K6
('K6', '高大的三相调压器，正面输入、输出两组端子，顶部旋钮', 'A tall three-phase variable autotransformer with input and output terminal groups and a top knob. No people.', '电源接三相调压器输入，四百七十伏、十安。', '三相调压器', ['输入', '输出', '470 V 10 A']),
('K6', '旋钮转动，三根输出电压条一起从零上升', 'The knob turns and three output voltage bars rise together from zero. No people.', '调压器能让三相电压从零平滑调高。'),
# K7
('K7', '电路图：调压器输出 1 经电流表接 A1', 'A circuit diagram icon: output one of the autotransformer goes through an ammeter to terminal A1. No people.', '输出一经电流表接 A1。', '星形接线', ['电流表']),
('K7', '输出 2、3 分别接 B1、C1，A2、B2、C2 连成星点', 'The diagram continues: outputs two and three go to B1 and C1, and A2, B2, C2 are joined at the star point. No people.', '输出二接 B1，输出三接 C1。'),
# K8
('K8', '一只电压表跨在两根线之间', 'A voltmeter connected between two of the three line wires in the diagram. No people.', '线电压：任意两根线之间的电压。', '线电压：两线之间', ['线电压']),
# K9
('K9', '另一只电压表接在一根线和星点之间', 'A second voltmeter connected between one line wire and the star point. No people.', '相电压：一根线和中性点之间的电压。', '相电压：一线与中性点之间', ['相电压']),
# K10
('K10', '星形中一根线上的电流箭头直接流进一盏灯', 'A star diagram where the current arrow in one line flows straight into one lamp with no branch. No people.', '星形里，线电流就是相电流。', '星形：线电流等于相电流'),
('K10', '只有一只电流表打绿勾', 'A single ammeter icon with a green check. No people.', '所以只用一只电流表就够了。'),
# K11
('K11', '小研在空白报告纸上画电路图并标注', 'The female graduate student draws a neat circuit diagram on a blank report sheet and adds small rating tags.', '考试时电路图要画清楚，标明额定值。', '电路图要标额定值'),
# K12
('K12', '镜头扫过调压器、配电箱、三盏灯和三只表', 'A panning view over the three-phase autotransformer, the wall distribution box, the three bulbs and three analog meters. No people.', '调压器、三极开关、三盏灯、三只表。', '认识实物'),
('K12', '两只电压表一只电流表并排，表盘空白', 'Two voltmeters and one ammeter side by side with blank dials. No people.', '一只测线电压，一只测相电压，一只测电流。'),
# K13
('K13', '三极开关在断开位置，调压器旋钮在零位，各打绿勾', 'The three-pole switch in the off position and the autotransformer knob at zero, each with a green check. No people.', '开始时：开关断开，调压器在最小位置。', '先断开、先回零，再合闸升压', ['开关断开', '调压器最小']),
('K13', '老周合上三极开关', 'The older man closes the three-pole switch on the distribution box.', '按图接好线，再合闸。'),
('K13', '老周盯着电压表慢慢转动调压器旋钮', 'The older man slowly turns the autotransformer knob while watching the voltmeter.', '慢慢升到所需线电压，约四百伏。', '', ['约400 V']),
# K14
('K14', '电压表接线柱被圈出，箭头指向上刻度', 'A voltmeter terminal circled with an arrow pointing to the upper scale. No people.', '按所接量程，读上刻度或下刻度。', '读数并记录'),
('K14', '三盏灯亮起，小研在空白表格上记录', 'Three lamps glow while the female graduate student writes in a blank table.', '记下线电压、相电压，线电流约零点四安。', '', ['约0.4 A']),
# K15
('K15', '调压器旋钮转回零，再拉下三极开关', 'An icon sequence: the autotransformer knob turned back to zero, then the three-pole breaker switched off. No people.', '读完先把调压器调回零，再断闸。', '先回零，再断闸', ['1 回零', '2 断闸']),
# K16
('K16', '三个线圈首尾相连成三角形', 'A diagram of three coils where the end of each coil joins the start of the next, forming a closed triangle. No people.', '三角形：一相末端接下一相首端。', '三角形：首尾相连成闭环'),
('K16', '沿三角形画出一个闭合的箭头环', 'A closed loop arrow traced around the triangle. No people.', '三相首尾相连，形成闭合回路。'),
# K17
('K17', '三角形图标旁，电流箭头长、电压箭头短', 'A triangle connection icon with a long current arrow and a short voltage arrow beside it. No people.', '三角形正相反，用在大电流、低电压的负载。', '三角形的用途'),
# K18
('K18', '电路图：调压器三路输出经电流表分别接 A1、B1、C1', 'A circuit diagram icon: the three autotransformer outputs go to A1, B1 and C1, the first through an ammeter. No people.', '调压器三路输出，分别接三个首端。', '三角形接线'),
('K18', 'A2 接 B1、B2 接 C1、C2 接 A1 的连线依次亮起', 'The links A2 to B1, B2 to C1 and C2 to A1 light up in turn. No people.', '末端接下一相首端，连成三角形。', '', ['A2→B1', 'B2→C1', 'C2→A1']),
# K19
('K19', '第二只电流表串在一相负载里', 'A second ammeter placed inside one side of the triangle, in series with one lamp. No people.', '另一只电流表串在一相里，测相电流。', '测相电流，线电压即相电压', ['线电流', '相电流']),
('K19', '电压表跨在一盏灯两端，同时也跨在两根线之间', 'A voltmeter across one lamp, which is also across two line wires. No people.', '三角形里，线电压就是相电压。'),
# K20
('K20', '王老师指着三相配电箱，旁边警示标志', 'The safety administrator points at the three-phase distribution box next to an electrical hazard warning sign.', '三相电，安全措施一定要做足。', '三相电，安全措施要做足'),
('K20', '老李逐个按紧接线柱，检查导线插牢', 'The facility engineer presses each terminal and checks that every lead is firmly plugged in.', '严格按图接线，接头要牢固。'),
# K21
('K21', '老周合闸后慢慢转动调压器，电压表指针停在较低位置', 'After switching on, the older man slowly turns the autotransformer; the voltmeter needle stops low on the scale.', '三角形时，合闸后慢慢升压，只升到约二百三十伏。', '三角形只升到较低电压', ['约230 V']),
('K21', '两只电流表同时偏转', 'Two ammeters deflect at the same time. No people.', '读出线电流和相电流。'),
# K22
('K22', '两只电流表读数不同', 'Two ammeters side by side showing different needle positions. No people.', '线电流和相电流，读数不一样。', '三角形的读数'),
('K22', '调压器回零，开关断开，小研记录', 'The autotransformer knob back at zero and the breaker off, while the female graduate student writes in a blank table.', '读完回零断闸，把数据填进表。'),
# K23
('K23', '星形卡片：线电流等于相电流，线电压是相电压的根号三倍', 'A blank card with a star icon and two relation icons: equal currents, and voltage with a square root of three. No people.', '星形：电流相等，线电压是相电压的√3倍。', '实验结论', ['Y：IL=Iph', 'Y：VL=√3Vph']),
('K23', '三角形卡片：线电压等于相电压，线电流是相电流的根号三倍', 'A blank card with a triangle icon and two relation icons: equal voltages, and current with a square root of three. No people.', '三角形：电压相等，线电流是相电流的√3倍。', '', ['Δ：VL=Vph', 'Δ：IL=√3Iph']),
# K24
('K24', '阿杰看着两张卡片若有所思', 'The young male student studies the two cards thoughtfully.', '想一想：什么时候用星形，什么时候用三角形？', '理解为什么这样接'),
# 小结
('小结', '星形和三角形两张结论卡', 'Two conclusion cards: star and triangle connection icons. No people.', '星形电流相等，三角形电压相等。', '小结'),
('小结', '开关断开、旋钮归零、慢慢升压、先回零再断闸四个图标', 'Four icons: switch off, knob at zero, slowly raising voltage, knob back to zero then switch off. No people.', '断开回零再合闸，慢升压，先回零再断闸。'),
('小结', '按图接线、接头牢固两个打勾图标', 'Two icons with green checks: wiring by diagram and a firmly tightened terminal. No people.', '三相电要按图接线，接头牢固。'),
# 结尾
('结尾', '欣欣站在旋钮归零的三相实验台前挥手道别', 'The panda mascot waves goodbye in front of a three-phase lab bench with the knob at zero.', '星形三角形，都验证了，下次见！'),
]
