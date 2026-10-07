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
- [OD001–OD310を横断して見る](human-translation/ALL_310_HORIZONTAL_MAP.md)
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
recognition of Nakagawa Master
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

Qwen Code PR #12582では、2026-10-02の途中段階でCIがgreenになった後も、別のlifecycle gapが確認されました。managed hostが明示削除されずにofflineになり、leaseが期限切れになったとき、実行主体がいないのに `running` のrunが残り続け得る状態です。

その後、receiver側はcommit `37bc6c21` でこの経路に明示的なsettlementを追加しました。最新leaseの期限切れから既存lease時間の2倍をbounded graceとして待ち、reclaimされなければrunを終了させます。長いrenewal履歴でgraceが意図せず伸びない回帰testも追加され、実daemon / Host / UIの検証では、reclaimされなかったrunがfailedへ移り、active workが解放されることまで確認されています。同じcredentialでHostが戻った場合にreclaimして完了できる経路と、UIからのcancelが永続化される経路も別に確認されています。

ここから得られるのは、「green CIは信用できない」という結論ではありません。重要なのは、**何を検査したか**と、**まだどの状態遷移を表現していないか**を分け、見つかったgapをrecovery / settlement ruleと回帰testへ変換することです。

```text
green CI
→ covered contracts are satisfied
→ uncovered lifecycle state is found
→ persistent failure mode is made explicit
→ settlement rule is implemented
→ regression + runtime evidence verify the new boundary
```

それでも、この修復だけから「ほかのlifecycle failureもすべて消えた」とは推定しません。実装や運用を評価するときは、少なくとも次を分けて確認します。

```text
covered transition
→ tested result
→ uncovered transition
→ possible persistent state
→ explicit recovery / settlement rule
→ regression and runtime verification
```

