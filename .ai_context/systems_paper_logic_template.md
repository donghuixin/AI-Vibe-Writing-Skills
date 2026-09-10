# Systems Paper Logic Worksheet

以下工作表实例和项目配置路径均相对作者的论文 workspace；模板与提示词链接相对 skill 仓库。沿用项目已有位置，私有稿件、评审与证据不写入共享 skill 仓库。

本文件是模板。完整项目写作时填入 `.ai_context/systems_paper_logic.md`；局部检查可直接输出。`unknown` 表示尚无材料，不等于没有风险；ID 仅用于追踪，不写入论文正文。

## Scope & Venue Check

- **Manuscript / Spec Version**:
- **Task Scope**: full_paper / outline / section / rebuttal
- **Contribution Type**: mechanism / system / measurement / dataset / theory / experience
- **Venue / Year / Track / Stage**:
- **Official Sources / Checked At**:
- **Verified Rules**:
- **Unresolved Policy Items**:
- **Available Materials / Missing Sections**:

## One-Sentence Story

在 [场景与约束] 下，[有证据的现有瓶颈] 阻碍 [任务目标]；基于 [观测或洞察]，我们采用 [机制或研究方法]，[已有证据] 支持其在 [边界] 内的 [具体贡献]。

## Logic Chain

| Node | Content | Source / Location | Status |
| :--- | :--- | :--- | :--- |
| Scenario & objective | | | |
| Prior gap & challenge H1 | | | |
| Observation / insight | | | |
| Design D1 & implementation | | | |
| Evidence E1 | | | |
| Boundary B1 & reusable knowledge | | | |

## Claim-Evidence Ledger

| Claim ID & Exact Wording | Metric / Comparator / Conditions | H / D IDs | E IDs & Source Location | B IDs & Impact | Evidence Status | Allowed Wording / Next Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1 | | | | | missing | |

证据状态：`supported`（有证据支撑所述范围）、`partial`（只支持部分范围）、`missing`、`contradicted`。再写明证据种类：实测、模型估计、理论推导或文献。状态必须基于查看过的材料，不以作者语气或引用数量判断。

## Evidence Register

| E ID | Research Question / Claim | Design / Baseline / Controls | Independent Unit / Repeats / Uncertainty | Source Figure / Data / Config / Script | Result Type & Remaining Confounders |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E1 | | | | | |

## Section Contracts

| Section | Required Input | Question To Answer | Output To Next Section | Claim IDs / DoD |
| :--- | :--- | :--- | :--- | :--- |
| Introduction | 场景、前作、已有结果 | 问题为何重要，贡献究竟是什么？ | 待解释的 H 与 C | |
| Design / Analysis | H 与支撑洞察的证据 | 为什么选择 D，它如何工作？ | 实现接口与待验证命题 | |
| Evaluation | C、D、测量定义 | 是否有效、为何有效、代价与边界？ | E 与 B | |
| Discussion | E、B 与反证 | 哪些可迁移、哪些仍未知？ | 校准后的贡献与后续问题 | |

按实际贡献增删章节。每节可关联多条 claim。

## Breakpoints & Repair Plan

| Location | Severity | Broken Link / Affected C | Writing Repair Or Evidence Needed | Completion Check |
| :--- | :--- | :--- | :--- | :--- |
| | high / medium / low | | | |

## Defensive Handoff

| Risk / C / E / B | Validity Impact | Available Evidence | Response Choice / Reason | Missing Evidence / Applicable Rules |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

边界记录：`measured / model_estimated / theoretically_bounded / unknown`，附条件、来源及适用范围。分别记录论文修改计划与可提交 rebuttal；计划不能写成已经完成。

## Systems Logic DoD

- **Status**: pass / revise / needs_evidence / partial / not_applicable
- **Verified Links**:
- **Unresolved Core Claims**:
- **Cross-Section Updates Needed**:
- **Next Evidence Actions**:
