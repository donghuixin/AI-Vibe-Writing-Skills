# 能力索引

[SKILL.md](SKILL.md) 是统一入口，包含任务路由、路径约定和共同约束。下列提示词保留原有编号与路径，可单独调用；无需依次运行。详细规则由各提示词维护，本索引不另设流程。

| 提示词 | 用途 |
| :--- | :--- |
| [1 · Style Extractor](.ai_context/prompts/1_style_extractor.md) | 从作者样文与反馈提取可解释的语气偏好 |
| [2 · Writer](.ai_context/prompts/2_writer.md) | 有范围的日常写作、句段精炼和语气适配 |
| [3 · Error Logger](.ai_context/prompts/3_error_logger.md) | 记录适用于当前作者或项目的纠错规则 |
| [4 · Grammar Checker](.ai_context/prompts/4_grammar_checker.md) | 保留原意的语法、拼写与标点纠错 |
| [5 · Long-Term Memory](.ai_context/prompts/5_long_term_memory.md) | 按项目与来源管理事实、术语和偏好 |
| [6 · Outline Manager](.ai_context/prompts/6_outline_manager_agent.md) | 按写作任务建立和检查章节契约 |
| [7 · Content Writer](.ai_context/prompts/7_content_writer_agent.md) | 按已有大纲、证据和作者语气起草章节 |
| [8 · Content Review](.ai_context/prompts/8_content_review_agent.md) | 定位论证、证据、结构与表达问题 |
| [9 · Workflow Coordinator](.ai_context/prompts/9_workflow_coordinator.md) | 协调涉及多阶段的写作和修订 |
| [10 · PDF Reader](.ai_context/prompts/10_pdf_reader_agent.md) | 阅读指定论文、定位证据并按任务入库 |
| [11 · Context Compactor](.ai_context/prompts/11_context_compactor_agent.md) | 保留任务、来源、证据状态与未完成项的交接 |
| [12 · Router](.ai_context/prompts/12_router_agent.md) | 按目标交付与编辑范围组合提示词 |
| [13 · LaTeX Self-Healing](.ai_context/prompts/13_latex_self_healing_agent.md) | 根据实际编译日志修复排版问题 |
| [14 · Defensive Writing](.ai_context/prompts/14_defensive_writing_agent.md) | 用证据判断审稿风险、贡献边界与合理表述 |
| [15 · Systems Paper Logic](.ai_context/prompts/15_systems_paper_logic_agent.md) | 检查场景、挑战、设计、证据与边界的联系 |
| [16 · Response Letter](.ai_context/prompts/16_response_letter_agent.md) | 对齐真实审稿要求、作者回复和稿件修改状态 |

## 兼容入口

- [`.traerules`](.traerules) 加载统一入口，适用于旧的 IDE 配置。
- [`/ai_vibe_writing`](.agents/workflows/ai_vibe_writing.md) 按任务选择写作流程。
- [`/pdf_ingestion`](.agents/workflows/pdf_ingestion.md) 阅读论文或整理参考资料。
- [`/defensive_writing`](.agents/workflows/defensive_writing.md) 检查投稿前风险和局限。
- [`/response_letter`](.agents/workflows/response_letter.md) 起草、审计或修订正式回复。

旧调用继续使用原路径。workflow 仅说明如何调用相应提示词；不会再维护一套独立的审批、评分或审稿策略。

## 模板与项目实例

模板位于 skill 仓库。填好的实例、作者偏好和研究事实保存到作者当前论文 workspace，沿用其已有文件位置。未填写的模板和仓库样例不能作为事实。

| 资源 | 当前论文中的用途 |
| :--- | :--- |
| [Document Spec](.ai_context/document_spec_template.md) | 写作目标、范围与约束；不替代证据 |
| [Systems Paper Logic](.ai_context/systems_paper_logic_template.md) | C/H/D/E/B、证据状态、章节交接与缺口 |
| [Revision Response](.ai_context/revision_response_template.md) | 原意见覆盖、作者答覆与实际修改状态 |
| [Outline](.ai_context/outline_template.md) | 需要大纲时使用的章节契约 |
| [Style Profile](.ai_context/style_profile.md) | 按作者样文和明确偏好填入项目实例 |
| [Custom Specs](.ai_context/custom_specs.md) | 当前任务选择与可选设置 |
| [Reference Learning](.ai_context/reference_learning.md) | 文献摘要、来源和支持范围的整理 |
| [PDF Ingestion](.ai_context/pdf_ingestion_template.md) | PDF 阅读时的来源定位与提取记录 |

系统论文的方法取舍见 [调研说明](docs/research/mobicom-sensys-writing-skills.md)。
