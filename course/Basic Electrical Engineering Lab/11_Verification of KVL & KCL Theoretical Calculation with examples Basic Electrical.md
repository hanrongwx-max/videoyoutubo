# 11_Verification of KVL & KCL Theoretical Calculation with examples Basic Electrical

## 基本信息
| 项目 | 内容 |
|---|---|
| 剧集 | Basic Electrical Engineering Lab |
| 原标题 / 链接 | Verification of KVL & KCL Theoretical Calculation with examples Basic Electrical Engineering Lab VTU；https://youtu.be/iFedb0fc1w4 |
| 时长、分辨率 | 00:10:00（600.0 秒），1276×720 |
| 语言 | 英语（印度口音女声画外音；转写为 Whisper small.en，“14.14 ohm”为口误 / 识别错误，按板书应为 14.4 Ω；“V1 is power”= four；“I button”= info 按钮；“set a current 0.2 volt 2 amps”语义不清，已按上下文理解） |
| 类型 | 讲座录屏（幻灯片 + 手写批注 + 扫描的手写计算稿），无实拍，演示留到下一集 |
| 适用对象 | 工科一年级本科生，“电工基础 / 电工学实验”课程 |
| 与“实验室安全”主题的相关度 | 低：本片是基尔霍夫定律验证实验的器材、步骤和理论计算讲解；安全内容只有稳压电源旋钮初始位置一条注意事项；其余安全知识需审查补充 |

## 内容概要
本片是基尔霍夫电压定律（KVL）和电流定律（KCL）验证实验的上半部分：理论计算。讲者先提醒观众先看理论课视频，然后讲实验目的、器材（0–30 V/2 A 稳压直流电源 RPS、三只 12 V/10 W 直流灯、三只 0–1 A 磁电式电流表、三只 0–30 V 磁电式电压表，没有电压表可用万用表直流档）、注意事项（RPS 电压旋钮置最小、电流旋钮置最大）、电路（灯 1 串联在干路，灯 2、灯 3 并联；V1 为电源电压，V2 测灯 1，V3 测并联部分；I1、I2、I3 为三路电流）和六步实验步骤。接着讲理论值与实测值两套记录表，并用扫描的手写稿做一个 4 V 的算例：由灯的额定值求电阻 R = V²/P = 14.4 Ω，求等效电阻 21.6 Ω，总电流 0.185 A，用分流公式得 I2 = I3 = 0.0925 A，验证 I1 = I2 + I3；再由欧姆定律得 V2 = 2.664 V、V3 = 1.336 V，验证 V1 = V2 + V3。最后说明实测演示在下一集，并建议复习串并联、分压和分流公式。

## 知识点
- K1 先学理论再做实验：先弄懂 KVL、KCL 的理论讲解，再做电路验证（00:00–00:32）
- K2 实验目的：对给定的直流电路，从理论计算和实际测量两方面验证 KVL 和 KCL（00:32–00:45）
- K3 器材：稳压直流电源（RPS）、三只同规格直流灯、三只磁电式（MC）直流电流表、三只磁电式直流电压表；没有电压表时可用万用表并拨到直流档（00:45–01:30）
- K4 注意事项：接通前 RPS 的电压旋钮放在最小位置、电流旋钮放在最大位置，否则可能损坏电源（01:30–01:55）
- K5 电路：RPS 输出为 V1；灯 1 串在干路上，电流 I1，两端电压 V2；灯 2、灯 3 并联，电流 I2、I3，两端电压相同为 V3；三只灯额定值相同，便于计算电阻（01:55–02:55）
- K6 直流电表要标 MC 和正负极（02:20–02:40）
- K7 实验步骤：按图接线→合上 RPS 开关→在 RPS 上设定一个电压→记下电流表、电压表读数→换几个电压重复→断开电源并拔下插头（02:55–03:50）
- K8 组内分工：每位组员各取一个不同的电压读一组数（03:10–03:30，04:09–04:24）
- K9 先画好两套表：理论值和实测值；KVL 表记 V1、V2、V3 并验证 V1 = V2 + V3，KCL 表记 I1、I2、I3 并验证 I1 = I2 + I3（03:50–05:14，08:40–09:10）
- K10 计算第一步：由灯的额定功率和额定电压求电阻，R = V²/P（例：12 V、10 W 得 14.4 Ω），三灯相同（05:14–06:10）
- K11 计算第二步：等效电阻 Req = R1 + R2R3/(R2 + R3)（例：21.6 Ω）（06:10–06:40）
- K12 计算第三步：总电流 I1 = V1/Req（例：4 V 时 0.185 A），用分流公式求 I2 = I1·R3/(R2 + R3)、I3 = I1·R2/(R2 + R3)（各 0.0925 A），验证 I1 = I2 + I3（06:40–07:45）
- K13 计算第四步：V2 = I1·R1（2.664 V），V3 = V1 − V2（1.336 V），验证 V1 = V2 + V3（07:45–08:40）
- K14 先把理论值填进表里，下一集做实测演示；复习串联、并联电路和分压、分流公式（08:40–10:00）

