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

原典は合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` と表す。この式が示すのは三変数の非代替的な関係であり、一般的な採点尺度ではない。意味再現が失われればログ量を増やしてもUは戻らず、責任ノードが不明なら公開情報量を増やしてもRは戻らない。

Uは同じ一次資料から第三者が同じ意味へ再現可能に到達できるか、Rは誰がどの根拠・委任・承認関係で決めたか、Hは前回との差分、変更理由、訂正履歴を後から検証できるかを扱う。対立が存在しても三変数が維持されていれば修正可能な合意状態は残り得る。反対に、表面上の賛成や静けさがあっても三変数が失われれば安定は脆い。

## Concepts
- 合意形成の物理
- 観測可能性の原理
- 合意安定度 S
- S = U × R × H
- U: 理解可能性 / 第三者再現性
- R: 責任追跡可能性
- H: 履歴公開度 / 差分追跡可能性
- 状態観測
- 人物評価 / 状態修理
- 意見一致 / 合意
- 決定ノード
- 差分理由
- 時間方向の維持
- 非代替性
- 修理可能性

## Causal chain
炎上・対立・不信が発生する → 問いが「誰が悪いか」へ集中する → 人物評価が状態観測を置き換える → Uの意味再現可能性が確認されなくなる → Rの決定主体・根拠・責任接続が追われなくなる → Hの変更差分・理由・訂正履歴が失われる → 修理点と修正主体を特定できなくなる → 責任追及と対立固定が続く → 同型の崩壊が再発する → U/R/Hへ観測を戻す必要が生じる。

## State model
- conflict_or_disagreement_present
- shared_information_available_or_missing
- interpretability_reproducible_or_fragmented
- decision_actor_traceable_or_opaque
- decision_basis_traceable_or_missing
- change_history_available_or_erased
- difference_reason_traceable_or_missing
- u_state_observed
- r_state_observed
- h_state_observed
- first_degraded_variable_identified_or_unknown
- repair_path_open_or_closed
- temporal_maintenance_verified_or_unverified
- origin_return_verified

## Applications
**会議・組織意思決定。** 同じ資料から意味が再現できるか、決定者と根拠が追えるか、前回との差分と変更理由が残るかを監査する。

**制度変更。** 新旧制度の差分、変更理由、決定主体、対象範囲、訂正経路を追跡し、単なる制度公開と観測可能性を区別する。

**SNS・公開議論。** 切り抜き、編集、訂正、文脈消失がU/Hを壊していないか、掲載・編集判断の責任位置がRとして追えるかを見る。

**AI要約。** AIが条件、文脈、決定主体、変更理由を落とし、読みやすさだけを増やしていないかを見る。流暢さは第三者再現性の証明ではない。

## Measurements and audit
`S = U × R × H` は原典に存在する構造式である。原典はU/R/Hの一般採点尺度、係数、合格ライン、成功確率、成熟度を定義していないため、式から直接判断できるのは三変数の関係と、その低下・回復の方向である。

- 同じ一次資料から意味が再現できるか
- 解釈差の分岐点を説明できるか
- 決定主体、根拠、委任、承認を追えるか
- 誰が変更責任を持つか追えるか
- 差分、変更理由、訂正履歴を追えるか
- 情報量やログ量と観測可能性を混同していないか
- 最初に落ちた変数を特定できるか
- 他変数の増量で欠落を代替していないか
- 修正後も時間方向にU/R/Hが維持されるか

## Validity conditions
- 合意を意見一致へ縮約しない。
- U/R/Hを人物評価ではなく状態変数として扱う。
- 意味再現、責任追跡、差分追跡が可能である。
- 変数低下時に修理点と修理主体を特定できる。
- 対立や異論があっても観測可能性を維持する。
- 時間方向の変更・訂正後も追跡可能性を保つ。

## Failure conditions
- U/R/Hを人物、部署、組織のランキングへ変換する。
- 情報公開量が多いだけでU/R/Hが高いとみなす。
- ログの存在だけでRやHが成立したとみなす。
- 対立そのものを合意崩壊と判定する。
- 倫理、感情、制度内容、外部条件を三変数で消去する。
- 監視や処罰のための式へ反転利用する。

## Falsification conditions
親原典の統合監査要旨では、監査周期δでSが高いにもかかわらずD（実害）が増幅し続ける場合、Hを上げてもEが縮まらない場合、または差分追跡不能・決定ノードの恒常的消失・第三者再現の系統的失敗などの現象Mが確認された場合、定義・測定・束化に欠落があるものとして仮説Aを棄却・改訂する。

## Required distinctions
- 合意 / 意見一致
- 対立 / 合意崩壊
- 情報存在 / 解釈可能性
- 同じ資料 / 同じ意味の再現
- ログ存在 / 責任追跡可能性
- 履歴量 / 差分・変更理由の追跡可能性
- 責任追跡 / 人物処罰
- 観測可能性 / 監視強化
- 状態方程式 / 採点KPI

## Origin return
U/R/Hの厳密な定義、`S = U × R × H` の位置づけ、適用限界、反例、後続論との接続はParent URL、Parent Post ID 2788、Parent NCL-ID、Parent Diff-IDへ戻って確認できる。

---
導線: [公式派生物014トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
