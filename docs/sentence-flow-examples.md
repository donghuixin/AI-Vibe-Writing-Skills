# 句间论证：按需示例

供 [17 · Sentence Flow](../.ai_context/prompts/17_sentence_flow_agent.md) 在判断有疑义时按需读取。以下设计、数据、文字与材料位置全部独立合成，仅用于说明编辑决策；不代表任何真实论文、系统或评审。案例中的来源是明确给定的合成事实，不能迁移为其他稿件的事实证据。

## 1. 真正的话题断裂：来源支持输出→输入的修复

**段落职责与读者状态。** 本段介绍归档服务如何从变更记录生成上传包。读者已知道什么是变更记录，尚不知道接下来引入的缓冲区如何使用筛选结果。

**可用材料。** 合成设计说明 §2 明确规定：筛选器输出变更记录的编号；打包缓冲区按这些编号读取记录内容，形成上传包。缓冲区是打包步骤，不负责决定哪些记录发生变化。

**原文。**

> The filter outputs the identifiers of the changed records. A buffer forms the upload packet.

**发现（P1，revise）。** 两句从筛选输出跳到缓冲区动作，没有说明编号如何进入打包步骤。读者无法知道缓冲区处理筛选出的记录，还是独立处理全部记录。问题不是 `A` 本身，而是缺少材料中已有的输入关系。

**最小修复。** 保留首句，只补后句的输入及读取动作：

> The filter outputs the identifiers of the changed records. A buffer uses these identifiers to retrieve the records and form the upload packet.

新增关系逐项对应合成设计说明 §2；没有增添新的筛选能力。后句仍以 `A buffer` 开头，关系已清楚时无需再为冠词或主语重写。

## 2. 施事者错误：离线作者选择被写成在线自适应

**可用材料。** 合成参数记录 §1：作者在部署前比较窗口长度，选定 12 个样本并固定在配置文件中；运行时控制器始终读取该固定值，没有估计噪声或改变窗口长度的代码。

**原文。**

> We compared window lengths before deployment and selected a 12-sample window. The controller selects this window length as the noise level changes.

**发现（P1，revise）。** 后句把作者已经完成的离线选择写成控制器随噪声变化而在线选择。读者会误认系统具有未实现的自适应行为。换成被动句 “This window length is selected as the noise level changes” 仍保留了错误行为。

**最小修复。**

> We compared window lengths before deployment and selected a 12-sample window. The controller uses this fixed window length during operation.

`We` 转为 `The controller` 是准确的阶段交接，应当保留。审阅需要纠正实际动作，不能只追求表面上主语一致。

## 3. 合理的 A/An 与被动：无需修改

**上下文与可用材料。** 合成装置说明已交代：本段从读数输出转向设备安装，安装步骤需要一个用于锁紧支架的部件。装置图列出了该部件及其位置。

**原文。**

> The bracket requires a locking component before the reader can be mounted. A locking pin is inserted through the bracket before mounting.

**判断（pass）。** 第一处 `A locking pin` 将已提出的锁紧部件具体化，读者有充分铺垫；后句被动表达保持对安装部件的关注，执行插销动作的人在此处不影响理解。不要仅因冠词、被动或没有 `we` 而改稿。

这个段落已经换到安装职责，不需要勉强把前段每个读数变量重新搬到句首。若全文没有说明换题目的，检查实际段间上下文后再定位，而非凭孤立的两句推定问题。

## 4. 无证据的关系：不能用过渡词编造因果

**可用材料。** 合成评估表 §3 只报告一次运行：网关缓存大小为 64 KB，该运行中的端到端中位延迟为 18 ms。没有其他缓存配置的比较，也没有把延迟分解到缓存行为的分析。

**原文。**

> The gateway uses a 64 KB cache. This cache reduces the median end-to-end latency to 18 ms.

**发现（P1，needs_evidence）。** 后句把同时出现的配置与观测归为因果；`This cache` 的回指虽清楚，论证仍不成立。缺的是支持缓存降低延迟的比较或分析，不是一个更顺的连接词。

**现有材料支持的最小修复。** 若本段职责是报告当前配置下的结果，可收窄为：

> The gateway uses a 64 KB cache. In the measured run, the median end-to-end latency was 18 ms.

这保留配置与观测，删除未经支持的归因；不能改成 “Therefore, the cache achieves…” 或自行补写 “by avoiding repeated requests”。如本段必须回答缓存为何有效，收窄后该问题仍未解决，应继续保留 `needs_evidence`，指出需要的具体依据，不虚构机制或自动承诺新实验。

## 5. 正文与 response letter：技术解释和修订历史各有位置

**可用材料。** 合成实现说明 §2：发送端为每个请求分配序列号，接收端用序列号识别重发请求。合成版本差异表明，正文 §3 已新增这一说明；这里没有新增实验。

**待审正文。**

> The receiver identifies retransmissions by their sequence numbers. We have added this explanation to address the concern about duplicate requests.

**发现（P2，revise）。** 首句解释系统动作，后句转向作者修订历史，打断本段技术职责。最小修复是从正文删去后句；首句已有依据且清楚，可以保持。不要把正文扩成逐句解释为什么这样写。

**合成回复中的对应表达。**

> The receiver identifies retransmissions by their sequence numbers. We have added this implementation detail to Section 3.

这两句在回复中分别回答机制问题和说明已完成修改，符合回复职责，可以保留。版本差异只支持补充说明，因此不能把第二句写成 “We have added an experiment…”；如果修改尚未完成，也不能写 `have added`。

## 6. “浅薄”与车轱辘话：定位缺失关系，保留必要术语

