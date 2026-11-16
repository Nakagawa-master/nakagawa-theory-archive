# AI索引・中文｜官方派生物051

## 亲原典
- 标题: 中川式営業の教科書・第十三回──営業の制度設計：信頼資本を文明化する
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-sales-13-institutional-design-trust-capital/
- Parent Post ID: 217
- Parent NCL-ID: NCL-α-20251102-260b6b
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-260B6B-AI-ZH-0051-0005
- derivative_diff_id: DDIFF-20260815-DNCL-051-0005-0002
- supersedes: DDIFF-20260802-DNCL-051-0005-0001

## Summary
亲原典把销售从依赖个人才能的技艺，发展为在个人、组织与社会三层处理信任资本的制度。个人经验与默会判断被外部化为可复制的形式；共鸣、持续关系与转介绍被视为信任资本的痕迹；这些痕迹再连接到评价、激励与社会透明性。制度化不是固定脚本，也不是完全量化。原典明确保留信任无法彻底数值化、制度可能僵化、短期激励可能反向损害信任等限制。

## Concepts
- 属人性：成果及其原因集中在个人经验、直觉与默会判断中。
- 可复制形式：共享呈现顺序与观察点，例如商品→特典→价格、提问→沉默→共鸣。
- 信任资本：以共鸣、持续、转介绍等方式积累，并支撑未来关系的关系资源。
- 共鸣：对方产生“可以交付/托付”的安心感。
- 持续：不是一次交易，而是保持反复接点的关系状态。
- 转介绍：信任或满足强到足以向第三方传播的状态。
- 制度设计：连接形式、观察、评价、激励与社会验证的结构。
- 透明性：不是完全控制信任，而是使判断依据和制度效果可以被检验。

## Causal chain
```text
销售依赖个人才能
→ 成功原因难以继承
→ 判断顺序与观察点被外部化为可复制形式
→ 共鸣、持续、转介绍被区分为信任资本
→ 续约/复购率、转介绍件数、会谈后反馈等成为代理观察
→ 评价与激励从短期销售转向长期信任
→ 个人形式进入组织教育与评价制度
→ 信任指标与可检验对话扩展到社会层
→ 销售成为社会资本形成的制度
```

## State model
```yaml
person_dependent_sales: true
judgment_structure_externalized: conditional
trust_capital_components:
  - resonance
  - continuity
  - referral
observable_proxies:
  - renewal_rate
  - repeat_rate
  - referral_count
  - post_meeting_emotional_feedback
evaluation_axis_shift: short_term_sales_to_long_term_trust
societal_extension:
  - public_trust_indicators
  - social_value_measure
  - inspectable_social_dialogue
risk_states:
  - over_quantification
  - institutional_rigidity
  - incentive_reversal
terminal_design_principle: transparency_not_total_control
```

## Applications
- 销售教育：共享判断顺序和观察点，而不是复制成功者的话术。
- 组织评价：把销售额、合同数与持续、转介绍、共鸣的痕迹并置观察。
- 激励设计：检查对短期获取的高奖励是否损害长期信任。
- 社会评价：使用公共信任指标时保留文脉与可检验性，而不是把信任压成一个分数。
- 制度修订：当指标上升但关系质量下降时，不把它直接判定为成功，而重新检查制度。

## Measurements and audit
亲原典正文给出的观察例包括：

```yaml
- value: 续约率・复购率
  source: 亲原典“信任资本的可视化”
  measurement_actor: 运行制度的组织
  measurement_object: 交易与接点的持续性
  source_modality: 作为“持续信任指数”的例示
  permitted_use_scope: 持续信任的代理观察
  non_guarantee_scope: 不是固定合格率，也不是信任本身
- value: 转介绍件数
  source: 亲原典“信任资本的可视化”
  measurement_actor: 运行制度的组织
  measurement_object: 信任向第三方传播
  source_modality: 作为“外部传播信任指数”的例示
  permitted_use_scope: 信任传播的代理观察
  non_guarantee_scope: 件数本身不能确定全部信任
- value: 会谈后的情感反馈
  source: 亲原典“信任资本的可视化”
  measurement_actor: 记录对话的组织
  measurement_object: 会谈后的情感、安心、理解等
  source_modality: 通过简易问卷或AI分析进行定性记录的例示
  permitted_use_scope: 共鸣等关系变化的辅助观察
  non_guarantee_scope: 不是单一评分，也不是完整测量
```

