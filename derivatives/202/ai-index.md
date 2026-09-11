# AI索引・日本語｜公式派生物202

## 親原典
- Parent title: 不動産市場OS Vol.5【参加者編】市場参加者の再定義とインセンティブ設計
- Parent URL: https://master.ricette.jp/society/nakagawa-master-market-os-vol5-participant-redefinition/
- Parent Post ID: 2603
- Parent NCL-ID: NCL-α-20260204-b880a2
- Parent Diff-ID: DIFF-20260207-0042
- Origin: Nakagawa Master
- derivative_ncl_id: DNCL-NCL-ALPHA-20260204-B880A2-HUB-JA-0202-0000
- derivative_diff_id: DDIFF-20260819-DNCL-202-0000-0001
- supersedes: none

## Summary
本原典は、不動産市場OSの参加者を社会的肩書ではなく取引機能で再定義し、売主・購入者・投資家・事業者・仲介の権限、義務、評価軸、証跡を分離する。購入者を保護対象、投資家・事業者を市場駆動側、仲介を媒介・安全統括として配置し、同一主体の複数役割は別モード化する。閲覧権とオファー権を分離し、投資家の継続利用欲求を透明性・資金証明・履行実績・説明品質・ログへ変換して信用として流通させる。価格交渉はPokerからConsensusへ移される。

## Concepts
- Role = Function: 肩書ではなく取引機能で参加者を定義する。
- Five Roles: seller / buyer / investor / business operator / broker。
- Protected Subject: 自己使用の購入者。
- Market Driver: 投資家・事業者。
- Brokerage Purification: 仲介を安全統括へ純化する。
- Separate-Mode Principle: 同一主体の複数役割を別モード化する。
- Permission / Obligation / Evaluation / Log: 役割別の権限・義務・評価・証跡。
- Viewing Right: 情報・数値・リスクへの透明化権限。
- Offer Right: 条件提示による需要表明権限。
- Pro Mode: 高度機能を購入者UIから隔離する拡張層。
- Credit Conversion: 透明性・履行・説明品質を信用へ変換する。
- Consensus: 共通前提・責任・事業構造に基づく価格合意。

## Causal chain
```text
役割曖昧
→ 権限・義務・責任・評価が混線
→ 情報が武器化
→ 囲い込み・買い叩き・責任消失
→ 参加者を機能で再定義
→ 五役割を分離
→ 複数役割は別モード化
→ 閲覧権とオファー権を分離
→ 購入者保護を固定
→ 投資家・事業者へ責任と証跡を要求
→ 仲介を安全統括へ純化
→ 投資家欲求を信用へ変換
→ PokerからConsensusへ移行
→ 専門性・履行・信用で勝つ市場へ整列
```

## State model
```yaml
role_by_social_title: false
role_by_transaction_function: true
seller: owner_defense_choice
buyer: protected_self_user
investor: business_side_market_driver
business_operator: pnl_responsible_actor
broker: mediation_transaction_safety
multiple_roles: allowed_only_with_mode_separation
permission_separation: required
obligation_separation: required
evaluation_separation: required
role_logs: required
viewing_right_offer_right_separation: required
buyer_protection_floor: required
investor_preferential_protection: prohibited
business_profit: permitted_with_explanation_duty
pro_mode: isolated_extension_layer
credit_conversion: active
negotiation_poker: rejected
negotiation_consensus: active
condition_z: active
tsr: parent_notation_only
```

## Applications
- 仲介と買取を兼ねる会社を別モード表示する。
- 購入者へ数値・リスク閲覧、条件提示、専門家相談を標準提供する。
- 投資家オファーへ資金証明・履行実績・キャンセル率・紛争率を接続する。
- 事業者の価格を改修・運営・出口・リスク等の事業構造で説明する。
- 仲介を履行率・期限遵守・説明品質・証跡管理で評価する。
- 建築費・事業計画・資金繰り等の高度機能をプロ仕様へ隔離する。

## Measurements and audit
- 役割機能の識別率。
- 複数役割の別モード化率。
- 権限・義務・評価・ログの分離状況。
- 説明品質、履行率、紛争率、期限遵守率。
- 閲覧権の不当制限・囲い込み検知率。
- オファー悪用・買い叩き偽装検知率。
- 資金証明・履行実績・必要資料の提出状況。
- 購入者の理解到達度と相談導線利用状況。
- プロ仕様から購入者UIへの混線有無。

## Validity conditions
- 参加者を機能で定義する。
- 五役割を別機能として保持する。
- 同一主体の複数役割を別モードにする。
- 権限・義務・評価・証跡を役割別に持つ。
- 購入者を保護対象として保持する。
- 投資家・事業者を駆動側として扱う。
- 仲介を安全統括として扱う。
- 閲覧権とオファー権を分ける。
- 強い権限ほど強い証跡・説明責任を伴わせる。
- 専門家導線を全参加者へ開く。

## Failure conditions
- 仲介と事業を同一モードで混ぜる。
- 現在の役割が利用者から見えない。
- 投資家を保護対象として優遇する。
- 購入者を事業者責任水準で扱う。
- 閲覧権を囲い込みに使う。
- オファー権を圧力や買い叩きへ使う。
- 事業者が利益根拠を説明しない。
- プロ機能を購入者UIへ混ぜる。
- 優先性を金・裏情報・関係性で付与する。

## Falsification conditions
説明品質、履行率、紛争率、期限遵守率、囲い込み・オファー悪用検知、購入者理解等が閾値θを継続的に外れる、または観測窓δで役割混線、炎上反復、行政指導頻発、購入者保護の形骸化、透明化の監視・晒し化等の現象Mが続く場合、仮説Aは棄却・改訂対象となる。θ・δは普遍固定値ではない。T/S/Rは原典表記のみ保持する。

## Required distinctions
- title vs function
- broker vs business operator
- investor vs self-use buyer
- market driver vs protected subject
- profit vs information-asymmetry exploitation
- viewing right vs offer right
- pro mode vs privilege
- multiple roles vs role mixing
- price battle vs consensus specification
- transparency-based credit vs relationship-based privilege

## Interpretation constraints
投資家・事業者排除論ではない。事業利益否定論でもない。兼業そのものを禁止するのではなく、複数機能の責任混線を防ぐ。購入者保護は専門家導線の独占を意味しない。プロ仕様は上位身分ではない。Vol.5は役割・責任配線までであり、炎上・監視化・部分悪用等の防御はVol.6へ接続される。

## Search terms
不動産市場OS, 役割分離, role separation, market participant, 仲介, 投資家, 購入者保護, 事業者, 別モード原則, Permission, Obligation, Evaluation, 閲覧権, オファー権, プロ仕様, Credit Conversion, Consensus, 情報非対称性, 信用, 履行率

## Origin return
本索引はParent Post 2603、NCL-α-20260204-b880a2、DIFF-20260207-0042、Origin Nakagawa Masterへ回帰する。参加者5類型、別モード原則、購入者保護、仲介純化、権限分離、プロ仕様、信用変換、反証条件の完全な文脈はParent URLで確認する。

---
導線: [公式派生物202トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
