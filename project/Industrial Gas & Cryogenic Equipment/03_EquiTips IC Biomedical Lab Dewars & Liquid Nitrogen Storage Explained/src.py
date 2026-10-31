# 03 液氮杜瓦罐 原著版卡通剧本作者源
# 完全照原片：液氮罐厂家的推广短视频，K1–K6（液氮罐与取液器、从小到大的容量、带相分离器的出液嘴、拆出液嘴接软管充装、
# 工厂喷涂与“美国制造”、到经销商购买），无补充知识点；原片无人实际操作、未讲冻伤窒息等，剧本同样不加；品牌、人名、电话不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室杜瓦瓶与液氮储存解析",
    "edition": "原著版",
    "points": {
        "K1": "实验室液氮杜瓦罐用于储存和转运液氮，配套的液体取出器用于安全取出液氮",
        "K2": "液氮罐有从小到大的多种容量规格，应按用量选择",
        "K3": "取液器装在储罐上，出液嘴带相分离器，使液氮平稳流出、减少飞溅",
        "K4": "充装时尽量少拆装取液器：不拆整个取液器、经接口接软管充装，更快、更安全，也减少部件磨损",
        "K5": "储罐由专门工厂制造、经表面处理（原片以喷涂镜头和“美国制造”表现产地）",
        "K6": "液氮罐和配件应从正规渠道采购",
    },
    "avoid": ["EquiTips", "Equi-Tips", "EquiGas", "Equigas", "Equigash", "IC Biomedical", "ICBiomedical",
              "Biomedical", "Jada Collett", "Collett", "Niko Arevalo", "Nico Arvelo", "Arvelo", "Arevalo",
              "LD", "Made in USA", "Made in the USA", "Made in America", "844"],
}

