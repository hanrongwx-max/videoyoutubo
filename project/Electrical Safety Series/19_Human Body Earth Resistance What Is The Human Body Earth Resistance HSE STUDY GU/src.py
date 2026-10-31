# 19_Human Body Earth Resistance What Is The Human Body Earth Resistance HSE STUDY GU 卡通剧本作者源
# 原著版：完全照原片（一道面试选择题：人体电阻约多少），K1–K6，不加补充知识点、不做本土化和更正
# （保留原片答案 D 约 1000 Ω、依据美国国家职业安全卫生研究所的说法；机构只写中文，META["avoid"] 照抄国内版）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "人体对地电阻",
    "edition": "原著版",
    "points": {
        "K1": "面试常问：人体电阻多少",
        "K2": "四个选项",
        "K3": "答案：约一千欧",
        "K4": "依据：美国机构，潮湿约一千欧",
        "K5": "干燥时电阻更高",
        "K6": "人体会成为电流入地的通路",
    },
    "avoid": ["HSE Study Guide", "HSE STUDY GUIDE", "HSE study guide", "NIOSH",
              "National Institute of Occupational Safety and Health",
              "National Institute for Occupational Safety and Health"],
}

SHOTS = [
# 开场
("开场", "欣欣站在白板前，白板上画着一个空白的人形轮廓",
 "The panda mascot stands in front of a whiteboard with a simple blank human outline drawn on it and waves at the camera.",
 "这一课聊聊人体电阻。", "人体对地电阻"),
("开场", "人形图标、电阻符号、水滴三个图标",
 "Three icons in a row: a human pictogram, a resistor symbol and a water droplet. No people.",
 "它有多大，湿了又会怎样。", "", ["人体", "电阻", "潮湿"]),
# 情景
("情景", "阿杰刚洗完手，湿着手伸向仪器的电源开关",
 "The young male student, hands still dripping after washing, reaches toward the power switch of a lab instrument.",
 "阿杰洗完手，湿着手就去开仪器。"),
("情景", "小研递给他一张擦手纸，指了指他的手",
 "The female graduate student hands him a paper towel and points at his wet hands.",
 "小研拦住他：先把手擦干。"),
("情景", "阿杰挠头，一脸不解",
 "The young male student scratches his head with a puzzled look, holding the paper towel.",
 "阿杰不解：人不是有电阻吗？"),
("情景", "欣欣在白板前竖起手指",
 "The panda mascot stands in front of the whiteboard and raises one finger.",
 "这个电阻，可没你想的那么大。"),
# K1
("K1", "面试场景：王老师坐在桌后，阿杰坐在对面",
 "An interview scene: the safety administrator sits behind a desk with blank papers, the young male student sits across.",
 "安全岗位面试，常会问到这个问题。", "面试常问：人体电阻多少"),
("K1", "阿杰面前浮现一个问号气泡",
 "A big question mark bubble floats above the young male student's head.",
 "人体电阻大约是多少？"),
# K2
("K2", "白板上四张空白卡片排成一列",
 "Four blank answer cards in a column on a whiteboard, each with a small letter circle. No people.",
 "四个选项，选一个。", "四个选项", ["A 5欧", "B 25欧", "C 500欧", "D 1000欧"]),
("K2", "沙漏图标，卡片旁有思考气泡",
 "An hourglass icon beside the four answer cards and a thought bubble. No people.",
 "先想一想，你会选哪个？"),
# K3
("K3", "第四张卡片亮起，打绿勾",
 "The fourth answer card lights up with a green check mark. No people.",
 "答案是D，大约一千欧。", "答案：约一千欧", ["D 约1000欧"]),
("K3", "前三张卡片变灰",
 "The first three answer cards turn gray and fade. No people.",
 "前三个数都太小了。"),
# K4
("K4", "一只湿手图标，水滴往下滴",
 "An icon of a wet hand with water droplets dripping down. No people.",
 "潮湿条件下，人体电阻约一千欧。", "依据：美国机构，潮湿约一千欧", ["潮湿", "约1000欧"]),
("K4", "空白文件夹图标，旁边地球图标",
 "A blank document folder icon next to a small globe icon. No people.",
 "依据美国国家职业安全卫生研究所。"),
# K5
("K5", "干燥的手图标，电阻符号变大",
 "An icon of a dry hand next to a resistor symbol that grows larger. No people.",
 "皮肤干燥时，电阻会更高。", "干燥时电阻更高"),
("K5", "湿手和干手两个图标，中间一个大于号",
 "A dry hand icon and a wet hand icon side by side with a greater-than sign between them. No people.",
 "一沾水，电阻就降下来。", "", ["干燥", "潮湿"]),
# K6
("K6", "简化电路：电源、开关、灯泡，一个简笔人手碰导线",
 "A simple circuit diagram: power source, switch and a light bulb; a stick figure touches the live wire. No people.",
 "人碰到带电导线，", "人体会成为电流入地的通路"),
("K6", "黄色箭头从手经身体流到脚下的接地符号",
 "A yellow arrow runs from the stick figure's hand through its body down to a ground symbol at its feet. No people.",
 "电流就会经过人体流入大地。"),
("K6", "电阻符号变小，电流箭头变粗",
 "A resistor symbol shrinks while the current arrow beside it grows thicker and red. No people.",
 "电阻越小，流过人体的电流越大。"),
("K6", "湿手图标旁电流箭头变粗",
 "An icon of a wet hand next to a current arrow that grows thicker. No people.",
 "潮湿时电阻低，电流就更大。"),
# 小结
("小结", "欣欣身旁浮现湿手和电阻图标",
 "The panda mascot stands beside floating icons of a wet hand and a small resistor symbol.",
 "潮湿时人体电阻只有约一千欧。", "小结"),
("小结", "电阻变小、电流变大的箭头",
 "Icons of a shrinking resistor and a growing current arrow. No people.",
 "电阻越小，触电越危险。"),
("小结", "面试桌和打绿勾的D选项卡片",
 "An interview desk icon next to answer card D with a green check. No people.",
 "面试再问到，记住答案选D。"),
# 结尾
("结尾", "欣欣用毛巾擦干手，向镜头挥手",
 "The panda mascot dries its paws with a towel and waves goodbye at the camera.",
 "擦干双手再用电，下次见！"),
]
