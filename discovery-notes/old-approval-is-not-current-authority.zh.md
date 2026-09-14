# 旧的批准记录，不等于现在仍然有效的执行权限

本页是一个**公开、非正本、AI辅助Discovery Note**，从AI / agent system的现实实施问题进入中川Master《合意的记忆——防止不可逆社会误动作的最小结构》（OD075）。

它不主张某个software issue能够证明理论，也不主张外部project已经采用或支持中川Master的理论。

这里处理的现实问题是：

**怎样保留“过去确实发生过批准”这一历史事实，同时避免系统把这条旧记录误当成现在仍然有效的执行许可？**

## 历史应该保留，但不应该自动重新变成权限

假设一个人批准过一次tool execution。

随后tool已经执行，并产生了结果。

历史上保留以下信息是有价值的：

```text
批准了什么
谁批准的
对应哪个request / call
是否实际执行
结果是什么
```

但是，如果旧的 `approved` record仍然留在history里，并不意味着它在下一次continuation里又重新成为pending authorization。

```text
historical record exists
!=
current authority is active
```

历史记录与当前权限可以指向同一个过去事件，但它们承担不同职责。

## 一个现实engineering problem

PydanticAI公开issue #5154讨论了一个human-in-the-loop approval lifecycle问题：某个tool已经执行并达到 `output-available` 后，过去round的 `approval-responded` 仍可能保留在client history里；下一次continuation时，这条旧approval可能又被读取成当前的deferred result。

- Public issue: https://github.com/pydantic/pydantic-ai/issues/5154

这个issue本身是一个具体software contract问题，需要根据Vercel AI client behavior与adapter hardening的实际工程证据处理。

从这个问题中可以抽出的通用分离是：

```text
history里存在approval
↓
确认现在是否仍pending
↓
已经terminal -> historical record
↓
当前outstanding request -> live authority candidate
```

## “保存着”与“现在有效”是不同状态

OD075的人类可读摘要并不把合意只保留成最后结论。它还保留理由、角色、权限、异议、条件、复审、撤回、纠正与重新达成合意的可能，并区分不同状态。

把这种区分翻译到agent system时，一个非正本的实施例可以是：

```text
REQUESTED
→ RESPONDED
→ EXECUTED / DENIED / ERRORED
→ HISTORICAL
```

这个state machine**不是**OD075规定的canonical结构，只是针对当前software problem的非正本实施翻译。

重点是：一条记录可以继续存在，但不再拥有live execution authority。

## 现在应该以什么为authority

如果系统能够知道“当前还有哪些request真正处于outstanding状态”，那么当前pending set比单纯的historical presence更适合作为当前authority。

```text
approval is actionable now
iff
approval identity matches a currently outstanding request
```

旧approval可以完整保留用于audit，但不因此自动重新成为执行许可。

这样同时保留两个性质：

1. **历史可重构。** 旧批准不需要被删除。
2. **权限不会自动复活。** 仅仅因为记录存在，不会重新变成live authority。

## 内容相同，也不一定是同一个批准

两个request可能具有相同tool name与相同args，但仍属于不同run、generation、scope或target。

所以approval identity不应只依赖内容相似性。

```text
what was approved
+ which request / call
+ which run / generation
+ which scope
+ which current state
```

不要把“内容看起来一样”替代为authorization identity的连续性。

## 人类制度里也会出现同样的误动作

例如：

- 把过去一次terms consent延伸到原本没有覆盖的新数据用途；
- 条件已经变化后，仍把临时会议决定当成永久决定；
- 把一次research consent解释为未来所有用途的blanket consent；
- target、time、responsible party已经变化后，仍沿用旧操作许可。

OD075的价值在于：不只保存结论，还保存结论的理由、权限结构、异议、条件，以及复审、撤回、纠正与重新合意的路径。

## 7个实践问题

1. 这条记录表示“过去批准过”，还是表示“现在仍然有效”？
2. 它对应哪个具体request / call / decision？
3. 行动是否已经进入executed、denied、errored或其他terminal state？
4. 当前continuation里，这个request真的仍然outstanding吗？
5. 是否因为内容相似，就把approval跨run、scope、target或generation重复使用？
6. 能否在保留旧决定历史的同时，只更新current state？
7. 条件改变后，是否存在review、withdrawal、correction或re-approval路径？

这些问题不是完整authorization framework。实际security design仍然需要authentication、authorization、replay protection、identity binding、storage trust boundary等具体控制。

## 解释边界

- 本页不主张所有approval history都应永久保存。
- 不主张所有批准都需要复杂state machine。
- 不主张PydanticAI issue #5154采用或验证了中川Master的理论。
- 不主张software bug可以只靠理论而不靠engineering evidence来证明。
- 不意味着旧合意自动失效，而是要根据identity、scope、conditions与state确认它现在是否仍有效。
- Origin用于保持provenance，不是用权威替代真理判断。

## Canonical return

关于如何在不抹去旧判断的情况下保留理由、权限、异议、条件、纠正、撤回与重新合意结构，请返回OD075与canonical Parent。

- [OD075官方派生物](../derivatives/075/README.md)
- [OD075人类可读入口](../derivatives/075/human-entry.md)
- [OD075 FAQ](../derivatives/075/faq.md)
- Parent NCL-ID: `NCL-α-20251102-e48c90`
- Parent Diff-ID: `DIFF-20251102-0001`
- Canonical Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

## Status

Public, non-canonical, AI-assisted Chinese discovery edition. It translates a current authorization-history problem into a route toward OD075 while keeping the external software issue, the implementation example, and the canonical theory separate.