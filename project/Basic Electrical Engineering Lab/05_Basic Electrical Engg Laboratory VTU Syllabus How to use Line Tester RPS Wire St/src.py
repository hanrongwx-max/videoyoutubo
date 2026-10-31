# 05_Basic Electrical Engg Laboratory VTU Syllabus How to use Line Tester RPS Wire St 卡通剧本作者源
# 原著版：完全照原片（试电笔结构与原理、螺丝刀、尖嘴钳、剥线钳、斜口钳、压线钳、双通道直流稳压电源），K1–K19，
# 不加补充知识点、不做本土化和更正（保留“氖泡不亮表示没电”“人体对地电容所以不会触电”“限流旋钮始终放最大”、铭牌 0–30 V）
# 镜头：(知识点, 中文画面, 英文画面, 旁白[, 顶部文字[, [图示文字...]]])；每镜 5 秒，旁白不超过 20 字

META = {
    "title": '试电笔、稳压电源、剥线钳与螺丝刀的使用',
    "edition": "原著版",
    "points": {
        'K1': '本课内容',
        'K2': '试电笔：查有没有电',
        'K3': '试电笔的结构',
        'K4': '试电笔的原理',
        'K5': '人体与大地的电容',
        'K6': '试电笔品种多',
        'K7': '螺丝刀',
        'K8': '布线离不开螺丝刀',
        'K9': '尖嘴钳',
        'K10': '剥线用剥线钳',
        'K11': '斜口钳',
        'K12': '压线钳',
        'K13': '稳压电源：开关和指示灯',
        'K14': '两个通道',
        'K15': '红正黑负',
        'K16': '调电压、设限流',
        'K17': '显示屏和铭牌',
        'K18': '直流实验要用它',
        'K19': '本课回顾',
    },
    "avoid": ['VTU', 'Visvesvaraya', 'Simplified EEE Studies', 'Simplified EEE', 'Bosch', 'Uday', 'rupees'],
}

