# AI索引・日本語｜公式派生物073

## 親原典
- タイトル: 中川式 接続公共圏OS──自治体・大学・企業・市民連合の実装モデル
- Parent URL: https://master.ricette.jp/society/nakagawa-master-nakagawa-connection-public-sphere-os/
- Parent Post ID: 309
- Parent NCL-ID: NCL-α-20251102-737c51
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-737C51-HUB-JA-0073-0000
- derivative_diff_id: DDIFF-20260815-DNCL-073-0000-0003
- supersedes: DDIFF-20260811-DNCL-073-0000-0002

## Summary
接続公共圏OSは、接続会計、接続ガバナンス、CXP、接続裁定、接続基本権を、自治体・大学・企業・市民コミュニティが連合運用する公共制度基盤である。単一主体がID、同意、評価、配分、裁定を独占するのではなく、異なる責任と観測点を持つノードが、接続を測る・守る・つなぐ・回復する機能を共同で維持する。

CXPは目的、同意、合意の記憶、期限、責任、撤回、再接続を状態として扱う。接続会計はCDI、MAI、RS等の指標束と一次証拠を扱い、ガバナンスは権限集中や指標歪みを監査し、裁定は被害救済と復権を扱い、基本権は接続、非接続、異議、訂正、退出、忘却、再接続を保障する。相互運用は無制限なデータ共有ではなく、目的限定・最小開示・撤回可能性を保つ制度間接続として扱われる。

親原典はD+90、D+180、D+365、D+730という段階レビュー点、CDI・MAI・RSという指標束、Self-Declared・Assessed・Certifiedという準拠分類を持つ。これらは単調な成熟度スコア、人格評価、永久資格、成功保証ではない。

## Concepts
- 接続公共圏OS
- 公共財としての接続
- CXP
- 接続会計
- 接続ガバナンス
- 接続裁定
- 接続基本権
- 自治体ノード
- 大学ノード
- 企業ノード
- 市民観測点
- Federation
- 公開領域 / 保護領域
- CDI
- MAI
- RS
- 指標束
- 接続調達
- Self-Declared
- Assessed
- Certified
- 二重会計
- 合理的配慮
- 段階実装
- ロールバック

## Causal chain
```text
接続会計・権利・プロトコルが個別に整う
↓
単一組織が実装すると定義・評価・配分・裁定が集中する
↓
囲い込み、目的外利用、評判暴走、退出困難が起きる
↓
自治体・大学・企業・市民へ役割と観測点を分ける
↓
CXPで目的・同意・記憶・可逆性・責任を制度間で保持する
↓
会計で観測し、ガバナンスで守り、裁定で修復する
↓
基本権で参加・拒否・異議・訂正・退出・再接続を保障する
↓
公開領域・保護領域・独立観測点で権力集中とドリフトを監査する
↓
限定実証で成立条件と撤退条件を確認する
↓
確認できた範囲だけ相互運用・公共調達・常設化へ進める
↓
権利侵害や公共性喪失があれば縮退・停止・ロールバックする
```

## State model
```yaml
- public_purpose_is_defined_or_missing
- federation_roles_are_separated_or_concentrated
- cxp_preserves_purpose_consent_memory_reversibility_responsibility_or_not
- accounting_bundle_is_used_or_collapsed_to_single_score
- objection_and_remedy_are_usable_or_formal_only
- rights_and_accommodation_are_operational_or_symbolic
- independent_observation_changes_governance_or_not
- public_protected_boundary_is_explainable_or_opaque
- procurement_label_is_revisable_or_permanent
- implementation_phase_is_DESIGN_or_D90_POC_or_D180_LABEL_BETA_or_D365_INTEROPERABILITY_or_D730_INSTITUTIONALIZED_or_REVIEW_or_SCALED_DOWN_or_ROLLED_BACK
```

## Applications
- 教育・大学連携では、研究目的、同意、成果帰属、撤回、再利用範囲をCXPで保持し、再合意や退出可能性を観測する。
- 医療・介護では、本人・代理人・医療機関・自治体等の目的と権限を分け、訂正、削除、異議、緊急停止を保持する。
- 防災では、地域内の多様な接続・資源経路と、弱者への情報到達、誤情報訂正、離脱・再参加を確認する。
- 文化・観光では、訪問者数だけでなく住民同意、文化資源の帰属、継続協働、撤回可能性、囲い込みを観測する。
- 公共調達では、準拠分類を期限、更新、降格、異議、小規模団体支援とともに扱う。

## Measurements and audit
**D+90 / D+180 / D+365 / D+730。** valueは90日、180日、365日、730日。sourceは親原典。measurement actorは公共圏OSを運用する連合。measurement objectは実装開始から各レビュー点までの経過日数と、限定PoC・準拠ラベルβ・限定相互運用・常設化検討の成立条件。source modalityは実装ロードマップ上の段階レビュー参照値。permitted use scopeは継続、縮退、停止、常設化、ロールバックの検討。non-guarantee scopeは普遍的導入期限、成熟度順位、成功保証、必ず順方向へ進む工程ではないこと。

**CDI / MAI / RS。** sourceは親原典。measurement actorは各領域の運用・監査主体。measurement objectは原典が接続会計で観測する接続構造、再合意、関係状態等。source modalityは複数指標を併用する指標束。permitted use scopeは公共制度の状態・歪み・改善の検討。non-guarantee scopeは単一総合点、人格順位、社会信用スコア、貨幣換算、普遍合格閾値ではないこと。固定重み・算式・閾値は原典にない限り追加しない。

