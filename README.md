# anxi-skill

> 教练，我想练 Skill。

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/883565ab-b515-4afd-ab59-74f1a562defe" />


有些 Skill 刚出生的时候很有天赋。

它能在 demo 里暴扣，能靠大模型的身体素质硬吃几个回合，能在群里被人夸“这个 prompt 写得好”。

但一到需要稳定出手的关键场景，它就开始：

- 该收束时继续抒情；
- 该追问时直接开写；
- 该小改时整包重构；
- 该记住教训时下次换个发型又来；
- 该练中投时，非要从三分线外闭眼起跳。

这时候你不能只喊“加油”。

也不能跟它说“你很有潜力，再试试”。

你需要一个教练。

`anxi-skill` 就是这个教练。

它不会上来就把你的 Skill 改成另一个人。  
它只问一个问题：

> 这次，我们到底要练稳哪个动作？

---

## 一句话介绍

`anxi-skill` 是一个本地 Agent Skill，用来**训练、优化和修复完整的 Agent Skill package**。

它不是 PromptOps 平台。  
不是云端评估系统。  
不是全自动提示词炼丹炉。  
更不是那种一开口就说“我帮你整体优化一下”，然后把你的整包洗成企业白皮书的热心同学。

它做的事情很克制：

> 选定一个不稳定动作，生成有边界的候选补丁，展示修改依据，让人类决定是否接受，并把训练记录留下来。

---

## 为什么叫 anxi？

这是一个教练隐喻。

一个冷静的教练不会说：

> 你很有天赋，继续冲。

他会说：

> 今天先练这个动作。  
> 不是全国大赛。  
> 不是重建篮球馆。  
> 就这个点，练到稳定为止。

对 Skill 来说也一样。

一个 Skill 靠模型能力可以临场发挥，但这不等于它拥有稳定能力。  
真正可靠的能力，需要训练：

- 目标明确；
- 动作可拆；
- 修改有界；
- 结果可验；
- 失败可记；
- 下一轮不再犯同一个错。

所以 `anxi-skill` 的核心精神是：

> 不是重写 Skill，而是训练 Skill。

---

## 它训练的不是一份孤零零的 Markdown

`anxi-skill` 面向的是**完整 Skill package**，而不只是 `SKILL.md`。

典型结构：

```text
skill/
|-- SKILL.md
|-- references/
|-- assets/
|-- scripts/
|-- agents/openai.yaml
`-- tests/ 或项目自带验证命令
```

很多 Skill 的问题不只在主提示词里。

有时候是：

- `SKILL.md` 触发条件太宽，逮谁练谁；
- `references/` 里的判断标准太虚，读完跟没读一样；
- `assets/` 里的模板不够收束，越补越长；
- `scripts/` 能跑，但边界没验证；
- `examples/` 没覆盖真实失败场景；
- `agents/openai.yaml` 描述太浪，调度器都看懵了。

所以 `anxi-skill` 训练的是整个包。

不是只给主角换发型。

---

## 什么时候该叫教练上场？

当你发现一个 Skill 出现下面这些症状时。

### 1. 一改就整包重写

你只是想让它少追问一句。

结果 AI 给你重构了：

- 使命；
- 愿景；
- 方法论；
- 世界观；
- 三年路线图；
- 以及一段看起来像上市公司年报的结语。

这不是训练。  
这是拆馆。

### 2. 修好一个问题，撞坏三个旧能力

你修了“不要过度心理化”。  
结果它开始变得像流程机器人。

你修了“多给行动建议”。  
结果它开始每次输出十条计划。

你修了“语气更有力量”。  
结果它突然开始给用户打鸡血。

这就是典型的打地鼠式修改：

> 一个洞按下去，三个洞冒出来。

### 3. Skill 越改越长，动作越来越虚

`SKILL.md` 从 200 行变成 900 行。

每一条都看起来有道理。  
每一段都像是为了防止上一次出错。  
最后模型读完以后，像刚跑完两万圈操场：

> 道理都懂，但手已经不会投了。

### 4. 同一个错误下次换个发型又来了

你明明上次已经拒绝过这个方向：

> 不要把用户原话改成正确废话。

下次 AI 换了个说法回来：

> 为了提升表达的专业性，我建议将用户的原始表述规范化为……

不行。  
这个错误动作必须进错题本。

### 5. 你说不清哪里不好，但就是觉得不对

有些问题不是“错了”，而是：

- 味道没了；
- 原话被洗平了；
- 该停的地方没停；
- 该问的地方没问；
- 该收束时还在抒情；
- 该上场时还在热身；
- 明明只是要练中投，它突然开始研究球队文化。

这时候 `anxi-skill` 会先帮你把模糊不满收束成一个具体的 `target_move`。

目标没收束前，不动文件。

---

## 典型使用方式

你可以这样说：

```text
使用 anxi-skill 训练这个 skill：path/to/skill

