# 20_Maximum Power Transfer Theorem Viva Voce Questions and Answers Basic Electrical 卡通剧本作者源
# 原著版：完全照原片（“最大功率传输定理验证”实验的口试问答），K1–K8，
# 不加补充知识点、不做本土化和更正（保留 Rth = RL、效率 50%、Pm = E0²/(4RL)，
# 讲者“用 MPPT 获得最大效率”的说法，交流条件只说高年级再学）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "最大功率传输定理口试问答",
    "edition": "原著版",
    "points": {
        "K1": "最大功率传输定理",
        "K2": "交流电路以后再学",
        "K3": "最大功率时效率只有一半",
        "K4": "最大功率怎么算",
        "K5": "什么是内阻",
        "K6": "应用：光伏最大功率点跟踪",
        "K7": "应用：音频放大与收音机",
        "K8": "有疑问就提出",
    },
    "avoid": ["VTU", "Visvesvaraya", "Simplified EEE Studies", "Simplified EEE", "21ELEL17", "21ELEL27", "BE/BTech",
              "Experiment 8"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台前，台上有电池组、滑线变阻器和电表",
 "The panda mascot stands at a lab bench with a battery pack, a sliding rheostat and a blank-dial meter, waving at the camera.",
 "大家好！今天复习最大功率传输定理。", "最大功率传输定理口试问答"),
("开场", "电池、变阻器、光伏板三个图标",
 "Three icons in a row: a battery, a sliding rheostat and a solar panel. No people.",
 "定理、效率、公式、内阻和应用。", "", ["定理", "内阻", "应用"]),
# 情景
("情景", "阿杰调变阻器，盯着功率表读数忽大忽小",
 "The young male student turns a sliding rheostat while watching a meter needle rise and fall.",
 "阿杰调负载，功率先升后降，纳闷了。"),
("情景", "小研在空白纸上画出一条先升后降的曲线",
 "The female graduate student sketches a curve that rises to a peak and then falls on a blank sheet.",
 "小研说：顶点那儿，就有门道。"),
# K1
("K1", "电源和内阻串联，外接一个可变负载电阻的电路图标",
 "A circuit icon: a source with an internal resistor in series, connected to a variable load resistor. No people.",
 "第一题：什么是最大功率传输定理？", "最大功率传输定理", ["Rth", "RL"]),
("K1", "天平两边分别放内阻和负载电阻，正好平衡",
 "A balance scale with an internal resistor icon on one side and a load resistor icon on the other, perfectly level. No people.",
 "条件：负载电阻等于电源内阻。", "", ["Rth=RL"]),
("K1", "负载电阻图标亮起，功率柱达到最高",
 "The load resistor icon glows and a power bar reaches its highest point. No people.",
 "这时负载得到的功率最大。"),
("K1", "功率随负载变化的曲线，顶点被圈出",
 "A curve of power versus load resistance with its peak circled. No people.",
 "负载太大太小，功率都上不去。"),
# K2
("K2", "正弦波图标和一本空白高年级教材",
 "A sine wave icon next to a blank advanced textbook. No people.",
 "交流电路的条件，高年级再详细学。", "交流电路以后再学"),
# K3
("K3", "一个圆饼图一半给负载、一半在内阻上发热",
 "A pie chart split in half: one half flowing to the load, the other half turning into heat in the internal resistor. No people.",
 "第二题：此时效率多少？百分之五十。", "最大功率时效率只有一半", ["50%"]),
("K3", "内阻图标冒出热气",
 "An internal resistor icon giving off heat waves. No people.",
 "一半功率，消耗在电源内部。"),
# K4
("K4", "白板上写着最大功率公式",
 "A whiteboard with a maximum power formula in symbols only. No people.",
 "第三题：最大功率有多大？", "最大功率怎么算", ["Pm=E0²/(4RL)"]),
("K4", "公式中分母的 4 和负载电阻被高亮",
 "The denominator of the formula highlighted. No people.",
 "电动势平方，除以四倍负载电阻。"),
# K5
("K5", "一节电池剖开，里面有一个小电阻图标",
 "A battery icon cut open, revealing a small resistor icon inside. No people.",
 "第四题：什么是内阻？", "什么是内阻"),
("K5", "电池符号与一个电阻串联，被圈在一起",
 "A battery symbol in series with a small resistor, both circled together. No people.",
 "电源内部本身就有电阻，画成串联。", "", ["Rint"]),
("K5", "欧姆符号图标",
 "A large ohm symbol icon. No people.",
 "内阻的单位也是欧姆。"),
# K6
("K6", "屋顶上的光伏板，太阳时隐时现",
 "A solar panel on a rooftop under a sun that moves in and out of clouds. No people.",
 "第五题：应用。光伏发电最典型。", "应用：光伏最大功率点跟踪", ["光伏"]),
("K6", "光照强弱变化，光伏板输出柱子跟着高低起伏",
 "As sunlight brightens and dims, a power bar beside the solar panel rises and falls. No people.",
 "光照一变，光伏板的输出就变。"),
("K6", "一个控制盒连着光伏板，曲线顶点上有一个小圆点跟着移动",
 "A small controller box connected to a solar panel, and a dot that keeps tracking the peak of a power curve. No people.",
 "跟踪控制器随时找功率最高点。", "", ["MPPT"]),
("K6", "小研指着跟踪曲线讲解",
 "The female graduate student points at the tracking curve on a board and explains.",
 "让光伏板始终工作在最大功率点。"),
("K6", "老周竖起大拇指，旁边一个上升箭头",
 "The older man gives a thumbs up beside a rising arrow icon.",
 "原片说：这样能获得最大效率。"),
# K7
("K7", "功放和音箱图标",
 "An audio amplifier icon connected to a loudspeaker icon. No people.",
 "功放带音箱，也讲究匹配。", "应用：音频放大与收音机"),
("K7", "老式收音机调谐旋钮图标",
 "An old radio icon with a tuning knob. No people.",
 "收音机调谐，也用到这个思想。"),
# K8
("K8", "阿杰举手，王老师走过来",
 "The young male student raises his hand and the safety administrator walks over.",
 "复习有疑问，及时问老师。", "有疑问就提出"),
# 小结
("小结", "天平平衡图标和 50% 饼图",
 "A balanced scale icon next to a half-filled pie chart. No people.",
 "负载等于内阻，功率最大，效率一半。", "小结", ["Rth=RL", "50%"]),
("小结", "最大功率公式卡和电池内阻图标",
 "A formula card for maximum power next to a battery icon with a small internal resistor. No people.",
 "最大功率公式和内阻，也要记牢。"),
("小结", "光伏板、功放、收音机三个图标",
 "Three icons: a solar panel, an audio amplifier and a radio. No people.",
 "光伏跟踪、功放、收音机都用得上。"),
# 结尾
("结尾", "欣欣在整理好的实验台前挥手",
 "The panda mascot waves goodbye at a tidy lab bench with a battery pack and a rheostat.",
 "祝口试顺利，下次见！"),
]
