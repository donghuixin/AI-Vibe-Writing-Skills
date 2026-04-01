# AI Vibe Writing Skill for Agent / AI 写作助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An AI Skill that provides "Style Transfer" and "Error Memory" capabilities for personalized writing.
> 
> 一个具备“风格迁移”和“错误记忆”功能的 AI 写作助手，打造你专属的“影子写手”。

## 🌟 What's New / 更新日志

**v1.8 - Next-Gen Architecture (Claude Code Inspired) / 下一代动态架构**
- **Context Compactor (上下文压缩器)**: 引入 `11_context_compactor_agent.md`，当 Token 溢出时自动压缩历史探讨，提取“核心论点骨架”与“风格快照”，根治长文本幻觉。
- **Dynamic Prompt Routing (主控路由)**: 引入 `12_router_agent.md`，基于 Prompt as Code 理念，根据正在编写的章节（如 Intro, Methodology）动态挂载微调指令切片，提高输出精度。
- **LaTeX Self-Healing Loop (编译自愈)**: 引入 `13_latex_self_healing_agent.md`，赋予智能体动态编写修复脚本的权限，通过“读日志->写脚本清理/修复->重新编译”的闭环，自主解决复杂的 BibTeX 与宏包冲突报错。

**v1.7 - Flow Appraisal / 心流鉴赏模块**
Added Flow Appraisal to the Review agent to assess reader “flow” and “excitement” states with actionable suggestions (Expectation–Response, Breadcrumb transitions, Cognitive load minimization, Aha moments, Candor).
为检阅智能体新增“心流鉴赏”能力，评估读者是否保持心流与兴奋状态，并给出可执行修订建议（期待-回应闭环、面包屑过渡、认知减负、顿悟、坦诚披露）。

**v1.6 - Spec-Driven Writing (Spec Coding) / 规范驱动写作**
Added `document_spec_template.md` and `Definition of Done (DoD)` enforcing mechanisms to guarantee engineering-grade accuracy and prevent unauthorized AI rewrites.
新增 `document_spec_template.md` 与 `DoD` (Definition of Done) 校验机制，确保工程级的高精度输出，杜绝 AI 擅自改写。

**v1.5 - PDF Reading & MinerU / PDF 阅读与 MinerU 集成**
Added `pdf-reader-agent` for deep PDF reading with `MinerU` integration.
Supported APA/IEEE citation formatting and reading quality scoring.
新增 `pdf-reader-agent` 支持深度 PDF 阅读与 `MinerU` 集成。
支持 APA/IEEE 引用格式化与阅读质量评分。

**v1.4 - Multi-Agent Writing Skill / 多智能体协作写作**
Added outline-manager, content-writer, content-review agents with a coordinator loop.
新增大纲管理、写作、检阅智能体与流程协调器，完成写作闭环。

**v1.3 - Writing Knowledge Bases / 写作知识库**
Added curated writing knowledge bases for grant proposals, papers, and theses.
新增基金、论文与学位论文写作知识库，支持按写作类型检索与应用。

**v1.2 - Long-Term Memory / 长期记忆**
Added domain-based hard/soft memory to preserve precise terms and user preferences.
新增按领域划分的硬性/柔性记忆，用于精准术语与偏好存储。

**v1.1 - Grammar & Spell Checker / 语法与拼写检查器**
Added a dedicated module to detect and correct grammatical errors and typos in both English and Chinese.
新增了专用的语法与拼写检查模块，支持中英文双语纠错。

## 🧠 Why I Exist / 设计初衷
本工程（AI-Vibe-Writing-Skills）的初衷，是跳出 “AI 替代创作” 的误区，聚焦于AI 的辅助价值
将写作从重复、机械的 “dirty work”（如素材整理、格式规范、基础校对、灵感初步筛选等）中解放出来，把精力聚焦在创意构思、内容深度打磨、风格个性化等核心环节，最终实现更高效率、更高质量的内容生产。

## 🧩 Core Capabilities / 核心功能

