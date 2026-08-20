# AI索引・中文｜官方派生物210

## Parent identity
- Parent title: 合意形成の物理 第5論 時間劣化と制度寿命 ― 説明更新なき制度は必ず死ぬ
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol5-time-decay-and-system-longevity/
- Parent Post ID: 2897
- Parent NCL-ID: NCL-α-20260215-e2d7e7
- Parent Diff-ID: DIFF-20260215-0025
- Origin: Nakagawa Master

## Derivative identity
- derivative_ncl_id: DNCL-NCL-ALPHA-20260215-E2D7E7-AI-ZH-0210-0002
- derivative_diff_id: DDIFF-20260820-DNCL-210-0002-0001
- supersedes: none

## Summary
本原典把制度劣化描述为第三方可再现性 U 随时间下降的过程，而不是道德失败或突然事件。S=U×R×H 是状态量，T 是解释追不上环境变化的速度量；运行相中的观测影为 `T̂ = −ΔU/Δt`。制度寿命不是存在年数，而是 U 进入临界区域之前的时间。Update 不是增加文件，而是重新连接前提、术语、参照、责任节点和可验证历史，使 U 恢复。

## Concepts
- U：第三方可再现性
- R：唯一且可用于修复的责任节点
- H：可验证的决策历史公开性
- S=U×R×H：合意稳定度状态量
- T：解释落后于环境变化的时间劣化速度
- T̂=−ΔU/Δt：运行相中T的观测影
- institutional lifetime：U进入临界区域前的时间
- meaning compression：成功反复与省略造成的内部劣化源
- Update：恢复U的重新连接
- pseudo update：更新后U仍未恢复
- K：认知带宽
- formal H：公开但无法由第三方验证的历史
- hanging R：名义或惩罚化、不能作为修复入口的责任
- exploration / operation：探索相与运行相

## Causal chain
制度反复运行 → 外部环境变化＋内部意义压缩 → 解释与现实坐标偏移 → 前提缺失、术语漂移、参照短路、责任节点溶解 → U(t)下降 → T̂显示下降斜率 → R/H也可能被侵蚀 → S下降 → S<θ持续δ后进入临界转移。修复不是追加资料，而是定位断线并重新连接，再在下一δ重新测量U/R/H/S。

## State model
```yaml
S: U_times_R_times_H
state_quantity: S
velocity_quantity: T
T_hat: minus_delta_U_over_delta_t
T_sources:
  external: environmental_change
  internal: meaning_compression
lifetime: time_until_U_enters_critical_region
update_success: U_recovers_after_update
pseudo_update: U_t_plus_delta_less_or_equal_U_t
critical_transition: S_below_theta_for_delta
phase_boundary:
  exploration: uncertainty_can_be_generation_resource
  operation: reproducibility_is_sustainability_condition
```

## Applications
- 规则或制度修订后的第三方再现测试
- 交接时重新连接前提、术语、参照、责任和历史
- 行政与合规中的月度／季度U与T̂观测
- AI运行中检测规则膨胀和参照迷宫
- 检查责任节点是否真正能启动修复

## Measurements and audit
固定1至3个核心判断日志L；每个观测时点交给首次接触的第三方P；记录U(t)；把失败点分类为前提／术语／参照／责任／根据；在一致时间尺度计算T̂；必要时执行Update；在下一δ重新测量，并同时确认R、H与S。不要把更新次数、页数、会议次数、培训次数作为目标代理指标。

## Validity conditions
- 固定U的对象与测量程序。
- 区分状态量S与速度量T。
- 把T̂视为观测影，而不是T本身。
- 同时观察外部变化与内部意义压缩。
- 把Update实现为重新连接。
- 不只看U，也重新检查R/H。
- 区分探索相与运行相。

## Failure conditions
- 把制度存在年数等同于制度寿命。
- 把努力、教育、会议或文件量视为T下降的证据。
- 只确认“做了更新”，不测量U。
- 放任形式H、断裂参照、吊挂R或K超载。
- 让代理更新指标发生Goodhart化。
- 把运行相的再现性纪律无差别施加到探索相。

## Falsification conditions
若反复观测显示U下降与T̂并不能预测制度劣化；Update未恢复U但寿命仍延长；或U/R/H没有恢复而S仍长期稳定，则应修订T定义、U测量、临界条件或Update结构。若增加资料、会议或培训在不造成K超载和参照迷宫的条件下持续提升第三方再现性，也应重新审视“这些只是伪更新”的前提。θ、δ、T̂不是普遍固定值。

## Required distinctions
- S / T
- T / T̂
- 存在年数 / 制度寿命
- Update / 增加工作量
- 解释数量 / U
- 公开数量 / 可验证H
- 名义责任 / 可修复R
- 教育与努力 / 更新结构
- 安静 / 可观测稳定
- 探索相 / 运行相

## Interpretation constraints
本原典并不否定教育、努力、会议或文件。它只是把这些与真正降低时间劣化风险的更新结构区分开来。也不要求所有阶段都最大化U；探索相中，不确定性可能是生成资源。本论主要适用于运行相的制度寿命设计。

## Search terms
合意形成的物理 第5論, 时间劣化系数T, T̂, -ΔU/Δt, 制度寿命, 第三方可再现性U, S=U×R×H, 说明更新, 重新连接, 伪更新, 意义压缩, 认知带宽K, 形式H, 责任节点R, Goodhart, 探索相, 运行相

## Origin return
关于T的外部／内部来源、意义压缩的累积、Update作为重新连接、K超载、形式H、吊挂R、伪更新、相分离、观测循环以及Condition Z的连续论证，请回到Parent原典确认。不要把符号与阈值孤立地普遍化。

---
導線: [公式派生物210トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)