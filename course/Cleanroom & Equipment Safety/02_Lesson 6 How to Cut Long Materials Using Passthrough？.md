# 02_Lesson 6 How to Cut Long Materials Using Passthrough？

## 基本信息
| 项目 | 内容 |
|---|---|
| 剧集 | Cleanroom & Equipment Safety |
| 原标题 / 链接 | Lesson 6: How to Cut Long Materials Using Passthrough?；https://youtu.be/6VaMiheDwVs |
| 时长、分辨率 | 00:11:13（673.0 秒），1920×1080，镜头 65 个（镜 9 为 3 分多钟的软件录屏长镜头） |
| 语言 | 英语（男声画外讲解，带英文字幕） |
| 类型 | 操作演示（厂商系列课第 6 课：实拍 + 设计软件录屏） |
| 适用对象 | 使用该品牌激光焊机配套的封闭式数控切割机（带两侧穿透槽和夹具）的用户 |
| 与“实验室安全”主题的相关度 | 低：纯加工技术演示（超长板材分段切割与手动对位），安全内容只有一句“加工后戴耐热手套” |

> 剧集说明：本剧集名为“Cleanroom & Equipment Safety”，实际 33 个视频全部是同一品牌手持式激光焊机及其配套切割机的产品视频，与洁净室无关。

## 内容概要
本片讲如何利用封闭式激光切割机两侧的穿透槽（passthrough），分两段切割超过加工幅面的长板材，以 1 mm 不锈钢“WELCOME”门牌为例。先把板材从侧槽穿入、两端到机架距离相等后拧紧夹具旋钮，装切割嘴、接空压机。然后在设计软件里处理字母：给 O 加“桥”保留内芯、把孔和字母与边框合并；图案超出幅面，就旋转 90° 后用矩形把它分成左右两半，并用剪刀工具去掉多余线条。设置加工参数、校准电容传感器、走边框，切出第一段。之后戴耐热手套松开夹具，把板材平行右移、重新对齐固定，用焊接头红光和软件中的箭头图案记录两个接缝点坐标，必要时算出板材偏转角并旋转图案，再走边框检查、切出第二段。最后推出板材，展示接缝几乎看不出来的成品。

## 知识点
- K1 本课目标：用穿透槽切割超出幅面的长板材，以 1 mm 不锈钢为例（00:00–00:13）
- K2 切割前把板材从设备侧槽穿入，左右两侧都可以，本片从左往右（00:13–00:40）
- K3 固定前确保板材两端到机架的距离相等（箭头所指处），否则板材会有角度偏移；对齐后拧紧两侧夹具旋钮（00:40–00:59）
- K4 安装合适的切割嘴；本片用普通切割嘴，配空压机供气，气压 600 kPa（00:59–01:12）
- K5 设计处理：直接切字母 O 只会留下一个圆洞；要保留内部的椭圆，先加一个宽 5 mm 的矩形竖直居中放在 O 内，与 O 做“合并—减去”，形成连接筋（01:12–01:53）
- K6 把分散的图形合为一体：两个孔与边框做“重叠处减去”；字母图层必须在边框图层之上（不在就上移），再把字母与边框做“重叠处减去”，得到最终加工图（01:53–02:36）
- K7 图案太长超出画布需手动分割：先旋转 90°，加矩形作分割线；尽量从空白处分割以减少后续对位误差；本片若在空白处分，右段会超过 600 mm，只能从字母 C 中间分（02:36–03:08）
- K8 分割操作：复制粘贴整体图案，用矩形与图案做“重叠处减去”得到左半，同法得到右半；分割后出现 4 条多余线，双击进入编辑，用剪刀工具在线变色时点击删除；两半用不同颜色区分（03:08–04:26）
- K9 加工参数：模式“夹具切割”，材料 1 mm 304 不锈钢，气体为空压机，工作喷嘴 2 mm 切割嘴；红色图案关闭输出（否则报错）；调整黑色图案位置，图案边缘到材料边缘留 1.5 cm（04:26–05:08）
- K10 点击“校准电容传感器”再点材料完成校准；点边框图标并按设备上的按钮走边框；点加工，阅读右侧检查提示，确认切割头旋钮设在 −1，点开始，切出第一段（05:08–05:55）
- K11 加工后戴耐热手套操作：松开两侧旋钮，把板材平行右移；两端到机架的距离要与之前相同，否则角度会偏；拧紧旋钮（05:55–06:24）
- K12 把焊接头的红光移到接缝点（第一段切线的端点），红光较大时让其中心对准接缝点中心；在软件中沿 Z 轴下降焊接头，红光变小后再微调（06:24–06:53）
- K13 软件中移走黑色图案并关闭输出，红色图案打开输出并放上画布；添加箭头图案（换色区分）并放大，使箭头尖与激光十字准线完全重合，记录 X1、Y1；移到第二条切线的接缝点，重复下降、对准，记录 X2、Y2（06:53–08:12）
- K14 对位检查：把图案角对齐第一个箭头尖，看另一个点是否对齐；对不上说明上一步板材有角度偏移，用两点坐标在斜率计算器中算出角度（本片 89.77°），90° 减去得偏转量 0.23°，图案逆时针倾斜时取 −0.23° 输入，再对齐，两角都与箭头尖重合即完成（08:12–09:24）
- K15 删除多余图案和字母，记得打开红色图案的输出；这一步不必再校准电容传感器，但必须走边框检查对位，确认后点“边框完成”、加工、开始（09:24–10:02）
- K16 加工完成后松开两侧旋钮，从侧槽推出板材；接缝处精度很好，只要按步骤操作，看不出是手动对位的（10:02–11:13）

