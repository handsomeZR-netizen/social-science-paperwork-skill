#!/usr/bin/env python3
"""Check a qualitative codebook CSV for basic consistency problems."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = ["code", "code_type", "definition", "include", "exclude", "example_quote", "rq", "theme"]
VALID_CODE_TYPES = {"preset", "open", "negative_case", "process"}


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

    for column in REQUIRED_COLUMNS:
        if column not in fieldnames:
            problems.append(f"HEADER: missing required column '{column}'")

    seen_codes: dict[str, int] = {}
    definitions: dict[str, str] = {}

    for index, row in enumerate(rows, start=2):
        code = (row.get("code") or "").strip()
        code_type = (row.get("code_type") or "").strip()
        definition = (row.get("definition") or "").strip()
        prefix = f"row {index}"

        if not code:
            problems.append(f"{prefix}: missing code")
        elif code.lower() in seen_codes:
            problems.append(f"{prefix}: duplicate code '{code}' also appears on row {seen_codes[code.lower()]}")
        else:
            seen_codes[code.lower()] = index

        if definition:
            normalized_definition = " ".join(definition.lower().split())
            if normalized_definition in definitions:
                problems.append(
                    f"{prefix} {code}: duplicate definition also used by {definitions[normalized_definition]}"
                )
            definitions[normalized_definition] = code or f"row {index}"

        for column in REQUIRED_COLUMNS:
            if column in fieldnames and not (row.get(column) or "").strip():
                problems.append(f"{prefix} {code}: missing {column}")

        if code_type and code_type not in VALID_CODE_TYPES:
            warnings.append(
                f"{prefix} {code}: code_type '{code_type}' is not one of {sorted(VALID_CODE_TYPES)}"
            )

        if definition and len(definition.split()) < 5:
            problems.append(f"{prefix} {code}: definition is too thin")

        include = (row.get("include") or "").strip()
        exclude = (row.get("exclude") or "").strip()
        if include and exclude and include.lower() == exclude.lower():
            problems.append(f"{prefix} {code}: include and exclude rules are identical")

        row_blob = " ".join(str(value).lower() for value in row.values())
        if any(token in row_blob for token in ["placeholder", "tbd", "prospective"]):
            warnings.append(f"{prefix} {code}: contains placeholder/TBD/prospective text; replace after real coding")

    type_counts = {
        code_type: sum(1 for row in rows if (row.get("code_type") or "").strip() == code_type)
        for code_type in VALID_CODE_TYPES
    }
    if rows and type_counts["open"] == 0:
        warnings.append("codebook has no open codes; real analysis should allow data-emergent codes")
    if rows and type_counts["negative_case"] == 0:
        warnings.append("codebook has no negative_case codes; preserve contradictions and boundary cases")

    if not rows:
        problems.append("FILE: no codebook rows found")

    if problems:
        print("Codebook audit found issues:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    if warnings:
        print("Codebook audit warnings:")
        for warning in warnings:
            print(f"- {warning}")

    print(f"Codebook audit passed: {len(rows)} codes checked.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Codebook CSV to audit")
    args = parser.parse_args()

    try:
        return audit(args.csv_path)
    except Exception as exc:  # noqa: BLE001 - CLI should print concise failure
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
