## Outline Template

Copy only the needed structure into the author's paper workspace. Ranges of zero and constraints containing X/Y/Z/N/E are placeholders, not actual requirements. Replace or omit them using the current task and evidence; defensive fields are optional for ordinary drafting.

### JSON
```json
{
  "outline_id": "outline-001",
  "topic": "",
  "core_points": [],
  "structure": [
    {
      "section_id": "sec-1",
      "title": "",
      "core_points": [],
      "paragraph_range": {
        "min": 0,
        "max": 0
      },
      "word_range": {
        "min": 0,
        "max": 0
      },
      "paragraphs": [
        {
          "paragraph_id": "p-1",
          "thesis": "",
          "evidence_type": "",
          "claim_ids": [],
          "systems_logic_dod": [],
          "word_range": {
            "min": 0,
            "max": 0
          },
          "definition_of_done": [
            "Must cite reference X",
            "Must use term Y",
            "No more than N words"
          ],
          "defensive_dod": [
            "Identify the reviewer question and select an evidence-supported response",
            "Check whether the limitation affects the stated contribution",
            "Must disclose limitation Z and its evidence-supported impact on the claim",
            "Must anchor defensive framing to evidence E"
          ]
        }
      ]
    }
  ]
}
```

### YAML
```yaml
outline_id: outline-001
topic: ""
core_points: []
structure:
  - section_id: sec-1
    title: ""
    core_points: []
    paragraph_range:
      min: 0
      max: 0
    word_range:
      min: 0
      max: 0
    paragraphs:
      - paragraph_id: p-1
        thesis: ""
        evidence_type: ""
        claim_ids: []
        systems_logic_dod: []
        word_range:
          min: 0
          max: 0
        definition_of_done:
          - "Must cite reference X"
          - "Must use term Y"
          - "No more than N words"
        defensive_dod:
          - "Identify the reviewer question and select an evidence-supported response"
          - "Check whether the limitation affects the stated contribution"
          - "Must disclose limitation Z and its evidence-supported impact on the claim"
          - "Must anchor defensive framing to evidence E"
```

### Systems Paper Extension
`claim_ids` 与 `systems_logic_dod` 为可选字段，非系统任务可省略。系统论文从 `.ai_context/systems_paper_logic.md` 关联 C/H/D/E/B；例如验收“D1 的输出与下一模块输入一致”“C1 只使用 E1 已验证范围”。缺失实验标记为待补证据，不能用一句正文当作已经完成该 DoD。
