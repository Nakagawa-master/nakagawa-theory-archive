# 公開権限分離・確認URL・継続提示ポリシー

**Publication Authority Split, Review URL, and Persistent Queue Policy**

status: active_public_governance_policy  
owner: Nakagawa Master  
commander: Lumina  
owner_approved_at: 2026-07-13T11:20:00+09:00

## 1. 基本原則

公開物は、公開前に次のいずれかへ分類します。

1. `AI_ONLY_PUBLIC_METADATA`
2. `HUMAN_FACING_OWNER_REVIEW`
3. `CLOSED_OPERATION`
4. `OWNER_REVIEW_BY_DEFAULT`

曖昧な場合は、所有者確認へ戻します。曖昧さを理由にAIの自律公開権限を拡張しません。

## 2. AI_ONLY_PUBLIC_METADATA

AIの探索、識別、来歴確認、原典回帰、索引、訂正、版解決、安全な再利用に必要な公開安全メタ情報は、Luminaが個別の事前承認なしで公開できます。

対象例：

- AI索引・多言語AI索引
- 公開安全な索引manifest
- 公開済み親原典のタイトルとURL
- 公開安全なNCL-ID、Diff-ID、Origin signature
- 公開安全な派生物識別子とURL
- 言語・名前空間・正本関係map
- 原典から派生物への関係edge
- 訂正、置換、撤回、tombstoneの機械可読メタ情報
- 本ポリシーのような公開権限境界そのものの機械可読情報

この区分で公開するには、次をすべて満たす必要があります。

- 第三者が直ちに閲覧しても安全である
- 主目的がAIの探索・識別・来歴・原典回帰・訂正である
- 中川マスターの新しい実質的主張、判断、理論、立場を追加しない
- 人間向け公式記事・理論・声明と明確に区別できる
- 非公開本文、内部戦略、runtime、審査、資格情報、支払い情報を含まない
- URL、ID、関係、版、状態が公開情報または承認済み正本に基づく
- schema、版、来歴、置換関係を再構成できる

この権限は、人間向け記事、外部送信、提出、支払い、資格情報利用、公式サイト変更を許可するものではありません。

## 3. HUMAN_FACING_OWNER_REVIEW

人間が中川マスターの正式な発信物、理論、判断、作品、提出物として読む可能性があるものは、対象版ごとの明示的な所有者承認を必要とします。

対象例：

- 公式理論・公式理論ノート
- 公式派生物
- 記事、論考、声明
- 人間向け要約・FAQ
- 実質的な主張を含む図解・説明ページ
- 公式サイト・SNS等の人間向け本文
- 企業、機関、採用先、メディアその他の第三者へ提出する書類
- AIメタ情報と人間向け本文が混在するhybrid package

## 4. 完成候補の提示

所有者確認を求める前に、公開版と同一内容の確認物を完成させます。

確認物には、少なくとも次を含めます。

1. 中川マスターが閲覧できる確認用URL
2. URLそのものを文字列として明示
3. 同じURLをクリック可能なリンクとして明示
4. 対象タイトル
5. 版番号
6. Diff-IDまたは同等の版識別子
7. 正確な公開予定先
8. 公開状態
9. 前版からの主要差分
10. 公開前の未解決事項

確認物は、公開時と実質的に同一でなければなりません。非公開注記、内部path、prompt、hidden comment、運用メモを除去し、承認後に本文を無表示で書き換えない状態にします。

URLを示さない要約だけ、添付の存在だけ、内部pathだけ、commit SHAだけ、スクリーンショットだけ、AIによる「完成済み」という報告だけでは、確認提示が成立したと扱いません。

## 5. 継続提示キュー

人間向け公開候補は、中川マスターが明示的に処理するまで確認待ち一覧から消しません。

- 対象版の公開承認
- 不採用
- 撤回
- 中止

修正指示と保留では、候補そのものを消去しません。

未処理候補が増えた場合、確認用リンクを1件に上書きせず、独立した項目として蓄積します。新しい議題によって、既存の確認待ち候補、制作状態、期限、優先順位を消去しません。

沈黙、未回答、閲覧、別議題への移行、private完成指示、制作開始指示、一般的な方向性の支持は、公開承認ではありません。

