# 31_xTool MetalFab Laser Welder - Clean or replace the lens protector 卡通剧本作者源
# 原著版：完全照原片（手持激光焊机厂商教程片段：清洁或更换焊枪保护镜片，画外音讲解），K1–K11，不加补充知识点、不做更正；
# 保留原片的步骤和做法（从擦焊枪直接开始、未讲关机，棉签蘸酒精擦，烧坏擦不净就换）；品牌不出现
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光焊接机保护镜片的清洁与更换",
    "edition": "原著版",
    "points": {
        "K1": "功率下降、火花变弱，查镜片",
        "K2": "在干净的环境里操作",
        "K3": "先擦焊枪，洗手戴手套",
        "K4": "拆顶盖，取出镜片",
        "K5": "脏了用棉签蘸酒精擦",
        "K6": "烧坏擦不净就更换",
        "K7": "取下垫圈和旧镜片",
        "K8": "新镜片不碰玻璃",
        "K9": "撕膜、装片、再撕膜",
        "K10": "装回垫圈",
        "K11": "方向装对，压到位",
    },
    "avoid": ["xTool", "XTOOL", "X-Tool", "MetalFab", "Metal Fab"],
}

SHOTS = [
# 开场
("开场", "欣欣捏着一片小小的圆形镜片，对着光看",
 "The panda mascot holds a small round protective lens up to the light and looks through it.",
 "这一课讲焊枪保护镜片的清洁和更换。", "激光焊接机保护镜片的清洁与更换"),
# 情景
("情景", "阿杰焊接时火花明显变弱，皱起眉头",
 "The young male student, wearing a face shield, welds but the spark is weak and dim; he frowns.",
 "阿杰发现，焊接火花越来越弱了。"),
("情景", "老李走过来，拿起焊枪看了看枪头",
 "The facility engineer walks over, picks up the welding gun and looks at its head.",
 "老李说：多半是保护镜片的问题。"),
("情景", "欣欣在空白白板前竖起一根手指",
 "The panda mascot stands in front of a blank whiteboard and raises one finger.",
 "我们看看怎么清洁和更换。"),
# K1
("K1", "火花强弱对比图，弱火花旁一个镜片图标",
 "Two icons: a bright strong weld spark and a weak dim spark, with a lens icon beside the weak one. No people.",
 "功率下降、火花变弱，可能是镜片脏了坏了。", "功率下降、火花变弱，查镜片"),
# K2
("K2", "老李把焊枪拿到一张干净整洁的台面上",
 "The facility engineer carries the welding gun to a clean, uncluttered bench away from the dusty welding area.",
 "换到干净、少灰尘的地方操作。", "在干净的环境里操作"),
# K3
("K3", "老李用白色无尘布擦拭焊枪外壳",
 "The facility engineer wipes the outside of the welding gun with a white lint-free cloth.",
 "先用无尘布把焊枪外面擦干净，", "先擦焊枪，洗手戴手套"),
("K3", "老李洗手后戴上蓝色无尘手套",
 "The facility engineer washes his hands and pulls on blue lint-free gloves.",
 "再洗手，或者戴上无尘手套。"),
# K4
("K4", "老李拆下焊枪顶部的小盖子",
 "The facility engineer removes the small cover on top of the welding gun.",
 "拆下焊枪顶部的盖子，", "拆顶盖，取出镜片"),
("K4", "老李抽出镜片座",
 "The facility engineer slides the lens holder out of the gun.",
 "取出保护镜片。"),
# K5
("K5", "镜片对着灯光，能看到几个小污点",
 "The lens held up to the light shows a few small spots of dirt. No people.",
 "对着光检查镜片。", "脏了用棉签蘸酒精擦"),
("K5", "老李用棉签蘸酒精，轻轻擦镜片",
 "The facility engineer dips a cotton swab in alcohol and gently wipes the lens.",
 "脏了，就用棉签蘸酒精擦干净。"),
("K5", "擦干净的镜片装回焊枪",
 "The cleaned lens holder is slid back into the welding gun. No people.",
 "擦干净后装回焊枪。"),
# K6
("K6", "一片发黑、有烧痕的镜片",
 "A protective lens with dark burn marks and a crack. No people.",
 "烧坏了、严重脏污擦不掉的，", "烧坏擦不净就更换"),
("K6", "烧坏的镜片和新镜片之间一个箭头",
 "An arrow from the burned lens to a new clear lens. No people.",
 "就要换新的。"),
# K7
("K7", "老李从镜片座上取下白色垫圈和旧镜片",
 "Wearing gloves, the facility engineer removes the white gasket and the old lens from the holder.",
 "戴着手套，取下垫圈和旧镜片。", "取下垫圈和旧镜片"),
# K8
("K8", "老李从透明小盒里取出新镜片",
 "The facility engineer takes a new lens in sealed film out of a small clear box.",
 "取出新镜片。", "新镜片不碰玻璃"),
("K8", "手指按在镜片玻璃上的图标，被红叉划掉",
 "Icon of a fingertip pressing on the lens glass, crossed out with a red X. No people.",
 "手指和工具都不要碰玻璃面。"),
("K8", "老李用干净棉签轻扫镜片表面",
 "The facility engineer gently brushes the lens surface with a clean cotton swab.",
 "不小心沾了灰，用棉签清洁。"),
# K9
("K9", "老李撕掉镜片上面的保护膜，放进镜片座",
 "The facility engineer peels the protective film off the top of the new lens and sets it into the holder.",
 "撕掉上面的保护膜，装进镜片座，", "撕膜、装片、再撕膜"),
("K9", "老李撕掉另一面的保护膜",
 "The facility engineer peels the film off the other side of the lens.",
 "再撕掉另一面的膜。"),
# K10
("K10", "老李把白色垫圈压回镜片上",
 "The facility engineer presses the white gasket back onto the lens in the holder.",
 "装回垫圈。", "装回垫圈"),
# K11
("K11", "老李按方向把镜片座插回焊枪，压到位",
 "The facility engineer slides the lens holder back into the gun in the correct orientation and presses it home.",
 "按正确方向装回焊枪，压到位。", "方向装对，压到位"),
# 小结
("小结", "欣欣身后浮现几个图标",
 "The panda mascot stands with icons behind: a weak spark, a clean bench, a cotton swab and a clear lens.",
 "火花变弱查镜片，干净环境里操作。", "小结", ["查镜片", "干净环境", "酒精棉签", "不碰玻璃"]),
("小结", "欣欣伸出手指数着",
 "The panda mascot counts on its fingers.",
 "脏了擦，坏了换，撕膜装片压到位。"),
# 结尾
("结尾", "欣欣、老李和阿杰挥手告别，焊枪放在支架上",
 "The panda mascot, the facility engineer and the young male student wave goodbye beside the welding gun resting on its cradle.",
 "镜片处理好了，下次见！"),
]