这次 target_move 是：
减少过度追问，同时保留必要澄清。
```

或者：

```text
使用 anxi-skill 训练这个 skill：path/to/skill

我说不清它哪里不好。
大概是：输出越来越完整，但越来越没劲。
请先帮我收束 target_move，不要直接改文件。
```

`anxi-skill` 会先判断：

```text
这次到底是在练什么动作？
```

可能收束成：

```text
target_move:
在保留用户高能原话的前提下，把输出收束成一个 7 天内可执行的小实验。
```

然后才进入训练。

先确定练什么，再开始训练。  
不要上来就全国大赛。

---

## 它实际会做什么？

完整流程：

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

重点不是“AI 帮你改了”。  
重点是：

> AI 不能趁你不注意，把整个 Skill 改成另一个人。

---

## 核心概念

### target_move：这次只练一个动作

`target_move` 是本轮训练目标。

好的 `target_move`：

```text
减少过度追问
稳定输出 7 天小实验
避免心理诊断
更准确判断何时调用图片
减少文章评审中的空泛评价
```

不好的 `target_move`：

```text
优化一下
写好一点
更高级
更完整
更像专家
```

如果你的目标太虚，`anxi-skill` 会先帮你收束。

教练不会让你今天同时练投篮、传球、防守、体能、战术和人生意义。

---

### bounded patch：有界补丁

`anxi-skill` 默认**不整包重写**。

它优先生成局部补丁：

```text
insert_after
insert_before
replace_block
delete_block
append_to_section
```

默认每轮最多 **3 个补丁**。

因为训练不是一口气把人改造成全国第一。  
训练是：

> 今天先把这个动作练稳。  
> 不拆球馆。

---

### validation：验收

如果一个补丁改了 `scripts/`，它**必须声明并运行验证命令**。

比如：

```bash
python scripts/check_skill_structure.py .
python scripts/validate_patch_yaml.py assets/candidate-patch-template.yaml
python -m unittest tests.test_scripts -v
```

自然语言说：

> 我觉得没问题。

不算验证。

这最多算教练推了推眼镜，不代表测试通过。

---

### rejected buffer：拒绝缓冲区

被拒绝的修改不会消失。  
它会进入 rejected buffer，成为下次训练的负面记忆。

记录内容包括：

```text
这次想怎么改
为什么看起来合理
为什么被拒绝
下次应该避免什么
```

因为一个错误动作如果不记录，它下次会换个姿势回来：

> “这次我不是整包重写，我只是系统性重构一下你的全部表达框架。”

不，你还是想拆馆。

---

### training log：训练日志

每次训练都会留下记录，包括：

```text
目标 Skill
本轮 target_move
候选补丁
用户决策
接受项
拒绝项
验证结果
下一轮观察点
```

这让你以后能回答一个非常关键的问题：

> 当初为什么加了这条规则？

如果回答不上来，那它大概率不是训练，是冲动消费。

---

## 它会碰哪些文件？

`anxi-skill` 会根据训练目标判断可能涉及的文件。

常见范围：

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

- `SKILL.md`：主入口，负责触发条件、角色边界和核心流程。
- `references/`：长规则、判断标准、训练流程和验收边界。
- `assets/`：画像、计划、候选补丁、日志、拒绝记录和检查报告模板。
- `scripts/`：只读检查和确定性校验。
- `tests/`：脚本测试。
- `examples/`：训练样例和演示场景。

如果补丁涉及 `scripts/`，必须运行验证。  
如果补丁只涉及文案规则，也必须展示 diff 和修改理由。  
没人能在教练眼皮底下蒙混过关。

---

## 它不会做什么？

V0.1 不提供：

- Web UI
- GitHub Action
- 云端平台
- 自动 PR
- 复杂 benchmark
- 默认整包重写
- 数据库
- 团队权限系统
- 生产链路追踪
- 自动证明新版一定更好

它不是：

```text
PromptOps 平台
LLMOps 平台
自动提示词优化器
云端评测系统
```

它只是一个本地训练教练。

功能边界很简单：

> 读取一个 Skill package，围绕一个 target_move，生成有限候选补丁，让人类确认，并把训练记录留下来。

---

## 和普通“AI 优化提示词”有什么不同？

普通做法：

```text
帮我优化一下这个 Skill。
```

结果：

```text
AI：没问题，我给你一个更完整、更专业、更系统的版本。
```

危险信号已经出现了。

`anxi-skill` 的做法：

```text
你要训练哪个动作？
为什么它现在不稳定？
哪些东西不能动？
这次最多改几个点？
补丁依据是什么？
你接受还是拒绝？
拒绝原因要不要写入记录？
```

普通 AI 像热血队友：

> 交给我，我来！

`anxi-skill` 像教练：

> 先别燃。  
> 动作变形了。

---

## 和 SkillOpt 有什么关系？

`anxi-skill` 受到 SkillOpt 一类工作的启发。

SkillOpt 证明了一个重要方向：

> Skill 文档可以被当成冻结 Agent 的外部可训练状态，通过有界编辑、验证门、拒绝缓冲区等机制进行优化。

但 `anxi-skill` 不复现完整 SkillOpt。

它不做大规模 benchmark。  
不做自动训练平台。  
不追求学术实验矩阵。  
不把人类从流程里拿掉。

`anxi-skill` 做的是更轻的事情：

> 把“有界编辑 + 验收 + 拒绝记忆”这套训练纪律，放进普通 Skill 作者能用的本地开发流程里。

---

## 本地验证

当前仓库包含以下检查脚本：

```bash
python scripts/check_skill_structure.py .
python scripts/validate_patch_yaml.py assets/candidate-patch-template.yaml
python -m unittest tests.test_scripts -v
```

如果你修改了结构、模板或脚本，请至少运行这些检查。

如果你改了 `scripts/` 却不运行测试，教练会沉默。  
但那种沉默通常不是认可。

---

## 适合加入 Git 的训练产物

建议保留：

```text
assets/*-template.*
references/*.md
examples/*.md
scripts/*.py
tests/*.py
```

可选保留：

```text
training-log
rejected buffer
check report
candidate patch
```

如果训练记录包含敏感项，可以脱敏后再提交。

---

## 公开使用时的注意事项

`anxi-skill` 使用的是“教练训练”隐喻。

请不要在项目中使用任何受版权保护的角色形象、官方台词、截图或作品名营销。

可以使用：

- 教练；
- 训练场；
- 投篮训练；
- 稳定动作；
- 两万次练习；
- 不靠天赋硬吃；
- 赛后复盘。

不要使用：

- 具体漫画角色名；
- 原作截图；
- 官方台词；
- 同人头像；
- 易被误解为官方授权的视觉。

我们致敬的是训练精神，不是复刻 IP。

---

# English Version

> Coach, I want to train my Skill.

Some skills are born talented. They can dunk. They can rebound. They can survive a few rounds on raw model athleticism.

But when the task gets specific, they wobble:

- they keep writing when they should narrow down;
- they ask more questions when they should act;
- they rebuild the whole package when one patch would do;
- they forget the same rejected idea — and next week it comes back with a new haircut;
- they grow longer while the actual move gets weaker.

That’s when you need a coach.  
`anxi-skill` is that coach.  
It doesn’t rewrite your skill into a different player.  
It asks one question first: **What move are we training this time?**

---

## What is anxi-skill?

`anxi-skill` is a local Agent Skill for **training, improving, and repairing complete Agent Skill packages**.

It is not a PromptOps platform.  
It is not a cloud evaluator.  
It is not an automatic prompt optimizer.  
It is not the friend who says “I improved the whole thing” and returns a corporate whitepaper wearing your Skill’s jacket.

It does one focused thing:

> Pick one unstable move, generate bounded candidate patches, show the rationale, let a human accept or reject them, and preserve the training record.

---

## It trains a package, not a lonely Markdown file

```text
skill/
|-- SKILL.md
|-- references/
|-- assets/
|-- scripts/
|-- agents/openai.yaml
`-- tests/
```

A skill’s problem is rarely just inside `SKILL.md`.  
`anxi-skill` treats the whole package as the training surface.

---

## Core Concepts

- **target_move** — one round trains one unstable move. (“Reduce over-questioning”, not “Make it better”.)
- **bounded patch** — local edits only (`insert`, `replace`, `delete`, `append`). Default budget: 3 patches.
- **human-on-the-loop** — every candidate patch must be Approved, Rejected, Edited or Skipped by a human.
- **rejected buffer** — rejected ideas are recorded as negative memory, so the same bad move doesn’t return next week in a different jacket.
- **validation** — patches to `scripts/` must declare and run verification commands. “Looks fine to me” is not a test.

---

## What V0.1 does NOT do

- Web UI
- GitHub Action
- cloud platform
- automatic PRs
- complex benchmarks
- default full-package rewrites
- database
- team permissions
- production tracing
- automatic proof that the new version is better

It is a local training coach. Nothing more, nothing less.

---

## Local Checks

```bash
python scripts/check_skill_structure.py .
python scripts/validate_patch_yaml.py assets/candidate-patch-template.yaml
python -m unittest tests.test_scripts -v
```

If you touch `scripts/` without running the tests, the coach will be silent.  
That silence is not approval.
