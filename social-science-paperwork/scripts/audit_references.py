#!/usr/bin/env python3
"""Compare manuscript citation keys with BibTeX entries."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.IGNORECASE)
LATEX_CITE_RE = re.compile(r"\\(?:cite|citep|citet|parencite|textcite|autocite)(?:\[[^\]]*\])*\{([^}]+)\}")
PANDOC_CITE_RE = re.compile(r"@([A-Za-z0-9_:\-./]+)")


def split_keys(raw: str) -> list[str]:
    return [key.strip() for key in raw.split(",") if key.strip()]


def extract_manuscript_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in LATEX_CITE_RE.finditer(text):
        keys.update(split_keys(match.group(1)))
    keys.update(match.group(1) for match in PANDOC_CITE_RE.finditer(text))
    return keys


def extract_bib_keys(text: str) -> set[str]:
    return {match.group(1).strip() for match in BIB_ENTRY_RE.finditer(text)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", required=True, type=Path, help="Manuscript text, Markdown, or LaTeX file")
    parser.add_argument("--bib", required=True, type=Path, help="BibTeX file")
    args = parser.parse_args()

    try:
        manuscript = args.manuscript.read_text(encoding="utf-8")
        bib = args.bib.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        manuscript = args.manuscript.read_text(encoding="utf-8-sig")
        bib = args.bib.read_text(encoding="utf-8-sig")
    except Exception as exc:  # noqa: BLE001 - CLI should print concise failure
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    cited = extract_manuscript_keys(manuscript)
    bib_keys = extract_bib_keys(bib)
    missing = sorted(cited - bib_keys)
    unused = sorted(bib_keys - cited)

    print(f"Cited keys: {len(cited)}")
    print(f"BibTeX keys: {len(bib_keys)}")

    if missing:
        print("Missing from BibTeX:")
        for key in missing:
            print(f"- {key}")

    if unused:
        print("Unused BibTeX entries:")
        for key in unused:
            print(f"- {key}")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
