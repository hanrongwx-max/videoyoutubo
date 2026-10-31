# 17_Three Voltmeter Method Viva Voce Questions and answers Basic Electrical Engineer

## 基本信息
| 项目 | 内容 |
|---|---|
| 剧集 | Basic Electrical Engineering Lab |
| 原标题 / 链接 | Three Voltmeter Method Viva Voce Questions and answers Basic Electrical  Engineering Laboratory VTU；https://youtu.be/OsWkasB_CKU |
| 时长、分辨率 | 00:09:15（555.5 秒），1280×720 |
| 语言 | 英语（印度口音男声，右上角有讲者小窗；转写为 Whisper small.en，术语识别错误较多：“even choke coil”= given choke coil，“Viva woes / YWAS”= viva voce，“positive components”= passive components，“triad”= TRIAC，“gait”= gate，“2 pi O / in terms of O”= 2πf / ohm，“easy electrical”= EEE，已按上下文和板书更正） |
| 类型 | 讲座录屏（实验口试问答：幻灯片 + 讲者手写板书，无实拍操作） |
| 适用对象 | 工科一年级本科生，“电工基础实验”课程中“三电压表法测扼流线圈电阻和电感”实验的口试复习 |
| 与“实验室安全”主题的相关度 | 低：本片是实验原理的口试问答（感抗、阻抗、仪表选择、容抗、TRIAC），全片没有安全内容；仅“交流电路用动铁式仪表、不要用动圈式仪表”与正确使用仪表有关。安全知识需审查补充 |

## 内容概要
本片是电工基础实验系列的口试（viva voce）复习课，对应实验“用三电压表法测量扼流线圈的电感和电阻”（幻灯片标为 Experiment 4）。讲者在一张“Important Questions”幻灯片上列出 6 个问题，边讲边手写公式：三电压表法是什么、感抗的定义与公式和单位、阻抗的含义与 RLC 阻抗公式、动铁式与动圈式仪表的区别、三电压表法中扼流线圈阻抗的算法、感抗与电源频率的关系。随后在“Thank you for listening!”页面上补充几道可能被问到的题：频率与角频率的单位、容抗公式及其与频率的反比关系（画出曲线）、容抗单位，最后介绍扼流线圈的用途以及现在常用的电力电子器件 TRIAC（三端、双向、用于交流调压）。讲者强调口试不必展开，记住公式和概念、简明作答即可。

## 知识点
- K1 三电压表法的用途：测量未知扼流线圈（电感线圈）的电阻 R 和电感 L（00:00–00:55）
- K2 感抗：电感在交流电路中对电流的阻碍作用，符号 XL，XL = ωL = 2πfL，单位欧姆（00:55–01:58）
- K3 电感的单位是亨利（H）（01:58–02:05）
- K4 阻抗：电阻、电感、电容等无源元件在交流电路中对电流的总阻碍，只用于交流电路，符号 Z，单位欧姆；RLC 串联电路 Z = √(R² + (XL − XC)²)（02:05–03:15）
- K5 动铁式（MI）与动圈式（MC）仪表：讲者的说法是交流测量选动铁式、直流测量选动圈式，不要用动圈式仪表测交流（03:15–04:00）
- K6 扼流线圈阻抗的算法：三电压表法中 Z = V3 / I（V3 为第三只电压表读数，I 为电路电流）；RL 电路的一般公式 Z = √(R² + XL²)（04:00–04:55）
- K7 感抗与电源频率成正比：频率越高，感抗越大（04:55–05:28）
- K8 口试技巧：记住公式和概念，记在笔记本上常复习，回答简明扼要（05:28–06:09）
- K9 单位：频率单位赫兹（Hz），角频率 ω 的单位弧度每秒（rad/s）（06:09–06:30）
- K10 容抗：电容在交流电路中对电流的阻碍，XC = 1/(ωC) = 1/(2πfC)，单位欧姆（06:30–06:50，07:12–07:25）
- K11 容抗与电源频率成反比，XC–f 曲线呈双曲线形，可能被要求画出（06:50–07:12）
- K12 扼流线圈的应用与 TRIAC：扼流线圈是电感器，过去用于调压等场合，现在很多被电力电子器件 TRIAC（交流双向晶闸管）构成的电子装置替代；TRIAC 有 MT1、MT2、G 三个端子，双向导通，主要用于交流调压；电气、电子类专业高年级会深入学习（07:25–08:44）
- K13 结束：有问题可以提出，祝考试顺利（08:44–09:15）

