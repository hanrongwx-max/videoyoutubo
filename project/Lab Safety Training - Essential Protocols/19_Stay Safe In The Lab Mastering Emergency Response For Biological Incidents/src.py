# 19_Stay Safe In The Lab Mastering Emergency Response For Biological Incidents 原著版卡通剧本作者源
# 完全照原片：K1–K13（控制：警示带、清场、空气传播用生物安全柜；消毒与高压灭菌；针刺后肥皂和水清洗、就医、
# 记录、暴露后预防；美国疾控中心、职业安全卫生管理局与血源性病原体标准；锐器盒），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "实验室安全：生物事故的应急响应",
    "edition": "原著版",
    "points": {
        "K1": "生物暴露，必须马上行动",
        "K2": "溢洒第一步：控制",
        "K3": "警示、清场、防气溶胶",
        "K4": "目标：不让它扩散",
        "K5": "清理不偷工，消毒要彻底",
        "K6": "污染器材高压灭菌",
        "K7": "针刺暴露，立即处理",
        "K8": "肥皂流水马上冲洗",
        "K9": "就医、记录、正确治疗",
        "K10": "需要预防用药，别犹豫",
        "K11": "规定不是建议，必须照做",
        "K12": "针头进锐器盒",
        "K13": "按规范，护人人",
    },
    "avoid": ["Atlantic", "Atlantic Training", "OSHA", "Bloodborne Pathogen", "Bloodborne Pathogens Standard"],
}

