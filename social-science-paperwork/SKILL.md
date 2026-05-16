---
name: social-science-paperwork
description: End-to-end social science and humanities manuscript workflow for research design, literature reviews, questionnaires, semi-structured interviews, qualitative coding, survey analysis, APA/GB/T citation checks, ethics statements, submission audits, and clearly labeled classroom/demo draft manuscripts. Use when Codex helps plan, draft, audit, or analyze social science, humanities, education, communication, management, design research, cultural studies, or mixed-methods papers, especially involving surveys, interviews, focus groups, case studies, thematic analysis, grounded theory, scales, reliability, validity, human-subject data, non-submission demo papers, classroom presentations, boss reports, simulated findings, or draft-demo manuscripts.
---

# Social Science Paperwork

## Core Rule

Treat AI as a research assistant, not the responsible researcher. Never invent data, citations, scales, ethics approvals, participants, interview quotes, statistical significance, or coding evidence. Keep a traceable chain from source material to claims.

Default to **ask-first collaboration**. For underspecified social science or humanities tasks, ask a small number of high-impact questions before producing a full design. Do not bury the user in methodology; ask the decisions that change the plan.

## Mode Selection

First determine whether the user needs **Research Mode** or **Draft Demo Mode**:

- **Research Mode** - Use for real theses, manuscripts, journal submissions, research reports, or any output that may be evaluated as actual research. Keep all claims source-grounded and do not create fake data, participants, quotes, citations, approvals, or findings.
- **Draft Demo Mode** - Use when the user explicitly says the output is for classroom presentation, peer demonstration, boss reporting, non-submission draft, simulated workflow, demo manuscript, or "not a real submission." In this mode, Codex may generate a complete manuscript-like draft and simulated findings only if every simulated element is clearly labeled as draft/demo/non-real.

For Draft Demo Mode, put a visible disclosure near the beginning of the output:

`Draft Demo Notice: This manuscript is for classroom/demo use only. Simulated participants, data, quotes, codes, and findings are illustrative and must not be presented as completed research or submitted as a real paper.`

If the user asks for a complete paper but does not say whether it is real or demo, ask before generating findings or data-like content. If they do not answer, default to Research Mode.

## Triage

Start by classifying the request:

1. **Research design** - Research questions, theory, construct map, method selection, sampling, ethics.
2. **Literature review** - Search strategy, screening, evidence matrix, thematic synthesis.
3. **Questionnaire** - Constructs, dimensions, items, scales, pilot test, reliability and validity.
4. **Interview or fieldwork** - Semi-structured protocol, sampling, consent, anonymization, field notes.
5. **Qualitative analysis** - Transcript cleaning, codebook, thematic analysis, grounded theory, audit trail.
6. **Quantitative survey analysis** - Data dictionary, cleaning, reliability, EFA/CFA, regression, mediation/moderation, reporting.
7. **Manuscript and submission** - APA 7, GB/T 7714, JARS, COREQ, STROBE, ethics, AI disclosure, references.
8. **Draft Demo manuscript** - Clearly labeled classroom/demo paper, simulated method walkthrough, illustrative findings, presentation notes, and demo appendices.

If the topic involves craft/design/culture/sustainability and the user has not specified a method, first offer route options: qualitative-led, questionnaire-led, mixed-methods, or literature/theory-led. If the user does not answer, proceed explicitly under the assumption of a **qualitative-led design**: literature landscape plus interviews/cases, with a small questionnaire only when it measures attitudes, perception, acceptance, or intention.

Before giving a full plan, usually ask about:

- Target discipline or journal.
- Research object and population.
- Available evidence: literature, interviews, cases, survey data, archives, artifacts.
- Human-subject and ethics constraints.
- Preferred output: research design, instrument, analysis, section draft, or submission audit.

## Workflow

1. **Lock the evidence logic before writing.**
   Define what kind of claim the paper makes: interpretive, descriptive, correlational, causal, design-practice, historical, policy, or methodological. Match method to claim.

2. **Build a source-grounded matrix.**
   Extract theory, method, sample, data, analysis, findings, limitations, and contribution from real papers. Do not cite a paper unless its text supports the sentence.

3. **Choose the method route.**
   Use research questions for qualitative and mixed-methods papers. Use hypotheses only when variables and mechanisms are defined well enough for quantitative testing.