## 讲解内容（逐段）
1. **00:00–00:24 开场（K1）**：标题页“Basic Electrical Engineering Laboratory / Important Viva-voce Question & Answers / Experiment 4: Measurement of Inductance and Resistance of Choke Coil”，配实验台、仪表、导线拼图和闪电警示三角。原话：“In this session, I am going to discuss important Viva question from the experiment namely measurement of inductance and resistance of a given choke coil.”
2. **00:24–00:55 问题 1（K1）**：切到“Important Questions”幻灯片，打勾第 1 题，旁写 “R and L”。原话：“3 voltmeter method is used to measure the unknown resistance and inductance of given choke coil.”
3. **00:55–02:05 问题 2（K2、K3）**：画交流电源接电感的小电路，写 XL = Lω = L×2πf，“unit = ohm”。原话：“a certain resistance which is going to offer by the inductor. That is called inductive reactance.” 补充电感单位亨利。
4. **02:05–03:15 问题 3（K4）**：写 “→ Z unit = ohm”，右上角写 Z = √(R² + (XL − XC)²)。讲阻抗只适用于交流电路，是电阻、电感、电容等无源元件对电流的阻碍。原话：“Impedance is applicable only for AC circuit.”
5. **03:15–04:00 问题 4（K5）**：在 MI、MC 下写 “moving iron”“moving coil”，标 AC、DC。原话：“while selecting the measurement devices for AC circuit, kindly use moving iron. Don't use moving coil for AC circuit.”
6. **04:00–04:55 问题 5（K6）**：写 “3 voltmeter method → Z = V3/I”，方框写 Z = √(R² + XL²)，请观众参考实验手册中的公式。
7. **04:55–05:28 问题 6（K7）**：写 XL = Lω = L×2πf，XL ∝ f↑。原话：“as the supply frequency is high, definitely inductive reactance is also high.”
8. **05:28–06:09 口试建议（K8）**：要求记下要点、公式和概念；口试不必展开，“Whatever you know, try to convince the examiner.” 板书逐渐擦除。
9. **06:09–06:30 补充：单位（K9）**：“Thank you for listening!”页上写 f → Hz，ω → rad/sec。
10. **06:30–07:25 补充：容抗（K10、K11）**：写 XC = 1/(Cω) = 1/(C×2πf)，画 XC–f 下降曲线，XC ∝ 1/f，“XC → unit = ohm”。原话：“Capacitive reactance is inversely proportional to the supply frequency.”
11. **07:25–08:44 补充：扼流线圈与 TRIAC（K12）**：写 “TRIAC ↓ PE”，画 TRIAC 符号，标 MT1、MT2、G。讲过去使用传统扼流线圈，现在被电力电子器件 TRIAC 替代；TRIAC 是双向器件，用于交流调压，电气电子类专业高年级会学。原话：“it is a bidirectional device… mainly for AC voltage control.”
12. **08:44–09:15 结束（K13）**：总结本节题目，请观众在评论区提问，祝考试顺利。

## 画面文字（字符）
| 时间 | 文字 |
|---|---|
| 00:00–00:24 | Basic Electrical Engineering Laboratory；Important Viva-voce Question & Answers；Experiment 4: Measurement of Inductance and Resistance of Choke Coil；闪电警示三角；页脚 09-10-2022、频道名水印、页码 42 |
| 00:24–06:09 | Important Questions：1. What is three voltmeter method? 2. What is Inductive Reactance? 3. What do you mean by Impedance? 4. What are the difference between MI and MC instruments? 5. How do you calculate the Impedance of choke coil? 6. What is the relation between supply frequency and the Inductive Reactance?；页码 43 |
| 00:24–06:09（手写） | R and L；交流电源接线圈小图；XL = Lω = L×2πf；unit = ohm；→ Z unit = ohm；Z = √(R² + (XL − XC)²)；moving Iron（AC）、Moving Coil（MC − DC）；3 voltmeter method，Z = V3/I；Z = √(R² + XL²)；XL = Lω = L×2πf，XL ∝ f↑ |
| 06:09–09:15 | Thank you for listening!；页码 44；手写：f → Hz；ω → rad/sec；XC = 1/(Cω) = 1/(C×2πf)；XC–f 曲线；XC ∝ 1/f；XC → unit = ohm；TRIAC ↓ PE；TRIAC 符号，MT1、MT2、G |
| 全程 | 右上角讲者摄像头小窗（人物，不进入剧本）；页脚频道名水印 |

