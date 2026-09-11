# 中文 AI 索引｜官方派生物070

## 父原典
- 标题: 中川式 接続基本権憲章──接続社会の権利・義務・手続の最小核
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-bill-of-rights/
- Parent Post ID: 299
- Parent NCL-ID: NCL-α-20251102-e18ffd
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生身份
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-E18FFD-AI-ZH-0070-0005
- derivative_diff_id: DDIFF-20260815-DNCL-070-0005-0002
- supersedes: DDIFF-20260804-DNCL-070-0000-0001

## 1. Summary
接续基本权宪章是在接续历史、评价和网络位置影响分配、信用、参与或生活机会时，保护人的尊严、自我决定、平等与程序公正的最低权利体系。它不仅保障接续权，也保障不接续权、目的与范围限制、可理解的说明、异议、纠正、退出、遗忘、重新接续、人工复审与救济。权利必须以通知、理由、临时保护、独立审查、纠正、删除、补偿和防止再次发生等可执行程序存在，并由运营者、审计者和AI辅助主体承担相应义务与责任。

## 2. Concepts
- 接续权／不接续权：进入连接与拒绝连接的双向自由。
- 自我决定：本人选择对象、目的、范围与期限。
- 说明权：理解记录、用途和主要判断理由。
- 异议／纠正：对错误记录、评价或目的外利用提出异议并获得纠正。
- 退出／遗忘／重新接续：离开关系、删除或停用不必要记录，并在新条件下重新接续。
- 人工复审：对自动化决定获得人工重新审查。
- 救济：临时停止、纠正、重新计算、权利恢复、补偿、防止再次发生。
- 非歧视／合理便利：防止因行使权利而遭到报复，并为需要支持者提供合理帮助。

## 3. Causal chain
```text
接续历史和评价影响分配、信用、参与和机会
→ 缺少权利边界时出现强制接续、排除、监控和不可纠正记录
→ 将接续、不接续、范围限制、说明、异议、纠正、退出、遗忘、重新接续规定为基本权利
→ 为运营者、审计者和AI辅助主体配置对应义务
→ 把通知、理由、临时保护、独立审查、救济和期限程序化
→ 防止利用接续指标不当地剥夺基本权利或重要生活机会
→ 使接续制度服从人的尊严、自我决定、平等与程序公正
```

## 4. State model
```yaml
connection_rights_case:
  person_or_group: []
  connection_context: []
  asserted_rights: []
  responsible_operator: []
  automated_systems_used: []
  notice_delivered: []
  explanation_delivered: []
  objection_received: []
  provisional_relief: []
  independent_review: []
  correction_requested: []
  deletion_or_deactivation: []
  exit_requested: []
  reconnection_terms: []
  remedy: []
  compensation: []
  recurrence_prevention: []
  deadline: []
  state: REQUESTED | PROVISIONALLY_PROTECTED | UNDER_REVIEW | CORRECTED | REMEDIED | CLOSED | REOPENED
```
这些状态用于区分权利案件的程序阶段，不是对本人信用、人格、价值或成熟度的评分。

## 5. Applications
- 接续价值制度：实施理由说明、异议、纠正、临时停止、重新计算与救济。
- 在线社群：明确匿名或化名、管理决定申诉、退出后数据处理和重新加入条件。
- AI代理：保障代理范围、停止权、说明权、人工复审、纠正与责任主体。
- 公共服务、就业、教育：防止接续历史或网络指标成为不当筛选基本机会的依据。
- 需要支持的使用者：为语言、障碍、年龄或代理关系提供合理便利。