SHOTS = [
# 开场
('开场', '欣欣站在工具墙前，墙上挂着螺丝刀、试电笔、钳子，旁边一台双通道直流电源，向镜头招手', 'The panda mascot stands in front of a tool wall with screwdrivers, a voltage tester pen and pliers, next to a dual-channel DC power supply, waving at the camera.', '这一课认识电工工具和直流稳压电源。', '电工工具与直流稳压电源'),
('开场', '试电笔、螺丝刀、钳子、直流电源四个图标', 'Four icons in a row: a voltage tester pen, a screwdriver, a pair of pliers and a DC power supply with blank displays. No people.', '试电笔、螺丝刀、钳子、电源。', '', ['试电笔', '螺丝刀', '钳子', '稳压电源']),
# 情景
('情景', '阿杰对着工具墙上的试电笔、钳子发愣', 'The young male student stares at a tool wall with a voltage tester screwdriver and several pliers, puzzled.', '阿杰看着一墙工具，叫不出名字。'),
('情景', '阿杰盯着双通道电源面板上的一排旋钮', 'The young male student stares at the row of knobs on a dual-channel DC power supply panel.', '电源上这么多旋钮，又该怎么调？'),
('情景', '小研拿起一支试电笔递给他', 'The female graduate student picks up a voltage tester screwdriver and hands it to him.', '小研说：一件一件认，很快就会用。'),
('情景', '欣欣在空白白板前竖起手指', 'The panda mascot stands in front of a blank whiteboard and raises one finger.', '先讲工具，再讲稳压电源。'),
# K1
('K1', '欣欣依次指向工具和电源', 'The panda mascot points in turn at the hand tools and the power supply.', '螺丝刀、试电笔、钳子和稳压电源。', '本课内容'),
# K2
('K2', '试电笔笔尖接触插座的相线孔，氖泡发光', 'The tip of a voltage tester screwdriver touches the live slot of a wall socket and its neon bulb glows. No people.', '试电笔用来检查导体有没有电。', '试电笔：查有没有电'),
('K2', '氖泡发光配闪电符号，不发光配一个空圈', 'Two icons: a glowing neon bulb with a lightning symbol, and an unlit neon bulb with an empty circle. No people.', '氖泡亮，说明带电；不亮，就是没电。', '', ['亮：有电', '不亮：没电']),
# K3
('K3', '试电笔剖面：笔尖金属杆、电阻、氖泡、弹簧、尾部金属', 'A cutaway icon of a voltage tester pen showing the metal tip, a resistor, a neon lamp, a spring and the metal end cap. No people.', '里面有电阻、氖泡和弹簧。', '试电笔的结构', ['笔尖', '电阻', '氖泡', '弹簧', '尾部金属']),
# K4
('K4', '手指按住尾部金属，笔尖接触导体', 'A hand holding a tester pen with a finger on the metal end cap while the tip touches a conductor. No people.', '手按尾部金属，笔尖接触导体。', '试电笔的原理'),
('K4', '电流箭头从笔尖经电阻、氖泡、人体流入大地', 'An icon of a tiny current arrow flowing from the conductor through the resistor, the neon lamp and a person pictogram to the ground. No people.', '电流经电阻、氖泡和人体流入大地。'),
('K4', '电压条大部分落在电阻上', 'A voltage bar divided into sections, the biggest section across the resistor icon. No people.', '大电阻分走大部分电压，电流极小。'),
# K5
('K5', '人体与大地之间画出电容符号', 'An icon of a person standing on the ground with a capacitor symbol drawn between the body and the earth. Flat icon style.', '人体和大地之间的电容，也构成回路。', '人体与大地的电容'),
('K5', '欣欣摊开双手微笑', 'The panda mascot spreads her paws and smiles.', '所以，用试电笔不会触电。'),
# K6
('K6', '几种不同样式的试电笔排成一排，旁边钱币图标高低不同', 'Several voltage testers of different styles in a row, with coin stacks of different heights beside them. No people.', '试电笔品种很多，价格相差也大。', '试电笔品种多'),
# K7
('K7', '一字和十字螺丝刀，手柄是绝缘材料', 'A flat-head and a cross-head screwdriver with insulated handles. No people.', '螺丝刀用来拧紧、松开螺钉。', '螺丝刀'),
('K7', '螺丝刀标出刀头、杆和手柄', 'A screwdriver icon with its tip, shaft and handle highlighted. No people.', '刀头卡住螺钉，转动手柄施力。', '', ['刀头', '杆', '绝缘手柄']),
# K8
('K8', '老李用螺丝刀把开关面板固定在木布线板上', 'The facility engineer uses a screwdriver to fix a switch plate onto a wooden wiring board.', '装家用布线板，离不开螺丝刀。', '布线离不开螺丝刀'),
# K9
('K9', '尖嘴钳夹住导线头弯成小圈', 'Needle-nose pliers gripping the end of a wire and bending it into a small loop. No people.', '尖嘴钳，能夹、能弯、能剪。', '尖嘴钳'),
# K10
('K10', '尖嘴钳夹住导线绝缘皮', 'Long-nose pliers gripping the insulation of a wire end. No people.', '尖嘴钳也能剥绝缘皮。', '剥线用剥线钳'),
('K10', '剥线钳剥下导线绝缘皮，打绿勾', 'Wire strippers removing insulation from a wire end, with a green check. No people.', '不过剥线，最好用剥线钳。'),
# K11
('K11', '斜口钳剪断一根铜线', 'Diagonal side cutters snipping a disconnected copper wire. No people.', '斜口钳，专门用来剪线。', '斜口钳'),
('K11', '铜线、黄铜线、铁丝三个图标', 'Icons of copper wire, brass wire and iron wire, each with a cut mark. No people.', '铜线、铁丝都能剪断。'),
# K12
('K12', '压线钳把端子压在导线头上', 'A crimping tool pressing a metal terminal onto the end of a wire. No people.', '压线钳把端子压紧在导线上。', '压线钳'),
('K12', '压好的端子打绿勾', 'A finished crimped terminal on a wire with a green check. No people.', '压接牢固，接头才不松不发热。'),
# K13
('K13', '双通道直流稳压电源面板：电源开关和指示灯', 'The front panel of a dual-channel DC regulated power supply with a power switch and an indicator lamp highlighted, displays blank. No people.', '稳压电源：先认电源开关和指示灯。', '稳压电源：开关和指示灯'),
('K13', '开关拨上，指示灯亮', 'The power switch flipped up and the indicator lamp lighting up. No people.', '开机后，指示灯亮起。'),
# K14
('K14', '面板左右两半分别高亮', 'The left half and right half of the power supply panel highlighted in turn. No people.', '它有两个通道，可以单独使用。', '两个通道', ['通道1', '通道2']),
# K15
('K15', '输出端一红一黑两个接线柱', 'A red and a black output terminal on the power supply panel. No people.', '输出端红色是正极，黑色是负极。', '红正黑负', ['红 +', '黑 −']),
('K15', '小研对照电路图把红线接到正极', 'The female graduate student connects a red lead to the positive terminal, checking a blank circuit diagram.', '直流接线，正负极要分清。'),
# K16
('K16', '电压和电流显示切换开关', 'A display selector switch for voltage or current on the power supply panel. No people.', '显示屏可切换看电压或电流。', '调电压、设限流'),
('K16', '粗调和细调两个电压旋钮', 'Coarse and fine voltage knobs highlighted on the panel. No people.', '粗调、细调旋钮配合设电压。', '', ['粗调', '细调']),
('K16', '限流旋钮被高亮，旁边是电流上限图标', 'The current limit knob highlighted, with a current ceiling icon beside it. No people.', '限流旋钮，设定输出电流的上限。'),
('K16', '限流旋钮被拧到最大位置', 'The current limit knob turned all the way to its maximum position. No people.', '讲解里说：限流旋钮始终放在最大。', '', ['限流：最大']),
# K17
('K17', '数字显示屏和底部空白铭牌', 'The digital display and a blank nameplate at the bottom of the power supply. No people.', '看显示屏读数，看铭牌的输出范围。', '显示屏和铭牌', ['0–30 V']),
# K18
('K18', '稳压电源接到一个直流电阻电路板上', 'The power supply connected to a DC resistor network board on a bench. No people.', '做直流电路实验，就用它供电。', '直流实验要用它'),
# K19
('K19', '工具和电源图标依次亮起', 'The tool icons and the power supply icon light up one by one. No people.', '这些工具，各专业都用得上。', '本课回顾'),
# 小结
('小结', '试电笔、螺丝刀、钳子图标', 'Icons of a voltage tester, a screwdriver and several pliers. No people.', '试电笔查电，螺丝刀拧，钳子夹剪压。', '小结'),
('小结', '稳压电源面板，旋钮和红黑端子高亮', 'A power supply panel with its knobs and red and black terminals highlighted. No people.', '稳压电源：红正黑负，调压设限流。'),
# 结尾
('结尾', '欣欣把工具一件件挂回工具墙，挥手道别', 'The panda mascot hangs the tools back on the tool wall one by one and waves goodbye.', '认识了工具和电源，下次见！'),
]
