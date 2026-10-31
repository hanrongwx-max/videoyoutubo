# 01_Innovative Laser Cutting Industrial Jan2020SloMo MusicCam Vizion wwwPhoto 卡通剧本作者源
# 原著版：完全照原片（35 秒宣传短片，无讲解，只有成品与切割画面），K1–K5，不加补充知识点、不做更正；
# 原片只展示工艺：成批定制零件、慢动作切割火花、压力表与格栅台、打标、按图核对；原片没有安全讲解，本版也不加
# 企业名、网址、客户标志、电话和专利号不出现；原片不足 2 分钟，只复述原片画面内容补足时长
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "看懂激光切割，也看懂它的危险",
    "edition": "原著版",
    "points": {
        "K1": "激光切割能做什么",
        "K2": "切割时发生了什么",
        "K3": "切割头、压力表和格栅台",
        "K4": "激光打标，便于追溯",
        "K5": "成品按图核对",
    },
    "avoid": ["Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "Laser Maintenance Group", "LMG", "Cam Vizion", "Vizion", "Kiser"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台工业激光切割机旁，向镜头招手",
 "The panda mascot stands beside a large industrial laser cutting machine and waves at the camera.",
 "今天带大家看看工业激光切割。", "看懂激光切割，也看懂它的危险"),
("开场", "金属零件、切割头、火花、打标四个图标排成一行",
 "Four icons in a row: a metal part, a laser cutting head, flying sparks and an engraved part. No people.",
 "看它怎么切零件，怎么打标。", "", ["零件", "切割", "打标"]),
# 情景
("情景", "阿杰和小研站在桌边，看着图纸上几叠金属零件",
 "The young male student and the female graduate student stand at a bench looking at stacks of metal parts on blank drawings.",
 "阿杰和小研收到一批金属零件。"),
("情景", "阿杰拿起一块连接板，满脸好奇",
 "The young male student picks up a metal strip with holes and looks at it curiously.",
 "边缘这么整齐，是怎么切出来的？"),
("情景", "老李招手，带两人走向车间里的激光切割机",
 "The facility engineer waves and leads the two students toward a laser cutting machine in a workshop.",
 "老李带他们去看激光切割机。"),
# K1
("K1", "图纸上摆着几叠切好的垫片、连接板和方框件",
 "Several neat stacks of laser-cut metal parts on blank engineering drawings: round washers, long plates with holes and square frame pieces. No people.",
 "激光切割能按图纸切出各种金属件。", "激光切割能做什么"),
("K1", "垫片、长条连接板、方框厚件三个图标",
 "Three icons: a round washer, a long plate with holes and a thick square frame piece. No people.",
 "垫片、连接板、支架，还有厚板件。", "", ["垫片", "连接板", "厚板件"]),
("K1", "一叠形状完全相同的长条连接板",
 "Close-up of a tall stack of identical metal strips with matching holes and chamfered ends. No people.",
 "成批切出，大小孔位都一样。"),
("K1", "小研拿起一个垫片，与旁边的图纸比对",
 "The female graduate student picks up a metal washer and compares it with a blank drawing on the bench.",
 "按需定制，图纸画什么就切什么。"),
# K2
("K2", "示意图：一束光从切割头向下聚成一点，落在钢板上",
 "A simple diagram: a light beam inside a cutting head narrows down to a bright focal point on a steel sheet. No people.",
 "激光聚焦在切割头下方的板材上。", "切割时发生了什么"),
("K2", "钢板上的亮点处金属熔化，气流向下吹出熔渣",
 "A cross-section diagram: metal melts at the bright spot and a downward gas stream blows molten droplets through the cut. No people.",
 "金属熔化，被气流从切口吹走。"),
("K2", "慢动作：切割头下火花向四周飞溅",
 "Slow motion: orange sparks spray outward from under a laser cutting head on a steel sheet. No people.",
 "慢动作里，切口处火花四溅。"),
("K2", "切割头在钢板上切出一个圆孔，火花呈弧线飞散",
 "Close-up: a cutting head cuts a round hole in a steel sheet, orange sparks flying in arcs. No people.",
 "切直线、切圆孔，火花跟着走。"),
# K3
("K3", "切割头特写：机头上有一块圆形压力表",
 "Close-up of a cutting head with a round analog pressure gauge with a blank dial. No people.",
 "切割头旁有辅助气体压力表。", "切割头、压力表和格栅台"),
("K3", "老李指着压力表给阿杰看",
 "The facility engineer points at the pressure gauge on the cutting head while the young male student looks.",
 "吹走熔渣的气流，压力看这块表。"),
("K3", "钢板平放在一排排带长条孔的格栅台面上",
 "A steel sheet lies flat on a slatted grid table with rows of long slots. No people.",
 "板材放在格栅式工作台上。"),
("K3", "剖面图：熔渣从切口落进台面下方的通道",
 "A cross-section diagram: molten slag drops through the cut into a channel under the grid table. No people.",
 "台面下方留出通道，排出熔渣。"),
# K4
("K4", "L形金属支架表面刻着空白图标和一串点线",
 "Close-up of an L-shaped steel bracket with a laser-engraved blank logo shape and a dotted line pattern, no readable text. No people.",
 "激光还能在零件表面打标。", "激光打标，便于追溯"),
("K4", "圆形垫片上刻着标志和编号的形状",
 "A round metal washer with an engraved blank logo shape and a row of small engraved marks, no readable text. No people.",
 "刻上标志、文字和编号。", "", ["标志", "文字", "编号"]),
("K4", "装上拨动开关的L形支架，一个零件连到空白记录册",
 "An L-shaped bracket fitted with a toggle switch, and an arrow from the engraved part to a blank record book. No people.",
 "装到产品上，一看就能识别追溯。"),
# K5
("K5", "老李把切好的零件按批码放，逐件对照图纸",
 "The facility engineer stacks finished parts in batches and checks each against a blank drawing.",
 "切好的零件按批次堆放。", "成品按图核对"),
("K5", "小研把零件放到图纸上比对，打勾后装箱",
 "The female graduate student lays a part on a blank drawing, gives a check mark, then packs the parts into a box.",
 "与图纸核对无误后交付。"),
# 小结
("小结", "欣欣身旁浮现零件、切割头、格栅台、打标四个图标",
 "The panda mascot stands beside four icons: metal parts, a cutting head, a grid table and an engraved part.",
 "按图成批切零件，激光熔化气流吹渣。", "小结"),
("小结", "阿杰和小研看着整齐的零件点头",
 "The young male student and the female graduate student nod while looking at neat stacks of finished parts.",
 "看压力表，格栅排渣，打标追溯。"),
# 结尾
("结尾", "欣欣和阿杰、小研、老李在切割机旁挥手",
 "The panda mascot waves goodbye with the young male student, the female graduate student and the facility engineer beside the laser cutting machine.",
 "激光切割就看到这里，下次见！"),
]
