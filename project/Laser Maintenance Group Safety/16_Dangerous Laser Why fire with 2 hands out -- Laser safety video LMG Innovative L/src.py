# 16_Dangerous Laser Why fire with 2 hands out -- Laser safety video LMG Innovative L 卡通剧本作者源
# 原著版：完全照原片（1 分 43 秒：用厚亚克力块演示为什么手动出光时双手要在外面），K1–K8，不加补充知识点、不做更正；
# 保留原片内容：讲解人干了 25 年；切割时很安静让人觉得温和安全，喷嘴与金属间的间隙却极其剧烈、金属被汽化；
# 用与胶带打点、对中镜片相同的出光设置打穿亚克力（“比手指硬多了”），光斑很细，从背面出来；
# 旧式接触式切割头有人用两根手指垫在喷嘴下，手指一滑光就穿过，手指受伤、指甲裂开像被钉子钉穿
# 讲解人出光前把手伸到喷嘴下摆放亚克力块照原片；原片没讲双按钮机理、灼伤处置、塑料烟气，本版也不加；玩笑和调侃不用
# 讲解人姓名、公司名和联系方式不出现，讲解人改为老李
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "危险激光：为什么出光时双手要放在外面",
    "edition": "原著版",
    "points": {
        "K1": "安静，不等于安全",
        "K2": "喷嘴下面，金属瞬间汽化",
        "K3": "手动出光：双手在外",
        "K4": "演示：打一块透明硬塑料",
        "K5": "光斑很细，一穿到底",
        "K6": "这就是双手在外的原因",
        "K7": "手指垫在喷嘴下，最危险",
        "K8": "手指受伤，非常疼",
    },
    "avoid": ["Scott Kiser", "Kiser", "Kyzer", "Innovative Laser", "Innovative Laser & Design", "InnovativeLaserCutting", "LaserServiceGuy", "Laser Maintenance Group", "LMG", "lasersolutions", "comcast", "Darwin"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光切割机旁，举起两只手掌",
 "The panda mascot stands beside a laser cutting machine and holds up both paws.",
 "出光时，为什么双手要放在外面？", "危险激光：为什么出光时双手要放在外面"),
("开场", "两只手图标在机器外面，喷嘴下一块透明块",
 "Two hand icons placed outside a machine outline, and a clear block under a nozzle. No people.",
 "老李用一块亚克力来说明。"),
# 情景
("情景", "老李站在车间里，身后是储罐和激光切割机",
 "The facility engineer stands in the workshop with cryogenic tanks and a laser cutting machine behind him.",
 "老李干激光这一行，已经25年了。"),
("情景", "老李走到切割头前，手里拿着一块厚透明亚克力块",
 "The facility engineer walks to the cutting head holding a thick clear acrylic block.",
 "今天他要做一个小演示。"),
# K1
("K1", "切割头在钢板上安静地移动，只有细细的气流",
 "A cutting head moves quietly over a steel sheet with only a soft stream of gas. No people.",
 "切割正常的时候，非常安静。", "安静，不等于安全"),
("K1", "一个轻柔的声音图标",
 "A soft, gentle sound wave icon. No people.",
 "只听到轻轻的气流声。"),
("K1", "安静的声音图标旁一个笑脸和盾牌",
 "A soft sound icon next to a smiling face and a shield. No people.",
 "让人觉得它很温和、很安全。"),
# K2
("K2", "喷嘴下方小小的间隙放大图，金属变成蒸汽冒出",
 "A magnified view of the small gap under the nozzle: metal turning into vapor and shooting out. No people.",
 "可喷嘴和金属之间那一小段间隙，", "喷嘴下面，金属瞬间汽化"),
("K2", "间隙里光和火花剧烈翻腾",
 "Inside the tiny gap, intense light and sparks churn violently. No people.",
 "其实极其剧烈。"),
("K2", "金属块图标瞬间消失，变成一缕烟",
 "A metal block icon vanishes instantly into a wisp of vapor. No people.",
 "金属是被直接汽化掉的。"),
