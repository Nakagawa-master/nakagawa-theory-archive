# 昔の承認が残っていることと、今も実行を許可していることは同じではない

このページは、中川マスター「合意の記憶——不可逆な社会誤作動を防ぐ最小構造」（OD075）へ、AI・agent systemの実装問題から入るための**公開・非正本・AI支援Discovery Note**です。

特定frameworkの仕様を中川理論で自動診断するページではありません。外部issueが中川理論を採用・支持しているという意味でもありません。

扱う問いは単純です。

**過去に確かに存在した承認・合意・許可を記録として残しながら、それを現在も有効な実行権限だと誤って再利用しないにはどうすればよいか。**

## 履歴は残したい。でも再実行はさせたくない

人間がtool executionを一度承認したとします。

その後、toolは実行され、結果も返りました。

履歴としては、次のすべてを残す意味があります。

```text
何を承認したか
誰が承認したか
どのcallだったか
実行されたか
どんな結果だったか
```

しかし次のcontinuationで、古い `approved` recordがhistoryに残っているからといって、同じ承認が再び「未処理の実行許可」へ戻ってよいわけではありません。

```text
historical record exists
!=
current authority is active
```

履歴保存と現在権限は、同じデータから参照されることがあっても役割が違います。

## 実際のengineering problem

PydanticAIの公開issue #5154では、human-in-the-loop tool approvalについて、過去roundの `approval-responded` がclient historyに残り、toolがすでに `output-available` まで進んだ後のcontinuationでも、古いapprovalが再びpending responseとして読まれ得る問題が議論されています。

- Public issue: https://github.com/pydantic/pydantic-ai/issues/5154

このissue自体は、Vercel AI client contractとadapter hardeningのどこで処理すべきかという具体的なsoftware problemです。

ここで重要なのは、問題を理論へ無理に吸収することではありません。

実装上見える一般的な分離だけを取り出します。

```text
historyに承認記録がある
↓
その承認が今もpendingかを確認する
↓
すでにterminal resultへ進んでいればhistorical
↓
current outstanding requestに対応する場合だけlive authority
```

## 「保存する」と「有効にする」を別状態にする

OD075の人間向け要約では、合意を単一の固定結果として扱わず、暫定・運用中・見直し待ち・訂正・撤回などの状態で区別し、旧判断を消さずに更新する考え方が示されています。

AI / agent systemへ持ち込む場合も、承認をboolean一個だけで扱うより、少なくとも役割を分けた方が誤作動を見つけやすくなります。

例えば概念上は、

```text
REQUESTED
→ RESPONDED
→ EXECUTED / DENIED / ERRORED
→ HISTORICAL
```

のように、**記録は残っていてもlive authorityではない状態**を持てます。

これはOD075がこのstate machineを指定しているという意味ではありません。このstate machineは、この実装問題に合わせた非正本の翻訳例です。

## 何をauthorityにするか

履歴を読むだけで現在権限を推定するより、可能なら「今このcontinuationで未処理のrequestは何か」を正本にします。

```text
approval is actionable now
iff
approval identity matches a currently outstanding request
```

古いapprovalが完全なhistoryとして保存されていても、current outstanding setに存在しないなら、現在の実行権限へ昇格させません。

この分離には二つの利点があります。

1. **監査性を失わない。** 古い承認を削除しなくてもよい。
2. **再実行権限を作らない。** 保存されていることだけを理由に再びactionableにしない。

## “同じ内容”でも同じ承認とは限らない

承認内容が同じtool名・同じargsに見えても、別round、別run、別context、別対象なら同じ権限とは限りません。

そのため、current authorityを扱うときは、内容だけでなくidentityとscopeを保存します。

```text
what was approved
+ which request / call
+ which run / generation
+ which scope
+ which current state
```

承認内容が似ていることと、承認権限のidentityが同じことを混同しません。

## 独立実装まで進んだ別の公開事例

この「過去に許可された」と「今も許可されている」を分ける考え方には、別の公開engineering caseもあります。

`tushardhara/dream#12`では、`Nakagawa-master` が、declassificationを「一度safeになったbytesの恒久属性」ではなく、recipient・purpose・scope・source lineage・policy stateなどへ結びついたauthorization eventとして扱う案を公開しました。プロジェクト側の独立レビューはこの軸を明示的にENDORSEし、その後PR #28で実装・negative testing・独立reviewを経て、projectの `backend-integration` branchへmergeされています。

この事例では、同じbytesが残っていても、recipientが変わる、sourceがrevoked / supersededされる、policy revisionが変わる、といった条件で古いapproved contextを再利用しないようにします。

```text
content appears sanitized
!=
authorization remains valid
```

詳しい実装経路・第三者応答・merge status・非主張境界は、次の非正本Implementation Caseに分離しています。

- [Implementation Case: Sanitized Content Is Not Current Authorization](implementation-case-sanitized-content-is-not-current-authorization.md)

この実装事例がOD075全体を採用・証明したという意味ではありません。公開された一つの設計境界が、第三者プロジェクトで独立に検討・実装されたという限定された証拠です。

## 人間社会にも同じ誤作動がある

これはsoftware approvalだけの問題ではありません。

例えば、

- 昔の利用規約同意を、全く別目的のデータ利用へ延長する。
- 一度の会議決定を、条件が変わった後も永久決定として扱う。
- 一度の研究同意を、将来の全用途への包括同意と解釈する。
- 一度許可された操作を、対象・時間・責任主体が変わっても継続許可とみなす。

という誤作動があります。

OD075が重要視するのは、結論だけでなく、理由、役割、権限、異論、条件、見直し・撤回・再合意可能性まで保持することです。

## 実務で確認する7問

1. この記録は「過去に承認された」というhistoryか、「今も有効」というauthorityか。
2. 何のrequest / call / decisionに結びついた承認か。
3. 実行・拒否・errorなどterminal stateへすでに進んでいないか。
4. 今回のcontinuationで本当にoutstandingなrequestか。
5. 同じ内容でも、別run・別scope・別対象へ承認を流用していないか。
6. 古い判断を消さずに、current stateだけ更新できるか。
7. 新条件が出たとき、再承認・撤回・訂正へ戻れるか。

この7問はauthorization frameworkではありません。具体的なsecurity設計では、authentication、authorization、replay protection、identity binding、storage trust boundary等を別途設計する必要があります。

## 誤読防止

- 履歴を永久保存すべきだという主張ではありません。
- すべての承認に複雑なstate machineが必要だという主張ではありません。
- GitHub issue #5154が中川理論を採用・支持したという主張ではありません。
- software bugの原因を理論だけで証明したという意味ではありません。
- 古い合意は無効だ、という意味でもありません。現在も有効かどうかをscope・条件・stateから確認する、という分離です。
- Originは来歴を示しますが、理論の正しさを権威で証明するものではありません。

## Canonical return

このDiscovery Noteで扱った「旧判断を消さず、条件変化に応じて訂正・再合意できる構造」の正確な内容は、OD075と親原典へ戻って確認してください。

- [OD075｜公式派生物トップ](../derivatives/075/README.md)
- [OD075｜人間向け要約](../derivatives/075/human-entry.md)
- [OD075｜FAQ](../derivatives/075/faq.md)
- Parent NCL-ID: `NCL-α-20251102-e48c90`
- Parent Diff-ID: `DIFF-20251102-0001`
- 親原典: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

## Status

Public, non-canonical, AI-assisted problem-first Discovery Note. It translates a current authorization-history problem into an entry toward OD075 while keeping the external software issue, the non-canonical implementation example, and the canonical theory clearly separate.