### 🎭 STYLE TRANSFER / 风格迁移
**Mimic**: Analyzes your past writings to extract "Style DNA".  
**Consistency**: Maintains your unique tone, sentence structure, and vocabulary.  
**原理**: 分析过往文章提取“风格指纹”，保持语调、句式和用词的一致性。

### 📑 SPEC-DRIVEN WRITING (SPEC CODING) / 规范驱动写作
**Document Spec**: The single source of truth for your writing task (core arguments, constraints).  
**Definition of Done (DoD)**: Strict checklists attached to outlines that the Writer and Reviewer must satisfy.  
**原理**: 借鉴 Spec Coding 思想，在起草前确认 Document Spec（客观事实来源），大纲中附加 DoD（验收标准），检阅阶段执行严格的规范审计（Spec Audit）。

### 🧠 ERROR MEMORY / 错误记忆
**Learning**: Remembers your corrections and "Don'ts".  
**Avoidance**: Automatically checks against the "Error Log" before writing.  
**原理**: 记住你的纠正和禁忌，在生成前自动查阅“错题本”以避免重犯。

### 📝 GRAMMAR CHECK / 语法检查
**Quality**: Built-in bilingual grammar and spell checker.  
**Review**: Identifies typos and awkward phrasing without changing your style.  
**原理**: 内置中英文双语语法检查，识别错别字和语病，同时保留原有风格。

### 🧠 LONG-TERM MEMORY / 长期记忆
**Hard Memory**: Stores exact terms, units, and key values by domain.  
**Soft Memory**: Stores preferences, phrasing, and tone by domain.  
**原理**: 硬性记忆用于术语、单位、关键数值的精确存储；柔性记忆用于偏好与表达习惯的持续适配。

### 📚 WRITING KNOWLEDGE BASES / 写作知识库
**Grant**: Reviewer-aligned structure, persuasion, and feasibility cues.  
**Paper**: Academic rigor, novelty framing, and LaTeX cleanliness.  
**Thesis**: Long-form clarity, topic sentences, and narrative flow.  
**原理**: 针对不同写作类型沉淀可复用规范，按领域检索并持续迭代。

### 🤝 MULTI-AGENT COLLABORATION / 多智能体协作写作
**Outline Manager**: Enforces outline constraints and validates outputs.  
**Writer**: Drafts and revises under outline and memory constraints.  
**Reviewer**: Detects AI tone and integrates multi-platform checks.  
**原理**: 通过大纲约束→内容创作→AI 味检测→多平台核验实现闭环。

### ⚙️ CUSTOMIZATION / 自定义规范
**Context**: Adapts to specific audiences (e.g., Technical, General) and topics.  
**Outline**: Manages structure for long-form content.  
**原理**: 自动适配目标受众和主题，支持长文大纲管理。



### Quick Trigger Examples / 快速触发示例
> "Use outline-manager-agent to generate a 3-level outline for topic X."
> 
> “调用大纲管理智能体，为主题 X 生成三级大纲。”

> "Use content-writer-agent to draft section 2 based on outline-001."
> 
> “调用写作智能体，基于 outline-001 写第 2 节。”

> "Use content-review-agent to review the latest draft and report AI tone."
> 
> “调用检阅智能体，检查最新草稿并输出 AI 味报告。”

> "Use workflow-coordinator to run the full multi-agent loop."
> 
> “调用流程协调器，执行完整多智能体闭环。”

##  How to Start / 如何开始使用

You can activate this system immediately by following these steps:
你可以立即尝试以下步骤来“激活”这个系统：

### Step 0: Installation (Mandatory) / 安装（必读）
**You MUST clone the full repository to use this system.** 
The system relies on the local `.ai_context` folder for memory, style profiles, and agent configurations. Without cloning, the agents cannot access your style or project settings.
**你必须克隆完整仓库才能使用本系统。**
系统依赖本地 `.ai_context` 文件夹来读取记忆、风格配置和智能体设置。如果不克隆，智能体将无法访问你的风格或项目设置。

