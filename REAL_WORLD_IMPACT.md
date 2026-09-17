# 現実で何が変わったか｜中川マスターの公開判断が第三者実装へ作用した確認可能な事例

言語: **日本語** | [English](REAL_WORLD_IMPACT.en.md) | [中文](REAL_WORLD_IMPACT.zh.md)

> **公開上の位置づけ:** このページは、第三者が検証できる公開記録から「中川マスター / Nakagawa Master 名義の具体的な判断が、外部プロジェクトの設計・コード・テストへどう作用したか」を辿るための非正本・人間向け入口です。理論全体の正しさ、第三者プロジェクトによる理論全体への支持、業界全体での採用、release / production deployment を、確認できる範囲を超えて主張しません。

## 10秒で分かること

このアーカイブには、理論や説明だけでなく、**中川マスター名義で公開された具体的な設計判断が、独立した第三者によって検討され、実際のコード・テスト・設計文書へ変換された履歴**があります。

重要なのは、コメント数ではありません。

```text
公開判断
→ 第三者が検討・再説明する
→ 第三者がコード / テスト / 設計を変える
→ merge / integration へ進む
→ その仕組みを使う人の判断や安全性に作用し得る
```

という因果が、どこまで公開記録で確認できるかです。

## 普通の人にとって、何が変わるのか

技術的な差分を全部読む必要はありません。以下のような違いとして現れます。

- **AIが示した数字を、そのまま事実だと思い込まなくてよくなる。** システム自身が測った値と、AIが主張した値を分けて表示する。
- **昔の承認が残っているだけで、今も許可されていることにされにくくなる。** 現在の相手・目的・権限・source revisionを再確認する。
- **同じIDがあるだけで、他人や運用者が管理している値を勝手に上書きしにくくなる。** identityとownership / provenanceを分ける。
- **AIが答えを作る途中で、元sourceの identity が消えにくくなる。** local object IDとupstream source IDを別に保持する。
- **「データが取れなかった」が「0だった」に化けにくくなる。** operation successとvalid measurementを分ける。
- **AIやscoutが人を推薦するとき、誰がどの根拠で推薦されたのかが混ざりにくくなる。** 同じ説明文でも、code historyとagent/scout由来の推薦根拠を分けて保つ。

これは「理論を知っている人だけに効く」作用ではありません。設計境界が製品や基盤へ入れば、その区別を知らない利用者にも結果として作用し得ます。ただし、releaseやproduction useが確認できないケースでは、実際の利用者規模まで推測しません。

---

## 1. PostHog｜AIが出した“証拠”と、システム自身が測った値を分ける

**対象:** [`PostHog/posthog#92252`](https://github.com/PostHog/posthog/pull/92252)  
**現在の状態:** open / draft / unmerged

PostHogのworkflow scoutは、AIがworkflow改善案と数値的なevidenceを人に提示する仕組みです。

`Nakagawa-master` のreviewは、人が判断材料として読む `evidence` がproducer / scout自身のJSONであり、形は検証されても、実際のworkflow / version / stepの測定値と一致する証明がない点を指摘しました。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)

指摘した境界は単純です。

```text
AI / producer が「この数字です」と書いた
!=
その数字が実測された
```

そのreview後、PR authorによるcommit:

