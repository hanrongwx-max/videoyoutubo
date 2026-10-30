# 08_Modelling for Synthetic Biology - iGEM 2020 Opening Weekend Festival

## 基本信息
| 项目 | 内容 |
|---|---|
| 剧集 | General Lab Safety Practices |
| 原标题 / 链接 | Modelling for Synthetic Biology - iGEM 2020 Opening Weekend Festival；https://youtu.be/z7isDdt0lS0 |
| 时长、分辨率 | 00:52:07（3127.8 秒），1920×1080 |
| 语言 | 英语（男声讲解，非母语口音；右上角小窗为讲者摄像头，主画面为幻灯片和软件演示） |
| 类型 | 讲座录屏（2020 年 5 月 17 日面向国际合成生物学学生竞赛参赛队的线上讲座，幻灯片 + 交互式绘图小程序演示 + 问答） |
| 适用对象 | 参加合成生物学项目的本科生、研究生（生物、生化、工程、计算机背景） |
| 与“实验室安全”主题的相关度 | 低：本片是合成生物学数学建模的科研方法讲座（模型类型、设计—构建—测试循环、基因表达的常微分方程模型、希尔函数、准稳态近似、荧光报告与校准）。与安全相关的只有一句“模型可以在真实系统中危险或昂贵的条件下做‘实验’”；生物安全、基因工程审批、废物灭活、两用研究等均未涉及 |

## 内容概要
讲者先说明本讲两个目标：为什么要在进实验室之前先建模和设计，以及如何开始为合成生物学建模；再用时装模特、建筑模型、模式生物斑马鱼说明“模型是代表另一个系统的东西”，介绍示意图、生化反应式、常微分方程三类模型。随后把建模放进“设计—构建—测试”工程循环，反对“先做一堆实验再拿模型去拟合”的做法，并列举建模的好处。主体部分从中心法则和转录单元四元件（启动子、核糖体结合位点、编码序列、终止子）出发，写出组成型表达的质量作用动力学方程，讲参数来源，再用希尔函数描述激活子和阻遏子调控（用自编交互小程序演示半浓度常数、希尔系数、泄漏表达的影响），用准稳态近似把模型化简，并说明如何用时程实验和稳态剂量—响应实验与模型对接；以群体感应负反馈电路为例说明大模型可化简。最后讲荧光报告蛋白的选择、荧光与光密度的校准，以及校准后的单位如何对应模型中的“每个细胞的分子数”，把测试结果带回再设计；问答环节比较了机器学习黑箱模型与第一性原理机理模型。

