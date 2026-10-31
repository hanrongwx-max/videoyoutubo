# 15_Obey Laser Warning Signs, Safety Stickers, and Barriers Innovative Laser Mainten 卡通剧本作者源
# 原著版：完全照原片（2 分 38 秒：机器背面的链条、光路上的黄色警示贴和红外激光），K1–K12，不加补充知识点、不做更正；
# 保留原片说法：正面有安全地垫、背面没有，用链条像安全拉绳一样拦住，起类似的保护作用（原话照用，不改为“只能警示”）；
# 背面只有做光路校准的维修人员；防被龙门架、风琴管、导轨缠住；链条挂着即不得进入；
# 激光在柜内产生、经反射镜送到切割头；贴纸=揭开后面可能有光束；维修人员懂规程（用靶对中）；开盖开激光，红外光看不见、打到哪里都可能起火
# 讲解人伸手扶镜座照原片；原片没讲上锁挂牌、标志维护、光束终止器，本版也不加；讲解人姓名、公司名和联系方式不出现，讲解人改为老李
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "遵守激光警示标志、安全标贴与隔离栏",
    "edition": "原著版",
    "points": {
        "K1": "访客不熟悉车间，要照看",
        "K2": "正面有地垫，背面没有",
        "K3": "背面用链条拦住",
        "K4": "背面是维修人员的地方",
        "K5": "防被龙门架和风琴管缠住",
        "K6": "进去的人要清楚在做什么",
        "K7": "链条挂着：不得进入",
        "K8": "光路上到处是黄色警示贴",
        "K9": "光从柜里经反射镜到切割头",
        "K10": "贴纸的意思：后面可能有激光",
        "K11": "维修人员按规程开护罩",
        "K12": "开盖出光：看不见，会起火",
    },
    "avoid": ["Scott Kiser", "Kiser", "Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "LaserServiceGuy", "Laser Maintenance Group", "LMG"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一条黄黑链条前，旁边贴着黄色激光警告标志",
 "The panda mascot stands in front of a yellow and black chain barrier next to a yellow laser warning sign.",
 "警示标志、贴纸和链条，要听它们的。", "看懂激光警示：标志、贴纸和链条"),
("开场", "警告标志、贴纸、链条三个图标",
 "Three icons in a row: a laser warning sign, a warning sticker and a chain barrier. No people.",
 "老李带我们去机器背面看看。", "", ["标志", "贴纸", "链条"]),
# 情景
("情景", "办公区门口，老李对着镜头讲话，几位访客在旁",
 "At an office door, the facility engineer talks to the camera while a few visitors wait.",
 "老李又要带客户进车间了。"),
# K1
("K1", "访客们指着激光切割机，满脸好奇",
 "Visitors point curiously at a laser cutting machine.",
 "客户都想看看我们在做什么。", "访客不熟悉车间，要照看"),
("K1", "家、办公室和车间三个图标",
 "Three icons: a home, an office and an industrial workshop with an exclamation mark. No people.",
 "他们习惯家和办公室，不熟悉工业车间。"),
("K1", "老李走在访客身旁，伸手示意他们跟紧",
 "The facility engineer walks beside the visitors and gestures for them to stay close.",
 "所以要照看好他们。"),
# K2
("K2", "机器正面铺着黑色安全地垫",
 "A black safety mat lies in front of the laser cutting machine. No people.",
 "机器正面有安全地垫。", "正面有地垫，背面没有"),
("K2", "老李走到机器背面，地上什么也没有",
 "The facility engineer walks to the back of the machine, where the floor has no mat.",
 "到了背面，就没有这种装置了。"),
# K3
("K3", "背面通道口拉着一条黄黑相间的链条，旁边是氧气储罐",
 "A yellow and black chain is stretched across the back walkway, next to an oxygen tank. No people.",
 "所以背面用链条拦住。", "背面用链条拦住"),
("K3", "老李拉开链条，像拉一根安全拉绳",
 "The facility engineer stretches the chain out like a safety cord.",
 "像安全拉绳一样拉开，"),
("K3", "链条图标和地垫图标之间一个约等号",
 "A chain icon and a floor mat icon with an approximately-equal sign between them. No people.",
 "起到类似的保护作用。"),
# K4
("K4", "维修人员图标拿着工具站在背面",
 "An icon of a maintenance technician with tools at the back of the machine. No people.",
 "背面通常只有维修人员进来。", "背面是维修人员的地方"),
("K4", "光路反射镜座和校准工具",
 "A beam path mirror mount with an alignment tool beside it. No people.",
 "在这里做光路校准这类工作。"),
