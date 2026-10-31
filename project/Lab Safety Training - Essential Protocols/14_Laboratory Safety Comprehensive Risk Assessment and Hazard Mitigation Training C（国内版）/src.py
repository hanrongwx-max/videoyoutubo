# 14_Laboratory Safety Comprehensive Risk Assessment and Hazard Mitigation Training C 卡通剧本作者源
# 原片讲电气危害的风险评估步骤、管理控制和电气安全规范：保留全部知识点 K1–K12，审查补充 S1–S4
# （书面评估与审批、条件变化要复评、评估结果告知到人、自制改装用电装置先评估）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "用电风险，先评估再动手",
    "points": {
        "K1": "电气风险可以按步骤评估",
        "K2": "风险评估五步",
        "K3": "管理措施比单靠防护有效",
        "K4": "管理措施一：培训",
        "K5": "管理措施二：警示标识",
        "K6": "管理措施三：操作规程",
        "K7": "规定要执行，不能放一边",
        "K8": "接触电气设备的人都要培训",
        "K9": "电气测试不戴金属饰物",
        "K10": "规范管设计，也管干活的人",
        "K11": "行业标准推动了规范",
        "K12": "测试按标准，电弧要评估",
        "S1": "评估要写下来、经审批",
        "S2": "情况变了，重新评估",
        "S3": "评估结果人人知晓",
        "S4": "自制改装用电装置先评估",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "NFPA", "IEEE", "Subpart S", "CFR"],
}

