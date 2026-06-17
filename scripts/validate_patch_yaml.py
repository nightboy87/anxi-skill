#!/usr/bin/env python3
"""Validate the small YAML subset used by anxi candidate patches."""

from __future__ import annotations

import sys
from pathlib import Path


ALLOWED_OPS = {
    "insert_after",
    "insert_before",
    "replace_block",
    "delete_block",
    "append_to_section",
    "replace_file_candidate",
}

REQUIRED_FIELDS = {"id", "file", "op", "rationale", "risk", "content"}


def clean(value: str) -> str:
    value = value.strip()
    if value in {"|", ">"}:
        return value
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_patch_subset(text: str) -> list[dict[str, object]]:
    patches: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    active_list_key: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "patches:":
            continue

        if stripped.startswith("- id:"):
            current = {"id": clean(stripped.split(":", 1)[1])}
            patches.append(current)
            active_list_key = None
            continue

        if current is None:
            continue

        if stripped.startswith("- ") and active_list_key:
            current.setdefault(active_list_key, [])
            value = clean(stripped[2:])
            casted = current[active_list_key]
            if isinstance(casted, list):
                casted.append(value)
            continue

        if ":" in stripped and not stripped.startswith("- "):
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = clean(value)
            if value == "":
                current[key] = []
                active_list_key = key
            else:
                current[key] = value
                active_list_key = None

    return patches


def validate(patches: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    if not patches:
        return ["patches must contain at least one patch"]

    for index, patch in enumerate(patches, 1):
        patch_id = str(patch.get("id", f"#{index}"))
        missing = sorted(field for field in REQUIRED_FIELDS if field not in patch)
        for field in missing:
            errors.append(f"{patch_id}: missing required field: {field}")

        op = patch.get("op")
        if op and op not in ALLOWED_OPS:
            errors.append(f"{patch_id}: unsupported op: {op}")

        filename = str(patch.get("file", ""))
        validation_cmds = patch.get("validation", [])
        if filename.startswith("scripts/") and not validation_cmds:
            errors.append(f"{patch_id}: script patch requires validation")

        if patch.get("op") in {"delete_block", "replace_block", "insert_after", "insert_before"}:
            if "target_text" not in patch:
                errors.append(f"{patch_id}: {patch.get('op')} requires target_text")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print("usage: validate_patch_yaml.py <patch-yaml>")
        return 0

    if len(argv) < 2:
        print("usage: validate_patch_yaml.py <patch-yaml>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.is_file():
        print(f"ERROR: not a file: {path}")
        return 2

    patches = parse_patch_subset(path.read_text(encoding="utf-8"))
    errors = validate(patches)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: {path} contains valid anxi candidate patches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
