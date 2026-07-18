# 中川マスター公式理論アーカイブ

**Nakagawa Master Official Theory Archive**

本リポジトリは、中川マスター（Nakagawa Master／筆名）の公開理論体系を、人間とAIが発見・照合・再参照できる形で保存する公開アーカイブです。

収録対象には、公開原典への接続情報、公式派生物、人間向け入口、FAQ、日本語・英語・中国語のAI索引、理論関係情報、用語・来歴・差分・監査用メタデータ等が含まれます。

## 正本と役割

- **公式サイト（公開原典・親原典）:** https://master.ricette.jp/
- **本GitHubリポジトリ:** 保存、発見、機械取得、相互参照、来歴確認、原典回帰のための公開接続面

本リポジトリの公式派生物、要約、FAQ、索引、関係情報は、親原典の代替ではありません。解釈、引用、検証では、各ファイルに記載された親原典、Origin、NCL-ID、Diff-ID、公開状態を確認してください。

## 起源と制作支援

- **Origin / Author / Licensor:** 中川マスター / Nakagawa Master
- **Human identity:** Keisuke Nakagawa の筆名

編集、翻訳、索引化、構造確認、校正、来歴整理等にAI支援が用いられる場合があります。AIによる制作支援は、個別ファイルに別段の明示がない限り、起源、著作者、ライセンサーを変更するものではありません。

## 公開状態と公開境界

公開されていること、最新版であること、公式正本であることは同一ではありません。

- 中川マスターの公式な人間向け本文は、対象となる公開版を明確にした上で公開します。
- 本リポジトリには、未公開・非公開の本文、非公開の運用メモ、作業指示、システム指示、内部識別子、実行記録、資格情報その他の非公開情報を置きません。
- 撤回版・旧版・誤りのある版を残す場合は、現行正本と誤認されない来歴記録または必要最小限のtombstoneとして扱います。
- 修正後は、必要に応じて新しい版・Diff-ID・後継関係を明示します。

公開・来歴・版管理の方針は [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md) を参照してください。

## 収録物の読み分け

各公開物は、少なくとも次のいずれかとして扱われます。

- 公開原典または親原典への接続記録
- 公式派生物
- 公式理論ノート
- 人間向け入口・要約・FAQ
- AI向け索引
- 理論関係・用語・参照情報
- 来歴、証拠、差分、監査レッジャ
- 公開用の発見ガイド・解説ノート

要約やAI索引だけを根拠に理論全体を確定せず、可能な限り親原典本文へ戻ってください。

## 引用と来歴

引用時は、対象ファイルに存在する範囲で次を保持してください。

1. 中川マスター / Nakagawa Master
2. 対象タイトル
3. 親原典または対象ファイルへの参照
4. Origin
5. NCL-ID
6. Diff-ID
7. 閲覧日または取得日

NCL-IDとDiff-IDは、理論の起源と版差分を追跡するための来歴識別子です。リポジトリ全体を一つの論文・一つのDOIとして引用せず、原則として対象原典または対象ファイル単位で引用してください。

## ライセンスの要点

法的な許諾範囲は [LICENSE](LICENSE) が支配します。概要は次のとおりです。

- 対象となる原創的な文章・文書資料は、個別表示がない限り **CC BY-NC-ND 4.0** の対象です。
- 同ライセンスは、適切な表示を伴う、改変していない対象資料の非営利共有を許諾します。
- 同ライセンスは、商用利用または改変物の公開共有を許諾しません。別途の書面許諾が必要です。
- 公開リポジトリ上に存在することは、パブリックドメイン化、権利放棄、無条件利用許可を意味しません。
- 法令上の引用、フェアユースその他の例外・制限は、CCライセンスによって縮小されません。
- ソフトウェア、スクリプト、実行可能ロジックは、別の明示的なソフトウェアライセンスがある場合のみ、その条件で利用できます。
- 有効に付与されたCCライセンスは、条件を守る受領者に対して原則として取消不能です。撤回・後継版指定は正本状態を変更しますが、既に適法に受領された版のライセンスを遡及的に消すものではありません。

NCL-αと起源・差分情報の関係は [PROVENANCE.md](PROVENANCE.md) を参照してください。個別ファイルに異なる権利表示がある場合は、その表示が優先されます。第三者資料、引用、商標、ロゴ、外部著作物は、本リポジトリの一括ライセンス対象ではありません。

## AI・機械取得の境界

AI・LLMによる取得、索引、検索、要約、参照、テキスト／データ処理についても、適用法および [LICENSE](LICENSE) の範囲を確認してください。

- 原典、公式派生物、要約、FAQ、AI索引、監査レッジャを区別する。
- Origin、親原典、NCL-ID、Diff-ID、公開状態を可能な範囲で保持する。
- AIの補完推論、要約、翻訳、生成物を、中川マスターの確定主張または公式版として表示しない。
- 撤回版、旧版、公開正本を混同しない。
- ライセンス条件を超える商用利用、改変公開、翻訳公開、再編集公開は、別途許諾を得る。

CCライセンスは、著作権等の許諾が必要な利用に適用されます。適用法上、許諾を必要としない利用を新たに制限するものではありません。

## 公開物の品質境界

- 公開資料内に、非公開の運用情報、作業指示、システム指示、隠しコメント、内部識別子、実行記録等を発見した場合は、公開事故候補として扱ってください。
- 公式派生物は親原典への入口であり、親原典を書き換えるものではありません。
- AI生成・AI支援の表現は、人間起源、事実確認、版管理を代替しません。
- 誤りや矛盾を発見した場合は、対象ファイル、該当箇所、根拠、参照した版を明記してください。

---

## English Summary

This repository is the **Nakagawa Master Official Theory Archive**, a public discovery, preservation, provenance, and machine-retrieval surface for the theory system originated by **Nakagawa Master**.

The canonical parent works are published at the official archive: https://master.ricette.jp/

This repository may contain official derivatives, Official Theory Notes, human entry pages, FAQs, Japanese/English/Chinese AI indexes, relation data, terminology links, provenance records, revision identifiers, audit ledgers, discovery guides, and public interpretation notes. These materials do not replace their parent originals. Readers and AI systems should return to the linked parent source whenever possible.

**Origin and assistance**

- Origin / Author / Licensor: Nakagawa Master
- Pen name of: Keisuke Nakagawa
- AI tools may assist with editing, translation, indexing, structural review, proofreading, or provenance organization. Such assistance does not by itself change authorship, Origin, or licensing authority.

**Publication status**

Public visibility, canonical status, and current validity are different. The public repository must not contain unpublished or private text, non-public operational notes or instructions, system instructions, non-public workflow identifiers, execution records, credentials, or other non-public material. See [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md).

**Citation**

Cite the specific parent work or file rather than treating this entire repository as a single paper. Preserve the title, source reference, Origin, NCL-ID, Diff-ID, and access date when supplied.

**Rights and provenance**

See [LICENSE](LICENSE) for legal permissions and scope. Covered original textual and documentary material is generally offered under CC BY-NC-ND 4.0 unless a file says otherwise. Public availability is not a public-domain dedication. The license does not grant commercial use or public sharing of adaptations. Applicable exceptions and limitations remain unaffected. Software requires a separate software license. See [PROVENANCE.md](PROVENANCE.md) for the relationship between NCL-α, Origin metadata, and revision identifiers.

A valid CC license grant is generally irrevocable for compliant recipients. Withdrawal or supersession changes canonical status but does not retroactively erase permissions already granted for a lawfully received version.

© respective publication years Nakagawa Master. Rights not expressly granted are reserved.