SHOTS = [
# 开场
("开场", "欣欣站在实验台旁，手里拿着一张空白评估表，向镜头招手",
 "The panda mascot stands by a lab bench holding a blank assessment sheet and waves at the camera.",
 "这一课讲：用电风险，先评估再动手。", "用电风险，先评估再动手"),
# 情景
("情景", "阿杰抱来一台旧的大功率加热设备，准备接上插线板",
 "The young male student carries an old high-power heating device to the bench and reaches for a power strip.",
 "阿杰找来一台旧加热设备，想马上用。"),
("情景", "老周拦住他，递过一张空白评估表",
 "The older man stops him and hands him a blank risk assessment form.",
 "老周说：先把风险评估做了。"),
("情景", "阿杰挠头，头顶冒出问号",
 "The young male student scratches his head with a question mark above him, holding the blank form.",
 "评估？从哪儿下手呢？"),
# K1
("K1", "放大镜照着设备、电线和插座",
 "A magnifying glass icon moving over an instrument, its power cord and a wall outlet. No people.",
 "用电的风险，可以按步骤评估。", "电气风险可以按步骤评估"),
("K1", "危害图标和天平图标",
 "A warning triangle icon next to a balance scale icon weighing likelihood and harm. No people.",
 "找出潜在危害，估计可能发生的风险。"),
# K2
("K2", "阶梯第一级：放大镜找到闪电图标",
 "Step one on a staircase diagram: a magnifying glass finding a lightning bolt icon. No people.",
 "第一步，找出这项工作有哪些电气危害。", "风险评估五步", ["1 找危害"]),
("K2", "阶梯第二级：空白任务卡和扳手",
 "Step two on the staircase: a blank task card with a wrench icon. No people.",
 "第二步，说清要做的是什么电气工作。", "", ["2 明确工作"]),
("K2", "阶梯第三级：从轻到重的伤害刻度",
 "Step three on the staircase: a severity scale from a small bandage to a red cross. No people.",
 "第三步，估计一旦出事伤得多重。", "", ["3 估严重度"]),
("K2", "阶梯第四级：断线、老化、误操作图标指向触电",
 "Step four on the staircase: icons of a broken wire, an aged plug and a wrong switch, all pointing to a shock symbol. No people.",
 "第四步，想想哪些故障会让人触电。", "", ["4 找故障方式"]),
("K2", "阶梯第五级：风险表红色区域加上盾牌后变绿",
 "Step five on the staircase: a risk gauge in the red zone turns green after a shield icon is added. No people.",
 "第五步，风险太高，就加措施再评估。", "", ["5 加措施"]),
# K3
("K3", "倒三角控制层级图，管理措施一层亮起",
 "An inverted triangle of five control levels with the administrative controls level glowing, above the protective equipment level. No people.",
 "控制措施有层级，管理措施比单靠防护有效。", "管理措施比单靠防护有效", ["消除", "替代", "工程控制", "管理措施", "个人防护"]),
# K4
("K4", "王老师给大家讲用电安全，大家记笔记",
 "The safety administrator teaches electrical safety to the young male student and the female graduate student, who take notes.",
 "一是培训：人人懂危害，会安全操作。", "管理措施一：培训"),
# K5
("K5", "配电间门口的当心触电标志和仅限授权人员图标",
 "An electrical hazard warning sign and an authorized-personnel-only icon on an electrical room door. No people.",
 "二是标识：提醒危险，提示怎么做。", "管理措施二：警示标识"),
# K6
("K6", "仪器旁贴着空白的操作规程卡",
 "A blank step-by-step procedure card posted beside a lab instrument. No people.",
 "三是操作规程，最重要。", "管理措施三：操作规程"),
("K6", "小研对照规程卡一步步操作",
 "The female graduate student follows the posted blank procedure card step by step at the instrument.",
 "一步一步写清楚，谁来做都一样安全。"),
# K7
("K7", "规范文本被丢在角落积灰，打叉",
 "A blank rule booklet left dusty in a corner, crossed out with a red X. No people.",
 "规定写了不执行，等于没有。", "规定要执行，不能放一边"),
# K8
("K8", "装、修、维护、靠近四个图标都连到培训证书",
 "Four icons for installing, repairing, maintaining and working nearby, each linked to a blank training certificate. No people.",
 "安装、维修、维护或在旁边工作，都要培训。", "接触电气设备的人都要培训"),
# K9
("K9", "戒指、手表、金属手链图标被打叉",
 "Icons of a ring, a wristwatch and a metal bracelet crossed out. No people.",
 "电气测试时，不戴戒指手表等金属饰物。", "电气测试不戴金属饰物"),
# K10
("K10", "图纸上的电路和戴安全帽的电工图标",
 "A blueprint with circuit lines next to an electrician icon with a hard hat. No people.",
 "规范既管系统设计，也管装修人员。", "规范管设计，也管干活的人"),
# K11
("K11", "行业标准书推动规范文本",
 "A blank industry standard book with an arrow pushing into a blank regulation booklet. No people.",
 "行业标准走在前面，推动了规范完善。", "行业标准推动了规范", ["以现行标准为准"]),
# K12
("K12", "老李用万用表按规程测量，旁边电弧图标被盾牌挡住",
 "The facility engineer measures with a multimeter following a blank procedure card; an arc flash icon is blocked by a shield beside him.",
 "电气测试按标准做，事先评估电弧风险。", "测试按标准，电弧要评估"),
# S1
("S1", "阿杰在空白评估表上填写",
 "The young male student fills in a blank risk assessment form at a desk.",
 "评估不能只在脑子里，要写成书面。", "评估要写下来、经审批"),
("S1", "老周签字，王老师盖章",
 "The older man signs the blank form and the safety administrator stamps it.",
 "实验室负责人审核，高风险报学院审批。"),
# S2
("S2", "新设备、新人、方案改动、事故四个图标连到循环箭头",
 "Four icons, a new instrument, a new person, an edited plan and a warning flash, each linked to a circular arrow. No people.",
 "换设备、来新人、改方案、出事后，", "情况变了，重新评估", ["新设备", "新人", "改方案", "出事后"]),
("S2", "评估表上旧日期划掉，写上新日期",
 "A blank assessment form with an old date crossed out and a new blank date box. No people.",
 "都要重新评估，及时更新。"),
# S3
("S3", "小研向阿杰讲解评估表，阿杰签字确认",
 "The female graduate student explains the blank assessment form to the young male student, who signs to confirm.",
 "评估结果讲给每个参与的人，签字确认。", "评估结果人人知晓"),
# S4
("S4", "自制加热装置和改装电源图标",
 "Icons of a homemade heating setup and a modified power supply with exposed wiring, under a question mark. No people.",
 "自制或改装的用电装置，风险最难估。", "自制改装用电装置先评估"),
("S4", "老李检查阿杰的旧设备，贴上空白合格标签",
 "The facility engineer inspects the young male student's old heating device and attaches a blank passed label.",
 "先评估、经检查批准，再通电使用。"),
# 小结
("小结", "欣欣身旁浮现五级台阶图标",
 "The panda mascot stands beside a five-step staircase icon.",
 "五步评估：找危害，估风险，加措施。", "小结"),
("小结", "培训、标识、规程三个打勾图标",
 "Three icons with green checks: a classroom, a warning sign and a procedure card. No people.",
 "培训、标识、规程，规定要执行。"),
("小结", "评估表、审批章、循环箭头图标",
 "Icons of a blank assessment form, an approval stamp and a circular arrow. No people.",
 "写下来、经审批、常更新、人人知。"),
# 结尾
("结尾", "欣欣举着盖好章的评估表挥手道别",
 "The panda mascot holds up a stamped blank assessment form and waves goodbye.",
 "先评估再动手，平安实验，下次见！"),
]
