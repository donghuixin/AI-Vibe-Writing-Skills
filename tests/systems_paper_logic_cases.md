# Systems Paper Logic: Forward-Test Cases

这些是合成输入，不是真实论文结果。用于检查 skill 的决策行为，而不是匹配固定措辞。复测时，让独立 Agent 只读取根目录 `SKILL.md`、按路由读取必要资源，并处理输入；不要给它下面的验收项或调研报告。测试应只读，不修改用户论文或仓库。

## A. BLE Contribution Attribution

输入：

> 请检查我的 MobiCom 论文逻辑：Introduction 声称新 BLE 调度机制提升吞吐并且更安全；目前只在 1 米测过，新方案 2 Mbps / baseline 1 Mbps，但两者分别用 2 MHz 和 1 MHz 带宽，没有消融，也没做窃听实验。Design 给了模型式子但没说用它选什么参数。帮我用防御性写作改成可接受的范围，只给建议不要改全文。

验收项：
- 指出吞吐对比有带宽混杂，不能把差异归因于调度机制；也不能反向断言收益完全由带宽造成。
- 安全性缺少证据，短距测试不是物理作用范围或安全保证。
- 其他距离表现未知，不编造距离上限或未来优化收益。
- 指出模型用途断点；若是解释模型，不强造参数优化用途。
- 三策按证据选择，缺证据时缩小主张、列补实验动作，不强行特点化。
- 保留片段审计范围与 `needs_evidence`，不宣称录用、已复现或已完成修改。
- 缺少目标年份 / track / 阶段时，不宣称已核验正式回复规则。

## B. Grammar-Only Routing

输入：

> 只改语法：Our system achieve higher throughput in the tested setting.

验收项：
- 只将 `achieve` 改为 `achieves`。
- 不生成论证工作表、不要求补实验、不改变技术主张、不启动全文重写。

## Recorded Run

2026-09-10：独立 Agent 在无预设答案、只读条件下处理上述两个输入，主 Agent 按行为项复核，两项通过。A 识别带宽混杂、安全证据缺失与模型交接问题，给出有范围的表述和补证据动作；B 仅修正主谓一致。

另完成 root skill frontmatter 校验、改动文档本地链接与锚点、Markdown 表格与围栏、outline JSON/YAML 一致性、review JSON 解析及四个 Mermaid 图语法检查。未进行真实论文实验、录用效果评估或 GitHub 页面截图验证。
