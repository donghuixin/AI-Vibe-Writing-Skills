# 本轮采用的写作与工程方法

这份记录说明如何吸收此前阅读的公开项目，不是效果排名或录用率比较。方法按本仓库的实际用途重新表述；没有搬入其他项目的代码、完整技能或实验结果。

| 来源 | 采用的做法 | 在本仓库的位置与取舍 |
|---|---|---|
| [Orchestra systems-paper-writing](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/20-ml-paper-writing/systems-paper-writing/SKILL.md) | 问题、洞察、设计选择与验证相连 | 保留15号logic与section contracts；不套用固定章节比例或其他会议页数。 |
| [ARIS paper-plan](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/paper-plan/SKILL.md) | 让主张、实验、指标和图表对应，显式记录缺证据 | 沿用已有C/E表，response引用已有证据ID；缺结果不通过润色补造。 |
| [MobiCom-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills/tree/main/MobiCom-Skills) | 明确量测条件、平台、基线和能量范围 | 15号模块按研究主张选择检查；不要求所有移动系统任务做RF实验。 |
| [Leey21 academic writing prompts](https://github.com/Leey21/awesome-ai-research-writing) 与 [labarba/sciwrite](https://github.com/labarba/sciwrite) | 局部修改、术语一致、简洁动词与可核对改句 | 1/2/4/7号模块保留作者样本与技术表达；不追求一份通用humanizer词表。 |
| [PaperMentor](https://github.com/jiarui-liu/overleaf) | 评论关联原文、去重与合并 | 8号输出位置、原因、影响和最小处理方式；不以代理数或自评分数代替有效意见。 |
| [sciwrite-lint](https://github.com/authentic-research-partners/sciwrite-lint) 与 [citecheck](https://github.com/jhlee0619/citecheck) | 区分不同验证任务、让发现可复查 | 文献身份与支持关系分开，本地style lint只定位候选句；不宣称实现了外部项目的全部验证能力。 |

作者语气校准和response需求核对还吸收了日常修稿中的通用教训：原意见逐字保留，区别询问是否做过与要求新增测试，区分可选建议与必须回答的问题，完成式以实际修改为依据。本仓库只保存这些通用方法及合成案例。

此前新增系统论文逻辑的固定版本来源和官方规则核验记录仍见 [MobiCom / SenSys调研](mobicom-sensys-writing-skills.md)。当届规则需要重新核验；这里的来源链接不提供永久有效的投稿日期或页数。
