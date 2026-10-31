# 22_Fire safety Safety measures in microbiology labs part3 laboratory microbiologyla 原著版卡通剧本作者源
# 完全照原片：K1–K6（灭火器好取用并定期维护、培训会用、安全出口畅通标识清楚、定期检查疏散路线、易燃品进专用柜、少用明火且不离人），
# 无补充知识点；不加火情报警、灭火器选型和使用要领、扑救与撤离、身上着火处置
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "微生物实验室安全措施：消防安全",
    "edition": "原著版",
    "points": {
        "K1": "灭火器：好拿到，常维护",
        "K2": "灭火器：人人会用",
        "K3": "安全出口：畅通、标识清楚",
        "K4": "疏散通道：定期检查",
        "K5": "易燃品：放进专用柜",
        "K6": "明火：少用，不离人",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "ARH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在走廊的灭火器箱旁，向镜头招手",
 "The panda mascot stands beside a fire extinguisher cabinet in a lab corridor and waves at the camera.",
 "今天讲微生物实验室的消防安全。", "微生物实验室的消防安全"),
("开场", "欣欣身旁浮现灭火器、安全出口、易燃品柜三个图标",
 "The panda mascot points to three floating icons: a fire extinguisher, an emergency exit sign and a flammable storage cabinet.",
 "灭火器、安全出口、易燃品和明火。", "", ["灭火器", "安全出口", "易燃品", "明火"]),
# 情景
("情景", "阿杰在台面上用酒精灯接种，旁边放着乙醇瓶",
 "The young male student inoculates a culture with a lit alcohol lamp on the bench, an ethanol spray bottle standing close by.",
 "阿杰点着酒精灯接种，乙醇瓶就在旁边。"),
("情景", "阿杰起身去接电话，酒精灯还燃着",
 "The young male student walks away to answer his phone while the alcohol lamp is still burning on the bench.",
 "他起身接电话，灯还燃着。"),
("情景", "小研走过来，用灯帽盖灭酒精灯",
 "The female graduate student walks over and puts out the alcohol lamp by covering it with its cap.",
 "小研赶紧用灯帽把它盖灭。"),
("情景", "欣欣在空白白板前严肃地点头",
 "The panda mascot nods seriously in front of a blank whiteboard.",
 "微生物实验室，火源和燃料都不少。"),
# K1
("K1", "走廊墙边的灭火器箱，前面没有遮挡",
 "A fire extinguisher cabinet on a corridor wall with nothing blocking it. No people.",
 "灭火器要放在显眼、好拿的地方，", "灭火器：好拿到，常维护", ["灭火器"]),
("K1", "灭火器前堆着纸箱被打叉",
 "A fire extinguisher hidden behind stacked boxes, crossed out in red. No people.",
 "不能被杂物挡住。"),
("K1", "老李查看灭火器压力表和检查卡",
 "The facility engineer checks the pressure gauge of a fire extinguisher and signs a blank inspection tag.",
 "还要定期检查维护，"),
("K1", "日历上每隔一段时间一个对勾，旁边灭火器图标",
 "A calendar with check marks at regular intervals beside a fire extinguisher icon. No people.",
 "保证需要时能用。"),
# K2
("K2", "王老师在空地上组织灭火器培训",
 "The safety administrator leads a fire extinguisher training session outdoors with several students, including the young male student.",
 "灭火器要人人会用，事先培训。", "灭火器：人人会用"),
("K2", "阿杰在王老师指导下练习拿起灭火器",
 "Under the safety administrator's guidance, the young male student practises lifting a training fire extinguisher.",
 "学会了，真遇到时才不慌。"),
# K3
("K3", "实验室门口上方的绿色安全出口标志亮着",
 "A green emergency exit sign glows above a lab corridor door. No people.",
 "安全出口要保持畅通，", "安全出口：畅通、标识清楚", ["安全出口"]),
("K3", "出口门前堆着仪器纸箱被打叉",
 "An exit door blocked by equipment boxes, crossed out in red. No people.",
 "门口不堆东西。"),
("K3", "走廊地面上的疏散指示箭头亮着",
 "Evacuation direction arrows glow along the corridor floor and wall. No people.",
 "出口标志、疏散指示要清楚。"),
# K4
("K4", "老李沿着疏散路线巡查",
 "The facility engineer walks along the evacuation route with a blank checklist.",
 "疏散路线，要定期检查，", "疏散通道：定期检查"),
("K4", "楼层平面图上标出两条疏散路线",
 "A floor plan with two evacuation routes highlighted toward two exits. No people.",
 "确认一路畅通，没有阻挡。"),
# K5
("K5", "黄色易燃品储存柜，门上有火焰象形图",
 "A yellow flammable storage cabinet with a flame pictogram on its door. No people.",
 "易燃物品，要放进指定的易燃品柜。", "易燃品：放进专用柜", ["易燃品柜"]),
("K5", "小研把乙醇大瓶放进易燃品柜，关好门",
 "The female graduate student puts a large ethanol bottle into the flammable storage cabinet and closes the door.",
 "乙醇、有机溶剂，都放在柜里。"),
# K6
("K6", "电热接种环灭菌器图标打勾，旁边酒精灯",
 "An electric loop sterilizer icon with a green check, beside an alcohol lamp icon. No people.",
 "明火要尽量少用，", "明火：少用，不离人"),
("K6", "燃着的酒精灯旁无人，被打叉",
 "A burning alcohol lamp on an empty bench with nobody around, crossed out in red. No people.",
 "点着的火，人不能离开。"),
# 小结
("小结", "欣欣站在灭火器和安全出口标志之间",
 "The panda mascot stands between a fire extinguisher and a glowing emergency exit sign.",
 "一起回顾一下。", "小结"),
("小结", "灭火器和检查卡图标",
 "A fire extinguisher icon with an inspection tag icon. No people.",
 "灭火器好拿、常查，人人会用。"),
("小结", "安全出口和疏散路线图标",
 "An emergency exit sign icon and an evacuation route icon. No people.",
 "出口畅通，路线常检查。"),
("小结", "易燃品柜和盖上灯帽的酒精灯",
 "A flammable storage cabinet icon and a capped alcohol lamp icon. No people.",
 "易燃品进柜，明火少用不离人。"),
# 结尾
("结尾", "欣欣和阿杰、小研在安全出口标志下挥手告别",
 "The panda mascot, the young male student and the female graduate student wave goodbye under a glowing emergency exit sign.",
 "防火在平时，下次见！"),
]
