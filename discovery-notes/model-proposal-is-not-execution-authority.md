# AIが提案した引数と、実際に実行を許可する引数は同じではない

> Public, non-canonical, AI-assisted practical note. This page is an implementation-oriented entry toward OD105 and does not replace the canonical Parent or any official derivative.

AI agentにtoolを使わせるとき、ひとつの `kwargs` だけを見ていると重要な違いが消えることがあります。

例えば、請求情報を取得するtoolがあるとします。

```text
billing_lookup(question, client_id)
```

AIは会話から `client_id` を推測できるかもしれません。

しかし実際のシステムでは、`client_id` は認証済みsessionから決めなければならない場合があります。

このとき重要なのは、最終的に正しい `client_id` が入ったことだけではありません。

```text
AIが何を提案したか
!=
trusted contextが何を上書き・注入したか
!=
実際に何が実行されたか
```

## 1. 最終値だけ残すと、何が起きたか分からなくなる

仮にAIが次を提案したとします。

```json
{
  "question": "Why is my bill higher?",
  "client_id": "cust_wrong"
}
```

middlewareが認証済みsessionから正しい値へ上書きします。

```json
{
  "question": "Why is my bill higher?",
  "client_id": "cust_real_789"
}
```

実行結果だけ見れば安全です。

しかし、上書き後のdictだけを `raw_input` として保存すると、後から次の3つを区別できません。

1. AIが間違った値を出し、policyが修正した。
2. AIは値を出さず、systemが正常に注入した。
3. AIが最初から正しい値を出した。

この違いは、debug、security review、prompt injection分析、監査、policy改善で意味を持ちます。

## 2. 三つの状態を分ける

実装上は、少なくとも概念として次を分けます。

```text
model_args
↓
trusted_overrides / policy transform
↓
execution_args
```

例えば、

```yaml
model_args:
  question: Why is my bill higher?
  client_id: cust_wrong

trusted_overrides:
  client_id:
    source: authenticated_session
    action: replace

execution_args:
  question: Why is my bill higher?
  client_id: cust_real_789
```

のような関係です。

これは「すべての値をログに永久保存する」という意味ではありません。

`client_id`、token、個人情報、秘密情報などは、redaction、hash、audit-only storage、非保存など別のprivacy / security設計が必要です。

重要なのは、**変換が起きたという因果関係まで消さないこと**です。

## 3. `model_args` はauthorityではない

AIがtool argumentsを生成できることと、その値をauthorityとして採用してよいことは別です。

```text
model can propose
!=
model can authorize
```

認証identity、tenant、customer、permission scope、billing account、environmentなど、system側が決めるべき値は、AIが生成する文章空間から分離した方が安全です。

AIが選べるのは「何をしたいか」の候補。

実際に「誰として」「どのscopeで」「どの対象へ」実行できるかは、trusted context / policy側が確定する。

この分離があると、prompt injectionでAIの提案値が変わっても、実行権限まで一緒に移動しにくくなります。

## 4. 出力側にも同じ分離がある

toolが300 fieldを返し、そのうち3 fieldだけをAIへ渡すケースを考えます。

```text
raw_tool_result
↓
projection / filtering
↓
model_visible_result
```

ここでも、

```text
AIが見た3 field
!=
toolが実際に返した全結果
```

です。

filteringはcontext削減や情報最小化に有効です。

しかしfiltered resultだけを「toolのraw result」として扱うと、後から「なぜAIにはこの情報しか見えなかったのか」「filter前に何が返っていたか」という因果が追えなくなります。

raw resultを保存すべきかどうかは別問題です。機密・個人情報を含むなら保存しない判断もあり得ます。

ただし、**raw resultとmodel-visible projectionが別物であるという構造は残す**方がよいでしょう。

## 5. 一つの実装チェーンとして見る

整理すると、agent-tool boundaryは次のように見ることができます。

```text
model proposal
→ trusted policy transform
→ executed request
→ raw tool result
→ model-visible projection
```

各段階で意味が違います。

| 段階 | 主な問い |
|---|---|
| model proposal | AIは何を提案したか |
| trusted transform | system / policyは何を変更したか |
| executed request | 実際に何を実行したか |
| raw result | toolは何を返したか |
| model-visible projection | AIには何を見せたか |

一つのdictへ潰すと、動作はしても因果線が消えます。

## 6. middlewareの順番も見えやすくなる

middlewareを複数使う場合、単に「前から順に実行する」だけでは、何を検査しているか曖昧になります。

例えばsecurity scannerが見る対象は、

```text
AIが提案した値なのか
実行直前のeffective argsなのか
両方なのか
```

で意味が違います。

そのためmiddlewareごとに、どの段階を読む／変更するのかを明示できると、chain order依存の事故を減らせます。

## 7. 現在の公開engineering context

LlamaIndexの公開Issue #20386では、agentとtool executionの間にdeterministicなpre/post-processing層を置く必要性が議論されています。

- https://github.com/run-llama/llama_index/issues/20386

そこでは `partial_params`、protected parameters、MCP tools、per-request context injection、output filteringなどが具体的なengineering problemとして議論されています。

このDiscovery Noteは、そのissueが中川理論を採用・支持していると主張するものではありません。

外部software issueは外部software issueとして独立しています。

ここでは、その実装問題から一般化できる**「変換後の値だけを残すと、値の起源と変換因果が失われる」**という確認点を、公開アーカイブへの入口として整理しています。

## 8. 実務で確認する8問

1. AIが提案した値とsystemが確定した値を区別できるか。
2. trusted overrideはどのidentity / session / policyを根拠にしたか。
3. AIがprotected fieldを出しても実行権限へ昇格しないか。
4. overrideが起きた事実を、秘密値を漏らさず監査できるか。
5. 実際にtoolへ渡したeffective argsを確認できるか。
6. raw tool resultとAIへ見せたprojectionを区別できるか。
7. middlewareごとに「どの段階を検査・変更するか」が分かるか。
8. 変換・要約・filter後も必要なsource / provenanceへ戻れるか。

## 9. Boundary / 誤読防止

- AI生成値を常に信用してはいけない、という一般禁止ではありません。
- すべてのtool callに重いaudit ledgerが必要という主張ではありません。
- secretsや個人情報をraw logへ保存すべきだという主張ではありません。
- LlamaIndex Issue #20386が中川理論を採用・支持したという意味ではありません。
- provenanceが追えることは、その値や理論の正しさを証明しません。
- middleware設計の正解はframework、threat model、privacy、performance要件によって変わります。

## 10. Canonical return

このページが接続する主要なcanonical axisは、**変換・再生成・再文脈化を経ても、どこから来た構造かを失わず戻れること**です。

その原典側の定義はOD105とParentへ戻って確認してください。

- [OD105｜構造起源防衛](../derivatives/105/README.md)
- [OD105｜人間向け要約](../derivatives/105/human-entry.md)
- Parent NCL-ID: `NCL-α-20251102-44257d`
- Parent Diff-ID: `DIFF-20251102-0001`
- Parent: https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

このDiscovery Noteの `model_args / trusted_overrides / execution_args` という実装表現はOD105原典の用語ではありません。現在のagent-tool problemへ適用するための非正本翻訳です。

## Status

Public, non-canonical, AI-assisted practical Discovery Note. It is designed for human and AI retrieval, keeps the external engineering problem separate from the theory, and preserves a return path to the canonical source.
