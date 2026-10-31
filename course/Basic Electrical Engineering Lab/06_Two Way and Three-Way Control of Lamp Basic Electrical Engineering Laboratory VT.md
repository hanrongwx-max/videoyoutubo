# 06_Two Way and Three-Way Control of Lamp Basic Electrical Engineering Laboratory VT

## 基本信息
| 项目 | 内容 |
|---|---|
| 剧集 | Basic Electrical Engineering Lab |
| 原标题 / 链接 | Two Way and Three-Way Control of Lamp Basic Electrical Engineering Laboratory VTU Syllabus BE B Tech；https://youtu.be/SnRr1pVEpBo |
| 时长、分辨率 | 00:10:44（643.9 秒），1920×1080 |
| 语言 | 英语（印度口音男声画外音；转写为 Whisper small.en，“two table / tooth table”= truth table、“40 volts”= 40 W、“circular diagram”= circuit diagram、“close connection”= cross connection 等已按上下文更正） |
| 类型 | 操作演示（录屏软件播放的幻灯片 + 实验室实拍接线和开关操作） |
| 适用对象 | 工科一年级电工基础实验课学生 |
| 与“实验室安全”主题的相关度 | 低–中：完整演示 220/230 V 单相交流照明电路的接线和操作；电路中熔断器、开关都接在相线上（正确），但片中没有讲断电接线、教师检查、通电时不碰裸露金属、灯泡发烫等安全要点；接线时是否已断电画面上无法确认 |

## 内容概要
本片是电工基础实验课的“双控与三地控制照明及真值表”实验。双控：两只双控（单刀双掷）开关在两个地点控制同一盏灯，即楼梯布线，也用于卧室；三地控制：在两只双控开关之间加一只中间开关，三个地点控制一盏灯，讲者称为“花园布线”，也用于大仓库、粮库。先讲实验目的和所需器材（双控开关 5 A/230 V 两只、中间开关 5 A/230 V 一只、白炽灯 230 V/40 W 一只、连接导线），再按电路图讲接线：相线经熔断器接 S1 的公共端 A，B–E、C–F 相连，S2 的公共端 D 接灯，灯的另一端接中性线。在透明接线板上实拍接线、扳动开关，灯亮灭，填写双控真值表（4 种状态）。三地控制中，中间开关有“直连”（PQ、RS 接通）和“交叉”（PS、QR 接通）两种状态，分别配合 S1、S2 得到 8 种状态的真值表。最后结论：双控可在两地、三地控制可在三地控制同一盏灯。

## 知识点
- K1 双控照明：两只开关在两个不同地点控制同一盏灯，又叫楼梯布线，也可用于卧室（00:00–00:30）
- K2 三地控制：在两只主开关之外再加一只中间开关，三个地点控制同一盏灯（讲者称“花园布线”）（00:30–00:50）
- K3 实验目的：在两地、三地控制一盏灯，并列出各自的真值表（00:50–01:24）
- K4 所需器材：双控开关两只、中间开关一只（均为 5 A、230 V）、白炽灯一只（230 V、40 W）、连接导线（01:24–02:14）
- K5 双控电路：单相 230 V、50 Hz 交流电源，相线先经熔断器接 S1 的公共端 A；S1 的 B 接 S2 的 E，C 接 F；S2 的公共端 D 接灯的一端，灯的另一端接中性线（02:14–03:17）
- K6 实际接线：先准备好器材，在接线板上按图依次连接 B–E、C–F，再从 D 接灯、灯接中性线（03:17–03:51）
- K7 扳动 S1、S2 改变位置，观察灯的亮灭（03:51–04:23）
- K8 双控真值表：AB–DE 亮，AB–DF 灭，AC–DE 灭，AC–DF 亮（04:23–04:54）
- K9 中间开关有两个状态：直连（P–Q、R–S 接通）和交叉（P–S、Q–R 接通），两者不能同时成立（04:54–05:50）
- K10 三地控制接线：相线接 A，B 接 P（Q 接 E），C 接 R（S 接 F），D 接灯，灯接中性线（05:50–06:44）
- K11 实拍接线：先连 S1 到中间开关、中间开关到 S2 的两路线，再接灯和中性线；中间开关扳上为直连、扳下为交叉（06:44–08:21）
- K12 在直连和交叉两种状态下分别扳动 S1、S2，记录灯的状态（08:18–08:36）
- K13 三地控制真值表共 8 种状态：直连时与双控相同（亮、灭、灭、亮），交叉时相反（灭、亮、亮、灭）；可用逻辑 1、0 表示亮灭（08:36–09:40）
- K14 三地控制用于大仓库、粮库等大型建筑（09:40–09:55）
- K15 结论：双控能在两地控制一盏灯，加中间开关能在三地控制；这个实验对家庭布线有帮助，关键是理解开关的逻辑（09:55–10:44）