## 讲解内容（逐段）
| 时间 | 讲解要点 | 原话摘录 |
|---|---|---|
| 00:00–00:13 | 片头“Lesson 6”，切割机与焊机主机；提出主题，1 mm 不锈钢为例 | “how to cut a long metal using the pass-through” |
| 00:13–00:40 | 戴棉纱手套从左侧槽插入板材，左视 / 右视图标出侧槽 | “You can start from either side slot.” |
| 00:40–00:59 | 两端距离相等，拧紧旋钮 | “Otherwise, the material may have an angle shift.” |
| 00:59–01:12 | 装普通切割嘴，空压机 600 kPa | — |
| 01:12–02:36 | 软件：字母 O 加桥、孔与边框合并、图层顺序、字母与边框合并 | “To preserve the ellipse inside, we need to perform extra operations.” |
| 02:36–04:26 | 旋转、分割、去多余线、两色区分 | “Try to split from the blank space to minimize subsequent calibration errors.” |
| 04:26–05:55 | 参数、红色图案关闭输出、留边 1.5 cm、电容传感器校准、走边框、检查提示（旋钮 −1）、开始切割（火花从机下溅出） | “Remember to reserve 1.5 centimeters between the edges…” |
| 05:55–06:24 | 戴耐热（皮质焊接）手套松旋钮、平移板材、重新对齐 | “After processing, wear heat-resistant gloves for subsequent operations.” |
| 06:24–08:12 | 红光对接缝点、Z 轴下降、箭头对十字、记录两点坐标 | “Make sure they overlap exactly.” |
| 08:12–09:24 | 对位检查、斜率计算器算角度、输入负角度 | “If the alignment fails, the material angle was shifted in the previous step.” |
| 09:24–10:02 | 打开红色图案输出、走边框检查、加工第二段 | “we should perform the framing to check the alignment.” |
| 10:02–11:13 | 推出板材，展示接缝；门牌挂在门边的效果图；“Tips”卡 | “You can't even tell it was manually adjusted.” |

## 画面文字（字符）
- 00:00 片头：“Lesson 6 / How to Cut Long Materials Using Passthrough”；全片左上角品牌标志，机身有品牌字样和黄色激光警告标签。
- 00:35 分屏标注：“Left view / Right view”，红框标侧槽。
- 字幕（与讲解一致）：You can start from either side slot；After alignment, tighten the knobs on both sides；use [品牌] Air Compressor with 600 kPa gas pressure；For example, the letter "O"；Here, we get the final design for processing；Unlock the aspect ratio；the pattern on the right side would be over 600 mm long；But you'll notice four unwanted lines in the patterns；Select Cutting with fixture as the processing mode；Select 1 mm 304 stainless steel as the processing material；Select 2 mm cutting nozzle as the working nozzle；Remember to reserve 1.5 cm between the edges；Press the button on the device；Read the instructions on the right panel；and ensure that the cutting tip knob is set at the value -1；wear heat-resistant gloves for subsequent operations；Y1 is 20.7；Y2 is 320.6；In this video, the angle value is 89.77；instead of 0.23；Remember to enable Output for the red pattern；Push out the material from the side slots；You can't even tell it was manually adjusted。
- 软件界面：顶部提示“Before processing, we recommend reviewing metal cutting tips for better cutting results”；右栏 Gas pressure（约 600–770 kPa 波动）、Mode: Cutting with fixture、Material: 3/64"(1mm, Ga.19) 304 St…、Gas: 空压机、Nozzle: 2mm cutting nozzle、Calibrate the capacitive sensor、Output 开关；选材料窗口（Precautions：Remove protective film before…、Use odor protection during processing…）；选气体窗口（空压机、Air、Oxygen、N2、Ar）；选喷嘴窗口；Tips 窗口“The framing function is ready. Press the button on the device to start framing…”、“Framing completed”；“Check before processing”页（Pressure、Nozzle、Focus position −1）；Jog 面板（XY / Z 步距）。
- 08:45 网页斜率计算器（第三方网站，品牌不使用）。
- 11:03 结尾卡“Tips”。

