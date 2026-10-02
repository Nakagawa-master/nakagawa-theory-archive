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

## 8. 下書きを作ることと、外へ送ることは同じか

MemberJunction PR #4568では、agentがemail draftを作る処理と、人間が最終的に送信する処理が分けられています。短いdraftは本人のmail clientを開き、長すぎるdraftは途中で切れた文章をそのまま送らせないfallbackへ回します。

```text
draft creation
≠
external send
```

このPRでは、もう一つ別の境界も実際の実装変更につながりました。

```text
送信する本人の確認画面で見せてよい宛先・件名
≠
Slack / Teams の共有会話にそのまま見せてよい宛先・件名
```

Explorer内では、送信前に宛先を見せることが誤送信を防ぐ確認材料になります。一方、SlackやTeamsの会話は、送信者本人より広い人が読めることがあります。そこでNakagawa-masterのreviewは、共有チャネルのfallbackへ宛先や件名を出すと、draftを送らない設計でも別の情報漏えい面を作り得ると指摘しました。

開発側はこの区別を認め、Slack / Teams fallbackからrecipientとsubjectを外し、機密性のある宛先・件名が共有面へ出ないことを回帰testで固定しました。この変更を含むPR #4568は2026-10-01にmergeされています。

同じ情報でも、**誰が見る面なのかが変われば、安全な表示範囲も変わる**。本人向け画面では確認可能性を高め、共有面では不要な情報を減らす。この二つは矛盾せず、表示先ごとに境界を分けることで両立できます。

ここで確認できるのはreviewへの応答、実装変更、test追加、mergeまでです。release後の利用規模や実userへの作用は、mergeした事実だけからは推定しません。

