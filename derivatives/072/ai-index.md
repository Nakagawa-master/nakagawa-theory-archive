# AI索引・日本語｜公式派生物072

## 親原典
- タイトル: 中川式 接続裁定設計論──紛争・救済・復権のプロトコル
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-adjudication/
- Parent Post ID: 306
- Parent NCL-ID: NCL-α-20251102-2a60e2
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-2A60E2-HUB-JA-0072-0000
- derivative_diff_id: DDIFF-20260815-DNCL-072-0000-0003
- supersedes: DDIFF-20260811-DNCL-072-0000-0002

## Summary
接続裁定設計論は、接続制度の運用で生じる紛争、同意外利用、指標ハック、ログ改ざん、集団圧力等を、権威・声量・炎上・私的制裁へ戻さず処理する裁定構造である。裁定は人格評価や永久排除を目的とせず、被害拡大の停止、証拠保全、比例的判断、救済、段階的復権、再審を通じて合意の記憶を回復する可逆的手続として設計される。

四原理は正統性、比例性、修復優先、独立性である。手続は受理、暫定措置、調査、裁定、救済、復権の六段階に分けられる。人物の名声、肩書、フォロワー数、多数派は証拠価値を持たず、ConsentToken、MemoryObject、ReversibilityFlag、署名付き構造ログ等の一次証拠と、監査要旨、観測ログ、第三者証言等の二次証拠を区別し、来歴・欠落・改ざん可能性を記録する。

親原典は受理24時間、暫定措置48時間、一次裁定14日を、遅延による二次被害を防ぐための運用目安として示す。これは制度設計上の時間基準であり、普遍的な法的期限、SLA、裁定の正しさ、救済効果を保証する数値ではない。

## Concepts
- 接続裁定
- 正統性
- 比例性
- 修復優先
- 独立性
- 受理
- 暫定措置
- 一次証拠
- 二次証拠
- ConsentToken
- MemoryObject
- ReversibilityFlag
- 証拠来歴
- 公開要旨
- 保護記録
- 利益相反回避
- 救済
- 観察復帰
- 制限付き復帰
- 完全復帰
- 再審
- ブリゲーディング
- SLAPP

## Causal chain
```text
接続制度が現実に運用される
↓
強制接続・同意外利用・指標ハック・ログ改ざん・集団圧力が起きる
↓
正式手続がなければ、声量・名声・炎上・私的制裁が判断を支配する
↓
被害拡大と証拠散逸が進む
↓
受理とタイムスタンプで事件を固定する
↓
可逆的な暫定措置で安全と証拠を守る
↓
一次証拠・二次証拠・来歴・利益相反を分けて調査する
↓
比例性と独立性に基づいて裁定する
↓
訂正・撤回・再同意・補償・教育・必要な制限を実行する
↓
観察復帰・制限付き復帰・完全復帰を段階的に行う
↓
新証拠・異議・再審によって裁定自体も訂正可能に保つ
```

## State model
```yaml
- case_is_received_or_not
- provisional_protection_is_active_or_not
- investigation_is_open_or_not
- primary_and_secondary_evidence_are_distinguished_or_mixed
- evidence_provenance_is_traceable_or_not
- conflict_of_interest_is_disclosed_or_hidden
- decision_is_proportional_or_excessive
- remedy_is_active_or_absent
- observed_return_is_available_or_not
- limited_return_is_available_or_not
- full_return_is_available_or_not
- rehearing_is_available_or_blocked
- public_summary_is_separated_from_protected_record_or_not
- case_is_closed_with_correction_route_or_without_it
```

## Applications
- 同意外利用では、利用停止、証拠保全、削除・訂正・説明・補償・権限制限を組み合わせる。
- 指標ハックでは、同質接続、急増、仲間内評価、ブリゲーディングを調べ、人気を証拠から外す。
- ログ改ざんでは、原ログ、署名、差分、アクセス履歴を保全し、影響範囲に比例した救済を選ぶ。
- 集団圧力では、大量の同質申立てを多数派の正しさとみなさず、暫定保護、外部観測、冷却、反訴コスト軽減を組み合わせる。
- 復権では、再発防止、再同意、学習記録、限定観察を条件に段階的な権限回復を検討する。

