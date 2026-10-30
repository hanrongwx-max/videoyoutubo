Series note — "BIORISK MANAGEMENT" (47) and "Microbiology Biosafety" (59): biosafety / biorisk-management videos.
- BIORISK MANAGEMENT: mostly MOOC / OER lectures (some CC-BY) on the AMP model (Assessment–Mitigation–Performance), WHO risk groups & Laboratory Biosafety Manual, BSC operation, double-bagging waste, containment / BSL-3 facilities, PPE (incl. COVID-19, PAPR), clinical / hospital samples, SOPs, biosafety officer, vector-borne diseases, plus one product video (an automated nucleic-acid extractor — treat as promotional, generic equipment only, brand in avoid). Many lectures overlap: when a video repeats a topic already done in the series, keep its own K points but pick different S points (check project/BIORISK MANAGEMENT/*/src.py).
- Microbiology Biosafety: short explainer clips from one microbiology channel (raqbamicrohub / ARHMicroHub) on biosafety levels, risk groups, BSC vs fume hood vs laminar flow, biosecurity, bioterrorism, lab hazards, SDS, chemical / fire / electrical safety, plus a few off-topic clips (light microscopy, lab report, COD, biostatistics, bioremediation microbes) — mark those relevance 低, keep their K points and add relevant lab-safety S points.

Domestic framework (cite by name; clause numbers and values “以现行文本为准”):
- 《中华人民共和国生物安全法》；《病原微生物实验室生物安全管理条例》；GB 19489-2008《实验室 生物安全通用要求》；WS 233-2017《病原微生物实验室生物安全通用准则》；《人间传染的病原微生物目录》（国家卫生健康委 2023 年版）；YY 0569（Ⅱ级生物安全柜，以现行文本为准）；《医疗废物管理条例》与感染性废物处置；高校实验室三级管理与准入。
- **Direction of classification is opposite**: WHO Risk Group 1 = lowest hazard; China's 病原微生物分类 第一类 = most dangerous, 第四类 = least. Every video that mentions risk groups must state this clearly. Lab levels BSL-1…4 ↔ 国内 BSL-1…4 / ABSL 同向.
- 高致病性病原微生物（第一、二类）实验活动须在相应级别实验室并经批准；学生不得擅自开展。新微生物/新实验的防护级别由风险评估确定、经单位生物安全委员会审批。
- 生物安保：菌（毒）种与样本的保藏、领用、运输（《可感染人类的高致病性病原微生物菌（毒）种或样本运输管理规定》，以现行文本为准）、丢失被盗报告；两用研究与伦理。
- Bioterrorism / biosecurity threats: teach recognition, prevention and reporting only — no agent-specific weaponization, production, enhancement or dissemination details; real attacks only as generic icons without names.
- Emergency: 溢洒、针刺、暴露后立即处置 → 报告实验室负责人→学院→学校生物安全管理部门/保卫处，必要时 120；如实记录与随访.
- COVID-19 era content: keep principles, mark time-specific rules as 当时做法，以现行规定为准.
- Avoid in scripts: WHO/CDC/organisation names in narration are allowed only as “国际组织” background; channel names (raqbamicrohub, ARHMicroHub, MOOC4DEV, UMS BRI), lecturer names, university names, product brands go in META["avoid"].
Use unique filenames for any scratch files. Publish each video with tools/publish.py right after its build passes.
A finished example: course/CDC Laboratory Safety Series/12_*.md and project/CDC Laboratory Safety Series/12_*/ (BSC), and course/General Lab Safety Practices/06_Centrifugation Hazards.md — match format; don't edit them.