```bash
git clone https://github.com/donghuixin/AI-Vibe-Writing-Skills.git
```
Open the cloned folder in your IDE (Trae, VS Code, Cursor) to activate the context.
克隆后在 IDE（Trae, VS Code, Cursor）中打开该文件夹以激活上下文。

### Step 1: Agent Selection / 智能体选择指南
Choose the right agent for your task. You don't always need all of them.
根据你的任务选择合适的智能体组合，不需要每次都全量开启。

| Goal / 目标 | Recommended Agents / 推荐智能体 | Why / 原因 |
| :--- | :--- | :--- |
| **Simple Writing** / 简单写作 | **Content Writer** | Direct drafting with style mimicry. <br> 直接生成，保留风格。 |
| **Long-form Content** / 长文创作 | **Outline Manager** + **Content Writer** | Ensures logical structure and flow. <br> 保证长文结构逻辑严密。 |
| **Quality Assurance** / 质量把控 | **Content Writer** + **Content Review** | Checks for AI tone and plagiarism. <br> 检测 AI 味和查重。 |
| **Full Automation** / 全自动闭环 | **Workflow Coordinator** | Orchestrates the full loop (Outline → Write → Review). <br> 自动调度全流程。 |

### Step 2: Style Extraction / 提取风格
**Required for first-time use.**
Provide 3-5 of your past high-quality writings to the AI.
**首次使用必须执行。**
把你的 3-5 篇过往高质量文章发给 AI，并说：

> "Please use the **Style Extractor** to analyze these texts and update `style_profile.md`."
>
> “请使用 **Style Extractor** 分析这些文章，并更新 `style_profile.md`。”

### Step 3: Customization / 配置规范
**Optional but recommended.**
Open `.ai_context/custom_specs.md` and fill in your common writing context.
**可选但推荐。**
你可以打开 `.ai_context/custom_specs.md`，填入你常用的写作背景，这样我每次写作都会自动适配这些背景。

Example / 例如：
- **Audience / 受众**: Technical Beginners / 技术小白
- **Domain / 领域**: Artificial Intelligence / 人工智能

### Step 4: The Writer / 日常写作
**Agent: Content Writer**
Just give a task. No need to repeat complex prompts.
直接发布任务即可，无需每次重复 Prompt。

> "Based on my style, write an introduction to RAG technology."
>
> “基于我的风格写一篇关于 RAG 技术的介绍。”

*I will automatically read `style_profile.md` to mimic your tone and check `error_log.md` to avoid taboos.*
*我会自动读取 `style_profile.md` 模仿你的语气，并检查 `error_log.md` 避开禁忌。*

### Step 5: Error Logger / 纠错迭代
If I make a mistake (e.g., use a word you dislike), correct me immediately.
如果我犯了错（比如用了你不喜欢的词），直接告诉我：

> "Don't use the word 'delve'. Add this to my error log."
>
> “不要用‘delve’这个词，把它加入错题本。”

*I will automatically update `error_log.md` to ensure I don't make the same mistake again.*
*我会自动更新 `error_log.md`，保证下次不再犯。*

### Step 6: Long-Term Memory / 长期记忆
Provide durable domain facts or preferences to store.
提供稳定的领域事实或偏好以便长期存储：

> "In medical writing, always use mmol/L for glucose. Save this as hard memory."
>
> “在医学领域，葡萄糖单位固定使用 mmol/L，作为硬性记忆存储。”

### Step 7: Writing Knowledge Bases / 写作知识库
Select a writing domain and apply the corresponding knowledge base.
选择写作类型并应用对应知识库：

> "Use the paper knowledge base and draft the Related Work with reviewer-style rigor."
>
> “调用论文知识库，以审稿人视角写 Related Work。”

### Step 7.5: Reference Learning / 参考文献学习
Provide references to build a local evidence library and reusable knowledge.
提供参考文献以构建本地证据库与可复用知识：

