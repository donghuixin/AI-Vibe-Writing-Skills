# AI Vibe Writing Skills

Academic writing skills for author voice, evidence-based arguments, and reviewer responses.

把作者习惯、论文证据和修稿记录保存在文件中，让 Agent 在多轮写作里继续使用。适合既有稿件的局部修改、系统论文的论证整理，以及期刊修订和审稿回复。

从 [SKILL.md](SKILL.md) 进入；完整能力见 [SKILLS.md](SKILLS.md)。指令、模板和可选本地工具分别组织，按当前任务读取。

## 从你的任务开始

| 现在要做什么 | 入口 | 得到什么 |
|---|---|---|
| 只改语法或错字 | [Grammar Checker](.ai_context/prompts/4_grammar_checker.md) | 保留含义和语气的最小修改 |
| 学习自己的语气，再修改一段话 | [Style Extractor](.ai_context/prompts/1_style_extractor.md) + [Writer](.ai_context/prompts/2_writer.md) | 有样本依据的风格记录、改句及理由 |
| 整理长文或多章修订 | [Workflow Coordinator](.ai_context/prompts/9_workflow_coordinator.md) | 按所需步骤推进的规范、大纲和稿件 |
| 检查 MobiCom / SenSys 等系统论文 | [Systems Paper Logic](.ai_context/prompts/15_systems_paper_logic_agent.md) | 问题、洞察、设计、实验和适用范围的对应关系 |
| 评估局限与审稿风险 | [Defensive Writing](.ai_context/prompts/14_defensive_writing_agent.md) | 有位置、有证据、范围适当的处理建议 |
| 修改 response letter | [Response Letter](.ai_context/prompts/16_response_letter_agent.md) | 原意见覆盖、作者口吻回覆、修改位置和待确认项 |
| 读论文并整理支持证据 | [PDF Reader](.ai_context/prompts/10_pdf_reader_agent.md) | 来源、页图位置、支持范围与未核验项 |

## 快速开始

```bash
git clone https://github.com/donghuixin/AI-Vibe-Writing-Skills.git
```

在支持本地文件上下文的 Agent 或 IDE 中，提供仓库的 `SKILL.md` 路径，以及要修改的稿件。已有论文工程继续使用原目录和构建方式。

例如：

> 读取 AI-Vibe-Writing-Skills/SKILL.md。按这两段作者原稿的语气修改 response.tex，保留 reviewer 原文、技术术语、公式和引用。先回答实际问题，已完成修改才用完成式，未知结果留短标记。给我修改后的 LaTeX 和必要核对项。

或者：

> 只检查 Introduction 和 Design 是否对得上。沿用已有图表与数据，指出哪条主张没有解释或证据。先使用现有材料，不默认重做所有实验。

仅改一句语法时，直接提供句子即可，无需建立完整Spec或运行全部模块。

## 作者语气怎么保留

先区分作者自己的文本、合著稿、他人范文和经过编辑的版本，再记录有来源的习惯。作者确认与样本推断分开；论文正文与response letter也分开。

- 保留作者常用的系统、模块和动作称呼，让具体机制承担解释。
- 技术术语可以重复，不为换词把 goodput 写成另一种指标，或把 orthogonal 换成不准确的近义词。
- 模板感落到句子检查：冗余致谢、空泛修饰、无作用的转折，以及混入正文的内部审计语气。
- 语法错误和过强结论照常修正。没有作者样本时采用普通、清楚的写法，不声称已经学得个人风格。

风格档案使用 [style_profile.md](.ai_context/style_profile.md)。通用建议单列在 [writing-guidelines.md](docs/writing-guidelines.md)，不当作作者的历史偏好或禁词表。

## 论证围绕证据组织

系统论文保留已有的 C/H/D/E/B 工作表：贡献（Claim）、挑战（Challenge）、设计（Design）、证据（Evidence）和范围（Boundary）。每条主张关联实际图表、数据、配置或推导，并记录 `supported / partial / missing / contradicted`。

读者应能看清：问题为什么值得研究，设计为什么能处理这个问题，实验实际支持什么结论。无线、移动系统、感知和部署论文按各自主张选择检查，不强制相同的硬件、实验数量或章节配方。

[系统论文工作表](.ai_context/systems_paper_logic_template.md)沿用原来的ID；response和内容审计引用同一份证据，不各自生成不同口径。文献身份、原文是否支持陈述、本文结果是否成立，按 [参考学习流程](.ai_context/reference_learning.md) 分别核对。

