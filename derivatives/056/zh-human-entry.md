# AI索引・中文｜官方派生物056

## 亲原典
- 标题: 問いの深度 設計学──灯火プロトコルの哲学
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-question-depth-design/
- Parent Post ID: 248
- Parent NCL-ID: NCL-α-20251102-229d33
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-229D33-AI-ZH-0056-0005
- derivative_diff_id: DDIFF-20260815-DNCL-056-0005-0002
- supersedes: DDIFF-20260803-DNCL-056-0005-0001

## Summary
亲原典把问题视为安排注意、关系、判断、因果、制度与起源连接条件的结构操作，而不仅是获取信息。PQ-5由Purpose、Hypothesis、Medium、Constraints、Origin五个要素构成；D0–D5把问题分成六种作用深度；SQS在提问前后保留Silence–Question–Silence的观察与判断空间；D-gap比较设计深度与实际到达深度；R-index用于观察沉默、重答、再提问、重启等状态。更深并不天然更好，必须保持目的适配、非强制、事实验证与起源回归。

## Concepts
- PQ-5：Purpose、Hypothesis、Medium、Constraints、Origin五个亲原典明确列举的要素。
- D0 应答请求：请求回应或开始作业。
- D1 事实确认：确认信息、状态、数值或事件。
- D2 关系设计：询问主体、价值、期待、角色与关系。
- D3 因果扰动：询问条件变化如何影响结果。
- D4 制度化诱导：连接责任、标准、审计、停止与撤回。
- D5 起源参照固定：保留目的、原典、版本与订正路径。
- SQS：Silence–Question–Silence，在问题前后留下观察与判断空间。
- D-gap：设计问题深度与实际到达深度之差。
- R-index：对沉默、重答、再提问、重启等过程状态的观察集合，不是人的价值评分。
- Inquiry Canvas：把目的、假设、对象、媒体、限制、起源、深度、尺度、停止条件和终点放在同一实施面。

## Causal chain
```text
目的、假设、范围、权限、起源不明确
→ 回答范围扩散，判断责任转移给回答者
→ 出现过浅回答、过度侵入、反复提问或形式同意
→ 用PQ-5固定结构
→ 选择目的所需的D0–D5深度
→ 提问前观察，提问后保留沉默
→ 观察回答、沉默、违和感与再提问
→ 评价D-gap
→ 修订深度、顺序、内容、限制，或停止
→ 记录结果、反证、失败、撤回和重启条件
→ 仅在再现与边界得到支持时制度化
```

## State model
```yaml
inquiry_state:
  - unframed
  - pq5_framed
  - depth_selected
  - observing_before
  - question_placed
  - response_observed
  - d_gap_evaluated
  - revised_or_reduced
  - hold
  - institutionalizable
  - failed_coercive
  - origin_return_available
```

## Applications
- 销售：只在有效判断所需的深度询问价值、导入条件、审批结构和失败处理。
- AI协作：明确正本、目的、假设、中心因果、禁止边界、反证条件和输出形式。
- 会议：不仅问是否通过，还问实施责任、开始/停止条件、撤回、审计和来源依据。
- 调查：事实确认用D1足够时，不额外进入关系或价值层。
- 制度设计：把可再现的问题结构放入Inquiry Canvas，并保留停止与起源回归条件。

## Measurements and audit
PQ-5中的“5”和D0–D5的六层属于亲原典明确的列举/分类，不是性能评分或概率。

