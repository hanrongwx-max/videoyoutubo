# 03_Why Do Routine Laser Maintenance -- Laser Maintenance Group Kiser 卡通剧本作者源
# 原著版：完全照原片（53 秒访谈，小贴士第 1 条），K1–K6，不加补充知识点、不做更正；
# 保留原片数字：原厂要求每 1000 小时维护、一班制约半年一次、两班各 10 小时一天 20 小时约六周到期（原话“六周”照用）；
# 保留原片说法：零件不贵但可能是灾难性的，更大损失是停机（等两天、修几个小时、再把机器调起来）；维修者徒手拿镜座照原片
# 受访者姓名、公司名和网址不出现，访谈双方改为老周（提问）和老李（维修负责人）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "为什么要做激光设备例行维护",
    "edition": "原著版",
    "points": {
        "K1": "按厂家要求定期维护",
        "K2": "按运行小时算周期",
        "K3": "“太忙了，不想停机”",
        "K4": "小零件，可能酿大祸",
        "K5": "最贵的是停机时间",
        "K6": "切割头里的易损件",
    },
    "avoid": ["Scott Kiser", "Kiser", "Kaiser", "Laser Maintenance Group", "LMG", "LaserServiceGuy", "Innovative Laser", "InnovativeLaserCutting"],
}

SHOTS = [
# 开场
("开场", "欣欣站在一张摆满激光零件的桌子旁，向镜头招手",
 "The panda mascot stands beside a table covered with laser machine parts and waves at the camera.",
 "激光设备为什么要例行维护？", "为什么要做激光设备例行维护"),
("开场", "欣欣举起一张空白卡片，上面画着一个扳手和数字1",
 "The panda mascot holds up a blank card with a wrench icon and the number one.",
 "这是维护小贴士的第一条。", "", ["小贴士 1"]),
# 情景
("情景", "老周和老李坐在桌边，桌上放着拆下来的切割头部件",
 "The older man and the facility engineer sit at a table with disassembled laser cutting head parts on it.",
 "老周请维修负责人老李来聊维护。"),
("情景", "老李手里转着一个黄铜镜座",
 "The facility engineer turns a brass mirror mount over in his bare hands.",
 "老李一边摆弄零件，一边回答。"),
("情景", "老周掰着手指提问",
 "The older man counts on his fingers while asking a question.",
 "老周问：到底多久维护一次？"),
# K6
("K6", "桌上排着黄铜镜座、金黄色透镜、铜喷嘴和一段弯折的铜管",
 "On a black table: a brass mirror mount, a golden lens in a clear case, a copper nozzle and a bent copper tube. No people.",
 "桌上是切割头里拆下的零件。", "切割头里的易损件"),
("K6", "示意图：切割头剖面，镜片、喷嘴、冷却水管的位置",
 "A cross-section diagram of a laser cutting head showing where the mirror mount, lens, nozzle and cooling water tube sit. No people.",
 "镜座、透镜、喷嘴，还有冷却水管。", "", ["镜座", "透镜", "喷嘴", "冷却水管"]),
("K6", "老李翻过镜座，露出顶部水接头和中间透镜孔",
 "The facility engineer flips the brass mount to show a water fitting on top and a lens opening in the middle.",
 "这些都是例行维护要检查的地方。"),
# K1
("K1", "老李翻开一本空白设备说明书，指着一页",
 "The facility engineer opens a blank equipment manual and points at a page.",
 "原厂的要求是：每1000小时维护一次。", "按厂家要求定期维护", ["1000小时"]),
("K1", "运行计时器图标走到1000，弹出扳手图标",
 "A run-hour counter icon reaches one thousand and a wrench icon pops up. No people.",
 "机器每跑满1000小时，就该保养。", "", ["每1000小时"]),
("K1", "说明书图标连到一个周期循环箭头",
 "A blank manual icon linked to a circular repeat arrow with a wrench. No people.",
 "维护要按周期，一轮接一轮。"),
# K2
("K2", "三台机器：一个班、两个班、三个班的图标",
 "Three machine icons labeled with one, two and three work shift symbols. No people.",
 "开一班、两班、三班，大不一样。", "按运行小时算周期", ["一班", "两班", "三班"]),
("K2", "一个太阳图标的机器慢慢走表，日历翻过半年",
 "A machine with a sun icon whose hour counter turns slowly while a calendar flips through six months. No people.",
 "只开一班，1000小时大约半年。", "", ["一班 约半年"]),
("K2", "两个10小时班接力，一天20小时",
 "Two shift icons of ten hours each side by side, adding up to a twenty-hour day. No people.",
 "老周的厂两班各10小时，一天20小时。", "", ["2×10小时"]),
("K2", "日历上的维护标记从远处挪到很近",
 "A maintenance mark on a calendar moves from far away to only a few weeks ahead. No people.",
 "这样大约六周就到维护周期了。", "", ["约六周"]),
# K3
("K3", "老周站在忙碌的车间里，指着运转的机器摇头",
 "The older man stands in a busy workshop pointing at a running machine and shaking his head.",
 "老周说：机器正忙，真不想停。", "“太忙了，不想停机”"),
("K3", "一张被一推再推的日历图标",
 "A calendar icon whose maintenance mark keeps getting pushed later and later. No people.",
 "生产一忙，维护就一拖再拖。"),
# K4
("K4", "老李把镜座翻过来，露出中间的透镜孔",
 "The facility engineer turns the brass mount over to show the lens opening in the middle.",
 "老李说：这次坏的零件不算贵。", "小零件，可能酿大祸"),
("K4", "一个小小的镜片图标，价格标签很小",
 "A small lens icon with a tiny blank price tag. No people.",
 "就零件本身来说，花不了多少钱。"),
("K4", "小镜片图标旁一个巨大的警告三角",
 "A small lens icon next to a huge warning triangle. No people.",
 "可后果，本来可能是灾难性的。"),
# K5
("K5", "一个大大的沙漏，旁边是停着的切割机",
 "A large hourglass next to a stopped laser cutting machine. No people.",
 "更大的代价，是停机的时间。", "最贵的是停机时间"),
("K5", "日历上两天被划掉，再加一个扳手和时钟",
 "Two days crossed out on a calendar, then a wrench icon and a clock showing a few hours. No people.",
 "等两天人才进场，再修几个小时。", "", ["等2天", "修几小时"]),
("K5", "机器重新启动、调试的图标",
 "An icon of a machine being restarted and adjusted with a wrench and a check mark. No people.",
 "修完还得把机器重新调起来。"),
# 小结
("小结", "欣欣身旁浮现1000小时、日历、沙漏三个图标",
 "The panda mascot stands beside three icons: a run-hour counter, a calendar and an hourglass.",
 "原厂要求每1000小时维护一次。", "小结", ["1000小时"]),
("小结", "老周和老李握手，桌上的零件摆放整齐",
 "The older man and the facility engineer shake hands over the table of neatly arranged parts.",
 "按运行小时算，别因为忙就拖。"),
# 结尾
("结尾", "欣欣举着扳手挥手告别",
 "The panda mascot holds a wrench and waves goodbye.",
 "小贴士第一条就到这里，下次见！"),
]
