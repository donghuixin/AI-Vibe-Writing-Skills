# 写作技艺总览（Skills）

本文件汇总当前仓库中所有写作能力、核心提示词（prompts）与写作注意事项，并梳理知识库与参考文献学习的使用方式，便于用户快速理解和配置。

## 1. 系统级写作流程（必须遵循）

本系统采用 **Spec-Driven (规范驱动)** 写作理念，工作流贯穿所有任务：
1. **规范制定 (Spec Definition)**：系统生成 `document_spec.md`，明确核心论据、证据与负面约束。此为单点客观真相 (Single Source of Truth)。
2. **规划 (Outline)**：生成带有严格 `definition_of_done` (DoD) 的大纲章节。
3. **分析与召回**：读取 `style_profile.md` 与长短期记忆，避免已知错误并对齐领域术语。
4. **写作 (Draft)**：写作 Agent 根据 DoD 与约束生成内容。遇大规模修改须先提交 `<Revision_Plan>`。
5. **防御性预审 (Defensive Red-Team Review)**：防御性写作 Agent 提前识别审稿攻击面，区分核心贡献、适用边界与未来工程优化。
6. **规范审计 (Spec Audit) 与自检**：检阅 Agent 对照 `document_spec.md` 逐条审计。排查 AI 味及词汇违例。
7. **迭代**：未能通过审计直接打回强制重写。用户反馈更新对应记忆库。

参考配置入口：
- `.traerules`
- `.ai_context/document_spec_template.md` (新增)
- `.ai_context/style_profile.md`
- `.ai_context/error_log.md`
- `.ai_context/custom_specs.md`
- `.ai_context/outline_template.md` (含 DoD 更新)
- `.ai_context/memory/hard_memory.json`
- `.ai_context/memory/soft_memory.json`

## 2. 核心 Prompts 与能力定位

### 基础模块
- **风格提取器**（1_style_extractor）：抽取写作风格 DNA 与 Do/Don’t。
- **写作引擎**（2_writer）：按风格、错题本、记忆生成内容，并在生成前后自检。
- **错误记录器**（3_error_logger）：将用户修正转为“负面约束规则”，写入错题本并重写。
- **语法检查器**（4_grammar_checker）：定位语法、拼写和标点问题，尽量不改写。
- **长期记忆管家**（5_long_term_memory）：将事实与偏好写入硬/软记忆并按领域检索。

### 多智能体模块
- **大纲管理智能体**（6_outline_manager_agent）：创建/校验/存储大纲并输出结构化校验结果。
- **写作智能体**（7_content_writer_agent）：在大纲与记忆约束下生成与修订内容。
- **检阅智能体**（8_content_review_agent）：AI 味检测与外部查重能力整合（如 GPTZero）。
- **流程协调器**（9_workflow_coordinator）：串联大纲 → 写作 → 防御性预审 → 检阅的闭环流程。
- **PDF 阅读智能体**（10_pdf_reader_agent）：读取本地/在线 PDF 并入库参考文献与证据。
- **上下文压缩器**（11_context_compactor_agent）：将长上下文压缩为核心论点骨架、风格快照与已决规范。
- **主控路由智能体**（12_router_agent）：根据章节与文件类型动态挂载 Prompt 切片。
- **LaTeX 编译自愈智能体**（13_latex_self_healing_agent）：通过日志分析、动态脚本与重编译闭环修复 LaTeX 问题。
- **防御性写作智能体**（14_defensive_writing_agent）：执行审稿人红队式预审，按上策（特点化）→中策（工程边界分析）→下策（rebuttal 兜底）选择策略，并输出攻击面、贡献边界、防御性表述与 rebuttal backup。

Prompts 位置：
- `.ai_context/prompts/1_style_extractor.md`
- `.ai_context/prompts/2_writer.md`
- `.ai_context/prompts/3_error_logger.md`
- `.ai_context/prompts/4_grammar_checker.md`
- `.ai_context/prompts/5_long_term_memory.md`
- `.ai_context/prompts/6_outline_manager_agent.md`
- `.ai_context/prompts/7_content_writer_agent.md`
- `.ai_context/prompts/8_content_review_agent.md`
- `.ai_context/prompts/9_workflow_coordinator.md`
- `.ai_context/prompts/10_pdf_reader_agent.md`
- `.ai_context/prompts/11_context_compactor_agent.md`
- `.ai_context/prompts/12_router_agent.md`
- `.ai_context/prompts/13_latex_self_healing_agent.md`
- `.ai_context/prompts/14_defensive_writing_agent.md`

