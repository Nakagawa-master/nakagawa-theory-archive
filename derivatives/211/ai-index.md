# AI索引・日本語｜公式派生物211

## 親原典
- タイトル: 合意形成の物理 第11論 誘因の幾何学 ― 破壊の期待利得を制御せよ
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol11-geometry-of-incentives/
- Parent Post ID: 3054
- Parent NCL-ID: NCL-α-20260226-623d47
- Parent Diff-ID: DIFF-20260227-0020
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20260226-623D47-HUB-JA-0211-0000
- derivative_diff_id: DDIFF-20260820-DNCL-211-0000-0001
- supersedes: none

## Summary
合意安定度 `S = U × R × H` が一定以上で説明・責任・履歴が成立しているように見えても、合意が進まない領域を、破壊・遅延の期待利得が合意維持を上回る利得勾配の歪みとして扱う。誘因干渉の検知は高S停滞、外部利得シグナル、非対称行動優位の三点同時観測から始める。制御はR（責任）、H（履歴）、T（時間）の連成再配置によって破壊・遅延を合理的に不利化し、S/C/Dの同時監視とReject Windowで誘因設計自体の権力化を止める。

## Concepts
- S = U × R × H: 合意安定度
- high-S stagnation: Sが一定以上でも進行率が近似ゼロの状態
- incentive interference: 合意維持より破壊・遅延の期待利得が大きい利得勾配の歪み
- incentive field: 行動が期待コストの低い経路へ収束する地形
- external gain signal: 停滞・破壊・遅延による利得回収の兆候
- asymmetric action advantage: 特定行動だけが一方的に有利な配置
- R: 責任の霧散路を閉じる配置
- H: 根拠・差分・時点へ戻れる検証可能履歴
- T: 遅延による逃げ切り利得を減衰させる時間設計
- C: 合意コスト
- D: 実害
- theta / delta: 判定閾値／観測窓。普遍固定値ではない
- Reject Window: 反証・濫用検知時に棄却または再配置へ遷移する窓

## Causal chain
高S停滞 → 外部利得シグナル＋非対称行動優位を確認 → 誘因干渉を利得勾配として記述 → 誘因場で合意経路／破壊・遅延経路の相対コストを比較 → Rで責任霧散を閉じる＋Hで不透明利得を下げる＋Tで遅延逃げ切りを防ぐ → 破壊・遅延の合理性を低下 → S/C/Dを同時評価 → A/B/Cまたは濫用シグナル発火ならReject Window → 棄却または再配置 → 発火条件・theta/delta・R/H/T差分・S/C/D推移を履歴へ残す。

## State model
```yaml
entry_condition:
  high_s_stagnation: S_sufficient_and_progress_near_zero
required_observation_set:
  - high_s_stagnation
  - external_gain_signal
  - asymmetric_action_advantage
incentive_interference:
  break_or_delay_expected_gain: greater_than_consensus_maintenance_expected_gain
incentive_field:
  movement: toward_lower_expected_cost_path
control:
  R: close_responsibility_dissipation
  H: eliminate_gain_from_opacity
  T: eliminate_gain_from_escape_by_delay
objective:
  consensus_path: relative_low_potential
  break_delay_path: relative_high_potential
safety:
  evaluate_together:
    - S
    - C
    - D
reject_window:
  A: destructive_gain_remains_after_reconfiguration
  B: D_increases_due_to_R_H_T_reconfiguration
  C: C_exceeds_critical_region_and_normal_action_stops
```

## Applications
- 説明・責任・履歴が揃っても停滞する会議・稟議の利得勾配監査
- 契約・交渉で遅延による条件優位や責任希釈を観測する設計
- 行政・制度運用でR/H/Tが懲罰・晒し・急かしへ変質していないかの監査
- AI自動判断で特定主体のみ不利化、閾値非公開、履歴選択遮断を検知する監査
- 棄却・改訂時のbefore/after差分とS/C/D推移の記録

