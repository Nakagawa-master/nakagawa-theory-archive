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



## 同意した記録が残っていれば、今もそのデータを使ってよいのか

人がある時点で同意した事実は、あとから消さずに履歴として残せます。しかし、その記録が残っていることと、現在も同じ目的・範囲でデータを保持・処理・利用してよいことは別です。撤回、期限、目的変更、契約変更などが起きれば、履歴は真実のままでも現在の利用可否は変わります。

**区別:** `historical consent event ≠ current eligibility to retain / process / use`

Replay #67では、Nakagawa Masterがこの境界を提示したあと、repository ownerがNakagawa Masterを起点として明示しながら、immutableなconsent eventとcurrent eligibility、withdrawal / deletion receipt、downstream gateを分ける方針として再記述しました。ここで確認できるのは、**相手側が境界を明示的に受け取り、protocol方針へ反映したこと**です。schema / code / tests、merge、release、実データ運用はまだ別段階です。

別systemで試すなら、過去のconsent eventを監査履歴として保持したまま、現在のretention / processing / use可否を目的・scope・期限・撤回状態から再評価できるかを確認します。履歴削除と現在権限の更新を同じ操作にしないことが要点です。

- [公開事例の状態と証拠境界](REAL_WORLD_IMPACT.md)
- [Nakagawa Masterの提案](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository ownerの明示的な受け取り](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [理論内容の正本｜合意の記憶](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)


## AIに「この処理は中止」と伝えたのに、次の依頼で中止済みの指示がまた混ざるのはなぜか

これは、人間の仕事予定が勝手に復活するという話ではありません。AIエージェントが過去の会話やtool実行履歴を、次のmodel入力へ組み直すときに起きる実装上の問題です。

中止済みの指示は、監査や履歴のために残してよい。しかし、次の無関係な依頼で「いま実行すべき指示」として再びmodelへ渡してはいけない。この二つは別です。

**区別:** `durable / audit history ≠ fresh-turn context ≠ current execution authority`

Qwen Codeでは、この境界が二つの別経路で確認されています。#13463はworkspace-agents / managed-host側、#13487はHosted Harnessのtool-profile側です。両方ともQwen側のtriageで別個のP2 bugとして受理され、#13487は第三者によるsource verificationでも、cancelled turnのactionable contentが後続のfresh turnへ入る経路が確認されました。

これは「Qwenが解決策を採用した」という意味ではありません。現在確認できるのは、**同じ問題境界が別々の実装経路で再現し、receiver側でも実バグとして扱われている**ところまでです。修正PR・merge・releaseはまだ別段階です。

別のAI agent systemで確認するなら、cancelled turn Aを履歴には残しつつ、無関係なfresh turn Bの通常contextにはAの命令やtool transcriptを戻さないことを確認します。Aを本当にやり直すなら、明示的なRetry / resubmitを新しい実行意思として扱います。

- [Section 20の回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#20-cancelled-history-is-not-fresh-execution-authority)
- [Qwen #13463](https://github.com/QwenLM/qwen-code/issues/13463)
- [Qwen #13487](https://github.com/QwenLM/qwen-code/issues/13487)
- [複数frameworkへの実装bridge](machine-discovery/current-authority-multi-framework-implementation-bridge-v1.json)
- [理論内容の正本｜合意の記憶](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)


## 親で承認したのに、子タスクでは「届いていない」「user cancelled」になるのはなぜか

人が親の会話で「この操作をしてよい」と明確に承認しても、その判断が委譲先のtaskへ届いたとは限りません。さらに、届いたとしても、そのtaskがその承認を今回のexact actionに使えるとは限りません。

この三つを一つの「permission problem」にまとめると、内部のhandoff失敗やreview拒否まで「ユーザーがキャンセルした」と誤って説明することがあります。

**区別:**
- `user authorized ≠ authorization handoff admitted ≠ executor can consume that authority`
- `executor needs fresh approval ≠ user can actually reach that exact approval request`
- `internal abort / transport failure / review rejection ≠ user cancellation`

OpenAI Codex #50769では、Nakagawa Masterがこの三層を分離して診断する契約を提示しました。その後、別の参加者が **“Using the distinctions in the comment above”** と明示し、自分の別incidentを `authority/provenance` 層として分類しています。これは限定された第三者reuseです。Codexによる実装・maintainer採用・広い人物認知までは意味しません。

さらに別の参加者 `seeton` も、同じprivate repositoryへの保存で多数の成功後に後続writeだけが承認reviewで止まる別incidentを報告しました。成功時と拒否時のpayloadが同一だったとは確認されていないため、ここから「判定がランダムだ」とは言えません。ただし、後の拒否時に **どの現在条件が変わったのか**──grantのscope/期限、destinationのidentity・visibility・ownership、action class、reviewの中断/拒否──を追跡できなければ、利用者は原因を区別できません。Nakagawa Masterはその差分を追えるdecision traceとA/B回帰へ落としました。これは二人目の現実事例によるproblem-class recurrenceであり、OpenAIの採用や人物Origin認知を意味しません。

その後、第三の参加者 `unwashedlugosi` が、iPhoneの親会話でexactな変更を明示承認したのに、Mac上の委譲taskではその承認がuntrusted扱いされ、しかもそのtask自体がiPhoneのtask一覧から見えず、親会話にもactionableなapproval controlやrequest IDが返らない別経路を報告しました。ここで追加される困りごとは、**承認の内容や来歴だけでなく、fresh approvalが必要なとき人間がそのexact requestへ実際に到達できるか**です。

人間から見ると、

```text
「Yes」と答えた
→ 子taskではその承認を使えない
→ もう一度承認が必要
→ しかしその承認画面・task自体に人間が到達できない
→ 正しい承認をしたくても完了できない
```

という詰まり方になります。

Nakagawa Masterはこのケースを、authorization provenanceとは別の **authorization reachability** として分離し、exact task/action/destinationに結びついた `approval_request_id` を、親会話やRemote UIなど人間が到達できるfirst-party surfaceへ返す回帰契約へ落としました。これは新しい問題面への提案であり、OpenAIが採用・実装したことはまだ意味しません。

- [二人目の独立incident](https://github.com/openai/codex/issues/50769#issuecomment-5996162016)
- [現在のauthority input差分を追うA/B回帰](https://github.com/openai/codex/issues/50769#issuecomment-5996528096)
- [第三の独立incident｜iPhone→Macで承認taskに到達できない](https://github.com/openai/codex/issues/50769#issuecomment-6008257866)
- [authorization reachability 回帰提案](https://github.com/openai/codex/issues/50769#issuecomment-6010928315)
- [関連するDot-created task visibility問題 #49848](https://github.com/openai/codex/issues/49848)

別systemで試す場合は、親でexact action Aを承認したあと、handoffを意図的に一度失敗させ、childに新しいadmitted turnがないことを確認します。その失敗を `user_cancelled` とせず、handoff/admission failureとして区別できるかを見ます。次にhandoffを成功させ、Aだけがscope内で実行可能か、materially differentなBではfresh authorityを要求するかを確認します。

さらに、child側でfresh approvalが必要になったとき、そのtaskを直接開けない人でも、親会話やRemote UIなど**実際に到達できる場所**へexact approval requestが戻るかを確認します。承認対象が見えない・taskが一覧に出ない・request IDが返らない状態を「ユーザーが承認しなかった」と扱わないことが要点です。

- [Section 18の回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#18-you-approved-it--but-the-delegated-task-still-says-user-cancelled)
- [OpenAI Codex #50769](https://github.com/openai/codex/issues/50769)
- [Nakagawa Masterの三層分離](https://github.com/openai/codex/issues/50769#issuecomment-5986370673)
- [第三者による明示的reuse](https://github.com/openai/codex/issues/50769#issuecomment-5987001957)
- [machine-readable challenge R](machine-discovery/independent-reuse-challenges-v1.json)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 共有を出したあと、同じAIの能力や実行場所が変わったら？

共有がまだ有効でも、発行した時と現在でagentの能力や実行場所が変わることがあります。

最初は手元で動いていたagentを共有し、その後同じagentを別の実行環境へ移した場合、古いshareが現在の状態に追随するのか。それとも発行時の状態へ結びつくのか。どちらの設計もあり得ますが、利用者に見えないまま意味だけが変わる状態にはしない方が安全です。

**区別:** `valid grant ≠ unchanged authority meaning`

Qwen Code PR #12851では、Nakagawa-masterが「share発行後にagentの能力が変わった時、既発行shareが何を許すのか」を具体的に指摘しました。開発側は後に @Nakagawa-master を明示して論点を再説明し、現在のshareは利用時点のcurrent policyに追随する方式だと整理しました。

続くPR #12582では、agentの実行場所自体をlocalからmanaged runtimeへ移せるようになりました。Nakagawa-masterがこの新しい境界を指摘すると、開発側は **“@Nakagawa-master Good catch”** と返答し、commit `74bf55053d` で英語・中国語の契約文とshare画面を変更しました。

現在の明示契約では、実行場所を変えてもexisting grantは自動失効せず、後の依頼はその時点で割り当てられているruntimeのworkspaceで動きます。これはauthorization方式そのものを変えたのではなく、既に採用されていたlive-policyの意味を実行場所まで明示した変更です。

PR #12582は2026-10-02にmergeされました。したがって、第三者側のcontract / UI / runtime変更が`main`まで到達したことは確認できます。ただし、mergeだけからreleaseへの収録、実利用者への到達、広い人物認知までは推定しません。

- [人間向けの短い話から入る](human-translation/entry-stories/09-same-share-different-runtime.md)
- [自分のsystemで確認する](CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [開発側の返答](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [変更commit `74bf55053d`](https://github.com/QwenLM/qwen-code/commit/74bf55053d271595cf5bab8e1fcd91bb3a8188b2)


## 改訂を始めた権限で、終了時の現在stateまで確定してよいのか

改訂やreleaseの開始時に正しいreceiptを持っていても、処理の途中でcurrent stateが別のversionへ変わることがあります。

**区別:** `authorized to begin revision ≠ authorized to finalize current state`

Agent Marketplace issue #322では、古いcheckoutが新しいexecution planを古いplan / contract revisionで上書きし、その後revision barrierが解除される状態が独立に報告されています。Issue自身はstale publicationの拒否とbarrier ownershipのbindingを提案しています。

追加で試せる防御は、`finish(E)` の時点でもcurrent published stateを読み直し、そのstateがepoch Eで確定してよいlineageに属している場合だけbarrierを解除することです。

この項目はAgent Marketplace側によるNakagawa Master理論の採用事例ではありません。公開された第三者問題を、別systemでも再利用できるcurrent-authority regressionへ変換した入口です。

- [一般向けの短い話](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md)
- [Current-Authority Reuse Kit — revision finalization](CURRENT_AUTHORITY_REUSE_KIT.md#15-a-revision-barrier-is-not-authority-to-release-whatever-state-is-current)
- [Agent Marketplace issue #322](https://github.com/agentrof/agent-marketplace/issues/322)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 前のAI修復が「結果不明」のまま残っただけで、次の修復まで永遠に止めてよいのか

CIや自動修復でAIに修正を任せていると、AI自体は動き始めたのに、その後のrunnerや記録処理だけが落ちて、最終結果だけ残らないことがあります。

人間から見ると、困るのはここです。

```text
古い版 H1 でAI修復Aが始まる
→ AIは実際に動いた
→ しかし「成功/失敗」の最終記録だけ失われる
→ その後、人間や別処理がH2へ進める
→ H2では別のCI失敗が発生する
→ systemは「昔のAが未解決だから」と新しい修復まで永久に止める
```

ここで分ける必要があるのは、

**昔の処理Aの結果が分からないこと**と、  
**Aがいまも実行中であること**と、  
**Aに現在の別問題まで止める権限が残っていること**

です。

**区別:**

```text
unknown historical outcome
!=
currently executing attempt
!=
authority to suppress future current work
```

安全側に倒すなら、Aとまったく同じH1・同じ失敗証拠を勝手に再実行しないのは合理的です。

しかし、Aの実行runがすでに終わっていて、現在のPR headや失敗証拠がH2へ変わっているなら、古い「結果不明」を歴史として残したまま、新しいH2の修復まで永久停止させない設計が必要です。

Proffera PR #937では、Nakagawa Masterがこの境界を指摘した後、receiver側の実装が前に進みました。古いmodel-launched attemptは、結果を勝手に「失敗」や「成功」と決めず `unknown` として残せるようになり、**同じ古いhead・同じ失敗証拠は引き続き抑止しつつ、headや失敗証拠が実質的に変わった新しい修復は再び入れる**回帰testが追加されています。

これで状態は「問題提案」から**receiver-owned code + regression test**へ進みました。PRはまだopenで、merge・release・実利用は未確認です。またreceiverから「Nakagawa Masterの指摘を採用した」という明示的なOrigin attributionは確認できていないため、exclusive causationやperson-Origin returnはclaimしません。

- [Proffera PR #937](https://github.com/ibboabdoli-ai/Proffera/pull/937)
- [Nakagawa Masterのpost-model orphan / current-authority指摘](https://github.com/ibboabdoli-ai/Proffera/pull/937#issuecomment-6011643787)
- [Section 21の再利用手順](CURRENT_AUTHORITY_REUSE_KIT.md#21-an-indeterminate-old-attempt-is-not-permanent-authority-to-block-new-work)

## 終了した仕事の遅い報告で、いま動いている別の仕事を止めてよいのか

遠隔のAIやworkerに仕事を任せると、管理側では時間切れや取消で「終了」と判断したあとに、古いworkerから結果や使用量が遅れて届くことがあります。

遅れて届いた事実そのものは、消す必要がありません。問題は、その数字を現在の実行予算へそのまま書き戻すことで、すでに終了した仕事が、いま動いている別の仕事を止める力まで持ってしまう場合です。

ここでは、**何が実際に起きたかを記録すること**と、**その記録に現在の仕事を動かす権限を持たせること**を分けます。

**区別:**
- `same lease / attempt lineage ≠ accepted-result proof`
- `late physical observation ≠ current control authority`

Qwen Code #13241では、取消や回復のあとに届いた古いHost結果を採用しないだけでなく、終了後の使用量が現在の実行budgetを書き換えない境界まで実装されました。receiver側は実daemon / HostとWeb Shellを使った確認を報告し、PR本文には、今回のno-post-terminal-budget-write実装が **@Nakagawa-masterの外部技術提案** に基づくことが明記されています。PRは2026-10-04にmergeされました。

ここで確認できるのは、第三者側の実装・test・receiver検証・人間review・source continuity・mergeまでです。これを含むrelease、独立した実利用、利用者規模、後日の自発的なOrigin再言及までは、まだ確認できていません。

- [一般向けの説明から入る](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md#終了した仕事の報告が別の仕事を止める)
- [別systemで試す回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#17-a-late-observation-can-still-control-current-work)
- [Qwen Code PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)
- [merge commit `35616f3b`](https://github.com/QwenLM/qwen-code/commit/35616f3b643f6d87cc00112d961a0fbb448aca00)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

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

## 309件全体から探す

ここに当てはまらない問題は、[24テーマの世界地図](human-translation/WORLD_MAP.md) または [OD001–OD309水平マップ](human-translation/ALL_309_HORIZONTAL_MAP.md) から探せます。

個別ページは公式派生物です。正確な理論内容が必要な場合は、各ページから公式アーカイブのcanonical Parentを確認してください。

## 関連資料

- [Influence Map](INFLUENCE_MAP.md)
- [Reuse Kits](REUSE_KITS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Practical Use](PRACTICAL_USE.md)
- [Machine Discovery](machine-discovery/README.md)

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