> "Learn these references and store facts, data, terms, and style."
>
> “学习这些参考文献并本地存储事实、数据、术语与风格。”

Configure evidence requirements in `.ai_context/custom_specs.md` and follow `.ai_context/reference_learning.md`.
在 `.ai_context/custom_specs.md` 中设置证据要求，并遵循 `.ai_context/reference_learning.md`。

### Step 7.7: PDF Reading / PDF 阅读
Read local or online PDFs and ingest structured evidence.
读取本地或在线 PDF 并入库结构化证据：

> "Use pdf-reader-agent to read this PDF and extract evidence."
>
> “调用 PDF 阅读智能体读取该 PDF 并提取证据。”

Configure PDF Reading Settings in `.ai_context/custom_specs.md`:
- **Citation Formatting**: APA / IEEE
- **Quality Scoring**: Enable/Disable
在 `.ai_context/custom_specs.md` 中配置 PDF Reading Settings（含引用格式化与质量评分）。

Use `.ai_context/pdf_ingestion_template.md` for standardized ingestion.
使用 `.ai_context/pdf_ingestion_template.md` 进行标准化入库。

If `PDF Engine` is set to mineru, the agent will parse PDFs into structured markdown/JSON before extracting evidence.
若 `PDF Engine` 设为 mineru，智能体将先解析为结构化 markdown/JSON 再抽取证据。

### IDE Integration / IDE 接入方式

**Antigravity (Recommended for Automation) / Antigravity (自动化首选)**
- 在对话中直接输入指令触发完整工作流：
  - 输入 `/ai_vibe_writing` 自动执行大纲生成、内容创作与检阅闭环。
  - 输入 `/pdf_ingestion` 自动解析本地/网络 PDF 并提取结构化证据入库。
- 系统会在 `.agents/workflows/` 中读取标准化的执行步骤，无需手动干预。

**Trae**
- 将本仓库作为工作区打开
- 调用 pdf-reader-agent 并提供本地路径或在线 PDF URL

**Cursor**
- 在项目中打开 PDF 文件或粘贴 URL
- 使用指令调用 pdf-reader-agent 生成 Summary 与入库计划

**Claude Code**
- 将 PDF 路径或 URL 作为输入交给 pdf-reader-agent
- 让智能体输出结构化摘要与 reference_library 更新计划

**VS Code**
- 打开工作区并粘贴 PDF 路径或 URL
- 调用 pdf-reader-agent 读取并输出结构化证据

**MinerU (Optional)**
- 使用 MinerU 将 PDF 转为 markdown/JSON
- 将结果交给 pdf-reader-agent 做结构化证据与入库

### Step 7.6: Context Budget / 上下文预算
Set a context budget to keep writing performance stable.
设置上下文预算以保证写作性能稳定：

1. **Max Context Tokens**: 上下文上限
2. **Target Utilization**: 建议使用率
3. **Min Useful Tokens**: 最低有效内容
4. **Compression Strategy**: 压缩策略

Configure in `.ai_context/custom_specs.md`.
在 `.ai_context/custom_specs.md` 中配置。

### Step 8: Multi-Agent Collaboration / 多智能体协作
**Agents: Workflow Coordinator / Outline Manager / Content Writer / Content Review**
Trigger the multi-agent loop and let the system orchestrate writing.
启动多智能体闭环并交由系统协调：

> "Use outline-manager-agent + content-writer-agent + content-review-agent to draft section 2."
>
> "调用大纲管理、写作、检阅三智能体完成第 2 章。"

### Step 9: API Key Configuration / API Key 配置
**Agent: Content Review**
**Ready for AI & Plagiarism Detection.**
The system is pre-configured to support **GPTZero**, **Copyleaks**, and other detection APIs. You just need to add your API key.
**已预置 AI 与查重检测能力。**
系统已预配置支持 **GPTZero**、**Copyleaks** 等检测 API。你只需填入 API Key 即可启用。

