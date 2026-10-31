# 08_CO2 or Class D Fire Extinguishers with Laser Systems Which should you use Innova 卡通剧本作者源
# 原著版：完全照原片（1 分 17 秒：激光设备旁用二氧化碳还是 D 类灭火器），K1–K8，不加补充知识点、不做更正；
# 保留原片说法：按原片的 D 类（Class D）称呼；干粉喷一次修理费多一千美元、干粉遇湿气腐蚀金属“毁掉一切”是“一场灾难”；
# 二氧化碳排开氧气、挥发不留东西、比干粉贵但一次损坏够买好几个；电气火灾肯定用二氧化碳；D 类只为钛等能燃烧的特殊金属，烧起来很难扑灭
# 原片没讲二氧化碳的人员风险、断电、报警撤离，本版也不加；讲解人姓名、公司名、网址和联系方式不出现，讲解人改为老李
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光设备旁，选对灭火器",
    "edition": "原著版",
    "points": {
        "K1": "人人都想看激光",
        "K2": "车间里的两种灭火器",
        "K3": "干粉会让维修费大涨",
        "K4": "干粉残留会腐蚀设备",
        "K5": "二氧化碳：灭火不留痕",
        "K6": "贵一点，反而更省",
        "K7": "带电设备着火用二氧化碳",
        "K8": "D类灭火器只为特殊金属",
    },
    "avoid": ["Scott Kiser", "Kiser", "Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "LaserServiceGuy", "Laser Maintenance Group", "LMG"],
}

SHOTS = [
# 开场
("开场", "欣欣站在两个灭火器之间，一红一黄，向镜头招手",
 "The panda mascot stands between a red extinguisher and a yellow extinguisher and waves at the camera.",
 "激光设备旁，该用哪种灭火器？", "激光设备旁，选对灭火器"),
("开场", "二氧化碳灭火器和D类灭火器两个图标，中间一个问号",
 "Two icons, a carbon dioxide extinguisher and a metal fire extinguisher, with a question mark between them. No people.",
 "二氧化碳，还是D类？", "", ["二氧化碳", "D类"]),
# 情景
("情景", "办公区门口，老李对着镜头讲话",
 "At an office door, the facility engineer talks to the camera.",
 "老李在车间门口开讲。"),
# K1
("K1", "访客们兴奋地看激光切割机工作",
 "Excited visitors watch a laser cutting machine at work.",
 "人人都想来看看激光。", "人人都想看激光"),
("K1", "访客回家给朋友讲述的图标",
 "An icon of a visitor at home telling friends about the laser, with a speech bubble. No people.",
 "回去还要讲给朋友听。"),
# K2
("K2", "废料架旁地上放着一个黄色灭火器",
 "A yellow fire extinguisher stands on the floor next to a scrap metal rack. No people.",
 "车间里有D类灭火器，", "车间里的两种灭火器", ["D类"]),
("K2", "门边墙上挂着带喇叭筒的红色灭火器，旁边是卷管",
 "A red carbon dioxide extinguisher with a horn nozzle hangs on the wall by the door, next to a coiled air hose. No people.",
 "也有二氧化碳灭火器。", "", ["二氧化碳"]),
("K2", "老李一手指黄色，一手指红色",
 "The facility engineer points at the yellow extinguisher with one hand and the red one with the other.",
 "两种各有各的用处。"),
# K3
("K3", "激光机控制柜打开，里面是密密麻麻的电路板",
 "An opened laser machine control cabinet full of circuit boards. No people.",
 "激光设备里有很多精密娇贵的电子件。", "干粉会让维修费大涨"),
("K3", "白色粉末喷满电路板",
 "White extinguisher powder covers the circuit boards. No people.",
 "要是用干粉灭火器一喷，"),
("K3", "一张空白维修账单上加了一千美元",
 "A blank repair bill with a stack of dollar coins added to it. No people.",
 "修理费就多出一千美元。", "", ["+1000美元"]),
# K4
("K4", "粉末遇到水汽图标，电路板上出现锈斑",
 "Powder meets water vapor droplets in the air and rust spots spread on the circuit board. No people.",
 "干粉遇到空气里的湿气，", "干粉残留会腐蚀设备"),
("K4", "金属件生锈损坏的图标",
 "Icons of corroded and ruined metal parts. No people.",
 "会腐蚀金属，把一切都毁掉。"),
("K4", "老李摇头，摊开双手",
 "The facility engineer shakes his head and spreads his hands.",
 "老李说：那简直是一场灾难。"),
# K5
("K5", "示意图：二氧化碳气体罩住火焰，把氧气挤走",
 "A diagram: carbon dioxide gas covers a flame and pushes the oxygen away. No people.",
 "二氧化碳把氧气排开，火就灭了。", "二氧化碳：灭火不留痕"),
("K5", "气体散去，电路板干干净净",
 "The gas drifts away and the circuit board is left clean. No people.",
 "然后它挥发掉，什么都不留。"),
# K6
("K6", "一个二氧化碳灭火器和一个干粉灭火器，价签一高一低",
 "A carbon dioxide extinguisher with a higher blank price tag next to a powder extinguisher with a lower one. No people.",
 "二氧化碳灭火器比干粉的贵。", "贵一点，反而更省"),
("K6", "一张维修账单对面摆着好几个二氧化碳灭火器",
 "A long repair bill on one side and several carbon dioxide extinguishers on the other side of a scale. No people.",
 "可一次干粉损坏的钱，"),
("K6", "天平倒向灭火器一边",
 "The scale tips toward the row of carbon dioxide extinguishers. No people.",
 "够买好几个二氧化碳灭火器。"),
# K7
("K7", "老李手扶墙上的二氧化碳灭火器",
 "The facility engineer rests his hand on the red carbon dioxide extinguisher on the wall.",
 "所以电气火灾，", "带电设备着火用二氧化碳"),
("K7", "电闪图标加火苗，连到二氧化碳灭火器打勾",
 "An electrical bolt icon with a flame, linked to a carbon dioxide extinguisher with a green check. No people.",
 "肯定要用二氧化碳灭火器。"),
# K8
("K8", "老李指向废料架旁的黄色灭火器",
 "The facility engineer points at the yellow extinguisher by the scrap rack.",
 "D类灭火器只为特殊金属准备。", "D类灭火器只为特殊金属", ["D类"]),
("K8", "钛和合金块的图标",
 "Icons of titanium blocks and alloy pieces. No people.",
 "比如钛，还有一些能燃烧的合金。", "", ["钛", "合金"]),
("K8", "金属块上冒出白亮的火焰",
 "A metal block burning with a bright white flame. No people.",
 "这些金属一旦烧起来，很难扑灭。"),
# 小结
("小结", "欣欣身旁浮现电路板、粉末、二氧化碳、D类四个图标",
 "The panda mascot stands beside four icons: a circuit board, powder, a carbon dioxide extinguisher and a metal fire extinguisher.",
 "干粉伤设备，二氧化碳不留东西。", "小结"),
("小结", "红色和黄色两个灭火器并排",
 "The red and yellow extinguishers side by side. No people.",
 "电气火灾用二氧化碳，特殊金属用D类。"),
# 结尾
("结尾", "欣欣在两个灭火器之间挥手",
 "The panda mascot waves goodbye between the two extinguishers.",
 "选对灭火器，下次见！"),
]
