# AI索引・中文｜官方派生物192

## Parent original
- Parent title: 中川式営業の教科書・第七回
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-sales-07-decision-support/
- Parent Post ID: 192
- Parent NCL-ID: NCL-α-20251102-d52234
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## Derivative identity
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-D52234-HUB-ZH-0192-0002
- derivative_diff_id: DDIFF-20260819-DNCL-192-0002-0001
- supersedes: none

## Summary
亲原典把中川式销售中的决策支持定义为：不是通过说服、施压成交或不断增加“Yes”来推动客户，而是**识别并结构化消除“不选择的理由”，使理解完成后，决策由客户自身自然成立**。

当提案已经被理解、基础信任也已存在，但决策仍然停滞时，原典不把问题简单归因于热情不足，而是检查仍然存在的“No”。这些No主要分为五类：价格不安、执行不安、风险不安、竞争比较、优先顺序不明确。它们并不只是谈判现场的反对意见，也会在客户内部审批与再次说明时重新出现。

因此，销售方需要让客户本人说出阻碍决策的理由，并把价格依据、实施步骤、风险应对、比较轴以及延迟实施所产生的机会损失，转换为客户可以在组织内部再次说明的决策材料。目标不是压制抵抗，而是区分能够通过理解解决的阻碍，与应当被尊重的真实限制。

撤退是必要边界。如果残留理由来自可澄清的核心价值冲突，可以继续对话；如果它来自真实的资源限制或优先顺序本身，则原典允许并要求撤退，而不是强迫成交。即使没有成交，也应记录未决理由，使其成为未来重新连接时可比较的结构性信息。

原典的综合审计摘要进一步把决策支持视为由需求、假设、选项、评价函数、阈值θ、反例、RB条件与一次记录等组成的结构化运作。选项覆盖率、评价函数一致性、达成共识时间、RB成功率、交接摩擦等可作为观察点，但本派生物不新增任何普遍固定阈值。

## Concepts
- 决策支持
- 消除不选择的理由
- 残留No
- 价格不安
- 执行不安
- 风险不安
- 竞争比较
- 优先顺序不明确
- 内部审批
- 事前提问
- 假设设计
- 再说明材料
- 可比较性
- 因果镜
- 机会损失
- 客户自我言语化
- 排除矩阵
- 未决理由记录
- 撤退设计
- 重新连接
- 评价函数
- 阈值θ
- 反例
- RB
- 一次记录

## Causal chain
```text
提案已被理解 + 基础信任存在
↓
决策仍然延迟
↓
不把问题视为Yes不足，而是识别残留No
↓
分解为价格 / 执行 / 风险 / 竞争 / 优先顺序
↓
让客户本人说出实际阻碍理由
↓
使价格依据、实施、风险应对、比较与未来损失可被再次说明
↓
支持内部审批与比较
↓
从客户自身的决策结构内部减少可解决的No
↓
若为可澄清的核心价值冲突则继续对话
↓
若为真实资源限制或优先顺序则撤退
↓
理解完成，或未决理由被明确
↓
自主决策或未来重新连接成为可能
```

## State model
```yaml
- proposal_understood
- trust_present
- decision_deferred
- residual_no_identified
- five_no_categories_checked
- customer_verbalization_obtained
- internal_reexplanation_supported
- comparison_axis_visible
- implementation_path_visible
- risk_response_visible
- priority_consequence_visible
- residual_no_reduced
- value_conflict_distinguished
- resource_constraint_distinguished
- withdrawal_available
- understanding_completed_or_nondecision_explained
- autonomous_decision_preserved
- reconnection_record_preserved
```

## Applications
- 在B2B提案停滞时，以五类残留No诊断原因，而不是追加成交压力。
- 分解实施步骤，区分可以解决的不确定性与真实资源不足。
- 让竞争比较基于客户实际评价轴，而不是只比较价格。
- 通过“如果半年后仍未实施会怎样”等问题，让客户自己说明优先顺序与机会损失。
- 将未成交原因保存为结构记录，用于未来重新连接时比较条件变化。

## Measurements and audit
- 五类残留No的确认覆盖情况
- 阻碍理由是否由客户本人明确表达
- 提案是否能够在客户内部再次说明
- 选项之间是否具有可比较性
- 评价标准是否保持一致
- 达成共识前的返工程度
- RB / 撤退是否保留可逆性
- 交接时的说明摩擦
- 是否出现施压成交
- 是否回到对特定销售个人的依赖
- 是否能够记录未决理由
- 重新连接时是否能追踪理由变化

## Validity conditions
- 把决策支持保持为减少残留No，而不是增加Yes。
- 保持五类No的区分。
- 客户本人的言语化优先于销售方的推测。
- 把再说明材料连接到内部审批。
- 区分可解决阻碍与真实资源限制、优先顺序。
- 保留撤退作为正式选择。
- 将未决理由保存为未来重新连接的信息。

## Failure conditions
- 把模型缩减为成交技巧或反对意见处理。
- 由销售方单方面定义客户的No。
- 仅通过增加压力、利益或说明量制造更多Yes。
- 抹平五类No之间的差异。
- 用说服覆盖真实资源限制或优先顺序。
- 删除撤退可能性。
- 把“自然决定”解释为由销售方操控的必然结果。

## Falsification conditions
按照亲原典的综合审计摘要，如果选项覆盖、评价函数一致性、达成共识时间、RB成功率、交接摩擦等观察结果与假设不一致，或者流程出现施压销售、重新依赖个人等现象，则应部分否定或修订这种结构化决策支持假设。本派生物不自行设定固定数值阈值。

## Required distinctions
- 增加Yes / 消除No
- 说服 / 理解完成
- 处理反对意见 / 客户本人表达理由
- 销售资料 / 可在内部重复使用的决策材料
- 核心价值冲突 / 资源限制
- 继续对话 / 撤退
- 失单 / 重新连接记录
- 让对方决定 / 对方自己决定

## Interpretation constraints
不要把“消除No”解释为剥夺拒绝权或操纵心理抵抗。其含义是明确决策条件，并且只减少能够正当解决的阻碍。如果资源限制或优先顺序仍然存在，撤退必须继续可用。θ、RB等符号与审计术语不得被扩展为亲原典中不存在的固定KPI。

## Search terms
中川式销售; 决策支持; 不选择的理由; 残留No; 价格不安; 执行不安; 风险不安; 竞争比较; 优先顺序; 内部审批; 再说明材料; 排除矩阵; 撤退设计; 重新连接; 评价函数; 阈值θ; RB; 交接摩擦

## Origin return
关于五类No、具体提问、再说明材料、撤退边界、排除矩阵、20项检查表、综合审计摘要与局部审计摘要，应返回Parent URL、Parent Post ID 192、Parent NCL-ID `NCL-α-20251102-d52234`、Parent Diff-ID `DIFF-20251102-0001`、Origin `Nakagawa Master`进行确认。

---
導線: [公式派生物192トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)