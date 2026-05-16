# Premium Draft Demo Mode

Use this reference when the user wants a one-click, polished, complete social-science or humanities demo paper, especially with LaTeX/PDF output.

## Purpose

Premium Draft Demo Mode should produce a finished-looking artifact for classroom, peer, or supervisor presentation. It is not a real empirical paper. The output must be beautiful, coherent, and self-contained, while every simulated element remains visibly marked.

## Mandatory Output Package

Default output directory:

`reports/social_science_premium_demo_paper/paper/`

Create:

- `main.tex`
- `sections/00_abstract.tex`
- `sections/01_introduction.tex`
- `sections/02_literature_framework.tex`
- `sections/03_research_questions.tex`
- `sections/04_methodology.tex`
- `sections/05_illustrative_findings.tex`
- `sections/06_discussion.tex`
- `sections/07_conclusion.tex`
- `appendix/interview_protocol.tex`
- `appendix/questionnaire_demo.tex`
- `appendix/codebook_demo.tex`
- `demo_disclosure.tex`
- `quality_audit.md`
- `main.pdf` when XeLaTeX or latexmk is available.

## Writing Order

Do not write in raw manuscript order. Build the argument first:

1. **One-sentence argument**
   `In [setting], this demo shows how [topic] can be studied through [approach], supported by [real inputs + simulated evidence], within [boundary].`
2. **Claim-evidence map**
   For each major claim, state the evidence type and whether it is real, proposed, or simulated.
3. **Manuscript spine**
   Context -> gap -> framework -> research questions -> method -> illustrative findings -> discussion -> demo-to-real path.
4. **Section drafting**
   Write each section with one rhetorical job per paragraph.
5. **Quality audit**
   Check disclosure, unsupported claims, fake citations, findings labels, and real-data replacement needs.
6. **Compile**
   Use XeLaTeX for Chinese output.

## Premium Quality Rules

- The manuscript should read like a complete paper, not a workflow note.
- Use section-level transitions, not isolated bullet advice.
- Use tables, a workflow figure, callout boxes, and appendices for a polished artifact.
- Keep demo labels visible but not so intrusive that the paper stops looking professional.
- Cite real user-provided sources only. If citation support is missing, insert `% TODO: verify citation` in LaTeX and list it in `quality_audit.md`.
- Never write "we interviewed", "participants reported", "the survey found", or p values unless real data was provided.

## Default LaTeX Style

- Use `ctexart` and XeLaTeX for Chinese manuscripts.
- Use warm but restrained colors suitable for the topic.
- Use `tcolorbox` for disclosure and evidence boundary boxes.
- Use `booktabs`, `tabularx`, and small appendices for methods artifacts.
- Keep the main paper around 10-15 pages unless the user requests otherwise.

## Borrowed Quality Principles

Use these principles, adapted from high-impact writing workflows:

- Argument before sentences.
- Reader order: relevance -> novelty -> trust -> reuse -> meaning.
- Hourglass structure: broad problem to specific gap in Introduction, then wider implications in Discussion.
- One paragraph, one job.
- Claim near evidence.
- Calibrate verbs: `shows` only for real evidence; `illustrates`, `demonstrates the workflow`, or `would support` for simulated material.
- Run an overclaim check before final output.