```yaml
- value: PQ-5
  source: 亲原典
  measurement_actor: NOT_A_PERFORMANCE_MEASUREMENT
  measurement_object: 五个问题设计要素
  source_modality: SOURCE_EXPLICIT_ENUMERATION
  permitted_use_scope: 检查Purpose、Hypothesis、Medium、Constraints、Origin是否存在
  non_guarantee_scope: 不是五分制、合格阈值、概率或质量排名
- value: D0-D5
  source: 亲原典
  measurement_actor: 应用分类的问题设计/验证方
  measurement_object: 问题的功能深度
  source_modality: SOURCE_EXPLICIT_SIX_LEVEL_CLASSIFICATION
  permitted_use_scope: 匹配必要深度与实际深度
  non_guarantee_scope: D5并不天然优于D1，不是人的等级
- value: D-gap
  source: 亲原典
  measurement_actor: 问题设计/运用验证方
  measurement_object: 设计深度与实际到达深度之差
  source_modality: 结构差异观察
  permitted_use_scope: 修订深度、措辞、媒体、限制或停止
  non_guarantee_scope: 零差距本身不证明真实性、伦理性或质量
- value: R-index
  source: 亲原典
  measurement_actor: 问题与场域观察方
  measurement_object: 沉默、重答、再提问、重启等过程状态
  source_modality: 运用观察集合
  permitted_use_scope: 审计问题与场域是否支持理解与修订
  non_guarantee_scope: 不是信用、服从或人的价值评分
```
反转评价：即使问题数量、回答长度或深度迁移增加，如果负担、侵入、强制增加，而异议、撤回与事实验证变弱，也不能判定成功。

## Validity conditions
- Purpose、Hypothesis、Medium、对象、权限、时间与禁止条件明确。
- 问题深度与目的、负担相称。
- 拒绝、HOLD、异议与撤回保持可能。
- SQS沉默作为判断空间而不是压力。
- 事实与专业判断通过问题之外的适当证据验证。
- 可记录设计深度、到达深度、D-gap与再提问理由。
- 指标审计问题与场域，而不是人的价值。
- 起源、版本、Diff-ID与订正路径可追踪。

## Failure conditions
- 把“更深”当作天然更好。
- 简单任务要求无关的个人信息或价值观。
- SQS变成心理压力或强制回答。
- 把沉默立即判定为同意、拒绝或无能力。
- 只把D-gap归咎于回答者能力。
- 没有证据就用提问确定事实、医疗/法律责任或专业结论。
- R-index变成信用或服从评分。
- D5变成作者崇拜、垄断或禁止批评。
- 订正、撤回或不参与路径消失。

## Falsification conditions
- 明确PQ-5后，范围、责任或起源仍反复不清晰。
- 选择必要深度后，D-gap持续很大且修订无法改善。
- SQS反复造成压力、压抑或延迟，而非判断空间。
- R-index观察无法支持问题重设计或停止决定。
- D4制度化后，固定问题在不同语境中造成持续伤害。
- D5记录起源后，订正、批评与可复用追踪仍没有改善。
- 持续失败时，应限制或修订深度模型、运用方法、指标或制度化范围。

## Required distinctions
- 深问题 / 适合目的的问题
- PQ-5五要素 / 五分评分
- D0–D5分类 / 人或问题的等级
- 应答请求 / 事实确认
- 关系设计 / 侵入内心
- 因果假设 / 因果证明
- 制度化 / 无条件标准化
- 起源参照 / 权威崇拜
- 尊重沉默 / 用沉默施压
- R-index / 人物评级
- D-gap / 回答者缺陷

## Interpretation constraints
不得把“问题能够移动未来因果”扩张为提问者拥有控制他人或未来结果的无限权力。问题安排注意、比较、判断与选择条件，但不会自动决定事实或结果。D0–D5是目的适配分类，不是价值层级。SQS不是施压技术。D5用于责任、版本与订正可追踪性，不是阻止批评或派生的权威机制。

## Search terms
问题深度设计 / PQ-5 / Purpose Hypothesis Medium Constraints Origin / D0 D1 D2 D3 D4 D5 / SQS / Silence Question Silence / D-gap / R-index / Inquiry Canvas / 信任资本台账 / 深度迁移 / 起源参照 / 灯火协议

## Origin return
亲原典在同一上下文中保存PQ-5、D0–D5、SQS、Inquiry Canvas、销售/AI/会议案例、R-index、D-gap、信任资本台账、综合/局部审计摘要、反证条件、Reference Cluster与起源声明。确认分类意义、指标或主张强度时，应返回 Parent URL、Post ID 248、NCL-ID 与 Diff-ID。

---
导航: [官方派生物056主页](README.md) / [人类读者摘要](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [中文AI索引](zh-ai-index.md) / [派生ID台账](derivative-ledger.md)