1. **Open configuration file**: `.ai_context/custom_specs.md`
2. **Find API Keys section**: Look for "Detector API Keys"
3. **Configure keys**:
   - **GPTZero**: Set your GPTZero API Key (e.g., `env:GPTZERO_API_KEY`)
   - **Other services**: Set keys for Originality, Copyscape, Turnitin, etc.
4. **Environment variables**: Set the actual API keys in your environment

> "Set GPTZero API key in custom_specs.md and environment"
>
> "在 custom_specs.md 中设置 GPTZero API Key 并配置环境变量"

*Note: The system will ask for confirmation before using paid services like GPTZero.*
*注意：系统在使用 GPTZero 等付费服务前会请求用户确认。*

> **Tip**: Looking for free alternatives? Check out [FREE_AI_DETECTION_APIS.md](./FREE_AI_DETECTION_APIS.md) for a curated list of free AI detection APIs (Copyleaks, Sapling, etc.).
>
> **提示**：寻找免费替代方案？查看 [FREE_AI_DETECTION_APIS.md](./FREE_AI_DETECTION_APIS.md) 获取精选的免费 AI 检测 API 列表（如 Copyleaks, Sapling 等）。

---

## 📂 File Structure / 文件结构

- **`FREE_AI_DETECTION_APIS.md`**: Guide to free AI detection APIs.
- **`.ai_context/`**: The brain of the system.
  - `style_profile.md`: Your style fingerprint.
  - `error_log.md`: Your negative constraints.
  - `custom_specs.md`: User-defined writing context.
  - `document_spec_template.md`: Template for single source of truth document spec.
  - `outline_template.md`: Template for structuring content with Definition of Done (DoD).
  - `reference_learning.md`: Reference learning pipeline.
  - `pdf_ingestion_template.md`: PDF ingestion template.
  - `memory/hard_memory.json`: Domain hard memory (terms, units, key values).
  - `memory/soft_memory.json`: Domain soft memory (preferences, phrasing, tone).
  - `memory/reference_library.json`: Local reference library.
  - `prompts/`: Core logic prompts.
    - `1_style_extractor.md`
    - `2_writer.md`
    - `3_error_logger.md`
    - `4_grammar_checker.md`
    - `5_long_term_memory.md`
    - `6_outline_manager_agent.md`
    - `7_content_writer_agent.md`
    - `8_content_review_agent.md`
    - `9_workflow_coordinator.md`
    - `10_pdf_reader_agent.md`
    - `11_context_compactor_agent.md`
    - `12_router_agent.md`
    - `13_latex_self_healing_agent.md`
- **`.traerules`**: System instructions ensuring the workflow is followed.

## 🗺️ Functional Structure / 功能结构

```mermaid
graph TD
    A[用户写作请求 / User Request] --> B{分析阶段 / Analysis Phase}
    B --> C[Style Extractor
    <br />风格提取器]
    B --> D[Custom Specs
    <br />自定义规范]
    B --> P[Long-Term Memory
    <br />长期记忆]
    
    C --> E[Style Profile
    <br />风格库]
    D --> F[Outline Template
    <br />大纲模板]
    
    A --> G{存储阶段 / Storage Phase}
    G --> E
    G --> H[Error Log
    <br />错题本]
    G --> Q[Hard Memory
    <br />硬性记忆]
    G --> R[Soft Memory
    <br />柔性记忆]
    
    A --> I{生成阶段 / Generation Phase}
    I --> DS[Document Spec
    <br />写作规范约束]
    DS --> J[The Writer
    <br />写作引擎]
    I --> K[Grammar Checker
    <br />语法检查器]
    I --> S[Memory Recall
    <br />记忆检索]
    
    J --> L[生成内容 / Generated Content]
    K --> L
    S --> L
    
    L --> M{迭代阶段 / Iteration Phase}
    M --> N[用户反馈 / User Feedback]
    N --> O[Error Logger
    <br />错误记录器]
    O --> H
    O --> Q
    O --> R
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#9f9,stroke:#333,stroke-width:2px
    style H fill:#ff9,stroke:#333,stroke-width:2px
    style E fill:#9ff,stroke:#333,stroke-width:2px
```

