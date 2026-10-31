# 53_What are common examples of hazardous materials in daily life trending question 卡通剧本作者源
# 原片是无人声的文字幻灯片（5 分钟）：日常危险物品五类（清洁剂、燃料、电池、杀虫剂、药品）+ 微生物降解石油烃的原理
# 原著版：完全照原片，K1–K10，无补充知识点；前半只列五类家用危险物品名称，后半讲烃类生物降解原理（菌属照原片）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "日常生活中常见的危险物品",
    "edition": "原著版",
    "points": {
        "K1": "生活里也有危险物品",
        "K2": "清洁剂",
        "K3": "燃料",
        "K4": "电池",
        "K5": "杀虫剂和驱虫剂",
        "K6": "药品",
        "K7": "能“吃油”的微生物",
        "K8": "以烃类为碳源和能源",
        "K9": "层层氧化，变成二氧化碳和水",
        "K10": "烃类生物降解，治理油污",
    },
    "avoid": ["Ragba Micro Hub", "Ragba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub"],
}

SHOTS = [
# 开场
("开场", "欣欣站在宿舍和家里厨房拼成的背景前，向镜头招手",
 "The panda mascot stands in front of a background combining a dorm room and a home kitchen, waving at the camera.",
 "危险物品，不只在实验室里。", "身边的危险物品，和吃油的微生物"),
("开场", "五个家用物品图标排成一排，后面跟着一个微生物图标",
 "Five household item icons in a row, followed by a microbe icon. No people.",
 "先看身边五类，再看吃油的微生物。"),
# 情景
("情景", "周末，阿杰在宿舍打扫卫生，手里拿着两瓶空白标签的清洁剂",
 "On the weekend the young male student cleans his dorm, holding two cleaning bottles with blank labels.",
 "周末，阿杰在宿舍大扫除。"),
("情景", "阿杰看着桌上的清洁剂、充电宝和杀虫喷雾，头顶问号",
 "The young male student looks at cleaners, a power bank and an insect spray on his desk, with a question mark above him.",
 "他想：这些也算危险物品吗？"),
("情景", "小研从门口探头，点点头",
 "The female graduate student leans in at the door and nods.",
 "小研说：算！我们一样样看。"),
# K1
("K1", "家里的厨房、卫生间、车库三个场景图标，各有几个瓶罐",
 "Icons of a kitchen, a bathroom and a garage, each with a few bottles and cans. No people.",
 "家里和宿舍，也藏着危险物品。", "生活里也有危险物品"),
("K1", "瓶罐背面放大，上面有小小的象形图",
 "Close-up of the back of a household bottle showing small hazard pictograms. No people.",
 "看看瓶子背面，就有警示。"),
# K2
("K2", "一瓶漂白剂和一瓶氨水味清洁剂并排",
 "A bleach bottle and an ammonia cleaner bottle side by side with blank labels. No people.",
 "第一类：清洁剂，比如漂白剂、氨水。", "清洁剂", ["漂白剂", "氨水"]),
# K3
("K3", "汽油桶、液化气罐、煤油瓶三个图标",
 "Icons of a fuel can, an LPG cylinder and a kerosene bottle. No people.",
 "第二类：燃料，汽油、液化气、煤油。", "燃料", ["汽油", "液化气", "煤油"]),
# K4
("K4", "汽车蓄电池和手机锂电池两个图标",
 "Icons of a car lead-acid battery and a phone lithium-ion battery. No people.",
 "第三类：电池，铅酸电池和锂电池。", "电池", ["铅酸电池", "锂电池"]),
# K5
("K5", "杀虫喷雾和驱蚊液两个图标",
 "Icons of an insect spray can and a mosquito repellent bottle. No people.",
 "第四类：杀虫剂和驱虫剂。", "杀虫剂和驱虫剂"),
# K6
("K6", "药盒和药瓶图标，旁边胶囊",
 "Icons of a medicine box, a pill bottle and capsules. No people.",
 "第五类：药品，比如抗生素、化疗药。", "药品", ["抗生素", "化疗药物"]),
# K7
("K7", "大海上一片油污，镜头推近到油滴里",
 "An oil slick on the sea; the view zooms in to a single oil droplet. No people.",
 "再说说：油污泄漏，微生物能帮忙。", "能“吃油”的微生物"),
("K7", "油滴周围聚集着杆状和球状的卡通微生物",
 "Cartoon rod-shaped and round microbes gather around the oil droplet. No people.",
 "有些细菌，专门分解石油烃。"),
("K7", "两个微生物图标下面贴着空白名牌",
 "Two microbe icons with blank name tags beneath them. No people.",
 "比如假单胞菌、食烷菌这类。", None, ["假单胞菌属", "食烷菌属"]),
# K8
("K8", "微生物抱着一条长链分子，像在吃饭",
 "A cartoon microbe holds a long chain molecule like a meal. No people.",
 "它们把烃类当作食物。", "以烃类为碳源和能源"),
("K8", "微生物身体里亮起电池和积木图标",
 "A battery icon and a building block icon light up inside the cartoon microbe. No people.",
 "既获取能量，又用来生长。", None, ["能源", "碳源"]),
# K9
("K9", "长链分子一步步被切短，变成小分子",
 "A long chain molecule is cut step by step into shorter pieces. No people.",
 "先把油氧化，变成脂肪酸。", "层层氧化，变成二氧化碳和水", ["脂肪酸"]),
("K9", "小分子最后变成气泡和水滴",
 "The small pieces finally turn into bubbles and water droplets. No people.",
 "最后分解成二氧化碳和水。", None, ["二氧化碳", "水"]),
# K10
("K10", "海面油污逐渐变淡，海水恢复清澈",
 "The oil slick gradually fades and the sea becomes clear again. No people.",
 "这叫烃类生物降解。", "烃类生物降解，治理油污", ["烃类生物降解"]),
("K10", "老周在实验室的生物安全柜里观察培养皿",
 "The older man observes a petri dish inside a biosafety cabinet in the lab.",
 "它是治理油污的重要办法之一。"),
# 回到情景
# 小结
("小结", "欣欣站在白板前，五个物品图标依次亮起",
 "The panda mascot stands at a whiteboard where five household item icons light up one by one.",
 "清洁剂、燃料、电池、杀虫剂、药品。", "小结", ["清洁剂", "燃料", "电池", "杀虫剂", "药品"]),
("小结", "微生物抱着油滴，油滴变成气泡和水",
 "A cartoon microbe hugs an oil droplet, which turns into bubbles and water.",
 "微生物吃油，变成二氧化碳和水。"),
# 结尾
("结尾", "欣欣在干净的宿舍里向镜头挥手",
 "The panda mascot waves goodbye to the camera in a clean, tidy dorm room.",
 "实验室外也要讲安全，再见！"),
]
