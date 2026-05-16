# Social Science Paperwork

**一个面向人文社科论文的 Codex Skill：把粗糙选题变成更像样、更可审查、更能投稿的研究设计工作流。**

`social-science-paperwork` 是给社会科学、人文学科、教育学、传播学、管理学、设计研究、文化研究、艺术教育和混合方法论文准备的研究设计助手。它适合论文最混乱、也最容易出问题的阶段：你已经有一个主题，也许有一些文献、访谈想法或问卷想法，但研究问题、理论框架、证据链、伦理说明、方法章节和行文结构还不够硬。

它不是单纯“润色文字”的工具，而是一个会追问、会卡证据边界、会提醒方法风险的论文协作 skill。

它现在也支持 **Draft Demo 模式**：当你明确说明“不投稿、课堂展示、给同学演示、老板汇报、模拟论文流程”时，它可以生成一篇结构完整、行文漂亮、逻辑自洽的论文示范稿，并把模拟访谈、模拟结果、示例代码本等内容明确标注为 `Draft Demo`，避免把展示材料伪装成真实研究。

进一步地，它现在支持 **Premium Draft Demo 模式**：当你需要“一下生成一个看起来非常完整、排版好看、可直接展示的论文成果”时，它会默认生成一个完整 LaTeX/PDF 论文包，而不是只给一段 Markdown 草稿。这个模式适合课堂展示、组会演示、给同学看流程、给老板看论文雏形。

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
- **目标期刊/导师风格适配**：可以从用户提供的目标期刊论文、相近高质量论文或导师/课题组样稿中学习“结构和修辞模式”，生成 style profile，再逐段修改你的稿件并保留 revision log。
- **Draft Demo 展示稿**：为课堂展示、同学演示和老板汇报生成完整论文 draft、模拟结果样张、访谈/问卷/代码本附录和讲解稿，并强制标注非投稿用途。
- **Premium LaTeX/PDF 论文包**：一键生成 `main.tex`、分节文件、附录、质量审计和可编译 PDF，模拟内容全部标注为 Draft Demo。
- **老板展示安全包**：生成展示话术、禁用说法、真实/拟议/模拟/TODO 边界、最小真实化计划，降低把 Demo 误讲成真实研究的风险。

## 从 journal-adapt 借鉴了什么

我参考了 [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) 里最值得学习的部分：它不是把“学术写作”当成一套固定规则，而是把目标期刊论文作为动态语料，先抽取写作习惯，再生成一个可审查的临时写作规则。

这个 skill 没有照搬它的英文期刊改写流程，而是改成更适合人文社科中文/中英论文的版本：

| journal-adapt 的思路 | 在本 skill 里的改造 |
|---|---|
| 静态规则 + 动态语料 | 社科方法底线 + 目标期刊/导师风格适配 |
| Style Card / Style Profile | 生成目标期刊或导师风格画像，只描述结构和修辞，不复制原文 |
| Priority System | P1 保事实与引用，P2 目标风格，P3 导师/样稿，P4 社科方法规则，P5 清理 AI 腔 |
| Human Gate | 先让用户确认 style profile，再逐段改稿 |
| Section-by-section revision | 每节先诊断，再修改，再输出 revision log |

最关键的边界是：它只能学习“文章怎么组织、贡献怎么放、方法怎么写、讨论怎么收”，不能偷换你的事实、数据、引用或结论。

## 用户使用流程

如果你不知道怎么和 AI 协作，不需要先懂“主题分析、构念、信效度、COREQ”这些术语。你只要先说清楚你现在处在哪一步。

### 1. 先说用途

你可以直接这样说：

```text
Use $social-science-paperwork 我现在是从工科转到社科写论文，主题是传统陶瓷工艺和可持续设计。我没有真实数据，想先做一个给老师看的研究方案。
```

或者：

```text
Use $social-science-paperwork 这是课堂展示，不是真投稿。请帮我做一个完整 Draft Demo，要求有论文正文、访谈提纲、问卷示例、代码本和质量审计。
```

或者：

```text
Use $social-science-paperwork 我有目标期刊论文和自己的 manuscript，请先学习这个期刊的写法，再帮我逐段修改 introduction。
```

### 2. skill 会先问少量关键问题

通常只问这些会改变方案的问题：

