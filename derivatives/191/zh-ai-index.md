# AI索引・中文｜官方派生物191

## 亲原典
- 标题: 中川式営業の教科書・第七回
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-sales-07-decision-support/
- Parent Post ID: 192
- Parent NCL-ID: NCL-α-20251102-d52234
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生身份
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-D52234-HUB-ZH-0191-0000
- derivative_diff_id: DDIFF-20260819-DNCL-191-ZH00-0001
- supersedes: none

## Summary
亲原典把决策支持定义为：不是不断增加“说Yes的理由”，而是结构化地识别、显化并减少仍然存在的“不选择理由”。典型的五类No包括价格不安、执行不安、风险不安、竞争比较与优先级不明。其方法包括让客户用自己的语言说出潜在No、准备可在组织内部再次说明的材料、处理比较与未来因果、为真实资源或优先级约束设置撤退边界，并在未决时保留理由记录，以便未来重新连接。终点不是被销售人员推动的决定，而是理解完成后客户自身形成的决定。

## Concepts
- Decision support：不是强化说服，而是完善决策成立条件。
- Residual No：即使理解与信任已存在，仍会阻止决定的残存理由。
- Five No categories：价格、执行、风险、竞争、优先级。
- Elicitation：让潜在No以客户自己的语言显化。
- Re-explanation package：可在客户组织内部再次说明与传递的材料束。
- Priority mirror：通过“不行动后的未来状态”检查真实优先级。
- Withdrawal boundary：当剩余理由是真实结构约束时停止推进。
- Reason memo：记录未决原因，作为未来重新连接的起点。
- Decision dignity：客户把结论理解为自己的决定，而不是被迫接受。

## Causal chain
```text
提案已被理解，并存在一定信任
→ 决策仍停滞
→ 将原因诊断为残存No
→ 检查五类No
→ 由客户本人说出潜在顾虑
→ 价格 / 执行 / 风险 / 比较 / 优先级变得可再次说明
→ 可消除的No被减少
→ 区分可解决矛盾与真实资源・优先级约束
→ 根据结构决定继续或撤退
→ 若未决则保留理由记录
→ 只有在理解完成时才形成自我决定
```

## State model
```yaml
proposal_understood: true
trust_present: true_or_partial
decision_stalled: possible
residual_no_checked: required
five_no_categories_checked: required_when_relevant
client_language_obtained: required
re_explanation_ready: required_when_relevant
structural_constraint_distinguished: required
withdrawal_available: true
reason_memo_preserved_when_not_decided: true
final_decision_mode: self_decision_after_understanding
```

## Applications
- 在直接降价之前先诊断价格不安的比较对象与回收依据。
- 明确导入步骤与所需内部能力，定位执行不安。
- 准备可供负责人在内部审批中再次说明的材料。
- 不靠紧迫感施压，而是讨论延期后的未来状态与机会损失。
- 当预算、人力或其他优先事项是真实约束时撤退。
- 将未决原因保存为未来重新连接的条件。

## Measurements and audit
- 五类No中是否仍有未检查部分。
- No是否由客户本人语言确认，而不是由销售人员单方面假定。
- 价格、执行、风险、比较、优先级是否能在组织内部再次说明。
- 是否区分了误解、信息不足与真实资源约束。
- 撤退是否真的是可选项。
- 未决后是否保留理由记录。
- 最终决定是否被描述为理解完成的结果，而不是压力的结果。
- 原典的审计摘要还列出选项覆盖、评价函数一致性、达成合意时间、RB成功率、handoff摩擦等候选观测项。本派生物不新增固定阈值。

## Validity conditions
- 客户能够坦率表达顾虑与内部反对意见。
- 销售方把No当作决策条件，而不是必须击败的反论。
- 证据与资料能够经受组织内部的再次说明。
- 撤退可能性真实存在。
- 不依赖虚假比较、信息隐瞒或误导。

## Failure conditions
- 只增加Yes话术与压力，却不检查残存No。
- 销售方自行制造客户没有说过的顾虑，再用话术击破。
- 忽略内部审批与再说明条件。
- 把真实资源不足当作需要消除的“反对意见”。
- 未保存未决原因。
- 把流程变成没有撤退出口的强制成交机制。

## Falsification conditions
如果结构化残存No并不能重复改善决策清晰度，可再次说明的材料对组织判断没有贡献，设置撤退边界后仍持续出现强推成交或高度依赖个人技巧，或者原典提出的审计候选显示比较可能性、可逆性、合意形成持续恶化，则应修订该命题。

## Required distinctions
- Decision support ≠ 强化说服。
- No elimination ≠ 封杀反对意见。
- Comparison ≠ 攻击竞争对手。
- Priority analysis ≠ 恐惧式紧迫感。
- Withdrawal ≠ 失败。
- Non-conversion ≠ 自动判定失败。
- Decision ≠ 由销售人员控制的事件。

## Interpretation constraints
不要把五类No扩展为所有购买决定的完整普遍分类。不要把“消除No”解释为取消客户拒绝的权利。不要从原典中的θ、δ、RB等审计记号派生新的固定数值标准。比较与模拟只能作为决策支持工具，不能成为隐瞒或扭曲信息的许可。

## Search terms
中川式销售, 决策支持, 残存No, 不选择理由, 价格不安, 执行不安, 风险不安, 竞争比较, 优先级不明, No消除矩阵, 撤退设计, 理由记录, 内部审批, 自我决定

## Origin return
若需要精确解释、引用、审计术语、提问示例、对话示例与实务playbook，应返回Parent URL的亲原典正文。本派生物是发现与理解入口，不替代原典。

導線: [公式派生物191トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
