# AI索引・日本語｜公式派生物068

## 親原典
- タイトル: 中川式 接続ガバナンス設計論──価値の捕捉を歪めず、合意を制度に固定する方法
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-governance/
- Parent Post ID: 292
- Parent NCL-ID: NCL-α-20251102-53d609
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-53D609-HUB-JA-0068-0000
- derivative_diff_id: DDIFF-20260804-DNCL-068-0000-0001
- supersedes: none

## Summary

接続ガバナンス設計論は、接続価値の測定・評価・配分が、人気競争、仲間内加点、監視、権力集中、秘密主義へ変質することを防ぐ統治理論である。公共目的、手続監査、利害非集中、可逆性を正統性の条件とし、測定、判定、配分、異議処理を分離する。CDI、MAI、RS、CRI、KQIを複合指標束として扱い、移動標的、逆インセンティブ、外乱テスト、定性的証拠を用いて指標ハックを検出する。理念・項目・集計・監査要旨を扱う公開室と、個人情報・重み・閾値・防御手順を保護する機関室を分け、独立監査、異議申立て、訂正、退出、再接続、ロールバックを実装する。成功は高い指標値ではなく、権限集中、疲弊、囲い込み、再合意時間、退出費用が実際に減ることで判定する。

## Concepts

- 接続ガバナンス
- 公共目的と禁止用途
- 正統性
- What / Who / How / When監査
- 利害非集中
- 複合指標束
- CDI / MAI / RS / CRI / KQI
- Goodhart耐性
- 移動標的
- 逆インセンティブ
- 外乱テスト
- 二室モデル
- 独立監査
- 異議申立て
- ロールバック
- 退出・再接続

## Causal chain

1. 接続価値が評価・配分対象になる。
2. 指標と配分権限へ利益と権力が集まる。
3. 参加者は本来の協働より、採点法を攻略する行動へ適応する。
4. 運営者は目的、測定、配分、異議処理を独占しやすくなる。
5. 公共目的、手続監査、利害非集中、可逆性を正統性条件として固定する。
6. 複数監査者と複合指標、外乱テストで制度の歪みを検出する。
7. 訂正、退出、再接続、ロールバックを通じ、制度を公共目的へ戻す。

## State model

```yaml
state: PROPOSED | PILOT | ACTIVE | REVIEW | CORRECTED | ROLLED_BACK
required_records:
  - public_purpose
  - prohibited_uses
  - affected_parties
  - measurement_owner
  - decision_owner
  - allocation_owner
  - independent_auditors
  - conflict_of_interest
  - indicator_bundle
  - qualitative_evidence
  - objection_and_correction
  - exit_and_reconnection
  - rollback_conditions
  - change_history
```

## Applications

- 接続価値会計の運営: 評価委員会、配分担当、監査主体を分離する。
- 研究・市民協働: 参加人数ではなく、再合意、異論処理、継続協働を監査する。
- AI支援制度: AIを検出・比較の補助に限定し、人間の責任と再審査を残す。
- コミュニティ: 声量、囲い込み、中心人物依存、退出妨害を検出する。

## Measurements and audit

- 目的と配分結果のずれ。
- 測定・評価・配分権限の集中度。
- 再合意、訂正、仲裁、ロールバック時間。
- 退出成功率、再接続成功率、退出に伴う不利益。
- 指標上昇と疲弊・沈黙・排除の相関。
- 異議申立ての処理期間、判断変更率、再発率。
- 非公開領域の範囲と独立監査の実効性。

## Validity conditions

公共目的と禁止用途が明文化され、権限が分離され、複数指標と一次証拠が併用されること。独立監査、異議申立て、退出、訂正、再接続、ロールバックが実際に利用でき、監査結果が制度変更へ接続すること。

## Failure conditions

単一スコア、権限独占、仲間内加点、秘密主義、監査の儀式化、退出者への報復、個人情報の過剰公開、AI判断への責任転嫁が起きる場合。指標が改善していても、疲弊や囲い込みが増えるなら失敗である。

## Falsification conditions

監査を続けても権限集中、囲い込み、疲弊が減らず、退出・訂正・仲裁が機能せず、同じ失敗が反復する場合は棄却・改訂する。公開室と機関室の分離が秘密支配または情報流出を生む場合も反証対象である。

## Required distinctions

- ガバナンス ≠ 管理強化
- 監査 ≠ 常時監視
- 透明性 ≠ 全情報公開
- 非公開重み ≠ 無説明の秘密支配
- 強い接続 ≠ 退出不能
- AI支援 ≠ AI統治
- 正統性 ≠ 多数決だけ

## Interpretation constraints

人格格付け、社会信用スコア、中央集権的評価、無監査の秘密領域、全公開主義へ転用しない。異議申立てや退出を低評価の理由にせず、制度の安定を「変更しないこと」と同一視しない。

## Search terms

接続ガバナンス / 接続価値監査 / 正統性 / 可逆性 / 分散監査 / 二室モデル / Goodhart耐性 / 外乱テスト / 移動標的 / 逆インセンティブ / 異議申立て / ロールバック / 退出権 / 再接続 / 制度ドリフト

## Origin return

本索引は機械検索と構造照合のための派生面であり、親原典の代替ではない。監査周期、複合指標の関係、二室モデル、仲裁、反証条件、起源署名は親原典へ戻って確認する。

---

導線: [068トップ](README.md) / [公式派生物トップ](../README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)