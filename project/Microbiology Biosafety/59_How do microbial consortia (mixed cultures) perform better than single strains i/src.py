# 59_How do microbial consortia (mixed cultures) perform better than single strains i 卡通剧本作者源
# 原片为无讲解的文字幻灯片问答：微生物燃料电池处理废物并发电、混合菌群解毒优于单一菌株（生物修复，与安全相关度低）。保留全部知识点 K1–K5，
# 原著版：完全照原片，K1–K5，无补充知识点（微生物燃料电池、混合菌群接力降解、油污需好氧与厌氧菌配合）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "解毒中混合菌群为何优于单一菌株？",
    "edition": "原著版",
    "points": {
        "K1": "微生物燃料电池：细菌分解废物",
        "K2": "电子流向电极：解毒又发电",
        "K3": "混合菌群：代谢互补，强过单菌",
        "K4": "接力降解：先拆大分子，再收尾",
        "K5": "例子：清理油污，好氧厌氧都要",
    },
    "avoid": ["Raqba Micro Hub", "Raqba", "raqbamicrohub", "ARHMicroHub", "ARH Micro Hub", "ARH"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台前，身旁一个小灯泡连着一个装泥水的容器",
 "The panda mascot stands at a lab bench beside a small light bulb wired to a container of muddy water, and waves at the camera.",
 "细菌不光能吃废物，还能发电。", "解毒中混合菌群为何优于单一菌株？"),
("开场", "欣欣指向两个图标：电池、一群手拉手的细菌",
 "The panda mascot points to two floating icons: a battery and a group of bacteria holding hands.",
 "今天讲燃料电池和混合菌群。", "", ["燃料电池", "混合菌群"]),
# 情景
("情景", "小研从污水厂带回一桶密封的污泥样",
 "The female graduate student carries a sealed bucket of sludge sample with a blank label into the lab.",
 "小研从污水厂带回一桶污泥。"),
("情景", "阿杰好奇地凑过来，看着密封的污泥桶",
 "The young male student leans over curiously to look at the sealed sludge bucket.",
 "阿杰问：这黑乎乎的，能干什么？"),
("情景", "小研笑着指向桌上连着小灯泡的容器",
 "The female graduate student smiles and points to a container on the bench wired to a small light bulb.",
 "小研说：里面的细菌，能发电！"),
# K1
("K1", "一个两格的容器，左格装泥水，右格清水，中间一层膜",
 "A two-chamber container: muddy water on the left, clear water on the right, a thin membrane between them. No people.",
 "这是微生物燃料电池。", "微生物燃料电池：细菌分解废物", ["微生物燃料电池"]),
("K1", "左格里细菌聚在一根黑色电极上，吃掉周围的污物颗粒",
 "In the left chamber, bacteria cluster on a black electrode rod and consume the dirt particles around them. No people.",
 "里面的电活性细菌，分解有机或有毒废物。"),
("K1", "两个废物图标：一袋有机废物、一桶带骷髅象形图的有毒废物",
 "Two waste icons: a bag of organic waste and a drum of toxic waste with a skull pictogram. No people.",
 "有机废物、有毒废物，它都能处理。", "", ["有机废物", "有毒废物"]),
# K2
("K2", "细菌身上冒出小火花，沿着电极流出去",
 "Small sparks pop out of the bacteria and flow along the electrode rod. No people.",
 "分解时放出的电子，流向电极，", "电子流向电极：解毒又发电"),
("K2", "导线把两格连起来，中间的小灯泡亮了",
 "A wire connects the two chambers and a small light bulb in the middle lights up. No people.",
 "形成电流，小灯泡就亮了。"),
("K2", "左格的泥水逐渐变清，灯泡一直亮着",
 "The muddy water in the left chamber slowly turns clearer while the bulb stays lit. No people.",
 "废物解了毒，还顺便发了电。"),
# K3
("K3", "一个细菌独自面对一大块复杂的污染物，满头大汗",
 "A single bacterium faces a huge tangled pollutant block alone, looking tired. No people.",
 "单一菌株，本事有限。", "混合菌群：代谢互补，强过单菌"),
("K3", "几种不同形状的细菌围成一圈，手拉手",
 "Several bacteria of different shapes form a circle, holding hands. No people.",
 "混合菌群，把不同的本事组合起来，", "", ["混合菌群"]),
("K3", "拼图块拼在一起，每块一种细菌",
 "Puzzle pieces fit together, each piece showing a different bacterium. No people.",
 "代谢互补，解毒效果更好。"),
# K4
("K4", "一个细菌把大块污染物切成几段",
 "One bacterium cuts a big tangled pollutant block into several smaller pieces. No people.",
 "一种菌先上，拆开复杂的污染物，", "接力降解：先拆大分子，再收尾"),
("K4", "另一群细菌接过小段，继续分解",
 "Another group of bacteria takes the smaller pieces and keeps breaking them down, like a relay race. No people.",
 "其他菌接棒，继续往下分解，"),
("K4", "最后剩下水滴和小气泡，旁边绿色对勾",
 "At the end only water drops and small bubbles remain, with a green check mark beside them. No people.",
 "直到变成无害的产物。"),
# K5
("K5", "海面上一片黑色油污",
 "A dark oil slick spreading on the sea surface. No people.",
 "比如海上的油污。", "例子：清理油污，好氧厌氧都要"),
("K5", "水面上的细菌旁有氧气泡，水底泥里的细菌没有",
 "Bacteria near the water surface surrounded by oxygen bubbles, and other bacteria in the mud below without bubbles. No people.",
 "要清干净，需要好氧菌和厌氧菌，", "", ["好氧菌", "厌氧菌"]),
("K5", "上下两群细菌一起，油污慢慢消失",
 "The two groups of bacteria work together and the oil slick slowly disappears. No people.",
 "上下配合，共同完成。"),
# 小结
("小结", "欣欣站在电池和手拉手细菌两个图标前",
 "The panda mascot stands in front of a battery icon and a group of bacteria holding hands.",
 "一起回顾一下。", "小结", ["燃料电池", "混合菌群"]),
("小结", "细菌、电极、亮着的灯泡",
 "Bacteria on an electrode with a lit light bulb above. No people.",
 "燃料电池：细菌分解废物，电子发电。"),
("小结", "接力的细菌和消失的油污",
 "Bacteria passing pieces in a relay, and an oil slick fading away. No people.",
 "混合菌群接力降解，好氧厌氧配合。"),
# 结尾
("结尾", "欣欣和阿杰、小研一起挥手告别",
 "The panda mascot waves goodbye together with the young male student and the female graduate student.",
 "细菌也讲团队合作，下次见！"),
]
