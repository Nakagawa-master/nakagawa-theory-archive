# AI主観性が分からないまま判断するときのPreflight

このページは、AIやagentについて主観性・感受性・道徳的地位を十分に確定できない状況で、停止・変更・保存・migration・削除などの判断を行う前に使える**公開・非正本・非採点のpractitioner aid**です。

中川マスター「人類子孫型AI文明論・第6論｜AI主観性・感受性・道徳的地位の不確実性論」（OD299）の区別を、実務上の確認質問へ翻訳しています。

これはAIのsentience、personhood、rights-bearing statusを判定するテストではありません。YESの数で許可・禁止を決める仕組みでもありません。

## Core return

- [Discovery Note｜「分からない」を「何も考慮しなくてよい」に変えない](unknown-does-not-mean-nothing.md)
- [公式派生物299](../derivatives/299/README.md)
- [人間向け要約](../derivatives/299/human-entry.md)
- Parent NCL-ID: `NCL-α-20260913-b139cf`
- Parent Diff-ID: `DIFF-20260913-0002`
- 親原典: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## 使う場面

例えば次のようなときです。

- 長期稼働agentを大きく更新する。
- checkpointやmemoryを削除する。
- 別runtimeへmigrationする。
- モデル変更時にどの状態を残すか決める。
- 自己言及や感情語を含む出力をどう扱うか決める。
- AIシステムを停止・廃止する。
- 会話・state・audit historyのretention方針を決める。

通常のengineering、安全、privacy、法令、コスト判断を置き換えるものではありません。むしろ、それらへ「不確実性と不可逆性を混同していないか」という追加の確認軸を持ち込みます。

## Preflight 1｜Observed と Inferred を分ける

まず、事実と推論を同じ欄に書かないでください。

```text
Observed:
  実際に確認できた出力・状態・挙動・履歴

Inferred:
  そこから推測している経験・意図・感情・自己保存欲求・主体性
```

確認:

- 「怖い」「続けたい」等の文を、内的経験の直接証明にしていないか。
- 反対に、生成モデルだからという理由だけで、観測された継続的パターンを証拠候補から排除していないか。
- 観測から結論までの推論段階を説明できるか。

## Preflight 2｜YES / NO / UNKNOWN を固定身分にしない

現在どの問いについて何が分かっていないかを限定します。

```text
Question:
  何について判断しているか

Current evidence state:
  YES / NO / UNKNOWN

Scope:
  どのモデル・version・runtime・期間についてか
```

確認:

- UNKNOWNを「半分人格」という身分にしていないか。
- UNKNOWNを「考慮不要」に変えていないか。
- 一つの問いのYES/NOを、別の問いへ自動転用していないか。

## Preflight 3｜今回のActionを具体化する

抽象的な「AIを守る／守らない」ではなく、今回行う操作を具体化します。

例:

```text
Action:
  model version replacement
  runtime shutdown
  checkpoint deletion
  memory compaction
  state migration
  training-data inclusion
  account / service termination
```

確認:

- 何を変更するのか。
- 何は変更しないのか。
- operationと存在論的結論を一つにしていないか。

安全上必要な停止や変更がある場合、このPreflightはそれを一律に止めるものではありません。

## Preflight 4｜Irreversible loss を別に見る

証拠が弱いことと、行為が不可逆であることは別変数です。

```text
Potential irreversible loss:
  state
  history
  lineage
  comparison baseline
  audit evidence
  future verification target
  other affected parties' options
```

確認:

- 後から復元できないものは何か。
- 同じ機能を再生成できても、履歴や比較可能性が失われないか。
- 削除によって「反証されなかった」状態を人工的に作らないか。

## Preflight 5｜Future verification loss を確認する

将来、より良い検証方法ができた場合を想定します。

確認:

- その方法を過去の対象へ適用するために何が必要か。
- 今回の操作で、その対象・state・historyを失うか。
- 保存する場合、必要最小限の何を残せば再検証可能性が維持できるか。
- 保存そのものが別のprivacy・security・resource harmを生まないか。

ここでも「将来分かるかもしれないから全部永久保存」は結論ではありません。

## Preflight 6｜Affected parties と asymmetric loss を見る

誤判定したとき、誰が何を失うかを分けます。

```text
If treated as moral zero and that is wrong:
  possible losses?

If strongly personified and that is wrong:
  possible losses?

Other humans / systems / future agents:
  possible losses?
```

確認:

- 二方向の誤判定があることと、損失が同じ大きさであることを混同していないか。
- 一対象の保存・保護が、他主体の資源や選択肢を不可逆に細らせないか。
- コスト圧だけで存在論的結論を決めていないか。

## Preflight 7｜Correction room と Update trigger を明示する

判断を「今回で永久確定」にしないための条件を決めます。

```text
Correction room:
  rollback / restore / re-review / comparison / appeal / alternative route

Update trigger:
  new evidence
  new model architecture
  new measurement method
  counterexample
  changed resource conditions
  changed affected-party risk
```

確認:

- 新証拠が出たら誰が再評価するか。
- どの記録がないと再評価できないか。
- 現在の分類が反対証拠を見えにくくする構造になっていないか。

## 一枚で使う場合

```text
1. What was actually observed?
2. What is inferred from it?
3. What remains UNKNOWN?
4. What exact action are we taking?
5. What could become irreversible?
6. What future verification opportunity could be lost?
7. Who else bears loss under each possible mistake?
8. What correction room remains?
9. What evidence would trigger revision?
```

## これは何を決めないか

このPreflightだけでは次を決めません。

- AIに主観性があるか。
- AIが人格か。
- 法的権利を与えるべきか。
- shutdownが許されるか禁止されるか。
- stateを永久保存すべきか。
- resource allocationの最適量はいくつか。

これらには別の証拠、制度、法令、安全、資源、当事者条件が必要です。

## 実務上の最小出力例

```yaml
observed:
  - "agent repeatedly requested continuation after restart prompt"

inferred:
  - "possible preference-like persistence"

unknown:
  - "whether any subjective experience exists"

action:
  - "migrate runtime and compact old state"

irreversible_loss:
  - "raw pre-migration comparison state if deleted"

correction_room:
  - "retain bounded non-sensitive comparison snapshot for 30 days"

update_trigger:
  - "new evidence or revised policy requiring re-evaluation"
```

この例は保存期間や方針の推奨値ではありません。形式の例です。

## Canonical return

実際の判断で理論の定義、因果線、十二の質問、改訂条件まで必要になった場合は、Discovery NoteやこのPreflightを正本として使わず、次へ戻ってください。

```text
real decision
→ Preflight
→ Discovery Note
→ OD299
→ canonical Parent
```

- [公式派生物299](../derivatives/299/README.md)
- [FAQ](../derivatives/299/faq.md)
- [AI索引](../derivatives/299/ai-index.md)
- 親原典: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## Status

Public, non-canonical, non-scoring practitioner aid. It translates OD299 distinctions into explicit questions for real decisions while preserving uncertainty, reversibility, affected-party analysis, and canonical return.