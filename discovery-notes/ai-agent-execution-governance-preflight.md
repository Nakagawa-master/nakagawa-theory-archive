# AI Agent Execution Governance Preflight｜実行前に確認する12問

> Public, non-canonical, AI-assisted practical note. AI agent が tool / MCP / external action を実行する前の実務チェックです。これは公式派生物やcanonical Parentを置き換えません。

AI agentの事故は、モデルが「間違ったことを言う」場合だけに起きるわけではありません。

実際の実行系では、次のような境界が崩れたときにも問題が起きます。

```text
AIが提案した値
≠ systemが実行を許可した値

過去に承認された
≠ 現在も実行してよい

証拠が添付されている
≠ 証拠が主張を検証している

違反が記録されていない
≠ 必要な評価が完了している

要約されたゴール
≠ 元のauthorityを持つゴール
```

以下は、こうした混同を実行前に発見するためのpreflightです。

---

## 1. その値は「AIが提案できる値」か、「systemだけが確定すべき値」か

確認する対象の例：

- user / tenant / customer identity
- permission scope
- billing account
- environment
- tool capability
- resource ID

```text
model can propose
!=
model can authorize
```

AIがargumentを生成できるからといって、その値をそのまま実行authorityとして扱う必要はありません。

**確認:** protected fieldがmodel-visible textから勝手にauthorityへ昇格しないか。

---

## 2. model proposal と effective execution args を区別できるか

最低限、概念として次を分けます。

```text
model_args
→ trusted policy / context transform
→ execution_args
```

例えばAIが誤った `client_id` を提案し、authenticated sessionが正しい値へ上書きした場合、最終値だけを残すと「何が修正されたか」が分からなくなります。

**確認:** 提案・上書き・実行の因果を、秘密情報を漏らさず追えるか。

---

## 3. 承認recordとcurrent execution authorityを分けているか

```text
historically approved
!=
currently authorized
```

approvalが存在した事実は、その後も永続的に実行権限が残ることを意味しません。

変化し得るもの：

- principal
- tool / capability scope
- args
- policy revision
- resource state
- time window
- session / workflow context

**確認:** resume / retry / replay時に、古いapprovalを現在のauthorityとして再利用していないか。

---

## 4. MODIFY後のcallを再評価しているか

policyがtool callを変更した場合、変更前の承認が変更後のcallを自動的に承認するとは限りません。

```text
approved envelope A
→ MODIFY
→ envelope B

approval(A) != approval(B)
```

**確認:** tool、args、scope等が変わった場合、必要なauthority checkをBに対して行うか。

---

## 5. raw tool result と model-visible result を分けているか

```text
raw_tool_result
→ filtering / projection
→ model_visible_result
```

300 fieldのうち3 fieldだけをAIへ渡すこと自体は有効です。

しかし3 fieldのprojectionを「toolが返したraw result」と同一視すると、AIが何を見て判断したのかを後から説明しにくくなります。

**確認:** rawとprojectionの区別が実装上消えていないか。

---

## 6. 「agentが完了と言った」と「完了が検証された」を分けているか

```text
completion claim
→ evidence reference
→ verification
→ acceptance / next authority
```

例えば、

```text
agent: "tests passed"
```

というclaimがあり、test reportへのlinkがあるとしても、それだけでreportがclaimを支持しているとは限りません。

**確認:** claim、evidence、verification、authorized acceptanceを一つの`done=true`へ潰していないか。

---

## 7. 「違反0」と「評価済み」を混同していないか

compliance / governanceでは、少なくとも次を区別する必要があります。

```text
NOT_APPLICABLE
UNASSESSED
ASSESSED_PASS
ASSESSED_PARTIAL
ASSESSED_FAIL
ASSESSMENT_ERROR
```

```text
0 violations
```

が、

```text
必要なcontrolsをすべて評価し、すべて満たした
```

とは限りません。

**確認:** assessment coverage と outcome / pass rateが分離されているか。

---

## 8. handoff / checkpoint / restartで元の因果chainが切れないか

AI workflowでは、途中状態がserialization、checkpoint、resume、handoffを跨ぎます。

そのとき、

```text
request
→ approval / policy decision
→ execution
→ result
```

の一部だけが残ると、孤立したoutputや、根拠のないresumeが生まれます。

**確認:** callとresult、decisionとexecution、originating principalとdelegation chainが再接続できるか。

---

## 9. ゴールの意味だけでなくauthority-bearing fieldsを保持しているか

semantic similarityが高くても、運用上重要なfieldだけ消えることがあります。

例：

- deadlineだけ消える
- completion conditionだけ弱くなる
- constraintが一つ抜ける
- summaryがsource authorityとして扱われる

