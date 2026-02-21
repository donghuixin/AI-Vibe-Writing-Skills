# 写作技艺总览（Skills）

本文件汇总当前仓库中所有写作能力、核心提示词（prompts）与写作注意事项，并梳理知识库与参考文献学习的使用方式，便于用户快速理解和配置。

## 1. 系统级写作流程（必须遵循）

工作流来自系统规则，贯穿所有写作任务：
1. **分析**：读取 `style_profile.md` 与 `custom_specs.md`，明确语气、主题、受众与约束。
2. **召回**：读取 `error_log.md` 与长期记忆，避免已知错误并对齐领域术语。
3. **规划**：对长文或复杂任务先出大纲（参考 `outline_template.md`）。
4. **写作**：按风格与约束生成内容。
5. **自检**：排查 AI 味、错题本违例、语法问题。
6. **迭代**：根据反馈更新错题本与长期记忆。

参考配置入口：
- `.traerules`
- `.ai_context/style_profile.md`
- `.ai_context/error_log.md`
- `.ai_context/custom_specs.md`
- `.ai_context/outline_template.md`
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
- **流程协调器**（9_workflow_coordinator）：串联大纲 → 写作 → 检阅的闭环流程。
- **PDF 阅读智能体**（10_pdf_reader_agent）：读取本地/在线 PDF 并入库参考文献与证据。

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

## 3. 写作注意事项（高优先级规则）

1. **必须读取风格与错题本**：避免风格漂移与历史错误复现。
2. **避免“AI 味”高频词**：如过度套路化的词组或机械性转折。
3. **长文先出大纲**：结构优先，再落地内容。
4. **严格对齐长期记忆**：术语、单位、关键事实以硬记忆为准。
5. **语法检查只做纠错**：除非用户明确要求重写。
6. **检阅阶段独立执行**：AI 味检测与查重输出需独立报告。

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

## 5. 快速配置入口

- `style_profile.md`：个人风格指纹
- `error_log.md`：禁忌清单（负面约束）
- `custom_specs.md`：主题/受众/检测/阈值等全局配置
- `outline_template.md`：大纲结构模板
- `hard_memory.json` / `soft_memory.json`：长期记忆存储
- `reference_library.json`：参考文献库
- `reference_learning.md`：参考文献学习流程
