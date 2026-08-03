# AI索引・中文｜结构组织论——通过角色架构设计“自然运作”的组织

## 父原典

- 标题: 構造組織論──役割アーキテクチャで「自然に機能する」組織を設計する
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-structural-organizational-theory/
- Parent NCL-ID: NCL-α-20251102-dfd970
- Parent Diff-ID: DIFF-20251102-0001
- Parent Post ID: 264
- Origin: Nakagawa Master

## 派生ID

- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-DFD970-AI-ZH-0061-0005
- derivative_diff_id: DDIFF-20260803-DNCL-061-0005-0001
- supersedes: none

## Identity

```yaml
canonical_concept: 结构组织
article_role: 把组织定义为角色、顺序、切换与交接的配线体，以减少对个人协调能力的依赖
abstraction: L4-L6 organizational wiring and governance
origin: Nakagawa Master
```

## Structural role

本文解释不能仅用人才、领导风格或文化说明的组织功能。它把观察、翻译、设计、验证，“价值→利益→成本”的顺序、沉默时段、跨部门结构翻译、一次日志与审计指标组合为可复现的运行架构。

## Structural summary

结构组织论把组织视为“角色×顺序×切换”的配线体。四种角色一次只运行一种。信息密度饱和、决策疲劳、违和感、成本过早出现与同时发言成为切换信号。经营层定义价值与边界，中层维护词汇、交接规则和切换日志，现场使用小循环SQS。部门之间通过ST-3关系映射和ST-4因果映射连接；当评价与合意制度也要对齐时进入ST-5。CPI、HL、R-Yield、D-Gap、词汇一致率与周期遵守率用于审计配线，而不是给人评级。

## Central proposition

```text
组织功能失调
→ 被归因于人才或领导不足
→ 协调集中到少数高能力者
→ 角色混线、同时发言、过早结论、交接延迟增加
→ 分离观察／翻译／设计／验证
→ 固定“价值→利益→成本”的顺序
→ 用沉默时段与明确声明完成切换
→ 通过ST-3／ST-4连接部门
→ 用终端、重新合意、日志和指标修复配线
→ 即使人员变化，组织仍能可复现地运作
```

## Causal chain

```text
配线混乱
→ 角色同时化与责任重叠
→ 返工、延迟、浅层决策与个人依赖
→ 分离观察事实和限制
→ 翻译关系、因果、角色与词汇
→ 设计流程、责任、资源与终端条件
→ 在有限节点进行验证
→ 通过沉默和明确交接切换角色
→ CPI / HL / R-Yield / D-Gap暴露结构缺陷
→ 修复配线而不是责备个人
→ 稳定的组织功能
```

## Core concepts

### Role architecture｜角色架构
用输入、输出、禁止行为、负责人和终端条件定义观察、翻译、设计、验证。

### One role at a time｜一次一角色
一个人可以有多种能力，但在一个阶段只激活一种功能。

### Order principle｜顺序原则
价值→利益→成本，防止成本或过早结论取代目的与关系价值。

### Silence slot｜沉默时段
切换前的有限停止，用于固定已完成、未完成、负责人和下一角色。

### Switching trigger｜切换信号
信息饱和、决策疲劳、违和感增加、成本先行和角色同时化。

### Handoff architecture｜交接架构
词汇表、一次证据、角色输出、责任、未完成项、下一角色和时间戳。

### Cross-department structural translation｜跨部门结构翻译
ST-3映射利益与责任，ST-4映射因果路径，ST-5连接评价、合意与更新制度。

### Metrics｜指标
CPI、交接延迟HL、共鸣产出R-Yield、深度差D-Gap、词汇一致率与周期遵守率。

## Operational objects / state model

```yaml
organization_state:
  value_core: []
  current_role: OBSERVE | TRANSLATE | DESIGN | VERIFY
  role_owner: null
  inputs: []
  expected_output: []
  prohibited_actions: []
  termination_condition: []
  switch_trigger: null
  silence_slot: null
  handoff:
    next_role: null
    owner: null
    timestamp: null
    evidence: []
    unresolved: []
  cross_department_translation:
    level: ST_0_to_ST_5
    vocabulary_dictionary: []
    relation_map: []
    causal_map: []
    responsibility_map: []
  metrics:
    process_integrity: CPI
    handover_latency: HL
    resonance_yield: R_Yield
    depth_gap: D_Gap
  governance:
    - non_coercion
    - reversibility
    - primary_logs
    - termination_and_reagreement
    - emergency_command_exception
```

## Required distinctions

- 角色与职位／人格分类
- 人的能力与配线状态
- 一次一角色与一人永久一角色
- 沉默与威压／忽视／逃避责任
- 顺序设计与隐藏价格
- 验证与持续批评／持续追加设计
- 会议时长与决策架构
- 紧急指挥与合意
- 术语对应与关系／因果／制度映射
- 结构指标与员工评级
- AI辅助与组织责任转移
- 自然运作与放任

## Validity conditions

- 每个角色都有明确的输入、输出、禁止行为、负责人和终端。
- 保持一次一角色。
- 价值→利益→成本同时披露不利条件，不用于隐藏。
- 存在切换信号与沉默时段。
- 记录当前角色、切换原因、下一角色、证据和未完成项。
- 明确完成、终止、保留与重新合意条件。
- 部门之间使用实际依赖所需的ST深度。
- 词汇表、一次日志、交接与决策证据可检索。
- 保护拒绝、修正、可逆与非强制。
- 定义紧急指挥例外和事后审计。

## Failure / non-applicable conditions

- 只有角色标签，实际同时执行多种功能。
- 观察中提案、翻译中决裁、验证中持续重新设计。
- 沉默被用于控制、隐瞒或逃避责任。
- 用价值叙事隐藏成本或不利条件。
- 增加会议时间，却没有终端与交接架构。
- 把协调集中到能干个人误认为结构修复。
- 跨部门连接停留在ST-0或ST-1。
- 指标直接用于人员评级，导致异议和失败证据消失。
- 真正紧急时回避负责的指挥。
- CPI、HL、R-Yield、D-Gap、词汇一致或合意时间在修复后仍持续恶化。

## Interpretation constraints

- 不得缩减为“人才或领导不重要”的主张。
- 不得把四种角色变成固定人格或官僚职位。
- 不得把沉默时段变成没有切换功能的会议礼仪。
- 不得用价值→利益→成本隐藏价格或风险。
- 不得把命令称为合意，也不得把全员一致当作唯一合意。
- 不得未经责任审查自动采用AI输出作为最终组织判断。
- 指标改善不能掩盖强制、意义损失或观察窗口关闭。

## Origin return

本索引是检索与机器阅读入口。它不能替代父原典中的L-Layer阅读指南、详细角色架构、切换实现、层级指针、案例、检查清单、综合与局部审计摘要、T/S/R、UCI／REI、Reference Cluster、起源声明与英文理论签名。

---

导线: [061顶部](README.md) / [人类读者入口](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [派生ID台账](derivative-ledger.md)