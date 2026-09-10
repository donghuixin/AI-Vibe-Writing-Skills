# Local Style Lint

离线检查稿件中可能冗余或模板化的表达，返回位置与原因，由作者结合语境判断。规则以英文为主，也包含少量中文引导语。它不估算 AI 作者概率、抄袭率或论文质量，也不自动改写文件。

## 使用

使用 Python 3.11 或更高版本，无需安装第三方依赖。

```bash
python Local_AI_Style_Check/style_lint.py path/to/manuscript.tex
python Local_AI_Style_Check/style_lint.py path/to/paper --format json
```

支持 UTF-8 的 `.tex` 与 `.md` 文件，也可递归检查目录中的这两类文件。JSON 中的每条提示包含 `path`、从 1 开始的 `line` / `column`、`excerpt`、`rule` 和 `reason`。`--json` 是 JSON 输出的快捷方式。

退出码：`0` 表示未发现候选问题，`1` 表示有候选问题，`2` 表示输入或读取错误。有提示不代表文字错误，没有提示也不代表内容已经通过审稿。

`--list-rules` 列出实际规则；`--no-recursive` 只检查指定目录的第一层。使用自定义 LaTeX 宏或环境时可以补充遮罩规则：

```bash
python Local_AI_Style_Check/style_lint.py response.tex --skip-macro reviewertext=2 --skip-env reviewerblock
```

`NAME=N` 表示跳过该宏的 N 个必需参数，前面的可选参数也会跳过。默认 `reviewcomment` / `reviewercomment` 各按两个参数处理，`overallcomment` / `closingcomment` / `reviewerquote` 各按一个参数处理。宏定义不同就用 `--skip-macro` 覆盖其参数数目；不要把作者正文宏加进遮罩。完整内置列表见 [style_lint.py](style_lint.py) 的 `SKIP_MACROS` / `SKIP_ENVS`。

## 如何处理提示

先读原句及上下文，判断短语是否多余、重复开头是否影响阅读，再决定保留或局部修改。工具只检查少量可解释的句型和重复模式，不使用词频或单个“高级词”推断文字来源。技术词、证明强度与作者偏好应由对应材料决定。

为减少误报，检查时遮罩常见 LaTeX 数学、引用命令、注释、verbatim、审稿引用宏，以及 Markdown 的引用和代码区域，同时保留原始行号。它不是完整的 TeX 或 Markdown 解析器；自定义宏和复杂嵌套可能识别不全。审稿意见原文仍需单独进行完整性比对，不能依靠本工具证明其未被修改。

## 旧入口迁移

```bash
python Local_AI_Style_Check/paper_ai_detector.py path/to/manuscript.tex --format json
```

旧文件名保留为相同 CLI 的转发入口。原来的模型下载、PPL 分类和作者身份判断接口已移除；旧参数或 Python 调用方应迁移到当前接口。`--help` 显示实际支持的参数。

`requirements.txt` 只保留说明，不再安装 PyTorch、Transformers 或语言模型。可选 PDF 提取工具的依赖独立配置。

## 验证

在仓库根目录运行：

```bash
python -m unittest discover -s tests -p "test_style_lint.py" -v
```

测试使用合成文本，检查提示位置、应跳过的区域、正常技术措辞、CLI 行为和输入错误。它们验证实现行为，不评估作者身份识别能力。
