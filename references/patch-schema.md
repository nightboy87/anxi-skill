# Candidate Patch Schema

Candidate patches use YAML and must be reviewable before application.

## Required Shape

```yaml
patches:
  - id: PATCH-001
    file: "SKILL.md"
    op: "insert_after"
    target_text: "## Workflow"
    rationale: "Why this patch is needed."
    evidence:
      - "target_move"
      - "package_scan"
    risk: "What could get worse."
    validation:
      - "manual_diff_review"
    content: |
      New content here.
```

## Supported Ops

```text
insert_after
insert_before
replace_block
delete_block
append_to_section
replace_file_candidate
```

## Forbidden Defaults

```text
rewrite_full_package
rewrite_full_skill
delete_resource_dir
change_public_identity_without_confirmation
```

## File Rules

- `file` must be a relative path inside the skill package.
- `scripts/` patches must include at least one executable validation command.
- `delete_block` must include `target_text`.
- `replace_file_candidate` is allowed only for generated candidate output, not direct overwrite.
