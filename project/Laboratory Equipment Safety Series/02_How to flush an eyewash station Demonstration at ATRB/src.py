# 02_How to flush an eyewash station Demonstration at ATRB 卡通剧本作者源（原著版）
# 完全照原片：嵌墙式喷淋/洗眼柜定期放水冲洗的无声演示（2 分 30 秒，知识点依据画面和屏幕字幕归纳），
# 知识点 K1–K8，不加补充知识点、不做本土化和更正（操作者照原片穿 T 恤短裤、不穿实验服）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "如何冲洗洗眼器",
    "edition": "原著版",
    "points": {
        "K1": "洗眼器要定期放水冲洗",
        "K2": "嵌墙式洗眼柜：先备引流装置",
        "K3": "准备好工具和纸巾",
        "K4": "接头接到排水口，拧紧",
        "K5": "水桶放稳，启动放水",
        "K6": "等水完全排净",
        "K7": "接住滴水，擦干地面",
        "K8": "冲洗水倒进水槽",
    },
    "avoid": ["Iowa State", "ISU", "ATRB", "Tom Maier", "Maier", "Jackson Goshon", "Goshon", "iastate",
              "Environmental Health and Safety"],
}

SHOTS = [
# 开场
("开场", "欣欣站在走廊墙边的嵌墙式洗眼柜旁，向镜头招手",
 "The panda mascot stands beside a recessed stainless steel eyewash cabinet in a corridor wall and waves at the camera.",
 "今天看看洗眼器怎样定期冲洗。", "洗眼器的定期冲洗"),
# 情景
("情景", "阿杰穿着T恤短裤，提着蓝色水桶走到柜前",
 "The young male student in a T-shirt and shorts walks up to the wall cabinet carrying a blue plastic water can with a black hose.",
 "今天轮到阿杰给洗眼柜放水。"),
# K1
("K1", "嵌墙柜：左边灭火器箱，右边洗眼柜，上方有标识",
 "A recessed stainless steel wall cabinet with a fire extinguisher compartment on the left and an eyewash cabinet on the right, an eyewash sign and a safety shower sign above it. No people.",
 "这是嵌在墙里的喷淋洗眼柜。", "洗眼器要定期放水冲洗"),
("K1", "柜门把手上挂着一张空白检查卡",
 "A close view of a blank inspection tag hanging on the handle of the stainless steel eyewash cabinet door. No people.",
 "柜门挂着检查卡，要定期放水。"),
# K2
("K2", "柜体底部的小排水口特写，下面没有接水盆",
 "A close view of a small drain outlet at the bottom panel of the recessed cabinet, with no basin below it, only the floor. No people.",
 "柜子底下只有排水口，没有水盆。", "嵌墙式洗眼柜：先备引流装置"),
("K2", "地面上的蓝色水桶，桶口接着黑色波纹软管",
 "A blue plastic water can on the floor with a black corrugated hose connected to its opening, ending in a rubber coupling. No people.",
 "所以要先做一套引流装置。"),
("K2", "软管、柔性接头和水桶三个部件，箭头连成一套",
 "Three parts linked by arrows into one setup: a black corrugated hose, a short rubber flexible coupling and a blue plastic water can. No people.",
 "引流软管、柔性接头，加一只水桶。", "", ["引流软管", "柔性接头", "水桶"]),
("K2", "水桶贴着一张只有洗眼器图标的标签",
 "A blue plastic water can with a blank label showing only an eyewash pictogram. No people.",
 "水桶标明：洗眼器冲洗专用。"),
# K3
("K3", "螺丝刀、引流装置和一叠纸巾三张图标卡",
 "Three icon cards side by side: a flathead screwdriver, the hose-and-can drainage setup and a stack of paper towels. No people.",
 "准备一字螺丝刀、引流装置和纸巾。", "准备好工具和纸巾", ["一字螺丝刀", "引流装置", "纸巾"]),
# K4
("K4", "阿杰蹲下，把柔性接头套在排水口上",
 "The young male student in a T-shirt and shorts crouches and fits a rubber flexible coupling onto the drain outlet of the cabinet.",
 "把柔性接头套在排水口上。", "接头接到排水口，拧紧"),
("K4", "螺丝刀拧紧接头上的卡箍特写",
 "A close view of a flathead screwdriver tightening the metal hose clamp on the rubber coupling. No people.",
 "用螺丝刀把卡箍拧紧。"),
("K4", "软管另一头垂下，插进水桶口",
 "The black hose hangs down from the drain and its other end goes into the opening of the blue water can on the floor. No people.",
 "软管另一头接进水桶。"),
# K5
("K5", "水桶平放在柜前地面，旁边放着纸巾和螺丝刀",
 "The blue water can stands steady on the floor in front of the cabinet, with paper towels and a screwdriver beside it. No people.",
 "水桶放稳，纸巾放在旁边备用。", "水桶放稳，启动放水"),
("K5", "阿杰伸手到柜体右上方，拉开洗眼器",
 "The young male student reaches up to the upper right of the eyewash cabinet and pulls it open to start the water.",
 "启动洗眼器，开始放水。"),
("K5", "水沿软管流进水桶的示意",
 "A simple diagram with blue arrows showing water flowing from the cabinet drain through the hose into the can. No people.",
 "水经排水口和软管，流进水桶。"),
("K5", "阿杰站在桶旁搓搓手，耐心等着",
 "The young male student stands beside the can, rubbing his hands together and waiting.",
 "放一会儿水，让管路里的水流出来。"),
# K6
("K6", "接头、软管和水桶的固定画面，旁边沙漏图标",
 "A still view of the coupling, the hose and the blue can, with an hourglass icon floating beside them. No people.",
 "关水后，再等上几分钟。", "等水完全排净"),
("K6", "软管里的水滴越来越少的示意",
 "A simple diagram of the hose with fewer and fewer water drops falling into the can. No people.",
 "让水完全排净，再拆装置。"),
# K7
("K7", "阿杰蹲下，用纸巾托在接头下方，慢慢拆下接头",
 "The young male student crouches, holds a paper towel under the coupling and slowly removes it from the drain.",
 "拆接头时，用纸巾接住滴水。", "接住滴水，擦干地面"),
("K7", "排水口面板上贴着滑倒警示标志",
 "A slip hazard warning sign on the small panel around the drain outlet. No people.",
 "面板上提醒：小心滑倒。"),
("K7", "阿杰用纸巾擦干地面上洒出的水",
 "The young male student wipes spilled water off the floor with paper towels.",
 "洒出来的水，全部擦干。"),
# K8
("K8", "阿杰提着水桶走到实验室水槽边",
 "The young male student carries the blue water can to a lab sink.",
 "把水桶提到水槽边。", "冲洗水倒进水槽"),
("K8", "水从水桶经软管倒进水槽",
 "Water pours from the tilted can through the hose into a lab sink. No people.",
 "把桶里的水倒进水槽，就完成了。"),
# 小结
("小结", "欣欣身旁浮现软管、水桶和螺丝刀图标",
 "The panda mascot stands beside floating icons of a hose, a water can and a screwdriver.",
 "接好引流，拧紧卡箍，启动放水。", "小结"),
("小结", "沙漏、纸巾和水槽三个打勾图标",
 "Three icons with green checks: an hourglass, paper towels and a lab sink. No people.",
 "等水排净，擦干地面，倒进水槽。"),
# 结尾
("结尾", "欣欣在洗眼柜旁挥手道别",
 "The panda mascot waves goodbye beside the clean recessed eyewash cabinet.",
 "洗眼器常冲洗，用时才靠得住！"),
]