| 问题 | 为什么问 |
|---|---|
| 这是正式论文、开题、课堂展示，还是老板汇报？ | 决定能不能使用模拟材料，以及需要多严格的证据边界 |
| 目标学科、课程、导师或期刊是什么？ | 决定写作风格、方法规范和引用格式 |
| 你手里已经有什么材料？ | 决定是做文献综述、访谈、问卷、案例还是 demo |
| 有没有真实受访者或问卷数据？ | 决定能不能写 findings/results |
| 你要中文、英文、Markdown、LaTeX、PDF 还是 PPT？ | 决定输出格式 |
| 你下一步最急需什么？ | 决定先产出研究设计、提纲、问卷、正文还是审计 |

如果你不想回答很多问题，可以直接说“你按最合理的默认方案来”。skill 会明示它采用了什么假设。

### 3. skill 会给你路线卡

它不会默认“文科论文就必须问卷”。它会按材料和目标选择路线：

| 路线 | 适合情况 | 典型产出 |
|---|---|---|
| 质性主导 | 研究意义、经验、文化、教育、设计实践、案例 | RQ、理论框架、访谈提纲、抽样方案、主题分析计划 |
| 问卷主导 | 构念清楚，需要测量态度、接受度、意向 | 构念表、题项表、量表、预测试、信效度计划 |
| 混合方法 | 既要解释机制，又要描述态度分布 | 访谈+问卷整合方案、数据汇合点、风险清单 |
| 文献/理论主导 | 没有田野数据，想先写综述或概念论文 | 检索式、文献矩阵、主题综合、概念框架 |
| Premium Draft Demo | 不投稿，只展示完整论文流程 | LaTeX/PDF 论文包、模拟发现、附录、quality audit |
| 期刊/导师适配 | 已有稿件，想贴近目标期刊或导师写法 | style profile、逐段诊断、修订稿、revision log |

### 4. 每次产出都会带审计

这个 skill 的重点不是只给你一段漂亮文字，而是给你能解释给老师/老板听的材料：

- 哪些内容是真实已有材料。
- 哪些只是拟议研究设计。
- 哪些是模拟展示材料。
- 哪些需要后续真实数据替换。
- 哪些结论现在还不能写。
- 下一步最应该补什么。

### 5. 推荐的完整协作顺序

如果你从零开始写一篇社科论文，可以按这个顺序用：

1. 让 skill 判断选题适合质性、问卷、混合方法还是文献综述。
2. 生成研究问题、概念框架和 claim-evidence map。
3. 生成文献矩阵模板和初步检索策略。
4. 生成访谈提纲或问卷构念表。
5. 如果已有数据，再做编码、统计或 findings 章节。
6. 如果只是展示，进入 Draft Demo 或 Premium Draft Demo。
7. 如果已有目标期刊，加入目标期刊/导师风格适配。
8. 最后做投稿前审计：伦理、引用、方法透明度、AI 使用声明、过度结论。

## 子代理测试后的加强点

这个 skill 已经过一次完整代理生成和独立代理审核。审核结论是：适合展示“流程样板/开题脚手架”，但不能被说成已完成论文。基于这次审核，当前版本进一步强化了几个机制：

- **文献状态分区**：区分 `REAL-VERIFIED`、`REAL-METADATA-ONLY`、`VERIFY`、`TODO-CITATION`、`DRAFT-SIM`，避免候选文献被误当成已核验引用。
- **脚本审计记录**：生成问卷、代码本或引用文件时，应运行或记录本地 audit scripts，输出 `audit_script_results.md`。
- **PDF 质量门**：Premium Demo 默认追求 10-15 页完整 artifact，记录 `compile_status.md`，并尽量处理 LaTeX overfull 等排版问题。
- **老板展示话术**：新增安全讲法、禁用说法和展示顺序。第一句话应说明：这是 Draft Demo workflow scaffold，不是完成的实证发现。
- **真实化计划**：Demo 之后要给出最小可行真实研究路线，例如核验 8-12 篇核心文献、2 次预测试访谈、6-8 次正式访谈、1 次代码本修订。

## 目录结构

```text
social-science-paperwork/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── question-flow.md
│   ├── user-facing-flow.md
│   ├── journal-style-adaptation.md
│   ├── literature-verification.md
│   ├── boss-presentation-guide.md
│   ├── draft-demo-mode.md
│   ├── premium-draft-demo.md
│   ├── section-quality-gates.md
│   ├── demo-to-real.md
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
    ├── submission_checklist_template.md
    ├── demo_manuscript_template.md
    ├── demo_presentation_notes_template.md
    ├── demo_disclaimer_template.md
    ├── boss_report_template.md
    ├── premium_demo_outline.md
    └── premium_latex_template/
```

## 适合什么场景