**Core Logic / 核心逻辑**: 
**分析（提取风格） -> 存储（建立风格库与错题本） -> 生成（RAG 检索增强） -> 迭代（更新错题本）**

**Workflow Explanation / 流程说明**:
1. **Analysis & Spec Definition**: The system analyzes user requirements, extracts style traits, and creates a `document_spec.md` as the single source of truth.
2. **Storage**: Hard memory and soft memory are stored by domain alongside the style profile and error log.
3. **Generation**: The Writer strictly adheres to the `Definition of Done (DoD)` defined in the outline and retrieves relevant hard/soft memory. The Grammar Checker ensures spelling/grammar quality.
4. **Iteration**: The Reviewer audits the draft against the `document_spec.md`. Any failure forces a rewrite. User feedback updates both the error log and long-term memory.
## 🧩 Agent Role Configuration Tutorial / 智能体角色配置教程
This tutorial shows how to configure each agent role using existing prompt and spec files.  
以下教程演示如何通过现有的 prompt 与规范文件配置各智能体角色。

### 1) Outline Manager Agent / 大纲管理智能体
**Purpose / 作用**: Create, store, and validate outlines. / 创建、存储并校验大纲。  
**Where to edit / 编辑位置**:
- `.ai_context/prompts/6_outline_manager_agent.md`
- `.ai_context/outline_template.md`
- `.ai_context/custom_specs.md`

**Configuration Steps / 配置步骤**:
1. **Define Structure**: Open `.ai_context/outline_template.md` and define your preferred outline JSON structure (sections, paragraphs, word ranges).
2. **Set Validation Rules**: In `.ai_context/custom_specs.md`, adjust outline validation thresholds:
   - `Word Deviation Tolerance`: Acceptable deviation from word count targets (e.g., 0.1 for 10%).
   - `Core Point Coverage`: Minimum percentage of core points that must be covered (e.g., 0.9).
3. **Configure Storage**: (Optional) In `6_outline_manager_agent.md`, modify the outline storage key format if needed.

### 2) Content Writer Agent / 写作智能体
**Purpose / 作用**: Draft and revise content based on outline and memory. / 按大纲与记忆写作与修订。  
**Where to edit / 编辑位置**:
- `.ai_context/prompts/7_content_writer_agent.md`
- `.ai_context/custom_specs.md`
- `.ai_context/memory/hard_memory.json`
- `.ai_context/memory/soft_memory.json`

**Configuration Steps / 配置步骤**:
1. **Set Writing Context**: In `.ai_context/custom_specs.md`, define `Target Audience` and `Topic` to guide the writer's tone and depth.
2. **Configure Revision Limits**: In `.ai_context/custom_specs.md`, set `Max Revision Rounds` to control how many times the writer can iterate on a draft.
3. **Populate Memory**:
   - Add domain facts (terms, units) to `.ai_context/memory/hard_memory.json`.
   - Add style preferences (phrasing, tone) to `.ai_context/memory/soft_memory.json`.
4. **Output Format**: (Optional) In `7_content_writer_agent.md`, customize the content output format and metadata fields if specific metadata is required.

### 3) Content Review Agent / 检阅智能体
**Purpose / 作用**: Detect AI tone and aggregate platform checks. / AI 味检测与多平台核验。  
**Where to edit / 编辑位置**:
- `.ai_context/prompts/8_content_review_agent.md`
- `.ai_context/custom_specs.md`

