# Literature Verification

Use this reference whenever a workflow includes literature matrices, citation placeholders, target-journal landscape results, or candidate papers.

## Status Labels

Use one of these labels for every literature row or citation candidate:

| Label | Meaning | Can support manuscript claim? |
|---|---|---|
| `REAL-VERIFIED` | Full text was read or provided, and the exact claim support was checked. | Yes |
| `REAL-METADATA-ONLY` | Title/abstract/metadata are real, but the full text was not checked. | No |
| `VERIFY` | Candidate source that may be relevant but still needs verification. | No |
| `TODO-CITATION` | A claim needs support but no specific source has been verified. | No |
| `BACKGROUND-ONLY` | Useful context, not direct evidence for a claim. | No |
| `DRAFT-SIM` | Simulated demo material. | No |

## Matrix Columns

For demo or real workflows, prefer these columns:

```csv
status,cite_key,authors,year,title,source,method,topic_fit,claim_supported,verified_anchor,notes
```

Rules:

- `claim_supported` must stay empty or `none yet` unless status is `REAL-VERIFIED`.
- `verified_anchor` should contain page, section, paragraph, DOI landing page note, or local file anchor when available.
- Do not use DOI/title alone as evidence that a paper supports a sentence.
- If the user only has metadata, write "candidate literature" instead of "supporting literature."

## Manuscript Sections

When references are incomplete, create three sections:

1. **Verified references used for claims** - only `REAL-VERIFIED`.
2. **Candidate references to verify** - `REAL-METADATA-ONLY` and `VERIFY`.
3. **Citation TODOs** - claims that still need sources.

In LaTeX, if no verified references exist, write a boundary note instead of a fake bibliography:

```tex
\section*{Reference Boundary}
No verified reference list is generated in this demo. Candidate papers are listed in the audit file and must be checked before they support manuscript claims.
```

## Advisor/Presentation Language

Safe wording:

- "These are candidate papers for the next verification step."
- "This gap is based on the current target-journal metadata screen."
- "This sentence needs a verified source before submission."

Unsafe wording:

- "The literature proves..."
- "These papers already support..."
- "The reference list is complete..."
- "The paper is ready to submit..."