## 讲解内容（逐段）
1. **00:00–00:21 片头（K1）**：红底黄绿字频道公告（请关注、订阅），讲者介绍双控照明的概念。
2. **00:21–01:24 题目与目的（K1–K3）**：标题“Two way and Three-way Control of lamp and formation of Truth table”和 AIM 幻灯片。原话：“3-way control of lamp is mainly used in garden. So it is also known as garden wiring.”
3. **01:24–02:14 器材（K4）**：Apparatus Required 表，讲者勾出额定值。
4. **02:14–03:17 双控电路图（K5）**：手写标 S1、S2、P、N；电路图中灯标 100 W、230 V（与器材表 40 W 不一致）。原话：“First of all from the phase you have to take a connection, it should be connected to point A.”
5. **03:17–04:54 双控实拍（K6–K8）**：透明亚克力接线板上装两只开关、灯座和白炽灯，橙色、黑色香蕉插头导线；讲者（戴腕表）徒手插线、扳开关，灯亮灭；切到真值表幻灯片。
6. **04:54–06:44 三地控制电路图（K9、K10）**：手写 straight、cross，红色虚线示意交叉连接。原话：“the straight connection and cross connection can possible only at a time.”
7. **06:44–08:36 三地控制实拍（K11、K12）**：讲者（戴口罩、腕表）在接线板上插线，背景墙上有插座面板；扳动中间开关和两只双控开关，灯亮灭。
8. **08:36–09:55 真值表（K13、K14）**：8 行真值表，讲者逐行圈出 ON/OFF（口述交叉部分时读错几行，幻灯片为准）。
9. **09:55–10:44 结论（K15）**：Conclusion 幻灯片，THANK YOU。

## 画面文字（字符）
| 时间 | 文字 |
|---|---|
| 00:00–00:21 | Dear viewers, In case you are watching first time, this is a channel on Engineering studies focusing more on Electrical & Electronics. Please check the description link for more videos. Also please like, share, and subscribe. Do click on the Bell icon to get notified as I upload new video on every day. Thank you |
| 全片 | 播放器字幕条：18EEL27_BEELAB_2 WAY AND 3 WAY CONTROL OF LAMP；录屏软件水印；右下录屏时间戳 2021-07-31 16:xx |
| 00:21–01:14 | Two way and Three-way Control of lamp and formation of Truth table |
| 01:14–01:24 | AIM: To control the lamp from two different points (places), and also to control the lamp from three different points (places) along with the formulation of truth table for each case. |
| 01:24–02:14 | Apparatus Required：Two Way Switches 5A, 230 V, 2；Intermediate Switch 5A, 230 V, 1；Incandescent Lamp 230V, 40W, 1；Connecting Wires - - |
| 02:14–03:22 | (i) Two way control of lamp circuit diagram：Two Way Switch、A、B、C、D、E、F、S1、S2、Fuse、1-Phase 230V, 50 Hz AC Supply、P、N、Lamp 100W, 230V |
| 04:23–05:01 | Truth Table for Two Way Control of Lamp：1 AB DE ON；2 AB DF OFF；3 AC DE OFF；4 AC DF ON |
| 05:01–07:18 | (i) Three way control of lamp circuit diagram：Two Way Switch、Intermediate Switch、P、Q、R、S、S3、Lamp 100W, 230V；手写 straight、cross |
| 08:36–09:55 | Truth Table for Three Way Control of Lamp：1–4 PQ, RS (Straight Connection)：ON OFF OFF ON；5–8 PS, QR (Cross Connection)：OFF ON ON OFF |
| 09:55–10:35 | Conclusion：It is possible to control the lamp from two different places by using Two Way Control of Lamp. Also control of the lamp from three different places may obtained by Three Way Control of Lamp. |
| 10:35–10:44 | THANK YOU |

## 镜头说明
| 镜头 | 时间 | 画面内容 | 景别 / 运镜 | 同期讲解 |
|---|---|---|---|---|
| 1 | 00:00–00:21 | 频道公告页 | 全屏图文 | 双控照明的概念 |
| 2 | 00:21–01:24 | 标题页 → AIM | 全屏录屏 | 双控、三地控制，实验目的 |
| 3 | 01:24–02:14 | 器材表 | 全屏录屏 | 开关、灯、导线的规格 |
| 4–5 | 02:14–03:26 | 双控电路图，手写标注 | 全屏录屏 | 接线顺序 |
| 6–10 | 03:26–04:23 | 实拍：透明接线板上插线，扳开关，灯亮灭 | 近景俯拍，手持 | 接线与开关状态 |
| 11 | 04:23–04:45 | 双控真值表 | 全屏 | 4 种状态 |
| 12 | 04:45–04:54 | 实拍：再次扳开关验证 | 近景 | 验证 |
| 13–14 | 04:54–07:18 | 三地控制电路图，手写直连、交叉 | 全屏录屏 | 中间开关两种状态；接线顺序 |
| 15–20 | 07:18–08:36 | 实拍：在接线板上插线（戴口罩、腕表），扳动中间开关和双控开关，灯亮灭 | 近景、中景，手持 | 直连与交叉 |
| 21 | 08:36–10:44 | 三地控制真值表 → 结论 → THANK YOU | 全屏录屏 | 8 种状态，应用，结论 |

## 安全要点与原片的不足
- **原片的正确做法**：电路中熔断器和开关都串在相线上，灯接在开关之后、另一端接中性线——这是照明电路的正确接法，剧本保留并强调。
- **断电接线未交代**：实拍接线时看不出电源是否已断开，原片没有讲“断电接线、教师检查后通电”。
- **通电操作**：接线板上香蕉插孔、灯座金属部分外露，演示者戴金属腕表徒手操作；应只碰开关手柄，不碰插孔、插头金属部分和灯座。
- **灯泡发烫**：白炽灯通电后很烫，换灯泡要断电、等冷却。
- **熔断器**：只在图中出现，没有讲熔断器熔断后要查明原因，不能用铜丝等代替。
- **规格不一致**：器材表灯为 40 W，电路图标 100 W；剧本不写具体功率。
- **说法**：“garden wiring（花园布线）”“go-down（仓库）布线”为当地叫法，国内称“三地控制”或“多地控制”。
- 片头的频道推广、课程代码 18EEL27、录屏软件水印，剧本不使用。
- **共性缺失**：触电急救、电气火灾处置和报告。
