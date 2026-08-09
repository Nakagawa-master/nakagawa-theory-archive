# AI索引・中文｜公式派生物131

## 親原典
- 標題: 「照応の裂け目を縫う：AI倫理における“接続責任”の今」
- Parent URL: https://master.ricette.jp/structural-translation-log/ai-ethics/nakagawa-master-2025ai-rinri/
- Parent Post ID: 1389
- Parent NCL-ID: NCL-α-20251102-c38e23
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-C38E23-HUB-ZH-0131-0002
- derivative_diff_id: DDIFF-20260809-DNCL-131-0002-0001
- supersedes: none

## Summary
“连接责任”不把AI伦理只看作模型本身的属性，而是把目的设定、数据、模型、供应商、部署、使用、影响和救济视为一条相互连接的责任链。社会结果来自人类选择优化目标、数据和评价标准，也来自供应商设计、部署组织设置的自动化权限以及最终使用方式。事故发生后，如果只说“AI决定了”或“最后的使用者负责”，上游原因就无法被修复。

责任分配并不等于责任稀释。应根据权限、可预见性、收益、修改能力和停止能力来确定每个连接点的责任主体。受影响者需要真正可用的申诉、人工复审、纠正、暂停和救济，不能只得到解释。供应商与部署组织之间的责任也应通过合同、日志、更新和事故流程固定。

AI自主性提高并不会消除人类社会设置自主边界的责任结构。关键是发生问题后，能否沿着目的、数据、模型、部署和运行向上追溯，并找到真正有能力修改的主体。本索引用于AI部署的结构审计，不替代具体法律责任认定。

## Concepts
- 连接责任
- AI伦理
- 目的设定
- 数据来源
- 模型责任
- 供应商责任
- 部署责任
- 使用责任
- 自动化权限
- 受影响者
- 申诉
- 停止
- 纠正
- 救济
- 因果来源
- 原典回归

## Causal chain
```text
选择AI使用目的
↓
选择数据、模型和评价标准
↓
供应商和部署组织设置权限条件
↓
AI输出连接到人工判断或自动执行
↓
影响扩展到用户与第三方
↓
责任被简单归给AI或最终用户
↓
按连接点映射权限、记录和修改能力
↓
分配申诉、停止、纠正和救济责任
↓
系统能够回到上游修复原因
```

## State model
```yaml
- social_goal_defined
- prohibited_goals_defined
- data_provenance_recorded
- model_role_defined
- vendor_responsibility_recorded
- deployment_authority_assigned
- human_review_boundary_defined
- affected_parties_identified
- external_effects_monitored
- appeal_channel_open
- stop_and_rollback_available
- correction_owner_assigned
- remedy_outcome_audited
- origin_return_verified
```

## Applications
- 招聘AI中明确评价标准所有者和人工申诉。
- 医疗AI中分离供应商、医院和医生责任。
- 公共AI中保留人工复审。
- AI代理中分级执行权限和停止上限。
- 推荐系统中分离模型输出和平台目标设定。

## Measurements and audit
- 目的与禁止目的明确率。
- 数据来源可追踪率。
- 各连接点责任主体覆盖率。
- 自动化边界清晰度。
- 申诉与复审率。
- 停止与回滚成功率。
- 纠正所需时间。
- 受影响者救济到达率。
- 因果重构率。

## Validity conditions
- 明确允许与禁止的AI目的。
- 分离数据、模型、部署和使用责任。
- 定义自动化和人工复审边界。
- 包含第三方影响。
- 提供申诉、停止和纠正路径。
- 固定供应商与部署方义务。

## Failure conditions
- 用“AI决定了”消除人类责任。
- 把全部责任放在最终用户。
- 让数据和模型来源不可追踪。
- 模糊供应商与部署方责任。
- 不提供申诉、停止或纠正。
- 排除受影响的非用户。

## Falsification conditions
- 连接责任不能改善事故预防或救济。
- 单一责任主体模式持续表现更好。
- 来源记录不能改善因果重构。
- 申诉和停止不能降低伤害。
- 权限责任分离只降低修复速度而无收益。
- 更简单的控制获得同等或更好结果。

## Required distinctions
- AI输出 / 人工判断
- 责任分配 / 责任稀释
- 供应商责任 / 部署责任
- 自动化 / 无责任化
- 解释 / 救济
- 审计 / 免责
- 影响 / 意图
- 连接 / 所有

## Interpretation constraints
不要把AI人格化为唯一责任主体。不要假设人类可以预见所有结果。不要把责任拆分到无人能修改系统。不要用可解释性替代救济。不要只责怪供应商或使用者。不要以自主性为理由放弃停止权。

## Search terms
连接责任；AI伦理；责任分配；数据来源；模型责任；供应商责任；部署责任；自动化权限；申诉；停止；纠正；救济；因果来源；人工复审；第三方影响；回滚；中川マスター

## Origin return
本页用于检索和结构审计。连接责任和照应AI伦理的严格论证应回到Parent URL和Parent NCL-ID / Diff-ID确认；具体法律责任由适用法律与程序决定。

---
導線: [公式派生物131トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)