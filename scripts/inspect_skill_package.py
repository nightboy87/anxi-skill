#!/usr/bin/env python3
"""Inspect a skill package and print a JSON package map."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def list_files(root: Path, directory: str) -> list[str]:
    base = root / directory
    if not base.is_dir():
        return []
    return sorted(
        rel(path, root)
        for path in base.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    )


def detect_validation_commands(root: Path) -> list[str]:
    commands: list[str] = []
    if (root / "tests").is_dir():
        if (root / "pyproject.toml").is_file() or (root / "pytest.ini").is_file():
            commands.append("python -m pytest")
        else:
            commands.append("python -m unittest discover")
    if (root / "package.json").is_file():
        commands.append("npm test")
    for script in sorted((root / "scripts").glob("*.py")) if (root / "scripts").is_dir() else []:
        commands.append(f"python {rel(script, root)} --help")
    return commands


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print("usage: inspect_skill_package.py <skill-package-dir>")
        return 0

    if len(argv) < 2:
        print("usage: inspect_skill_package.py <skill-package-dir>", file=sys.stderr)
        return 2

    root = Path(argv[1]).resolve()
    if not root.exists() or not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    entrypoints = [name for name in ["SKILL.md", "AGENTS.md"] if (root / name).is_file()]
    agent_metadata = [rel(path, root) for path in [root / "agents" / "openai.yaml"] if path.is_file()]
    validation_commands = detect_validation_commands(root)
    missing = []
    if "SKILL.md" not in entrypoints:
        missing.append("SKILL.md")

    payload = {
        "root": str(root),
        "root_type": "skill_package" if "SKILL.md" in entrypoints else "unknown",
        "files": {
            "entrypoints": entrypoints,
            "references": list_files(root, "references"),
            "assets": list_files(root, "assets"),
            "scripts": list_files(root, "scripts"),
            "agent_metadata": agent_metadata,
            "tests": list_files(root, "tests"),
        },
        "validation": {
            "candidate_commands": validation_commands,
            "script_validation_needed": bool(list_files(root, "scripts")),
        },
        "missing": missing,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
