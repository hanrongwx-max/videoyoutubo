# 08 二氧化碳 原著版卡通剧本作者源
# 完全照原片：经销商员工的万圣节特辑，讲 CO2 的正面用途，K1–K7（排放与气候、引用美国压缩气体协会列出的六大用途、
# 饮料气泡、干冰冷藏、疫苗冷藏、促进作物生长、“没有理由被CO2吓到”与危害管理看协会海报），无补充知识点；
# 结语照原片保留，不纠正、不补充窒息和干冰风险；经销商名、主持人姓名不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "认识二氧化碳及其应用",
    "edition": "原著版",
    "points": {
        "K1": "二氧化碳（CO2）是一种常见气体，人们常从排放和气候角度讨论它",
        "K2": "CO2 在日常生活和工业中用途广：水处理、医疗、基础设施、食品、饮料、农业",
        "K3": "饮料里的气泡来自 CO2",
        "K4": "干冰（固态 CO2）用于冷藏食品和饮料",
        "K5": "疫苗等需要低温储存的物品，借助 CO2（干冰）安全冷藏运输",
        "K6": "CO2 可促进作物生长",
        "K7": "使用 CO2 也有危害，需要按危害管理指引操作（原片只以“看链接海报”一句带过）",
    },
    "avoid": ["EquiTips", "Equi-Tips", "Equi-Tip", "EquiGas", "Equigas", "Ava Casper", "Casper", "CGA",
              "Halloween"],
}

SHOTS = [
# 开场
("开场", "欣欣站在仓库货架通道里，货架上摆着南瓜灯装饰，向镜头招手",
 "The panda mascot stands in a warehouse aisle with carved pumpkin lanterns on the shelves and waves at the camera.",
 "欢迎来到设备小课堂，万圣节快乐！", "认识二氧化碳及其应用"),
("开场", "大大的二氧化碳分子图标飞入画面",
 "A large carbon dioxide molecule icon, one carbon ball between two oxygen balls, flies into the frame. No people.",
 "今天的主题是二氧化碳。", "", ["CO2"]),
# 情景
("情景", "阿杰看着新闻屏幕上冒烟的烟囱，皱起眉头",
 "The young male student frowns at a blank news screen showing smoking chimneys and a hot globe icon.",
 "阿杰一听二氧化碳，就想到污染。"),
("情景", "欣欣摇摇手指，笑着示意阿杰别急",
 "The panda mascot wags a finger and smiles, gesturing to the young male student to wait.",
 "其实它在生活里大有用处。"),
# K1
("K1", "欣欣双手背在身后，旁边浮现二氧化碳分子",
 "The panda mascot stands with hands behind its back next to a floating carbon dioxide molecule.",
 "CO2就是二氧化碳。", "二氧化碳是一种常见气体"),
("K1", "欣欣做出起鸡皮疙瘩的鬼脸",
 "The panda mascot makes a playful spooky face, pretending to shiver.",
 "这个话题，也许会让人有点发毛。"),
("K1", "烟囱冒烟、地球变热的图标",
 "Icons of a smoking chimney and a globe with a rising thermometer. No people.",
 "人们通常讲它的坏处：排放影响气候。"),
("K1", "天平一边是烟囱，另一边是空着的问号",
 "A balance scale with a chimney icon on one side and a question mark on the empty other side. No people.",
 "可它在日常生活里也非常重要。"),
# K2
("K2", "一本空白小册子，带星条小旗图标",
 "A blank booklet with a small striped flag icon. No people.",
 "美国压缩气体协会列出了关键用途。", "二氧化碳用途广"),
("K2", "水滴、医疗十字、桥梁三个图标",
 "Three icons: a water drop, a medical cross and a bridge. No people.",
 "水处理、医疗、基础设施，", "", ["水处理", "医疗", "基础设施"]),
("K2", "餐盘、饮料杯、麦穗三个图标",
 "Three icons: a dinner plate, a drink cup and a wheat ear. No people.",
 "还有食品、饮料和农业。", "", ["食品", "饮料", "农业"]),
# K3
("K3", "一杯汽水里气泡不断往上冒",
 "A glass of soda with streams of bubbles rising to the top. No people.",
 "饮料里的气泡，就是二氧化碳。", "饮料里的气泡"),
# K4
("K4", "泡沫箱里的白色干冰块冒着白雾，旁边是饮料和食品",
 "White dry ice blocks giving off mist in a foam box next to drinks and food packs. No people.",
 "干冰是固态的二氧化碳，", "干冰用来冷藏"),
("K4", "冷藏箱里的食品和饮料保持冰凉，温度计指针很低",
 "Food and drinks kept cold in a cooler box with a low thermometer icon. No people.",
 "能让食品和饮料一直保持冰凉。"),
# K5
("K5", "疫苗小瓶装在放着干冰的运输箱里",
 "Small vaccine vials packed in a shipping box with dry ice. No people.",
 "疫苗要低温储存，", "疫苗低温冷藏运输"),
("K5", "运输箱从仓库运往医院的路线图标",
 "A route icon of the shipping box traveling from a warehouse to a hospital. No people.",
 "靠它一路冷藏，安全送达。"),
# K6
("K6", "温室里的作物，二氧化碳分子飘向叶片",
 "Crops in a greenhouse with carbon dioxide molecule icons drifting toward the leaves. No people.",
 "在农业上，二氧化碳能促进作物生长。", "促进作物生长"),
("K6", "幼苗长成茁壮植株的图标",
 "A seedling icon growing into a tall healthy plant icon. No people.",
 "作物长得更快更好。"),
# K7
("K7", "欣欣竖起大拇指，身旁是一排用途图标",
 "The panda mascot gives a thumbs up beside a row of use icons: soda, dry ice, vaccine and crops.",
 "今天只想让大家看看它好的一面。", "使用二氧化碳也有危害管理指引"),
("K7", "欣欣摆摆手，笑着对镜头说话",
 "The panda mascot waves a hand dismissively and smiles at the camera.",
 "没有理由被二氧化碳吓到。"),
("K7", "欣欣指向下方几张空白海报图标",
 "The panda mascot points down to several blank poster icons.",
 "危害管理指引，请看协会的海报。"),
# 小结
("小结", "汽水、干冰、疫苗、作物四个图标",
 "Four icons: a soda glass, dry ice, a vaccine vial and a growing plant.",
 "气泡、冷藏、疫苗、庄稼都靠它。", "小结"),
("小结", "六个用途图标围成一圈",
 "Six use icons arranged in a circle: water, medical cross, bridge, plate, cup and wheat. No people.",
 "水、医疗、基建、食品、饮料、农业。"),
("小结", "阿杰点点头，对着二氧化碳分子竖起大拇指",
 "The young male student nods and gives a thumbs up to a carbon dioxide molecule icon.",
 "阿杰说：原来它这么有用。"),
# 结尾
("结尾", "欣欣在南瓜灯装饰的货架前挥手道别",
 "The panda mascot waves goodbye in front of shelves decorated with pumpkin lanterns.",
 "万圣节快乐，我们下次见！"),
]