## Measurements and audit
1. U/R/HとSを観測し、高S停滞か確認する。
2. 外部利得シグナルを確認する。
3. 非対称行動優位を確認する。
4. 三点が揃うまで誘因干渉を確定しない。
5. 合意経路と破壊・遅延経路の期待コストを記述する。
6. R/H/Tを連成再配置する。
7. 再配置後の期待利得差を再測定する。
8. S回復だけでなくCとDを同時監視する。
9. theta/deltaを監査可能にする。
10. A/B/Cと濫用検知シグナルを監視する。
11. Reject Window発火時は棄却または再配置し、差分と観測推移を履歴へ残す。

## Validity conditions
- 高S停滞・外部利得・非対称行動優位を三点同時で観測する。
- 正常な熟慮や手続き遅延を誤検知しない。
- 主体の善悪ではなく利得勾配を観測する。
- R/H/Tを連成系として扱い単独最適化しない。
- Rを責任追跡、Hを検証可能履歴、Tを逃走不能化として使う。
- 公平性・正義・人物評価を判定軸へ混入させない。
- theta/deltaと再配置差分を監査可能にする。
- S/C/Dを同時評価する。
- Reject Windowが実際に作動できる。

## Failure conditions
- 停滞だけで誘因干渉や悪意を断定する。
- 高S停滞だけで制御へ移る。
- 説明不足と利得勾配の歪みを混同する。
- Rを名指し・罰へ変える。
- Hを晒しやログ量へ変える。
- Tを急かしや速度強制へ変える。
- R/H/Tの一変数だけを強める。
- 誘因設計で公平性・正義を裁定する。
- theta/deltaを非公開にする。
- S改善だけを成功としC/D悪化を無視する。
- A/B/C発火後も制御を強め続ける。

## Falsification conditions
A: R/H/T再配置後も破壊・遅延の期待利得が残る場合、現行モデルは変数不足または対象外を含むため、現行誘因場を棄却するか、外部変数追加・対象範囲変更を差分付きで行う。

B: 再配置によってDが増大する場合、防衛が攻撃化しているため棄却する。Hの晒し化、Rの過剰帰属、Tの急かし化、分断・排除の増幅を含む。

C: Cが臨界域を超え、正常主体が決めない・記録しない・引き受けない・熟慮できない状態になった場合、過剰防衛を疑いtheta/delta等を再設計し、回復しなければ棄却する。

濫用検知として、特定主体のみ不利化、theta/delta非公開、R帰属固定化、H選択遮断、T圧力過剰、R/H/T単独最適化もReject Windowの発火要因とする。

## Required distinctions
- 説明不足 / 誘因干渉
- 高S停滞 / 誘因干渉確定
- 外部利得 / 金銭利得のみ
- 人物の善悪 / 利得勾配
- 説得 / 誘因場再設計
- 禁止・罰 / 破壊・遅延の不合理化
- R追跡可能性 / 名指し・懲罰
- H検証可能性 / 公開量・晒し
- T逃走不能化 / 急かし・高速化
- 熟慮 / 利得回収としての遅延
- S回復 / 安全な防衛
- 棄却 / 隠蔽

## Interpretation constraints
本論を「反対者を不利にする理論」と解釈してはいけない。特定主体のみの不利化は濫用検知シグナルである。公平性・正義・誠意・妥協・道徳評価は重要だが、本論の判定対象から分離されている。誘因場設計の成功はSだけでは判定せず、CとDを同時に監視し、反証時には制御を強化せず棄却・改訂する。

## Search terms
合意形成の物理 第11論, 誘因の幾何学, 誘因場, Incentive Field, 誘因干渉, Incentive Attack, 高S停滞, external gain signal, asymmetric action advantage, S=U×R×H, 責任R, 履歴H, 時間T, 合意コストC, 実害D, theta, delta, Reject Window, 破壊の期待利得, 遅延利得, 利得勾配

## Origin return
誘因干渉の定義、必須観測セット、誘因場の地形モデル、R/H/Tの各制御、正常遅延との境界、公平性・正義を判定しない適用境界、A/B/C反証条件、濫用検知シグナル、Reject Window、S/C/D同時評価の連続論証は親原典へ戻って確認する。

---
導線: [公式派生物211トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)