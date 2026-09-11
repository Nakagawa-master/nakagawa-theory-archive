# AI索引・日本語｜公式派生物210

## 親原典
- タイトル: 合意形成の物理 第5論 時間劣化と制度寿命 ― 説明更新なき制度は必ず死ぬ
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol5-time-decay-and-system-longevity/
- Parent Post ID: 2897
- Parent NCL-ID: NCL-α-20260215-e2d7e7
- Parent Diff-ID: DIFF-20260215-0025
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20260215-E2D7E7-HUB-JA-0210-0000
- derivative_diff_id: DDIFF-20260820-DNCL-210-0000-0001
- supersedes: none

## Summary
制度寿命を存続年数ではなく第三者再現可能性Uが臨界域へ入るまでの時間として捉え、状態量S=U×R×Hと時間劣化速度Tを分離する。運用上の観測影は `T̂ = −ΔU/Δt`。Tは外部環境変化と内部意味圧縮によって説明が現実へ追随できなくなる速度であり、寿命延長の操作点は努力量ではなく、前提・用語・参照・責任・履歴を再接続してUを回復するUpdate構造である。

## Concepts
- U: 第三者再現可能性
- R: 責任主体の一意性／修復入口
- H: 検証可能な判断履歴の公開性
- S = U × R × H: 合意安定度という状態量
- T: 説明が環境変化へ追いつけなくなる時間劣化速度
- T̂ = −ΔU/Δt: 運用相でのTの観測影
- institutional lifetime: Uが臨界域へ入るまでの時間
- meaning compression: 成功・習熟で前提等が省略される内部劣化源
- Update: U回復のための再接続
- pseudo update: 更新後もUが回復しない状態
- K: 認知帯域
- formal H: 公開しているが第三者検証不能な履歴
- hanging R: 罰・名義だけとなり修復入口として働かない責任
- exploration / operation: 探索相と運用相

## Causal chain
制度の反復運用 → 外部環境変化＋内部意味圧縮 → 説明と現実の座標差 → 前提省略・用語漂流・参照短絡・責任ノード溶解 → U(t)低下 → T̂で低下傾向を観測 → R/Hも侵食 → S低下 → S<θがδ継続 → 崩壊相。修復は追加資料ではなく断線位置の再接続 → 次δでU/R/H/Sを再測定する。

## State model
```yaml
S: U_times_R_times_H
state_quantity: S
velocity_quantity: T
T_hat: minus_delta_U_over_delta_t
T_sources:
  external: environment_change
  internal: meaning_compression
lifetime: time_until_U_enters_critical_region
update_success: U_recovers_after_update
pseudo_update: U_t_plus_delta_less_or_equal_U_t
critical_transition: S_below_theta_for_delta
phase_boundary:
  exploration: uncertainty_is_generation_resource
  operation: reproducibility_is_sustainability_condition
```

## Applications
- 規程改訂後の第三者再現テスト
- 引継ぎ時の前提・用語・参照・責任・履歴の再接続
- 行政・監査での月次／四半期U・T̂観測
- AI運用におけるルール増殖・参照迷路の検出
- 責任ノードが修復入口として機能するかの確認

## Measurements and audit
1. 中核判断ログLを1〜3件固定する。
2. 時点ごとに初見第三者Pへ渡す。
3. U(t)＝同じ判断へ到達できた割合を記録する。
4. 失敗点を前提／用語／参照／責任／根拠へ分類する。
5. 同じ時間尺度でT̂を計算する。
6. Updateを実施する。
7. 次のδでUが回復したか確認する。
8. R/HとS全体も再確認する。
代理指標として更新回数・ページ数・会議数・研修数を目標化しない。

## Validity conditions
- Uの対象と測定手順を固定する。
- SとTを混同しない。
- T̂をTそのものではなく観測影として扱う。
- 外部変化と内部意味圧縮を両方見る。
- Updateを再接続として実装する。
- UだけでなくR/Hも確認する。
- 運用相と探索相を分ける。

## Failure conditions
- 長寿命を単なる存続年数で判定する。
- 努力・教育・会議・資料量をT低下と同一視する。
- Update実施を成果にしてUを測らない。
- 形式H、切れた参照束、吊るしR、K超えを放置する。
- Goodhart化した代理指標で更新を評価する。
- 探索相へ運用相の再現性規律を無差別適用する。

## Falsification conditions
U低下とT̂が制度劣化を予測しない、Update後にUが回復しなくても寿命が延びる、U/R/Hの回復なしにSが安定する等が反復される場合は、T定義・U測定・臨界条件・Update構造を改訂する。また資料・会議・研修増加がK超えなしに継続的U回復を生むなら、単なる擬似更新とする前提を再検討する。θ・δ・T̂は普遍固定値ではない。

## Required distinctions
- S / T
- T / T̂
- 存続年数 / 制度寿命
- Update / 作業追加
- 説明量 / U
- 公開量 / 検証可能H
- 責任名義 / 修復入口R
- 教育・努力 / 更新構造
- 静けさ / 観測可能な安定
- 探索相 / 運用相

## Interpretation constraints
本論は教育・努力・資料を否定しない。それらがTを下げる更新構造と同じではないと区別する。またU最大化を全局面へ要求しない。探索相では未確定性が価値を持ち得るため、本論の主対象は運用相の制度寿命設計である。

## Search terms
合意形成の物理 第5論, 時間劣化係数T, T̂, -ΔU/Δt, 制度寿命, 第三者再現可能性U, S=U×R×H, 説明更新, 再接続, 擬似更新, 意味圧縮, 認知帯域K, 形式H, 責任ノードR, Goodhart, 探索相, 運用相

## Origin return
Tの外部・内部発生源、意味圧縮累積、Updateの再接続定義、K超え、形式H、吊るしR、擬似更新、相分離、観測ループ、Condition Zとの関係は親原典へ戻って確認する。記号や閾値を単独で普遍値化しない。

---
導線: [公式派生物210トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)