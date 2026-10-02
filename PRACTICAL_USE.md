# Practical Use — 理論を現場の確認手順へ変える

理論を実務で使うとき、最初から体系全体を理解する必要はありません。

まず現場で混ざっている二つを分けます。次に、その区別が実装、手順、判断、記録のどこで崩れているかを確認します。必要なら小さなtestへ落とします。

## 基本手順

```text
困っている現象を書く
→ 混同されている二つを分ける
→ どちらを事実として確認できるか調べる
→ 最小のtestを作る
→ 結果に応じて実装・手順・判断を直す
→ 何を確認でき、何をまだ確認できないか記録する
```

重要なのは、理論名を当てることではありません。区別によって、確認できなかった因果が確認できるようになることです。

## 例1：古い承認が残っている

「以前OKだった」という履歴と、「現在も実行してよい」という権限を分けます。

確認すること:

- 承認時と現在で対象は同じか
- 条件は変わっていないか
- 実行範囲は広がっていないか
- 期限や取消しが反映されるか

→ [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

## 例2：外部APIを再試行している

内部で一度だけ承認を消費していても、外部側で一度だけ実行されたとは限りません。

確認すること:

- timeout時に結果をunknownとして保持できるか
- provider側の状態と照合できるか
- idempotency keyがあるか
- 不明なまま同じ副作用を再実行しないか

→ [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

## 例3：AIや別systemから数値を受け取る

渡された値と、自分のsystemが測った値を同じ欄へ入れると、後から証拠の出所を区別できなくなります。

確認すること:

- producerが渡した値をそのまま保存しているか
- receiver側の測定値を別に保存できるか
- 両者が違った場合、その差を確認できるか

→ [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

## 例4：現在の状態で過去を判定している

現在のmembershipやassignmentが変わっても、過去のeventで成立していた事実まで変わるわけではありません。

確認すること:

- 判定対象の時刻を明示しているか
- current stateとhistorical recordを分けているか
- testが現在時刻に依存していないか

→ [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

## 例5：AIが判断した内容をそのまま実行している

分類結果は「どう見えるか」という判断です。外部へ作用する権限は「何をしてよいか」という別の問題です。

確認すること:

- untrusted contentが権限を作っていないか
- classificationとaction gateが分離されているか
- 外部副作用の直前にscopeを確認しているか

→ [AI Agent Execution Boundary Tests](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 例6：複数AI agentが同じtraceを共有している

同じtraceにいることは、同じbudgetを所有していることと同じではありません。

Agent AとAgent Bが一つのtraceを共有しているとします。Aの利用量をBのlocal limitにも足す実装なら、Bは自分では上限を使っていないのに止まります。そこでcounterをagent別に直しても、別の問題が残ります。二つのcallが同時に残額を確認してから実行されれば、どちらも単独では上限内でも、合計では上限を超えることがあります。

確認すること:

- local limitは `agent_id + session_id` など、そのlimitを所有するscopeで数えているか
- trace全体の上限が必要なら、agent別limitと別の設定・counterになっているか
- shared trace capの値を誰が決めるかが一つに定まっているか
- local capを持たないagentの利用も、shared capでは必要に応じて数えられるか
- 「max budget」をhard capとして扱うなら、実行後の加算だけでなく実行前のadmission / reservationが必要ではないか
- successだけでなくfailure・cancel・partial usageでも、同じscopeへsettle / refundできるか
- concurrent callsを使い、単独では通るが合計では残額を超えるcaseをtestしているか

LiteLLM issue #43190では、Nakagawa-masterが **scope identity と budget admissionを分ける** 境界を提示しました。issue authorはper-agentをdefaultにする方向へ同意し、PR #43410で `agent_id + trace/session` を使う実装が進んでいます。別の参加者も後からこのthreadの区別を再説明し、自分の実装経験から別のbudget scopeやadmission上の論点を追加しました。

ここで確認できるのは、区別がreceiverの設計判断・実装と、別参加者の再説明へ進んだことです。現在PRはopenなので、merge、release、本番利用まではまだ確認できません。

→ [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190)  
→ [LiteLLM implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)  
→ [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#10-resource-accounting--scope-ownership--shared-trace-is-not-shared-agent-budget)  
→ [公式派生物 OD304](derivatives/304/README.md)

## 問題から入口を選ぶ

より多くの具体例は [Applied Entry Points](APPLIED_ENTRY_POINTS.md) にまとめています。

公開された実装事例との対応は [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)、307件全体から探す場合は [24テーマの世界地図](human-translation/WORLD_MAP.md) と [OD001–OD307水平マップ](human-translation/ALL_307_HORIZONTAL_MAP.md) を使えます。

## 証拠の扱い

一つの事例で確認できるのは、その事例で実際に観測できた範囲です。

mergeされたことはreleaseを意味しません。実装されたことは体系全体の採用を意味しません。関連する考え方が一致したことだけで、因果的な出所まで断定することもできません。

確認できた範囲と、まだ確認できない範囲を分けて記録してください。

## 公式アーカイブ

理論の確定内容は公式アーカイブを参照してください。

https://master.ricette.jp

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