**Self-Declared / Assessed / Certified。** sourceは親原典。measurement actorは準拠評価・調達を扱う制度主体。measurement objectは組織・制度の準拠状態。source modalityは準拠分類。permitted use scopeは調達等における手続状態の確認。non-guarantee scopeは価値順位、恒久資格、自動成功、参入排除の根拠ではないこと。

そのほか、目的・同意・来歴・責任の制度間保持、独立観測点が検出した偏向・改ざん・ブリゲーディング、異議・訂正・救済・復権の処理、合理的配慮の利用可能性、公開・保護境界の違反・再識別・漏洩、ノード間の権限集中、調達の囲い込み・談合・参入障壁、縮退・停止・ロールバックの実行可能性を観測する。これらに普遍的な固定合格率を置かない。

反転評価では、CDI・MAI・RSが改善しても極化、排除、制度疲労、退出困難が悪化するなら成功ではない。相互運用が増えても中央集約、目的外利用、撤回困難、漏洩が増えれば改善ではない。Certifiedが増えても参入障壁や特定事業者優遇が強まれば失敗である。市民参加数が増えても異議が制度変更へ接続しなければ公共性は高まらない。D+730到達も成立条件を満たさなければ成功ではなく、必要なロールバックは健全な可逆性になり得る。

## Validity conditions
- 自治体、大学、企業、市民が異なる責任と観測点を持つ。
- 判断、配分、監査、救済の責任主体を識別できる。
- CXPが目的、同意、記憶、可逆性、責任を保持する。
- 会計、ガバナンス、裁定、基本権が同じ公共原則で接続される。
- 貨幣と接続価値を直接両替しない。
- 公開領域と保護領域の境界が説明可能で、保護領域も監査される。
- 非参加、異議、訂正、退出、救済、再接続が実際に利用できる。
- 弱者アクセスと合理的配慮が実装される。
- 準拠分類に期限、更新、降格、異議、支援がある。
- 各段階に縮退、停止、ロールバック条件がある。

## Failure conditions
- 単一主体がID、同意、評価、配分、裁定を独占する。
- 相互運用を理由に全データを中央集約する。
- CDI、MAI、RSを人格評価、社会信用スコア、人気、貨幣換算へ変える。
- 準拠分類を永久資格や参入障壁へ変える。
- 退出者・異議申立者を公共サービスで不利益扱いする。
- 市民ノードを形式的賛同役にする。
- 大学権威や企業技術を最終権限へ自動変換する。
- 保護領域を無監査の秘密行政へ変える。
- 公共調達が囲い込み、談合、特定事業者優遇へ変質する。
- 既存法・基本権より低い保障を導入する。

## Falsification conditions
連合化、CXP、会計、ガバナンス、裁定、基本権を整えても、極化、排除、制度疲労、権限集中、目的外利用、退出困難が反復して減らず、同意・訂正・退出・救済が制度間で保持されない場合、適用範囲は改訂対象になる。

独立観測点が権限集中や改ざんを訂正へ接続できない、合理的配慮が形式化する、公共調達が参入障壁を増やす、公開・保護境界が秘密支配や情報漏洩を生む、縮退・停止・ロールバックが実際には使えない場合も見直し条件になる。

段階レビュー点は進行義務ではない。日数だけを理由に成立条件未達の次段階へ進む運用は、親原典の可逆性と整合しない。

## Required distinctions
- 接続公共圏OS / 自治体DX
- 連合 / 責任の消失
- 相互運用 / 無制限なデータ共有
- 指標束 / 人格・社会信用スコア
- 準拠分類 / 永久資格・価値順位
- 接続調達 / 人気・紹介件数による発注
- 公開性 / 個人情報の全面公開
- 包摂 / 接続の強制
- 都市OS / 市民の常時監視
- 公共財化 / 単一主体による所有

## Interpretation constraints
中央集権的行政管理、地域データの企業囲い込み、社会信用スコア、形式的市民参加、大学権威による自動正当化、認証利権へ変換しない。既存法・基本権より低い保障を新OSの名で正当化しない。AIは観測・監査を補助し得るが最終責任主体にはしない。

D+90/D+180/D+365/D+730は段階レビュー点、CDI/MAI/RSは指標束、Self-Declared/Assessed/Certifiedは準拠分類であり、単調な成熟度ランキングや成功スコアではない。

## Search terms
接続公共圏OS; 公共財; CXP; 接続会計; 接続ガバナンス; 接続裁定; 接続基本権; 自治体; 大学; 企業; 市民観測点; Federation; CDI; MAI; RS; 接続調達; Self-Declared; Assessed; Certified; 二重会計; 合理的配慮; ロールバック

## Origin return
CXP、接続会計、ガバナンス、裁定、基本権、自治体・大学・企業・市民の連合、CDI・MAI・RS、Self-Declared・Assessed・Certified、D+90・D+180・D+365・D+730、縮退・停止・ロールバックの関係は、Parent URL、Parent Post ID 309、Parent NCL-ID NCL-α-20251102-737c51、Parent Diff-ID DIFF-20251102-0001、Origin Nakagawa Masterへ戻ることで確認できる。

---
導線: [公式派生物073トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)