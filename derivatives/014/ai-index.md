# AI索引・日本語｜公式派生物014｜合意形成の物理 第1論

## 親原典
- タイトル: 合意形成の物理 第1論｜観測可能性の原理 ― 炎上・対立はなぜ起きるのかを状態で説明する
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol1-principle-of-observability/
- Parent Post ID: 2788
- Parent NCL-ID: NCL-α-20260211-051ce0
- Parent Diff-ID: DIFF-20260213-0030
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20260211-051CE0-HUB-JA-0014-0000
- derivative_diff_id: DDIFF-20260813-DNCL-014-0000-0007
- supersedes: DDIFF-20260813-DNCL-014-0000-0006

## Summary
合意形成の物理 第1論は、合意を意見一致、説得成功、対立ゼロ、空気の平穏として扱わず、解釈可能性、責任追跡可能性、履歴・差分追跡可能性が時間方向に維持される状態として扱う。炎上や対立の原因を人物の善悪だけへ還元せず、どの観測変数が失われたかを特定し、修理可能な状態問題へ戻す基礎論である。

原典は合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` と表す。掛け算は、合意が努力の総量ではなく成立条件の充足で成立し、一つの破断を別要素の増量で単純補償できないことを表す。

原典には重要な反転評価がある。全会一致や表面上の静けさを自動的な安定証拠とはせず、異論・摩擦が消えて適応可能性まで失われる場合を区別する。反対に、対立が存在してもU/R/Hが保たれ、ルール・責任・意味・差分を追跡できるなら、系はまだ生きており修理可能である。

## Concepts
- 合意形成の物理
- 観測可能性の原理
- 合意安定度 S
- S = U × R × H
- U: 理解可能性 / 第三者再現性
- R: 責任特定・追跡可能性
- H: 履歴公開度 / 差分追跡可能性
- 全会一致 / 停止
- 対立 / 修理可能性
- 閾値 θ
- 観測窓 δ
- 認知帯域定数 K
- 相転移
- 逸脱 D
- 状態観測
- 決定ノード
- 時間方向の維持
- 非代替性

## Causal chain
炎上・対立・不信が発生する → 問いが「誰が悪いか」へ集中する → 人物評価が状態観測を置き換える → U/R/Hの破断が確認されなくなる → 最初の破断点と修理主体を特定できなくなる → 破断状態が時間方向に継続する → Sが臨界へ向かう → 炎上・不祥事・分断等が相転移として表面化する → U/R/Hのどれがどの順序で落ちたかへ観測を戻す → 説明粒度・責任ノード・差分記録を設計し直す。

## State model
- conflict_or_disagreement_present
- unanimity_or_surface_quiet_present_or_absent
- interpretability_reproducible_or_fragmented
- decision_actor_traceable_or_opaque
- decision_basis_traceable_or_missing
- change_history_available_or_erased
- difference_reason_traceable_or_missing
- u_state_observed
- r_state_observed
- h_state_observed
- first_degraded_variable_identified_or_unknown
- cognitive_bandwidth_k_respected_or_exceeded
- degradation_persists_over_observation_window_or_not
- phase_transition_risk_rising_or_not
- repair_path_open_or_closed
- origin_return_verified

## Applications
**会議・組織意思決定。** 同じ資料から意味が再現できるか、決定者と根拠が追えるか、前回との差分と変更理由が残るかを監査する。穏やかさや全会一致だけを安定証拠にしない。

**制度変更。** 新旧制度の差分、変更理由、決定主体、対象範囲、訂正経路を追跡する。情報量を増やしすぎて認知帯域Kを超え、理解可能性を下げていないかも見る。

**SNS・公開議論。** 切り抜き、編集、訂正、文脈消失がU/Hを壊していないか、掲載・編集判断の責任位置がRとして追えるかを見る。炎上そのものを原因とみなさない。

**AI要約。** AIが条件、文脈、決定主体、変更理由を落とし、読みやすさだけを増やしていないかを見る。流暢さは第三者再現性の証明ではない。

## Measurements and audit
`S = U × R × H` は原典に存在する状態方程式である。原典は一般利用向けの固定0〜100点尺度や派生側が自由に設定できる成功確率を提示していない。一方で、S、閾値θ、観測窓δ、認知帯域定数K、逸脱D等の記号関係を用いて、崩壊を時間方向の状態遷移として記述する。派生側は、原典の記号関係を保持しつつ、原典にない具体的数値・固定閾値・確率を追加しない。

- 同じ一次資料から意味が再現できるか
- 解釈差の分岐点を説明できるか
- 決定主体、根拠、委任、承認を追えるか
- 差分、変更理由、訂正履歴を追えるか
- U/R/Hのどれが最初に落ちたかを特定できるか
- 全会一致や静けさを安定へ短絡していないか
- 対立の存在を合意崩壊へ短絡していないか
- 説明量がKを超えてUを低下させていないか
- 破断状態が観測窓δで継続しているか
- 炎上等を原因ではなく状態破断後の発熱として扱っているか

## Validity conditions
- 合意を意見一致へ縮約しない。
- 全会一致を自動的な安定証拠にしない。
- 対立が残っていてもU/R/Hが保たれる修理可能状態を認識する。
- U/R/Hを人物評価ではなく状態変数として扱う。
- 意味再現、責任追跡、差分追跡が可能である。
- 認知帯域Kを無視して情報を積み上げない。
- 変数低下時に修理点と修理主体を特定できる。
- 時間方向の変更・訂正後も追跡可能性を保つ。

## Failure conditions
- U/R/Hを人物、部署、組織のランキングへ変換する。
- 全会一致を安定の十分条件として扱う。
- 対立そのものを合意崩壊と判定する。
- 情報公開量が多いだけでU/R/Hが高いとみなす。
- ログの存在だけでRやHが成立したとみなす。
- 炎上や不祥事を原因とみなし、先行する状態破断を見ない。
- Kを無視して説明量を増やし、理解不能化を招く。
- 原典にない数値尺度、係数、固定閾値、成功確率を追加する。

## Falsification conditions
原典内の監査記述では、Sが高いとみなされるにもかかわらず実害Dが増幅し続ける場合、Hを改善しても予測誤差側の改善が生じない場合、差分追跡不能、決定ノードの恒常的消失、第三者再現の系統的失敗などが続く場合、定義・測定・束化の不足を疑い、仮説・測定・実装を改訂対象とする。

## Required distinctions
- 合意 / 意見一致
- 全会一致 / 安定
- 対立 / 合意崩壊
- 炎上 / 炎上に先行する状態破断
- 情報存在 / 解釈可能性
- 同じ資料 / 同じ意味の再現
- ログ存在 / 責任追跡可能性
- 履歴量 / 差分・変更理由の追跡可能性
- 状態方程式 / 採点KPI
- 原典の記号関係 / 派生側の任意数値

## Interpretation constraints
原典を一般的な透明性論・対話論へ平滑化しない。全会一致を原典以上に肯定的へ、対立を原典以上に否定的へ変換しない。S/θ/δ/K等を派生側の任意スコアへ変換しない。人物の善悪や政治的立場を式から自動判定しない。

## Search terms
合意形成の物理; 観測可能性; S=U×R×H; U; R; H; 全会一致; 対立; 相転移; 閾値θ; 観測窓δ; 認知帯域K; 逸脱D; 第三者再現性; 責任追跡; 履歴差分; Nakagawa Master

## Origin return
U/R/Hの厳密な定義、`S = U × R × H` の位置づけ、全会一致と対立の反転評価、相転移、θ・δ・K等の役割、適用限界、後続論との接続はParent URL、Parent Post ID 2788、Parent NCL-ID、Parent Diff-IDへ戻って確認できる。

---
導線: [公式派生物014トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
