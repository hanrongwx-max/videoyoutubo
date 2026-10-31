# 08_Laser Cutter 6.5 Updates 原著版卡通剧本作者源
# 完全照原片：规程更新通知，K1–K6（净化器从三格改为四格风量、挤出型亚克力气味大不再允许、只用标明浇铸的亚克力、
# 签到时出示证明、商家统一说明也可），无补充知识点
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": "激光切割机6.5：更新",
    "edition": "原著版",
    "points": {
        "K1": "规程会更新，以最新为准",
        "K2": "净化器风量改为四格",
        "K3": "亚克力只用浇铸型",
        "K4": "购买时找“浇铸”字样",
        "K5": "签到时出示证明",
        "K6": "有疑问问工作人员",
    },
    "avoid": ["xTool", "X-Tool", "Bozeman", "Public Library", "BPL", "Amazon", "Makerstock", "Glowforge",
              "Proofgrade", "David"],
}

SHOTS = [
# 开场
("开场", "欣欣站在激光切割机旁，举着一张空白通知单",
 "The panda mascot stands beside a closed desktop laser cutter holding up a blank notice sheet and waves at the camera.",
 "激光切割机的规程，有了新变化。", "激光切割机：规程更新须知"),
("开场", "风扇图标和一块透明板图标并排",
 "Two icons side by side: an air purifier fan and a clear plastic sheet. No people.",
 "一条关于净化器，一条关于亚克力。", "", ["净化器风量", "亚克力材料"]),
# 情景
("情景", "阿杰按旧习惯把净化器调到三格，墙上贴着新通知",
 "The young male student sets the air purifier to three lights out of habit, while a new blank notice is posted on the wall above it.",
 "阿杰还按老办法开净化器。"),
("情景", "小研指着墙上的新通知，阿杰挠头",
 "The female graduate student points at the new blank notice on the wall; the young male student scratches his head.",
 "小研提醒他：规程已经更新了。"),
# K1
("K1", "一本旧规程和一本新规程，新的上面有星标",
 "Two blank procedure booklets side by side, the newer one marked with a star icon. No people.",
 "培训视频拍完后，规程还会调整。", "规程会更新，以最新为准"),
("K1", "净化器上贴着更新后的空白标识",
 "A fresh blank sign with simple fan icons attached to the front of the air purifier. No people.",
 "一切以最新通知和现场标识为准。"),
# K2
("K2", "净化器顶上的指示灯从三格亮到四格",
 "The indicator lights on top of the air purifier go from three lit lights to four lit lights. No people.",
 "净化器风量，从三格改成四格。", "净化器风量改为四格", ["四格，不是三格"]),
("K2", "阿杰按风量键，数着亮起的灯",
 "The young male student taps the fan button on the air purifier and counts the lit indicator lights.",
 "要确认亮的是四个蓝灯。"),
("K2", "净化器正面的标识换成新的",
 "An old blank sign on the air purifier is replaced by a new blank sign with four small fan icons. No people.",
 "净化器上的标识，也已经换新了。"),
("K2", "烟雾被更强的气流吸进管道",
 "Smoke from the laser cutter is pulled more strongly through the duct into the air purifier, shown with bold airflow arrows. No people.",
 "风量大一点，烟尘抽得更干净。"),
# K3
("K3", "两块透明板图标，一块标着挤出、一块标着浇铸",
 "Two clear plastic sheet icons side by side, one with a roller pictogram and one with a mold pictogram. No people.",
 "亚克力分挤出型和浇铸型两种。", "亚克力只用浇铸型", ["挤出型", "浇铸型"]),
("K3", "挤出型板冒出浓重气味线，被红叉划掉",
 "The roller-type sheet icon gives off heavy wavy odor lines and is crossed out with a red X. No people.",
 "挤出型加工时气味太大，不再允许。"),
("K3", "浇铸型板打绿勾",
 "The mold-type sheet icon with a green check mark. No people.",
 "以后只用标明浇铸的亚克力。"),
# K4
("K4", "小研拿着一块包装好的透明板，查看空白标签",
 "The female graduate student holds a wrapped clear plastic sheet and checks its blank label closely.",
 "买的时候，先找浇铸这两个字。", "购买时找“浇铸”字样"),
("K4", "空白商品页上，标签、标题、描述、参数四处被放大镜依次扫过",
 "A blank product web page; a magnifying glass moves over four areas in turn: the label, the title, the description and the specifications table. No people.",
 "标签、标题、描述、规格参数都看看。", "", ["标签", "标题", "描述", "规格参数"]),
("K4", "其中一处亮起黄色高亮，打勾",
 "One spot on the blank page lights up with a yellow highlight and a green check. No people.",
 "找到明确写着浇铸，才算数。"),
# K5
("K5", "阿杰在服务台向小研出示手机上的空白商品页",
 "At the front desk, the young male student shows the female graduate student a blank product page on his phone next to his clear sheet.",
 "签到时，要能出示这份证明。", "签到时出示证明"),
("K5", "商家网站上的统一说明被高亮，打勾",
 "A blank store web page with one general statement highlighted in yellow and a green check. No people.",
 "商家声明只卖浇铸型的，也可以。"),
("K5", "说不清来历的透明板被放到一边",
 "A clear plastic sheet with no label and a question mark is set aside on a shelf with a red X. No people.",
 "拿不出证明，这块板就不能用。"),
# K6
("K6", "小研在服务台后微笑招手",
 "The female graduate student smiles and waves from behind the front desk.",
 "有疑问，随时问服务台工作人员。", "有疑问问工作人员"),
# 小结
("小结", "欣欣身旁浮现净化器四格灯图标",
 "The panda mascot stands beside a floating icon of an air purifier with four lit blue lights.",
 "净化器风量，开到四格。", "小结"),
("小结", "浇铸型板打勾、挤出型板打叉",
 "Icons of a mold-type sheet with a green check and a roller-type sheet with a red X. No people.",
 "亚克力只用浇铸型，挤出型不行。"),
("小结", "放大镜、手机商品页、服务台图标",
 "Icons of a magnifying glass, a phone with a blank product page and a front desk. No people.",
 "找准浇铸字样，签到出示证明。"),
# 结尾
("结尾", "欣欣在关好的切割机旁挥手道别",
 "The panda mascot waves goodbye beside a tidy closed desktop laser cutter and the air purifier.",
 "跟上新规程，下次见！"),
]
