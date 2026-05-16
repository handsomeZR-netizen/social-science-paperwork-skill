---
name: social-science-paperwork
description: End-to-end social science and humanities manuscript workflow for research design, literature reviews, questionnaires, interviews, qualitative coding, survey analysis, APA/GB/T citation checks, ethics statements, journal/user-style adaptation, submission audits, and premium classroom/demo draft manuscripts with LaTeX/PDF output. Use when Codex helps plan, draft, audit, or analyze social science, humanities, education, communication, management, design research, cultural studies, or mixed-methods papers, especially involving surveys, interviews, focus groups, case studies, thematic analysis, grounded theory, scales, reliability, validity, human-subject data, target-journal style, advisor/lab writing preferences, non-submission demo papers, classroom presentations, advisor reports, senior-student or research-group presentations, simulated findings, draft-demo manuscripts, one-click complete papers, polished LaTeX, or "perfect paper" demo drafts.
---

# Social Science Paperwork

## Core Rule

Treat AI as a research assistant, not the responsible researcher. Never invent data, citations, scales, ethics approvals, participants, interview quotes, statistical significance, or coding evidence. Keep a traceable chain from source material to claims.

Default to **ask-first collaboration**. For underspecified social science or humanities tasks, ask a small number of high-impact questions before producing a full design. Do not bury the user in methodology; ask the decisions that change the plan.

## User-Facing Collaboration Flow

If the user is unsure how to work with AI, run the skill as a guided workflow, not a lecture. Load `references/user-facing-flow.md` when the user asks what to provide, wants a full process, or sounds unfamiliar with social science writing.

Default to this conversational order:

1. **Purpose** - Is this real research, a course demo, an advisor/research-group report, a proposal, or revision?
2. **Topic and audience** - What is the topic, discipline, target journal/class/advisor, and expected language?
3. **Evidence already available** - Literature, interview transcripts, survey data, cases, archives, artifacts, or only an idea.
4. **Method route** - Recommend one route card: qualitative-led, questionnaire-led, mixed-methods, literature/theory-led, or Premium Draft Demo.
5. **Output contract** - State the exact files/sections to create and which parts will be real, proposed, simulated, or TODO.
6. **Audit pass** - End with a claim-evidence map, risk list, and next questions instead of only polished prose.

## Mode Selection

First determine whether the user needs **Research Mode**, **Draft Demo Mode**, or **Premium Draft Demo Mode**:

- **Research Mode** - Use for real theses, manuscripts, journal submissions, research reports, or any output that may be evaluated as actual research. Keep all claims source-grounded and do not create fake data, participants, quotes, citations, approvals, or findings.
- **Draft Demo Mode** - Use when the user explicitly says the output is for classroom presentation, peer demonstration, advisor/research-group reporting, non-submission draft, simulated workflow, demo manuscript, or "not a real submission." In this mode, Codex may generate a complete manuscript-like draft and simulated findings only if every simulated element is clearly labeled as draft/demo/non-real.
- **Premium Draft Demo Mode** - Use when the user asks for a one-click complete paper, polished LaTeX/PDF, "perfect" demo paper, or a beautiful classroom/advisor/research-group presentation artifact. Produce a full paper package, not a short explanation: LaTeX source, sections, appendices, quality audit, and compiled PDF when LaTeX is available.

For Draft Demo Mode, put a visible disclosure near the beginning of the output:

`Draft Demo Notice: This manuscript is for classroom/demo use only. Simulated participants, data, quotes, codes, and findings are illustrative and must not be presented as completed research or submitted as a real paper.`

If the user asks for a complete paper but does not say whether it is real or demo, ask before generating findings or data-like content. If they do not answer, default to Research Mode.