## 知识点
- K1 本讲两个目标：在动手实施、进实验室之前先建模和设计；学会如何开始为合成生物学建模（02:37–03:23）
- K2 模型是“代表我们想研究的另一个系统”的东西：时装模特、建筑模型、模式生物（斑马鱼）都是模型（03:23–04:18）
- K3 三类模型逐级深入：示意图（元件相互作用）→ 生化反应式（反应动力学）→ 数学模型（常微分方程组，可由质量作用定律从反应式转换得到，描述各物种浓度随时间的变化）（04:18–05:29）
- K4 不要“先做大量实验再拿模型去拟合”；按工程学科的设计—构建—测试循环：先设计和建模，再构建（组装、克隆），再校准测量和测试，不符合预期就回到再设计（05:29–07:46）
- K5 建模的作用：证明实验设计可行、指导元件选择与组装、实验前预测输出、提供更好的再设计；优点还包括分析小改动对整体的影响、找出最关键的变量、在真实系统中危险或昂贵的条件下做“实验”（建造前排障）、回答“如果改变……会怎样”、降低决策风险，从而节省时间和经费（07:46–09:59）
- K6 建模对象是中心法则（DNA 转录为 mRNA，核糖体翻译成蛋白质）；一个转录单元需要四种基本元件：启动子（控制转录速率）、核糖体结合位点 RBS（影响翻译起始速率）、编码序列（决定生产什么蛋白）、终止子（结束转录）；元件—转录单元—器件—系统逐级组成（09:59–12:32）
- K7 基因表达分两类：组成型（不受调控，基因一直开着）和受调控型（由转录因子蛋白结合启动子来激活或抑制，可开可关）（12:32–14:10）
- K8 组成型表达的质量作用模型：mRNA 变化率 = k1 − d1·m，蛋白变化率 = k2·m − d2·p；k1 为转录速率（取决于启动子），k2 为翻译速率（取决于 RBS），d1、d2 为降解速率；正项使数量增加，负项使数量减少（14:10–17:07）
- K9 参数从哪里来：可查汇集文献数值的生物学数据库，例如大肠杆菌中 mRNA 半衰期约 5–10 分钟、绿色荧光蛋白半衰期约 90 分钟（17:07–18:10）
- K10 同一启动子配不同强度的 RBS，相当于模型中改变 k2，得到不同的蛋白表达水平；模拟曲线可与（校准后的）实验数据对比；组成型表达始终开着，“比较无趣”（18:10–19:55）
- K11 激活子调控：mRNA 生成项用希尔函数描述，含基础表达 b0（无激活剂时的表达）、半浓度常数 K（输出达到一半时的激活剂量）和希尔系数 n（转录因子协同结合的程度，越大曲线越陡；自然界多为 1–4，乳糖阻遏蛋白常取 4）；讲者用交互小程序演示参数的影响（19:55–27:05）
- K12 阻遏子调控：希尔函数的分子换成 K，曲线反向——无阻遏蛋白时表达最高，阻遏蛋白越多表达越低；能压多低取决于启动子的泄漏表达 α0（理想启动子为 0，实验室常见约 0.05–0.2）；希尔系数越大，过渡越陡（27:05–31:13）
- K13 准稳态近似（QSSA）：若转录等反应很快，可令 mRNA 的变化率≈0，解出 m 代入蛋白方程，得到只剩一个变量的蛋白方程；用软件数值求解，不同激活剂浓度达到不同的蛋白水平（31:13–35:45）
- K14 模型与实验对接的两种方式：①固定激活剂浓度，按固定间隔（例中每 5 分钟）测荧光蛋白随时间的变化，与方程解比较；②等蛋白达到稳态后测不同激活剂浓度下的水平，得到希尔形剂量—响应曲线，用来表征 n、K 等模型参数（35:45–39:50）
- K15 复杂电路示例：群体感应信号分子进出细胞、与转录因子结合后抑制启动子，构成负反馈；写出 22 个反应、10 个物种，得到较大的常微分方程模型；用准稳态近似可得降阶模型，两者动态略有差别但稳态一致——可以舍弃部分复杂度，但要清楚自己在做什么（39:50–42:58）
- K16 荧光是观测细胞内部情况的好办法：绿色荧光蛋白（来自水母）是好的报告蛋白，但荧光蛋白种类很多，应根据激发和发射光谱为项目选择合适的一种或几种（42:58–44:35）
- K17 校准：用荧光素（绿色）和红色荧光染料标准品把读板仪荧光读数换算成标准分子数，用微球颗粒校准光密度换算成颗粒（细胞）数；二者相除得到“每颗粒的荧光分子当量”，相当于模型中每个细胞的蛋白分子数；校准与测量把测试结果带回设计与建模，完成循环（44:35–47:25）
- K18 问答：机器学习（神经网络）是需要大量数据的“黑箱”模型，能预测但不解释机理；本讲的模型基于第一性原理，可以从机理上解释细胞内发生的事（47:25–52:07）