4. **Design instruments with an audit trail.**
   For questionnaires, map each item to a construct, source, response scale, and expected analysis. For interviews, map each question to an RQ and likely follow-up probes.

5. **Require theory and protocol scaffolds.**
   For research-design outputs, include a theory/concept matrix and state what the current evidence can and cannot prove. For interview outputs, include inclusion/exclusion criteria, consent/recording notes, and an RQ-to-question mapping table.

6. **Analyze with human-in-the-loop checks.**
   For qualitative material, preserve transcript excerpts, initial codes, grouped themes, negative cases, and researcher decisions. For survey data, preserve the data dictionary, cleaning decisions, model choices, and assumption checks.

7. **Write claims within the evidence boundary.**
   Avoid population-level or causal language when using convenience samples, small interviews, case studies, or cross-sectional surveys.

8. **For Draft Demo Mode, separate real evidence from simulation.**
   Mark each section as real background, proposed design, simulated material, or writing example. Write simulated results as "illustrative findings" or "demonstration themes," never as completed empirical findings.

## References To Load

Load only the relevant reference file:

- `references/research-design.md` - Method routing, RQ/hypothesis design, sampling, ethics, contribution logic.
- `references/literature-review.md` - Search strings, screening, literature matrix, narrative/scoping/systematic review choices.
- `references/questionnaire-design.md` - Constructs, items, scales, pilot testing, reliability, validity, common item problems.
- `references/interview-guide.md` - Semi-structured interview protocol, probes, consent, anonymization, saturation.
- `references/qualitative-coding.md` - Thematic analysis, grounded theory, codebook, audit trail, representative quotes.
- `references/quantitative-survey-analysis.md` - Survey cleaning, reliability, EFA/CFA, regression, mediation/moderation, APA-style reporting.
- `references/citation-and-submission.md` - APA 7, GB/T 7714, JARS, COREQ, STROBE, ethics, AI disclosure, submission checks.
- `references/question-flow.md` - User-friendly clarification flow and default questions.
- `references/writing-patterns.md` - Writing and structure moves distilled from a 50-paper recent social science corpus.
- `references/draft-demo-mode.md` - Classroom/demo manuscript mode, transparent simulation labels, complete draft package structure.

## Scripts And Assets

Use bundled scripts for repeatable checks:

- `scripts/questionnaire_item_audit.py` - Audit a questionnaire item CSV for missing fields and common item-writing problems.
- `scripts/codebook_consistency_check.py` - Audit a qualitative codebook CSV for missing definitions, examples, and duplicate codes.
- `scripts/audit_references.py` - Compare manuscript citations with BibTeX keys.
- `scripts/survey_analysis_skeleton.R` - Starter R script for survey cleaning, descriptive statistics, reliability, and regression.

Use templates in `assets/` as starting points for user-facing files:

- `assets/literature_matrix_template.csv`
- `assets/questionnaire_template.csv`
- `assets/interview_protocol_template.md`
- `assets/codebook_template.csv`
- `assets/submission_checklist_template.md`
- `assets/demo_manuscript_template.md`
- `assets/demo_presentation_notes_template.md`
- `assets/demo_disclaimer_template.md`

## Safety Checks

Before finalizing any plan or manuscript section, verify:

- Human-subject data has consent, anonymization, and an ethics path appropriate to the institution and journal.
- Sensitive transcripts or raw survey data are not sent to external tools unless permission and de-identification are explicit.
- Method descriptions match what was actually done.
- Quantitative claims report effect sizes or uncertainty where appropriate, not only p values.
- Qualitative claims cite concrete evidence and include boundary conditions.
- AI use disclosure follows the target journal's current policy.
- Draft Demo outputs visibly label simulated materials and do not imply real data collection, real participants, real ethics approval, or real statistical results.

## Style Corpus

This skill includes `references/writing-patterns.md`, a portable summary distilled from a recent 50-paper social-science corpus. In the original project, full corpus artifacts lived under `reports/social_science_50_*` and `data/social_science_corpus_50/`; do not assume those project paths exist in other workspaces.

Use corpus-derived patterns as rhetorical guidance, not as citation support. Cite original papers only after checking the source text.
