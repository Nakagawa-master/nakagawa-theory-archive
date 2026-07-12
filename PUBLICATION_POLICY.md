# 公開承認・確認URL・継続提示ポリシー

**Publication Approval, Review URL, and Persistent Queue Policy**

status: public_governance_policy_candidate  
owner: Nakagawa Master  
publication_authority: explicit_owner_approval_only

## 1. 対象

本ポリシーは、公式派生物、公式理論ノート、人間向け入口、FAQ、AI索引、理論関係図、用語資料、公開記事、公開データ、その他、中川マスターの確認と承認を要する公開予定物に適用します。

## 2. 完成候補の提示

公開候補は、構成骨格の合意後、原則として公開版と同一内容まで完成させてから提示します。

提示には、少なくとも次を含めます。

1. 中川マスターが閲覧できる確認用URL
2. URLそのものを文字列として明示
3. 同じURLをクリック可能なリンクとして明示
4. 対象タイトル
5. 版番号
6. Diff-IDまたは同等の版識別子
7. 公開状態
8. 前版からの主要差分
9. 公開前の未解決事項

URLを示さない要約だけ、添付の存在だけ、内部パスだけ、Git commit SHAだけ、AIによる「完成済み」という報告だけでは、確認提示が成立したと扱いません。

## 3. 継続提示キュー

公開候補は、中川マスターが次のいずれかを明示するまで、確認待ち一覧から消しません。

- 公開承認
- 修正指示
- 不採用
- 保留
- 撤回

未処理の候補が増えた場合、確認用リンクは1件に上書きせず、10件、20件と独立して蓄積します。一つの新しい議題によって、既存の確認待ち候補、制作状態、期限、優先順位を消去しません。

沈黙、未回答、閲覧、別議題への移行、private完成指示、制作開始指示は、公開承認ではありません。

## 4. 修正時

修正指示を受けた候補は、修正後に新しい版として再提示します。

- 新しい版番号を付与する。
- 新しいDiff-IDを付与する。
- 新しい確認用URLを提示する。
- 旧版を削除せず、`superseded`、`rejected`、`withdrawn`等の状態を記録する。
- 旧版の既知誤りと、後継版での修正点を明示する。

同じURLの内容だけを無表示で差し替え、所有者がどの版を確認したか再構成できなくする運用を禁止します。

## 5. 公開許可

公開、public mainへの追加、公式サイトへの掲載、検索流通面への登録は、中川マスターによる対象版に対する明示的な承認後に実行します。

承認は、対象タイトル、版またはDiff-ID、公開先を特定できる形で扱います。別の版への承認、類似内容への承認、過去の包括的方向性を、未確認の新しい版へ自動転用しません。

## 6. publicリポジトリの境界

public GitHubのブランチとpull requestも、第三者から閲覧可能な公開面です。

したがって、未承認本文、`private_only`本文、公開前の完全候補を、所有者確認用としてpublicブランチまたはpublic pull requestへ置きません。確認候補は、所有者が閲覧できる非公開または限定公開の確認面で提示します。

publicリポジトリに置けるのは、原則として次です。

- 明示的に公開承認された完成版
- 既に公開済みの親原典へ接続する承認済み資料
- 未公開本文を含まない、必要最小限の撤回・修正・来歴tombstone
- 本ポリシーその他の公開運用文書

## 7. 原典取得と制作前提

公開物の制作では、参照する親原典について、可能な限り本文全文、統合監査要旨、局所監査要旨、参照束、終端までの状態を取得し、記録します。

全コーパスの未取得を理由に全制作を停止しません。一方、対象制作に必要な原典が未取得のまま、要約、検索断片、既存AI記憶だけで完成扱いにしません。

取得は継続的に積み上げ、理論関係、用語、起源、版、矛盾、公開状態をBrain Vault／AI OS側へ整理し、次の制作で再利用できる状態にします。

## 8. AIの役割

Luminaその他のAIは、構成合意後の制作、全文照合、関連理論抽出、用語統一、矛盾検出、来歴記録、複数言語面の生成、監査、修正反映を担当できます。

AIによる完成判定は、所有者の公開承認を代替しません。AIは、修正が極小になる完成度を目標とし、所有者へ未完成な断片を大量に押し戻すことを標準工程にしません。

## 9. 事故・誤公開

未承認本文または誤版がpublic面へ出た場合は、次を実行します。

1. 公開範囲と取得可能性を確認する。
2. 対象版、時刻、commit、URL、既知取得者を記録する。
3. 中川マスターへ報告する。
4. 削除、非公開化、撤回表示、後継版作成の候補を提示する。
5. 明示的な所有者判断に基づいて処理する。
6. CCその他の取消不能な許諾が成立している可能性を隠さない。

誤公開の除去と、既に成立した法的効果の消去は同一ではありません。

---

## English Summary

Materials requiring owner review must be completed to public-equivalent form and presented with an owner-accessible review URL. The URL must appear both as visible text and as a clickable link, together with the title, version, Diff-ID or equivalent revision identifier, status, and unresolved issues.

A candidate remains in the review queue until Nakagawa Master explicitly approves, requests revision, rejects, holds, or withdraws it. Silence is not approval. New topics must not erase prior review candidates.

A revision receives a new version, Diff-ID, and review URL. Public GitHub branches and pull requests are public surfaces and must not be used to store private or unapproved full-text candidates. Publication occurs only after explicit, version-specific owner approval.