SHOTS = [
# 开场
("开场", "欣欣站在展台旁，桌上一排大小不同的银色液氮罐，向镜头招手",
 "The panda mascot stands at an exhibition table lined with silver liquid nitrogen dewars of different sizes and waves at the camera.",
 "欢迎来到设备小课堂，今天看液氮罐。", "液氮杜瓦罐的安全使用"),
("开场", "小研走过来，和欣欣握手寒暄",
 "The female graduate student walks over and shakes hands with the panda mascot in a friendly greeting.",
 "嘉宾小研，是液氮罐厂家的销售代表。"),
# 情景
("情景", "阿杰站在展台前，看着一排银色罐子发呆",
 "The young male student stands in front of the exhibition table, staring at the row of silver dewars with a puzzled look.",
 "阿杰的实验室要买液氮罐，不知道怎么挑。"),
("情景", "欣欣招手让阿杰一起听",
 "The panda mascot waves the young male student over to listen in.",
 "一起来听听厂家怎么介绍。"),
# K1
("K1", "小研指着桌上的银色液氮罐",
 "The female graduate student points to the silver dewars on the table.",
 "小研说，他们专做液氮杜瓦罐，", "液氮杜瓦罐与液体取出器"),
("K1", "一个带压力表、阀门和长取液管的取液器图示",
 "A diagram of a liquid withdrawal device with a blank pressure gauge, a small valve and a long dip tube. No people.",
 "还有配套的液体取出器。", "", ["压力表", "阀门", "取液管"]),
("K1", "液氮罐从库房被推到实验室的箭头示意",
 "An arrow diagram of a dewar being wheeled from a storage room to a laboratory bench. No people.",
 "罐子用来储存和转运液氮。"),
("K1", "取液器装在罐口，液氮经管子流出的示意",
 "A diagram of a withdrawal device mounted on a dewar neck with liquid nitrogen flowing out through a tube. No people.",
 "取液器借助罐内压力，把液氮取出来。"),
# K2
("K2", "桌上的液氮罐从小到大依次排开",
 "Silver dewars lined up on the table from the smallest to the largest. No people.",
 "桌上这一排，是从小到大的系列。", "多种容量规格"),
("K2", "欣欣手捧一套取液器，小研指向其中一只大罐",
 "The panda mascot holds a liquid withdrawal device while the female graduate student points to one of the larger dewars.",
 "这只三十五升的罐上，就装着取液器。", "", ["35升"]),
("K2", "小罐、中罐、大罐三个图标旁各有一个用量刻度",
 "Three dewar icons small, medium and large, each beside a blank usage gauge. No people.",
 "用多少液氮，就挑多大的罐。"),
# K3
("K3", "小研走到装有取液器的罐旁，指着出液嘴",
 "The female graduate student walks to the dewar fitted with a withdrawal device and points to its outlet spout.",
 "关键在出液嘴，里面内置相分离器。", "出液嘴带相分离器"),
("K3", "相分离器剖面示意：气体从侧面排走，液体平稳流下",
 "A cutaway diagram of a phase separator: vapor escapes from side vents while liquid flows down smoothly. No people.",
 "气液分开，液氮流得平稳、少飞溅。", "", ["气体排出", "液体流出"]),
# K4
("K4", "图标：整个取液器被拔出罐口，旁边一个扳手",
 "An icon of a whole withdrawal device being pulled out of a dewar neck next to a wrench icon. No people.",
 "市面上别的产品，要先拆下整个取液器", "充装时少拆装取液器"),
("K4", "拆下的取液器放在一旁，再往罐里灌液氮的图标",
 "An icon of the removed withdrawal device set aside while liquid nitrogen is poured into the open dewar. No people.",
 "才能往罐里充装液氮。"),
("K4", "小研演示：只拧下出液嘴，接上一根软管",
 "The female graduate student demonstrates unscrewing only the outlet spout and attaching a transfer hose to the port.",
 "他们的只要拆下出液嘴，接上软管就能灌。"),
("K4", "秒表、盾牌、齿轮三个图标",
 "Three icons: a stopwatch, a shield with a check mark and a gear with a small wear mark. No people.",
 "充得更快，更安全，取液器也少磨损。", "", ["更快", "更安全", "少磨损"]),
("K4", "欣欣点头竖起大拇指",
 "The panda mascot nods and gives a thumbs up.",
 "欣欣说：听起来是个好产品。"),
# K5
("K5", "喷涂间里，戴白色送风式头罩和蓝手套的工人向转台上的银色罐体喷漆",
 "In a paint booth, a worker in a white supplied-air hood and blue gloves sprays coating onto a silver tank body on a turntable.",
 "罐子在专门的工厂里生产和喷涂。", "储罐由专门工厂制造"),
("K5", "转台另一角度，罐体表面均匀发亮，旁边浮现星条旗图标",
 "Another angle of the turntable with a freshly coated shiny tank, and a striped flag icon floating beside it. No people.",
 "原片说，这些罐子是美国制造。", "", ["美国制造"]),
# K6
("K6", "欣欣问在哪里能买到，小研指向展台边的经销商标牌",
 "The panda mascot asks where to buy, and the female graduate student points to a blank distributor sign by the table.",
 "去哪里买？就到合作的经销商那里。", "从正规渠道采购"),
("K6", "电话图标和空白号码条",
 "A telephone icon next to a blank number bar. No people.",
 "打经销商的免费电话就能订购。"),
# 小结
("小结", "液氮罐和取液器图标并排",
 "Icons of a dewar and a liquid withdrawal device side by side.",
 "液氮罐储运液氮，取液器取出液氮。", "小结"),
("小结", "出液嘴、软管、秒表三个图标",
 "Three icons: an outlet spout, a transfer hose and a stopwatch. No people.",
 "拆出液嘴接软管充装，又快又省心。"),
# 结尾
("结尾", "欣欣和小研在展台前挥手道别",
 "The panda mascot and the female graduate student wave goodbye at the exhibition table.",
 "今天的设备小课堂就到这里，下次见！"),
]
