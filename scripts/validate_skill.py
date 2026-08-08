#!/usr/bin/env python3
"""Validate PM Especialista structure and behavioral eval contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFS = ROOT / "references"
EVALS = ROOT / "evals" / "cases.json"
REQUIRED_EVAL_KEYS = {"id", "prompt", "expected_references", "must", "must_not", "max_references"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name: pm-especialista" not in text:
        fail("SKILL.md frontmatter is invalid")

    references = sorted(REFS.glob("*.md"))
    if len(references) != 28:
        fail(f"expected 28 reference files, found {len(references)}")

    cited = set(re.findall(r"references/[a-z0-9-]+\.md", text))
    missing = sorted(path for path in cited if not (ROOT / path).exists())
    if missing:
        fail("SKILL.md cites missing references: " + ", ".join(missing))

    data = json.loads(EVALS.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if len(cases) < 6:
        fail("at least 6 behavioral evals are required")

    ids = set()
    for case in cases:
        missing_keys = REQUIRED_EVAL_KEYS - case.keys()
        if missing_keys:
            fail(f"eval missing keys {sorted(missing_keys)}: {case}")
        if case["id"] in ids:
            fail(f"duplicate eval id: {case['id']}")
        ids.add(case["id"])
        if len(case["expected_references"]) > case["max_references"]:
            fail(f"{case['id']} exceeds max_references")
        for path in case["expected_references"]:
            if not (ROOT / path).exists():
                fail(f"{case['id']} cites missing reference: {path}")

    prioritization = (REFS / "prioritization-craft.md").read_text(encoding="utf-8")
    if "use 80% if unsure" in prioritization:
        fail("RICE still assigns 80% confidence when evidence is missing")

    print(f"OK: 1 skill, {len(references)} references, {len(cases)} behavioral evals")


if __name__ == "__main__":
    main()
