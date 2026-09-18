# 公開記録で確認できる外部実装事例｜中川マスターの公開コメント後に第三者プロジェクトで確認された変更

言語: **日本語** | [English](REAL_WORLD_IMPACT.en.md) | [中文](REAL_WORLD_IMPACT.zh.md)

**最終確認: 2026-09-18**

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
**現在状態:** open / draft / unmerged

PostHogのworkflow scoutは、AIがworkflow改善案と数値的なevidenceを人に提示する仕組みです。

`Nakagawa-master` のreviewは、producer / scoutが送った数値と、実際のworkflow・version・stepからPostHog側が測定した数値を同一視しないよう指摘しました。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)

その後、PR authorはserver側で対象stepのmetricを読み直し、producer由来の値とは別に保持する実装・テスト・表示変更を追加しました。UIでは `Measured by PostHog` と `Unverified` を区別し、producerの値とPostHog側の値が異なる場合も、その差を表示する設計になっています。

**公開記録から確認できること:** review後に第三者authorがcode / tests / UIを変更したこと。  
**まだ確認できないこと:** このPRのmerge、release、production deployment、利用者数。

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

**公開記録から確認できること:** 別の第三者reviewerがNakagawa-masterの指摘を名前付きで参照し、自分の検証結果とともにformal reviewへ取り込んだこと。  
**まだ確認できないこと:** そのreview後のauthor実装、merge、release。

---

## 6. PostHog｜推薦理由の文章と、その理由のsourceを混ぜない

**対象:** [PostHog/posthog#102550](https://github.com/PostHog/posthog/pull/102550) → [#102686](https://github.com/PostHog/posthog/pull/102686)  
**現在状態:** #102550 merged / deployed、#102686 open / unmerged

PostHogのreviewer推薦UIでは、同じ説明文を持つreviewerをgroup化すると、`Code history` と `Added by scout` のような異なるsourceが一つに見える可能性がありました。

`Nakagawa-master` のreviewは、説明文が同じことと、推薦根拠のsourceが同じことを分けるよう指摘しました。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

第三者maintainerはsource categoryをgroup keyへ含めるcode / tests / UI story変更を追加し、#102550は`master`へmergeされました。PostHogのdeploy status commentではdev / prod-us / prod-euへのdeploymentも記録されています。

- [merged PR #102550](https://github.com/PostHog/posthog/pull/102550)
- [deploy status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557)

その後、同じmaintainerが別のUI surfaceを扱う#102686でも、同じreasonであってもsource categoryが異なる場合は分ける設計を使っています。#102686は現時点でopenです。

**公開記録から確認できること:** review → code / tests / UI change → merge → deployment。さらに別PRで同じ設計区別が再利用されていること。  
**まだ確認できないこと:** #102686のmerge、実際の利用者数や利用結果。

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
