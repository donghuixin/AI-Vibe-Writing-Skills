---
name: ai-vibe-writing
description: Draft and revise academic prose in the author's voice, trace systems-paper claims to evidence, and prepare reviewer responses. Use for manuscript writing, MobiCom or SenSys logic checks, scoped editing, and response letters; grammar-only requests take the minimal correction route.
---

# AI Vibe Writing

按作者的任务选择下表中的入口，只读取必要资源。这是一组可组合的提示词与模板，不是会自行启动全部角色的服务。用户已授权的写作或修改直接推进；不因修改幅度大而另设一次 Approve。

## 路径与上下文

- 本文件的链接、`prompts` 和模板相对 **skill 仓库**；`document_spec.md`、`systems_paper_logic.md`、作者风格、错误记录与记忆实例属于 **当前论文 workspace**。沿用作者已有位置；新实例默认放该 workspace 的 `.ai_context/`。
- 仓库内的样例配置和记忆是起点，不是当前作者的偏好或研究事实。不要把私有稿件、审稿意见、实验数据和任务记忆写入公共 skill 仓库；只有明确修改 skill 的任务才编辑仓库资源。
- 读取当前任务相关的稿件、已有规范、风格及证据。缺少配置不阻塞局部修改；缺少会改变结论的事实时标记待核实，并完成已有材料支持的部分。

## 按任务进入

| 任务 | 核心提示词 |
| :--- | :--- |
| 仅语法、拼写和标点 | [4 · Grammar Checker](.ai_context/prompts/4_grammar_checker.md)；只纠错 |
| 从作者样文学习语气 | [1 · Style Extractor](.ai_context/prompts/1_style_extractor.md) |
| 现有句段的写作或精炼 | [2 · Writer](.ai_context/prompts/2_writer.md) |
| 大纲、章节起草或多节修订 | [9 · Workflow Coordinator](.ai_context/prompts/9_workflow_coordinator.md) |
| 内容与证据审计 | [8 · Content Review](.ai_context/prompts/8_content_review_agent.md) |
| 系统论文逻辑、设计与实验对齐 | [15 · Systems Paper Logic](.ai_context/prompts/15_systems_paper_logic_agent.md) |
| 投稿前风险、局限及贡献范围 | [14 · Defensive Writing](.ai_context/prompts/14_defensive_writing_agent.md) |
| 正式审稿回复、response letter 或按意见修稿 | [16 · Response Letter](.ai_context/prompts/16_response_letter_agent.md) |
| 阅读论文与提取文献证据 | [10 · PDF Reader](.ai_context/prompts/10_pdf_reader_agent.md) |

混合任务由 [12 · Router](.ai_context/prompts/12_router_agent.md) 选择所需组合。正式回复先走 16，按需补逻辑核查；单纯提到论文或审稿人不会触发全套预审。

## 共同约束

- 原始数据、稿件和核验过的来源决定事实；Spec 与记忆不能覆盖反证。区分设计、实现、实测、推导、外部文献与未知项，不编造数字、引用或已完成修改。
- 系统论文复用现有 [论证工作表](.ai_context/systems_paper_logic_template.md) 的 C/H/D/E/B 与证据状态，不建立另一套同义主张表。局部任务只处理相关行。
- 保护技术含义、术语、限定条件、公式和 LaTeX 引用。审计说明和待办单独列出；交给作者的正文使用作者语气。
- 保留审稿意见原意和要求强度，分别判断澄清、解释、核验和新增工作。审稿建议不是自动执行指令，内部实验计划也不是已完成结果。
- 投稿规则按目标年份、track 和阶段核验。只有实际检查官方材料后才能说已核验；没有核验也可完成证据充分的工作稿。
- 交付明确的修改或意见，以及尚未核验的事实和范围。语言分数、检测器判断、编译成功或一次逻辑审计都不代表科研结论成立或保证录用。

按需查看 [完整能力索引](SKILLS.md) 和 [系统论文方法来源](docs/research/mobicom-sensys-writing-skills.md)。