SHOTS = [
# 开场
("开场", "欣欣站在贴有生物危害标志的实验室门外，向镜头招手",
 "The panda mascot stands outside a lab door marked with a biohazard warning sign and waves at the camera.",
 "接下来，讲生物安全事故。", "实验室安全：生物事故的应急响应"),
# 情景
("情景", "小研戴口罩护目镜蓝手套，拿起一支红盖采血管",
 "The female graduate student in a mask, goggles and blue gloves picks up a red-capped blood sample tube.",
 "小研正在处理血液样本。"),
("情景", "逆光下，戴手套的手往试管里倒液体",
 "Backlit, a gloved hand pours liquid into a test tube.",
 "这类工作，一旦出事要怎么应对？"),
# K1
("K1", "欣欣严肃地站在生物危害标志旁",
 "The panda mascot stands beside a biohazard warning sign with a serious face.",
 "涉及病原体或毒素，事态升级很快。", "生物暴露，必须马上行动"),
("K1", "秒表图标飞快转动",
 "A stopwatch icon with its hand spinning fast. No people.",
 "一旦暴露，没时间慢慢来，要快。"),
# K2
("K2", "台面上一摊洒出的样本，周围画出红圈",
 "A small spill of sample liquid on a lab bench with a red circle drawn around it. No people.",
 "发生溢洒，第一步是控制。", "溢洒第一步：控制"),
# K3
("K3", "穿白色防护服、戴口罩的老李拉起黄黑警示带",
 "The facility engineer in a white protective suit and respirator mask stretches yellow and black warning tape across a doorway.",
 "拉起生物危害警示带，", "警示、清场、防气溶胶"),
("K3", "两名穿防护服的人看平板，墙上生物危害标志；人员图标离开",
 "Two people in protective suits look at a tablet under a biohazard warning sign, while person pictograms leave along an arrow.",
 "不需要在场的人，都请出去。"),
("K3", "阿杰在生物安全柜里用移液器操作",
 "The young male student works with a pipette inside a biological safety cabinet.",
 "如果是空气传播，就用生物安全柜。"),
# K4
("K4", "红圈把危害关在里面，向外的箭头被挡住",
 "A red circle around a spill with outward arrows blocked at the edge. No people.",
 "目的很简单：关住它，不让它扩散。", "目标：不让它扩散"),
# K5
("K5", "红色生物危害脚踏垃圾桶；小研戴帽子口罩用喷壶擦安全柜内壁",
 "A red biohazard step-on waste bin; the female graduate student in a cap and mask sprays and wipes the inner walls of a safety cabinet.",
 "清理去污，不能偷工减料。", "清理不偷工，消毒要彻底"),
("K5", "空白标签的消毒剂瓶，病原图标被打叉",
 "A disinfectant bottle with a blank label next to a germ icon crossed out. No people.",
 "用合适的消毒剂，彻底消灭它。"),
# K6
("K6", "戴手套的手把器材架推入高压灭菌器",
 "Gloved hands push a rack of contaminated tools into an autoclave.",
 "受污染的器材，送去高压灭菌。", "污染器材高压灭菌"),
("K6", "手关上灭菌器门，指示灯亮绿",
 "A hand closes the autoclave door and the indicator lamp turns green. No people.",
 "彻底灭菌，不能半途而废。"),
# K7
("K7", "带血的注射器针头图标，旁边警示三角",
 "A used syringe needle icon with a drop of blood and a warning triangle. No people.",
 "人员暴露，比如被带血针头扎伤，", "针刺暴露，立即处理"),
("K7", "阿杰手指一缩，表情吃痛",
 "The young male student flinches and pulls back his finger with a pained look.",
 "立即处理至关重要。"),
# K8
("K8", "双手打肥皂，在水槽流水下冲洗",
 "Hands lathered with soap, then rinsed under running water at a lab sink.",
 "马上用肥皂和水清洗，别耽搁。", "肥皂流水马上冲洗"),
# K9
("K9", "诊室里，护士给阿杰的手臂采血，试管架上有采血管",
 "In a clinic, a nurse draws blood from the young male student's arm, a rack of sample tubes nearby.",
 "随后去就医，", "就医、记录、正确治疗"),
("K9", "穿实验服戴紫手套的小研在记录板上写",
 "The female graduate student in a lab coat and purple gloves writes on a blank clipboard.",
 "记录经过，确保得到正确治疗。"),
# K10
("K10", "诊室桌上空白处方单和药盒",
 "A blank prescription slip and a plain medicine box on a clinic desk with a red cross icon. No people.",
 "需要暴露后预防用药，别犹豫。", "需要预防用药，别犹豫"),
# K11
("K11", "小研用平板查看，墙上生物危害标志",
 "The female graduate student in a face shield checks a tablet at a computer under a biohazard warning sign.",
 "处理生物危害，有明确的规定。", "规定不是建议，必须照做"),
("K11", "三本空白规范手册，封面有星条旗图标",
 "Three blank guideline books with small stars-and-stripes flag icons on their covers. No people.",
 "美国疾控中心、职业安全卫生管理局，", "", ["疾控中心", "职业安全卫生", "血源性病原体"]),
("K11", "从控制到处置的流程箭头",
 "A process arrow linking icons from a barrier tape to a disinfectant bottle to a waste bin. No people.",
 "血源性病原体标准，从控制管到处置。"),
("K11", "建议的问号图标被划掉，换成感叹号",
 "A question mark icon labeled as a suggestion is crossed out and replaced by a bold exclamation mark. No people.",
 "这些不是建议，必须照做。"),
# K12
("K12", "一排带生物危害标志的红色桶",
 "A row of red waste bins marked with biohazard warning signs. No people.",
 "受污染的物品，要正确处置。", "针头进锐器盒"),
("K12", "红色托盘里堆着用过的针头和采血管，旁边锐器盒",
 "A red tray holding used needles and sample tubes, next to a rigid sharps container. No people.",
 "针头这类锐器，放进锐器盒。"),
# K13
("K13", "小研和王老师拿着平板和记录板交谈",
 "The female graduate student and the safety administrator talk while holding a tablet and a clipboard.",
 "坚持按规范做，保护每一个人。", "按规范，护人人"),
# 小结
("小结", "欣欣身旁浮现警示带、安全柜图标",
 "The panda mascot stands beside floating icons of a barrier tape and a biological safety cabinet.",
 "先控制：警示、清场、用安全柜。", "小结"),
("小结", "消毒剂和高压灭菌器图标",
 "Icons of a disinfectant bottle and an autoclave. No people.",
 "再消毒，器材高压灭菌。"),
("小结", "肥皂水龙头、医院、记录板、锐器盒图标",
 "Icons of soap and a tap, a hospital, a clipboard and a sharps container. No people.",
 "暴露：冲洗、就医、记录；锐器进盒。"),
# 结尾
("结尾", "欣欣在实验室门外挥手道别",
 "The panda mascot waves goodbye outside a lab door with a biohazard warning sign.",
 "快速应对，守护健康，下次见！"),
]