## 3. Antigravity Workflows / Antigravity 自动化工作流

本仓库内置了专为 Antigravity Agent 设计的自动化执行脚本（位于 `.agents/workflows/` 目录下）：
- **`/ai_vibe_writing`**: 自动分析 `custom_specs.md`、生成大纲、起草文本并完成 AI 检阅与修订。
- **`/pdf_ingestion`**: 自动下载或读取本地 PDF，解析文本并提取结构化事实写入 `reference_library.json` 等长期记忆。
- **`/defensive_writing`**: 对论文片段、实验、Discussion、Limitations 或 Rebuttal 执行审稿攻击面红队式预审，生成防御性表述与审稿回复备份。

## 4. 写作注意事项（高优先级规则）

1. **必须敲定 Document Spec**：任何大型写作任务首要确认 Spec，不可跳过此步骤。
2. **严格遵守 DoD**：大纲中的 Definition of Done 是验收红线。
3. **重写需提案 (Revision Plan)**：遇到大规模用户修改意见，严禁直接生成正文，必须先输出修订方案 `<Revision_Plan>`，用户同意后再执行。
4. **必须读取风格与错题本**：避免风格漂移与历史错误复现。
5. **避免“AI 味”高频词**：如过度套路化的词组或机械性转折。
6. **长文先出大纲**：结构优先，再落地内容。
7. **严格对齐长期记忆**：术语、单位、关键事实以硬记忆为准。
8. **语法检查只做纠错**：除非用户明确要求重写。
9. **规范审计 (Spec Audit) 必须刚性**：检阅 Agent 若发现未满足 Spec，应直接打回 `failed_specs`，不可含糊通过。
10. **防御性写作必须走上中下三策**：遇到学术论文、实验、Discussion、Limitations 或 Rebuttal，必须先判断审稿人攻击的是核心贡献、证据链还是部署变量。优先使用上策：判断“这不是缺陷，这是特点”；若不成立，使用中策：分析缺点的原因、优化变量与工程边界；最后才用下策：rebuttal 兜底、补证据或降级 claim。若局限动摇核心创新，应建议补实验、补分析或降级 claim。

## 4. 知识库与参考文献学习（推荐流程）

### 写作知识库的使用方式
当前仓库支持通过配置与任务指令调用写作知识库（如基金、论文、学位论文）来增强结构与表达。建议流程：
1. **声明写作类型**：在任务或规范中明确是“基金/论文/学位论文”。
2. **提供参考文献要点**：用摘要、要点或引用列表提供给系统。
3. **沉淀稳定事实**：术语、单位、结论写入硬记忆。
4. **沉淀写作偏好**：措辞、语气、表达习惯写入软记忆。
5. **大纲先行**：基于知识库与参考要点先出大纲，再写正文。

### 参考文献学习建议
- 先整理“参考文献摘要/关键论点/可引用结论”。
- 按领域写入长期记忆，确保后续写作可复用。
- 对需要引用的内容明确标注来源与用途，避免误用。

### 参考文献学习链路
1. **采集**：接收用户提供的原文、摘要或要点清单。
2. **抽取**：提取事实、数据、术语、可引用片段与风格特征。
3. **入库**：写入 `reference_library.json` 并同步到硬/软记忆。
4. **引用**：写作时根据 Evidence Requirements 选取证据与引用格式。
5. **复核**：检阅阶段校验证据覆盖与引用数量。
6. **MinerU 路径**：当使用 MinerU 解析 PDF 时，先生成结构化 markdown/JSON 再抽取与入库。

## 5. 快速配置入口

- `style_profile.md`：个人风格指纹
- `error_log.md`：禁忌清单（负面约束）
- `custom_specs.md`：主题/受众/检测/阈值等全局配置
- `document_spec_template.md`：单点事实约束模板
- `outline_template.md`：含 DoD 的大纲结构模板
- `hard_memory.json` / `soft_memory.json`：长期记忆存储
- `reference_library.json`：参考文献库
- `reference_learning.md`：参考文献学习流程
- `pdf_ingestion_template.md`：PDF 入库模板