## 讲解内容（逐段）
1. **00:00–00:10 片头**：粉、黄、蓝三色斜块的会议片头，无讲解。
2. **00:10–01:00 开场与议程**：标题页（讲座名称、讲者、主办委员会、日期、讲者所在实验室标志）；议程五项：什么是模型及其在设计—构建—测试循环中的位置与重要性，建模对象（中心法则、转录单元及其元件），基因表达建模与准稳态近似，合成基因电路示例，报告蛋白与校准。原话：“First, what is a model and where is modeling and design, build and test cycle of synthetic biology.”
3. **01:00–01:49 问卷**：请观众扫码填写背景与知识问卷；约 70% 听众是当年参赛学生，背景以生物、生化为主，也有工程和计算机。（转写 “IGM” 应为竞赛名缩写。）
4. **01:49–02:37 讲者介绍**：电子工程学士、控制工程博士，从学生、指导教师到评委和测量委员会成员的经历（个人信息，不进入剧本）。
5. **02:37–03:23 两个目标（K1）**：为什么要在实施和进实验室之前先建模和设计；如何开始建模。讲者提到当年疫情使很多实验室无法开放，正好利用这段时间学习建模。原话：“why it's important to model and design before the implementation, and before going to the lab.”
6. **03:23–04:18 什么是模型（K2）**：时装模特、建筑师施工前做的建筑模型、生物学家研究用的模式生物斑马鱼；总结：模型是代表我们要研究的另一个系统的东西。原话：“A model is something that represents another system that we want to study.”
7. **04:18–05:29 模型类型（K3）**：示意图展示元件间相互作用（例为一个合成电路）；进一步写出底层生化反应式；再用质量作用动力学转换成常微分方程组，描述各物种数量随时间的变化。原话：“using the law of mass action kinetics, we can convert from the biochemical reactions into these sets of equations”。
8. **05:29–06:20 错误的起点（K4）**：常见做法是先构建电路、做大量读板仪、流式细胞术、显微镜实验，再“做个数学模型去拟合所有这些数据”——讲者明确说这不是要走的路。原话：“let me tell you that this is not the way we want to do.”
9. **06:20–07:46 设计—构建—测试循环（K4）**：引用前一天另一场讲座的比喻：如果土木工程师像分子生物学家那样造桥，桥塌了就再造一次，直到成功；工程做法是先设计并建模，再到实验室组装、克隆，再校准测量、测试，不符合预期就再设计。原话：“What we want to do is to first design … and to model the system that we want to build.”
10. **07:46–08:35 为什么建模（K5）**：证明实验设计可行；指导元件选择与组装；实验前预测电路输出；循环回来时提供更好的再设计。
11. **08:35–09:59 建模的优点（K5）**：幻灯片列五条，讲者重点讲第三条：可在真实系统中危险或经济代价高的条件下做“实验”，相当于构建和组装前的排障；过去只能“构建—测试—失败—再构建”，有了模型可先在模型里试各种方案，选中满意的再去构建，节省时间和经费。原话：“Mathematical model will allow you to perform experiments in conditions that would be dangerous or of high economic cost in the real system.”（转写 “in mind” 应为 “money”。）
12. **09:59–10:50 建模对象：中心法则（K6）**：信息储存在 DNA，RNA 聚合酶转录成 mRNA，核糖体翻译成蛋白质，蛋白质在细胞中执行功能——从信息到行动。
13. **10:50–12:32 转录单元及其元件（K6）**：要让转录、翻译发生，需要启动子、RBS、编码序列、终止子四种元件；前两者是控制元件，启动子控制与 RNA 聚合酶的关系和转录，RBS 控制核糖体结合和翻译起始速率；编码序列决定生产什么蛋白，终止子结束转录；元件可逐级组成转录单元、器件、系统，本讲只关注最底层两级。
14. **12:32–14:10 两类基因表达（K7）**：组成型表达——基因一直开着，转录翻译持续发生；受调控表达——可开可关，由转录因子结合启动子激活或抑制转录。原话：“It can be an unregulated process, which is … constitutive expression. The gene is always on.”
15. **14:10–17:07 组成型表达模型（K8）**：基因以转录速率 k1 产生 mRNA，核糖体以速率 k2 产生蛋白，mRNA 和蛋白分别以 d1、d2 降解；方程中带点的符号表示对时间的导数；正项使数量上升，负项使数量下降；蛋白生成项与 mRNA 数量成正比。原话：“positive terms in these equations means that the amount … will go up … and negative terms will be responsible for the amount of mRNA going down.”
16. **17:07–18:10 参数来源（K9）**：参数从哪里来是第一个难题；讲者在聊天区贴出一个收集大量文献数值的数据库链接，例如 mRNA 半衰期约 5–10 分钟、绿色荧光蛋白半衰期约 90 分钟。
17. **18:10–19:55 不同 RBS 的模拟（K10）**：图中纵轴为每颗粒荧光分子当量（后文解释），点为三个只换 RBS 的转录单元实验数据，线为不同 k2 的模拟；改变 RBS 得到不同表达水平。组成型表达一直开着，“有点无趣”。
18. **19:55–21:49 激活子模型（K11）**：蛋白方程不变；mRNA 生成项变为基础转录速率 b0 加上希尔函数项，其中 A 为激活剂数量，可由外部加入，也可在后续模型中由电路产生。（回答听众关于 K 的提问：此处 K 为半浓度常数，与解离常数相关但不相同。）
19. **21:49–27:05 希尔函数小程序演示（K11）**：归一化希尔函数 = 基础表达 β0 + Aⁿ/(Kdⁿ + Aⁿ)；设 K=400 时，激活剂为 0 则无表达，增大激活剂输出上升，在 400 处达到 50%；增大希尔系数曲线中段更陡，例如 n=4 表示需要 4 个激活剂分子共同结合启动子；自然界 n 一般 1（无协同）到 2–4，乳糖阻遏蛋白常用 4；这些数值也可在数据库查到。讲者答应之后提供小程序代码，并回答了软件授权的提问（不进入剧本）。原话：“a hill coefficient of four means that we need four molecules of the activator together to bind to the promoter”。（转写 “heal function” 应为 Hill function，“Basel” 应为 basal。）
20. **27:05–30:05 阻遏子模型与演示（K12）**：希尔函数分子改为 Kⁿ，变量 R 代表阻遏蛋白；无阻遏蛋白时表达最高（归一化为 1），阻遏蛋白增至半浓度常数（演示中约 250）时表达减半，再增加可达到更强抑制；能抑制到多低取决于泄漏表达 α0：理想启动子为 0，实验室中常见启动子约 0.2、0.1、0.05，“很差”的启动子更高；希尔系数越大过渡越陡。原话：“How much repression can we get? That depends on the leakiness of the promoter”。
21. **30:05–31:13 希尔函数小结（K11、K12）**：激活型启动子随激活因子增多表达上升，阻遏型随阻遏因子增多表达下降；泄漏表达是在最高阻遏水平下仍残留的表达。
22. **31:13–33:05 快反应假设（K13）**：若 DNA 到 mRNA 的转录很快，mRNA 迅速达到平衡，可令其导数为 0，解出平衡时的 m 表达式。
23. **33:05–35:50 准稳态近似（K13）**：把 m 代入蛋白方程，只剩一个描述蛋白随时间变化的方程，唯一随时间变化的输入是激活剂 A，其余 k2、d1、b0 等为由电路构建决定的固定参数；可手算，也可用软件数值求解；激活剂越多，蛋白最终水平越高。（问答插入：激活型称基础表达，阻遏型称泄漏表达。）
24. **35:50–37:35 时程实验（K14）**：固定激活剂浓度，用读板仪每隔一段时间（幻灯片写“每 5 分钟”）测荧光蛋白，随时间上升到稳态，与方程的解比较。讲者预告夏季将有专门讲座。
25. **37:35–39:50 稳态剂量—响应（K14）**：等蛋白浓度稳定后测不同激活剂浓度下的值；数学上令蛋白导数为 0 解出 p，得到的形状正是希尔函数；把实验点与模型曲线对照，可表征 n、K 等参数。原话：“in the experiment, what we do is we wait enough time until the concentration of the protein reaches the equilibrium.”
26. **39:50–41:15 群体感应电路示例（K15）**：信号分子 AHL 进出细胞，与转录因子 LuxR 结合、成对后抑制启动子，使目的蛋白和 AHL 合成酶 LuxI 减少，形成负反馈。（转写 “quantum sensing” 应为 quorum sensing，“LaxI/looks R” 应为 LuxI/LuxR，“demerize” 应为 dimerize。）
27. **41:15–42:58 模型化简（K15）**：22 个反应、10 个物种，得到 9N+1 个常微分方程的确定性模型（列出模型假设）；用准稳态近似去掉快变量，得到 4N+1 个方程加 1 个代数方程的降阶模型；模拟对比：降阶模型（红线）与完整模型（蓝虚线）动态略有差别，稳态一致。原话：“it's okay to drop some complexity and to simplify our models … but we just need to know what we are doing”。
28. **42:58–44:35 荧光报告（K16）**：荧光是测量细胞内部情况的好方法；绿色荧光蛋白最早来自水母，是好的报告蛋白；荧光蛋白种类很多，选择时要研究激发和发射光谱，官方测量资源页面可帮助选择。（转写 “Korea Victoria” 应为 Aequorea victoria。）
29. **44:35–45:38 校准（K17）**：用荧光素标准把读板仪绿色荧光读数换算为分子数，当年新增红色荧光标准；用微球颗粒校准光密度，换算为培养物中的颗粒（细胞）数。（转写 “beds” 应为 beads，“fluorescent in” 应为 fluorescein。）
30. **45:38–47:25 回到模型（K17）**：校准后的生长曲线（颗粒数）与荧光曲线（荧光分子当量）相除，得到每颗粒荧光分子当量，相当于模型中每个细胞内的蛋白分子数 p；校准和测量让我们从测试回到设计、建模和模拟，完成循环。
31. **47:25–48:33 结束语**：感谢收听，预告夏季工作坊，请填写问卷（含组织机构名，不进入剧本）。
32. **48:33–50:21 问答：人工智能（K18）**：深度学习、机器学习是用数据训练神经网络来预测，需要大量数据；本讲的模型基于第一性原理，能从机理解释细胞内发生什么；黑箱模型给出预测但不解释系统功能。原话：“that's what is called the black box model you put the data and you get the prediction but it doesn't explain you what the system is doing”。
33. **50:21–52:07 问答：推荐文献与联系方式**：将在网页上整理推荐文献（举了一本数学生物学教材）；问题可通过网站、邮件和即时通讯继续提问。（不进入剧本。）