## 讲解内容（逐段）
1. **00:00–00:32 开场（K1）**：片头标志和标题“Verification of KVL & KCL”。讲者请观众先看 KVL、KCL 理论讲解视频。原话：“first of all you please watch that video completely later on you can go ahead with practical circuit verification.”
2. **00:32–01:30 目的与器材（K2、K3）**：Aim 幻灯片；Apparatus Required：RPS 0–30 V、2 A 一台；DC 灯 12 V、10 W 三只；电流表 0–1 A MC 三只；电压表 0–30 V MC 三只。原话：“you can use a multimeter and set the multimeter into DC mode.”
3. **01:30–01:55 注意事项（K4）**：Procedure 幻灯片上的 Precautions 两条。原话：“otherwise there are chances for spoiling of your regulated DC power supply.”
4. **01:55–02:55 电路图（K5、K6）**：讲者圈出 RPS、三只灯的额定值、电流表 0–1 A，在电流表旁写 MC，说明灯 2、灯 3 并联电压相同。原话：“two lamps are connected in parallel therefore voltage across lamp 2 and lamp 3 are same.”
5. **02:55–03:50 步骤（K7、K8）**：六步步骤；电压可取 3、4、6、8、10 V，组员各取一个。原话：“switch off the supply okay and then remove the plug.”
6. **03:50–05:14 记录表（K9）**：Verification of KVL 表（理论 / 实测各一张，V1 列手写 3、4、6、8、10），Verification of KCL 表。原话：“kindly draw the table theoretical verification as well as practical verification.”
7. **05:14–06:10 灯电阻（K10）**：切到扫描手写稿 “Verification of KVL & KCL”：电路改画成 R1、R2、R3；Step 1：P = V²/R ⇒ R = 12²/10 = 14.4 Ω。原话：“first in the foremost I need to calculate the resistance of the lamp.”
8. **06:10–06:40 等效电阻（K11）**：Step 2：Req = 14.4 + 14.4×14.4/(14.4+14.4) = 21.6 Ω。
9. **06:40–07:45 KCL（K12）**：Step 3：I1 = 4/21.6 = 0.185 A（可选 4、6、8、10 V）；I2 = I3 = 0.185×14.4/28.8 = 0.0925 A；I1 = I2 + I3，KCL 得证。原话：“I can verify the relation I1 is equal to I2 plus I3.”
10. **07:45–08:40 KVL（K13）**：Step 4：V2 = I1×R1 = 0.185×14.4 = 2.664 V（欧姆定律）；V3 = V1 − V2 = 4 − 2.664 = 1.336 V；V1 = V2 + V3，KVL 得证。
11. **08:40–10:00 小结（K14）**：回到两套表，请先填理论值；“Demonstration”标题页，说明实测演示在下一集；建议复习串并联、分压分流。原话：“I am going to show the demonstration in the next session.”

