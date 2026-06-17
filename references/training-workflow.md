# Training Workflow

Use a PDCA loop for each training round.

## Plan

Inputs:

```text
target skill package
user request
optional failure/success examples
existing .anxi/rejected.md
```

Outputs:

```text
target_move
package scan
file impact estimate
acceptance criteria
validation plan
```

Do not edit files during Plan.

## Do

Generate at most 3 candidate patches. Each patch must include:

```text
id
file
op
target_text when applicable
rationale
evidence
risk
validation
content
```

## Check

Show diff and evaluate:

```text
Does it train only target_move?
Does it preserve skill identity?
Does it avoid rejected directions?
Does it require script validation?
Did validation pass?
```

## Act

Record the user's decision:

```text
Approve: write candidate files and training log
Reject: write rejected entry with avoid-next-time guidance
Edit: record user edit reason and candidate delta
Skip: record no change for this patch
```

## Versioned Candidate Rule

Never overwrite the target skill package during a training round. Every accepted candidate must be written to:

```text
.anxi/candidates/<session_id>/
```

Each session must record:

```text
session_id
base_version
candidate_version
changed_files
validation_status
```

Use git commit hash as `base_version` when the target package is a git repository. If git is unavailable, use a timestamp plus a file manifest hash or write `base_version: unversioned-<timestamp>`.
