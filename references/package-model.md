# Skill Package Model

anxi-skill trains a complete skill directory, not only `SKILL.md`.

## File Roles

| Path | Role | Typical training reason |
|---|---|---|
| `SKILL.md` | Trigger metadata, main workflow, boundaries, output rules | Behavior is unstable, too vague, too verbose, or missing guardrails |
| `references/` | Long-form method docs, rubrics, domain knowledge | Judgment criteria or detailed procedure is wrong or incomplete |
| `assets/` | Templates, report formats, examples, reusable output skeletons | Output shape is unstable or templates cause bad behavior |
| `scripts/` | Deterministic tools or code helpers | Executable behavior is wrong or repeated code should become deterministic |
| `agents/openai.yaml` | UI metadata and default prompt | Discovery, display, or default invocation is inaccurate |
| `tests/`, `pyproject.toml`, `package.json` | Validation surfaces | Script or package changes need executable verification |

## Scan Requirements

Before proposing patches, answer:

```text
Core capability:
Likely files for target_move:
Files not to touch:
Script validation needed:
Rejected-memory constraints:
Available validation commands:
```

## Touch Rules

- Prefer the smallest file set that can stabilize the target move.
- Keep `SKILL.md` concise; move long guidance to `references/`.
- Touch `assets/` when the issue is output structure or reusable template wording.
- Touch `scripts/` only when the unstable behavior is executable or deterministic.
- Touch `agents/openai.yaml` only when trigger/display/default prompt behavior is part of the target move.
- Preserve the original package by writing candidate files under `.anxi/candidates/<session_id>/`.
- Treat `.anxi/` as training state, not as part of the skill's public runtime surface unless the user explicitly chooses to publish it.
