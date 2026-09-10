# Memory With Provenance

在论文工作区维护事实与作者偏好，只读取当前任务相关条目。技能仓库中的空文件是模板，不应写入私人稿件数据。

## Classify Before Saving
- **Research fact**: 术语、数值、单位、条件及可定位原始来源。作者报告但未核验的结果标为 `author_reported`，不是 `verified`。
- **Author preference**: 区分 `author_confirmed` 与 `observed`；观察附作者样本、文体、位置及可信度。
- **Writing guideline**: 通用指南或他人论文的建议，不是研究事实，也不自动成为本作者偏好。保存在参考笔记。
- **Derived conclusion**: 保留输入来源、推导或脚本、范围与未解决条件，不是永久正确的硬记忆。

## Storage
沿用 作者论文工作区的 `.ai_context/memory/hard_memory.json` 与 `.ai_context/memory/soft_memory.json` 的 `domains` 分类。新增研究条目至少有 `id`、`value`或`definition`、`kind`、`status`、`source`、`scope`；数值另有单位与条件。偏好条目另记录 `genre` 与 `confidence`。已有旧条目可读取，但缺来源的视为待核实，不静默升级状态。

来源应足以重新找到证据，如文件及页码、图号、数据和配置版本、作者确认的任务与日期。只记摘要或URL通常不能证明具体结果。

## Update And Recall
1. 同一ID或同一事实更新版本，不无限追加重复项。
2. 新证据冲突时保留来源与取代关系，核查后修正使用中的主张。旧记忆不覆盖原始数据、当前作者纠正或适用决定信。
3. 文献量测不能混成本文实验；他人的修辞不能混成用户偏好。
4. 输出实际新增、更新、冲突条目及此次使用范围，不必打印完整记忆库。

参见 [参考文献学习](../reference_learning.md)。
