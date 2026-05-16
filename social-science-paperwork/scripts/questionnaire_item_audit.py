#!/usr/bin/env python3
"""Audit questionnaire item metadata for common social-science design risks."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from collections import Counter


REQUIRED_COLUMNS = [
    "construct",
    "dimension",
    "item_id",
    "item_text",
    "response_scale",
    "source",
    "reverse_coded",
]

DOUBLE_BARRELED = re.compile(
    r"\b(and|or)\b|/|;|, and |, or ",
    re.IGNORECASE,
)
LEADING_PATTERNS = [
    re.compile(r"\b(obviously|clearly|undoubtedly|excellent|best|should)\b", re.IGNORECASE),
    re.compile(r"^(do you agree|don't you think|wouldn't you say)\b", re.IGNORECASE),
]
VAGUE_PATTERNS = [
    re.compile(r"\b(often|usually|regularly|sometimes|many|few|good|bad)\b", re.IGNORECASE),
]


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        return reader.fieldnames, list(reader)


def audit(path: Path) -> int:
    fieldnames, rows = read_rows(path)
    problems: list[str] = []
    warnings: list[str] = []
    missing_columns = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
    for name in missing_columns:
        problems.append(f"HEADER: missing required column '{name}'")

    seen_ids: set[str] = set()
    seen_text: dict[str, str] = {}
    construct_counts: Counter[str] = Counter()

    for index, row in enumerate(rows, start=2):
        item_id = (row.get("item_id") or "").strip()
        text = (row.get("item_text") or "").strip()
        construct = (row.get("construct") or "").strip()
        source = (row.get("source") or "").strip()
        notes = (row.get("notes") or "").strip()
        prefix = f"row {index}"
        if construct:
            construct_counts[construct] += 1

        if not item_id:
            problems.append(f"{prefix}: missing item_id")
        elif item_id in seen_ids:
            problems.append(f"{prefix}: duplicate item_id '{item_id}'")
        seen_ids.add(item_id)

        normalized_text = re.sub(r"\s+", " ", text.lower())
        if normalized_text:
            if normalized_text in seen_text:
                problems.append(f"{prefix}: duplicate item_text also used by {seen_text[normalized_text]}")
            seen_text[normalized_text] = item_id or f"row {index}"

        for column in REQUIRED_COLUMNS:
            if column in fieldnames and not (row.get(column) or "").strip():
                problems.append(f"{prefix}: missing {column}")

        if text:
            word_count = len(re.findall(r"\w+", text))
            if word_count > 35:
                problems.append(f"{prefix} {item_id}: item is long ({word_count} words)")
            if DOUBLE_BARRELED.search(text):
                problems.append(f"{prefix} {item_id}: possible double-barreled wording")
            if any(pattern.search(text) for pattern in LEADING_PATTERNS):
                problems.append(f"{prefix} {item_id}: possible leading or evaluative wording")
            if any(pattern.search(text) for pattern in VAGUE_PATTERNS):
                problems.append(f"{prefix} {item_id}: contains vague or context-dependent wording")

        reverse = (row.get("reverse_coded") or "").strip().lower()
        if reverse and reverse not in {"yes", "no", "true", "false", "1", "0", "y", "n"}:
            problems.append(f"{prefix} {item_id}: reverse_coded should be yes/no or true/false")
        if reverse in {"yes", "true", "1", "y"}:
            warnings.append(f"{prefix} {item_id}: reverse-coded item needs cognitive/pilot testing")

        source_blob = f"{source} {notes}".lower()
        if any(token in source_blob for token in ["requires source verification", "tbd", "placeholder"]):
            warnings.append(f"{prefix} {item_id}: source or note is unresolved; verify literature source before fielding")

    for construct, count in sorted(construct_counts.items()):
        if count < 3:
            warnings.append(
                f"construct '{construct}' has {count} item(s); formal scale measurement usually needs at least 3"
            )

    if not rows:
        problems.append("FILE: no questionnaire items found")

    if problems:
        print("Questionnaire audit found issues:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    if warnings:
        print("Questionnaire audit warnings:")
        for warning in warnings:
            print(f"- {warning}")

    print(f"Questionnaire audit passed: {len(rows)} items checked.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Questionnaire item CSV to audit")
    args = parser.parse_args()

    try:
        return audit(args.csv_path)
    except Exception as exc:  # noqa: BLE001 - CLI should print concise failure
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