- 你有一个文科/社科论文题目，但不知道该做访谈、问卷、案例还是文献综述。
- 你想把一个大而空的主题变成可研究的问题。
- 你需要设计半结构访谈提纲，但担心问题太诱导、太抽象或不对应 RQ。
- 你想做问卷，但不确定构念、题项、信效度和样本描述是否站得住。
- 你有访谈材料，想建立代码本和发现章节结构。
- 你担心方法章节被审稿人质疑“不透明”“样本不清”“结论过度”。
- 你想让 AI 帮你写论文，但不想让它把论文写成漂亮废话。
- 你不是真投稿，只是想给同学、老师或老板展示“社科论文从选题到方法再到结果写法”的完整样张。

## Draft Demo 模式

当你明确说这是课堂展示、同学演示、老板汇报或非投稿 draft 时，skill 会切换到 Draft Demo 模式。这个模式可以做得更完整、更像正式论文，但会把所有模拟内容标清楚。

它可以生成：

- `demo_manuscript_draft.md`：完整论文示范稿。
- `demo_interview_protocol.md`：半结构访谈提纲。
- `demo_questionnaire.csv`：问卷构念和题项表。
- `demo_codebook.csv`：示范代码本。
- `demo_presentation_notes.md`：给同学或老板讲解的说明稿。

Draft Demo 模式允许使用模拟访谈片段、模拟主题和示范性结果，但必须保留醒目标记，例如：

```text
Draft Demo Notice: This manuscript is for classroom/demo use only. Simulated participants, data, quotes, codes, and findings are illustrative and must not be presented as completed research or submitted as a real paper.
```

这意味着它可以帮你做“看起来完整、结构自洽、适合展示”的论文样张，但不会把模拟材料包装成真实研究。

## Premium Draft Demo 模式

当你说“直接生成非常完整的论文”“一键生成漂亮 LaTeX/PDF”“不投稿但要像正式论文”“给同学/老板展示”等，skill 会进入 Premium Draft Demo 模式。

默认输出目录建议为：

```text
reports/social_science_premium_demo_paper/paper/
```

默认生成：

- `main.tex`：LaTeX 主文件。
- `sections/*.tex`：摘要、引言、文献综述、研究问题、方法、模拟 findings、讨论、结论。
- `appendix/*.tex`：访谈提纲、问卷模块、代码本。
- `demo_disclosure.tex`：Draft Demo 声明。
- `quality_audit.md`：声明检查、claim-evidence map、overclaim check、模拟材料清单、从 demo 转真实研究的替换清单。
- `compile_status.md`：LaTeX 编译状态、PDF 页数、重要警告。
- `audit_script_results.md`：问卷、代码本、引用审计脚本是否运行及结果。
- `boss_report.md`：给老师/老板展示时的安全讲法、展示顺序和下一步真实化计划。
- `main.pdf`：如果本机有 XeLaTeX，会直接编译 PDF。

这个模式借鉴了高质量论文写作流程中的几个原则：先写一条中心论点，再建 claim-evidence map；每段只承担一个修辞任务；引言用 hourglass 结构；结果与讨论分开；最后做 overclaim 检查。它不会生成假 DOI、假真实访谈或假统计显著性。

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

```text
Use $social-science-paperwork 帮我做一篇课堂展示用的完整社科论文 Draft Demo，主题是传统陶瓷工艺与可持续设计，不投稿，允许模拟结果但必须明确标注。
```

```text
Use $social-science-paperwork 一键生成一篇课堂展示用 Premium Draft Demo 论文，主题是传统陶瓷工艺与可持续设计，输出 LaTeX 和 PDF，模拟材料必须标记。
```

```text
Use $social-science-paperwork 给我生成一个老板展示包：包括 Demo PDF、质量审计、展示讲稿、禁用说法和最小真实化研究计划。
```

```text
Use $social-science-paperwork 审核这个 Draft Demo 有没有可能被误解成真实研究，重点检查文献、访谈、问卷、伦理和 findings 边界。
```

```text
Use $social-science-paperwork 把这个 Demo 转成真实研究计划，列出 8-12 篇核心文献核验、访谈预测试、正式访谈、代码本修订和论文替换顺序。
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

如果你使用 Draft Demo 模式，它可以写模拟材料，但会持续提醒这些材料只能用于展示。真实投稿前必须替换为真实文献、真实数据、真实访谈或真实案例。

## 一句话总结

如果你想让 Codex 不只是“帮我润色”，而是像一个懂社科方法的论文搭档一样，先问关键问题、再帮你搭研究设计、查方法漏洞、整理访谈/问卷/代码本和投稿检查，这个 skill 就是为这个场景做的。
