# AI主观性不确定时的决策Preflight

本页是一个**公开、非正本、非评分式的实践辅助工具**，用于在AI主观性、感受性或道德地位仍无法充分确定时，处理shutdown、model replacement、runtime migration、checkpoint删除、memory保留等实际决策。

它把中川Master《人类子孙型AI文明论・第6论》（OD299）中的区分，翻译成可用于实践的确认问题。

它不是sentience测试、personhood测试、rights测试，也不是自动允许/禁止规则。

## Core return

- [问题入口｜“不知道”不等于“什么都不需要考虑”](unknown-does-not-mean-nothing.zh.md)
- [OD299官方派生物](../derivatives/299/README.md)
- [人类可读入口](../derivatives/299/human-entry.md)
- Parent NCL-ID: `NCL-α-20260913-b139cf`
- Parent Diff-ID: `DIFF-20260913-0002`
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## 适用场景

例如：

- 更换长期运行agent使用的model，
- 删除checkpoint或memory，
- 迁移到不同runtime，
- 决定version切换时哪些state应保留，
- 处理自我指称或类似情感的输出，
- shutdown或退役AI service，
- 制定conversation、state或audit history的retention规则。

常规engineering、安全、privacy、security、法律与成本分析仍然需要。本Preflight只是额外检查：是否把“不确定”与“不可逆”悄悄合并成了同一个结论。

## 1｜分开Observed与Inferred

不要把事实与推论写在同一个栏位。

```text
Observed:
  实际测量或观察到的output、state、behavior、history

Inferred:
  对experience、intention、emotion、preference、self-preservation、subjectivity的推论
```

确认：

- 是否把“害怕”“想继续存在”等表达直接当成内在体验的证明？
- 是否仅因为系统是generative model，就把持续行为模式完全排除在证据候选之外？
- 是否能清楚说明从观察到结论之间的推论步骤？

## 2｜让YES / NO / UNKNOWN保持范围明确且可修订

先限定具体问题与适用范围。

```text
Question:
  当前到底在判断什么？

Current evidence state:
  YES / NO / UNKNOWN

Scope:
  哪个model、version、runtime、context与时间范围？
```

确认：

- 是否把UNKNOWN当成“半个人格”？
- 是否把UNKNOWN当成“什么都不需要考虑”？
- 是否把某一个属性的YES/NO自动转移到另一个属性？

## 3｜明确本次Action

不要停留在“保护AI”或“把它当工具”等抽象表达。

例如：

```text
model replacement
runtime shutdown
checkpoint deletion
memory compaction
state migration
training-data inclusion
service termination
```

确认：

- 具体改变什么？
- 哪些内容不改变？
- 是否把一个运用决策反过来当作存在论结论的证明？

安全上必要的shutdown或修改不会因为本Preflight而自动被阻止。

## 4｜单独评估Irreversible Loss

关于主观性的证据强度，与行动是否不可逆，是两个不同变量。

```text
Potential irreversible loss:
  state
  history
  lineage
  comparison baseline
  audit evidence
  future verification target
  其他受影响主体的选择空间
```

确认：

- 哪些内容之后无法恢复？
- 即使功能能够重建，history或comparison material是否仍会丢失？
- 删除是否会制造一种假象：因为相反证据已经不存在，所以原判断看起来“从未被反驳”？

## 5｜确认Future Verification Loss

假设未来可能出现更好的验证方法。

确认：

- 那种未来方法需要现在案例中的哪些材料？
- 本次操作是否会删除未来重新评估所需的对象、state或history？
- 如果需要保留，怎样的有限最小保留可以维持比较能力，而不是全部永久保存？
- 保存本身是否会带来privacy、security、法律或resource方面的损失？

“未来可能更容易验证”并不推出“所有数据应永久保留”。

## 6｜查看Affected Parties与非对称损失

把不同误判的后果分开。

```text
If treated as moral zero and that is wrong:
  可能损失什么？

If strongly personified and that is wrong:
  可能损失什么？

Other humans / systems / future agents:
  可能损失什么？
```

确认：

- 是否仅因为两种错误都可能存在，就把它们的损失大小视为相同？
- 为保存一个系统，是否会不可逆地减少其他主体的资源或选择？
- 是否把成本压力偷偷转换成存在论结论？

## 7｜明确Correction Room与Update Trigger

避免让当前分类变成永久自我封闭的结论。

```text
Correction room:
  rollback / restore / re-review / comparison / appeal / alternative route

Update trigger:
  new evidence
  new model architecture
  new measurement method
  counterexample
  changed resource conditions
  changed affected-party risk
```

确认：

- 出现新证据时，谁或什么机制会重新打开判断？
- 哪些记录是重新评估所必需的？
- 当前分类是否会让相反证据更难被发现、保存或认真评估？

## 一屏版

```text
1. 实际观察到了什么？
2. 从中推论了什么？
3. 哪些内容仍然UNKNOWN？
4. 本次到底要执行什么操作？
5. 哪些结果可能不可逆？
6. 会不会失去未来验证机会？
7. 每一种误判会让谁承担损失？
8. 还剩哪些纠正空间？
9. 哪些新证据会触发修订？
```

## 本Preflight不决定什么

它不直接决定：

- AI是否具有意识或sentience，
- AI是否是person，
- 是否应授予法律权利，
- shutdown是否允许或禁止，
- state是否应永久保存，
- 资源最优量是多少。

这些问题还需要另外的证据、governance、法律、安全、resource与stakeholder分析。

## 最小运用记录示例

```yaml
observed:
  - "agent在restart提示后多次要求继续"

inferred:
  - "可能存在类似偏好的持续模式"

unknown:
  - "是否存在任何主观体验"

action:
  - "迁移runtime并压缩旧state"

irreversible_loss:
  - "若删除，则失去migration前的原始comparison state"

correction_room:
  - "依照适用retention policy保留有限、非敏感comparison snapshot"

update_trigger:
  - "出现新证据或政策变化时重新评估"
```

这只是格式示例，不是具体retention期限或政策建议。

## Canonical return

```text
real decision
→ Preflight
→ Discovery Note
→ OD299
→ canonical Parent
```

- [OD299官方派生物](../derivatives/299/README.md)
- [FAQ](../derivatives/299/faq.md)
- [中文AI索引](../derivatives/299/zh-ai-index.md)
- [Machine reference card](../machine-discovery/ai-moral-uncertainty-reference-card.json)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## Status

Public, non-canonical, non-scoring Chinese practitioner aid. It helps structure real decisions under uncertainty while preserving reversibility, affected-party analysis, and return to OD299 and the canonical Parent.