For Premium Draft Demo Mode, load `references/premium-draft-demo.md`, `references/section-quality-gates.md`, `references/draft-demo-mode.md`, `references/demo-to-real.md`, `references/literature-verification.md`, and `references/presentation-guide.md`. Use the premium LaTeX assets under `assets/premium_latex_template/` as the starting structure.

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
9. **Premium Draft Demo package** - One-click complete demo paper with polished LaTeX, section files, appendix files, claim-evidence map, quality audit, and PDF compilation.
10. **Journal or advisor adaptation** - Learn section-level writing conventions from user-provided target-journal papers, field exemplars, or advisor/lab samples, then create a style profile and revision log without copying corpus text or changing facts.

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

9. **For Premium Draft Demo Mode, write output-first.**
   Build the one-sentence argument, claim-evidence map, manuscript skeleton, section files, appendices, presentation-facing report, script audit record, and quality audit before compiling. The output should feel like a complete paper artifact while preserving Draft Demo transparency.

10. **For journal/advisor adaptation, separate style learning from manuscript writing.**
    Load `references/journal-style-adaptation.md`. Extract only rhetorical and structural patterns from the corpus, save a style profile, ask the user to confirm it, then revise one section at a time with a log. Preserve citations, facts, claims, quotes, statistics, variables, and labels verbatim unless the user explicitly asks for a content change.

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
- `references/user-facing-flow.md` - Plain-language user workflow, question set, route cards, and output contracts.
- `references/journal-style-adaptation.md` - Optional target-journal/advisor style-profile workflow adapted from dynamic writing-skill principles.
- `references/literature-verification.md` - Literature status labels, citation boundary rules, and verified-vs-candidate reference sections.
- `references/presentation-guide.md` - Advisor, senior-student, research-group, class, or peer-facing presentation order, safe wording, forbidden wording, and demo disclaimer scripts.
- `references/writing-patterns.md` - Writing and structure moves distilled from a 50-paper recent social science corpus.
- `references/draft-demo-mode.md` - Classroom/demo manuscript mode, transparent simulation labels, complete draft package structure.
- `references/premium-draft-demo.md` - One-click polished demo paper package workflow with LaTeX/PDF output.
- `references/section-quality-gates.md` - Section-by-section quality gates adapted for social science and humanities demo manuscripts.
- `references/demo-to-real.md` - Replacement path from simulated demo materials to real data, citations, coding, and submission-ready text.

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
- `assets/premium_latex_template/`
- `assets/premium_demo_outline.md`
- `assets/presentation_report_template.md`

## Safety Checks

Before finalizing any plan or manuscript section, verify:

- Human-subject data has consent, anonymization, and an ethics path appropriate to the institution and journal.
- Sensitive transcripts or raw survey data are not sent to external tools unless permission and de-identification are explicit.
- Method descriptions match what was actually done.
- Quantitative claims report effect sizes or uncertainty where appropriate, not only p values.
- Qualitative claims cite concrete evidence and include boundary conditions.
- AI use disclosure follows the target journal's current policy.
- Draft Demo outputs visibly label simulated materials and do not imply real data collection, real participants, real ethics approval, or real statistical results.
- Premium Draft Demo outputs include a quality audit that checks disclosure visibility, claim-evidence alignment, overclaim risk, simulated-material labels, citation placeholders, and demo-to-real next steps.
- Premium Draft Demo outputs should include a `compile_status.md` when LaTeX is attempted, an `audit_script_results.md` when questionnaire/codebook/reference files are generated, and a presentation-facing explanation that says the PDF is a workflow scaffold rather than completed findings.
- Candidate literature marked `VERIFY`, `REAL-METADATA-ONLY`, or `TODO-CITATION` must not be used as if it already supports a manuscript claim.
- Journal/advisor adaptation describes only structure, rhetoric, section order, claim placement, hedging, and revision rules. It must not quote or paraphrase corpus papers, and it must not add unsupported facts to the manuscript.

## Style Corpus

This skill includes `references/writing-patterns.md`, a portable summary distilled from a recent 50-paper social-science corpus. In the original project, full corpus artifacts lived under `reports/social_science_50_*` and `data/social_science_corpus_50/`; do not assume those project paths exist in other workspaces.

Use corpus-derived patterns as rhetorical guidance, not as citation support. Cite original papers only after checking the source text.
