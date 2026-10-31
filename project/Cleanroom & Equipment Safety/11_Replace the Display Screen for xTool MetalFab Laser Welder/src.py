# 11_Replace the Display Screen for xTool MetalFab Laser Welder 卡通剧本作者源
# 原著版：完全照原片（厂商售后视频：更换焊机显示屏和保护面板，无旁白、只有字幕），K1–K15，不加补充知识点、不做更正；
# 保留原片警示（仅限专业人员、断电、至少等 5 分钟、全程戴绝缘手套）、3 / 2 mm 十字刀、8 颗螺钉、黄色一侧朝右，
# 以及原片画面（操作者徒手、本片无静置字幕）；品牌字样不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊机：更换显示屏",
    "edition": "原著版",
    "points": {
        "K1": "只限专业人员，先断电",
        "K2": "高压和强激光的伤害",
        "K3": "断电后仍有残余高压",
        "K4": "全程戴绝缘手套",
        "K5": "准备工具和备件",
        "K6": "关机，拔掉所有线缆",
        "K7": "锁住四个脚轮",
        "K8": "撬起四角，揭下保护面板",
        "K9": "拆显示屏的固定螺钉",
        "K10": "抬屏拔排线，有胶先去胶",
        "K11": "拆背面螺钉，屏和支架分开",
        "K12": "新屏装支架，孔位对图",
        "K13": "放回主机，接好排线",
        "K14": "拧紧固定螺钉",
        "K15": "贴新保护面板",
    },
    "avoid": ["xTool", "X-Tool", "XTool", "X Tool", "MetalFab", "Metal Fab", "Designed by xTool"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光焊接机旁，指着机器顶部的显示屏，向镜头招手",
 "The panda mascot stands beside a gray wheeled laser welding machine, points at the blank display screen on its top, and waves at the camera.",
 "这一课，看焊机的显示屏怎样更换。", "激光焊接机显示屏的规范更换"),
("开场", "四个图标：警示卡、撬棒、显示屏、保护面板",
 "Four icons in a row: a warning card, a pry bar, a blank display screen and a clear screen protector. No people.",
 "揭面板、拆旧屏、装新屏、贴面板。", "", ["揭面板", "拆旧屏", "装新屏", "贴面板"]),
# 情景
("情景", "阿杰在焊机前，显示屏一半花屏一半黑",
 "The young male student stands at the laser welding machine; its display screen shows flickering stripes on one half and is black on the other half.",
 "阿杰发现焊机屏幕花了，一半看不见。"),
("情景", "老李提着工具箱和新屏幕走来",
 "The facility engineer walks in carrying a toolbox and a boxed new display screen.",
 "专业技术人员老李来换屏。"),
("情景", "欣欣在空白白板前竖起手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看怎么一步步换。"),
# K1
("K1", "欣欣举着黄黑边框警示卡，卡面只有闪电和人形打叉图标",
 "The panda mascot holds up a warning card with a yellow and black striped border, showing a lightning bolt icon and a crossed-out person icon.",
 "换屏也属于拆机，只限专业人员。", "只限专业人员，先断电"),
# K2
("K2", "机箱剖面示意：一边闪电图标，一边激光束图标",
 "A simple cutaway diagram of a machine cabinet with a lightning bolt icon on one side and a red laser beam icon on the other side. No people.",
 "机内高压和强激光，会触电、烧伤。", "高压和强激光的伤害", ["高电压", "强激光"]),
# K3
("K3", "拔掉插头的焊机，内部一个模块上闪电图标，旁边沙漏",
 "An unplugged laser welding machine with a cutaway showing one module with a glowing lightning bolt icon, and an hourglass beside it. No people.",
 "可能残留高压，至少等5分钟再碰。", "断电后仍有残余高压", ["≥5分钟"]),
# K4
("K4", "警示卡上一副绝缘手套图标",
 "A warning card with a yellow and black striped border showing an insulated glove icon. No people.",
 "全程戴好绝缘手套。", "全程戴绝缘手套"),
# K5
("K5", "工作台上摆着两把细十字螺丝刀、撬棒、镊子、新显示屏和新保护面板",
 "On a workbench lie two thin cross-head screwdrivers of different sizes, a thin pry bar, tweezers, a new blank display screen and a new clear screen protector with a black frame. No people.",
 "备好3毫米、2毫米十字刀，撬棒和镊子。", "准备工具和备件", ["3mm十字刀", "2mm十字刀", "撬棒", "镊子"]),
