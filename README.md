# anxi-skill

> 教练，我想训练 Skill。

有些 skill 改着改着，就像在门口低着头说：

> 教练，我想打篮球。

`anxi-skill` 听完以后不会配乐，也不会拍肩膀说“你已经很努力了”。它会把这个 skill 拉到训练场上：先看它哪个动作不稳定，再给它一个有边界的候选补丁，最后让人类决定要不要收下。

简单说，`anxi-skill` 是一个本地 Agent Skill，用来训练、优化和修复完整的 Agent Skill package。

它训练的是完整 skill package，不是孤零零一份 Markdown。

```text
skill/
|-- SKILL.md
|-- references/
|-- assets/
|-- scripts/
|-- agents/openai.yaml
`-- tests/ 或项目自带验证命令
```

## 它适合什么时候用

当你发现一个 skill 有这种症状：

- 说好只练投篮，结果把篮球馆拆了重建。
- 一改就整包重写，像是换了个人。
- 修好一个问题，又撞坏三个旧能力。
- 每次都说“这次我懂了”，下次还是重犯。
- `SKILL.md` 越改越长，动作却越来越虚。
- 明明只想调一个行为，最后被写成了平台战略。

这时可以让 `anxi-skill` 介入。

典型请求：

```text
使用 anxi-skill 训练这个 skill：path/to/skill
这次 target_move 是：减少过度追问，同时保留必要澄清。
```

如果你还说不清要练哪个动作，它会先帮你收束成一个具体 `target_move`。目标没收束前，不动文件。

先确定练什么，再开始训练。不要上来就“全国大赛”。

## 它实际会做什么

```text
读取目标 skill package
-> 生成 skill 画像
-> 收束 target_move
-> 判断涉及文件范围
-> 生成训练计划
-> 等待用户确认
-> 生成候选补丁
-> 展示 diff
-> 记录 Approve / Reject / Edit / Skip
-> 如涉及 scripts，运行验证
-> 生成 candidate package
-> 写入 training-log 与 rejected buffer
```

重点不是“AI 帮你改了”。重点是：它不能趁你不注意把整包拆了重练。

## 它会碰哪些文件

```text
SKILL.md
agents/openai.yaml
references/
assets/
scripts/
tests/
examples/
```

大致分工：

- `SKILL.md`：主入口，负责触发条件和核心流程。
- `references/`：长规则、判断标准、训练流程和验收边界。
- `assets/`：画像、计划、候选补丁、日志、拒绝记录和检查报告模板。
- `scripts/`：只读检查和确定性校验。
- `tests/`：脚本测试。
- `examples/`：训练样例。

## 它不会做什么

V0.1 不提供：

- Web UI
- GitHub Action
- 云端平台
- 自动 PR
- 复杂 benchmark
- 默认整包重写

如果一个补丁想改 `scripts/`，它必须声明并运行验证命令。自然语言说“我觉得没问题”不算训练完成，只算教练皱眉。

## 本地验证

```bash
python scripts/check_skill_structure.py .
python scripts/validate_patch_yaml.py assets/candidate-patch-template.yaml
python -m unittest tests.test_scripts -v
```

---

# anxi-skill

> Coach, I want to train my Skill.

Some skills eventually stand at the gym door and say:

> Coach, I want to play basketball.

`anxi-skill` does not start the soundtrack. It brings the skill onto the court, identifies one unstable move, turns it into a bounded candidate patch, and asks a human whether the change should be accepted.

In plain terms, `anxi-skill` is a local Agent Skill for training, improving, and repairing complete Agent Skill packages.

It trains a complete skill package, not a lonely Markdown file.

```text
skill/
|-- SKILL.md
|-- references/
|-- assets/
|-- scripts/
|-- agents/openai.yaml
`-- tests/ or project validation commands
```

## When To Use It

Use `anxi-skill` when a skill shows symptoms like:

- it promised to practice shooting and somehow rebuilt the entire gym
- one small edit turns into a personality transplant
- fixing one case breaks three old behaviors
- the same rejected idea keeps coming back with a new haircut
- `SKILL.md` gets longer while the actual move gets weaker
- a behavior tweak somehow becomes a platform strategy

Example:

```text
Use anxi-skill to train this skill: path/to/skill
This target_move is: reduce over-questioning while preserving necessary clarification.
```

If the goal is vague, `anxi-skill` clarifies the `target_move` before editing files.

Choose the move before training. Do not start with the national tournament arc.

## What It Does

```text
scan target skill package
-> build skill profile
-> clarify target_move
-> identify affected files
-> create training plan
-> wait for user confirmation
-> generate candidate patches
-> show diff
-> record Approve / Reject / Edit / Skip
-> run validation when scripts are involved
-> create candidate package
-> write training-log and rejected buffer
```

The point is not that AI can edit files. The point is that it cannot quietly rewrite the whole package while looking confident.

## Boundaries

V0.1 does not include:

- Web UI
- GitHub Action
- cloud platform
- automatic PRs
- complex benchmarks
- default full-package rewrites

If a patch changes `scripts/`, it must declare and run validation commands. "Looks fine to me" is not a test.

## Local Checks

```bash
python scripts/check_skill_structure.py .
python scripts/validate_patch_yaml.py assets/candidate-patch-template.yaml
python -m unittest tests.test_scripts -v
```