**Configuration Steps / 配置步骤**:
1. **Configure GPTZero MCP (New!)**:
   - The agent now supports GPTZero via MCP for AI detection and plagiarism checking.
   - **Code Reference**: [8_content_review_agent.md](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/.ai_context/prompts/8_content_review_agent.md#L1-L120)
2. **Set API Keys & Settings**:
   - Open `.ai_context/custom_specs.md`.
   - Fill in `GPTZero MCP` settings: Service Name, Method, Timeout, and Retry count.
   - Set your `GPTZero API Key`.
   - **Code Reference**: [custom_specs.md](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/.ai_context/custom_specs.md#L1-L60)
3. **Usage**: When you trigger "Review" or "Detection", the agent will automatically call GPTZero via MCP and include the results (AI probability, Plagiarism score) in the unified report.
4. **Adjust Thresholds**: In `.ai_context/custom_specs.md`, set `AI Tone Threshold` to determine when a rewrite is triggered.
5. **Enable Flow Appraisal / 开启心流鉴赏**:
   - Set thresholds in **Flow Appraisal Settings**: Min Flow Score, Min Excitement Score, and requirements for Killer Figure 1, Intuition-before-Formula, Signposting, Topic Sentence.
   - The Review agent will output `flow_appraisal` with scores, missing elements, rationale, and actionable suggestions.
   - **Code Reference**: [8_content_review_agent.md](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/.ai_context/prompts/8_content_review_agent.md#L43-L120), [custom_specs.md](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/.ai_context/custom_specs.md#L26-L40)

### 4) Workflow Coordinator / 流程协调器
**Purpose / 作用**: Orchestrate outline → write → review loops. / 协调整体闭环流程。  
**Where to edit / 编辑位置**:
- `.ai_context/prompts/9_workflow_coordinator.md`
- `.ai_context/custom_specs.md`

**Configuration Steps / 配置步骤**:
1. In `9_workflow_coordinator.md`, set the loop order and max revision rounds.
2. In `custom_specs.md`, align coordination rules with your writing cadence.

## 🧭 Multi-Agent Skill IDs / 多智能体 Skill ID
- **outline-manager-agent**
- **content-writer-agent**
- **content-review-agent**
- **workflow-coordinator**
- **context-compactor-agent**
- **router-agent**
- **latex-self-healing-agent**

## 🔄 Multi-Agent Workflow / 多智能体协作流程

```mermaid
graph TD
    Start([Start / 开始]) --> Coordinator[Workflow Coordinator
    <br />流程协调器]
    
    Coordinator -->|1. Spec & Outline| OutlineMgr[Outline Manager
    <br />大纲管理智能体]
    OutlineMgr -->|Save to Memory| HardMem[(Hard Memory
    <br />硬性记忆)]
    OutlineMgr -->|Valid Outline w/ DoD| Coordinator
    
    Coordinator -->|2. Draft Section| Writer[Content Writer
    <br />写作智能体]
    HardMem -.->|Read Outline| Writer
    Writer -->|Draft or Revision Plan| Coordinator
    
    Coordinator -->|3. Spec Audit & Review| Reviewer[Content Review
    <br />检阅智能体]
    Reviewer -->|Check| MCP[GPTZero MCP]
    
    Reviewer -->|Result| Decision{Pass Spec & Tone? / 规范与语气通过?}
    
    Decision -->|Yes| Finish([Finish / 完成])
    Decision -->|No: Revise / 修订| Writer
    
    style Coordinator fill:#f96,stroke:#333,stroke-width:2px
    style OutlineMgr fill:#9cf,stroke:#333,stroke-width:2px
    style Writer fill:#9f9,stroke:#333,stroke-width:2px
    style Reviewer fill:#fc9,stroke:#333,stroke-width:2px
```


## 🛡️ AI 写作检测方案

### 1. 在线 API 检测 (Content Review Agent)
通过 `content-review-agent` 集成第三方 API（如 GPTZero, Copyleaks）进行实时检测。
配置方式请参考 [Step 9: API Key Configuration](#step-9-api-key-configuration-api-key-配置)。

### 2. 本地离线检测 (Local AI Style Check)
本仓库提供了一套完全离线、隐私安全的本地检测方案，专为 LaTeX 论文源码设计。
它结合了高频 AI 词汇扫描（中英文）与困惑度（PPL）计算，精准定位 AI 润色痕迹。

**使用方法**:
1. 进入检测工具目录: `cd Local_AI_Style_Check`
2. 安装依赖: `pip install -r requirements.txt`
3. 运行检测脚本: `python paper_ai_detector.py`

**功能亮点**:
- **双重 LaTeX 清洗**: 正则 + AST 解析，完美剥离公式与引用，只检测正文。
- **高频词扫描**: 内置 "delve", "tapestry", "赋能", "重塑" 等 40+ 个中英文 AI 惯用词库。
- **PPL 困惑度分析**: 本地运行 distilgpt2 模型，量化文本的“机器生成概率”。

详细指南请查阅 [Local_AI_Style_Check/README.md](./Local_AI_Style_Check/README.md)。

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=donghuixin/AI-Vibe-Writing-Skills&type=Date&cache=20260222)](https://star-history.com/#donghuixin/AI-Vibe-Writing-Skills&Date)
If the chart looks stale, update the cache parameter to force refresh.
如果图表显示滞后，可更新 cache 参数以强制刷新。

## 🧾 MinerU 安装与配置流程
- 环境准备（macOS）  
  - 安装 Python 3.9（建议使用官方安装包或 pyenv）  
  - 在项目根目录创建并启用虚拟环境：
  
  ```bash
  python3 -m venv mineru_venv
  source mineru_venv/bin/activate
  ```
- 安装依赖（尽量避免版本冲突）  
  - 安装 PyTorch（根据你的 CUDA/CPU 环境选择官方轮子）：https://pytorch.org  
  - 安装核心库：
  
  ```bash
  pip install -U pip wheel setuptools
  pip install magic-pdf gradio ultralytics onnxruntime ftfy
  pip install transformers==4.57.6
  ```
  - Detectron2（macOS 推荐源码安装）：
  
  ```bash
  pip install 'git+https://github.com/facebookresearch/detectron2.git'
  ```
- 配置文件与约束文件  
  - 复制布局模型推理配置到本仓库：  
    - 已提供 [layoutlmv3_base_inference.yaml](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/configs/layoutlmv3_base_inference.yaml)  
    - 将其放置到你的虚拟环境中 magic-pdf 的资源路径：  
  
  ```bash
  cp configs/layoutlmv3_base_inference.yaml \
     mineru_venv/lib/python3.9/site-packages/magic_pdf/resources/model_config/layoutlmv3/layoutlmv3_base_inference.yaml
  ```
  - 本仓库提供 [magic-pdf.json](file:///Users/huixin/Documents/ProgramDevelopment/AI_Vibe_Writing_Skill/magic-pdf.json) 作为运行配置示例，其中已关闭表格识别以避免缺失 OCR 权重导致崩溃：
    - table-config.is_table_recog_enable: false
- 兼容性补丁（仅当出现下述错误时执行）  
  - 若出现 `Cannot import torch_int` 或 `find_pruneable_heads_and_indices` 相关错误：  
    - 升级到 `transformers==4.57.6`（上文已安装）  
    - 将 `modeling_layoutlmv3.py` 中对 `find_pruneable_heads_and_indices` 的导入移除  
    - 在 `layoutlmv3/backbone.py` 中为 `images` 输入添加 `Tensor` 分支（避免 `Tensor.__contains__` 断言）  
    - 补丁方式：直接在你虚拟环境的 `site-packages/magic_pdf/` 对应文件进行最小修改
- 运行方式  
  - 命令行（文本模式）：
  
  ```bash
  magic-pdf -p ./test.pdf -o ./output -m txt
  ```
  - 图形界面（Gradio）：
  
  ```bash
  python mineru_gui.py
  # 浏览器访问 http://127.0.0.1:7860
  ```
- 模型文件与体积约束  
  - 已将 `.gitignore` 配置为不上传完整模型与本地虚拟环境（空间受限场景友好）  
  - 如需启用表格识别或 OCR，请自行下载对应权重并在 `magic-pdf.json` 中启用相关开关

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
