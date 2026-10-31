# 02_Burning Laser Bellows Jan2020 卡通剧本作者源
# 原著版：完全照原片（20 秒手机竖拍，无讲解：切割头上方风琴管被烧穿、阴燃，周围积灰），K1–K5，不加补充知识点、不做更正；
# 原片没有停机、灭火、报警等处置，只是近拍—拉远记录燃烧点，本版照此只讲看到了什么，不加应急步骤
# 企业名不出现；原片不足 2 分钟，只复述原片画面内容补足时长
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "风琴管着火了怎么办",
    "edition": "原著版",
    "points": {
        "K1": "风琴管：光路的保护套",
        "K2": "风琴管会被烧穿",
        "K3": "火点挨着管线和机头",
        "K4": "积灰既是隐患也是燃料",
        "K5": "阴燃不会自己熄灭",
    },
    "avoid": ["Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "Laser Maintenance Group", "LMG", "Kiser"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一台激光切割机旁，指着机头上方的波纹管",
 "The panda mascot stands beside a laser cutting machine and points at the folded bellows tube above the cutting head.",
 "今天看一段风琴管着火的现场。", "风琴管着火了怎么办"),
("开场", "风琴管、火苗、积灰三个图标排成一行",
 "Three icons in a row: a folded bellows tube, a small flame and a pile of dark soot. No people.",
 "看清它在哪、怎么烧、为什么危险。", "", ["风琴管", "火苗", "积灰"]),
# 情景
("情景", "老李走到一台激光切割机前，抬头看机头",
 "The facility engineer walks up to a laser cutting machine and looks up at the cutting head.",
 "老李来检查一台激光切割机。"),
("情景", "机头上方的波纹护套上透出一点橙红色火光",
 "An orange glow shows through a hole in the folded bellows tube above the cutting head. No people.",
 "机头上方的风琴管里透出火光。"),
("情景", "老李举起空白手机，对着火光竖拍",
 "The facility engineer holds up a blank phone vertically and films the glowing spot.",
 "老李举起手机，把这一幕拍了下来。"),
# K1
("K1", "示意图：切割头上方一根可伸缩的波纹管包着光路",
 "A simple diagram: a folding bellows tube above a laser cutting head encloses the beam path. No people.",
 "切割头上方的光路由风琴管包着。", "风琴管：光路的保护套"),
("K1", "切割头上下移动，风琴管随之伸长缩短",
 "Animation: the cutting head moves up and down and the bellows tube stretches and compresses with it. No people.",
 "它能伸缩，跟着切割头上下移动。"),
("K1", "风琴管外灰尘飞舞，管内的光路干干净净",
 "Dust floats outside the bellows tube while the beam path inside stays clean. No people.",
 "作用是挡住粉尘，保护光路。"),
("K1", "欣欣比划一个伸缩的动作",
 "The panda mascot mimes stretching and squeezing an accordion.",
 "名字就来自它像手风琴的褶皱。"),
# K2
("K2", "风琴管侧面褶皱上一个烧开的小洞，洞里橙红色火光",
 "Close-up of a black folded bellows tube with a burned hole on one side, an orange glow inside. No people.",
 "这根风琴管的侧面被烧穿了。", "风琴管会被烧穿"),
("K2", "洞下方还有一个亮黄色的小火点",
 "A small bright yellow spot of fire just below the burned hole on the bellows. No people.",
 "洞里有火光，下面还有一个亮点。"),
("K2", "火光在褶皱间忽明忽暗，洞口边缘发黑",
 "The orange glow flickers between the folds and the edges of the hole are blackened. No people.",
 "火光忽明忽暗，洞口边缘发黑。"),
("K2", "护套材料慢慢变红变黑的示意图",
 "A simple diagram: the bellows material slowly glows red and chars black without open flames. No people.",
 "说明护套材料正在阴燃。"),
# K3
("K3", "镜头拉远：风琴管下面是方形机座、切割头",
 "Wider view: below the bellows tube are a square mount and the laser cutting head. No people.",
 "镜头拉远，下面就是切割头。", "火点挨着管线和机头"),
("K3", "多根黑色气管和细电缆用白色扎带捆在机头旁",
 "Several black gas hoses and thin cables bundled with white cable ties beside the cutting head. No people.",
 "旁边是捆在一起的气管和电缆。"),
("K3", "示意图：火点外圈扩大，覆盖管线和机头",
 "A diagram: a red circle around the burning spot grows larger until it covers the hoses, cables and the cutting head. No people.",
 "火势一扩大，管线和机头都会被波及。"),
# K4
("K4", "风琴管旁的导轨和机架上积满黑色烟灰",
 "Thick black soot and debris cover the rails and frame next to the bellows tube. No people.",
 "风琴管周围积满了黑色烟灰。", "积灰既是隐患也是燃料"),
("K4", "齿条和导轨上的黑色絮状积灰特写",
 "Close-up of fluffy black soot built up on a toothed rack and guide rail. No people.",
 "齿条、导轨上也全是碎屑。"),
("K4", "积灰图标加上火苗图标，箭头指向更大的火",
 "An icon of soot plus an icon of a flame, with an arrow pointing to a bigger flame. No people.",
 "长期没清洁，积灰还是可燃物。"),
# K5
("K5", "远景中风琴管上部仍有一个暗红色的点",
 "A wide view of the machine head: a dark red glowing spot remains on the upper part of the bellows. No people.",
 "拉远以后，燃烧点还在发红。", "阴燃不会自己熄灭"),
("K5", "一旁红色数码显示仪表亮着，管线缠在下方",
 "A red digital display meter glows in the corner, with tangled hoses below. No people.",
 "机器旁的仪表还亮着。"),
("K5", "沙漏旁一个始终发红的小火点",
 "An hourglass next to a small glowing red spot that keeps glowing. No people.",
 "阴燃不会自己熄灭，要及时发现处理。"),
# 小结
("小结", "欣欣身旁浮现风琴管、烧洞、管线、积灰四个图标",
 "The panda mascot stands beside four icons: a bellows tube, a burned hole, bundled hoses and soot.",
 "风琴管护光路，也会被烧穿阴燃。", "小结"),
("小结", "老李看着机头上积灰的导轨，若有所思",
 "The facility engineer looks thoughtfully at the soot-covered rails on the machine head.",
 "火点挨着管线，积灰是燃料，要早发现。"),
# 结尾
("结尾", "欣欣在切割机旁挥手告别",
 "The panda mascot waves goodbye beside the laser cutting machine.",
 "风琴管的故事就到这里，下次见！"),
]
