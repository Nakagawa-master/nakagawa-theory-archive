# Nakagawa Master Influence Map — 問題から関連資料を探す

このページは、具体的な問題から関連する理論、検証例、再利用資料を探すための案内です。

各項目では、混同しやすい概念を分け、公開されている事例と関連資料を示します。個別事例は、その事例で確認できる範囲を示すものであり、理論体系全体の妥当性や外部プロジェクトによる全面採用を意味しません。

## 1. 過去の承認は、現在の実行権限と同じか

過去に承認された処理でも、対象、条件、責任、影響範囲が変われば、現在も同じ権限が有効とは限りません。

```text
historical approval
≠
current authority
```

関連資料:
- [Applied Evidence Map — current authority](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#2-temporal--structural-consistency--historical-approval-is-not-current-authority)
- [Real-World Impact](REAL_WORLD_IMPACT.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

## 2. 分類結果は、外部へ作用する権限と同じか

分類器やAIが危険・安全・重要などと判定することと、送信、公開、削除、支払いなどを実行する権限は別です。

```text
classification
≠
permission to act
```

関連資料:
- [Applied Evidence Map — classification is not permission](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#8-responsibility--authority-separation--classification-is-not-permission-to-act)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

## 3. 一度の承認は、外部処理が一度だけ起きたことを保証するか

通信断やtimeoutがあると、内部で承認を一度だけ処理していても、外部APIの結果が確定しているとは限りません。再試行によって送信、課金、削除などが重複する場合があります。

```text
approval consumed once
≠
external effect happened exactly once
```

Clientverseでは、unknown outcome、reconciliation、idempotency protectionに関する変更が実装されました。

関連資料:
- [Applied Evidence Map — external side effect](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#4-responsibility--causal-integrity--approval-is-not-exactly-once-external-effect)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

## 4. 渡された数値は、そのシステム自身が測定した値と同じか

上流のproducerから渡された値と、受信側が自ら測定した値では、証拠としての意味が異なります。

```text
producer-supplied claim
≠
receiver-side measurement
```

PostHogでは、producer側の値とserver側で取得した値を分離して保存し、不一致を確認できる変更が行われました。

関連資料:
- [Applied Evidence Map — epistemic integrity](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#6-epistemic-integrity--producer-claim-is-not-system-measurement)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

## 5. 現在の状態は、過去の事実と同じか

現在memberではない、現在権限を持っていない、といった状態から、過去の参加や権限まで否定することはできません。

```text
current state
≠
historical fact
```

TourCRMでは、この区別に関連する実装とtestが修正され、関連PRがmergeされました。

関連資料:
- [Applied Evidence Map — historical fact](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#3-state-relation--temporal-integrity--current-status-is-not-historical-fact)
- [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

## 6. 名前やaliasが変われば、外部から到達できなくなるか

内部名やaliasを変更しても、別のexport経路などから同じobjectへ到達できる場合があります。

```text
local spelling / alias
≠
external reachability
```

MemberJunction #4487では、public symbolの収集方法、tests、実装が修正され、mergeされました。

関連資料:
- [Applied Evidence Map — public reachability](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#9-public-surface-identity--reachability--exported-alias-is-still-external-reachability)
- [MemberJunction #4610](https://github.com/MemberJunction/MJ/issues/4610)

## 7. 同じtraceを共有するagentは、同じbudgetを共有すべきか

LiteLLMでは、複数agentが同じtraceを共有する場合のsession limitについて議論と実装が進められています。

```text
shared trace
≠
shared agent budget
```

関連資料:
- [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190)
- [Implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)

## 8. draftの生成は、外部送信と同じか

MemberJunctionでは、agentがemail draftを生成する処理と、人間が最終的に送信する処理が分かれています。recipientの表示や、長文が途中で切れた場合のfallbackも扱われています。

```text
draft creation
≠
external send
```

関連資料:
- [MemberJunction PR #4568](https://github.com/MemberJunction/MJ/pull/4568)

## 9. 予測値は、強制可能な上限と同じか

Qwen Codeでは、batchのforecastと実際のtoken消費の差が問題となり、上限を安全に計算できないrequestの扱いやcleanup stateに関する変更が行われました。

```text
forecast
≠
enforceable bound
```

関連資料:
- [Qwen Code PR #12895](https://github.com/QwenLM/qwen-code/pull/12895)

## 10. 測れなかった値を、0として記録してよいか

問い合わせやqueryが成功しても、必要な値が欠けていれば測定成功ではありません。

```text
successful call
≠
valid measurement

missing measurement
≠
measured zero
```

MemberJunction #4402では、結果0件、列欠落、null、非数値を人工的な0へ変換していたbudget evaluatorについて、Nakagawa-masterのreview後にreceiverが問題を確認し、branch上でfail-closed修正と回帰テストを追加しました。後にreceiver側が別reviewerへ`@Nakagawa-master`を明示して修正範囲を再説明しています。

ただしbudget subsystemは最終merge前に別follow-upへ切り出されているため、ここで確認できるのはbranch実装・tests・receiver-side再説明までです。

関連資料:
- [人間向けの入口](human-translation/entry-stories/08-could-not-measure-became-zero.md)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md#third-party-carry-could-not-measure-is-not-measured-zero)
- [MemberJunction PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [receiver fix commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e)

## 関連する索引と資料

- [24のテーマから見る](human-translation/WORLD_MAP.md)
- [OD001–OD305を横断して見る](human-translation/ALL_305_HORIZONTAL_MAP.md)
- [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)
- [Reuse Kits](REUSE_KITS.md)
- [Machine Discovery](machine-discovery/README.md)
- [AI Agent Execution Boundary Tests](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 記載範囲

このページでは、公開情報から確認できる区別、事例、関連資料を案内しています。個別の実装例は、その範囲で確認できる事実を示します。

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
