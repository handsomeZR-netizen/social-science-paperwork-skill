# Qualitative Coding

## Analysis Routes

Choose one route and name it:

- **Reflexive thematic analysis** - Identify patterned meaning across data.
- **Codebook thematic analysis** - Use a structured codebook with coder agreement.
- **Grounded theory** - Build categories and a process model from data.
- **Content analysis** - Classify text using predefined or emergent categories.
- **Discourse analysis** - Study language, power, identity, and meaning-making.

Do not mix labels casually. The method name implies different standards.

## Evidence Chain

Maintain:

`Transcript excerpt -> initial code -> focused code -> theme/category -> analytic claim`

For every major theme, preserve:

- Definition.
- Inclusion and exclusion rules.
- Representative quotes.
- Negative or deviant cases.
- Researcher memo.
- Link to RQ.

Use `assets/codebook_template.csv` as a starter.

## Codebook Fields

Recommended columns:

`code,code_type,definition,include,exclude,example_quote,source_id,rq,theme,memo`

Use codes that are specific enough to guide coding, but not so narrow that each code appears once.

Use `code_type` values such as:

- `preset` - theory- or RQ-informed starting code.
- `open` - code emerging from data.
- `negative_case` - contradiction, deviant case, or boundary condition.
- `process` - action sequence or mechanism.

Do not let preset codes crowd out emerging codes. A usable codebook should leave space for conflict, failure, silence, refusal, market constraints, institutional pressure, identity, policy, intellectual property, and other unexpected categories when the data support them.

## Coder Consistency

If multiple coders are used:

- Train on a subset.
- Compare disagreements.
- Revise definitions.
- Document adjudication.
- Report agreement only when it fits the analytic approach.

For reflexive thematic analysis, do not force inter-rater reliability if the method treats interpretation as researcher-situated. Instead report reflexive memoing and analytic transparency.

## Audit Script

Use:

```bash
python scripts/codebook_consistency_check.py assets/codebook_template.csv
```

The script checks missing definitions, duplicate codes, empty examples, and thin inclusion/exclusion rules.