## Response letter 的处理

1. **读原始决定信和完整意见。** 保留总评、编号评论、子问题和结语，核对旧回覆有无漏项。实际决定信与当前阶段规则优先于旧摘要和通用清单。
2. **辨别问题强度。** 询问是否测试先回答是否；either/or保留替代路径。审稿要求、可选建议、作者要求和内部核查分开，minor revision不自动扩大为全面重测。
3. **用作者口吻回答。** 先给直接答案，再给必要证据或解释，最后定位确已完成的改动。简单错字短答，技术问题按需要展开。
4. **如实记录进度。** 已有数据、估算、拟修订文字和待确认结果分开。源码检查、编译、PDF视觉检查各自报告，不能用其中一个替代其他验证。

工作表见 [revision_response_template.md](.ai_context/revision_response_template.md)。缺少源码或结果时仍可交付工作稿，保留可见待确认项；不会把“计划补充”改写成“已经完成”。

## 文件放在哪里

```text
AI-Vibe-Writing-Skills/        # 共享技能资源
  SKILL.md                    # 任务入口
  SKILLS.md                   # 能力索引
  .ai_context/
    prompts/                  # 1–16号指令；保留既有路径
    *_template.md             # 需要时复制到论文工作区
    style_profile.md          # 空白作者档案模板
    memory/                   # 空白项目记忆模板
    scripts/parse_pdf.py      # 可选PDF文字提取
  .agents/workflows/          # 可选工作流入口
  Local_AI_Style_Check/       # 离线、只读的候选句检查
  docs/                       # 方法来源、迁移与写作建议
  scripts/                    # 仓库资源检查
  tests/                      # 工具测试与合成行为案例

your-paper/                   # 作者论文工作区
  main.tex
  .ai_context/
    document_spec.md
    style_profile.md
    systems_paper_logic.md    # 系统论证任务需要时建立
    revision_response.md      # 正式回覆任务需要时建立
    memory/
```

沿用作者已有的工作区位置；无需为局部修改创建所有文件。私人稿件、评审、数据和样本留在作者工作区，共享仓库只保存可复用指令、空模板和合成案例。

`.traerules`与`.agents/workflows`保留为薄入口。已有授权的修改直接执行；缺少会改变研究结论的事实时标记待核实，完成其他有材料支持的工作。

## 可选本地工具

[Local Style Lint](Local_AI_Style_Check/README.md)定位冗余或模板表达的候选句，返回文件、行号、片段与原因。它只读文件，不自动替换，不下载语言模型，也不判断文字作者或抄袭率。旧 `paper_ai_detector.py` 保留命令入口，迁移见 [说明](docs/migration.md)。

[parse_pdf.py](.ai_context/scripts/parse_pdf.py)使用可选的 `pypdf` 提取本地PDF文字。提取成功不代表图表、公式或引文支持关系已经核验。原有MinerU辅助脚本仍保留，按实际复杂布局需要配置，不是写作技能的必需依赖。

## 验证

在仓库根目录运行：

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -p "test_*.py" -v
```

自动检查覆盖资源链接、数据样例和本地工具行为。另用 [系统逻辑案例](tests/systems_paper_logic_cases.md) 与 [修订／作者语气案例](tests/revision_voice_cases.md) 做独立试用：只给输入，随后检查实际输出。未逐案执行的案例不记作通过；这些检查也不等于论文录用效果评估。

已完成的六个合成试用及其实际表现见 [试用记录](tests/writing_trial_record.md)。GitHub Actions 在 Linux 与 Windows 上执行资源校验和工具测试。

## 方法来源与迁移

本轮学习了 Orchestra 的系统论证、ARIS 的主张与证据对应、MobiCom-Skills 的量测条件，以及局部精修和可定位评论的方法；具体采用与取舍见 [方法记录](docs/research/adopted-writing-patterns.md)。此前的固定版本比较与官方规则核验保留在 [MobiCom／SenSys调研](docs/research/mobicom-sensys-writing-skills.md)。

[迁移说明](docs/migration.md)解释旧评分配置、三策顺序、记忆模板和命令入口的变化。投稿日期、页数和rebuttal规则仍按目标年份、track和阶段查证，不从其他项目永久继承。

## License

[MIT](LICENSE)
