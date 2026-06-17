# Rejected Memory

Rejected changes are training data, not waste.

## Location

Each target skill package stores rejected memory in:

```text
.anxi/rejected.md
```

## Required Entry

```markdown
## REJECTED-YYYYMMDD-HHMM-PATCH-ID

target_move:
target_file:
patch_id:

### Rejected change

### Why it looked reasonable

### User rejection reason

### Risk it would introduce

### Avoid next time
```

## Usage Rule

Before generating new patches, read `.anxi/rejected.md` if it exists and avoid repeating rejected directions. If a new patch resembles a rejected direction, either skip it or explicitly explain why the new context is different.
