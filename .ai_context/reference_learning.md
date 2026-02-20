# Reference Learning Pipeline / 参考文献学习流程

本流程用于高效学习用户提供的参考文献，并将知识、数据、术语与写作风格沉淀到本地记忆与参考库。

## 1. Input Format / 输入格式
- 原文文本、摘要、要点列表或引用条目
- 标注基本元数据：标题、作者、年份、来源、领域标签

## 2. Extraction Targets / 抽取目标
- **Facts**：可验证事实与关键结论
- **Data**：数据、指标、数值区间与实验结果
- **Terms**：领域术语与标准化写法
- **Style**：段落节奏、句式偏好与论证方式

## 3. Storage Strategy / 本地存储策略
- **Reference Library**：`.ai_context/memory/reference_library.json`
  - 保存来源信息、摘要、可引用片段与标签索引
- **Hard Memory**：`.ai_context/memory/hard_memory.json`
  - 保存术语、单位、关键事实与稳定数据
- **Soft Memory**：`.ai_context/memory/soft_memory.json`
  - 保存措辞偏好、论证风格、语气与结构习惯

## 4. Evidence Usage / 证据使用规则
- 引用数量与覆盖度遵循 `.ai_context/custom_specs.md` 的 Evidence Requirements
- 写作时输出引用清单，便于审计与复用

## 5. Suggested Record Schema / 推荐条目结构
{
  "id": "ref:year:shortkey",
  "title": "",
  "authors": [],
  "year": "",
  "venue": "",
  "domain": "",
  "tags": [],
  "abstract": "",
  "key_points": [],
  "quotes": [],
  "data_points": [],
  "terms": [],
  "style_notes": []
}
