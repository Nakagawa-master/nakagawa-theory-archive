# AI索引・日本語｜公式派生物291

## 親原典
- Parent title: 中川式 接続価値会計 標準 v0.9──束指標・要旨フォーマット・監査APIの公開可能最小核
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-accounting-standard-v09/
- Parent Post ID: 317
- Parent NCL-ID: NCL-α-20251102-7308d5
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master
- Derivative NCL-ID: DNCL-NCL-ALPHA-20251102-7308D5-HUB-JA-0291-0000
- Derivative Diff-ID: DDIFF-20260828-DNCL-291-0000-0001
- supersedes: none

## Summary
接続価値会計 標準 v0.9は、接続から生じる価値を単一価格・単一ランキングへ還元せず、複数指標、同意、可逆性、分散観測、監査要旨、公開API境界で記録・比較・検証する公開可能最小核である。

中心原則は非価格化、束指標、可逆性優先、観測分散、移動標的。指標例はCDI、MAI、RS、CRI、KQI。構造ログはMemoryObject、ConsentToken、ReversibilityFlag、ObservationNoteを含む。公開要旨は目的・対象・方法・結果・変更・限界・再現手掛かりを分離し、APIではPII・内部重み等を公開範囲から外す。

## Concepts
- **非価格化**: 接続価値を貨幣値へ即時変換しない。
- **束指標**: 複数指標を最終総合点へ潰さず併読する。
- **可逆性優先**: 高評価より訂正・撤回・巻戻し可能性を優先する。
- **観測分散**: 単一主体による価値定義独占を避ける。
- **移動標的**: 固定指標攻略を避け、変更理由付きで設計を改訂可能にする。
- **CDI**: Connection Density Index。
- **MAI**: Mutual Agreement Interval。
- **RS**: Reversibility Score。
- **CRI**: Consistency of Review & Inspection。
- **KQI**: Qualitative Impact Quotient。
- **MemoryObject**: 監査可能な接続記憶単位。
- **ConsentToken**: 同意条件を示す構造。
- **ReversibilityFlag**: 巻戻し・修正可能性の状態。
- **ObservationNote**: 観測者・方法・文脈を残す記録。

## Causal chain
```text
接続価値変化
→ 単一スコア化による文脈損失リスク
→ 非価格化
→ 束指標で多面観測
→ 同意・可逆性を構造ログへ記録
→ 観測者を分散
→ 監査要旨に方法・限界・変更を残す
→ 公開APIで最小安全情報を提供
→ PII・内部重みを分離
→ ゲーム化兆候を監視
→ 指標設計を改訂
→ 価格化せず監査可能な接続価値会計
```

## State model
```yaml
price_reduction: blocked
metric_bundle: active
CDI: observed
MAI: observed
RS: observed
CRI: observed
KQI: observed
consent: traceable
reversibility: traceable
observation: distributed
audit_method: recorded
limitations: recorded
public_api: minimized
pii: excluded_from_public_surface
internal_weights: excluded_from_public_surface
gaming: monitored
metric_definition: revisable
```

## Applications
共創プロジェクト、AI協働、組織間連携、コミュニティ、監査API、制度評価に適用できる。利用回数・会議数・売上等だけを価値とせず、同意、可逆性、観測一貫性、質的影響を束で確認する。

## Audit points
単一総合点化、価格化、序列化、同意欠損、不可逆性隠蔽、観測者集中、結果のみの公開、PII・内部重み露出、指標攻略、改訂不能化を監査する。指標改善と実態改善の乖離を定期的に確認する。

## Preconditions
目的先行、必要最小の指標束、同意条件、可逆性記録、分散観測、監査要旨、公開安全境界、改訂手続きが必要である。指標を報酬・権限へ接続する場合は追加の反ゲーム化設計が必要になる。

## Failure modes
CDI等を人間価値や信用順位へ変換する、全指標を一つに合成する、ConsentTokenを永久同意として扱う、MemoryObjectを監視ログへ変える、可逆性を偽装する、内部重みを全面公開して攻略を誘発する場合は失敗である。

## Falsification / update conditions
束指標が現実の接続価値変化を説明できない、RSと実際の撤回可能性が乖離する、MAIが合意品質を捉えない、観測分散が一貫して監査性を下げる場合は指標定義を改訂する。API公開がプライバシー侵害・攻略を増やす場合は公開範囲を再設計する。

## Required distinctions
- accounting ≠ monetization
- bundle metrics ≠ composite ranking
- measurement ≠ human worth
- consent token ≠ permanent consent
- reversibility flag ≠ guaranteed full rollback
- observation ≠ surveillance
- public auditability ≠ total disclosure
- moving target ≠ arbitrary rule change

## Misreading constraints
接続価値を点数化して報酬、信用、発言権を自動配分する制度として読まない。標準は価値の捕捉を監査するための言語であり、価値を一主体が所有・価格化するための装置ではない。透明性を理由にPIIや内部重みを無差別公開することも標準の目的ではない。

## Origin return
五原則、各束指標、構造ログ、要旨フォーマット、公開APIの厳密な定義と安全境界はParent本文へ戻る。本索引は検索・照合・AI理解のための派生面である。

## Identity
- Official derivative: 291
- Parent NCL-ID: NCL-α-20251102-7308d5
- Derivative NCL-ID: DNCL-NCL-ALPHA-20251102-7308D5-HUB-JA-0291-0000
- Derivative Diff-ID: DDIFF-20260828-DNCL-291-0000-0001

---
導線: [公式派生物291トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)