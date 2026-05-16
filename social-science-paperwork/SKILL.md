---
name: social-science-paperwork
description: End-to-end social science and humanities manuscript workflow for research design, literature reviews, questionnaires, semi-structured interviews, qualitative coding, survey analysis, APA/GB/T citation checks, ethics statements, and submission audits. Use when Codex helps plan, draft, audit, or analyze social science, humanities, education, communication, management, design research, cultural studies, or mixed-methods papers, especially involving surveys, interviews, focus groups, case studies, thematic analysis, grounded theory, scales, reliability, validity, or human-subject data.
---

# Social Science Paperwork

## Core Rule

Treat AI as a research assistant, not the responsible researcher. Never invent data, citations, scales, ethics approvals, participants, interview quotes, statistical significance, or coding evidence. Keep a traceable chain from source material to claims.

Default to **ask-first collaboration**. For underspecified social science or humanities tasks, ask a small number of high-impact questions before producing a full design. Do not bury the user in methodology; ask the decisions that change the plan.

## Triage

Start by classifying the request:

1. **Research design** - Research questions, theory, construct map, method selection, sampling, ethics.
2. **Literature review** - Search strategy, screening, evidence matrix, thematic synthesis.
3. **Questionnaire** - Constructs, dimensions, items, scales, pilot test, reliability and validity.
4. **Interview or fieldwork** - Semi-structured protocol, sampling, consent, anonymization, field notes.
5. **Qualitative analysis** - Transcript cleaning, codebook, thematic analysis, grounded theory, audit trail.
6. **Quantitative survey analysis** - Data dictionary, cleaning, reliability, EFA/CFA, regression, mediation/moderation, reporting.
7. **Manuscript and submission** - APA 7, GB/T 7714, JARS, COREQ, STROBE, ethics, AI disclosure, references.

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

## Safety Checks

Before finalizing any plan or manuscript section, verify:

- Human-subject data has consent, anonymization, and an ethics path appropriate to the institution and journal.
- Sensitive transcripts or raw survey data are not sent to external tools unless permission and de-identification are explicit.
- Method descriptions match what was actually done.
- Quantitative claims report effect sizes or uncertainty where appropriate, not only p values.
- Qualitative claims cite concrete evidence and include boundary conditions.
- AI use disclosure follows the target journal's current policy.

## Style Corpus

This skill includes `references/writing-patterns.md`, a portable summary distilled from a recent 50-paper social-science corpus. In the original project, full corpus artifacts lived under `reports/social_science_50_*` and `data/social_science_corpus_50/`; do not assume those project paths exist in other workspaces.

Use corpus-derived patterns as rhetorical guidance, not as citation support. Cite original papers only after checking the source text.