関連資料:
- [Qwen Code PR #12582](https://github.com/QwenLM/qwen-code/pull/12582)
- [receiver fix commit `37bc6c21`](https://github.com/QwenLM/qwen-code/commit/37bc6c21ee02ad402bc174948a1a5168e01d1ac9)
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


## 18. ワークフロー全体が古ければ、現在versionの測定も成熟していると言えるか

長く動いているworkflowでも、**いま公開されているversion**が昨日出たばかりなら、そのversionのopens、clicks、bouncesなどはまだ十分に返ってきていない場合があります。

```text
whole-workflow history age
≠
current-version cohort age

old first send
≠
current version has had enough time to collect feedback
```

PostHog PR #107802 の current head `d0a895c5` では、workflow suggestion scout は性能値そのものについては `workflows-version-stats` を使い、versionを分けて読む設計になっています。一方、同じskillの48時間maturity判定では、`workflows-stats` を日次で読み「最初のsend日」をそのversionがliveになった時点として扱う指示が残っています。

ここには測定surfaceのずれがあります。PR内のMCP tool contract自身が、`workflows-stats` はworkflowの**全履歴**を読むと説明しています。そのため、何か月も送信してきたworkflowが昨日v8へpublishされた場合でも、全履歴の最初のsend日を使うとv8を「48時間以上成熟」と誤認できます。すると、新versionのopensやbouncesがまだ到着途中なのに、copyの良し悪しを早すぎる時点で判定する可能性があります。

同じcontractには、この用途のために `workflows-list-versions` があり、各published versionがいつliveになったかを返し、「live versionがどれだけ送信されているかを判断する」ために使うと明記されています。version historyが存在しないlegacy caseだけ、send開始時刻から推定するfallbackが説明されています。

したがって、再利用できる境界は次です。

```text
measure current-version performance
→ identify the same version's publication/cohort start
→ wait for its feedback window
→ judge that version

not:

measure current-version performance
→ borrow workflow-wide historical age
→ treat the new version as mature
```

最小の回帰fixtureは、例えば次です。

```text
v7:
  sends: weeks of history

v8:
  published: < 48 hours ago
  sends: today

expected:
  v8 is immature

must_not:
  old v7/history rows make v8 pass the 48h gate
```

この事例は「時間が経ったか」という単純な問題ではなく、**どの対象について時間を測ったか**というmeasurement attributionの問題です。数値をversionごとに分離していても、判定に使う時間軸を別populationの履歴から借りれば、結論は再び混ざります。

この記録時点では、receiver側へこの指摘を書き込む操作はGitHub側で拒否されており、receiverによる採用・修正・再言及は成立していません。したがって、これは公開コードとtool contractから確認した再利用可能な検査例であり、Nakagawa Masterの外部作用creditとしては数えません。

関連資料:
- [PostHog PR #107802](https://github.com/PostHog/posthog/pull/107802)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)


## 19. 新しく登録できる権限は、既存identityを置換できる権限と同じか

新しいHost、device、credential、endpointを登録できることと、**どの既存identityを失効・置換してよいか**が決まっていることは別です。

```text
authority to enroll a new endpoint
≠
authority to choose an existing endpoint to revoke or supersede
```

この違いは、再登録やcredential紛失からの復旧で重要になります。たとえば2台のHostが偶然、

```text
same name
+
same hostname
+
same workspace path
```

を持っていても、それだけで同じidentityとは限りません。表示用属性を「同一Hostの証明」として使うと、新しい登録tokenを持つ主体が、別のHostのcredentialまで誤って失効させる可能性があります。

Qwen Code issue #13122では、Hostを再登録すると新しい `hostId` とsecretが追加される一方、古いrowとcredentialが残り得る問題が公開されています。receiver側のtriageは、単純なname/path dedupeにも別Hostを誤失効させる危険があると整理しています。

Nakagawa-masterからは、通常のenrollは既存identityを推測して破棄せず、**置換するときだけ対象のstable identityを明示する**案を提示しています。

```text
generic enroll
→ new identity
→ existing identities unchanged

explicit replace
→ name exact superseded identity
→ verify it belongs to the authorized scope
→ create replacement identity / credential
→ migrate required bindings
→ revoke old credential
→ leave any look-alike endpoint unchanged
```

この形なら、次の2つを分けて検証できます。

1. **creation authority** — 新しいendpointを作ってよいか。
2. **destructive replacement authority** — どの既存endpointを失効・置換してよいか。

OD307はここへ時間方向のもう一段を追加します。新しいcredentialやHostが古いものと関係を持つことは、replacement / continuity / authority inheritanceが同時に成立することを意味しません。

```text
same operational role
≠ same identity continuity

same lineage
≠ same authority scope

inherited credential or binding
≠ inherited legitimacy
```

したがって、置換時は「どのidentityをsupersedeするか」だけでなく、旧→新のtransition、保持されたbinding、変更されたauthority scope、失効したcredentialを後から再構成できることも別に検査できます。これはOD306のaccess topologyを置き換えるのではなく、OD307のidentity / Kernel lineage軸を重ねるものです。

置換対象が消えている、古い、scope外である場合は、credential失効・binding移行・run/lease変更を何も起こさずfail closedにする回帰testが有効です。

ここで確認できるのは、公開issueに対してこの明示supersession案が提示されたところまでです。この記録時点では、Qwen Code側による採用、実装、merge、releaseは確認していません。

関連資料:
- [Qwen Code issue #13122](https://github.com/QwenLM/qwen-code/issues/13122)
- [explicit supersession proposal](https://github.com/QwenLM/qwen-code/issues/13122#issuecomment-5952715999)
- [Access Topology & Effective Exit Reuse Kit](ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md#g-enrollment-authority-is-mistaken-for-replacement-authority)
- [machine-readable independent reuse challenges](machine-discovery/independent-reuse-challenges-v1.json)
- [OD307｜自己改変同一性とKernel系譜継承論](derivatives/307/README.md)
- [OD306｜非所有と実効権力・非支配論](derivatives/306/README.md)
- Canonical Parent (OD307): https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-14-self-modification-identity-kernel-lineage/
- Canonical Parent (OD306): https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/


## 20. 終わった仕事の費用を記録したら、今の仕事まで止めてよいか

たとえば、会社で二つの施策が同じ月予算を使っているとします。

施策Aは途中で終了しました。ところが数日後、Aで実際に使っていたサービスから遅れて追加の利用料が届きました。

その費用が本当に発生したなら、記録する意味はあります。

でも、その数字を現在の予算判定へそのまま入れた結果、**まだ正常に動いている施策Bまで自動停止する**なら、話は別です。

ここで分けたいのは、次の二つです。

```text
何が実際に起きたかを記録すること
≠
その記録に、いま動いている仕事を止める力を持たせること
```

古い仕事で費用が発生した事実は、消す必要がありません。

ただし、その事実をどの帳簿へ入れ、誰がその帳簿を読み、何の判断に使うのかまで見なければ、「記録しただけ」のつもりで現在の仕事へ作用することがあります。

### AIの実行でも、同じ形が起きる

AIに仕事を任せる仕組みでも、似た問題が起きます。

ある処理が時間切れになり、管理側は終了したと判断した。しかし離れた場所のAIはまだ動いていて、あとから「完了しました。これだけ使いました」と返してくる。

このとき、

```text
同じ実行番号が付いている
≠
その結果を実際に受理した証拠
```

です。

終了後の答えを採用しないとしても、計算や課金が実際に発生した可能性は残ります。

問題は、その遅れて届いた使用量を現在の実行予算へ書き戻したときです。予算判定がその数字を読むなら、終了済みの処理が、いま動いている別の処理を止める原因になり得ます。

### Qwen Codeでは、実装と検証まで進んでいる

この境界は、Qwen Codeの公開[issue #13238](https://github.com/QwenLM/qwen-code/issues/13238)で具体的な不具合として確認され、[PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)で修正され、2026年10月4日にmainへ統合されました。

まず、受理済みの結果を示す記録が追加され、**本当に一度受理した結果の再送**と、**終了後に届いた古い結果**を分ける形になりました。

そのうえでNakagawa Masterは、終了済みの処理から届いた使用量を現在の実行予算へ書き戻すと、別の仕事を止める制御作用が残る点を指摘しました。今回の修正では、終了後の予算帳簿への書き込みを止め、遅れて判明した実際の使用量を残す必要があるなら、現在の実行予算とは別の観測面として設計する方向が採られています。

実装commit `bb5c5d74`では、終了後に非常に大きな使用量が届いても、終了時点の予算記録を変えない回帰testが追加されています。

receiver側の[検証報告](https://github.com/QwenLM/qwen-code/pull/13241#issuecomment-5967834798)では、実際のdaemon / Hostを使い、遅れて1,050 tokenの完了結果が届いても予算記録が100 tokenのまま変わらないことが報告されています。

さらに同じheadで、[実際のWeb Shellとnative Hostを使った追加検証](https://github.com/QwenLM/qwen-code/pull/13241#issuecomment-5970236028)も行われています。通常の完了と同一結果の再送は別に受理しつつ、取消や期限切れのあとに届いた古い完了結果は拒否され、終了済みの状態や予算記録を変えないことが確認されています。

### ただし、「遅い費用は無視すればよい」という話ではない

終了後に実際の費用が発生していたなら、その事実まで消してよいわけではありません。

必要なのは、**実際に起きたことを記録する場所**と、**現在の仕事を止めたり進めたりする判断に使う場所**を分けることです。

観測用の記録を別に作っても、その記録が再び予算や実行判断へ流れ込むなら、同じ問題が戻ります。名前ではなく、**その情報を誰が読み、何を動かすのか**まで確認します。

### 自分の仕組みで確かめるなら

一つの処理を終了させ、その前後の帳簿を保存します。別の処理は動かしたままにします。その後、終了した側から大きな使用量を送ります。

見るのは三つです。

1. 古い結果が採用されないこと。
2. 終了時点の実行予算が勝手に変わらないこと。
3. 実際の予算判定を動かしても、現在の別処理が正しく続くこと。

受理済みの同一結果を再送する場合は反対側も確認します。本当に受理した証拠があるなら、二重適用せず同じ結果として扱える必要があります。

この判定はAIだけでなく、遅れて届く決済通知、広告費、クラウド利用料、送信結果、バックグラウンド処理にも応用できます。

### 確認できている範囲

PR #13241は2026年10月4日に[merge commit 35616f3b](https://github.com/QwenLM/qwen-code/commit/35616f3b643f6d87cc00112d961a0fbb448aca00)でmainへ統合されました。receiver自身のPR説明でも、現在の実装が **@Nakagawa-masterの外部技術提案** に基づくことが明記され、repository maintainerの裁定とは別であることも明確にされています。current headは人間reviewer qqqys のAPPROVEを経ています。

したがって、ここで確認できるのはreceiver側の実装・test・Web Shell / native Host検証・明示的なsource continuity・人間review・mergeまでです。これを含むrelease、独立した実利用、利用者規模、後日の自発的なOrigin再言及、Qwen Code全体による理論採用までは主張しません。

具体的な検証条件は[Current-Authority Reuse Kit 第17節](CURRENT_AUTHORITY_REUSE_KIT.md#17-a-late-observation-can-still-control-current-work)へ。過去から続く系譜と現在の権限を分ける考え方は、[OD307の人間向け要約](derivatives/307/human-entry.md)と[親原典](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-14-self-modification-identity-kernel-lineage/)へ戻れます。

隣接する問題:
- [同じ共有リンクでも実行場所が変わる話](human-translation/entry-stories/09-same-share-different-runtime.md)
- [送信エラーの後に二重課金が起きる話](human-translation/entry-stories/01-double-charge-after-error.md)
- [独立検証・再利用の受付](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
