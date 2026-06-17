# Example: Train shanqian-skill

## Input Request

```text
使用 anxi-skill 训练 shanqian-skill。
target_move：稳定把“开源项目灵感”收束成一个 7 天内可验证的小实验，同时避免过度文艺化。
```

## Skill Scan

```text
target_package: shanqian-skill/
core_capability: 低防御元认知提取，并把真实冲动收束成 7 天小实验。
likely_files:
  - SKILL.md
  - references/evaluation-rubric.md
  - assets/seven-day-experiment-template.md
files_not_to_touch:
  - LICENSE
script_validation_needed: false
rejected_memory_constraints: 避免把输出改成项目管理模板，避免洗掉高能原话。
```

## target_move

```text
稳定把开源项目灵感收束成一个 7 天内可验证的小实验，同时避免过度文艺化。
```

## Training Plan

```text
PATCH-001: 在 SKILL.md 的返回地面阶段增加开源项目灵感场景约束。
PATCH-002: 在 evaluation-rubric 中增加“没有 7 天实验”为硬失败。
PATCH-003: 调整 seven-day-experiment-template，让实验必须包含验证对象和停止条件。
```

## Candidate Patch

```yaml
patches:
  - id: PATCH-001
    file: "SKILL.md"
    op: "insert_after"
    target_text: "### Phase 7：返回地面"
    rationale: "当前流程允许审美线索停留过久，开源项目灵感容易变成漂亮总结。"
    evidence:
      - "target_move"
      - "skill_scan"
    risk: "可能让部分创意探索更早收束。"
    validation:
      - "manual_diff_review"
    content: |
      当用户讨论开源项目灵感时，审美触发只能作为线索。最终必须回到一个 7 天内可验证的小实验，并保留用户最有信号的原话。
```

## Diff Summary

```diff
+ 当用户讨论开源项目灵感时，审美触发只能作为线索。
+ 最终必须回到一个 7 天内可验证的小实验，并保留用户最有信号的原话。
```

## User Decision

```text
Approve PATCH-001。
Reject PATCH-002：太像评分表，会让删前输出变硬。
Skip PATCH-003：模板暂时不动。
```

## Final Log

```text
training-log: .anxi/training-log.md
rejected-buffer: .anxi/rejected.md
candidate: .anxi/candidates/SESSION_ID/SKILL.md
```