# K5
("K5", "老李沿背面走，指着导轨和风琴管",
 "The facility engineer walks along the back and points at the rail and the folding bellows.",
 "背面有风琴管，有导轨。", "防被龙门架和风琴管缠住"),
("K5", "龙门架在导轨上来回滑动",
 "Animation: the gantry slides back and forth along its rail while cutting. No people.",
 "切割时，整个龙门架来回滑动。"),
("K5", "人被运动部件卷住的图标，被红叉划掉",
 "An icon of a person caught by a moving gantry, crossed out with a red X. No people.",
 "链条就是防止人被它缠住。"),
# K6
("K6", "背面的检修面板、电线和气路",
 "Service panels, wires and gas lines on the back of the machine. No people.",
 "检修面板、气路要维护时才进来。", "进去的人要清楚在做什么"),
("K6", "老李背对镜头，看着检修面板",
 "The facility engineer, back to the camera, looks at a service panel.",
 "链条挂着，进来的人得清楚在做什么。"),
("K6", "一个人不知不觉走进去的图标，被红叉划掉",
 "An icon of a person wandering in without noticing, crossed out with a red X. No people.",
 "不能稀里糊涂走进来，受了伤。"),
# K7
("K7", "老李手拉链条",
 "The facility engineer holds the chain with his hand.",
 "链条挂起来，", "链条挂着：不得进入"),
("K7", "链条图标连到禁止进入标志",
 "A chain icon linked to a no entry sign. No people.",
 "就是“不得进入”的警示。"),
# K8
("K8", "老李走到出光口和反射镜座旁",
 "The facility engineer walks to the laser output and a mirror mount.",
 "再看光路上这些贴纸。", "光路上到处是黄色警示贴"),
("K8", "光路护管和镜座上贴着一张张黄色激光警告标志",
 "Yellow laser warning signs stuck on beam tubes and mirror mounts all along the beam path. No people.",
 "黄色警示贴，到处都是。"),
# K9
("K9", "示意图：激光在柜内产生，经几面反射镜转向，送到切割头",
 "A diagram: the laser beam is generated in a cabinet, bounces off a series of mirrors and goes down to the cutting head. No people.",
 "激光在柜子里产生，", "光从柜里经反射镜到切割头"),
("K9", "光束在镜子间整形、转向的动画",
 "Animation of the beam being shaped and turned between mirrors. No people.",
 "经过一组反射镜整形、转向，送到切割头。"),
# K10
("K10", "老李手扶反射镜座，指着上面的贴纸",
 "The facility engineer rests a hand on a mirror mount and points at the sticker on it.",
 "每一张贴纸都在说：", "贴纸的意思：后面可能有激光"),
("K10", "护罩揭开，后面有一条光路",
 "A diagram: a cover is lifted and a beam path is right behind it. No people.",
 "揭开这里，后面可能有激光束。"),
# K11
("K11", "维修人员图标揭开护罩，查看反射镜",
 "An icon of a technician removing a cover and checking a mirror. No people.",
 "维修人员懂得怎么规范作业。", "维修人员按规程开护罩"),
("K11", "镜座上放着一个对中靶，光斑落在靶心",
 "An alignment target placed on a mirror mount, with a spot in its center. No people.",
 "揭开护罩查镜片，在镜座上用靶对中。"),
("K11", "激光关闭的图标打勾",
 "A laser-off icon with a green check. No people.",
 "他们清楚，这时不会出光。"),
# K12
("K12", "开着激光揭开护罩的图标",
 "An icon of a cover lifted while the laser is switched on. No people.",
 "可要是揭开护罩又开了激光，", "开盖出光：看不见，会起火"),
("K12", "看不见的光束示意：一条虚线和一只闭着的眼睛图标",
 "A diagram of an invisible beam drawn as a dotted line, next to a closed eye icon. No people.",
 "光束射出来，是红外光，看不见。"),
("K12", "虚线光束落在纸箱上冒起火苗",
 "The dotted beam lands on a cardboard box far away and a flame starts. No people.",
 "打到哪儿，就可能在哪儿起火。"),
# 小结
("小结", "欣欣身旁浮现地垫、链条、禁止进入、黄色贴纸图标",
 "The panda mascot stands beside icons of a floor mat, a chain, a no entry sign and a yellow warning sticker.",
 "背面没有地垫，链条挂着不得进入。", "小结"),
("小结", "黄色贴纸和虚线光束图标",
 "A yellow warning sticker icon and a dotted invisible beam icon. No people.",
 "贴纸后面可能有光，红外看不见会起火。"),
# 结尾
("结尾", "欣欣在链条前挥手告别",
 "The panda mascot waves goodbye in front of the chain barrier.",
 "听从警示，下次见！"),
]