## 画面文字（字符）
| 时间 | 文字 |
|---|---|
| 00:00–00:10 | 无文字（粉黄蓝色块片头） |
| 00:10–00:30 | (Introduction to) Modeling for Synthetic Biology / by（讲者姓名）/ An iGEM Measurement Committee Webinar / iGEM Opening Weekend / May 17th, 2020；左上讲者实验室与大学标志（sb2cl Lab、ai2 等），右上竞赛 2020 Measurement 标志 |
| 00:30–01:00 | Today Webinar's Topics：What is a model and where is modeling in the design, build and test cycle of Synthetic Biology, and why is it important? / What are we modeling? – Central dogma of molecular biology – TU and its bioparts / Modeling gene expression and QSSA / Example of synthetic gene circuit and its model / Reporters and calibration |
| 01:00–01:49 | Please fill in the Background and knowledge survey: / 二维码 / Who are you? / 问卷平台链接 |
| 01:49–02:37 | Who am I? 讲者姓名、所在城市与大学；Electronic Engineer (2009)；PhD in Control Engineering with applications in SynBio (2014)；Ass. Prof. of Synthetic Biology and Computational Biology (2019)；2010 Student First time / 2018 Instructor Grand Prize winners / 2018-2020 Judge / 2019-2020 Measurement Committee（附团队合影） |
| 02:37–03:20 | Two important things we want you to get from this Webinar / Why it is important to model and design before the implementation.（竖食指手势图） |
| 03:20–03:36 | But first, What is a MODEL? |
| 03:36–04:19 | 照片：时装秀 T 台、建筑模型、斑马鱼，无文字 |
| 04:19–05:30 | Types of models：Schematic / Biochemical Reactions / Mathematical Model (ODEs)；电路示意图标注 LuxR、AHL、LuxI、Pol、cell membrane 等；方程细字不可辨认；From Y. Boada (2018) |
| 05:30–06:20 | How do we start?（实验数据拼图：读板仪曲线、流式直方图、显微照片、试管）；弹出框 Let us make a mathematical model to fit all these experimental data!! |
| 06:20–07:50 | Modeling in the Design, Build and Test cycle：(Re) Design – Modeling and simulation / Build – Assembly and Cloning / Test – Calibration and Measurement |
| 07:50–08:35 | Why modeling for synthetic biology? Prove an experimental design is feasible / Guide us in the selection of parts and assembly / Predict expected outputs before lab work / Provide us with a better design: Re-design |
| 08:35–09:57 | Advantages of mathematical modeling：Allows you to analyze the effect on the overall performance of a system of small changes made to one or more of its components / The analysis of the model can allow you to suggest possible improvements to the real system, as well as to detect the most influential variables in the performance / It allows you to perform experiments in conditions that could be dangerous or of high economic cost in the real system (troubleshooting before construction and assembly) / It allows to answer questions such as "what would happen if we made this change in…" / It contributes to reducing the risk inherent in decision making. |
| 09:57–10:50 | What are we modeling? The central dogma of molecular biology；Transcription of DNA by RNA polymerase / Translation of mRNA by Ribosomes；图中 DNA、mRNA、PROTEIN、Ribosome、Amino acids、Prokaryote cell |
| 10:50–12:35 | Transcriptional units (TUs) and its bioparts：Systems / Devices / TUs / Bioparts；Promoter: Controls transcription rate；Ribosome Binding Site (RBS): Affects translation initiation rate；Gene of interest: DNA coding for a protein (CDS)；Terminator；侧标 SBOL visual、BioBrick；底部序列条 P1、RBS、rfp、TERM |
| 12:35–13:20 | Gene expression can be: Unregulated – On – Constitutive: the gene is always on / Regulated – Off ⇄ On – Gene transcription regulation: Expression controlled by some proteins |
| 13:20–14:05 | Modelling gene expression：Unregulated gene is always on (Constitutive Promoter, RBS, Gene, TT) / Regulated by some proteins as: Activators, Repressors (transcription factor TF, Induced Promoter) |
| 14:05–17:20 | Constitutive gene expression / Mass action kinetic model：ṁ = k1 − d1m；ṗ = k2m − d2p；标注 Transcription rate (Promoter)、mRNA degradation rate、Translation rate (RBS)、Protein degradation rate；左侧 Gene→Transcription→mRNA→Translation→Protein，各自 →∅ |
| 17:20–18:20 | Some numbers from（数据库标志）：RNA polymerase transcription rate of mRNA, related to k1, 28-89 Nucleotide/sec, E. coli；mRNA half life, related to d1, 5-10 min；Rate of translation by ribosome, related to k2, 12-21 Aa/sec；Total translation time of the lacZ gene (1025 codons) ~82 sec；Half-life of GFP, related to d2, ~90 min；GFP maturation time 6.5 min；Constant for binding of activator CRP to lac promoter activating site 0.02 nM |
| 18:20–20:05 | 同上方程 + 图：纵轴 Protein (MEFL/Particle)，横轴 Time (min)；图例 Experimental（三个元件编号）/ Simulation Strong / Medium / Weak RBS |
| 20:05–21:49 | Gene expression regulation: Activator / Mass action kinetic model + Hill function：ṁ = b0 + k1·Aⁿ/(Kⁿ+Aⁿ) − d1m；ṗ = k2m − d2p；basal transcription rate、Hill function；右下 Hill Function Plot App 与软件标志 |
| 21:49–27:05 | Hill Function Plot App / Normalized Hill function Activator：Hill(A) = β0 + Aⁿ/(Kdⁿ+Aⁿ)；小程序窗口：Hill Function (Activator) 曲线、旋钮 Half-concentration constant (Kd)（刻度 0.1–2000）、Hill Coefficient 滑块、Basal Expression；底部 Windows 任务栏 |
| 27:05–27:55 | Gene expression regulation: Repressor：ṁ = b0 + k1·Kⁿ/(Kⁿ+Rⁿ) − d1m；（27:26 误弹出西班牙语右键菜单） |
| 27:55–30:05 | Normalized Hill function Repressor：Hill(A) = α0 + Kdⁿ/(Kdⁿ+Aⁿ)；小程序 Hill Function (Repressor)，滑块 Leakiness |
| 30:05–31:20 | The Hill function: How to model regulation of gene expression：h(A) = k1·Aⁿ/(Kⁿ+Aⁿ)；number of activators that need to cooperatively bind the promoter；Maximal transcription rate；Activation Coefficient (Half concentration)；Activator / Repressor 两行示意与曲线 |
| 31:20–33:05 | Gene expression regulation: Activator → Fast → ṁ ≈ 0 |
| 33:05–35:50 | Quasi steady state approximation (QSSA) / Fast reactions (transcription, binding/unbinding some species) are in steady state；ṁ≈0 → m = (1/d1)(b0 + k1Aⁿ/(Kⁿ+Aⁿ)) → ṗ = (k2/d1)(…) − d2p / Protein concentration equation；图：Number of molecules vs Time (hours)，Increasing Activator；Depending on the Activator concentration: we obtain different levels of protein concentration. |
| 35:50–37:35 | We can make an experiment to characterize the dynamics of the protein concentration；For a fixed activator concentration / Measure the protein concentration every 5 minutes… |
| 37:35–39:50 | Steady state concentration：ṗ≈0 → p = k2/(d1d2)·(b0 + k1Aⁿ/(Kⁿ+Aⁿ))；We wait the protein concentration to stabilize and then measure for different values of the activator concentration. ↓ We can caracterize some parameters of the model. Like for example: n, K, b0k2/d2, k1；横轴 Activator concentration (nM) |
| 39:50–41:15 | Example of modeling for synthetic biology / Controlling expression of a protein of interest pol；Quorum sensing: Exchange of AHLext and AHL for consensus among cells；Negative feedback: AHL together with LuxR protein repress Pol and LuxI proteins at the same time；文献出处行；41:11 Transcription and Translation reactions / Degradation reactions / QS/Fb gene circuit 10 biochemical species, 22 biochemical reactions |
| 41:15–41:50 | Mass action kinetics we design a Deterministic model of the QS/Fb circuit / 9*N+1 ODEs / Model assumptions 1–7（RNA polymerase fast time-varying fluctuations are neglected; Specific growth rate μ added to degradation; Plasmid number of genes is kept as a constant; At cell division plasmids are duplicated…; AHLext is not subject to dilution; Binding of (LuxR.AHL)2 to the repressor is always possible; AHLext diffusion is a pseudo-reaction modeled using a lumped approximation of the Fick's law） |
| 41:50–42:20 | Applying QSSA we can obtain a reduced model / 4*N+1 ODEs + 1 algebraic eq. / Reduced model assumptions: Invariants of genes; Fast reactions are in equilibrium（RNA polymerase to promoter binding/unbinding; Transcription factor to promoter binding/unbinding; Transcription; AHL and LuxR binding/unbinding）; 19 model parameters; N cells；变量表 |
| 42:20–42:58 | Simulations（软件名）of both models. The reduced order model is OK；九格曲线 LuxI、LuxR、AHL、mRNA、DNA 等，图例 Reduced / Complete；It is OK to drop some complexity and to simplify our models, just know what you are doing! |
| 42:58–43:26 | Fluorescence is a good way to measure what happens in the cell（培养皿与发绿光的离心管照片） |
| 43:26–43:40 | Green Fluorescent Protein (GFP) is a good reporter. Jellyfish Aequorea victoria；238 amino acids；β-barrel structure, 11 antiparallel β-sheets；Fluorophore in the centre of the barrel (Ser65-Tyr66-Gly67) |
| 43:40–43:58 | 同标题；显微镜屏幕上的绿色荧光细胞与两支黄绿色溶液离心管照片 |
| 43:58–44:35 | But there are many fluorescent proteins / How to select the Right Fluorescent Protein(s)?；一排不同颜色荧光的管子；Excitation / Emission 光谱图；资源页链接 |
| 44:35–45:38 | Calibrated Fluorescent Proteins together with Calibrated Optical Density (OD) is even better.；Plate Reader（读板仪照片，机身品牌字样）；Fluorescein / Texas Red 孔板；微球电镜照片；柱状图；协议页链接 |
| 45:38–46:55 | Why, and how it relates back to modeling?；Particles、Fluorescence (MEFL) → MEFL/Particle；MEFL/Particle unit is equivalent to number of molecules/cell in a mathematical model |
| 46:55–47:25 | Calibration and measurements brings you back in the cycle into Re-design；(Re) Design / Build – DNA Assembly methods and Cloning / Test – Calibration and Measurement |
| 47:25–52:07 | Questions? / Thank You & Have an Exceptional Year of（竞赛名）! / The（竞赛名）Measurement Committee is actively working on preparing workshops this summer, stay tuned! / Go check out the Measurement Hub! / 网址；左右下角竞赛标志 |

