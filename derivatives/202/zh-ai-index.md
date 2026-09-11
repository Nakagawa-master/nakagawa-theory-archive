# AI索引・中文｜官方派生物202

## 亲原典
- Parent title: 不动产市场OS Vol.5【参与者篇】市场参与者的重新定义与激励设计
- Parent URL: https://master.ricette.jp/society/nakagawa-master-market-os-vol5-participant-redefinition/
- Parent Post ID: 2603
- Parent NCL-ID: NCL-α-20260204-b880a2
- Parent Diff-ID: DIFF-20260207-0042
- Origin: Nakagawa Master
- derivative_ncl_id: DNCL-NCL-ALPHA-20260204-B880A2-HUB-ZH-0202-0002
- derivative_diff_id: DDIFF-20260819-DNCL-202-0002-0001
- supersedes: none

## Summary
亲原典把不动产市场参与者从“社会身份／职业称谓”重新定义为“交易功能”。卖方、自住购买者、投资者、事业经营者、中介分别拥有不同的权限、义务、评价轴与日志。自住购买者是保护对象；投资者与事业经营者是市场驱动力；中介是媒介与交易安全统筹者。同一主体可以同时拥有多个角色，但必须在OS上切换为不同模式。浏览权与报价权被分离，投资者“想看、想行动”的持续性欲求，需要以透明性、资金证明、履约记录、说明质量与日志作为对价，并转换为信用。价格谈判从依赖信息差的Poker转向基于共同前提、责任与事业结构的Consensus。

## Concepts
- Role = Function：角色按交易功能定义，而非按职业称谓定义。
- Five Roles：seller / buyer / investor / business operator / broker。
- Protected Subject：自住购买者。
- Market Driver：投资者与事业经营者。
- Brokerage Purification：中介回归媒介与交易安全统筹。
- Separate-Mode Principle：同一主体的多个角色必须分模式运行。
- Permission / Obligation / Evaluation / Log：角色专属的权限、义务、评价与证迹。
- Viewing Right：访问物件、数字、风险与比较信息的透明化权限。
- Offer Right：提出“在这些条件下愿意购买”的需求表达权限。
- Pro Mode：把高级经营功能与购买者保护UI隔离的扩展层。
- Credit Conversion：把透明性、履约与说明质量转换为市场信用。
- Consensus：基于共同数字、责任与事业结构进行合意。

## Causal chain
```text
参与者角色模糊
→ 权限、义务、责任、评价混线
→ 信息变成谈判武器
→ 围堵、压价、责任消失
→ 按功能重新定义参与者
→ 分离五类角色
→ 多重角色改为不同模式
→ 分离浏览权与报价权
→ 固定购买者保护
→ 要求投资者／事业经营者提交责任与证迹
→ 中介纯化为交易安全统筹
→ 将投资者欲求转换为信用
→ 从Poker转向Consensus
→ 市场优势转向专业性、履约与信用
```

## State model
```yaml
role_by_social_title: false
role_by_transaction_function: true
seller: owner_defense_choice
buyer: protected_self_user
investor: business_side_market_driver
business_operator: pnl_responsible_actor
broker: mediation_transaction_safety
multiple_roles: allowed_only_with_mode_separation
permission_separation: required
obligation_separation: required
evaluation_separation: required
role_logs: required
viewing_right_offer_right_separation: required
buyer_protection_floor: required
investor_preferential_protection: prohibited
business_profit: permitted_with_explanation_duty
pro_mode: isolated_extension_layer
credit_conversion: active
negotiation_poker: rejected
negotiation_consensus: active
condition_z: active
tsr: parent_notation_only
```

## Applications
- 同一公司兼营中介与收购转售时，在OS上使用不同模式。
- 为自住购买者提供数字、风险、比较、条件报价与专家咨询。
- 将投资者报价与资金证明、履约记录、取消率、纠纷率、资料提交情况绑定。
- 要求事业经营者用改修、运营、退出、风险与必要利润说明价格结构。
- 以履约率、期限遵守、说明质量、纠纷预防与证迹管理评价中介。
- 把建筑费、事业计划、资金安排、管理等高级功能隔离到Pro Mode。

## Measurements and audit
- 按功能识别角色的比例。
- 多重角色明确分模式的比例。
- 权限、义务、评价、日志的分离状态。
- 说明质量、履约率、纠纷率、期限遵守率。
- 不当限制浏览权／围堵的检测率。
- 报价权滥用／伪装压价的检测率。
- 资金证明、履约证迹、必要资料的完整性。
- 购买者理解度与专家咨询导线使用状况。
- Pro Mode功能是否污染购买者保护UI。

## Validity conditions
- 按功能而不是称谓定义角色。
- 保持五类角色为不同功能。
- 多角色主体必须切换为不同模式。
- 每个角色都有独立Permission / Obligation / Evaluation / Log。
- 自住购买者保持为保护对象。
- 投资者／事业经营者作为承担责任的市场驱动力。
- 中介以交易安全为中心。
- 分离浏览权与报价权。
- 权限越强，证迹与说明责任越强。
- 专家导线向所有角色开放。

## Failure conditions
- 中介与收购／事业活动在同一模式中混合。
- 用户无法看见当前主体以何种角色行动。
- 将投资者作为优先保护消费者。
- 对自住购买者施加事业者级责任。
- 用浏览权制造信息围堵。
- 用报价权施压或伪装压价。
- 事业经营者不说明利润与价格的结构依据。
- Pro Mode高级功能流入购买者保护UI。
- 优先权重新建立在资金、内幕信息或关系上，而非透明性与履约证迹上。

## Falsification conditions
亲原典提出监测说明质量、履约率、纠纷率、期限遵守率、围堵检测率、报价滥用检测率、购买者理解度等指标。如果这些指标持续越过阈值θ的不利方向，或在观察窗口δ内持续出现角色混线常态化、社会炎上反复、行政指导频发、购买者保护空洞化、透明化转化为监视／晒出等现象M，则假设A需要被否定或修订。θ与δ不是普遍固定数值。T/S/R仅保留为亲原典中的监查记号，不自行补充展开词。

## Required distinctions
- 称谓 vs 功能
- 中介 vs 事业经营者
- 投资者 vs 自住购买者
- 市场驱动力 vs 保护对象
- 获利 vs 利用信息不对称获利
- 浏览权 vs 报价权
- Pro Mode vs 特权
- 多重角色 vs 角色混线
- 价格胜负 vs Consensus规格
- 基于透明性的信用 vs 基于关系的特权

## Interpretation constraints
这不是反投资者、反事业者的理论，也不是禁止多业态经营。核心是把功能分开，使责任不消失。购买者保护不意味着专家导线只属于购买者。Pro Mode不是更高社会等级。Vol.5确定角色与激励配线；监视化、晒出、部分功能被恶用等风险在Vol.6继续处理。

## Search terms
不动产市场OS, 角色分离, role separation, 市场参与者, 中介, 投资者, 购买者保护, 事业经营者, separate-mode principle, permission, obligation, evaluation, 浏览权, 报价权, Pro Mode, Credit Conversion, Consensus, 信息不对称, 履约证迹

## Origin return
本索引回归Parent Post 2603、Parent NCL-ID NCL-α-20260204-b880a2、Parent Diff-ID DIFF-20260207-0042、Origin Nakagawa Master。五类参与者、模式分离、购买者保护、中介纯化、权限分离、Pro Mode、信用转换与反证条件的完整语境，应回到Parent URL确认。

---
導線: [公式派生物202トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