## 画面文字（字符）
| 时间 | 文字 |
|---|---|
| 00:00–00:32 | Simplified EEE Studies 标志；Basic Electrical Engineering Laboratory；Verification of KVL & KCL；水印 www.BANDICAM.com（全片） |
| 00:32–00:45 | Aim：To verify Kirchhoff's Voltage Law (KVL) & Kirchhoff's Current Law (KCL) for the given circuit. |
| 00:45–01:30 | Apparatus Required：1 RPS (Regulated DC Power Supply) 0-30V, 2 A 1；2 DC Lamps 12V,10W 3；3 Ammeter 0-1A MC 3；4 Voltmeter 0-30V MC 3 |
| 01:30–01:55，03:00–04:00 | Procedure — Precautions: 1. Voltage control knob should be kept at minimum position. 2. Current control knob of RPS should be kept at maximum position. Procedure: 1. Circuit connections are made as per the circuit diagram. 2. Supply switch of RPS is closed 3. Set a value of voltage in RPS. 4. Note down the corresponding ammeter and Voltmeter readings. 5. Repeat the steps 3 & 4 for different values of voltages. 6. Switch off the Supply. |
| 01:55–03:00 | Circuit Diagram：12V,10W Lamp 1/2/3、0-1A、A1、I1、I2、I3、V1 V2 V3 0-30V、RPS、+ − 极性符号；手写圈注 |
| 04:00–05:14，08:40–09:10 | Verification of KVL：Theoretical Values for the Verification of KVL / Practical Values for the Verification of KVL — Sl.No / Voltage in Volts V1 V2 V3 / V1=V2+V3；手写 3、4、6、8、10（5 人）；Verification of KCL：Theoretical / Practical Values — Current in Amperes I1 I2 I3 / I1=I2+I3；一度弹出系统配色提示框 |
| 05:14–08:40 | 扫描手写稿（Scanned with CamScanner）：Verification of KVL & KCL 电路（R1 R2 R3、I1 I2 I3、V1 V2 V3）；Step 1 Calculation of R1, R2 and R3: power rating of the lamp = 10 W, voltage rating = 12 V, P = V²/R ⇒ R = 12²/10 = 144/10 = 14.4 Ω, R1 = R2 = R3 = R = 14.4 Ω；Step 2 Req = R1 + R2R3/(R2+R3) = 14.4 + 14.4×14.4/(14.4+14.4) = 21.6 Ω；Step 3 Verification of KCL: I1 = V1/Req = 4/21.6 = 0.185 A (chose V1 = 4V, 6V, 8V, 10V etc), I2 = I1×R3/(R2+R3) = 0.185×14.4/28.8 = 2.664/28.8 = 0.0925 A, I3 同理 = 0.0925 A, It is found that I1 = I2 + I3. Hence KCL for the given Circuit is verified.；Step 4 Verification of KVL: V2 = I1×R1 = 0.185×14.4 = 2.664 V (Ohm's Law), V3 = V1 − V2 = 4 − 2.664 = 1.336 V, It is found that V1 = V2+V3. Hence KVL for the given Circuit is verified. |
| 09:10–10:00 | Demonstration |

## 镜头说明
| 镜头 | 时间 | 画面内容 | 景别 / 运镜 | 同期讲解 |
|---|---|---|---|---|
| 1 | 00:00–00:32 | 片头标志与标题页 | 全屏幻灯片 | 欢迎；先看理论视频 |
| 2 | 00:32–05:14 | Aim、Apparatus Required、Procedure（含注意事项）、Circuit Diagram（手写圈注 RPS、灯额定值、MC）、Verification of KVL / KCL 表格 | 全屏录屏，手写批注 | 目的、器材、旋钮位置、电路、步骤、组员分工、两套表 |
| 3 | 05:14–08:40 | PDF 阅读器中的扫描手写计算稿，上下滚动 | 全屏录屏，滚动 | 灯电阻、等效电阻、总电流、分流、KCL、V2、V3、KVL |
| 4 | 08:40–10:00 | KVL、KCL 表格，随后“Demonstration”标题页 | 全屏幻灯片 | 先填理论值；下一集演示；复习串并联、分压分流 |

## 安全要点与原片的不足
- 原片只有一条与设备保护相关的注意事项（RPS 电压旋钮最小、电流旋钮最大），没有人身安全内容。
- “电流旋钮放最大”是本实验室的做法，目的是让电源不因限流而无法输出；但从保护电路和仪表的角度，更稳妥的做法是先按预估电流设好限流值（系列 05 已讲“限流设好，输出别短路”）。剧本照原片讲“电压旋钮先放最小”，电流旋钮写成“按老师要求设置”，在审查报告中说明。
- 灯的额定电压为 12 V，而 RPS 可输出到 30 V，原片未提示所加电压不得超过灯和电表的额定值（讲者举例最高 10 V）。
- 磁电式直流表有正负极，接反指针反偏、可能损坏，原片只在图中画了“+”号，没有讲。
- 原片未提示“先算后测”的用途：理论值可以用来预估电流、核对量程，实测值与理论值相差很大时应停下检查。
- 技术问题：灯丝电阻随温度变化很大，低电压下灯丝不热、电阻远小于按额定值算出的 14.4 Ω，所以实测电流会明显偏离理论值；原片未说明。V3 由 V1 − V2 求出，本身就用到了 KVL，作为“理论验证”是循环论证；剧本按原片步骤讲述，不加评论。转写中 “14.14 ohm” 为口误，以板书 14.4 Ω 为准。
- 画面中有频道名、录屏软件和扫描软件水印，剧本不使用。