## 镜头说明
场景检测切出 13 个镜头，其中镜头 6（04:19–21:49）和镜头 7（21:49–42:58）为长镜头（幻灯片翻页不触发切分），下表按 15 秒关键帧和讲解细分。全片画面构成固定：顶部正中为讲者摄像头小窗（白墙前、深色上衣的男讲者，近景，固定），下方为幻灯片或软件全屏。

| 镜头 | 时间 | 画面内容 | 景别 / 运镜 | 同期讲解 |
|---|---|---|---|---|
| 1 | 00:00–00:10 | 粉黄蓝三色斜块片头 | 全屏图形，固定 | 无（开始前） |
| 1 | 00:10–00:30 | 讲者小窗 + 标题页 | 屏幕录制，固定 | 欢迎，本讲为该委员会最后一场讲座 |
| 1 | 00:30–01:00 | 议程页 | 屏幕录制 | 介绍五部分内容 |
| 1 | 01:00–01:49 | 问卷二维码页 | 屏幕录制 | 请填问卷；听众背景统计 |
| 2 | 01:49–02:37 | “Who am I?”个人经历页及合影 | 屏幕录制 | 讲者学历与参赛、指导、评审经历 |
| 2 | 02:37–03:20 | 两个目标页，竖食指手势图 | 屏幕录制 | 先建模设计再实施；疫情下利用时间学建模（K1） |
| 2 | 03:20–03:36 | “But first, What is a MODEL?” | 屏幕录制 | 引出模型定义 |
| 3 | 03:36–03:43 | 时装秀 T 台照片 | 全屏照片 | 时装模特（玩笑） |
| 4 | 03:43–03:55 | 木质建筑模型照片 | 全屏照片 | 建筑模型（K2） |
| 5 | 03:55–04:19 | 斑马鱼照片（蓝底） | 全屏照片 | 模式生物；模型定义（K2） |
| 6 | 04:19–05:30 | “Types of models”三栏逐步出现：电路示意图、反应式、ODE | 屏幕录制，逐项动画 | 三类模型、质量作用定律（K3） |
| 6 | 05:30–06:20 | “How do we start?”实验数据拼图，弹出“拟合所有数据”框 | 屏幕录制 | 先做实验再拟合不是正确方法（K4） |
| 6 | 06:20–07:50 | 设计—构建—测试循环图 | 屏幕录制 | 造桥比喻、工程循环（K4） |
| 6 | 07:50–08:35 | “Why modeling…”四条 | 屏幕录制 | 可行性、选元件、预测、再设计（K5） |
| 6 | 08:35–09:57 | “Advantages…”五条文字页 | 屏幕录制 | 重点讲危险或昂贵条件下的模拟、建造前排障（K5） |
| 6 | 09:57–10:50 | 空白标题页 → 中心法则示意图 | 屏幕录制 | DNA→mRNA→蛋白（K6） |
| 6 | 10:50–12:35 | 转录单元及其元件图（层级框 + 元件符号） | 屏幕录制 | 四元件功能与层级（K6） |
| 6 | 12:35–14:05 | 组成型 / 调控型表达对比图，“Modelling gene expression” | 屏幕录制 | 两类表达、转录因子（K7） |
| 6 | 14:05–17:20 | 组成型表达方程页，红色激光笔逐项指示 | 屏幕录制 | 方程各项含义（K8） |
| 6 | 17:20–18:20 | 数据库数值表（讲者小窗短暂放大） | 屏幕录制 | 参数来源、半衰期示例（K9） |
| 6 | 18:20–20:05 | 方程 + 三组 RBS 实验与模拟曲线 | 屏幕录制 | 改变 RBS 即改变 k2（K10） |
| 6 | 20:05–21:49 | 激活子方程页（希尔函数高亮） | 屏幕录制 | 基础表达、激活剂 A；回答听众提问（K11） |
| 7 | 21:49–27:05 | 希尔函数小程序（激活型），调旋钮和滑块，曲线变陡；底部任务栏可见 | 屏幕录制，软件操作 | K=400 处达 50%；希尔系数与协同性（K11） |
| 7 | 27:05–27:55 | 阻遏子方程页（中途误弹右键菜单） | 屏幕录制 | 阻遏子模型（K12） |
| 7 | 27:55–30:05 | 希尔函数小程序（阻遏型），调节泄漏表达 | 屏幕录制，软件操作 | 半浓度约 250；泄漏表达 0.05–0.2（K12） |
| 7 | 30:05–31:20 | 希尔函数小结页（激活/阻遏两行） | 屏幕录制 | 激活与阻遏对比、泄漏表达（K11–K12） |
| 7 | 31:20–33:05 | 激活子模型圈出 + “Fast → ṁ≈0” | 屏幕录制 | 快反应假设（K13） |
| 7 | 33:05–35:50 | QSSA 推导页与不同激活剂浓度的时程曲线 | 屏幕录制 | 化为单一蛋白方程、数值求解（K13） |
| 7 | 35:50–37:35 | 时程实验数据点与拟合曲线 | 屏幕录制 | 固定激活剂、定时测量、与模型比较（K14） |
| 7 | 37:35–39:50 | 稳态剂量—响应曲线页 | 屏幕录制 | 稳态测量、表征参数（K14） |
| 7 | 39:50–41:15 | 群体感应负反馈电路图 → 反应式列表 | 屏幕录制 | 电路原理，22 反应 10 物种（K15） |
| 7 | 41:15–42:20 | 完整模型方程与假设 → 降阶模型 | 屏幕录制 | QSSA 化简（K15） |
| 7 | 42:20–42:58 | 两模型九格模拟曲线对比 | 屏幕录制 | 稳态一致，可简化但要知其所以然（K15） |
| 8 | 42:58–43:26 | 发绿色荧光的培养皿与离心管照片，标题叠字 | 全屏照片 | 荧光是好的测量方法（K16） |
| 9 | 43:26–43:40 | 水母照片、绿色荧光蛋白结构图 | 屏幕录制 | 绿色荧光蛋白是好的报告蛋白（K16） |
| 10 | 43:40–43:58 | 显微镜屏幕荧光细胞与两支黄绿色溶液管照片 | 屏幕录制 | 显微图像与纯化蛋白（K16） |
| 11 | 43:58–44:35 | 一排多色荧光管与激发/发射光谱 | 屏幕录制 | 按光谱选择荧光蛋白（K16） |
| 12 | 44:35–45:38 | 读板仪照片、荧光标准孔板、微球电镜照片、柱状图 | 屏幕录制 | 荧光与 OD 校准（K17） |
| 13 | 45:38–46:55 | 颗粒数与荧光曲线 → 每颗粒荧光分子当量 | 屏幕录制 | 对应模型中每细胞分子数（K17） |
| 13 | 46:55–47:25 | 再设计循环图 | 屏幕录制 | 校准与测量带回再设计（K17） |
| 13 | 47:25–48:33 | “Questions?”致谢页 | 屏幕录制，固定 | 结束语、预告工作坊 |
| 13 | 48:33–50:21 | 同上（讲者小窗时而放大） | 屏幕录制，固定 | 问答：机器学习黑箱 vs 机理模型（K18） |
| 13 | 50:21–52:07 | 同上 | 屏幕录制，固定 | 推荐文献、联系方式、感谢 |

