# 官方派生物291｜中文 AI 索引

## Parent identity
- Parent title: 中川式 接続価値会計 標準 v0.9──束指標・要旨フォーマット・監査APIの公開可能最小核
- 中文说明: 中川式连接价值会计标准 v0.9——指标束、审计摘要与审计API的公开最小核心
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-accounting-standard-v09/
- Parent Post ID: 317
- Parent NCL-ID: NCL-α-20251102-7308d5
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master
- Derivative NCL-ID: DNCL-NCL-ALPHA-20251102-7308D5-AI-ZH-0291-0002
- Derivative Diff-ID: DDIFF-20260828-DNCL-291-0002-0001
- supersedes: none

## Summary
本原典提出“连接价值会计”v0.9的公开最小核心。它不是把关系、协作或人的价值换算成价格或总分，而是建立一种可审计的测量语言：保留非价格化、指标束、可逆性优先、分散观察和移动目标五项原则。

公开指标束包括CDI、MAI、RS、CRI、KQI；结构记录包括MemoryObject、ConsentToken、ReversibilityFlag、ObservationNote。审计摘要分开记录目的、对象、方法、结果、变更、限制和复现线索。公开API示例包括 `/v0/summary`、`/v0/observations`、`/v0/memory`，但PII与内部权重不应默认公开。

## Concepts
- **非价格化**: 不把连接价值直接压缩成货币。
- **指标束**: 多个指标并读，而不是合成最终排名。
- **可逆性优先**: 比高分更重视修正、撤回和回滚能力。
- **分散观察**: 避免单一观察者垄断价值定义。
- **移动目标**: 指标被攻略时，可以留下理由和历史后修订。
- **CDI**: Connection Density Index。
- **MAI**: Mutual Agreement Interval。
- **RS**: Reversibility Score。
- **CRI**: Consistency of Review & Inspection。
- **KQI**: Qualitative Impact Quotient。
- **MemoryObject**: 可追踪的连接记忆单元。
- **ConsentToken**: 同意条件记录。
- **ReversibilityFlag**: 回滚／修正状态。
- **ObservationNote**: 观察者、方法和语境记录。

## Causal chain
```text
连接产生价值变化
→ 单一价格/分数会损失语境
→ 非价格化
→ 指标束多面观察
→ 记录同意与可逆性
→ 分散观察
→ 审计摘要保留方法与限制
→ API只公开安全最小信息
→ PII/内部权重留在公开面之外
→ 监测指标游戏化
→ 必要时修订指标设计
→ 形成不依赖总价格的可审计连接价值语言
```

## State model
```yaml
monetization: not_required
metric_bundle: active
CDI: observed
MAI: observed
RS: observed
CRI: observed
KQI: observed
consent: traceable
reversibility: traceable
observation: distributed
limitations: explicit
public_api: minimized
pii_public: false
internal_weights_public: false
gaming: monitored
metrics: revisable
```

## Applications
可用于共创项目、人机协作、组织间合作、社区、审计接口与制度评价。会议次数、使用次数、收入或受欢迎程度都不能单独代表连接价值，必须和合意、可逆性、观察一致性、质性影响一起读。

## Audit points
检查是否出现总分排名化、直接货币化、同意不可撤回、观察权集中、方法与限制缺失、PII或内部权重泄露、指标被攻略后仍固定不变等问题。还要比较“指标改善”与“真实连接改善”是否发生分离。

## Preconditions
必须先定义评价目的，选择必要最小指标束，记录同意和可逆性，分散观察，保留审计方法与限制，划分公开／非公开边界，并建立指标修订程序。

## Failure modes
把CDI当成人的价值，把五项指标合成社会信用分，把ConsentToken当永久同意，把MemoryObject变成监控日志，隐藏不可逆性，单一管理者垄断评价，公开敏感内部权重，或放任固定指标被攻略，均属于失败。

## Falsification / update conditions
如果指标束无法解释现实变化，RS与实际回滚能力长期不一致，MAI无法反映有效合意，分散观察只增加噪声而不提高审计性，就应修订定义。如果公开API增加隐私风险或游戏化而没有提升问责，也应缩小公开范围。

## Required distinctions
- 会计 ≠ 货币化
- 指标束 ≠ 排名总分
- 连接价值 ≠ 人的价值
- 同意令牌 ≠ 永久同意
- 观察 ≠ 监控
- 透明 ≠ 全部公开
- 移动目标 ≠ 任意改规则

## Misreading constraints
不能把本标准用作社会信用、受欢迎排名或自动分配报酬的机器。测量的目的在于可检查、可修正，而不是让某一主体垄断并定价所有关系价值。隐私边界与反游戏化也是问责的一部分。

## Origin return
各指标的精确定义、结构日志语义、审计摘要字段、API示例、安全边界、保留条件与修订条件应回到Parent正文确认。本AI索引只承担检索和对照功能。

## Identity
- Official derivative: 291
- Parent NCL-ID: NCL-α-20251102-7308d5
- Derivative NCL-ID: DNCL-NCL-ALPHA-20251102-7308D5-AI-ZH-0291-0002
- Derivative Diff-ID: DDIFF-20260828-DNCL-291-0002-0001

---
導線: [公式派生物291トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)