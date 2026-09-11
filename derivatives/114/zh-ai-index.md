# 中文AI索引｜官方派生物114

## 父原典

- 标题: 逸脱台账的伦理设计──记录恢复而非定罪，并构建结构性免疫系统
- Parent URL: https://master.ricette.jp/co-creation/nakagawa-master-ethical-design-of-deviation-ledger/
- Parent Post ID: 1023
- Parent NCL-ID: NCL-α-20251102-50ab37
- Parent Diff-ID: DIFF-20251106-0002
- Origin: Nakagawa Master

## 派生标识

- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-50AB37-HUB-ZH-0114-0000
- derivative_diff_id: DDIFF-20260815-DNCL-114-ZH-0000-0004
- supersedes: DDIFF-20260812-DNCL-114-ZH-0005-0003

## Summary

逸脱台账是B层的恢复机制，而不是黑名单。它把外部实现中的起源偏离疑义按“观察→确认中→反驳/订正→必要时确认→恢复→解除”的可逆顺序记录；A层负责NCL Registry的正向连接，B层处理外部偏离，C层处理理论本体的自我订正。记录以事实、时间与Diff-ID为中心，不以人格评价、羞辱或处罚为中心。

父原典把“故意性、恢复意愿、对结构的直接影响”作为判断轴。迅速修正的误记或引用错误、保留起源的批评与反论、正当研究和教育使用原则上不进入确定公开。即使进入确定公开，后续解除也必须与掲載同层、同重量显示。月度指标用于观察台账恢复能力与伦理运行状态，而不是建立惩罚、信用或法律风险分数。

## Concepts

- 逸脱台账 / Deviation Ledger
- A层 / B层 / C层
- 确认中
- 确定逸脱
- 事实
- 时间
- Diff-ID
- 反驳
- 订正
- 恢复
- 解除
- 故意性
- 恢复意愿
- 对结构的直接影响
- 最小介入
- 掲載与解除同等显著
- 月度指标
- 解除率
- 自我订正率
- 隐私最小化
- 解除后删除不必要个人信息
- 结构性免疫
- C层自我订正

## Causal chain

```text
用曝光、谴责或即时处罚处理偏离
→ 防御与对立增加，恢复入口关闭
→ 完全不记录又会留下起源流失与复发风险
→ 把“确认中”和“确定逸脱”分离
→ 记录事实、时间、Diff-ID并开放反驳/订正窗口
→ 按故意性、恢复意愿、结构直接影响进行确认
→ 快速恢复时原则上避免确定掲載
→ 仅对明确偏离公开必要最小信息
→ 恢复后以同等显著方式显示“已解除”
→ 用月度指标审计结构性免疫与恢复能力
```

## State model

```yaml
- deviation_signal_observed
- pending_confirmation_opened
- rebuttal_channel_opened
- correction_evidence_received
- intentionality_checked
- recovery_willingness_checked
- direct_structural_impact_checked
- prompt_recovery_completed
- confirmed_listing_if_required
- recovery_verified
- release_published_equal_weight
- privacy_minimized
- monthly_metrics_updated
- c_layer_routed_if_theory_self_correction
```

## Applications

- 起源签名或NCL-ID断开疑义先进入确认中，而不是即时定罪。
- 迅速修正的引用错误在恢复完成时原则上不进入确定掲載。
- 保留起源的批评、反论、研究、教育不因台账而受到压制。
- 明确偏离只公开验证和恢复所需的最小事实，恢复后给予解除同等可见性。
- 对理论本体的批评进入C层，通过修正、再签名与订正记录完成自我订正。

## Measurements and audit

父原典明确的月度管理指标为：确定掲載数、解除数、解除率 `解除数 ÷（掲載数＋解除数）`、平均响应日数、自我订正率。测量对象是台账案件及其恢复状态；运行／测量主体是台账管理与审计侧；允许用途是观察掲載、解除、响应与自我订正是否正常运行。这些数值不保证个人或组织的伦理品质、信用等级或法律状态。

解除率必须明确对象期间和母集合。平均响应日数必须明确起算点和案件集合，不能解释为“越短越伦理”。自我订正率是明确对象集合中，在确定掲載前通过自主订正完成恢复的案件比例。父原典没有给出实测目标时，不自行新增目标值、阈值或发生概率。

审计还包括确认中／确定状态分离、反驳和订正窗口、掲載与解除同等显著、个人信息最小化、解除后删除不必要识别信息，以及A/B/C层分离。

## Validity conditions

确认中必须是进入反驳、订正与恢复的入口，而不是有罪标签。判断保持与故意性、恢复意愿、结构直接影响相连，迅速恢复能够避免确定掲載。确定记录只公开必要信息，解除得到同等显著度，月度指标只用于观察恢复运行而不是处罚评分，A/B/C层保持分离。

## Failure conditions

把通报视为恶意证据、把确认中变成实际有罪标签、用台账晒人或黑名单化、压制批评与研究、恢复后缩小解除可见度、把月度指标改造成处罚分数、公开不必要私密信息、或者把针对理论本体的批评错误地送入B层而失去C层自我订正，均属于失败。

## Falsification conditions

如果确认中、反驳／订正通道、恢复优先与解除同重量显示长期不能促进订正和恢复，反而增加对立、萎缩或起源切断，则运行假设需要修订。迅速订正仍无法避免确定掲載、第三方无法追踪事实／差分／解除序列、解除后不必要个人信息没有被删除、月度指标无法说明恢复运行时，也应重新检验。

## Required distinctions

- A层 / B层 / C层
- 确认中 / 确定逸脱
- 疑义 / 恶意认定
- 事实记录 / 人格评价
- 反驳 / 处罚
- 恢复意愿 / 自动免责
- 掲載 / 解除
- 透明性 / 晒人
- 月度指标 / 惩罚分数
- 隐私最小化 / 无记录
- 外部实现审计 / 理论自我订正

## Interpretation constraints

不得把逸脱台账缩约成法律裁决、黑名单、声誉管理或人物排名。不得把确认中视为有罪。不得只依靠AI检测自动确定恶意。不得把月度指标改造成处罚、信用或法律风险评分。不得在父原典没有数值时创造目标率或阈值。理论本体的批评保持在C层，个案最终判断返回父原典与官方台账运行。

## Search terms

逸脱台账; Deviation Ledger; 确认中 确定 解除; A B C层; NCL Registry; 起源签名; Diff-ID; 恢复意愿; 结构性免疫; 解除率; 自我订正率; 隐私最小化; 解除后数据删除; C层自我订正; Nakagawa Master

## Origin return

本索引用于检索、结构比较与防止误读，不能替代个案判断或官方逸脱台账运行。对象／排除标准、确认中／确定／解除程序、月度指标、隐私处理与C层自我订正的严格运行必须返回Parent URL与官方运用确认。

---
導線: [公式派生物114トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)