## 安全要点与原片的不足
1. **本片是科研方法讲座，不是安全片**：全片围绕数学建模与测量校准，没有任何实验室安全、生物安全或基因工程管理内容。唯一相关的一句是“模型可以在真实系统中危险或昂贵的条件下做‘实验’”，但讲者没有说明：模型只能辅助判断，**不能代替实验前的生物安全风险评估和审批**。
2. **缺少合成生物学生物安全与生物安保知识**：片中涉及在大肠杆菌中构建表达电路、群体感应电路、荧光蛋白报告株，提到哺乳动物细胞显微图像，但未提《中华人民共和国生物安全法》、基因工程（重组 DNA）实验的风险评估与学校生物安全委员会审批、实验室生物安全防护等级、基因工程菌的防逃逸与废物灭活、两用研究风险与科研伦理、溢洒与事故报告。
3. **未提准入与个人防护**：校准、读板、培养等实验环节在国内须先经实验室准入培训，穿实验服、戴手套等；原片只有照片，无人员操作镜头，无法判断防护是否到位。
4. **模型局限讲得不够**：讲者强调模型可预测和节省成本，问答中也提到参数难得、简化要“知道自己在做什么”，但没有强调参数不确定、模型假设（如稳态、确定性、单一细胞类型）在真实环境中可能失效；模型预测“表达量低”“电路受控”不等于工程菌对人和环境安全。
5. **环境释放问题**：群体感应等电路常被设计用于细胞间通讯和环境感应，原片未提基因工程生物不得擅自带出实验室或向环境释放。
6. **转写错误**：IGM / IgM → 竞赛名缩写；“in structure” → instructor；“in mind” → money；“bio numbers” → 生物数值数据库名；“heal function” → Hill function；“Basel” → basal；“quantum sensing” → quorum sensing；“LaxI / looks R” → LuxI / LuxR；“demerize” → dimerize；“Korea Victoria” → Aequorea victoria；“beds” → beads；“fluorescent in” → fluorescein；“very valid promoter” 应为 “very leaky/bad promoter”；“Murai” → Murray（教材作者）。幻灯片拼写 “caracterize” 应为 characterize。
7. **出镜信息**：标题页、致谢页、个人经历页含竞赛与委员会名称、讲者姓名与照片、大学与实验室标志、问卷平台链接、合影中的他人肖像；数值表含数据库标志；演示使用商业数学软件（标志与名称可见）；读板仪照片有品牌字样；红色荧光标准使用商品染料名。卡通改编中全部不使用。