```text
semantic fidelity
!=
structural integrity
```

**確認:** required fieldが欠けたgoal recordを「ほぼ同じだから有効」と扱っていないか。

---

## 10. 変更は「解釈」か「正式なamendment」か

```text
source v1
→ explicit amendment
→ source v2 + diff + provenance
```

と、

```text
source
→ AI summary
```

は別です。

AI summaryやplanner interpretationが便利でも、それを元のauthorityへ昇格すると、条件・責任・期限などが静かに変わり得ます。

**確認:** interpretationがsourceを書き換えていないか。

---

## 11. fail-open / fail-closed / interrupt を対象ごとに決めているか

policy serviceが落ちたとき、すべて同じ挙動にする必要はありません。

例：

```text
read-only → fail-openを許容する場合がある
side-effecting → fail-closedが必要な場合がある
high-impact / ambiguous → human interruptが必要な場合がある
```

**確認:** availability failureが暗黙にauthorizationへ変換されていないか。

---

## 12. 後から「なぜ実行されたか」に戻れるか

最終的な問いは単純です。

> このactionは、誰の、どのauthorityで、どの情報・policy・approval・contextを通り、なぜこの形で実行されたのか。

これに戻れない場合、動作が成功していても、監査・修正・再発防止・責任分離は難しくなります。

**確認:** 結果からdecision、decisionからcontext、contextからsourceへ戻れるか。

---

# 5分版チェックリスト

```yaml
agent_execution_preflight:
  model_proposal_separated_from_authority: false
  proposed_and_effective_args_distinguished: false
  approval_freshness_checked: false
  modified_call_reauthorized_if_needed: false
  raw_and_model_visible_result_distinguished: false
  claim_evidence_verification_acceptance_separated: false
  assessment_coverage_separated_from_outcome: false
  handoff_checkpoint_causal_chain_preserved: false
  goal_structural_integrity_checked: false
  amendment_separated_from_interpretation: false
  failure_mode_explicit_per_action_class: false
  decision_to_source_return_path_available: false
```

`false`の数を単純な安全scoreとして使うための表ではありません。

重大度はaction、system、利用者、不可逆性によって変わります。ひとつでも重要境界が崩れていれば、その境界を先に確認します。

---

## Public engineering context

このpreflightの各論点は、現在のagent ecosystemで独立に現れている実装問題とも重なります。

例：

- LlamaIndex #20386 — deterministic tool I/O pre/post-processing
  - https://github.com/run-llama/llama_index/issues/20386
- Pydantic AI #5536 — durable / trusted approval context周辺の議論
  - https://github.com/pydantic/pydantic-ai/issues/5536
- OpenAI Agents Python #4827 / #4828 — approval resume とsession persistenceの整合
  - https://github.com/openai/openai-agents-python/issues/4827
  - https://github.com/openai/openai-agents-python/pull/4828

ここで挙げる外部projectが中川理論を採用・支持しているという意味ではありません。

独立したengineering problemと、このアーカイブの構造軸に重なる点があるため、実務上の比較対象として示しています。

---

## Canonical return｜理論へ戻る

このページは複数の実務問題をまとめた**非正本の運用preflight**です。単一の新しいcanonical theoryではありません。

特に関係する既存の軸は分けて確認してください。

### 起源・変換・return path

- [OD105｜構造起源防衛](../derivatives/105/README.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

OD105は、AIによる要約・翻訳・再文脈化でorigin / context / causal sourceが失われる問題と、原点へ戻れる構造を扱います。

### 合意・判断・見直し可能性

- [OD075｜合意の記憶](../derivatives/075/README.md)
- Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

OD075は、結論だけではなく前提・理由・異論・責任主体・見直し条件・撤回・再合意可能性を保持する軸を扱います。

このpreflightで使う `model_args`、`execution_args`、`coverage`、`verification_state`、`GoalRecord` 等は、OD075 / OD105のcanonical用語ではありません。現在のAI agent実装問題へ接続するための非正本翻訳です。

## Boundary

- これは万能なAI security standardではありません。
- 12項目すべてを全systemへ同じ重さで要求するものではありません。
- provenanceがあることは正しさを証明しません。
- auditabilityはauthorizationの代替ではありません。
- loggingを増やせば安全になる、という主張ではありません。
- secrets / personal data / confidential dataを保存することを推奨しません。
- 外部projectの掲載はadoption / endorsementの主張ではありません。

## Status

Public, non-canonical, AI-assisted practical Preflight. Human and AI readers may use it as an implementation checklist, while canonical interpretation returns to the linked OD075 / OD105 Parents.
