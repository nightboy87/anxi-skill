# Script Validation

Scripts are executable behavior, so script patches require stronger proof than Markdown patches.

## Rules

1. Modify `scripts/` only when `target_move` explicitly depends on script behavior.
2. Every script patch must list validation commands.
3. Prefer existing tests when available.
4. If no tests exist, run the smallest smoke test such as `python scripts/name.py --help`.
5. A script patch cannot be accepted if validation fails.
6. Do not use natural-language judgment as a substitute for executable validation.

## Validation Discovery

Look for:

```text
tests/
pyproject.toml
pytest.ini
package.json
scripts/*.py --help
```

## Decision Language

Use precise status:

```text
Verified by running: <command>
Not verified because: <reason>
Rejected because validation failed: <command>
```