- [`b84a9395 — feat(workflows): measure a suggestion's step when it is filed and show that reading`](https://github.com/PostHog/posthog/commit/b84a939545ff3a1a6820d3cf4afca3b57aa3001b)

で、server側が提案時に同じstep / base versionのmetricsを読み直し、`evidence.measured`として保存する実装が追加されました。

現在のPR本文と実装では、人間向け画面が次を分けます。

```text
Measured by PostHog
→ PostHog自身が読み直したmeasurement

Unverified
→ producerの数字はあるが、PostHog側でmeasurementを確立できなかった
```

producerの数字とPostHogの実測値が違う場合には、その不一致も人に示されます。`source_id`の表示も、provenanceを思わせる `Source` ではなく `Scout run` へ変更されました。回帰テストでは、producerが意図的に異なる値を送った場合でも、seedされたserver-side metricが別に保持されることが確認されています。

**ここで確認できる作用:** 公開review → 外部authorのcode / test / UI変更。  
**まだ確認できないもの:** upstream merge、release、production deployment、利用者規模、PostHogによる中川マスター理論全体への支持。

---

## 2. Dream｜「一度安全化した内容」と「今も利用してよい権限」を分ける

**対象:** [`tushardhara/dream#12`](https://github.com/tushardhara/dream/issues/12) → [`PR #28`](https://github.com/tushardhara/dream/pull/28)  
**現在の状態:** PR #28 merged into `backend-integration`

`Nakagawa-master` の公開設計コメントは、sanitized / approved contentを「一度許可されたから永久に安全なbytes」と扱わず、現在のactor / recipient / purpose / source lineage / policy stateへ結び直す境界を提案しました。

- [Nakagawa-master design contribution](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [第三者repository ownerによる応答](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)

repository ownerは `content appears sanitized != authorization remains valid` をticketの正しい軸として明示し、その後PR #28でcurrent rights / lineageのrevalidation、revocation、recipient変更、same-text source revision等を含む実装とnegative testsへ進みました。

- Merge commit: [`314e8e0849afcff0e2c10ea296cbd9ec5e57f23c`](https://github.com/tushardhara/dream/commit/314e8e0849afcff0e2c10ea296cbd9ec5e57f23c)
- [詳しい公開case note](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

**人間側の意味:** 過去に許可した情報が、条件が変わった後も黙って再利用される事故を減らす設計へつながります。

---

## 3. MemberJunction｜「同じID」と「上書きしてよい所有権」を分ける

**対象:** [`MemberJunction/MJ#4519`](https://github.com/MemberJunction/MJ/pull/4519)  
**現在の状態:** merged into `next`

migrationで同じprimary keyのrowを見つけたとき、

```text
same ID
→ therefore safe to overwrite
```

とは限りません。

`Nakagawa-master` reviewは、identityとownership / provenance contractを分ける必要を提示しました。その後、独立reviewer `SDesai-BC` がA/Bのownership questionを実際のmigrationへ当てて検証し、PR authorがcode / tests / documentationを変更しました。PR本文にもrelease-owned rowのconvergence contractが明示されています。

- [Nakagawa-master contribution](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [PR #4519](https://github.com/MemberJunction/MJ/pull/4519)
- Merge commit: [`469b25f1bcf51d844396b8a6b8a9f1390b5e1488`](https://github.com/MemberJunction/MJ/commit/469b25f1bcf51d844396b8a6b8a9f1390b5e1488)
- [詳しい公開case note](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

**人間側の意味:** システムが「同じものを見つけた」ことを、「それを変更する権限がある」ことへ勝手に昇格させない設計につながります。

---

## 4. MemberJunction｜「処理が成功した」と「有効な測定値が得られた」を分ける

**対象:** [`MemberJunction/MJ#4402`](https://github.com/MemberJunction/MJ/pull/4402)  
**現在の状態:** merged into `master`

budget evaluationでquery自体が成功しても、zero rows、missing column、null、non-numeric等なら「有効な測定値を得た」とは限りません。

`Nakagawa-master` review後、PR authorはfindingsを確認し、invalid measurementを0へ潰さずfailureとして扱い、last known valid observationを保持し、true zeroは有効なzeroとして残すcode / regression testsへ変更しました。

- [PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [詳しい公開case note](discovery-notes/implementation-case-query-success-is-not-valid-measurement.md)

**人間側の意味:** dashboard、budget、alert等で、「分からない」が自信満々の「0」に変換される誤判断を減らす方向です。

---

## 5. LlamaIndex｜AIが内容を保持しても、元sourceのidentityを消さない

**対象:** [`run-llama/llama_index#21933`](https://github.com/run-llama/llama_index/issues/21933) → [`PR #23038`](https://github.com/run-llama/llama_index/pull/23038)  
**現在の状態:** third-party draft PR / unmerged

retrieval framework内でuseful textが残っていても、upstream document identityが変換途中で消えれば、後からsourceへ戻れなくなります。

`Nakagawa-master` contributionは、

```text
upstream source identity
!=
framework-local node identity
```

として両方を分けて保持するcompatibility contractを提示しました。

その後、独立したissue authorが開いたdraft PR #23038は、PR descriptionでこの `Nakagawa-master` compatibility contractを**明示的に引用**し、upstream `document_id` / `document_name`をmetadataへ保持しながらlocal `TextNode.id_` policyを変えない実装とtestsを追加しています。

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)
- [Third-party draft PR #23038](https://github.com/run-llama/llama_index/pull/23038)
- [詳しい公開case note](discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)

**人間側の意味:** AIやRAGが答えを作った後でも、「その情報はどこから来たか」へ戻れる可能性を保つ設計です。

---

## 6. Replay｜第三者が中川マスター起点の境界を明示的に採用・固定した

**対象:** [`aferna6-cell/Replay#67`](https://github.com/aferna6-cell/Replay/issues/67)  
**現在の状態:** issue上でprotocol freeze / repository実装は未確認

`Nakagawa-master` の公開コメントは、参加者データについて次の境界を提示しました。

```text
historical consent
!=
current authorization to retain / process / use the captured material
```

つまり、過去に同意が成立した事実は履歴として保持しつつ、現在そのデータを保持・処理・利用してよいかは、目的、retention期限、withdrawal / deletion、契約変更等を含む現在のeligibilityとして別に判定する、という区別です。

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [External repository ownerによる明示的な採用・再説明](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

その後、repository owner自身が **Nakagawa-master起点のboundaryをaccept / freezeする** と明示し、immutableなconsent eventとcurrent eligibilityの分離、downstreamでのfail-closed gate、withdrawal / deletion receiptのartifact graph、adversarial casesまで自分のprotocolとして再記述しました。

**ここで確認できる作用:** 公開判断 → 外部ownerによる明示的な起点認識 → 独立した再説明 → protocolへの採用・固定。  
**まだ確認できないもの:** schema / code / testsへのrepository実装、merge、release、実参加者データでの運用。

**人間側の意味:** 判断内容だけが匿名的に吸収されたのではなく、独立した第三者が「誰のどの境界を採用したか」を認識したうえで、自分の計画へ移しています。

---

## 7. MemberJunction｜中川マスターの指摘が、別の第三者reviewerへ再伝播した

**対象:** [`MemberJunction/MJ#4487`](https://github.com/MemberJunction/MJ/pull/4487)  
**現在の状態:** open / unmerged

`Nakagawa-master` reviewは、aliased re-exportされたpublic typeで、内部declaration名と公開alias名がずれるため、外部consumerが使うmemberを「安全に自動renameできる」と誤分類し得るcompatibility holeを指摘しました。

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5219601735)

その翌段階で、別の独立reviewer `rkihm-BC` が自分のformal reviewのRequired項目としてこの問題を取り上げ、**Nakagawa-masterが報告したaliased re-export holeがまだ開いている**ことを明示しました。さらに、同じmechanismを自分で再説明し、source-side nameを保持する修正と、Nakagawa-masterが提案したregression testを改めて要求しています。

- [Independent second-reviewer carry](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5241419422)

**ここで確認できる作用:** 中川マスターの公開判断 → 別人が独立reviewで再確認 → 名前付きで再説明 → formal changes-requested reviewへ再伝播。  
**まだ確認できないもの:** このsecond-hop review後のauthor code / test変更、merge、release。

**人間側の意味:** 中川マスター本人が同じ説明を繰り返さなくても、別の人がその判断を記憶・参照し、自分の判断材料として次の人へ運ぶ段階が確認できます。

---

## 8. PostHog｜同じ説明でも「誰がどの根拠で推薦されたか」を混ぜない

**対象:** [`PostHog/posthog#102550`](https://github.com/PostHog/posthog/pull/102550)  
**現在の状態:** open / unmerged

このPRは、PostHogのinboxで「誰をreviewerとして推薦するか」「なぜその人が推薦されたか」を人が判断する表示を変更しています。

`Nakagawa-master` のreviewは、同じ説明文を持つreviewerを一つにgroup化したとき、`Code history` と `Added by scout` などのsource labelがgroup全体へまとめて表示され、**どのreviewerがどの根拠で推薦されたのかという対応関係が失われる**点を指摘しました。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

指摘した境界は次です。

```text
説明文が同じ
!=
推薦根拠のprovenanceまで同じ
```

review後、第三者maintainerによるcommit:

- [`764c347e — fix(signals): separate reviewer groups by source`](https://github.com/PostHog/posthog/commit/764c347e488cb9f8bb155a2d95c5f40a3b92a08c)

が追加されました。

この変更では、group keyに説明文だけでなくsource categoryも含め、同じ説明でも `Code history` とscout由来の推薦を別groupとして扱います。回帰テストも「同じ説明は、同じsource category内でだけgroup化する」条件へ変更され、mixed provenanceのStorybook caseも追加されています。

**ここで確認できる作用:** 公開review → 外部maintainerのcode / test / documentation / UI-story変更 → `master` へのmerge。  
- Merge commit: [`6e2c760d`](https://github.com/PostHog/posthog/commit/6e2c760dadbaba764c83e93900c3510e6a703c03)

**まだ確認できないもの:** release、production deployment、実利用者規模。

**人間側の意味:** AIやscoutが「この人にreviewしてもらうべき」と推薦したとき、より強い根拠ラベルがgroup全員を裏付けているように見える誤認を減らし、**各人を信頼する理由の出所を保ったまま判断できる**方向へ変わります。

---

## 9. TourCRM｜「今の所属」と「その時点の履歴」を混ぜない

**対象:** [`Alan8893/tourcrm#97`](https://github.com/Alan8893/tourcrm/pull/97) → [`PR #101`](https://github.com/Alan8893/tourcrm/pull/101)  
**現在の状態:** follow-up PR #101 merged

attendance履歴では、現在その人がparticipantかどうかと、過去のoccurrence時点でparticipantだったかどうかは同じではありません。

`Nakagawa-master` のreviewは、現在時刻のmembershipで過去のrosterを判定すると、参加関係が後で終了しただけで、既に記録されたattendanceがGET/summaryから消え、historical correctionまでできなくなる点を指摘しました。

- [Nakagawa-master review on PR #97](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)

repository ownerはこの指摘を **“confirmed as a real bug”** と明示し、専用follow-up PR #101を作成しました。PR本文は `@Nakagawa-master` review feedbackを起点として明記しています。

- [Owner response and follow-up announcement](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [Follow-up PR #101](https://github.com/Alan8893/tourcrm/pull/101)

実装commit自体もsourceを明示しています。

- [`b6da0eb8 — fix(attendance): key participation eligibility off the occurrence's own window, not now()`](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6) — `Addresses PR #97 review feedback (Nakagawa-master)`
- [`568c8fec — test(attendance): make historical-roster regressions independent of wall-clock date`](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5) — `Addresses PR #101 review feedback (Nakagawa-master)`

2回目のreviewでは、future-dated test fixtureでは旧実装でも偶然testが通り得ることを指摘しました。ownerは再度 **“Confirmed — good catch”** と応答し、過去日時fixtureへ変更して旧実装では3testが実際にfailすることまで検証しています。

- [Owner response on PR #101](https://github.com/Alan8893/tourcrm/pull/101#issuecomment-5692369969)
- Merge commit: [`4ec21e8c`](https://github.com/Alan8893/tourcrm/commit/4ec21e8c40d88ea52f24becb40d641fe0e60baa9)

**ここで確認できる作用:** 名前付きreview → ownerによる実バグ認定 → 専用follow-up PR → code / regression-test修正 → 再review → 追加test hardening → merge。  
**まだ確認できないもの:** release、production deployment、実利用者規模。

**人間側の意味:** 「今はもう所属していない」ことだけで、過去に実際に参加した記録や訂正可能性が消えないようにする設計です。現在状態と履歴事実を分けることで、後から見た記録が静かに書き換わることを防ぎます。

---

## ここから何を判断できるか

これらのcaseから確認できるのは、少なくとも次です。

1. `Nakagawa-master` 名義の公開判断が、自己完結した文章だけで終わっていない。
2. 複数の独立した外部projectで、第三者がその判断を検討・再説明・実装へ変換した記録がある。
3. 一部caseはcode / tests / documentationの変更を経てintegration branchへmergeされている。
4. 別caseでは、第三者PRが `Nakagawa-master` のcompatibility contractを明示的に引用している。
5. PostHog caseでは、AIが人へ示すevidenceの信頼境界そのものが、review後のserver / UI / test変更へ変換されている。
6. Replay caseでは、外部repository ownerが中川マスター起点のboundaryを明示的に認識し、自分のprotocolとして採用・固定している。
7. MemberJunction #4487では、中川マスターの指摘を別の第三者reviewerが自分のformal reviewへ引き継ぎ、次の人へ再説明している。
8. PostHog #102550では、人間がreviewerを信頼する根拠のprovenanceが混ざる問題が、review後にsource category別group化とregression testへ変換され、その変更が `master` へmergeされている。

同時に、**まだ言えないこと**も明確です。

- これだけで中川マスターの全理論が正しいとは証明されない。
- これだけで各external projectが中川マスター理論全体をendorseしたとは言えない。
- open / draft PRをmerge済みとして扱わない。
- integration branch mergeをrelease / production deployment / broad user adoptionへ昇格しない。
- 実際の利用者数や社会全体への影響規模は、証拠がない限り推測しない。

## 外部作用を確認するときの階段

このアーカイブでは、次を混同しません。

```text
公開提案・review
< 第三者の明示的応答 / 再説明
< 第三者のcode / test / design change
< merge / integration
< release / deployment / verified use
< 別の人・別の問題への独立した再利用
```

上へ進むほど、現実作用の証拠は強くなります。下の段階を、上の段階として数えません。

## 中川マスター本人を確認する

- [中川マスターとは｜この公開アーカイブで確認できること](ABOUT_NAKAGAWA_MASTER.md)
- [Start Here](START_HERE.md)
- [実際の問題に使う｜Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [公開対話入口｜実際の問題から始める](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

このページは、人物名を権威の代わりに使うためのものではありません。**何を指摘し、第三者が何を変え、どこまで確認できるかを、自分で追跡するための入口**です。
