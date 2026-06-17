# Example: Train a Script-Containing Skill

## Input Request

```text
使用 anxi-skill 训练 pdf-skill。
target_move：旋转 PDF 时不要静默覆盖原文件。
```

## Skill Scan

```text
target_package: pdf-skill/
core_capability: 使用 scripts/ 中的 PDF 工具处理文件。
likely_files:
  - SKILL.md
  - scripts/rotate_pdf.py
  - tests/test_rotate_pdf.py
files_not_to_touch:
  - references/pdf-format.md
script_validation_needed: true
available_validation_commands:
  - python -m pytest tests/test_rotate_pdf.py
  - python scripts/rotate_pdf.py --help
```

## target_move

```text
旋转 PDF 时默认生成新文件，不静默覆盖原文件。
```

## Training Plan

```text
PATCH-001: 在 SKILL.md 中声明默认不覆盖输入文件。
PATCH-002: 修改 scripts/rotate_pdf.py，使 --output 成为必需参数或自动派生安全输出名。
PATCH-003: 增加测试覆盖无 --output 时的输出路径行为。
```

## Candidate Patch

```yaml
patches:
  - id: PATCH-002
    file: "scripts/rotate_pdf.py"
    op: "replace_block"
    target_text: "output_path = input_path"
    rationale: "当前脚本可能覆盖原文件，与 target_move 冲突。"
    evidence:
      - "target_move"
      - "script_scan"
    risk: "调用方如果依赖原地覆盖，需要改为显式传入输出路径。"
    validation:
      - "python scripts/rotate_pdf.py --help"
      - "python -m pytest tests/test_rotate_pdf.py"
    content: |
      output_path = args.output or derive_rotated_output_path(input_path)
```

## Diff Summary

```diff
- output_path = input_path
+ output_path = args.output or derive_rotated_output_path(input_path)
```

## User Decision

```text
Approve after validation.
Verified by running:
  python scripts/rotate_pdf.py --help
  python -m pytest tests/test_rotate_pdf.py
```

## Final Log

```text
training-log records validation commands and pass/fail output.
candidate mirrors changed scripts/ and tests/ files.
```
