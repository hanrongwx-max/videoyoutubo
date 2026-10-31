# 06_Safety Prep For Tourists and Visitors Laser Safety at Laser Maintenance Group In 卡通剧本作者源
# 原著版：完全照原片（1 分 17 秒，车间负责人讲“做一个安全的参观向导”），K1–K7，不加补充知识点、不做更正；
# 保留原片做法：鼓励访客拍视频、带切割小玩意回家；访客穿裙子凉鞋时保持通道畅通、不卸钢板；钢头/复合材料头安全鞋也不保险；
# 站在能看又安全的地方；替访客留意储罐起跳、行车、叉车、带锯突然启动；先讲再指给他们看
# 原片没讲登记审批、着装要求、激光防护，本版也不加；讲解人姓名、公司名、网址和联系方式不出现，讲解人改为老李
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "访客参观前的安全准备：激光安全",
    "edition": "原著版",
    "points": {
        "K1": "让访客有好的体验",
        "K2": "保护访客是第一位",
        "K3": "便装访客：通道畅通，不卸钢板",
        "K4": "安全鞋也不是保险",
        "K5": "站在看得清又安全的地方",
        "K6": "留意突然启动的设备",
        "K7": "先说清楚，再动手",
    },
    "avoid": ["Scott Kiser", "Kiser", "Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "LaserServiceGuy", "Laser Maintenance Group", "LMG", "lasersolutions", "comcast"],
}

SHOTS = [
# 开场
("开场", "欣欣戴着导游小旗站在车间门口，向镜头招手",
 "The panda mascot holds a small tour guide flag at a workshop entrance and waves at the camera.",
 "怎样做一个安全的参观向导？", "访客参观前的安全准备：激光安全"),
("开场", "相机、鞋子、站位、警示灯、说话气泡五个图标",
 "Five icons in a row: a camera, a shoe, a standing spot, a warning light and a speech bubble. No people.",
 "老李在车间里讲了七件事。"),
# 情景
("情景", "车间里型材货架、低温储罐和一台大型激光切割机",
 "Inside a laser workshop: metal stock racks, cryogenic tanks and a large laser cutting machine. No people.",
 "这是一间激光加工车间。"),
("情景", "老李站在货架和储罐旁，对着镜头讲话",
 "The facility engineer stands between the stock racks and the tanks and talks to the camera.",
 "老李经常带客户来这里参观。"),
# K1
("K1", "访客们看着激光切割机切割纸板，很兴奋",
 "Excited visitors watch a large laser cutting machine cutting a sheet of cardboard.",
 "带访客参观，希望他们玩得开心。", "让访客有好的体验"),
("K1", "一位访客举着空白手机拍视频",
 "A visitor holds up a blank phone to film the machine.",
 "可以拍拍视频。"),
("K1", "一位访客手里拿着一个激光切割的小纪念品",
 "A visitor holds a small laser-cut metal souvenir.",
 "还可以带个切出来的小玩意回家。"),
("K1", "访客回家给朋友同事讲述的图标",
 "An icon of a visitor at home telling friends and coworkers about the trip, with a speech bubble. No people.",
 "回去跟朋友同事讲今天看到的。"),
# K2
("K2", "老李站在访客和机器之间",
 "The facility engineer stands between the visitors and the machines.",
 "但向导最重要的事，是保护他们。", "保护访客是第一位"),
("K2", "老李一边展示，一边扫视四周",
 "The facility engineer shows off a part while glancing around the workshop.",
 "可以稍微炫耀一下，但始终要留心。"),
# K3
("K3", "凉鞋和裙子图标",
 "Icons of sandals and a skirt. No people.",
 "访客可能穿着裙子、凉鞋就来了。", "便装访客：通道畅通，不卸钢板"),
("K3", "老李把通道上的板材挪开",
 "The facility engineer moves sheet metal off a walkway so the aisle is clear.",
 "所以通道要保持畅通。"),
("K3", "有访客在场时卸钢板的图标，被红叉划掉",
 "An icon of unloading steel plates while visitors stand nearby, crossed out with a red X. No people.",
 "他们在场的时候，不卸钢板。"),
# K4
("K4", "老李脚上的深色工作鞋特写",
 "Close-up of the facility engineer's dark work shoes.",
 "就算穿着钢头或复合材料头的鞋，", "安全鞋也不是保险"),
("K4", "一块钢板压在安全鞋上的示意，旁边感叹号",
 "A diagram of a steel plate landing on a safety shoe, with an exclamation mark. No people.",
 "也不能保证你不会受伤。"),
# K5
("K5", "老李把穿便服的访客带到一处空地",
 "The facility engineer leads visitors in casual clothes to an open spot in the workshop.",
 "穿便服的访客，要带到安全的地方。", "站在看得清又安全的地方"),
("K5", "访客站在那里，能清楚看到切割机",
 "The visitors stand at the spot and can clearly see the laser cutting machine.",
 "站在既能看清、又安全的位置。"),
# K6
("K6", "老李指向身旁的低温储罐",
 "The facility engineer points at a cryogenic tank beside him.",
 "你还要替他们留意周围的设备。", "留意突然启动的设备"),
("K6", "储罐起跳、行车、叉车、带锯四个图标",
 "Four icons: a tank relief valve, an overhead crane, a forklift and a band saw. No people.",
 "储罐要起跳，行车、叉车要启动，", "", ["储罐", "行车", "叉车", "带锯"]),
("K6", "带锯开动，发出很大的声响",
 "A band saw starts up with a loud burst of sound lines. No people.",
 "还有带锯要开动的时候。"),
("K6", "几位访客同时被响声吓了一跳",
 "Icons of several visitors jumping in surprise at a sudden noise. No people.",
 "这些会突然动、突然响，吓人一跳。"),
# K7
("K7", "老李对访客说话，手指向行车",
 "The facility engineer talks to the visitors and points at an overhead crane.",
 "所以要跟访客说清楚你要做什么。", "先说清楚，再动手"),
("K7", "示意图：箭头标出声音来处和移动方向",
 "A diagram with arrows showing where a sound will come from and which way a machine will move. No people.",
 "声音从这里来，它会这样动。"),
("K7", "访客点头，行车启动时神情平静",
 "The visitors nod and stay calm as the crane starts moving.",
 "先讲好、指给他们看，就不会受惊。"),
# 小结
("小结", "欣欣身旁浮现相机、通道、鞋子、站位、说话气泡图标",
 "The panda mascot stands beside icons of a camera, a clear aisle, a shoe, a standing spot and a speech bubble.",
 "让访客开心，但保护他们第一。", "小结"),
("小结", "老李带着访客站在安全的位置看机器",
 "The facility engineer and the visitors watch the machines from a safe spot.",
 "通道畅通，站对位置，先讲再动。"),
# 结尾
("结尾", "欣欣挥动导游小旗告别",
 "The panda mascot waves the small tour guide flag goodbye.",
 "安全参观向导就讲到这里，下次见！"),
]