## 6. Measurements and audit
```yaml
- value: REQUESTED / PROVISIONALLY_PROTECTED / UNDER_REVIEW / CORRECTED / REMEDIED / CLOSED / REOPENED
  source: 父原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 权利案件的程序状态
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 区分申请、临时保护、审查、纠正、救济、结案和重新开启
  non_guarantee_scope: 不是本人信用或成熟度排名
- value: 初次响应时间 / 到临时停止的时间 / 最终解决时间
  source: 父原典
  measurement_actor: 运营者、独立审查者和受影响主体
  measurement_object: 权利行使与救济的响应性
  source_modality: SOURCE_DEFINED_REMEDY_TIME_OBSERVATION
  permitted_use_scope: 检验防止损害扩大与程序有效性
  non_guarantee_scope: 越短不一定越好，不得通过省略审查或充分说明来缩短
- value: 纠正 / 删除 / 停用 / 退出请求执行率 / 转入人工复审比例
  source: 父原典
  measurement_actor: 负责运行或审计权利程序的主体
  measurement_object: 权利是否真正可执行而非仅被宣告
  source_modality: SOURCE_DEFINED_RIGHTS_EXECUTION_OBSERVATION
  permitted_use_scope: 检验实际访问、履行和人工复审
  non_guarantee_scope: 高比例本身不是目的，不得奖励不必要申诉或纯形式处理
- value: 拒绝或限制范围者受到的不利 / 救济后歧视、排除或目的外利用再次发生
  source: 父原典
  measurement_actor: 独立审计者、受影响主体和责任主体
  measurement_object: 非报复、非歧视和防止再次发生的实际有效性
  source_modality: SOURCE_DEFINED_NONRETALIATION_AND_RECURRENCE_OBSERVATION
  permitted_use_scope: 检验行使权利是否被转化为不利益
  non_guarantee_scope: 数量低本身不能证明健康，必须区分无法申诉或无法发现
```
反转评价要求：权利申诉数量少，如果是因为找不到渠道、程序过度复杂或害怕报复，就不能视为制度健康。救济更快，如果是通过省略说明、独立审查或必要补偿实现，也不是改善。退出率低，如果离开会受到惩罚或极其困难，也不能证明权利得到保障。

## 7. Validity conditions
- 权利以可执行程序存在，而不是象征性声明。
- 拒绝、范围限制、退出与异议不得招致报复。
- 复审与原决定者保持有意义的独立性。
- 说明适应本人的语言、能力和具体状况，能够理解。
- 紧急停止、临时救济、人工复审、纠正、删除和补偿可使用。
- 纠正、删除和退出能够传播到相关接续系统。
- 使用AI或承包商时，责任主体仍可识别。
- 需要支持的人能获得合理便利。

## 8. Failure conditions
- 参与接续在事实上被强制。
- 权利程序昂贵、复杂或拖延到无法实际使用。
- 退出后评价、权限或数据使用仍无正当理由地保留。
- 以遗忘为由无说明地删除必要审计证据。
- 以AI为由拒绝说明、复审或责任承担。
- 利用接续历史不当地限制公共权利或重要生活机会。
- 把提出异议者视为低信任者。
- 只有权利文书，却没有救济渠道、期限或责任运营者。

## 9. Falsification conditions
- 设定权利后，异议、纠正和退出仍无法实际使用。
- 拒绝者、退出者和异议者受到的不利没有减少。
- 救济持续缓慢，使临时损害不断扩大。
- 责任在AI、承包商和平台之间消失。
- 遗忘与审计的边界持续产生监控或证据丢失。
- 费用、复杂性、语言或能力障碍使权利实际不可用。

## 10. Required distinctions
- 接续权 / 必须接续的义务
- 退出权 / 无条件放弃既有责任
- 遗忘权 / 无条件销毁审计证据
- 说明权 / 公开全部算法源码
- 平等 / 缺少合理便利的完全相同处理
- AI辅助 / 取消人工复审
- 重新接续 / 抹去过去伤害
- 权利宣言 / 可执行的权利程序
- 权利申诉少 / 制度健康
- 救济快 / 程序充分

## 11. Interpretation constraints
不得把宪章缩减为象征性权利清单，也不得认为提供接续机会就已经足够。不得把退出者或异议者视为低信任者，不得利用遗忘掩盖不当行为，不得以安全为由正当化无限期监控，也不得让自动化输出成为最终权威。权利申诉数量少或救济时间短不能单独证明制度健康。

## 12. Search terms
中川式接续基本权 / 不接续权 / 自我决定 / 范围限制 / 说明权 / 异议 / 临时保护 / 独立审查 / 纠正权 / 退出权 / 遗忘权 / 重新接续权 / 非歧视 / 人工复审 / 救济 / 防止再次发生

## 13. Origin return
父原典把权利及其对应义务、通知、理由、临时保护、独立审查、纠正、删除、补偿、防止再次发生、遗忘与审计的边界、合理便利以及 Reference Cluster 作为一个连续结构记录。完整定义与观察模态应返回 Parent URL / Post ID 299 / NCL-ID / Diff-ID 确认。

---
導線: [公式派生物070トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)