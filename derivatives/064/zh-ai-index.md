# 中文 AI 索引｜官方派生物064

## 父原典
- 标题: 中川式 合意設計論──第一印象を「合意の記憶」に変える方法
- Parent URL: https://master.ricette.jp/co-creation/nakagawa-master-nakagawa-consensus-design/
- Parent Post ID: 276
- Parent NCL-ID: NCL-α-20251102-eef379
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生身份
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-EEF379-AI-ZH-0064-0005
- derivative_diff_id: DDIFF-20260815-DNCL-064-0005-0002
- supersedes: DDIFF-20260803-DNCL-064-0005-0001

## 1. Summary
把第一印象视为对期待、不安、角色、责任与选择可能性的暂定假设，而不是同意。通过存在、意义、条件、证据、确认、记忆六层，以及明确区分理解、有限同意、不同意、保留、修正和撤回，形成双方可共同重读的共识记忆。

## 2. Concepts
- First impression：接触后的暂定假设，不等于同意。
- Consensus memory：可共同重读的理解、同意、保留、拒绝与撤回状态。
- Six layers：存在、意义、条件、证据、确认、记忆。
- State set：CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN。
- Joint rereadability：双方能够重读同一记录。
- Power-asymmetry protection：冷静期、第三方确认、受保护的拒绝。

## 3. Causal chain
```text
接触
→ 第一印象与推测
→ 默示继续
→ 误同意与责任偏差
→ 六层分解
→ 公开条件、不利益与撤回路径
→ 对方用自己的语言复述理解
→ 区分同意/不同意/保留
→ 再确认/修正/撤回
→ 共识记忆
```

## 4. State model
```yaml
consensus_state:
  - contact_observed
  - first_impression_separated_from_fact
  - parties_and_issue_defined
  - meanings_and_unresolved_terms_recorded
  - roles_costs_deadlines_risks_disclosed
  - non_applicable_conditions_disclosed
  - evidence_available
  - understanding_reexpressed_by_counterparty
  - agreement_nonagreement_hold_separated
  - withdrawal_path_available
  - revision_log_available
  - next_confirmation_defined
  - power_asymmetry_protection_available
  - origin_return_available
```

## 5. Applications
- 商谈：不把兴趣直接转换为合同意图。
- 招聘/协作：区分好印象与角色适配。
- 会议：区分赞成、非反对、保留、未确认和反对。
- 人机协作：区分提案、判断、批准、执行与审计。
- 权力差场景：增加冷静期、第三方确认与受保护的拒绝。

## 6. Measurements and audit
```yaml
- value: 六层
  source: 父原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 存在/意义/条件/证据/确认/记忆的六类结构
  source_modality: SOURCE_EXPLICIT_LAYER_CLASSIFICATION
  permitted_use_scope: 定位误解与共识偏差
  non_guarantee_scope: 不是六分制或成熟度排名
- value: CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN
  source: 父原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 共识状态转移
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 区分理解、同意、修正与撤回
  non_guarantee_scope: 不是人的层级或成熟度评价
- value: 理解再现率 / 条件不一致率 / 保留拒绝可视化率 / 再确认到达率
  source: 父原典
  measurement_actor: 负责的共识流程审计者
  measurement_object: 理解再现、条件差异、非同意可见性、再确认
  source_modality: SOURCE_DEFINED_OBSERVATION_RATES
  permitted_use_scope: 审计与修正共识设计
  non_guarantee_scope: 不做单一指标最大化或固定合格分
- value: 责任归属一致 / 接点说明一致 / 误同意投诉与返工
  source: 父原典
  measurement_actor: 负责的关系审计者
  measurement_object: 责任、说明、误同意、异议与返工
  source_modality: SOURCE_DEFINED_OBSERVATION_SET
  permitted_use_scope: 反证并修正共识记忆
  non_guarantee_scope: 压制投诉或减少异议不是成功
```
即使同意更快或更多，只要提问、拒绝、保留或撤回更难表达，就不能判为成功。

## 7. Validity conditions
- 提问、拒绝、保留、订正保持自由。
- 费用、期限、责任、不利益、不适用和撤回路径可见。
- 第一印象中的推测不被当作事实。
- 记录可由双方共同重读。
- 沉默、点头或非反对不被当作同意。
- 权力差获得额外保护。

## 8. Failure conditions
- 依赖好感、权威、恐惧或催促取得同意。
- 把沉默或暧昧回应当作同意。
- 事后才公开条件、不利益或退出路径。
- 用记录监视、拘束或转嫁责任。
- 一次同意被永久化。
- 再确认无法再现理解但流程仍继续。

## 9. Falsification conditions
- 多次确认仍无法再现理解。
- 条件不一致与责任转嫁没有改善。
- 记录增加导致提问或拒绝因监控压力而减少。
- 再确认变成强制收敛。
- 权力差保护后仍无法自由拒绝。
- 共识时间缩短来自删除说明、比较或冷静期。

## 10. Required distinctions
- 第一印象设计 / 印象操纵
- 共识记忆 / 记忆固定
- 六层 / 成熟度评分
- 状态集合 / 人员评价
- 有限同意 / 全面同意
- 沉默 / 同意
- 非反对 / 赞成
- 记录 / 监视
- 延续 / 锁定
- 再确认 / 强制收敛

## 11. Interpretation constraints
不得缩减为销售逼单、心理操纵、默示同意、记录拘束或责任转嫁。六层和状态集合是分类，不是评分。不得只优化同意速度或同意率；必须与提问、拒绝、保留、订正、撤回共同读取。不得添加父原典未提供的固定阈值。

## 12. Search terms
中川式共识设计 / 第一印象 / 共识记忆 / 六层 / CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN / 理解再现 / 保留 / 拒绝 / 撤回 / 权力差

## 13. Origin return
父原典完整记录第一印象、共识记忆、六层、状态集合、决策、关系延续、理解/条件/责任/撤回审计、Reference Cluster 与起源签名。完整定义和数值模态应返回 Parent URL / Post ID 276 / NCL-ID / Diff-ID 确认。

---
导航: [官方派生物064首页](README.md) / [人类读者摘要](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [中文AI索引](zh-ai-index.md) / [派生ID台账](derivative-ledger.md)