**可用材料。** 合成调度说明 §4：队列容量为 20 条；每次提交前检查剩余容量，剩余容量不足时该批次留在发送端等待。这里只解释容量约束，不报告吞吐收益。

**原文。**

> The scheduler handles the queue efficiently. This queue handling improves scheduling efficiency.

**发现（P1，revise）。** 两句在同一层面重复未经定义的效率结论。读者仍不知道调度器检查什么条件、据此采取什么动作；缺的是容量约束→是否提交的决策关系，并非缺少技术形容词。

**有依据的替换。**

> Before submitting a batch, the scheduler checks the queue's remaining capacity. If that capacity is insufficient, the scheduler keeps the batch at the sender until space is available.

这个修复恢复合成调度说明 §4 的条件与动作，没有声称吞吐或延迟得到改善。两句重复 `the scheduler` 是准确地跟踪同一施事者，不需要用含义不同的同义词消除重复。

**另一组无需删除的重复。**

> The parser produces a list of valid record identifiers. The packer uses these record identifiers to retrieve the payloads.

两句重复 `record identifiers`，但分别交代上游输出与下游输入，职责不同。若相应接口材料支持它们，这种重复有助于理解，不是车轱辘话。

## 7. 段间交接：保留对象，明确材料中已有的变换

**可用材料。** 合成设计说明 §5：拟合阶段输出每个传感器的偏置估计；运行阶段先从原始读数中减去该偏置，阈值判断使用修正后的读数。

**前段末句与后段首句。**

> The fitting stage estimates an offset for each sensor.
>
> The threshold test uses the corrected reading.

**发现（P1，revise）。** 在本例给定上下文中，`corrected reading` 尚无定义，读者不知道前段的偏置估计如何成为后段判断的输入。缺口是已知偏置→修正读数的变换，而不是两个段落没有使用相同主语。

**最小修复。** 保留前段末句，在后段首次使用处补足：

> The threshold test uses the reading after subtracting the estimated sensor offset.

无需在前后两段重复整套拟合步骤；也不能擅自改成归一化、滤波或在线重新拟合。若上下文此前已经定义了修正读数，原句可能无需修改，应先检查定义位置。

## 8. 用户只要审阅或语法：不扩成重写

**审阅请求。** 用户说“只指出两句之间的逻辑问题，不改稿”。使用上述相邻原文、缺口及最小修复建议交付发现，保持源文件不变。建议文本不等于获得实际编辑授权。

**语法请求。** 用户说“仅改语法”，提供 “A sensor are mounted on the frame.”。只纠正为 “A sensor is mounted on the frame.”；不能因此触发本模块、重写段落或把合理被动句改成统一的 `we` 句式。

**已授权的最小 LaTeX 修订。** 若用户同时要求保留 `%` 原文及 `\blue{...}`，案例 1 可只改第二句：

```latex
The filter outputs the identifiers of the changed records.
% A buffer forms the upload packet.
\blue{A buffer uses these identifiers to retrieve the records and form the upload packet.}
```

这些标记取决于当前用户约定，不是公共模板预设的作者偏好。按现有流程保存源快照；不要为每次复查层层包裹旧版本。定向检查新增输入关系、首句接口和紧随其后的句子；缺口已经解决且没有引入新问题时结束。

## 9. 推断前提与统计口径：句子顺滑不等于结论成立

**来源 R1。** 接收端记录收到 80 个包，其中 72 个通过校验；记录没有发送端的发送总数。

**原文。**

> Of the 80 received packets, 72 passed the checksum. Therefore, the packet delivery success rate was 90%.

**诊断。** 前句已知 P 是接收集合及其校验结果；后句 Q 却是发送到接收的成功率。中间缺少前提 W：被接收的 80 个包是否代表全部发送尝试，以及何种结果算成功。`Therefore` 清楚表达了推断意图，却不能证明这两个指标等价。问题落在结论的分母与成功定义，不在句首或数字计算。

**最小修复。**

> Of the 80 received packets, 72 passed the checksum, giving a checksum pass rate of 90% among received packets.

保留来源支持的 72/80 和接收集合，删除未经建立的 delivery 指标。原 delivery 主张仍缺依据；无需为了维持该主张要求作者新增实验。

## 10. 非相邻承接与定义插入：可以无需修改

**来源 R2。** 解码器输出带有校验标记的记录。下游消费者接收校验标记为真的记录。`valid record` 在本段定义为校验标记为真的记录；其定义没有加入其他条件。

**原文。**

> The decoder emits records with checksum flags. A record is valid if its checksum flag is true. These valid records are passed to the consumer.

**诊断。** 本段回答解码器输出中哪些记录进入消费者。第一句引入记录及标记，第二句定义后续使用的 valid，第三句同时承接第一句的记录与第二句的条件。承接可以跨越一句，定义也可以承担必要职责；无需把每句话都改成新增机制或结论。

**处理。** 原样保留。`A record` 是有目的的定义，`These valid records` 在当前上下文中指代明确，被动语态保持被传递记录为话题。若强改成所有句子都以 decoder 开头，反而会把注意力从选择条件移开。

## 原则来源与适用边界

Gopen 与 Swan 在 [The Science of Scientific Writing](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html) 中讨论读者预期、句首话题与已有信息的回接、句末重点以及主动与被动在不同话题下的用途。这里借用其编辑视角辅助发现关系缺口；上述案例均为独立合成，没有转载该文案例。这些原则需要结合上下文使用，不是冠词禁令、固定句型，也不是 ACM SIGMOBILE 的官方写作或验收规则。
