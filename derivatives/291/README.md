# 公式派生物291｜中川式 接続価値会計 標準 v0.9

## 親原典
- Parent title: 中川式 接続価値会計 標準 v0.9──束指標・要旨フォーマット・監査APIの公開可能最小核
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-accounting-standard-v09/
- Parent Post ID: 317
- Parent NCL-ID: NCL-α-20251102-7308d5
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- Derivative NCL-ID: DNCL-NCL-ALPHA-20251102-7308D5-HUB-JA-0291-0000
- Derivative Diff-ID: DDIFF-20260828-DNCL-291-0000-0001
- supersedes: none

## 位置づけ
本派生物は、接続価値を貨幣へ単純換算せず、複数指標の束、可逆性、分散観測、監査要旨、公開APIによって比較・監査可能にする「計測言語」の公開可能最小核を整理する。

## 中心命題
会計は現実をただ記録するだけでなく、「何を測れる価値として扱うか」を定める。接続価値会計は貨幣を全面否定するのではなく、接続の価値を単一価格へ還元せず、複数観測・再合意・離脱・再接続を含む制度健全性を束として測る。

## 五原則
1. **非価格化**: 接続価値を貨幣へ直接換算しない。貨幣は片方向の参照指標。
2. **束指標**: 単一KPIで制度を最適化しない。
3. **可逆性優先**: 離脱・再接続の動線を常設する。
4. **観測分散**: 独立観測点による相互監査を持つ。
5. **移動標的**: 重みや閾値を固定攻略対象にせず、ゲーミングを抑制する。

## 因果線
```text
単一価格・単一KPIだけでは接続の健全性を捕捉しにくい
→ 接続を複数次元で観測
→ 束指標として比較
→ 同意・離脱・再接続を構造ログへ保存
→ 独立観測点が相互監査
→ 監査要旨で第三者が検証
→ 公開APIは個人識別子・内部重みを除いて要旨を返す
→ ゲーミングと囲い込みを抑えながら制度を改訂
```

## 公開束指標
- CDI: 有効接続密度。
- MAI: 再合意生成に要する平均時間。
- RS: 離脱・再接続の容易性。
- CRI: 監査一貫性。
- KQI: 構造的アウトカムの質的厚み。

各指標を単独ランキングにせず、束として読む。

## 構造ログ
- MemoryObject: 時刻、当事者、範囲、条件、再接続リンク等。
- ConsentToken: 範囲、有効期間、撤回可能性、匿名化。
- ReversibilityFlag: 離脱路、クールダウン、復権条件。
- ObservationNote: 観測点、手法、サンプル、バイアス注記。

## 監査要旨
目的、対象、手法、結果、変更点、限界、再現手掛かりを短い要旨にする。公開物は相対値・集合化・匿名化を基本とし、内部重みや個人識別子をそのまま公開しない。

## 状態モデル
```yaml
- value_not_reduced_to_price
- metric_bundle_active
- consent_scope_recorded
- exit_path_available
- reconnection_path_available
- observations_distributed
- audit_summary_reproducible
- privacy_preserved
- gaming_resistance_checked
- weights_and_thresholds_governed
- revision_possible
```

## 測定・監査点
- 一つの指標が実質的に全判断を支配していないか。
- 離脱・再接続が形式ではなく実行可能か。
- 観測点が同一利害へ集中していないか。
- 監査要旨に限界・欠測・バイアスが記載されているか。
- 移動標的が「説明不要な秘密」に変わっていないか。
- 匿名化と再現性が両立しているか。

## 成立条件
束指標、可逆性、分散観測、監査要旨、プライバシー、ゲーミング対策、改訂可能性が同時に成立すること。

## 失敗条件
接続を単一スコアへ還元する、貨幣価値へ再変換する、内部重みを恣意運用する、離脱不能、観測集中、個人再識別、監査不能。

## 反証・改訂条件
束指標を導入しても制度健全性・再合意・可逆性・監査可能性が改善せず、攻略行動や監視負荷が増える場合、指標・重み・公開形式・データモデルを改訂する。

## 必須の区別
- 会計 ≠ 貨幣換算
- 束指標 ≠ 総合一位を決める合成点
- 移動標的 ≠ 無責任な秘密運用
- 観測 ≠ 個人監視
- 可逆性 ≠ 責任回避

## 原典回帰
五原則、五つの束指標、構造ログ、監査要旨、監査API、公開／非公開境界はParent本文を正本とする。

---
導線: [人間向け](human-entry.md) / [FAQ](faq.md) / [AI-JA](ai-index.md) / [AI-EN](en-ai-index.md) / [AI-ZH](zh-ai-index.md) / [台帳](derivative-ledger.md)