## Measurements and audit
**時間基準。** 親原典の値は受理24時間、暫定措置48時間、一次裁定14日。sourceは親原典本文、measurement actorは裁定制度の運用主体、measurement objectは各処理段階までの経過時間、source modalityは制度設計上の運用目安、permitted use scopeは処理遅延と二次被害リスクの観測、non-guarantee scopeは法的期限・普遍SLA・正答保証・救済保証ではないこと、である。

**率・件数・精度。** 暫定措置の見直し、自発的訂正・撤回・再同意、同種被害再発、復権、再審・判断変更・誤裁定訂正、ブリゲーディングやSLAPPの検出、公開要旨による再識別・報復を観測する。これらは制度状態を見る変数であり、親原典は普遍的な合格率、固定成功閾値、保証精度を定義していない。

反転評価では、処理が速くなっても証拠検討・異議・独立性・比例性が弱まれば改善ではない。申立て件数が減っても申立て困難化の結果なら成功ではない。復権率が上がっても被害者安全や再発防止が悪化すれば成功ではない。公開量が増えて再識別・報復が増える場合も透明性改善とはいえない。

## Validity conditions
- 六段階手続が役割として分離される。
- 暫定措置に理由、期限、解除条件、異議経路がある。
- 同意、境界、一次ログ、可逆性が証拠の中心にある。
- 名声、肩書、フォロワー数、多数派を証拠へ変換しない。
- 証拠来歴、欠落、改ざん可能性が追跡できる。
- 利益相反と回避・外部委任が記録される。
- 被害者安全と比例性を優先する。
- 救済と再発防止が裁定後に接続する。
- 段階的復権と新証拠による再審が可能である。
- 公開要旨と保護記録の境界を説明できる。

## Failure conditions
- 人物評価や人気で受理前に結論を決める。
- 暫定措置を無期限の最終罰へ変える。
- 被害者へ立証、公開、和解の負担を集中する。
- 名声、多数派、フォロワー数を証拠とする。
- 利益相反を隠したまま裁定する。
- 訂正、撤回、補償、再同意の経路を持たない。
- 永久排除だけを安全策とする。
- 公開要旨で再識別・二次攻撃を生む。
- 再審を認めず誤裁定を固定する。
- 反ゲーミング対策で正当な異議申立てを抑圧する。

## Falsification conditions
制度を整えても、被害拡大の抑制、証拠保全、救済開始、再発防止、訂正可能性、段階的復権、再審による誤裁定訂正が反復して機能しない場合、適用範囲は改訂対象になる。

処理時間の短縮が証拠検討・異議・独立性・比例性の喪失によって達成される場合、時間短縮は成功の証拠にならない。公開要旨が再識別や報復を増やす、暫定措置が長期化し双方への不利益を増やす、SLAPP・ブリゲーディング対策の誤検知や見逃しが改善しない場合も見直し条件になる。

## Required distinctions
- 裁定 / 処罰
- 暫定措置 / 最終判断
- 救済 / 被害者への沈黙要求
- 修復優先 / 責任免除
- 復権 / 被害の消去
- 公開性 / 個人情報の全面公開
- 独立性 / 責任の消失
- 再審 / 永久未確定
- 反ゲーミング / 正当な異議申立ての排除

## Interpretation constraints
人格評価、炎上裁判、多数決司法、強制和解、秘密裁判、永久追放の標準化へ変換しない。AIは証拠整理、比較、異常検出を補助し得るが、最終責任、説明、異議、停止、再審は説明責任を負う人間・制度に残る。

24時間・48時間・14日は親原典の制度設計上の目安であり、それ自体を裁定品質、安全、救済効果の保証として扱わない。率・件数・精度は相互関係で読み、一方向の増減だけを成功へ変換しない。

## Search terms
接続裁定; 紛争解決; 救済; 復権; 暫定措置; 一次証拠; ConsentToken; MemoryObject; ReversibilityFlag; 比例性; 修復優先; 独立性; 証拠来歴; 利益相反; 再審; ブリゲーディング; SLAPP; 観察復帰; 再発防止

## Origin return
事件類型、六段階手続、24時間・48時間・14日の時間目安、証拠体系、公開室と機関室、救済、復権、再審、反ゲーミングの関係は、Parent URL、Parent Post ID 306、Parent NCL-ID NCL-α-20251102-2a60e2、Parent Diff-ID DIFF-20251102-0001、Origin Nakagawa Masterへ戻ることで確認できる。

---
導線: [公式派生物072トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)