# Reference Learning And Evidence

文献摘要、书目信息和支持某条主张的证据分开保存。只读取任务需要的来源，保留实际读到的范围。

## Three Checks
1. **Identity**：文献是否存在，标题、作者、年份、版本、DOI是否对应。
2. **Support**：原文哪一页、图、表或段落支持当前陈述；结果的比较对象、条件与指标是否相同。
3. **Use**：它是背景、方法依据、对照结果还是作者推论；不得把外部实验写成本文量测。

检索命中或摘要相似只能支持第一层或部分背景，不能冒充全文查证。缺访问权限时记录未核验，不猜测引用内容。沿用稿件citation keys和版本选择；系统会议论文不应被通用“优先journal”的规则自动替换。

## Source Record
在论文工作区的 `.ai_context/memory/reference_library.json` 保留 `sources` 列表。条目按需要包含：

```json
{
  "id": "ref-example",
  "title": "",
  "authors": [],
  "year": null,
  "version": "",
  "url_or_file": "",
  "access_scope": "abstract_only / selected_pages / full_text",
  "checked_at": null,
  "summary": "",
  "evidence": [
    {
      "claim_id": "C1",
      "locator": "page / figure / table / paragraph",
      "statement": "",
      "conditions": "",
      "result_type": "measured / derived / estimated / author_inference",
      "support_status": "verified / partial / unverified / contradicted"
    }
  ],
  "gaps": []
}
```

这里只是字段模板，不是已完成的来源记录。少量文献可用同等信息的简表，沿用既有来源ID。引用数量、模型评分和正文生成长度不代表证据充分。

## PDFs And Author Style
- 文字提取失败、读过的页码和图表视觉检查状态分别记录；`parse_pdf.py`仅做文字提取。
- 关键公式、曲线、图例和多栏顺序需要核对原页，不能把OCR数值直接当作事实。
- 从别人的文章学习结构时，记录为参考建议；只有作者自己的样本或确认才进入其style profile。
- 事实或偏好需记忆时遵循 [长期记忆规则](prompts/5_long_term_memory.md)。
