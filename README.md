# Social Science Paperwork

**A Codex skill that turns rough humanities and social-science paper ideas into methodologically defensible research workflows.**

This is a research-design and writing assistant for social science, humanities, education, communication, management, design research, cultural studies, and mixed-methods projects. It is built for the messy middle of real papers: when you have a topic, some literature, maybe interviews or survey ideas, but the research question, evidence chain, ethics, methods, and manuscript structure are not yet sharp enough.

## Why It Exists

Engineering-style papers often win by improving a measurable system. Social-science and humanities papers win differently: by making concepts precise, matching claims to evidence, reporting human-subject methods transparently, and showing why a finding matters theoretically and practically.

`social-science-paperwork` helps Codex behave less like a generic writing assistant and more like a strict but useful methods collaborator:

- It asks the important questions before generating a plan.
- It separates qualitative, quantitative, mixed-methods, and theory-led routes.
- It prevents "I need a questionnaire" from becoming the default answer to every humanities/social-science problem.
- It keeps ethics, consent, anonymization, sample boundaries, and AI-use disclosure visible.
- It turns vague topics into research questions, theory matrices, interview protocols, construct maps, codebooks, and submission checks.

## What Makes It Strong

- **Ask-first workflow**: defaults to clarifying target journal, research object, evidence, data availability, and ethics before producing a full design.
- **Evidence-bound claims**: constantly distinguishes what the data can support from what would require stronger evidence.
- **Qualitative rigor**: supports semi-structured interviews, thematic analysis, grounded-theory-aware coding, negative cases, and audit trails.
- **Survey discipline**: pushes construct-first questionnaire design, item-source tracking, pilot testing, reliability, and validity checks.
- **Writing-pattern intelligence**: includes a portable pattern library distilled from a recent 50-paper social-science corpus, focused on rhetorical moves rather than copying text.
- **Submission awareness**: covers APA/GB/T citation checks, COREQ/STROBE/JARS-style reporting concerns, ethics statements, data availability, and AI disclosure.

## Included Modules

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

## Best Use Cases

- Turning a broad humanities/social-science topic into researchable questions.
- Designing a qualitative interview study with real sampling, consent, and analysis logic.
- Auditing whether a questionnaire has constructs, sources, response scales, and pilot-test needs.
- Building a literature matrix and identifying a bounded research gap.
- Creating a codebook that preserves evidence chains and negative cases.
- Drafting method sections that do not overclaim causality or representativeness.
- Preparing a manuscript for journal or thesis review.

## Example Prompts

```text
Use $social-science-paperwork to help me design a qualitative study on traditional ceramic craft in contemporary sustainable design.
```

```text
Use $social-science-paperwork to audit this questionnaire before I send it to participants.
```

```text
Use $social-science-paperwork to turn my interview transcripts into a codebook and findings structure.
```

```text
Use $social-science-paperwork to check whether my social-science manuscript overclaims its evidence.
```

## Installation

Copy the skill directory into your Codex skills directory:

```powershell
Copy-Item -Recurse .\social-science-paperwork "$env:USERPROFILE\.codex\skills\social-science-paperwork"
```

Restart Codex or start a new session so the skill metadata is discovered.

## Validation

Run the basic skill validator:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\social-science-paperwork
```

Run the included template audits:

```powershell
python .\social-science-paperwork\scripts\questionnaire_item_audit.py .\social-science-paperwork\assets\questionnaire_template.csv
python .\social-science-paperwork\scripts\codebook_consistency_check.py .\social-science-paperwork\assets\codebook_template.csv
```

## Important Boundary

This skill is powerful, but it does not replace research responsibility. It will not invent participants, ethics approval, interview quotes, survey data, significance, citations, or methods. It is designed to make those weak points harder to hide.

Use it to become clearer, stricter, and faster. Do not use it to make unsupported work look stronger than it is.

