#!/usr/bin/env python3
"""Validate the anxi-skill package structure."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/package-model.md",
    "references/training-workflow.md",
    "references/patch-schema.md",
    "references/script-validation.md",
    "references/rejected-memory.md",
    "references/acceptance-rubric.md",
    "assets/skill-scan-template.md",
    "assets/training-plan-template.md",
    "assets/candidate-patch-template.yaml",
    "assets/training-log-template.md",
    "assets/rejected-entry-template.md",
    "assets/check-report-template.md",
    "scripts/inspect_skill_package.py",
    "scripts/validate_patch_yaml.py",
]

REQUIRED_DIRS = ["references", "assets", "scripts", "agents"]


def has_frontmatter(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    frontmatter = parts[1]
    return "name:" in frontmatter and "description:" in frontmatter


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print("usage: check_skill_structure.py [skill-package-dir]")
        return 0

    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    errors: list[str] = []

    if not root.exists() or not root.is_dir():
        print(f"ERROR: not a directory: {root}")
        return 2

    for directory in REQUIRED_DIRS:
        if not (root / directory).is_dir():
            errors.append(f"missing directory: {directory}")

    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            errors.append(f"missing file: {filename}")

    skill_file = root / "SKILL.md"
    if skill_file.is_file() and not has_frontmatter(skill_file):
        errors.append("SKILL.md must contain YAML frontmatter with name and description")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: {root} has the required anxi-skill structure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