## 镜头说明
| 镜头 | 时间 | 画面内容 | 景别 / 运镜 | 同期讲解 |
|---|---|---|---|---|
| 1 | 00:00–00:04 | 片头：切割机与焊机主机 | 全景字卡 | 主题 |
| 2–6 | 00:04–00:40 | 戴棉纱手套从侧槽插入长不锈钢板；左右视图 | 中景 / 分屏 | 侧槽穿板 |
| 7 | 00:40–00:59 | 调整板材、拧紧旋钮 | 中景 | 两端等距、拧紧 |
| 8 | 00:59–01:12 | 装切割嘴 | 近景 | 喷嘴与气源 |
| 9 | 01:12–04:30 | 设计软件录屏：加桥、合并、图层、旋转、分割、去线 | 录屏长镜头 | 软件操作 |
| 10–14 | 04:30–05:08 | 软件：模式、材料、气体、喷嘴、图案位置 | 录屏 | 参数与留边 |
| 15–19 | 05:08–05:29 | 电容传感器校准（实拍切割头）、走边框提示与实拍 | 录屏 / 实拍 | 校准、走边框 |
| 20–22 | 05:29–05:42 | 加工前检查页、切割头旋钮 −1 实拍 | 录屏 / 画中画 | 检查提示 |
| 23–24 | 05:42–05:55 | 第一段切割，火花从下方溅出 | 全景 | — |
| 25–29 | 05:55–06:24 | 戴焊接手套松旋钮、平移板材、红箭头标两端距离、拧紧 | 中景 | 平移与重新对齐 |
| 30–34 | 06:24–06:53 | 手指指示接缝点；红光；Jog 面板下降 Z 轴；红光变小 | 特写 / 画中画 | 红光对位 |
| 35–41 | 06:53–08:12 | 软件放红色图案、加箭头、对十字、记录 X1/Y1、X2/Y2 | 录屏 / 实拍 | 记录坐标 |
| 42–48 | 08:12–09:19 | 对位检查、斜率计算器、输入 −0.23° | 录屏 | 偏转校正 |
| 49–54 | 09:19–09:53 | 两角对齐、打开输出、走边框、点加工 | 录屏 / 实拍 | 走边框检查 |
| 55–57 | 09:53–10:11 | 第二段切割与完成 | 全景 | — |
| 58–59 | 10:11–10:21 | 从侧槽推出长板 | 中景 | 推出板材 |
| 60–63 | 10:21–10:46 | 成品门牌在绿色台面上，接缝处 C 字特写 | 近景 / 特写 | 接缝效果 |
| 64 | 10:46–10:53 | 门牌挂在住宅门边的效果图 | 全景 | — |
| 65 | 10:53–11:13 | 结尾“Tips”卡 | 字卡 | — |

## 安全要点与原片的不足
- **定位**：纯加工技术演示，安全内容只有“加工后戴耐热手套”。
- **穿透槽的激光与火花风险未提**：封闭式切割机两侧开槽后，罩体不再完全封闭，可能有反射光、火花和烟尘从槽口逸出；原片没有讲加工时槽口附近不站人、不伸手、不拆改联锁、设备的激光安全等级以铭牌和说明书为准。
- **对位时手伸进机内**：镜 30–34 演示者手指靠近切割头指点接缝点；原片没说明此时应确认出光未启用、运动停止，也没讲红光不可直视、龙门运动夹手风险。
- **手套**：上料、对位用棉纱手套，加工后才换皮质耐热手套；长不锈钢板边缘锋利，切割件刚切完很烫，应全程戴防割 / 耐热手套，长板两人搬运。
- **烟尘与防火**：切割时火花从机下大量溅出（镜 24），没有讲排风、废料抽屉清理和灭火器材；软件材料窗口本身提示“处理时注意气味防护”，原片未展开。
- **气源**：空压机 600 kPa 只作参数提及，没有讲压力管路、接头检查。
- **数值**：600 kPa、5 mm 桥宽、1.5 cm 留边、−1 旋钮等是本型号的参数，剧本只保留“留边”“按检查提示设置”等做法，不写本型号数值（5 mm、1.5 cm 作为通用做法保留在图示文字中）。
- **缺失**：准入授权、急停与应急、事故报告、用后收尾。