関連資料:
- [MemberJunction PR #4568](https://github.com/MemberJunction/MJ/pull/4568)
- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4568#pullrequestreview-5256077986)
- [開発側の修正説明](https://github.com/MemberJunction/MJ/pull/4568#issuecomment-5762411184)

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

MemberJunction #4402では、結果0件、列欠落、null、非数値を人工的な0へ変換していたbudget evaluatorについて、Nakagawa-masterのreview後に開発側が問題を確認し、開発ブランチ上で安全側に止める修正と回帰テストを追加しました。後に開発側が別reviewerへ`@Nakagawa-master`を明示して修正範囲を再説明しています。

ただしbudget subsystemは最終merge前に別follow-upへ切り出されているため、ここで確認できるのは開発ブランチ上の修正・tests・開発側の再説明までです。

関連資料:
- [人間向けの入口](human-translation/entry-stories/08-could-not-measure-became-zero.md)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md#third-party-carry-could-not-measure-is-not-measured-zero)
- [MemberJunction PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [修正commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e)

## 11. 共有が有効でも、あとで実行場所が変わったら同じ意味か

共有が期限内でも、同じagentの能力や実行場所が後から変われば、発行時と利用時で実際の作用範囲が変わることがあります。

```text
grant still valid
≠
authority meaning stayed unchanged
```

Qwen Code PR #12582では、Nakagawa-masterの指摘後、開発側が @Nakagawa-master へ返答し、既存shareがlocal↔managed runtimeの変更にもlive-policyで追随することをfrozen contractと英語・中国語のshare UIへ明記しました。

この記録時点ではPRはopenです。contract/UI変更までは確認できますが、merge・releaseまでは数えません。

関連資料:
- [一般向けの入口](human-translation/entry-stories/09-same-share-different-runtime.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [receiver response](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)

## 12. 改訂を始めた権限は、終了時の現在stateを確定する権限と同じか

長いrevisionの途中では、開始時に正しかった対象と、終了時に存在するstateがずれることがあります。

```text
authorized to begin revision
≠
authorized to finalize whatever state is current
```

Agent Marketplace issue #322では、古いcheckoutが新しいexecution planを古いplan / contract revisionで上書きし、その後revision barrierが解除される状態が独立に報告されています。

Issue自身のstale-publication対策に加えて、終了時にcurrent published lineageを再確認し、今回のrevisionが確定してよいstateだけをreleaseする回帰テストとして再利用できます。

これは第三者によるNakagawa Master理論の採用証拠ではありません。独立した公開問題を、current-authorityの再利用challengeへ接続したものです。

関連資料:
- [一般向けの入口](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md#15-a-revision-barrier-is-not-authority-to-release-whatever-state-is-current)
- [Agent Marketplace issue #322](https://github.com/agentrof/agent-marketplace/issues/322)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 13. 所有していなければ、重要な入口を握っていても実効的な力はないと言えるか

所有関係と、実際に何を実行できるかを左右する入口の構造は別です。所有していなくても、認証、計算、通信、data、移行、export、監査などの重要な入口を一方が変更でき、その変更で他方の実行可能な選択肢が狭まるなら、実効的な力は残り得ます。

一方で、入口が集中している、依存している、単一providerを使っている、という事実だけで支配や不正を認定することもできません。実際に使える独立代替、退出・移行、異議・訂正、権限の範囲と期間まで分けて確認します。

```text
non-ownership
≠
non-domination

nominal alternative
≠
viable independent alternative

export is available
≠
effective exit is already proven
```

Freenet issue #4381 は、この区別を別の文脈で検査できる独立した公開事例です。Issue自身が、public proxy は導入障壁を下げる一方、hosted peer が利用者のprivate delegate dataを扱う trusted centralized intermediary になると明記しています。その後、hosted proxyであることを利用者へ表示するUI、per-user isolation、node側のexport endpoint、browserからの実data exportが実装されました。

さらに重要なのは、その後の #4592 が「exportできる」だけでは実効的な退出として摩擦が大きいと明示した点です。nodeを止めてCLI importする必要があったため、#4603 ではrunning nodeへlive importする経路がmergeされ、#4724 では自分のpeer側で明示操作すると hosted側から一回限りのmigration dataをpullしてimportするmagic-link経路までmergeされています。#4724には mint → pull → import の統合試験もあります。

したがって、この事例では次の段階を分けて読めます。

```text
export exists
→ exit is technically possible
→ import can run on the receiving peer without stopping it
→ migration becomes a bounded user path
→ mint / pull / import is integration-tested
```

それでも、実際の利用者がhosted依存から自分のpeerへ移り、必要なstateを継続できたという実運用上の退出までを、この公開記録だけから自動的に認定することはしません。設計・実装・統合試験と、現実の利用者移行は別の証拠層です。

ここで再利用できる問いは、「exportボタンがあるか」だけではありません。

1. proxyが利用できなくなっても、dataを自分のpeerへ移し、必要なstateを継続できるか。
2. exportだけでなく、受け側のimport・認証・復旧まで普通の利用者が実行できるか。
3. export・authentication・migrationの入口を同じoperatorが止めた場合、利用者に実行可能な別経路が残るか。
4. 複数のproxy候補があっても、同じ上流の認証・保存・移行基盤へ依存していないか。
5. hosted modeの便利さが、不要になった後も恒久的なdependencyへ変わっていないか。
6. 改善後に、実際のswitching lossとoperator leverageが下がったか。

Freenetの実装はNakagawa Master理論の採用証拠ではありません。第三者が独立に扱っている公開問題と、その後に実装された退出経路へ、第13論のaccess-topology / effective-exitの検査軸を再利用できる、という位置づけです。

関連資料:
- [OD306｜非所有と実効権力・非支配論](derivatives/306/README.md)
- [人間向け要約](derivatives/306/human-entry.md)
- [Access Topology & Effective Exit Reuse Kit](ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md)
- [AI索引・日本語](derivatives/306/ai-index.md)
- [Freenet issue #4381](https://github.com/freenet/freenet-core/issues/4381)
- [generic delegate-secret export/import PR #4506](https://github.com/freenet/freenet-core/pull/4506)
- [hosted proxy disclosure PR #4530](https://github.com/freenet/freenet-core/pull/4530)
- [node export endpoint PR #4531](https://github.com/freenet/freenet-core/pull/4531)
- [browser export wiring PR #4562](https://github.com/freenet/freenet-core/pull/4562)
- [low-friction migration issue #4592](https://github.com/freenet/freenet-core/issues/4592)
- [live import PR #4603](https://github.com/freenet/freenet-core/pull/4603)
- [magic-link migration PR #4724](https://github.com/freenet/freenet-core/pull/4724)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/

## 14. 入力欄に書かれたauthorは、認証された実行Originと同じか

APIのrequest bodyに `author` や `actor` のような文字列があっても、その値をcallerが自由に選べるなら、**認証された主体**とは別物です。表示用のラベルなら許容できる場合でも、downstreamのcontrol logicがその値を信頼するなら境界は変わります。

```text
caller-chosen identity label
≠
authenticated control-path origin
```

Hermes Agent PR #61982のKanban REST APIでは、commentの `author` をcallerが送信でき、その値がdurable historyへ保存されていました。一方、実際のworker側comment bridgeは、comment authorがworker自身のidentityと一致すると「自分のcomment」としてskipします。

この二つを組み合わせると、service credentialを持つ外部controllerがworker名を `author` に指定し、本来はoperator steerとして届くべきcommentをworker自身のcommentに見せてskipさせることができます。つまり問題は表示上の帰属だけでなく、**callerがdownstreamの制御判定に使われるOriginを選べること**でした。

Nakagawa-masterのreview後、receiverはこの区別へ明示的に同意し、commit `9ebf06e8c2` で次を変更しました。

- `CommentRequest.author` を削除し、余分な `author` を送るrequestは422で拒否する。
- durable comment authorをtoken-auth seamが検証したprincipalから決める。
- service tokenがないsurfaceではcaller文字列ではなく固定の `external-api` を使う。
- taskの `created_by` も同じactor derivationへ揃える。
- regressionで `author="worker-bot"` の偽装が拒否され、正規commentが `kanban-api` として保存され、実際にoperator steerとしてworkerへ届くことまで確認する。

同じ「誰がやったか」という文字列でも、**UI上の説明**と**認証・制御に使うOrigin**は分ける必要があります。後者をcallerが自由に選べると、監査履歴だけでなく、skip・routing・approval・suppressionなどのcontrol pathまで変わり得ます。

この記録時点でPR #61982はopenです。receiverの明示的な同意、code/test変更、review scopeの再確認までは確認できますが、merge・release・production use・利用者規模はまだ数えません。

関連資料:
- [Hermes Agent PR #61982](https://github.com/NousResearch/hermes-agent/pull/61982)
- [Nakagawa-master provenance/control-path review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5376987496)
- [receiver response](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930276480)
- [receiver fix commit `9ebf06e8c2`](https://github.com/NousResearch/hermes-agent/commit/9ebf06e8c2c8882f307a18eda3237d62ba4a84b7)

## 関連する索引と資料

- [24のテーマから見る](human-translation/WORLD_MAP.md)
- [OD001–OD306を横断して見る](human-translation/ALL_306_HORIZONTAL_MAP.md)
- [Theory → Real-World Influence](THEORY_TO_REAL_WORLD_INFLUENCE.md)
- [Reuse Kits](REUSE_KITS.md)
- [Machine Discovery](machine-discovery/README.md)
- [AI Agent Execution Boundary Tests](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 記載範囲

このページでは、公開情報から確認できる区別、事例、関連資料を案内しています。個別の実装例は、その範囲で確認できる事実を示します。

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)


## 15. 検索で上位に出ても、読まれた・理解されたと言えるか

検索結果に表示されることと、実際にクリックされ、読まれ、理解され、人物や理論へ戻ることは別です。

```text
high search position / impression
≠
click
≠
reading
≠
understanding
≠
person-Origin recognition
```

2026-09-29〜2026-10-01のGoogle Search Consoleでは、master.ricette.jp の「ai文明論」が複数の理論ページで1位表示を含む露出を持ち、「実績」でも公式アーカイブ関連ページが上位に表示されました。一方、この観測範囲ではクリックは0でした。

したがって、検索順位やimpressionは「発見可能性が存在する」という証拠にはなりますが、影響作用力そのものの成立証拠にはしません。次に必要なのは、検索意図と着地ページの意味が一致し、一接触の中で読者が価値を受け取り、必要なら原典・人物Originへ自然に戻れることです。

再利用時は、少なくとも次を分けて確認します。

```text
discovery
→ voluntary entry
→ in-page payoff
→ deeper source re-entry
→ later return / restatement / carry
```

関連資料:
- [一般向け入口](human-translation/README.md)
- [中川マスターとは誰か](human-translation/who-is-nakagawa-master.md)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)


## 16. テストが全部通ったら、残っている設計上の失敗可能性も消えたと言えるか

CIがすべてgreenでも、テスト集合が表現していない状態遷移や時間経過の問題は残り得ます。

```text
all tested checks pass
≠
all materially possible lifecycle failures are covered
```

Qwen Code PR #12582では、2026-10-02時点でCIが24 pass / 0 fail / 0 pendingまで進みました。一方、reviewでは別のlifecycle gapが残りました。managed hostが明示削除されずにすべてofflineになり、leaseが期限切れになった場合、`running` のrunを自動settleする対称的なsweepがなく、実行主体がいないままrunning状態が残り続け得る、という問題です。

ここで重要なのは「CIが弱い」という一般論ではありません。**何を検査したか**と**何がまだ検査・settleされていないか**を分けることです。

```text
green CI
→ tested contracts are currently satisfied

but

unmodeled lifecycle state
→ may still leave operator-visible stuck state
```

実装や運用を評価するときは、少なくとも次を分けて確認します。

```text
covered transition
→ tested result
→ untested transition
→ possible persistent state
→ explicit recovery / settlement rule
```

関連資料:
- [Qwen Code PR #12582](https://github.com/QwenLM/qwen-code/pull/12582)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)


## 17. 「同じ人がやった」と書いてあれば、制御上のOriginも同じか

表示上の名前と、認証された実行主体は同じものではありません。とくに、その名前が後続のskip・routing・approval・suppressionに使われる場合、単なる表示ラベルではなく制御入力になります。

```text
displayed actor label
≠
authenticated control-path origin
```

Hermes Agent PR #61982では、REST APIのcomment bodyにcallerが `author` を指定でき、その値が保存されていました。一方、実行中worker側は、comment authorがworker自身のidentityと一致すると「自分のcomment」とみなしてlive steerから除外します。

そのため、service credentialを持つ外部controllerがworker名をauthorに指定すると、本来は外部operatorから届いた指示なのに、worker自身のcommentとして扱わせる余地がありました。

Nakagawa-masterのreview後、receiverはこの境界を認め、caller指定のauthorを廃止し、durable authorとtask created_byを認証済みprincipalから決めるよう変更しました。回帰testも、worker名の偽装requestを422で拒否し、正規commentが `kanban-api` として保存され、実際にoperator steerとして届くことまで確認しています。

ここから再利用できる問いは、「名前が正しそうか」ではありません。

```text
who authenticated
→ what durable Origin is recorded
→ what downstream control logic consumes that Origin
→ can the caller choose a label that changes control behavior
```

という順で確認します。

関連資料:
- [Hermes Agent PR #61982](https://github.com/NousResearch/hermes-agent/pull/61982)
- [Nakagawa-master review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5376987496)
- [receiver fix explanation](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930276480)
- [Independent verification & reuse registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
