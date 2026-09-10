# 本次结构整理与迁移

## 保留的入口
`SKILL.md`仍是统一入口，`SKILLS.md`是完整能力索引。原编号prompts、`.traerules`和`.agents/workflows`保留路径；它们按任务路由，不各自维护一份强制全流程。

原有15号系统论文逻辑模块、C/H/D/E/B、证据表和领域调研继续使用。新增16号response模块连接正式意见、正文修改和作者回覆，不另造一套系统论文证据ID。

## 配置与记忆
- AI Tone、Flow、Excitement、PPL阈值不再作为重写或“通过”门槛。旧字段即使仍在作者项目里，也不触发评分循环。
- `upper_first`及上中下策略强制排序取消。先判断证据与主张，再选择澄清、纠正、收窄、补证据或有依据地不同意。
- 仓库hard/soft memory模板改为空记录；原内置通用建议迁入 [writing-guidelines.md](writing-guidelines.md)，不再冒充作者事实或偏好。
- 不批量清空作者已有项目记忆。旧条目保留，按来源、状态、范围逐步补信息；新证据冲突时记录取代关系。
- 实际论文的Spec、style profile、review原文、数据和记忆放在作者工作区。共享技能仓库保存指令与模板。

## 本地工具
`Local_AI_Style_Check/paper_ai_detector.py`保留旧命令入口，转向本地风格lint。没有模型下载、PPL分类或作者身份判断，也不自动改稿。现行参数及输出见 [工具说明](../Local_AI_Style_Check/README.md)。依赖模型/PPL的旧Python调用方需迁移到文档化的新接口，CLI兼容不等于所有内部API保持不变。

## 交付与验证
LaTeX结构检查、编译、PDF视觉检查分别报告。无引擎可以交付可编辑源码并说明未编译，不以隐藏待办或替代排版制造完成状态。自动检查覆盖确定性工具与资源完整性，合成任务的独立试用检查路由和决策；两者都不等于录用效果验证。
