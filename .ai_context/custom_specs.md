# Project Settings

这是项目配置模板。只填写本次需要的项，未填写不阻止局部修改。实例放在作者的论文工作区。已有用户指令与授权优先于这里的默认建议。

## Task
- **Topic / Audience**:
- **Deliverable**: manuscript / response_letter / outline / local_edit / reading_notes
- **Requested Scope**: 文件、章节或段落；是否仅语法
- **Available Inputs / Missing Inputs**: 原稿、可编辑源码、数据、图表、review、decision letter
- **Output Language / Format**:
- **Max Revision Rounds**: 3；只有新修改或未解决问题才继续，不为用满轮次重复检查

## Author Voice
- **Author Samples**: 文件、版本与位置；区分作者原稿和其他人的范文
- **Genre**: paper / response_letter / thesis / grant
- **Author-Confirmed Preferences**:
- **Observed Tendencies**: 附样本与可信度；未确认观察不变成永久禁令
- **Terms / Symbols To Preserve**:
- **Style Review Output**: 原句、位置、具体原因、最小改句；不输出AI作者概率或风格总分

## Evidence And References
- **Citation Style**: 稿件现有样式，或目标venue的明确要求
- **Evidence Worksheet**: 系统论文使用 `.ai_context/systems_paper_logic.md`；已有表格可沿用
- **Required Sources**: 与实际主张相关的来源，不设通用最少引用数或覆盖率门槛
- **Evidence States**: supported / partial / missing / contradicted
- **Evidence Types**: measured / derived / estimated / literature / author_reported
- **Source Detail**: 页码、图表、数据与配置版本、访问范围
- **Reference Library**: `.ai_context/memory/reference_library.json`

## Systems Paper Logic Settings
- **Mode**: auto
- **Mode Meaning**: auto仅用于系统论文论证、结构或实验解释；on显式检查；off跳过。仅语法不自动触发。
- **Contribution Type**: mechanism / system / measurement / dataset / theory / experience
- **Logic Worksheet**: `.ai_context/systems_paper_logic.md`
- **Target Venue / Year / Track / Stage**:
- **Official Sources / Checked At / Unresolved Policy Items**:
- **Domain Checks**: 按主张选择无线、移动系统、感知或部署检查，不强制同一套实验

## Reviewer Response
- **Decision Letter / Reviewer Source**: 逐字原文、版本与位置
- **Decision / Round**: 依原信填写，不从评论数量推测决定
- **Deadline / Timezone**: 未给具体时刻就保留未知，不默认为当日结束
- **Requirement Source**: editor / reviewer / author_request / internal_check
- **Response Matrix**: `.ai_context/revision_response.md`；使用对应模板或已有表格
- **Submission State**: draft / revised_in_source / compiled / visually_checked；分别记录
- **Pending Marker**: 如 `[AUTHOR CHECK: ...]`，未解决内容保持可见

## Review And Limitations
- **Review Depth**: 与任务、主张风险和证据缺口相称
- **Finding Format**: 位置、问题、证据、影响、最小处理方式
- **Response Choice**: 澄清 / 纠正 / 收窄 / 补分析或实验 / 有依据地不同意
- **Strategy Rule**: 先判断事实与主张，再选处理方式；不预设先把限制包装成优点
- **Optional Local Tool**: `Local_AI_Style_Check/style_lint.py`；候选问题由作者语境裁定
- **External Text Services**: 默认不调用；外发稿件须符合用户已有授权与服务的实际能力

## PDF And LaTeX
- **PDF Engine / Reading Scope**: 已有本地工具；复杂版面可选MinerU；记录未读区域
- **Source / Main File / Build Command / Available Tools**:
- **Verification**: 源码结构、编译日志、最终PDF版面分别检查；无引擎可交付源码并说明未编译
- **Cleanup**: 只处理已确认可再生的构建产物，不把所有 `.bbl` 当作可删除缓存

## Context Management
- **Context Budget**: 由承载工具和任务决定，不设通用最少token量
- **Compact When Needed**: 保留事实来源、作者确认、有效决策、未解决项与授权

旧AI Tone、Flow、Excitement、PPL阈值及`upper_first`不再驱动重写，见 `docs/migration.md`。
