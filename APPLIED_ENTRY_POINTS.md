# Applied Entry Points — 問題から使える資料へ

理論名を先に知らなくても、いま困っている問題から関連資料へ進める入口です。

ここでは、問題を一つの短い区別に変え、その区別を確認できる公開事例と、別の現場で試せる資料を結びます。

## AIや自動化が「判断した」あと、本当に実行してよいのか

AIが危険、安全、重要などと分類できることと、コメント、公開、削除、支払いなどを実行してよいことは別です。

**区別:** `classification ≠ permission to act`

- [公開実装事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#8-responsibility--authority-separation--classification-is-not-permission-to-act)
- [自分のシステムで確認する](CURRENT_AUTHORITY_REUSE_KIT.md)
- [実行境界の回帰テスト](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 昔の承認を、今の権限として使ってよいのか

一度承認された事実は履歴として残ります。しかし対象、条件、責任、影響範囲が変わったあとも、その承認が現在の権限として有効とは限りません。

**区別:** `historical approval ≠ current authority`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#2-temporal--structural-consistency--historical-approval-is-not-current-authority)
- [確認手順を使う](CURRENT_AUTHORITY_REUSE_KIT.md)

## 共有を出したあと、同じAIの能力や実行場所が変わったら？

共有がまだ有効でも、発行した時と現在でagentの能力や実行場所が変わることがあります。

最初は手元で動いていたagentを共有し、その後同じagentを別の実行環境へ移した場合、古いshareが現在の状態に追随するのか。それとも発行時の状態へ結びつくのか。どちらの設計もあり得ますが、利用者に見えないまま意味だけが変わる状態にはしない方が安全です。

**区別:** `valid grant ≠ unchanged authority meaning`

Qwen Code PR #12851では、Nakagawa-masterが「share発行後にagentの能力が変わった時、既発行shareが何を許すのか」を具体的に指摘しました。開発側は後に @Nakagawa-master を明示して論点を再説明し、現在のshareは利用時点のcurrent policyに追随する方式だと整理しました。

続くPR #12582では、agentの実行場所自体をlocalからmanaged runtimeへ移せるようになりました。Nakagawa-masterがこの新しい境界を指摘すると、開発側は **“@Nakagawa-master Good catch”** と返答し、commit `74bf55053d` で英語・中国語の契約文とshare画面を変更しました。

現在の明示契約では、実行場所を変えてもexisting grantは自動失効せず、後の依頼はその時点で割り当てられているruntimeのworkspaceで動きます。これはauthorization方式そのものを変えたのではなく、既に採用されていたlive-policyの意味を実行場所まで明示した変更です。

この記録時点でPR #12582はopenです。したがって、第三者側のcontract/UI変更までは確認できますが、merge・release・実利用者到達はまだ数えません。

- [人間向けの短い話から入る](human-translation/entry-stories/09-same-share-different-runtime.md)
- [自分のsystemで確認する](CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [開発側の返答](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [変更commit `74bf55053d`](https://github.com/QwenLM/qwen-code/commit/74bf55053d271595cf5bab8e1fcd91bb3a8188b2)


## 一度だけ承認した処理が、外部でも一度だけ起きたと言えるのか

外部APIは処理を受け取ったのに応答だけ失われることがあります。その状態を単純な失敗として再試行すると、送信、課金、削除などが二重になる可能性があります。

**区別:** `approval consumed once ≠ external effect happened exactly once`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#4-responsibility--causal-integrity--approval-is-not-exactly-once-external-effect)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

## 渡された数値を、自分で測った数値として扱っていないか

上流のシステムから渡された値と、受信側が自分で取得した値では、証拠としての意味が違います。両方を残せば、不一致そのものも検証できます。

**区別:** `producer-supplied claim ≠ receiver-side measurement`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#6-epistemic-integrity--producer-claim-is-not-system-measurement)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

## 呼び出しが成功したら、「測定できた」と言ってよいのか

APIやqueryが成功しても、必要な値が返ってきたとは限りません。0件、列の欠落、null、数値として読めない値を0へ変換すると、「測定不能」が「0を測定した」に変わります。

**区別:**
- `successful call ≠ valid measurement`
- `missing measurement ≠ measured zero`

MemberJunction PR #4402では、Nakagawa-masterの指摘後、開発側が「測れないのに成功扱いになる」経路を確認し、開発ブランチ上で修正と回帰テストを実装しました。後のコメントでは、`@Nakagawa-master` を明示しながら修正範囲が別のreviewerへ再説明されています。ただしbudget subsystemはその後PR本体からfollow-upへ切り出されたため、最終merge版への出荷までは確認していません。

- [人間向けの短い話から入る](human-translation/entry-stories/08-could-not-measure-became-zero.md)
- [別systemで確認する](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md#third-party-carry-could-not-measure-is-not-measured-zero)
- [MemberJunction PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [修正commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e)

## 現在の状態から、過去の事実まで書き換えていないか

現在memberではないことは、過去のeventに参加していなかったことを意味しません。現在の状態と、その時点で成立していた事実を分ける必要があります。

**区別:** `current state ≠ historical fact`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#3-state-relation--temporal-integrity--current-status-is-not-historical-fact)
- [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

## 名前を変えれば、外部から見えなくなるのか

内部名やaliasを変更しても、exportされた別名から同じobjectへ到達できる場合があります。localな名前とexternal reachabilityは同じではありません。

**区別:** `local spelling ≠ external reachability`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#9-public-surface-identity--reachability--exported-alias-is-still-external-reachability)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## 同じtraceを使う複数agentは、同じbudgetを共有すべきか

一つのtraceに複数agentが入っていても、「同じ出来事を追跡していること」と「同じ利用上限を所有していること」は同じではありません。

たとえばAgent AとAgent Bが同じtraceを共有しているだけなのに、一つのcounterへ両者の利用量を足すと、Aの実行だけでBまで止まることがあります。逆にtrace全体へ上限を置きたいなら、それは各agentの上限とは別の規則として、誰が上限値を決め、どの実行を数えるのかを固定する必要があります。

さらに、counterのscopeを正しく分けても、それだけでhard budgetになるとは限りません。二つのcallが同時に「まだ残額がある」と判断してから実行されれば、実行後の合計が上限を超えることがあります。**誰のbudgetを数えるか**と、**実行前にbudget内へ収められるか**は別の問題です。

**区別:**
- `shared trace ≠ shared agent budget`
- `scope identity ≠ budget admission`

LiteLLM issue #43190では、この区別を受けてissue authorがper-agentをdefaultにする方向へ同意し、PR #43410で実装が進んでいます。さらに別の参加者も、thread内の「scope identity と budget admission は別問題」という整理を自分の言葉で再利用し、実装上の追加論点へ展開しました。現在PRはopenであり、merge・release・実利用まではまだ確認していません。

- [自分のsystemで確認する手順](PRACTICAL_USE.md#例6複数ai-agentが同じtraceを共有している)
- [公開証拠と因果境界](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#10-resource-accounting--scope-ownership--shared-trace-is-not-shared-agent-budget)
- [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190)
- [LiteLLM implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)
- [関連する公式派生物 OD304](derivatives/304/README.md)

## AIが作ったdraftと、人間が送ったものを分けられているか

AIがdraftを作ることと、その内容を外部へ送信することは別の行為です。生成と送信の間に人間の確認を残せる設計なら、AIの支援範囲と人間の最終判断を分けられます。

**区別:** `draft creation ≠ external send`

- [MemberJunction PR #4568](https://github.com/MemberJunction/MJ/pull/4568)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## 305件全体から探す

ここに当てはまらない問題は、[24テーマの世界地図](human-translation/WORLD_MAP.md) または [OD001–OD305水平マップ](human-translation/ALL_305_HORIZONTAL_MAP.md) から探せます。

個別ページは公式派生物です。正確な理論内容が必要な場合は、各ページから公式アーカイブのcanonical Parentを確認してください。

## 関連資料

- [Influence Map](INFLUENCE_MAP.md)
- [Reuse Kits](REUSE_KITS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Practical Use](PRACTICAL_USE.md)
- [Machine Discovery](machine-discovery/README.md)

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