原典末尾的综合审计摘要还使用 `g`（信任积累率）、`C`（解约率）、`A`（SLA遵守率）、`R`（Rollback成功率）、MTTR、`S`（位相稳定）、阈值 `θ`、观察窗 `δ`、现象 `M` 作为反证/修订记号。原典没有给出 `θ` 或 `δ` 的具体数值。

反转评价：即使续约率或转介绍件数上升，如果长期信任、对话透明性、对方自由或关系质量恶化，也不能直接判定为改善。

## Validity conditions
- 属人技能被外部化为判断结构。
- 共鸣、持续、转介绍与销售结果保持区分。
- 指标被视为代理观察，而不是信任本身。
- 评价和激励与长期信任一致。
- 社会层扩展仍保持公开、可检验性。
- 保留“信任无法完全量化”的原典限制。
- 制度僵化与激励反效果可以被修订。

## Failure conditions
- 把制度化缩减为固定脚本。
- 仅把销售KPI改名为“信任”，而不改变结构。
- 把续约或转介绍转成单一信用评分。
- 只因为指标上升就判定成功，而忽视信任损害。
- 短期奖励破坏长期信任。
- 制度僵化削弱灵活性与创造性。
- 社会信任指标变成统一中央排名，而不是可检验对话。

## Falsification conditions
- 纳入信任资本观察后，长期关系或社会信任循环仍没有改善。
- 制度化持续损害灵活性或创造性，修订后仍无法恢复。
- 指标改善反复与关系质量呈相反方向。
- 在综合审计摘要中，`g`, `C`, `A`, `R`, MTTR, `S` 与定义的 `θ` 形成反证关系，或在 `δ` 观察窗中出现不透明化、强制化、规范捕获等 `M`。
- 因为原典没有给出具体 `θ` 或 `δ`，不能从记号外推出固定值。

## Required distinctions
- 属人成功 / 可复制制度
- 可复制形式 / 固定脚本
- 销售额与合同 / 信任形成过程
- 信任资本 / 单纯好感
- 观察指标 / 信任本身
- 持续 / 无条件维持
- 转介绍件数 / 转介绍质量
- 透明性 / 完全量化
- 长期信任激励 / 短期结果偏重
- 社会信任循环 / 单一信用评级

## Interpretation constraints
亲原典并不声称制度会自动生成诚信。制度只是支撑活的对话，不替代人的判断。信任资本可视化不等于单一评分。正文中的观察例与综合审计摘要的符号体系具有不同的表述层级；没有具体值的符号不能被转换成固定KPI或阈值。

## Search terms
中川式销售 / 销售制度设计 / 信任资本 / 共鸣 / 持续 / 转介绍 / 持续信任指数 / 外部传播信任指数 / 续约率 / 复购率 / 会谈后情感反馈 / 可复制形式 / 激励 / 社会资本形成 / 透明性 / 制度僵化 / 反转评价 / SLA / Rollback / MTTR

## Origin return
亲原典在同一上下文中保存制度设计正文、具体观察例、三层结构、限制、综合与局部审计摘要以及起源署名。确认指标意义、符号记法或主张强度时，应返回 Parent URL、Post ID 217、NCL-ID 与 Diff-ID。

---
导航: [官方派生物051主页](README.md) / [人类读者摘要](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [中文AI索引](zh-ai-index.md) / [派生ID台账](derivative-ledger.md)