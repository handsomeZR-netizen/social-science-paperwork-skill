# Questionnaire Design

## Construct First

Do not start by writing questions. Start with:

- Research question.
- Construct name.
- Operational definition.
- Dimensions.
- Existing scale or source.
- Target population.
- Planned analysis.

Every item should map to one construct and one dimension.

## Item Rules

Good questionnaire items are:

- One idea only.
- Short and concrete.
- Matched to the respondent's experience.
- Neutral, not leading.
- Time-bounded when necessary.
- Written at a consistent reading level.
- Paired with an appropriate response scale.

Avoid:

- Double-barreled items: "useful and enjoyable".
- Leading items: "How important is this excellent program..."
- Vague frequency: "often", "regularly" without a defined period.
- Loaded terms: "backward", "advanced", "authentic" unless defined.
- Mixed direction without clear reverse coding.
- Demographic questions not needed for analysis.

## Scale Selection

Common response formats:

- 5- or 7-point Likert agreement.
- Frequency.
- Importance.
- Satisfaction.
- Semantic differential.
- Multiple choice.
- Open-ended supplement.

Keep anchors consistent. If using reverse-coded items, flag them clearly in the data dictionary and test whether respondents understand them.

## Reliability And Validity

Plan before collecting data:

- Content validity: expert review or literature-grounded item sources.
- Face validity: pilot participants understand the items.
- Construct validity: EFA/CFA where sample size and theory allow.
- Reliability: Cronbach's alpha or omega for multi-item scales.
- Criterion validity: relation to an external criterion if available.

Do not report alpha as proof of validity. High alpha can mean redundant items.

For formal multi-item constructs, use at least three well-justified items per construct when feasible. Two-item constructs may be acceptable for exploratory description, but they are weak for reliability, factor analysis, and publication-grade measurement unless strongly justified.

Treat "literature-derived" as incomplete until a real source, adaptation rationale, translation/back-translation decision, and pilot evidence are recorded.

## Pilot Test

Pilot with a small group resembling the target population. Record:

- Completion time.
- Ambiguous items.
- Sensitive or uncomfortable items.
- Missing response options.
- Technical problems.
- Items with low variance.

Revise before formal collection.

## Audit Script

Use:

```bash
python scripts/questionnaire_item_audit.py assets/questionnaire_template.csv
```

Expected columns:

`construct,dimension,item_id,item_text,response_scale,source,reverse_coded,notes`
