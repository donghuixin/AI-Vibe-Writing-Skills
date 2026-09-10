---
name: ai-vibe-writing
description: Draft, revise, and audit academic prose with style preservation, evidence tracking, systems-paper logic, and defensive reviewer analysis. Use for MobiCom or SenSys papers, Introduction-to-Design alignment, claim-to-experiment checks, limitations, and rebuttals; use the grammar-only route for minimal corrections.
---

# AI Vibe Writing

本仓库是一组可组合的提示词与工作流，不是独立执行的多 Agent 服务。路径均相对本文件所在目录；按任务读取相关资源，不需要加载全部 prompts。只更新用户指定的论文或工作文件，不把示例事实当成论文结果。

## 按任务进入

| 任务 | 读取资源 | 交付 |
| :--- | :--- | :--- |
| MobiCom / SenSys 系统论文、论证断点、Introduction 与 Design 对齐 | [.ai_context/prompts/15_systems_paper_logic_agent.md](.ai_context/prompts/15_systems_paper_logic_agent.md) | 逻辑链、贡献证据表、章节契约、优先修复项 |
| 审稿风险、局限与上中下三策 | [.ai_context/prompts/14_defensive_writing_agent.md](.ai_context/prompts/14_defensive_writing_agent.md) | 攻击面、证据化表述、回复备份 |
| 全文规划和写作闭环 | [.ai_context/prompts/9_workflow_coordinator.md](.ai_context/prompts/9_workflow_coordinator.md) | Spec、大纲、正文与审计报告 |
| 已有大纲下起草或修订 | [.ai_context/prompts/7_content_writer_agent.md](.ai_context/prompts/7_content_writer_agent.md) | 正文及证据引用 |
| 内容检阅 | [.ai_context/prompts/8_content_review_agent.md](.ai_context/prompts/8_content_review_agent.md) | 有定位、影响与修复动作的报告 |
| 仅语法纠错 | [.ai_context/prompts/4_grammar_checker.md](.ai_context/prompts/4_grammar_checker.md) | 最小纠错，不启动全文重构 |
| 阅读论文获取证据 | [.ai_context/prompts/10_pdf_reader_agent.md](.ai_context/prompts/10_pdf_reader_agent.md) | 带来源的文献事实 |

## 共同约束

- 读取已有 `document_spec.md`、`custom_specs.md`、`style_profile.md` 与 `error_log.md`；只召回相关记忆。缺少 Spec 时，局部审计可用临时假设并显式标注，全文写作沿用协调器的 Spec 确认流程。
- 原始数据、论文图表和可核验来源决定事实。Spec 是写作约定，不会把未经验证的作者主张变成事实；发现冲突应报告并修正主张。
- 区分实测、推导、假设和缺失证据。不捏造数字、引用、消融、统计显著性或已完成的修订。
- 年份、track 和阶段决定投稿规则。只有实际打开目标届官方材料后才能声称已核验；未联网或规则冲突时报告未核验项，不沿用其他会议或旧届规定。
- 保留技术术语、单位、符号和 LaTeX 引用。逻辑审计与防御性预审不能替代实验，也不保证录用。

完整能力索引见 [SKILLS.md](SKILLS.md)。来源比较和设计取舍见 [MobiCom / SenSys 调研](docs/research/mobicom-sensys-writing-skills.md)，仅在需要了解方法来源时读取。
