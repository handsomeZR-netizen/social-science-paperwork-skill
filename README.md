# Social Science Paperwork

**一个面向人文社科论文的 Codex Skill：把粗糙选题变成更像样、更可审查、更能投稿的研究设计工作流。**

`social-science-paperwork` 是给社会科学、人文学科、教育学、传播学、管理学、设计研究、文化研究、艺术教育和混合方法论文准备的研究设计助手。它适合论文最混乱、也最容易出问题的阶段：你已经有一个主题，也许有一些文献、访谈想法或问卷想法，但研究问题、理论框架、证据链、伦理说明、方法章节和行文结构还不够硬。

它不是单纯“润色文字”的工具，而是一个会追问、会卡证据边界、会提醒方法风险的论文协作 skill。

## 为什么需要它

工科论文通常靠实验、性能、模型或系统改进说服读者。文科和社科论文的说服方式不同：它更依赖概念是否清楚、理论是否能解释材料、样本和结论是否匹配、访谈或问卷是否透明、讨论是否真的回到理论和实践贡献。

很多人从工科写作转到文科/社科写作时，最容易掉进几个坑：

- 以为“文科论文必须做问卷”。
- 先写题项，再倒找理论和变量。
- 用小样本访谈，却写成普遍规律。
- 用“影响”“作用”“促进”这类因果词，但研究设计并不能支持因果结论。
- 访谈提纲看起来完整，但没有 RQ 映射、抽样边界、伦理和匿名化说明。
- 文献综述只是堆资料，没有真正形成研究缺口。

这个 skill 的目标就是把这些风险提前暴露出来。

## 核心能力

- **先问再写**：默认先问目标期刊、研究对象、已有证据、数据来源、伦理边界和当前要产出的材料，不会一上来就替你拍脑袋定方案。
- **路线分流**：区分质性研究、问卷研究、混合方法、理论/文献综述，不把所有问题都硬塞进问卷。
- **研究问题打磨**：把宽泛主题拆成可研究的 RQ、理论框架矩阵、变量/构念地图和证据链。
- **访谈研究支持**：生成半结构访谈协议、追问逻辑、纳入/排除标准、知情同意提醒、匿名化要求和 RQ-问题映射表。
- **问卷设计审计**：检查构念、维度、题项、来源、反向题、量表、预测试、信度和效度风险。
- **质性编码支持**：支持主题分析、扎根理论意识、代码本、负例、开放代码、证据链和研究者备忘录。
- **定量分析骨架**：提供 R 脚本骨架，用于问卷数据清洗、描述统计、信度分析和基础模型准备。
- **投稿前检查**：覆盖 APA/GB/T 引用、COREQ/STROBE/JARS 风格报告意识、伦理声明、AI 使用声明和数据可得性说明。
- **社科写作模式库**：内置从近年社科论文中蒸馏出的行文结构、段落动作和句式模板，重点学习写法，不复制原文。

## 目录结构

```text
social-science-paperwork/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── question-flow.md
│   ├── writing-patterns.md
│   ├── research-design.md
│   ├── literature-review.md
│   ├── questionnaire-design.md
│   ├── interview-guide.md
│   ├── qualitative-coding.md
│   ├── quantitative-survey-analysis.md
│   └── citation-and-submission.md
├── scripts/
│   ├── questionnaire_item_audit.py
│   ├── codebook_consistency_check.py
│   ├── audit_references.py
│   └── survey_analysis_skeleton.R
└── assets/
    ├── literature_matrix_template.csv
    ├── questionnaire_template.csv
    ├── interview_protocol_template.md
    ├── codebook_template.csv
    └── submission_checklist_template.md
```

## 适合什么场景

- 你有一个文科/社科论文题目，但不知道该做访谈、问卷、案例还是文献综述。
- 你想把一个大而空的主题变成可研究的问题。
- 你需要设计半结构访谈提纲，但担心问题太诱导、太抽象或不对应 RQ。
- 你想做问卷，但不确定构念、题项、信效度和样本描述是否站得住。
- 你有访谈材料，想建立代码本和发现章节结构。
- 你担心方法章节被审稿人质疑“不透明”“样本不清”“结论过度”。
- 你想让 AI 帮你写论文，但不想让它把论文写成漂亮废话。

## 示例 Prompt

```text
Use $social-science-paperwork 帮我把“传统陶瓷工艺在当代可持续设计中的应用”设计成一篇质性研究论文。
```

```text
Use $social-science-paperwork 审核我的问卷题项，看看有没有构念不清、双重提问、诱导性问题和信效度风险。
```

```text
Use $social-science-paperwork 根据这些访谈材料帮我建立代码本和 findings 章节结构。
```

```text
Use $social-science-paperwork 检查我的社科论文有没有证据不足、结论过度、伦理说明缺失的问题。
```

## 安装方式

把 skill 目录复制到你的 Codex skills 目录：

```powershell
Copy-Item -Recurse .\social-science-paperwork "$env:USERPROFILE\.codex\skills\social-science-paperwork"
```

然后重启 Codex 或开启新会话，让 Codex 重新发现 skill。

## 验证方式

运行 Codex skill 基础校验：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\social-science-paperwork
```

运行内置模板审计：

```powershell
python .\social-science-paperwork\scripts\questionnaire_item_audit.py .\social-science-paperwork\assets\questionnaire_template.csv
python .\social-science-paperwork\scripts\codebook_consistency_check.py .\social-science-paperwork\assets\codebook_template.csv
```

这两个脚本即使通过，也可能输出 warning。warning 是故意设计的：它会提醒你“这个题项来源还没验证”“这个构念题项太少”“代码本还没有开放代码或负例”等方法学风险。

## 它不会替你做什么

这个 skill 会让论文更清楚、更严格、更像一篇能被审查的方法论文。但它不会替你承担研究责任。

它不会也不应该：

- 编造受访者。
- 编造问卷数据。
- 编造伦理审批。
- 编造访谈原话。
- 编造显著性结果。
- 编造文献和 DOI。
- 把小样本便利访谈包装成普遍规律。
- 把 AI 生成内容伪装成真实材料。

它的真正价值不是把弱研究包装得更强，而是更早告诉你哪里弱、该怎么补。

## 一句话总结

如果你想让 Codex 不只是“帮我润色”，而是像一个懂社科方法的论文搭档一样，先问关键问题、再帮你搭研究设计、查方法漏洞、整理访谈/问卷/代码本和投稿检查，这个 skill 就是为这个场景做的。
