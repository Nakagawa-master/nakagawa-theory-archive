# 公開記録で確認できる外部実装事例｜中川マスターの公開コメント後に第三者プロジェクトで確認された変更

言語: **日本語** | [English](REAL_WORLD_IMPACT.en.md) | [中文](REAL_WORLD_IMPACT.zh.md)

**最終確認: 2026-09-24**

中川マスター（Nakagawa Master ／ pen-name of Keisuke Nakagawa）は、Keisuke Nakagawaの筆名です。SNSでは「マスター」、外部投稿では「MasterJP」名義も使用しています。

このページは、`Nakagawa-master` 名義で公開されたGitHub上のコメントやreviewと、その後に第三者プロジェクトで確認できる変更を、読者が自分で辿れる形にまとめた**公開記録の案内ページ**です。

このページの目的は、人物や理論を権威化することでも、影響度を自己採点することでもありません。個々の事例について、

- 何が公開されたのか
- 第三者が何を確認・変更したのか
- merge / release / deploymentまで確認できるのか
- どこから先は未確認なのか

を、公開リンクから区別して確認できるようにすることです。

## このページの読み方

各事例は、できるだけ次の4点に分けています。

1. **公開起点** — `Nakagawa-master` が第三者repositoryへ書いた具体的なコメントやreview
2. **第三者側の記録** — repository owner、author、reviewerなどによる応答、実装、テスト、文書変更
3. **現在状態** — open / merged / released / deployedなど、公開記録で確認できる状態
4. **確認できない範囲** — 利用者数、広範な採用、理論全体への支持など、証拠がないもの

コメントが存在するだけでは、実装されたことにはなりません。実装されたことと、mergeされたことも別です。mergeされたことと、release / deployment /実利用も別です。

## 利用者にとって分かりやすい例

以下の事例で扱われている区別は、たとえば次のような製品挙動につながります。

- AIが提示した数値と、システム自身が測定した数値を区別する
- 過去に許可された情報でも、現在の条件で利用権限を再確認する
- 同じIDであることと、そのデータを上書きしてよいことを区別する
- AI処理中のlocal IDと、元資料のsource identityを区別する
- データ取得処理の成功と、有効な測定値が得られたことを区別する
- 推薦理由の文章が同じでも、誰がどの根拠で推薦されたかを保持する
- 現在の所属状態と、過去時点の履歴事実を区別する
- 承認操作が一度だったことと、外部送信が一度だけ起きたことを区別する

以下では、公開記録で確認できる範囲だけを記載します。

---

## 1. PostHog｜AIが提示した数値と、PostHog自身の測定値を分ける

