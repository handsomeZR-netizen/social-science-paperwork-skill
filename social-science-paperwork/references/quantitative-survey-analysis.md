# Quantitative Survey Analysis

## Before Analysis

Create a data dictionary:

- Variable name.
- Label.
- Construct.
- Item text.
- Scale anchors.
- Reverse-coded status.
- Missing value codes.
- Source.

Check whether the data match the research design before running models.

## Cleaning Checks

Record decisions for:

- Duplicate submissions.
- Consent failures.
- Completion time thresholds.
- Attention checks.
- Straight-lining.
- Missingness.
- Outliers.
- Reverse coding.
- Scale score calculation.

Never let AI invent or "repair" missing responses.

## Typical Analysis Sequence

1. Descriptive statistics.
2. Missingness and response quality.
3. Reliability for multi-item scales.
4. EFA if dimensions are exploratory and sample size allows.
5. CFA if a prior measurement model is being tested and sample size allows.
6. Correlation matrix.
7. Regression, ANOVA, SEM, mediation, or moderation only when theory supports it.
8. Robustness or sensitivity checks.

## Reliability And Validity

Report reliability with interpretation. Cronbach's alpha is not validity. If a scale has multiple dimensions, reliability should be checked by dimension.

For EFA/CFA, report enough detail for review:

- KMO and Bartlett test if using EFA.
- Extraction and rotation choices.
- Factor loadings and cross-loadings.
- Fit indices for CFA when applicable.
- Item deletion rationale.

## Reporting

Use cautious language:

- "was associated with" for cross-sectional relation.
- "predicted" only in a statistical model sense unless design supports temporal prediction.
- "effect" only for experiments or defensible causal designs.

Include effect sizes, confidence intervals, and assumptions where appropriate.

## Starter R Script

Use `scripts/survey_analysis_skeleton.R` after copying it into the project. It assumes a CSV file and common packages but leaves construct-specific model choices to the researcher.
