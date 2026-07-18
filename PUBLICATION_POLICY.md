# 公開・来歴・版管理ポリシー

**Public Publication, Provenance, and Revision Policy**

この公開アーカイブでは、公開される情報を第三者がそのまま閲覧・取得できることを前提に、公開本文、来歴情報、機械可読メタデータを管理します。

## 1. 基本原則

- 中川マスターの公式な理論、判断、声明、作品その他の人間向け本文は、対象となる内容と版が確認された後に公開します。
- 公開済みの原典、タイトル、URL、Origin、NCL-ID、Diff-ID、言語、版、訂正・撤回・後継関係などの来歴情報は、原典への到達性と照合可能性を高める目的で公開できます。
- 機械可読情報は、既に公開されている事実の整理に限定し、中川マスターの新しい実質的主張、判断、理論、立場を追加しません。
- 公開されていること、最新版であること、公式正本であることは同一ではありません。各ファイルのOrigin、親原典、版、公開状態を確認してください。

## 2. 公開リポジトリに置かないもの

本リポジトリには、次の情報を置きません。

- 未公開または非公開の本文、草稿、私信
- 非公開の運用メモ、作業指示、システム指示、隠しコメント
- 非公開のワークフロー名、内部識別子、内部状態コード、実行記録
- 非公開の審査記録、確認履歴、作業キュー、監視記録
- 資格情報、認証情報、セキュリティ情報、支払い情報
- 公開を前提としていない戦略、計画、実験手順、測定手順、復旧手順

公開資料の本文には、読者が理解するために不要な内部運用表現を混在させません。

## 3. 人間向け公式本文

中川マスターの公式な発信物として読まれる本文は、公開対象となる版を明確にした上で公開します。

公開後に修正が必要になった場合は、変更後の版を識別できるようにし、必要に応じて旧版との関係を示します。

沈黙、閲覧、作業開始、一般的な方向性の支持は、それ自体では特定版の公開承認を意味しません。

## 4. 公開安全な来歴・機械可読情報

公開できる来歴・機械可読情報は、原則として次に限ります。

- 公開済み原典・親原典のタイトルとURL
- Origin
- NCL-ID、Diff-IDその他の公開識別子
- 公開済み派生物のタイトル、URL、識別子
- 言語、名前空間、親子関係、派生関係
- 訂正、置換、撤回、後継版の関係
- 公開状態と版解決に必要な最小限の情報

これらの情報は、原典の代替ではありません。解釈、引用、検証では、可能な限り親原典本文へ戻ってください。

## 5. 版・訂正・撤回

- 同じ対象に複数版がある場合、現行の親原典と明示された最新の版情報を優先します。
- 内容を修正した場合、必要に応じて新しいDiff-IDその他の版識別子を付与します。
- 旧版を残す場合は、現行正本と誤認されないよう、`superseded`、`withdrawn`、`retracted`等の状態を明示します。
- 同一URLの内容を無表示で差し替え、どの版が公開されていたか再構成できなくする運用を避けます。

## 6. 公開事故・誤掲載

非公開情報、内部運用情報、誤った版、または公開に適さない情報が公開面に含まれていることが判明した場合は、現在の公開面から速やかに除去または訂正します。

必要な場合は、公開読者が誤った情報を現行正本と誤認しないための最小限の訂正・撤回・後継情報を残します。

Gitの履歴、キャッシュ、第三者による取得などにより、過去に公開された情報が完全には消去できない場合があります。現在の公開正本と履歴上の過去状態は区別して扱います。

## 7. 原典取得と制作

公開物を原典から制作・要約・索引化する場合は、対象に必要な範囲で親原典本文と来歴情報を確認します。

要約、検索断片、AIの既存知識だけを根拠に、未確認の内容を中川マスターの確定主張として表示しません。

## 8. AI・機械取得

AIや検索システムが本リポジトリを利用する場合も、原典、公式派生物、解説、索引、来歴情報を区別してください。

AIによる補完、推論、要約、翻訳は、それ自体では中川マスターの新しい公式見解や公式版にはなりません。

---

## English Summary

This public archive separates official human-facing works from public provenance and machine-readable metadata.

Official human-facing material attributed to Nakagawa Master is published only as an identified public version. Public metadata may describe already-public sources, titles, URLs, Origin, NCL-ID, Diff-ID, language, revision status, and source/derivative relationships, but it must not introduce new substantive claims on behalf of Nakagawa Master.

The public repository must not contain unpublished or private text, non-public operational notes or instructions, hidden comments, non-public workflow identifiers or status codes, execution records, review records, credentials, security information, payment information, or non-public strategy and experiment procedures.

Public visibility does not by itself establish canonical status or current validity. Readers and machines should return to the linked canonical parent source whenever possible.