## 镜头说明
| 镜头 | 时间 | 画面内容 | 景别 / 运镜 | 同期讲解 |
|---|---|---|---|---|
| 1 | 00:00–00:24 | 标题页：实验台、仪表、导线、电路图拼图，闪电警示三角，实验名称 | 全屏幻灯片，静止；右上讲者小窗 | 本节讲三电压表法实验的口试题 |
| 2a | 00:24–00:55 | “Important Questions”6 题清单，打勾第 1 题，写 R and L | 全屏录屏，手写批注 | 三电压表法测未知线圈的 R 和 L |
| 2b | 00:55–02:05 | 同页，画交流电源—电感小电路，写 XL 公式、单位 ohm | 同上 | 感抗定义、公式、单位；电感单位亨利 |
| 2c | 02:05–03:15 | 同页，写 Z 单位、RLC 阻抗公式 | 同上 | 阻抗的含义，只用于交流 |
| 2d | 03:15–04:00 | 同页，在 MI/MC 下写 moving iron / moving coil、AC / DC | 同上 | 交流用动铁式，直流用动圈式 |
| 2e | 04:00–04:55 | 同页，写 Z = V3/I 和 Z = √(R² + XL²) | 同上 | 扼流线圈阻抗的算法 |
| 2f | 04:55–06:09 | 同页，写 XL ∝ f；之后板书逐步擦除 | 同上 | 感抗与频率成正比；口试建议 |
| 2g | 06:09–07:25 | “Thank you for listening!”页，写频率、角频率单位，容抗公式与曲线 | 全屏，手写批注 | 单位、容抗、容抗与频率成反比 |
| 2h | 07:25–09:15 | 同页，写 TRIAC、PE，画 TRIAC 符号；最后板书擦除 | 同上 | 扼流线圈被 TRIAC 替代、TRIAC 三端双向、交流调压；结束语 |

（shots.json 只切出 2 个镜头，镜头 2 是 8 分 51 秒的长录屏，按板书内容细分为 2a–2h。）

## 安全要点与原片的不足
- 全片没有任何安全内容。三电压表法实验要用到交流电源（通常经调压器供电）、电感线圈、电阻和多块电表，实际风险包括仪表选错、带电改线、调压装置调到最低时误以为已断电、手湿或脚下潮湿时操作、擅自拆开仪器或改动实验台内部接线、实验中途离开不断电、器材损坏不登记等。系列前几集已补过量程选择、调压器回零、电感断开感应电压、元件发热、电容残余电荷等，本片换用其他要点补充。
- K5 的说法不严谨：动圈式（永磁动圈式）仪表只能测直流；动铁式仪表交直流都能测，实验室多用于交流测量。剧本改成“测交流选动铁式，动圈式只测直流”。
- K12 的说法不严谨：扼流线圈作为电感器仍广泛使用；被 TRIAC 等电力电子器件取代的主要是用线圈调压的老式调速器、调光器（荧光灯电感镇流器被电子镇流器取代，与 TRIAC 无关）。剧本改说“很多调压场合改用电子调压装置”。
- 讲者鼓励“尽量说服考官（convince the examiner）”，剧本改为“简明作答，不会的如实说”。
- 幻灯片把本实验标为“Experiment 4”，与第 01 集大纲中的“实验三”编号不同，以本校实验指导书为准。
- 原片为印度高校课程，频道名、学校名、课程编号不进入剧本。