# K3
("K3", "两只手放在机器外侧的示意",
 "A diagram: two hands placed on the outside of the machine, away from the nozzle. No people.",
 "厂家要求，手动出光时双手放在外面。", "手动出光：双手在外"),
("K3", "老李把空白胶带贴在喷嘴下，准备打点",
 "The facility engineer sticks a piece of blank tape under the nozzle to prepare a test shot.",
 "比如胶带打点，对中镜片的时候。"),
("K3", "老李把手伸到喷嘴下，放好亚克力块，再收回手",
 "The facility engineer reaches under the nozzle, places the acrylic block, then pulls his hand back.",
 "为什么？老李把亚克力块放到喷嘴下。"),
# K4
("K4", "一块厚厚的透明亚克力块放在喷嘴下的纸板上",
 "A thick clear acrylic block sits on cardboard right under the nozzle. No people.",
 "出光设置，和打点对中完全一样。", "演示：打一块透明硬塑料"),
("K4", "手指图标和亚克力块图标比硬度，亚克力更硬",
 "A finger icon and an acrylic block icon compared on a hardness scale; the acrylic is harder. No people.",
 "亚克力，比手指可硬多了。"),
("K4", "切割头上方闪一下，出光",
 "The cutting head flashes briefly as the laser fires one shot. No people.",
 "按同样的功率、同样的时间，打一枪。"),
# K5
("K5", "亚克力块里出现一条细细的贯穿孔",
 "A thin channel appears through the acrylic block from top to bottom. No people.",
 "光从上到下，直接打穿了。", "光斑很细，一穿到底"),
("K5", "老李拿起亚克力块，对着镜头展示细孔",
 "The facility engineer holds up the acrylic block to the camera, showing the thin hole.",
 "光束就这么细。"),
("K5", "亚克力块底面的出口小孔特写",
 "Close-up of the small exit hole on the bottom face of the acrylic block. No people.",
 "看，它从背面出来了。"),
# K6
("K6", "老李举着亚克力块，另一只手竖起两根手指",
 "The facility engineer holds the acrylic block and raises two fingers with his other hand.",
 "这就是出光时，", "这就是双手在外的原因"),
("K6", "两只手图标在机器外面打勾",
 "Two hand icons outside the machine with a green check. No people.",
 "双手要放在外面的原因。"),
# K7
("K7", "旧式接触式切割头的示意图",
 "A diagram of an old contact-style cutting head touching the work surface. No people.",
 "以前有一种接触式切割头。", "手指垫在喷嘴下，最危险"),
("K7", "老李用手比划两根手指垫在喷嘴下的动作",
 "The facility engineer mimes putting two fingers under the nozzle, with the acrylic block in his other hand.",
 "有人会用两根手指垫在喷嘴下面。"),
("K7", "手指一滑，光束直接穿过的示意",
 "A diagram: a finger slips under the nozzle and the beam goes right through that spot. No people.",
 "手指一滑，光就穿过去了。"),
# K8
("K8", "手指侧面一道伤口的图标",
 "An icon of a finger with a cut on its side and a bandage. No people.",
 "很多人手指侧面留下了伤口。", "手指受伤，非常疼"),
("K8", "指甲裂开的图标和一颗钉子图标",
 "An icon of a split fingernail next to a nail icon. No people.",
 "还有人指甲被打裂，像被钉子钉穿。"),
("K8", "老李皱眉摇头",
 "The facility engineer frowns and shakes his head.",
 "据说疼得要命。"),
# 小结
("小结", "欣欣身旁浮现安静声音、汽化、亚克力细孔图标",
 "The panda mascot stands beside icons of a soft sound, vaporizing metal and an acrylic block with a thin hole.",
 "安静不等于安全，间隙里金属汽化。", "小结"),
("小结", "两只手图标在机器外面，手指图标打红叉",
 "Two hand icons outside the machine, and a finger-under-nozzle icon crossed out with a red X. No people.",
 "打点也能穿透，出光时双手在外。"),
# 结尾
("结尾", "欣欣双手举在身前挥手告别",
 "The panda mascot holds both paws up and waves goodbye.",
 "双手在外，下次见！"),
]
