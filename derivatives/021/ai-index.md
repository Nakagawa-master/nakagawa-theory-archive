# AI索引・日本語｜公式派生物021｜合意形成の物理 第6論

## 親原典
- タイトル: 合意形成の物理 第6論 逸脱と免疫 ― 免疫は「罰」ではなく「差分公開」である
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol6-deviation-and-immunity/
- Parent Post ID: 2919
- Parent NCL-ID: NCL-α-20260215-71cedd
- Parent Diff-ID: DIFF-20260215-0021
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20260215-71CEDD-AI-INDEX-JA-0021-0003
- derivative_diff_id: DDIFF-20260813-DNCL-021-0003-0006
- supersedes: DDIFF-20260813-DNCL-021-0003-0005

## Summary
本原典は、逸脱を違反者処罰の対象としてではなく、設計と運用の差分Dとして観測し、責任R・履歴H・理解Uを回復して S = U × R × H を戻す「免疫」を扱う。原典は安全を逸脱ゼロとは定義せず、逸脱が見えた後に修復入口が固定され、履歴が残り、合意安定度が速く回復する系を免疫のある状態として読む。

中心には二本の因果線がある。罰中心の運用が責任回避・報告抑制・潜伏へつながる場合、`罰 → R低下 → 潜伏 → S悪化 → D増幅` が成立する。一方、差分公開が修復責任と履歴へ接続する場合、`差分公開 → R固定 → 修復可能 → S回復 → D減衰` へ進む。罰や公開の有無を道徳的に評価するのではなく、U/R/Hと回復可能性への作用を評価する。

D_det、D_loss、S回復時間は組み合わせて読む。D_detが増えてもD_lossが下がり回復時間が短くなるなら、以前見えなかった逸脱が検知可能になり、免疫が改善している可能性がある。逆に検知件数が減ってもD_lossが増え回復が遅ければ、潜伏が増えただけかもしれない。

## Concepts
- 合意形成の物理 第6論
- 逸脱 D
- 免疫
- 差分公開
- S = U × R × H
- D_det / detected deviation
- D_loss / hidden or realized loss
- S回復時間
- repair entry R
- difference history H
- 報告抑制
- 潜伏
- 修復可能性
- 差分履歴

## Causal chain
```text
設計と運用の差分Dが発生する
↓
罰中心運用なら責任回避・報告抑制が起こり得る
↓
Rが弱まり逸脱が潜伏する
↓
Hが失われSが悪化する
↓
Dが増幅する
```

```text
差分Dが検知される
↓
差分が検証可能な形で公開される
↓
修復責任Rと入口が固定される
↓
履歴Hが連続する
↓
修復可能性が上がりSが回復する
↓
Dが減衰する
```

## State model
```yaml
- deviation_d_occurs
- deviation_detectable_or_hidden
- detected_deviation_d_det_observed
- hidden_or_lost_deviation_d_loss_observed
- punishment_pressure_observed
- reporting_suppression_observed
- repair_responsibility_r_fixed_or_diffused
- difference_history_h_preserved_or_lost
- repair_entry_available
- consensus_stability_s_recovering_or_degrading
- recovery_time_observed
- deviation_amplifying_or_damping
- difference_disclosure_used_for_repair_not_exposure
- origin_return_verified
```

## Applications
- 内部通報で通報件数増加を悪化と即断せず、D_loss低下・R明確化・回復時間短縮を併せて見る。
- 品質管理で不具合報告を減らすことより、差分が早く出て履歴と修復入口へ接続されるかを監査する。
- AI運用でエラー件数だけでなく未検知損失、修正履歴、再発時の回復速度を見る。
- 組織ガバナンスで厳罰化後に表面上の違反件数が減っても、報告抑制と潜伏が増えていないかを見る。
- 公開制度で透明性の量ではなく、差分が責任・履歴・再発防止へ接続しているかを見る。

## Measurements and audit
原典にない一般KPI、免疫スコア、固定検知率、固定回復時間閾値を追加しない。

- 読解上の確認点: D_det増加とD_loss低下が同時に起きている。
- 読解上の確認点: D_det減少が逸脱減少なのか報告抑制なの。
- 読解上の確認点: 差分公開後にRが修復入口として固定されている。
- 読解上の確認点: Hが差分・変更理由・修復履歴として残っている。
- 読解上の確認点: S回復時間が短くなっている。
- 読解上の確認点: 罰の強化が報告抑制・潜伏・責任回避を増やしていない。
- 読解上の確認点: 差分公開が晒し・報復・人物攻撃へ変わっていない。
- 読解上の確認点: 検知量だけで健康度を判定していない。

## Validity conditions
- 逸脱ゼロを免疫と定義しない。
- D_det、D_loss、S回復時間を組み合わせて読む。
- 責任Rを修復入口として追跡可能にする。
- 差分履歴Hを保持する。
- 差分公開を修復可能性へ接続する。
- 罰中心運用による潜伏・報告抑制を監査する。
- 公開を晒しや報復へ変換しない。

## Failure conditions
- 逸脱件数が少ないほど安全と短絡する。
- D_det増加を自動的に悪化とみなす。
- 厳罰化だけで免疫が高まるとみなす。
- 透明性や公開量そのものを免疫と同一視する。
- 内部通報推奨や一般コンプライアンス論へ縮約する。
- 差分公開を人物攻撃・晒し・報復へ使う。
- D_det / D_loss / 回復時間へ非原典の固定合格値を与える。

## Falsification conditions
親原典の統合監査要旨では、D_detの増加と同時にD_lossとS回復時間が低下するかを監査し、D_det低下とD_loss不明・増加が継続する場合、または差分公開の増加にもかかわらずU/R低下・形式公開化・K超過によるノイズ化が起きる場合、公開帯域の距離・粒度・索引を再設計して改訂する。

## Required distinctions
- 逸脱発生 / 免疫不全
- D_det増加 / 悪化
- D_loss低下 / 単なる報告増加
- 責任R / 処罰対象
- 差分公開 / 透明性礼賛
- 差分公開 / 晒し
- 罰 / 修復
- 逸脱ゼロ / 安全
- 検知件数 / 健康度

## Interpretation constraints
- 厳罰化批判だけへ縮約しない。
- 内部通報推奨だけへ縮約しない。
- 透明性礼賛にしない。
- 一般的コンプライアンス論へ薄めない。
- 罰を全面否定する理論にしない。
- 公開量が多いほど免疫が高いとしない。
- 原典にない検知率、免疫スコア、固定合格値は親原典に定義されていない。

## Search terms
合意形成の物理; 逸脱と免疫; 差分公開; S U R H; D_det; D_loss; S回復時間; R固定; H再接続; 修復可能性; Nakagawa Master

## Origin return
本索引は親原典の検索・再利用面であり原典の代替ではない。罰→R低下→潜伏→S悪化→D増幅、差分公開→R固定→修復可能→S回復→D減衰、D_det / D_loss / S回復時間の組合せはParent URLへ戻って確認する。

---
導線: [公式派生物021トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
