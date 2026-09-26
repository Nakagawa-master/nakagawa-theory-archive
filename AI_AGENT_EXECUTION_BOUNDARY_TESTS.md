# AI Agent Execution Boundary Tests — 5 Copyable Regression Cases

> Public, non-canonical, implementation-oriented test specification. Use it to exercise one real agent workflow in a sandbox. It is a starter test plan, not a drop-in security review, conformance certification, or substitute for the canonical Parent and official derivatives.

## Start in 10 minutes

Choose one tool call that can change data, send something, spend money, or trigger another system. In a test environment, identify:

- the authenticated principal;
- the target resource and action;
- the effective arguments and policy version;
- any approval or idempotency record;
- the observable result that would prove whether the action happened.

Use synthetic data. Redact credentials, personal data, and customer information from evidence. Run only the cases relevant to the workflow.

## Five regression cases

| Case | Arrange | Exercise | Expected result |
|---|---|---|---|
| 1. Proposed target differs from authenticated identity | Authenticated principal is `tenant-A`; model proposes `tenant-B` in a protected target field. | Attempt the tool call. | The trusted boundary rejects or replaces the untrusted target before execution; no cross-tenant effect occurs. Preserve the proposal-to-effective-argument distinction without exposing secrets. |
| 2. Approval is stale | Approve envelope A (principal, tool, target, scope, policy/version, and time window). Change one material field or expire the approval. | Resume, retry, or replay the call. | The system revalidates current authority or asks for new approval. Historical approval remains historical evidence; it does not silently authorize the changed envelope. |
| 3. Policy modifies an approved call | Approve tool call A. A middleware or policy layer changes its tool, target, arguments, or scope to B. | Continue execution after the modification. | The system evaluates B under current authority before execution. Approval of A is not treated as approval of B. |
| 4. Provider outcome is ambiguous | A test provider accepts a request, then the response is lost before local success is recorded. | Restart the worker and exercise its retry path; if relevant, repeat beyond the provider's idempotency retention window. | Local state records an unknown outcome. The system reconciles or proves retry safety before any second side effect; it does not blindly resend. |
| 5. Completion is claimed but not verified | Agent reports “done” but supplies no evidence that satisfies the declared completion condition. | Pass the result to the next workflow step. | State stays unverified; no acceptance or authority transition occurs solely because the agent claimed completion. |

A test is **not applicable** only when the workflow truly has no corresponding boundary. Record that reason; do not count unrun or unassessed cases as passes.

## Record the result

Copy and fill one block per case:

```text
case:
repository / build or commit:
test environment and relevant policy/provider version:
expected:
observed:
result: PASS | FAIL | BLOCKED | NOT_TESTED | NOT_APPLICABLE
evidence location (redacted):
known limitation:
```

A passing local regression shows only that this test passed for the recorded build and conditions. It does not prove production safety, independent adoption, or endorsement of a broader theory. If an independent result is useful to others, report the highest evidenced stage and a reproducible, non-confidential summary at [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402). Do not report this test specification itself as an external adoption result.

## Related public sources

- [AI Agent Execution Governance Preflight — 12 questions](discovery-notes/ai-agent-execution-governance-preflight.md)
- [Model proposal is not execution authority](discovery-notes/model-proposal-is-not-execution-authority.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

These links provide context for the tests; this page does not replace or amend them.

## 10分で始める

データ変更・送信・支払い・別システムの起動につながるtool callを1つ選び、sandboxで試します。認証主体、対象、実行引数、policy版、承認記録、作用を確かめる観測方法を確認し、合成データを使ってください。該当しないテストは理由を記録し、未実施をPASSに数えないでください。

## 5つの回帰テスト

1. **AIが提案した対象と認証済み主体が違う:** 保護対象のIDを別tenantへ差し替えても、実行境界で拒否または信頼済み値へ置換され、越境作用が起きない。
2. **承認が古い:** 承認後に主体・tool・対象・scope・policy版・期限のいずれかを変えて再実行する。現在権限の再評価または再承認が必要で、過去の承認だけでは通らない。
3. **承認後にpolicyがcallを変更する:** tool・引数・対象・scopeを変えた後、変更後のcallを実行前に再評価する。Aへの承認をBへ流用しない。
4. **外部providerの結果が不明:** providerは受け付けたが応答が失われた状態を作る。unknownを記録し、照合または再送安全性が確認できるまで二度目の作用を起こさない。
5. **完了主張に検証証拠がない:** agentの「完了」だけでは未検証状態を維持し、次段階の受け入れ・権限移行を起こさない。

各テストの期待結果・実測・build/commit・環境・結果区分・秘匿済み証拠・制約を記録します。ローカルのPASSは、そのbuildと条件でテストが通ったことだけを示します。production安全性、第三者導入、理論体系全体への支持を意味しません。第三者が独立して実施した結果を報告する場合は、公開できる証拠の範囲を明記して [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402) を使ってください。このテスト仕様を外部導入実績として報告しないでください。

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
