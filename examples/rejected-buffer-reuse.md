# Example: Rejected Buffer Reuse

## Input Request

```text
使用 anxi-skill 继续训练 shanqian-skill。
target_move：减少输出里的正确废话。
```

## Existing Rejected Memory

```markdown
## REJECTED-20260617-1430-PATCH-002

target_move: 稳定输出 7 天小实验
target_file: SKILL.md
patch_id: PATCH-002

### User rejection reason

这条会让输出太像项目管理模板，丢掉删前的原话感。

### Avoid next time

不要用标准项目管理模板替代用户高能原话。
```

## Skill Scan

```text
rejected_memory_constraints:
  - 不要用项目管理模板替代高能原话
  - 不要把输出改成通用效率工具话术
```

## Training Plan

```text
PATCH-001: 在输出评估标准中增加“正确废话”反例。
PATCH-002: 在报告模板中保留最多 3 条用户原话，先于总结出现。
Skipped direction: 不新增标准项目管理表格。
```

## Candidate Patch

```yaml
patches:
  - id: PATCH-001
    file: "references/evaluation-rubric.md"
    op: "append_to_section"
    target_text: "## 四、是否避免了正确废话"
    rationale: "目标是减少正确废话，同时 rejected buffer 禁止改成项目管理模板。"
    evidence:
      - "target_move"
      - "rejected_buffer"
    risk: "如果写得太硬，可能压掉用户原话的粗糙感。"
    validation:
      - "manual_diff_review"
    content: |
      如果一条修改把用户原话替换成“提升效率、优化体验、形成闭环”等通用表达，应判为退化。
```

## Diff Summary

```diff
+ 如果一条修改把用户原话替换成“提升效率、优化体验、形成闭环”等通用表达，应判为退化。
```

## User Decision

```text
Approve PATCH-001。
Rejected buffer was used to avoid a previously rejected project-management-template direction.
```

## Final Log

```text
training-log notes rejected-memory reuse under "Package scan summary" and "Candidate patches".
```