**対象:** [PostHog/posthog#92252](https://github.com/PostHog/posthog/pull/92252)  
**現在状態:** open / unmerged

PostHogのworkflow scoutは、AIがworkflow改善案と数値的なevidenceを人に提示する仕組みです。

`Nakagawa-master` のreviewは、producer / scoutが送った数値と、実際のworkflow・version・stepからPostHog側が測定した数値を同一視しないよう指摘しました。

- [Nakagawa-master evidence review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)
- [Nakagawa-master capability-boundary review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5245587245)

その後、PR authorはserver側で対象stepのmetricを読み直し、producer由来の値とは別に保持する実装・テスト・表示変更を追加しました。UIでは `Measured by PostHog` と `Unverified` を区別し、producerの値とPostHog側の値が異なる場合も、その差を表示する設計になっています。

さらに、別のreviewで指摘した「narrow capability と user-grantable capability は同じではない」という境界についても、current PRには `hog_flow_proposal` をprogrammatic / internalにし、通常のpersonal API key / OAuth / session grantから外し、server-minted scout scopeとして扱う変更が入っています。

- [server-side measurement commit `721311a9`](https://github.com/PostHog/posthog/commit/721311a97488781dd590708abe697480c5c0e9e8)
- [programmatic-only scope commit `3ecb122d`](https://github.com/PostHog/posthog/commit/3ecb122dd7062d864c135213282613bfc80a2ebf)
- [server-minted scope commit `d962e51c`](https://github.com/PostHog/posthog/commit/d962e51c22e34f526f94ce6d581aa429ed7d87a3)

これらのcommit本文は `Nakagawa-master` reviewを唯一の原因として明示していません。そのため本ページは、**review後に同じ境界へ対応する第三者実装が入ったこと**は記録しますが、唯一因果までは主張しません。

**公開記録から確認できること:** review後に第三者authorがcode / tests / UI / scope境界を変更したこと。  
**まだ確認できないこと:** このPRのmerge、release、production deployment、利用者数、変更の唯一因果。

---

## 2. Dream｜「内容が安全化されたこと」と「現在も利用してよいこと」を分ける

**対象:** [tushardhara/dream#12](https://github.com/tushardhara/dream/issues/12) → [PR #28](https://github.com/tushardhara/dream/pull/28)  
**現在状態:** PR #28 merged

`Nakagawa-master` の公開コメントは、内容が一度sanitized / approvedされたことを、将来も無条件に利用できる権限として扱わず、actor、recipient、purpose、source lineage、policy stateなど現在条件を再確認する設計を提案しました。

- [Nakagawa-master design contribution](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [repository owner response](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)
- [merged PR #28](https://github.com/tushardhara/dream/pull/28)
- [公開case note](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

repository ownerはこの区別をissue上で明示的に受け取り、その後のPRでcurrent rights / lineageの再確認、revocation、recipient変更、source revisionなどを扱う実装とnegative testsを追加しました。

**公開記録から確認できること:** コメント → owner応答 → code / tests → merge。  
**まだ確認できないこと:** 実利用者数や、この一事例を超えた広範な採用。

---

## 3. MemberJunction｜同じIDと、上書きしてよい所有権を分ける

**対象:** [MemberJunction/MJ#4519](https://github.com/MemberJunction/MJ/pull/4519) → [#4496](https://github.com/MemberJunction/MJ/pull/4496) → [#4546](https://github.com/MemberJunction/MJ/pull/4546) → [v6.1.2](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2)  
**現在状態:** merged → LTS backport merged → v6.1.2 released

migrationで同じprimary keyのrowを見つけても、そのrowを自動的に上書きしてよいとは限りません。

`Nakagawa-master` のreviewは、row identityと、そのrowを誰が管理・収束させる権限を持つかを分ける必要を提示しました。

- [Nakagawa-master contribution](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [PR #4519](https://github.com/MemberJunction/MJ/pull/4519)
- [公開case note](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

その後、第三者reviewerによる確認、authorによるcode / tests / documentation変更、merge、metadata migration生成、LTS backport、v6.1.2 releaseまで公開記録で確認できます。

さらに、MemberJunctionの公開certification issueには、既存rowを含むdatabaseをv6.1.2へupgradeし、該当migration群がcollisionなしで適用されたという外部報告があります。

- [External 6.1.2 certification report](https://github.com/MemberJunction/MJ/issues/4475#issuecomment-5715684968)

同じ報告には別のregressionも記載されているため、このページは「v6.1.2全体に問題がない」とは述べません。

**公開記録から確認できること:** review → 独立確認 → code / tests / docs → merge → backport → release → 該当collisionが発生しなかった外部upgrade report。  
**まだ確認できないこと:** 全利用環境での結果、利用者規模、一般市場での採用範囲。

---

## 4. LlamaIndex｜local node identityと、元sourceのidentityを分けて保持する

**対象:** [run-llama/llama_index#21933](https://github.com/run-llama/llama_index/issues/21933) → [PR #23038](https://github.com/run-llama/llama_index/pull/23038)  
**現在状態:** open / draft / unmerged

retrieval処理の途中でtextが保持されていても、upstream document identityが失われれば、後から元sourceへ戻れない場合があります。

`Nakagawa-master` のissue commentは、framework内部のnode identityと、upstream source identityを別の情報として保持するcompatibility boundaryを提示しました。

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)
- [third-party PR #23038](https://github.com/run-llama/llama_index/pull/23038)
- [公開case note](discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)

第三者が開いたPR #23038は、そのcommentをcompatibility contractとしてPR本文に明示し、`document_id` / `document_name`をmetadataへ保持する実装とtestsを追加しています。

**公開記録から確認できること:** source commentが明示的に参照され、第三者PRでcode / testsへ反映されていること。  
**まだ確認できないこと:** merge、release、deployment。

---

## 5. MemberJunction｜別のreviewerが同じ問題を自分で検証した例

**対象:** [MemberJunction/MJ#4487](https://github.com/MemberJunction/MJ/pull/4487) / [#4524](https://github.com/MemberJunction/MJ/pull/4524)  
**現在状態:** 両PRとも open / unmerged

#4487では、`Nakagawa-master` がaliased re-exportされたpublic typeについて、内部declaration名と公開alias名を混同するとunsafe renameにつながり得る点を指摘しました。

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5219601735)

その後、別のreviewer `rkihm-BC` が自分のformal reviewで同じ問題を再確認し、source-side nameを保持する修正とregression testを要求しています。

- [independent reviewer confirmation](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5241419422)

#4524でも同じreviewerが `@Nakagawa-master's point about D is confirmed` と明記し、自分でcheckerを実行した結果とともに修正方針をreviewへ取り込んでいます。

- [confirmation on #4524](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5242805347)

その後、両PRでauthor側の実装も進みました。#4487ではaliased re-exportについてalias名とsource declaration名の両方をpublic-symbol setへ保持し、published aliasは`warn`、未re-export siblingは`error`のままというregression testsが追加されました。Nakagawa-masterはcurrent headを再確認し、元指摘が解消されたことをreview `5252973190` で明示しています。#4524ではdirect `[__mj]` formのfail-openが修正され、同じ第三者reviewerが再実行してfalse-pass exit 0からfail-closed exit 1へ変わったことを確認しています。

- [#4487 closure review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5252973190)
- [#4524 independent re-verification](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5252195432)

**公開記録から確認できること:** 別の第三者reviewerによる名前付き確認に加え、author実装とregression tests、#4487でのorigin reviewer closure、#4524での独立再実行検証まで進んだこと。  
**まだ確認できないこと:** 両PRのmerge、release。

---

## 6. PostHog｜推薦理由の文章と、その理由のsourceを混ぜない

**対象:** [PostHog/posthog#102550](https://github.com/PostHog/posthog/pull/102550) → [#102686](https://github.com/PostHog/posthog/pull/102686)  
**現在状態:** #102550 merged / deployed、#102686 merged / deployed

PostHogのreviewer推薦UIでは、同じ説明文を持つreviewerをgroup化すると、`Code history` と `Added by scout` のような異なるsourceが一つに見える可能性がありました。

`Nakagawa-master` のreviewは、説明文が同じことと、推薦根拠のsourceが同じことを分けるよう指摘しました。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

第三者maintainerはsource categoryをgroup keyへ含めるcode / tests / UI story変更を追加し、#102550は`master`へmergeされました。PostHogのdeploy status commentではdev / prod-us / prod-euへのdeploymentも記録されています。

- [merged PR #102550](https://github.com/PostHog/posthog/pull/102550)
- [deploy status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557)

その後、同じmaintainerが別のUI surfaceを扱う#102686でも、同じreasonであってもsource categoryが異なる場合は分ける設計を使いました。current headは第三者reviewer `stamphog` からAPPROVEDを受け、2026-09-18T15:49:22Zにmergeされました。PostHogのdeploy statusはdev、prod-us、prod-euへのdeploymentを記録しています。

- [#102686 external approval](https://github.com/PostHog/posthog/pull/102686#pullrequestreview-5249196997)
- [merged PR #102686](https://github.com/PostHog/posthog/pull/102686)
- [#102686 deploy status](https://github.com/PostHog/posthog/pull/102686#issuecomment-5732760371)

**公開記録から確認できること:** 最初のreview → code / tests / UI change → merge → deployment。さらに別PRで同じ設計区別が再利用され、独立approval → merge → dev/prod-us/prod-eu deploymentまで進んだこと。  
**まだ確認できないこと:** 実際の利用者数や利用結果、別person・別contextでのさらなる再利用。

---

## 7. TourCRM｜現在の所属状態と、過去時点の履歴を分ける

**対象:** [Alan8893/tourcrm#97](https://github.com/Alan8893/tourcrm/pull/97) → [PR #101](https://github.com/Alan8893/tourcrm/pull/101)  
**現在状態:** follow-up PR #101 merged

attendance履歴では、「今その人がparticipantか」と「そのoccurrence時点でparticipantだったか」は別の条件です。

`Nakagawa-master` のreviewは、現在のmembershipだけで過去のrosterを判定すると、後からmembershipが終了しただけで過去のattendanceが見えなくなったり、訂正できなくなったりする問題を指摘しました。

- [Nakagawa-master review](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)
- [owner response](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [follow-up PR #101](https://github.com/Alan8893/tourcrm/pull/101)

repository ownerはこの指摘をreal bugとして認め、専用follow-up PRを作成しました。実装commitにもreview feedbackのsourceが明記されています。さらにtest fixtureについて追加reviewが行われ、旧実装で実際にfailする過去日時fixtureへ修正された後、PR #101はmergeされました。

**公開記録から確認できること:** review → ownerによるbug確認 → follow-up PR → code / tests → 追加test修正 → merge。  
**まだ確認できないこと:** release、production deployment、利用者規模。

---

## 8. Clientverse｜一度の承認と、一度の外部送信を同一視しない

**対象:** [ebyron357/Clientverse-crm#27](https://github.com/ebyron357/Clientverse-crm/pull/27)  
**現在状態:** merged

providerがmessageを受理した後にresponseだけ失われた場合、単純に`failed`として再送可能に戻すと、同じmessageを二重送信する可能性があります。

`Nakagawa-master` のreviewは、approvalがsingle-useであることと、外部side effectが一度だけ起きたことを分ける必要を指摘しました。

- [Nakagawa-master review](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690360136)
- [owner response](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690677339)
- [merged PR #27](https://github.com/ebyron357/Clientverse-crm/pull/27)

repository ownerはこれをstate machine上のreal defectとして認め、`outcome_unknown`、reconciliation、dispatch idempotency key、response-loss regression testなどを追加しました。

**公開記録から確認できること:** review → ownerによるdefect確認 → state-machine / provider contract / tests変更 → merge。  
**まだ確認できないこと:** real provider環境でのdeploymentや利用者規模。

---

## 9. Replay｜過去のconsent eventと、現在の利用可否を分ける

**対象:** [aferna6-cell/Replay#67](https://github.com/aferna6-cell/Replay/issues/67)  
**現在状態:** issue上で設計方針の採用を確認 / repository code実装は未確認

`Nakagawa-master` の公開コメントは、historical consentの記録と、現在そのデータを保持・処理・利用してよいかというeligibilityを別に扱う設計を提案しました。

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository owner response](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

repository ownerは起点を明示したうえで、immutable consent event、current eligibility、withdrawal / deletion receipt、downstream gateなどを自分のprotocolとして再記述しています。

**公開記録から確認できること:** comment → ownerによる明示的な受け取りと設計方針への反映。  
**まだ確認できないこと:** schema / code / tests実装、merge、release、実データ運用。

---

## 10. Cline｜委任を承認するとき、子agentへ渡る能力範囲を見えるようにする提案

**対象:** [cline/cline#14225](https://github.com/cline/cline/pull/14225)  
**現在状態:** base PR merged / この提案のfollow-up実装は未確認

configured subagentのdelegationでは、一回のapprovalで子agent側の複数tool callが進む設計があります。

`Nakagawa-master` のreviewは、delegation approval時に、実際に子agentへ渡るcapability setを人が理解できるようにするUXを提案しました。

- [Nakagawa-master review](https://github.com/cline/cline/pull/14225#pullrequestreview-5242232355)
- [external author response](https://github.com/cline/cline/pull/14225#issuecomment-5723653394)

external authorは`@Nakagawa-master`を名指しし、現状より良いUXだと応答し、将来のagent config改善へ含める意向を示しました。

base PR #14225自体はmerge済みですが、そのmergeはこの提案の実装を意味しません。

**公開記録から確認できること:** 名前付きreviewと、authorによる肯定的な応答・follow-up意向。  
**まだ確認できないこと:** 独立したfollow-up issue / PR、code / tests / UI実装、release。

---


## 11. Local Operator｜実行中agentが自分のapproval gateを弱められないようにする

**対象:** [damianvtran/local-operator#1282](https://github.com/damianvtran/local-operator/issues/1282) → [PR #1291](https://github.com/damianvtran/local-operator/pull/1291) → [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)  
**現在状態:** PR #1291 merged / v0.59.10 released・published（2026-09-19）

issue #1282では、実行中agentが自分を制約しているapproval policyを、同じagentが書ける設定ファイル経由で `ask → auto` に変更できると、人間approvalを自分で解除できてしまうという境界を提示しました。一方で、人間operatorが明示的にapproval modeを変更する経路は残す必要があります。

- [issue #1282](https://github.com/damianvtran/local-operator/issues/1282)
- [third-party PR #1291](https://github.com/damianvtran/local-operator/pull/1291)

第三者authorが開いたPR #1291は本文で明示的に `Closes #1282` と記載し、live approval gateの変更sourceを判定条件へ入れる実装を追加しています。別processからのraw config writeではgateを弱められず、同じprocessの明示的なoperator操作では変更できるpositive controlも含まれています。実際のsecond-process writeを使うregression testや、agent-facing codeからtrusted settings write pathへ抜け道を作らないためのtestsも追加されています。

Nakagawa-masterはcurrent headを元issueのacceptance boundaryに対して再確認し、元のsecurity findingが実装済みであることをreviewで明示しました。

- [closure review](https://github.com/damianvtran/local-operator/pull/1291#pullrequestreview-5253448083)

その後PR #1291はmergeされ、公開release `v0.59.10` に含まれました。release notesは #1291 を明示的に列挙し、変更内容を **“An agent can no longer weaken the approval gate”** と記録しています。repository ownerはPR threadで、publish workflow成功、PyPIでの `0.59.10` 配布、install後の `lop --version` smokeまで記録しています。

- [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)
- [release / publish / installed-smoke record](https://github.com/damianvtran/local-operator/pull/1291#issuecomment-5745312290)

**公開記録から確認できること:** issue → 明示的にそのissueをcloseする第三者PR → code / tests → 複数review/remediation → 元issue側からのclosure確認 → merge（`b1fc1f42`）→ release notesへの収録 → package publication → installed smoke。  
**まだ確認できないこと:** より広い利用者規模での効果、利用者数、またはこのreleaseを越えた独立downstream reuse。

---


### Follow-up: control-plane側でも同じauthority境界が第三者実装へ進んだ

#1291がconfig-file経路を閉じた後、`Nakagawa-master` は別のcontrol-plane境界を [issue #1310](https://github.com/damianvtran/local-operator/issues/1310) として分離しました。論点は、同じOS uidで動くmodel-authored subprocessが、同uidから読めるcontrol credentialだけを使って、自分を制約する `ask → auto` 変更やparked approvalの承認を行えてはならない、というものです。

repository ownerはこのissueを独立に再現し、公開コメントで **“confirmed, real, and being fixed”**、**“it named the right boundary”** と記録しました。さらに、issue本文が想定していた `slash` ではなく実際のsinkは `slash_result` であること、そして `approval_answer(approved=True)` というより強い兄弟経路も同じ問題を持つことを独立に発見しています。

- [owner reproduction / determination](https://github.com/damianvtran/local-operator/issues/1310#issuecomment-5740547291)
- [third-party implementation PR #1324](https://github.com/damianvtran/local-operator/pull/1324)

PR #1324はper-session operator capability、connection-bound proof、共通pre-dispatch guard、negative/positive/tightening controlsを実装し、複数の独立review・QA・design・UX roundを通っています。current head `fe2dc9b6` に対して、Nakagawa-masterは原issueの5 acceptance条件を再確認し、元の#1310 boundaryについてorigin-side closureを記録しました。ただしこれはmerge承認ではなく、PRはoperator/product decisionのためopenのままです。

- [origin-side closure review](https://github.com/damianvtran/local-operator/pull/1324#pullrequestreview-5257968951)

**このfollow-upで公開確認できること:** origin issue → third-party independent reproduction → origin diagnosisの修正 → stronger sibling bypassの独立発見 → third-party implementation → multiple independent remediation rounds → origin-side closure。  
**まだ確認できないこと:** #1324のmerge/release、host OS自体が同uid memory isolationを提供できない環境での保証、phone/device-bound authorityの完成、またはこの境界の別projectへの独立reuse。


## 12. MemberJunction｜row内容保護の次に残ったrow identity境界を第二work itemへcarry

**対象:** [MemberJunction/MJ#4595](https://github.com/MemberJunction/MJ/pull/4595) → [issue #4610](https://github.com/MemberJunction/MJ/issues/4610)  
**現在状態:** PR #4595 open / unmerged、issue #4610 open

PR #4595は、cache-invalidation broadcastでfull row内容をdefaultでは送らないようにしました。その後の `Nakagawa-master` reviewでは、その修正とは別に、`recordData` を消しても他rowのstable primary keyとmutation timingが見えるという残存metadata境界を分離しました。

- [Nakagawa-master row-identity review](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5253531713)
- [Nakagawa-master 二層分解follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [第三者実装・carry応答](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [follow-up issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

PR authorはこの二層分解を明示的に採用し、commit `293b9b40` でentity-level permission filterを実装しました。同時に、row-level disclosureはregressionを弱めて「解決済み」にせず、独立issue #4610へ持ち越しました。#4610本文はframingが主に `@Nakagawa-master` のreview由来であることを明記し、同一entityを読めるがrow visibilityが異なる二人を使う強いacceptance testを維持しています。

さらに#4610では、MemberJunction既存のClassFactory拡張機構へ落とす具体的な実装形を公開し、per-subscriber hot pathをsync / no-I/Oに保つ方向まで具体化しました。

- [#4610 implementation-shape contribution](https://github.com/MemberJunction/MJ/issues/4610#issuecomment-5739586260)

**公開記録から確認できること:** review → 第三者code/test変更 → 第三者による明示的source attribution → より強い境界とregressionを保った第二work item化。  
**まだ確認できないこと:** row-level policy実装、#4595 merge、#4610 close/merge、release、deployment、実利用規模。

---

## 13. Waves Customer Portal｜危険になったestimate CTAを除去しつつ、支払証跡は失わせない

**対象:** [wavespestcontrolfl/waves-customer-portal#4608](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608)  
**現在状態:** merged（2026-09-19）

このPRでは、estimate linkをprovider handoff直前に再評価するguardと、支払receiptだけは危険なCTAを除去してreceipt自体を送るrewrite policyが追加されました。

`Nakagawa-master` reviewは、このrewrite側とrefusal guard側でlink認識語彙がずれている点を指摘しました。refusal guardは、別entity用に発行されたshort codeでも、その `target_url` がestimate linkなら認識します。一方、`rewriteWithheldEstimateLinks()` は `entity_type='estimates'` のshort codeしかrewriteしなかったため、同じlinkを「危険と判定できるのに安全変換できず」、結果として支払receipt全体を拒否し得る状態でした。

- [Nakagawa-master review](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608#pullrequestreview-5254456120)

そのreview後のcommit `029ae44d53` で、`target_url` 由来short linkをrewriteする経路が追加されました。merge後の実装は、直接estimateに結び付くshort codeと、別用途short codeの `target_url` 内にestimate linkがある場合の両方を解決し、危険なliteral linkだけを除去してreceiptを維持し、rewrite対象estimate idを記録します。PRは最終的に `5cecd7627b70d739d7feaf6f45fd784b5741efc3` としてmergeされました。

**公開記録から確認できること:** review → 指摘したshort-link mismatchに対応するcode/test変更 → merge。  
**まだ確認できないこと:** production deployment、利用者規模での効果、project全体によるより広い理論採用。

---

## 14. UpGrade｜UIだけのdelete ruleがbackend authority work itemへcarryされた

**対象:** [CarnegieLearningWeb/UpGrade#3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323) → [issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)  
**現在状態:** #3323 open、#3326 open / implementation pending

`Nakagawa-master` reviewは、frontendのdelete permission matrixがbackendではauthorityとして強制されていないことを確認しました。review対象branchでは、UIがDeleteを隠していても、認証済みReaderがsingle/batchの破壊的APIを直接呼べる状態でした。

- [Nakagawa-master review](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)
- [第三者author response](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)
- [follow-up issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)
- [#3326 implementation-shape contribution](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355)

PR authorは `@Nakagawa-master` を名指しし、delete routeにrole enforcementが存在していなかったことを確認したうえで、single/batch両方へrole matrixとstate ruleを適用するための#3326を新規作成しました。

さらに#3326では、current branchに合わせて、current locked target stateに対してmutation前に一つのshared backend deletion policyを評価し、policy refusalとoperational delete failureを分離する実装形まで具体化しました。

**公開記録から確認できること:** review → authorによる確認・再説明 → 境界を保った専用child work item → source-level実装guidance。  
**まだ確認できないこと:** #3326のcode/test実装、merge、release、deployment、利用者規模。

---

## 15. FieldGIS Reference｜過去のPASS記録を、単発のactivation snapshotへ束ねる

**対象:** [lundus88/fieldgis-reference#273](https://github.com/lundus88/fieldgis-reference/issues/273) → [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288) → [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289) → [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290) → [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)  
**現在状態:** #288 / #289 / #290 / #291 merged（2026-09-20確認）

`Nakagawa-master` の公開コメントは、過去にPASSした証拠が存在することと、現在その商用システムをactivateしてよいことを分けました。具体的には、exact artifact、review証拠、事業・licence証拠、Preview identity、provider/configuration fingerprint、policy version、decision time、失効・再検証条件を一つのactivation snapshotへ束ねる形を提案しています。

- [Nakagawa-master contribution](https://github.com/lundus88/fieldgis-reference/issues/273#issuecomment-5737805962)

その後、第三者PR #288はsingle-useの `LDS_ACTIVATION_SNAPSHOT.json`、fail-closed validator、専用CIを追加しました。PR本文には **“Evidence existence is not activation authority”** と明記され、materialな入力変更があればsnapshotを無効化し、launchをHOLDへ戻すルールが実装されています。

- [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288)
- [独立review approval](https://github.com/lundus88/fieldgis-reference/pull/288#pullrequestreview-5254772097)
- [merge commit `f0aeaf7c`](https://github.com/lundus88/fieldgis-reference/commit/f0aeaf7c381488d5a38f21753d2043cf11f235ae)

後続PR #289は同じactivation-snapshotモデルをdomain/email readinessへ拡張し、#290はemail-provider selectionを同じHOLD/authority modelの下へ追加してmergeされました。さらに#291は、subscription完了の証拠を追加しつつ、DNS、mailbox ownership、Production、public launchを別gateとしてHOLDのまま維持しました。#291は第三者reviewer `rnairing123` のAPPROVEを受けた後、2026-09-19T23:15:06Zにmergeされました。つまり公開記録上、snapshotによるcurrent-authority区分は単発PRだけで終わらず、有料契約という実際の商用証拠が追加された段階まで、複数の運用subcontextで継続して使われています。

- [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289)
- [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290)
- [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)
- [#291 independent approval](https://github.com/lundus88/fieldgis-reference/pull/291#pullrequestreview-5258253534)
- [#291 merge commit `5772de11`](https://github.com/lundus88/fieldgis-reference/commit/5772de11e7b7262b0272deb7881274cff55438be)

ただし、#289 merge後のcurrent `main` を再確認すると、その拡張時に削除された既存fail-closed検証（stale-state rejection、ordered activation sequence、preview visual/workflow QA validation）はまだ復元されていません。mergeやモデル継承の事実と、それらのreview指摘が実装済みかどうかは分けて扱います。

- [fail-closed検証の復元を求めたreview](https://github.com/lundus88/fieldgis-reference/pull/289#pullrequestreview-5254935377)
- [merge後のcurrent mainに残る3 regressionを示したfollow-up](https://github.com/lundus88/fieldgis-reference/issues/289#issuecomment-5740198762)

**公開記録で確認できること:** 公開コメント → 第三者governance実装 → 独立review approval → merge → 同じcurrent-authority modelのdomain/email readiness・provider selection・有料subscription evidenceへのprompt-freeな継続利用 → #291でも独立review approval → merge。  
**この記録だけでは確認できないこと:** 唯一の原因であること、本番launch、顧客規模の効果、別personによる独立reuse、業界全体での再利用、理論体系全体への支持。

---

## 16. LlamaIndex｜cache hitで過去node identityを現在runへ持ち込まないためのcontract decision

**対象:** [run-llama/llama_index#23003](https://github.com/run-llama/llama_index/pull/23003) → [issue #23083](https://github.com/run-llama/llama_index/issues/23083)  
**現在状態:** PR #23003 open、issue #23083 open / maintainer contract decision pending

PR #23003は、ingestion cache keyで異なるdocumentの同一contentが衝突し、別documentの `ref_doc_id` を返し得る問題を修正するfocused PRです。

`Nakagawa-master` のreviewは、その修正後にもgeneric transformation cacheでは別の境界が残ることを指摘しました。SOURCE relationshipを持つintermediate nodeではcurrent chunk `id_` をkeyから外す一方、cacheはtransform済み `BaseNode` 全体を返すため、同じsource/contentでcurrent chunk identityだけが変わると、以前のrunのidentityを含むoutputが再利用され得ます。

- [Nakagawa-master review](https://github.com/run-llama/llama_index/pull/23003#pullrequestreview-5219816814)
- [third-party author response](https://github.com/run-llama/llama_index/pull/23003#issuecomment-5694376083)
- [dedicated follow-up issue #23083](https://github.com/run-llama/llama_index/issues/23083)

PR authorは、残るcollisionを自分の言葉で確認し、generic cache semanticsはこのfocused PR内で一方的に決めるべきではないとして、maintainer-level contract decisionへ分離することに同意しました。その後、専用issue #23083で、

```text
full-node transformation cache
vs
content-stable payload reuse
```

という二つのcoherent contractと、regenerated chunk idを使うacceptance regressionが独立したwork itemとして保持されています。

**公開記録から確認できること:** review → third-party authorによる残存問題の明示的確認・再説明 → maintainer-level専用work item化。  
**まだ確認できないこと:** #23083のcontract決定、follow-up code/test実装、merge、release、deployment、実利用規模。

## 17. Publications｜可逆性とauthority増加を別軸として第三者本文へ実装し、別文書へ再利用

**対象:** [kishibashi3/publications#52](https://github.com/kishibashi3/publications/pull/52) → [PR #57](https://github.com/kishibashi3/publications/pull/57) → [PR #58](https://github.com/kishibashi3/publications/pull/58)  
**現在状態:** #57 merged / GitHub Pages反映確認済み、#58 merged / 同一receiver内の別文書へ再利用

PR #52で `Nakagawa-master` のreviewは、操作を元に戻せるかどうかと、その操作が主体自身の将来の行動可能範囲を広げるかどうかを分離しました。

```text
reversible
!=
authority-neutral
```

そのreviewは、制約対象の主体自身を制約解除のauthority sourceにしないこと、looseningとtighteningを非対称に扱うことを提案しました。

- [Nakagawa-master review on #52](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687)
- [third-party author restatement](https://github.com/kishibashi3/publications/pull/52#issuecomment-5746627251)

receiverはこの指摘を独立した設計軸として再説明し、専用PR #57を起票しました。PR本文は起点を **PR #52 の @Nakagawa-master review** と明記し、第6条件「自己権限の固定 ― 制約される側が制約を緩められない」を本文・CHANGELOG・実務チェックへ実装しました。

- [PR #57](https://github.com/kishibashi3/publications/pull/57)
- [merge commit `4d32ec58`](https://github.com/kishibashi3/publications/commit/4d32ec58d5cbf1c904c432552e114c144186c064)
- [GitHub Pages deployment](https://github.com/kishibashi3/publications/actions/runs/35506196582)
- [merged reader-facing chapter](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)

さらにPR #58では、receiver側reviewerが#57でmergeされた条件と別の規範文書のD4/D7が衝突することを見つけ、D8「自己権限の固定」を別文書へ追加するよう提案しました。writerが採用し、再reviewでLGTMとなった後、#58もmergeされました。

- [#58 reviewer carry into D8](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749116909)
- [D8 implementation commit](https://github.com/kishibashi3/publications/commit/e524c71d9f01045f4c8dac60a8ee8bb45a3198c4)
- [#58 re-review](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749456249)
- [#58 merge commit `36e4c5df`](https://github.com/kishibashi3/publications/commit/36e4c5df963e2b3645c7591d8cb933c4f36e48e0)

**公開記録から確認できること:** origin-preserved review → third-party restatement → 専用reader-facing本文実装 → merge / Pages反映 → 同じreceiver内の別文書で整合条件として再利用 → merge。  
**まだ確認できないこと:** #58を別のpublic-site publicationとして数えること、別receiverによる独立carry、大規模読者反応、広範な人間認知、理論体系全体への支持。

---

## 18. PostHog｜反復agentの「要約承認」と、実際に繰り返し実行されるinstructionsを分ける

**対象:** [PostHog/posthog#101991](https://github.com/PostHog/posthog/pull/101991)  
**現在状態:** open / unmerged

このPRでは、会話から「毎週実行するscout」などの反復agentを作成できます。初期実装では、card上に名前・短い説明・cadence・送信先は表示される一方、実際に毎回実行されるmodel-authored `scout.body` は人間に表示・編集されないままcreate payloadへ入っていました。

`Nakagawa-master` のreviewは、次の境界を提示しました。

```text
approval of a summary
!=
approval of hidden recurring instructions
```

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/101991#pullrequestreview-5235367516)

その後、第三者authorのcommit `244ff417` は、scheduled agentが「user never saw」instructionsから作られていたことをcommit本文で明示し、card上に実際のinstructionsを表示・編集できるfieldを追加しました。create時には、draftされた隠れたbodyではなく、人間が確認・編集した `scoutBody` を送るよう変更され、regression testも追加されています。

- [implementation commit `244ff417`](https://github.com/PostHog/posthog/commit/244ff417b3b5228779a8b904035a881bc05cdff5)

このcommit本文も `Nakagawa-master` reviewを唯一原因として明示していません。そのため、確認できる範囲は「review後に、指摘された同じ承認境界へ対応する第三者実装が入った」までです。

**公開記録から確認できること:** review → 第三者code / UI / test変更。人間が見るinstructionsと、実際に反復実行へ渡すinstructionsが同じreviewed valueへbindされるようになったこと。  
**まだ確認できないこと:** merge、release、production deployment、利用者規模、変更の唯一因果。

---

## 19. DAIR Prompt Engineering Guide｜「content classification」と「action authority」を分離する

**対象:** [dair-ai/Prompt-Engineering-Guide#757](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757)  
**現在状態:** open / unmerged、第三者author実装commitあり

このPRは、投稿やコメントを分類し、その分類から「comment / react / skip」などの下流actionを選ぶreader-facing teaching pageを追加するものです。

`Nakagawa-master` のreviewは二つの境界を指摘しました。

```text
untrusted content
!=
instructions the classifier should obey

content classification
!=
current authorization to perform the downstream action
```

- [Nakagawa-master review](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757#pullrequestreview-5280350258)

第三者authorは公開thread上で両方の指摘を認め、follow-up commit `4a5334a` をpushしました。さらにcommit message自体が **“Two hardenings from @Nakagawa-master's review on #757.”** と起点を明示しています。

- [third-party author response](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757#issuecomment-5783121174)
- [implementation commit `4a5334ab`](https://github.com/dair-ai/Prompt-Engineering-Guide/commit/4a5334ab0ea82e97c122d53a78a6162d8e56e6b9)

commitは、interpolated fieldsをuntrusted dataとして区切る変更と、classificationからaction authorityを分離するsecond-stage gate / regression caseを追加しています。

このcaseでは、単に「review後に似た変更が起きた」のではなく、**receiver側のcommitが具体的な2変更を `@Nakagawa-master` review由来として明示**しています。ただし、これはこの具体的teaching artifactの変更に関する因果証拠であり、一般原理の知的優先権や理論体系全体の採用を意味しません。

**公開記録から確認できること:** review → third-party authorの明示的同意・再説明 → `@Nakagawa-master` reviewを起点として明記したimplementation commit → reader-facing teaching artifactの具体的変更。  
**まだ確認できないこと:** PRのmerge、release / deployment、読者規模、一般原理の発明者性、理論体系全体への支持。

---

## 20. TourCRM｜現在の参加資格で過去の出席事実を書き換えない

**対象:** [Alan8893/tourcrm#97](https://github.com/Alan8893/tourcrm/pull/97) → [PR #101](https://github.com/Alan8893/tourcrm/pull/101)  
**現在状態:** #97 merged / #101 merged

PR #97では、終了済みoccurrenceのAttendance row自体は残る一方、read / correction経路が「現在もparticipantか」を見るため、参加終了後に過去の出席記録が一覧・集計から消え、historical correctionもできなくなる境界が残っていました。

`Nakagawa-master` のcommentは、

```text
current roster
!=
historical occurrence roster
```

を明示し、終了後のcurrent membershipではなく、そのoccurrenceが起きた時間窓におけるparticipationで過去のroster / denominator / correction authorityを判定するよう提案しました。

- [Nakagawa-master comment on #97](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)

receiver側のcommit `b6da0eb8` は `has_participation()` と `list_attendance()` を `now()` 基準からoccurrence自身の `[starts_at, ends_at)` window基準へ変更し、commit messageで **“Addresses PR #97 review feedback (Nakagawa-master).”** と明記しています。

- [implementation commit `b6da0eb8`](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6)

その後のPR #101では、この修正を証明するため追加されたregression自体がfuture fixtureとreal wall clockの関係次第で旧実装でも通り得ることを `Nakagawa-master` が指摘しました。

- [Nakagawa-master regression-evidence comment on #101](https://github.com/Alan8893/tourcrm/pull/101#issuecomment-5691884921)

receiverは `_PAST_START` を導入してold `now()` predicateとoccurrence-overlap predicateが常に逆の結果になるようにし、旧実装へ一時的に戻した場合に3本のregressionがすべて失敗することまで確認しました。commit `568c8fec` も **“Addresses PR #101 review feedback (Nakagawa-master).”** と明記しています。

- [test-evidence commit `568c8fec`](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5)
- [Nakagawa-master re-review confirming the wall-clock weakness is resolved](https://github.com/Alan8893/tourcrm/pull/101#pullrequestreview-5219832326)

両PRはmerge済みです。このcaseでは、具体的な実装修正と、その修正を証明するregressionの強化の両方について、receiver側commitが `Nakagawa-master` review feedbackを明示しています。

**公開記録から確認できること:** historical-state boundaryの指摘 → receiverが実装変更をreview feedback由来として明記 → regression evidenceの弱点を追加指摘 → receiverがtest設計を修正し同じくreview feedback由来と明記 → merge。  
**まだ確認できないこと:** production deployment、利用者規模、一般的なtemporal-data原理の知的優先権、理論体系全体への支持。

---

## 21. MemberJunction｜export aliasの存在を「外部から触れない宣言」と誤認しない

**対象:** [MemberJunction/MJ#4487](https://github.com/MemberJunction/MJ/pull/4487)  
**現在状態:** merged（2026-09-24）

PR #4487は、大規模なTypeScript naming-conventions gateを導入し、外部consumerから安全にrenameできるmemberを自動判定・修正する変更です。

`Nakagawa-master` のreviewは、named re-exportでaliasだけをpublic-symbol setへ記録すると、宣言元のtype名が「非公開」と誤判定され得ることを指摘しました。

```ts
export { ChatParams as PublicChatParams } from "./shape.js"
```

この場合、外部consumerは `PublicChatParams` 経由で `ChatParams` のmemberを利用できます。しかしfinding側が宣言名 `ChatParams` を持つ一方、collector側がalias `PublicChatParams` しか保持しなければ、そのmemberをsafe-to-renameな `error` と誤分類し、runtime stubを作れないinterface memberを破壊し得ます。

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5219601735)

別の第三者reviewerは後にこのfindingを独立して再確認し、**“The aliased re-export hole Nakagawa-master reported on 2026-09-16 is still open.”** と明記しました。

- [independent reviewer confirmation](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5241419422)

receiver commit `dfd4588d` は、export aliasとsource declaration nameの両方をpublic-symbol setへ記録するよう修正し、alias経由で公開されたdata shapeは `warn` のまま、同じfileにあるがre-exportされていないsibling typeは `error` のままであることをregression testで固定しました。commit message自体が **“Reported by Nakagawa-master on 2026-09-16.”** とsource relationを明示しています。

- [implementation commit `dfd4588d`](https://github.com/MemberJunction/MJ/commit/dfd4588d798b68b982f2554295a0d4d3afb005c2)
- [Nakagawa-master focused re-check](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5252973190)

後続reviewでもこのfindingの修正が確認され、PR #4487は2026-09-24にmergeされました。

**公開記録から確認できること:** Nakagawa review → 別第三者reviewerによる同じholeの独立再確認 → receiver commitが `Reported by Nakagawa-master` と明示してcode/testを修正 → focused re-check → 後続reviewで修正確認 → merge。  
**まだ確認できないこと:** `@memberjunction/standards` の別repoでの実利用規模、この具体的fixのrelease / downstream adoption、一般的なAPI互換性原理の知的優先権、理論体系全体への支持。

---

## このページから言えること／言えないこと

### 公開記録から確認できること

複数の独立したGitHub repositoryで、`Nakagawa-master` 名義の具体的なコメントやreviewに対して、第三者が次のいずれかを行った公開記録があります。

- 内容を明示的に確認・再説明した
- code / tests / documentation / UIを変更した
- source relationをPR本文やcommitで明示した
- merge、backport、release、deploymentまで進んだ
- 別のreviewerまたは別のPRで同じ区別を再利用した

どの事例がどこまで進んでいるかは、各節に個別に記載しています。

### このページだけでは言えないこと

- 中川マスターの理論体系全体が正しいこと
- 各第三者projectが理論体系全体を支持・採用していること
- ここにないprojectや業界全体への影響
- 公開記録がない利用者数、売上、社会的効果
- open / draft PRについて、将来mergeされること
- merge済み変更について、release / deployment /利用が確認できない場合の実運用効果

このページは、確認できる範囲を超えて推測しません。

## 自分で確認する方法

事例を検証するときは、次の順にリンクを確認してください。

1. `Nakagawa-master` の元comment / reviewを開く
2. third-party author / owner / reviewerの応答を確認する
3. PR diff、commit、test変更を確認する
4. merge済みかどうかをPR stateで確認する
5. releaseやdeploymentを主張する場合は、release pageやdeploy記録を別に確認する
6. source relationが明示されていない変更は、このページだけを根拠に因果関係を推定しない

反証可能性を残すため、counterexampleや「この事例では適用できない」という結果も重要です。

## 関連する公開資料

- [中川マスターとは｜この公開アーカイブで確認できること](ABOUT_NAKAGAWA_MASTER.md)
- [Start Here](START_HERE.md)
- [実際の問題に使う｜Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [中川構造OS — Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [公開registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [公開対話入口｜実際の問題から始める](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

このページは、名前や件数だけで評価を求めるためのページではありません。**元の公開コメント、第三者側の応答、実際の変更、現在のrepository状態を読者自身が確認するための案内です。**
