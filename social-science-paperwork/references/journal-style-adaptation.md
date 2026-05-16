# Journal And Advisor Style Adaptation

Use this reference when the user wants the manuscript to fit a target journal, course, advisor, lab, or sample-paper style.

This is adapted from dynamic writing-skill workflows such as `WantongC/journal-adapt-writing-skill`, but narrowed for social science and humanities writing.

## What To Learn

Extract only structural and rhetorical patterns:

- abstract move order
- introduction opening type
- gap and contribution placement
- literature review organization
- method transparency level
- findings/result narration style
- discussion scope
- limitation placement
- hedging level
- transition style
- section length and paragraph job

Never quote, paraphrase, or reproduce corpus paper content.

## Inputs To Ask For

1. Target journal, course, advisor, or writing destination.
2. Primary corpus folder: 3-8 target-journal or target-style papers in Markdown/text if possible.
3. Optional secondary corpus: 2-5 high-quality similar papers.
4. Optional advisor/lab/user exemplar files.
5. Manuscript or section to revise.
6. Sections to revise: abstract, introduction, literature review, method, findings/results, discussion, conclusion, or full paper.

If the corpus is PDF-only, offer conversion but do not require a specific converter. Markdown/text is preferred.

## Priority System

- **P1 Hard preserve**: facts, citations, citation keys, quoted data, participant IDs, numerical results, statistics, variable names, labels, tables, figures, and section claims.
- **P2 Target destination**: patterns repeated across the primary corpus.
- **P3 Secondary corpus or advisor/lab exemplars**: use when P2 is absent or weak.
- **P4 Social-science base rules**: evidence boundary, method transparency, ethics, no overclaiming.
- **P5 Cleanup**: remove AI-taste phrases, hollow transitions, unsupported contribution claims, and vague overstatements.

P1 always wins. If P2 conflicts with P4, explain the conflict and ask the user if it affects research integrity.

## Style Profile Output

Save or present:

```markdown
# Style Profile: [destination]

## Corpus
- Primary papers: [N]
- Secondary papers: [N]
- User/lab exemplars: [N]

## Section Patterns
| Section | Observed pattern | Strength | Source role |
|---|---|---|---|

## Red Flags
- [patterns absent from target corpus or risky for this manuscript]

## Revision Rules
| Rule | Applies to | Priority | Rationale |
|---|---|---|---|
```

## Human Gate

Before revising the manuscript, show the style profile and ask:

> Does this profile match the journal/advisor style you want? If yes, I will apply it section by section. If not, tell me what to adjust.

Do not begin revision until the user confirms or gives revised instructions.

## Section Revision Process

For each section:

1. Diagnose paragraphs:
   - problem type: STYLE, JOURNAL-MISMATCH, AI-TASTE, LOGIC, EVIDENCE-BOUNDARY
   - severity: high, medium, low
   - fit score: 1-5
2. Revise only what can be revised without changing facts.
3. Produce a revision log:
   - paragraph number
   - issue
   - rule applied
   - preserved elements
   - remaining risk
4. Move to the next section only after completing the current one.

## Output Directory

Use:

`[manuscript_name]_style_adapted/`

Create:

- `style_profile.md`
- `[section]_diagnosis.md`
- `[section]_revised.md`
- `[section]_revision_log.md`
- `revision_summary.md`

## Safety Boundaries

- Do not add new literature, facts, findings, data, or claims.
- Do not weaken ethics, limitations, or AI disclosure to mimic a journal.
- Do not rewrite participant quotes unless the user explicitly asks for translation or anonymization.
- Do not use target-corpus style as evidence for the user's substantive claims.
