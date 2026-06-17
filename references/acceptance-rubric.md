# Acceptance Rubric

Use this rubric before marking a training round complete.

## Score

Score each item 0-2.

```text
target_move focus:
bounded edit:
skill identity preservation:
package role fit:
rejected-memory compliance:
script validation, if applicable:
version safety:
encoding and line endings:
```

## Hard Failures

Reject the candidate if any occur:

```text
Unconfirmed full-package rewrite
Treats package as a single prompt
Touches scripts without validation
Deletes unapproved reference or asset content
Repeats rejected direction
Changes public trigger/display identity without risk note
Claims improvement without evidence
Overwrites original files by default
Writes candidates without session_id, base_version, or candidate_version
Adds UTF-8 BOM or line-ending-only noise to candidate files
```