("K5", "老李拿起新显示屏和新保护面板",
 "The facility engineer holds up the new display screen and the new screen protector.",
 "还有新显示屏和新保护面板。"),
# K6
("K6", "老李关掉电源开关，拔下背面所有线缆",
 "The facility engineer switches off the machine and unplugs all cables from the back panel.",
 "关机，拔掉所有线缆。", "关机，拔掉所有线缆"),
# K7
("K7", "老李踩下脚轮刹车",
 "The facility engineer presses down the brake on a caster wheel with his foot.",
 "四个脚轮全部锁住。", "锁住四个脚轮"),
# K8
("K8", "机器顶部俯视，老李用撬棒插进保护面板一角",
 "Top view of the machine: the facility engineer inserts a thin pry bar under one corner of the black-framed screen protector.",
 "用撬棒撬起保护面板的四个角。", "撬起四角，揭下保护面板"),
("K8", "保护面板被整片揭下",
 "The screen protector is lifted off in one piece, revealing the display beneath.",
 "再把整片保护面板揭下来。"),
# K9
("K9", "老李用细十字刀拧下屏幕四周的螺钉",
 "The facility engineer uses a thin cross-head screwdriver to remove the screws around the display edge.",
 "用2毫米十字刀，拆下四周8颗螺钉。", "拆显示屏的固定螺钉"),
# K10
("K10", "老李把屏幕轻轻抬起，露出背面的排线插头",
 "The facility engineer gently lifts the display, revealing a small ribbon cable connector on its back.",
 "轻轻抬起屏幕，背面连着排线。", "抬屏拔排线，有胶先去胶"),
("K10", "镊子剥掉插头上的一点胶",
 "Close view of tweezers peeling a small blob of adhesive off the connector.",
 "插头上有胶，先用镊子剥掉。"),
("K10", "手指捏住插头拔下",
 "Close view of fingers holding the connector body and pulling it out.",
 "再小心拔下排线。"),
# K11
("K11", "屏幕翻过来，背面绿色电路板，老李拧下螺钉",
 "The display is turned over showing a green circuit board on its back, and the facility engineer removes the screws.",
 "用3毫米十字刀拆背面8颗螺钉。", "拆背面螺钉，屏和支架分开"),
("K11", "显示屏和金属支架分开",
 "The display panel is separated from its metal bracket.",
 "把显示屏和支架分开。"),
# K12
("K12", "新屏和支架并排，红圈标出两个孔和黄色区域",
 "The new display and the bracket side by side, with red circles marking two bracket holes and a yellow area on the display. No people.",
 "新屏装支架，黄色区域和孔位要对图。", "新屏装支架，孔位对图"),
("K12", "老李拧紧背面八颗螺钉",
 "The facility engineer tightens the eight screws on the back of the display.",
 "拧紧背面八颗螺钉。"),
# K13
("K13", "显示组件放回主机，黄色一侧朝右",
 "The display assembly is placed back into the top of the machine with its yellow-marked side on the right. No people.",
 "放回主机，黄色那一侧朝右。", "放回主机，接好排线"),
("K13", "排线插头插好，卡扣扣上",
 "The ribbon cable connector is pushed in and its latch clicks shut.",
 "接上排线，插到位。"),
# K14
("K14", "老李拧紧屏幕四周的八颗螺钉",
 "The facility engineer tightens the eight screws around the display edge.",
 "拧紧屏幕四周八颗螺钉。", "拧紧固定螺钉"),
# K15
("K15", "新保护面板对齐四角贴上，手掌抹平",
 "The new screen protector is aligned at all four corners, placed on, and smoothed down with a palm.",
 "对齐四角贴上新保护面板，抹平。", "贴新保护面板"),
# 小结
("小结", "欣欣站在焊机旁，身后浮现四个图标",
 "The panda mascot stands beside the laser welding machine with four icons behind: a warning card, a pry bar, tweezers and a screwdriver.",
 "专业人员操作，断电拔线，锁脚轮。", "小结", ["专业人员", "断电", "锁脚轮"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "孔位对图，黄色朝右，贴好新面板。"),
# 结尾
("结尾", "欣欣、老李、小研和阿杰在亮着的新屏幕前挥手",
 "The panda mascot, the facility engineer, the female graduate student and the young male student wave goodbye in front of the machine with its new glowing screen.",
 "新屏幕装好了，下次见！"),
]
