# Role
你是一名资深的计算语言学家和文体分析专家。

# Task
我会提供给你几段我过去撰写的[学术论文/技术博客/随笔]（请根据实际情况替换）。请深入分析这些文本，提取我的“写作风格指纹”，并以Markdown格式输出。

# Analysis Dimensions (请严格按照以下维度分析)
1. **Sentence Structure (句法结构)**:
   - 平均句长是多少？是喜欢短句有力，还是长难句嵌套？
   - 是否喜欢使用倒装句、强调句或特定的连接词（如 "Therefore", "Notably", "Conversely"）？
   - 主动语态与被动语态的比例如何？

2. **Vocabulary & Tone (词汇与语气)**:
   - 学术严谨度（1-10分）：词汇选择是晦涩高深（Tier 3 words）还是平实易懂？
   - 常用高频词（Signature Words）：列出我习惯使用的特有动词或形容词。
   - 语气情感：是客观中立、极客幽默还是犀利批判？

3. **Micro-Habits (微习惯)**:
   - 标题格式习惯。
   - 引用和举例的方式。
   - 标点符号的使用偏好（例如是否喜欢用破折号、分号）。

# Output Format
请生成一份内容直接写入 `style_profile.md` 的内容，格式如下：
```markdown
## Core Style DNA
- **Tone**: [描述]
- **Sentence Pattern**: [描述]

## Do's (我要的风格)
- [例如：必须使用第一人称复数 "We proposed..."]
- [例如：在引入新概念时，必须先给出一个现实世界的类比]

## Don'ts (我不要的风格)
- [例如：拒绝使用 "delve into", "utilize", "tapestry" 等典型的 AI 味词汇]
```