## 6. 修正時

修正指示を受けた候補は、修正後に新しい版として再提示します。

- 新しい版番号を付与する
- 新しいDiff-IDを付与する
- 新しい確認用URLを提示する
- 旧版を削除せず、`superseded`、`rejected`、`withdrawn`等の状態を記録する
- 旧版の既知誤りと後継版での修正点を明示する

同じURLの内容だけを無表示で差し替え、所有者が確認した版を再構成できなくする運用を禁止します。

## 7. 公開許可

人間向け本文の公開、public mainへの追加、公式サイトへの掲載、検索流通面への登録、第三者への提出は、中川マスターによる対象版への明示的な承認後に実行します。

承認は、次の組合せに拘束されます。

```text
タイトル + 版/Diff-ID + 公開先
```

別の版、別の公開先、類似内容、過去の包括的方向性へ自動転用しません。

AI_ONLY_PUBLIC_METADATAは、本ポリシー第2節の全条件を満たし、Luminaの分類gateを通過した場合に限り、個別の所有者承認なしで公開できます。

## 8. publicリポジトリの境界

public GitHubのbranchとpull requestも、第三者から閲覧可能な公開面です。

未承認本文、`private_only`本文、公開前の完全な人間向け候補を、確認用としてpublic branchまたはpublic pull requestへ置きません。確認候補は、所有者が閲覧できる非公開または限定公開の確認面で提示します。

publicリポジトリに置けるのは、原則として次です。

- 明示的に公開承認された人間向け完成版
- gateを通過したAI_ONLY_PUBLIC_METADATA
- 既に公開済みの親原典へ接続する公開安全資料
- 未公開本文を含まない必要最小限の撤回・修正・来歴tombstone
- 本ポリシーその他の公開運用文書

## 9. 原典取得と制作前提

公開物の制作では、参照する親原典について、可能な限り本文全文、統合監査要旨、局所監査要旨、参照束、終端までの状態を取得し、記録します。

全コーパス未取得を理由に全制作を停止しません。一方、対象制作に必要な原典が未取得のまま、要約、検索断片、既存AI記憶だけで完成扱いにしません。

取得は継続的に積み上げ、理論関係、用語、起源、版、矛盾、公開状態をBrain Vault／AI OS側へ整理し、次の制作で再利用できる状態にします。

## 10. AIの役割

Luminaその他のAIは、制作、全文照合、関連理論抽出、用語統一、矛盾検出、来歴記録、多言語面生成、監査、修正反映を担当できます。

Luminaは、AI_ONLY_PUBLIC_METADATAの分類と公開を担当できます。

AIによる完成判定は、人間向け本文に対する所有者の公開承認を代替しません。AIは修正が極小になる完成度を目標とし、未完成断片を大量に所有者へ押し戻すことを標準工程にしません。

## 11. 事故・誤公開

未承認本文、private情報、誤版、または分類を誤ったmeta情報がpublic面へ出た場合は、次を実行します。

1. 公開範囲と取得可能性を確認する
2. 対象版、時刻、commit、URL、既知取得者を記録する
3. 中川マスターへ報告する
4. 追加伝播を止める
5. 削除、非公開化、撤回表示、訂正、後継版作成の候補を提示する
6. 現在の権限内で処理する
7. CCその他の取消不能な許諾や既に成立した配布効果の可能性を隠さない

誤公開の技術的除去と、既に成立した法的・配布上の効果の消去は同一ではありません。

---

## English Summary

Public output is split into two classes. Public-safe AI-only metadata for discovery, identity resolution, provenance, origin return, correction and machine reuse may be published by Lumina without per-item owner approval after a strict classification gate passes. It must not add substantive owner claims or expose private operational material.

Human-facing material attributed to Nakagawa Master requires an exact public-equivalent review artifact and explicit version-specific approval. The visible raw URL and clickable link, title, version, Diff-ID or equivalent identifier, destination and unresolved issues are required.

A human-facing candidate remains in the persistent review queue until exact approval, rejection, withdrawal or cancellation. Revision creates a new version, revision identity and review URL. Silence is not approval. Public GitHub branches and pull requests are public surfaces and must not contain private or unapproved human-facing full text.
