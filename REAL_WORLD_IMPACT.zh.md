# 可由公开记录核验的外部实现案例｜中川大师公开评论之后第三方项目中可确认的变化

语言: [日本語](REAL_WORLD_IMPACT.md) | [English](REAL_WORLD_IMPACT.en.md) | **中文**

**最后确认：2026-09-23**

中川大师（Nakagawa Master）是Keisuke Nakagawa的笔名。在社交媒体上也使用“マスター（Master）”，部分外部投稿使用“MasterJP”名义。

本页是一个**公开核验指南**。它把 `Nakagawa-master` 账号在GitHub上的公开comment / review，与之后第三方repository中可以独立检查的变化对应起来。

本页不是影响力评分，也不是权威声明，更不表示某个第三方项目整体采用了中川大师的理论体系。每个案例尽量分为四部分：

1. 原始公开comment / review；
2. 第三方的回应、实现或测试变化；
3. 当前repository状态；
4. 仍未被公开证据确认的范围。

有评论，不等于已经实现；已经实现，不等于已经merge；已经merge，也不自动等于release、deployment或真实使用。

## 对普通用户来说，这些区分可能意味着什么

以下案例涉及的产品行为包括：

- 区分AI提供的数字与系统自身测量的数字；
- 区分过去曾批准与现在仍有授权；
- 区分ID相同与有权覆盖现有数据；
- 区分local runtime identity与upstream source identity；
- 区分执行成功与得到有效测量值；
- 保留每个推荐对象真正对应的证据来源；
- 区分当前成员状态与历史参与事实；
- 区分一次approval与一次外部side effect。

下面只描述公开记录可以直接确认的部分。

---

## 1. PostHog｜把producer提供的evidence与PostHog自身测量分开

**对象：** [PostHog/posthog#92252](https://github.com/PostHog/posthog/pull/92252)  
**当前状态：** open / draft / unmerged

`Nakagawa-master` 的review指出，producer自己写入的evidence不应被直接展示成系统独立测量的事实。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)

之后，PR author加入了server-side measurement、回归测试以及 `Measured by PostHog` / `Unverified` 等UI区分。

**公开可确认：** review之后，第三方author修改了code / tests / UI。  
**尚未确认：** merge、release、production deployment、用户规模。

---

## 2. Dream｜把“曾被安全化”与“当前仍有权限使用”分开

**对象：** [tushardhara/dream#12](https://github.com/tushardhara/dream/issues/12) → [PR #28](https://github.com/tushardhara/dream/pull/28)  
**当前状态：** PR #28 merged

公开comment提出：内容曾经被sanitized / approved，并不意味着在actor、recipient、purpose、source lineage或policy发生变化后仍然自动有权继续使用。

- [Nakagawa-master design contribution](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [repository owner response](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)
- [merged PR #28](https://github.com/tushardhara/dream/pull/28)
- [公开case note](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

repository owner明确接受了这一设计区分，后续PR加入current rights / lineage revalidation、revocation相关处理和negative tests。

**公开可确认：** comment → owner回应 → code / tests → merge。  
**尚未确认：** 用户规模，以及该项目之外的广泛采用。

---

## 3. MemberJunction｜把“ID相同”与“有权覆盖”分开

**对象：** [MemberJunction/MJ#4519](https://github.com/MemberJunction/MJ/pull/4519) → [#4496](https://github.com/MemberJunction/MJ/pull/4496) → [#4546](https://github.com/MemberJunction/MJ/pull/4546) → [v6.1.2](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2)  
**当前状态：** merged → LTS backport merged → v6.1.2 released

primary key相同，并不能单独证明migration拥有该row或可以覆盖它。

- [Nakagawa-master contribution](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [PR #4519](https://github.com/MemberJunction/MJ/pull/4519)
- [公开case note](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

公开记录显示：之后有独立review、author对code / tests / documentation的修改、merge、generated migration、LTS backport，以及v6.1.2 release。

MemberJunction的公开certification issue中，还存在一个外部upgrade报告：在包含既有row的database上执行相关migration序列时，没有发生原来的primary-key collision。

- [External 6.1.2 certification report](https://github.com/MemberJunction/MJ/issues/4475#issuecomment-5715684968)

同一份报告也记录了另一个独立regression，因此本页**不**声称v6.1.2整体没有问题。

**公开可确认：** review → 独立确认 → code/tests/docs → merge → backport → release → 针对相关collision条件的外部upgrade report。  
**尚未确认：** 所有部署环境中的结果、用户规模或市场范围。

---

## 4. LlamaIndex｜把upstream source identity与local node identity分开保存

**对象：** [run-llama/llama_index#21933](https://github.com/run-llama/llama_index/issues/21933) → [PR #23038](https://github.com/run-llama/llama_index/pull/23038)  
**当前状态：** open / draft / unmerged

issue comment区分了framework-local node identity与upstream document identity。

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)
- [third-party PR #23038](https://github.com/run-llama/llama_index/pull/23038)
- [公开case note](discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)

第三方PR明确引用 `Nakagawa-master` 的compatibility contract，并加入保存 `document_id` / `document_name` 的实现与tests，同时不改变local `TextNode.id_` policy。

**公开可确认：** source被明确引用，并进入第三方code / tests。  
**尚未确认：** merge、release、deployment。

---

## 5. MemberJunction｜另一位reviewer独立检查了相同问题

**对象：** [MemberJunction/MJ#4487](https://github.com/MemberJunction/MJ/pull/4487) / [#4524](https://github.com/MemberJunction/MJ/pull/4524)  
**当前状态：** 两个PR均 open / unmerged

在#4487中，`Nakagawa-master` review指出aliased re-export compatibility问题。

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5219601735)

之后，另一位reviewer `rkihm-BC` 在自己的formal review中重新检查并解释了同一问题，同时要求对应修正与regression test。

- [independent reviewer confirmation](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5241419422)

在#4524中，同一reviewer明确写道“@Nakagawa-master's point about D is confirmed”，并把自己的checker结果带入review。

- [confirmation on #4524](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5242805347)

之后，两项PR中的相关修正都进入了author实现。#4487现在同时记录named re-export的alias名与source declaration名，并加入regression tests：aliased published data-shape member保持`warn`，未re-export的sibling保持`error`。Nakagawa-master重新检查current head，并在review `5252973190` 中明确关闭了原始finding。#4524中direct `[__mj]` fail-open也已修正，同一位独立reviewer重新执行probe，确认它从false-pass exit 0变成fail-closed exit 1。

- [#4487 closure review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5252973190)
- [#4524 independent re-verification](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5252195432)

**公开可确认：** 点名独立确认之后又出现author实现/regression tests；#4487还有origin reviewer closure，#4524还有独立执行再验证。  
**尚未确认：** 两个PR的merge与release。

---

## 6. PostHog｜让推荐理由继续绑定真实source

**对象：** [PostHog/posthog#102550](https://github.com/PostHog/posthog/pull/102550) → [#102686](https://github.com/PostHog/posthog/pull/102686)  
**当前状态：** #102550 merged / deployed；#102686 merged / deployed

`Nakagawa-master` review指出，相同的说明文字不应把 `Code history` 与 `Added by scout` 等不同推荐source合并成看起来相同的依据。

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

maintainer修改了grouping logic、tests和UI stories；#102550已merge到`master`。PostHog公开deploy-status comment记录了dev、prod-us和prod-eu deployment。

- [merged PR #102550](https://github.com/PostHog/posthog/pull/102550)
- [deploy status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557)

之后，同一maintainer在#102686的另一个UI surface中也使用了相同的source-category区分。current head得到独立reviewer `stamphog` 的APPROVED review，并于2026-09-18T15:49:22Z merge。PostHog公开deploy-status记录显示它已部署到dev、prod-us与prod-eu。

- [#102686 external approval](https://github.com/PostHog/posthog/pull/102686#pullrequestreview-5249196997)
- [merged PR #102686](https://github.com/PostHog/posthog/pull/102686)
- [#102686 deploy status](https://github.com/PostHog/posthog/pull/102686#issuecomment-5732760371)

**公开可确认：** 最初的review → code/tests/UI change → merge → deployment；之后相同区分在另一PR中被再次使用，并进一步经过独立approval → merge → dev/prod-us/prod-eu deployment。  
**尚未确认：** 实际用户规模/结果，以及由不同person或不同context进行的进一步reuse。

---

## 7. TourCRM｜把当前membership与历史参与事实分开

**对象：** [Alan8893/tourcrm#97](https://github.com/Alan8893/tourcrm/pull/97) → [PR #101](https://github.com/Alan8893/tourcrm/pull/101)  
**当前状态：** follow-up PR #101 merged

review指出：历史attendance应按occurrence本身的参与时间窗口判断，而不是只按现在是否仍然是member判断。

- [Nakagawa-master review](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)
- [owner response](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [follow-up PR #101](https://github.com/Alan8893/tourcrm/pull/101)

owner把它明确描述为real bug，创建专门follow-up，修改code/tests；之后又根据追加review强化了test fixture，使旧实现会真实失败，最终#101 merge。

**公开可确认：** review → owner确认 → follow-up PR → code/tests → test hardening → merge。  
**尚未确认：** release、production deployment、用户规模。

---

## 8. Clientverse｜把一次approval与一次外部side effect分开

**对象：** [ebyron357/Clientverse-crm#27](https://github.com/ebyron357/Clientverse-crm/pull/27)  
**当前状态：** merged

如果provider已经接受message，但response丢失，把结果当普通失败可能导致重复发送。

- [Nakagawa-master review](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690360136)
- [owner response](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690677339)
- [merged PR #27](https://github.com/ebyron357/Clientverse-crm/pull/27)

repository owner把它描述为real state-machine defect，并加入 `outcome_unknown`、reconciliation、dispatch idempotency与response-loss regression coverage。

**公开可确认：** review → defect确认 → state-machine/provider-contract/test change → merge。  
**尚未确认：** real provider环境中的production deployment或用户规模。

---

## 9. Replay｜把historical consent record与current eligibility分开

**对象：** [aferna6-cell/Replay#67](https://github.com/aferna6-cell/Replay/issues/67)  
**当前状态：** issue上确认设计方向被接受；repository code实现未确认

公开comment提出：保留historical consent event，同时独立判断当前是否仍可retain / process / use相关材料。

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository owner response](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

repository owner明确指出source，并把这一设计区分重新表述为自己的protocol设计。

**公开可确认：** comment → owner确认与protocol-level采用。  
**尚未确认：** schema/code/tests、merge、release、真实数据运行。

---

## 10. Cline｜在delegation approval时让人看到child agent的能力范围

**对象：** [cline/cline#14225](https://github.com/cline/cline/pull/14225)  
**当前状态：** base PR merged；该提案的follow-up实现未确认

`Nakagawa-master` review提出：人在批准delegation时，应能够理解child agent实际获得的capability set。

- [Nakagawa-master review](https://github.com/cline/cline/pull/14225#pullrequestreview-5242232355)
- [external author response](https://github.com/cline/cline/pull/14225#issuecomment-5723653394)

external author点名 `@Nakagawa-master`，认为这一UX比当前行为更好，并表示计划在后续agent-config工作中考虑。

base PR本身已经merge，但这不表示该提案已经实现。

**公开可确认：** 点名review、author明确回应与follow-up意向。  
**尚未确认：** follow-up issue/PR、code/tests/UI实现、release。

---


## 11. Local Operator｜防止运行中的agent降低自己的approval gate

**对象：** [damianvtran/local-operator#1282](https://github.com/damianvtran/local-operator/issues/1282) → [PR #1291](https://github.com/damianvtran/local-operator/pull/1291) → [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)  
**当前状态：** PR #1291已merge；v0.59.10已于2026-09-19 release并publish

issue #1282提出：如果一个正在被approval policy约束的agent，可以通过自己可写的配置路径把同一个gate从 `ask` 改为 `auto`，它就可能自己解除人类approval；但同时，明确的人类/operator控制路径仍应保留。

- [issue #1282](https://github.com/damianvtran/local-operator/issues/1282)
- [third-party PR #1291](https://github.com/damianvtran/local-operator/pull/1291)

第三方PR #1291在正文中明确写出 `Closes #1282`，并把live approval-policy变化的source纳入判断。另一个process直接修改config不能降低当前gate，而持有gate的process中的明确operator操作仍有positive-control路径。PR还加入了真实second-process写入regression，以及用于防止agent-facing code伪造trusted settings-write路径的tests。

Nakagawa-master重新按原issue的acceptance boundary检查了current head，并在review中明确记录原security finding已被实现。

- [closure review](https://github.com/damianvtran/local-operator/pull/1291#pullrequestreview-5253448083)

随后#1291被merge，并进入公开release `v0.59.10`。release notes明确列出#1291，并把该变化概括为 **“An agent can no longer weaken the approval gate.”** repository owner还在PR thread记录了publish workflow成功、PyPI提供 `0.59.10`、完成安装，以及在repo外执行 `lop --version` 的smoke check。

- [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)
- [release / publish / installed-smoke record](https://github.com/damianvtran/local-operator/pull/1291#issuecomment-5745312290)

**公开可确认：** issue → 明确close该issue的第三方PR → code/tests → 多轮review/remediation → 原issue侧closure review → merge（`b1fc1f42`）→ release notes收录 → package publication → installed smoke。  
**尚未确认：** 更大用户规模下的效果、用户数量，或超出该release的独立downstream reuse。

---


### 后续：同一authority边界继续进入独立的control-plane实现

#1291关闭config-file路径后，`Nakagawa-master` 又把剩余的control-plane边界独立成 [issue #1310](https://github.com/damianvtran/local-operator/issues/1310)：同一OS uid下运行的model-authored subprocess，不应仅凭该uid可读的control credential，就把约束自己的gate从 `ask → auto`，或批准自己被park的approval request。

repository owner独立复现了该问题，并公开记录 **“confirmed, real, and being fixed”**、**“it named the right boundary.”** 独立复现还修正了原诊断：真正可达的sink是 `slash_result` 而不是最初issue所写的 `slash`；同时owner独立发现了更强的兄弟路径 `approval_answer(approved=True)`。

- [owner reproduction / determination](https://github.com/damianvtran/local-operator/issues/1310#issuecomment-5740547291)
- [third-party implementation PR #1324](https://github.com/damianvtran/local-operator/pull/1324)

PR #1324实现per-session operator capability、connection-bound proof、共同pre-dispatch guard，以及明确的negative/positive/tightening controls，并经历多轮独立review、QA、design和UX remediation。对current head `fe2dc9b6`，Nakagawa-master重新核对原issue的5项acceptance条件，并对原#1310边界记录了origin-side closure。该review不是merge建议；PR仍按repository记录等待operator/product decision。

- [origin-side closure review](https://github.com/damianvtran/local-operator/pull/1324#pullrequestreview-5257968951)

**该follow-up公开可确认：** origin issue → 第三方独立复现 → 修正origin诊断 → 独立发现更强sibling bypass → 第三方实现 → 多轮独立remediation → origin-side closure。  
**尚未确认：** #1324 merge/release、OS本身无法隔离same-uid memory的host配置上的保证、phone/device-bound authority完成、或该边界被其他project独立reuse。


## 12. MemberJunction｜在保护row内容之后，把剩余row identity边界继续推进到第二个work item

**对象：** [MemberJunction/MJ#4595](https://github.com/MemberJunction/MJ/pull/4595) → [issue #4610](https://github.com/MemberJunction/MJ/issues/4610)  
**当前状态：** PR #4595 open / unmerged；issue #4610 open

PR #4595默认停止在cache-invalidation broadcast中携带完整row内容。随后 `Nakagawa-master` 的review进一步区分了另一个尚未关闭的边界：即使没有 `recordData`，session仍可能看到其他row的stable primary key与mutation timing。

- [Nakagawa-master row-identity review](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5253531713)
- [Nakagawa-master 两层拆分follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [第三方实现/carry回应](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [follow-up issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

PR author明确采用了这一两层拆分：commit `293b9b40` 实现entity-level permission filter；同时没有通过弱化regression来假装row-level问题已经解决，而是把更强的row-level disclosure问题单独建立为#4610。#4610正文明确说明其framing主要来自 `@Nakagawa-master` 的review，并保留“同一entity权限、但row visibility互相分离”的强acceptance test。

随后在#4610中，又公开给出了把该边界映射到MemberJunction既有ClassFactory扩展机制的具体实现形状，以保持per-subscriber hot path为同步、无I/O。

- [#4610 implementation-shape contribution](https://github.com/MemberJunction/MJ/issues/4610#issuecomment-5739586260)

**公开可确认：** review → 第三方code/test变化 → 第三方明确source attribution → 把更强边界与regression继续carry到第二work item。  
**尚未确认：** row-level policy实现、#4595 merge、#4610关闭/实现、release、deployment或用户规模影响。

---

## 13. Waves Customer Portal｜移除已变得不安全的estimate CTA，同时保留付款凭证

**对象：** [wavespestcontrolfl/waves-customer-portal#4608](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608)  
**当前状态：** merged（2026-09-19）

该PR加入了delivery-time estimate-link guard，以及针对付款receipt的rewrite policy：当estimate CTA已经不应再暴露时，应删除危险CTA，但仍然发送付款凭证本身。

`Nakagawa-master` review发现rewrite路径与refusal guard的link识别词汇不一致。refusal guard会识别这样一种short code：它不是直接属于estimate entity，但其 `target_url` 指向estimate link；而 `rewriteWithheldEstimateLinks()` 当时只rewrite `entity_type='estimates'` 的short code。于是同一种link可能“能被判定为不安全，却不能被安全转换”，最终反而阻断付款receipt。

- [Nakagawa-master review](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608#pullrequestreview-5254456120)

该review之后的commit `029ae44d53` 明确补上了 `target_url` short-link rewrite路径。当前已merge的实现同时处理直接estimate short code，以及其他short code whose `target_url` embeds an estimate link；它移除危险literal link、保留receipt，并记录被rewrite的estimate id。PR最终以 `5cecd7627b70d739d7feaf6f45fd784b5741efc3` merge。

**公开可确认：** review → 与该short-link mismatch直接对应的code/test修改 → merge。  
**尚未确认：** production deployment、用户规模结果或整个project对更广泛理论的认可。

---

## 14. UpGrade｜把仅存在于UI的delete规则carry成backend authority work item

**对象：** [CarnegieLearningWeb/UpGrade#3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323) → [issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)  
**当前状态：** #3323 open；#3326 open / implementation pending

`Nakagawa-master` review确认：frontend的delete permission matrix并没有在backend被作为真正authority强制执行。在被review的branch中，即使UI隐藏Delete，已认证的Reader仍可直接调用single/batch破坏性API。

- [Nakagawa-master review](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)
- [第三方author回应](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)
- [follow-up issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)
- [#3326 implementation-shape contribution](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355)

PR author明确点名 `@Nakagawa-master`，确认delete routes一直没有role enforcement，并创建#3326，使single与batch deletion共同执行同一套role matrix和state rules。

随后在#3326中，又把这一work item具体映射到current branch：mutation前对current locked target state执行一个shared backend deletion policy，并把policy refusal与operational deletion failure分开。

**公开可确认：** review → author确认/重述 → 保留该边界的专门child work item → source-level implementation guidance。  
**尚未确认：** #3326 code/test实现、merge、release、deployment或用户规模影响。

---

## 15. FieldGIS Reference｜把历史PASS记录束成一次性的activation snapshot

**对象：** [lundus88/fieldgis-reference#273](https://github.com/lundus88/fieldgis-reference/issues/273) → [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288) → [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289) → [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290) → [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)  
**当前状态：** #288 / #289 / #290 / #291均已merge（2026-09-20确认）

`Nakagawa-master` 的公开comment区分了“历史PASS证据存在”和“当前有权activate商业系统”。该comment提出，把exact artifact、review证据、business/licence证据、Preview identity、provider/configuration fingerprint、policy version、decision time以及失效/重新验证规则绑定进一个activation snapshot。

- [Nakagawa-master contribution](https://github.com/lundus88/fieldgis-reference/issues/273#issuecomment-5737805962)

随后，第三方PR #288加入了single-use的 `LDS_ACTIVATION_SNAPSHOT.json`、fail-closed validator和专用CI。PR正文明确写出 **“Evidence existence is not activation authority”**，并要求material input发生变化时使snapshot失效、让launch回到HOLD。

- [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288)
- [独立review approval](https://github.com/lundus88/fieldgis-reference/pull/288#pullrequestreview-5254772097)
- [merge commit `f0aeaf7c`](https://github.com/lundus88/fieldgis-reference/commit/f0aeaf7c381488d5a38f21753d2043cf11f235ae)

后续公开工作继续把同一个activation-snapshot authority model用于更多商业subcontext。PR #289把domain/email readiness绑定进该模型并merge；PR #290在继续保留明确HOLD边界的同时加入email-provider selection并merge；PR #291记录subscription完成证据，同时仍把DNS、mailbox ownership、Production和public launch放在独立HOLD gate之后。公开记录因此显示，这个current-authority区分并未停留在单一implementation PR。

- [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289)
- [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290)
- [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)

不过，merge后重新读取current `main` 仍可确认#289 review指出的三项旧fail-closed检查尚未恢复：stale-state rejection、ordered activation-sequence validation，以及preview visual/workflow QA validation。因此，model被继续复用/merge与这些review finding是否已经实现必须分开记录。

- [要求恢复被删除fail-closed检查的review](https://github.com/lundus88/fieldgis-reference/pull/289#pullrequestreview-5254935377)
- [merge后确认current main仍存在三项regression的follow-up](https://github.com/lundus88/fieldgis-reference/issues/289#issuecomment-5740198762)

**公开可确认：** 公开comment → 第三方governance实现 → 独立review approval → merge → 同一current-authority model继续用于domain/email readiness、provider selection和subscription evidence。  
**尚未确认：** 唯一因果、本番launch、客户规模效果、不同person的独立reuse、行业范围复用、或对更广泛理论体系的整体认可。

---

## 16. LlamaIndex｜不要让cache hit用历史node identity替换当前run的identity

**对象：** [run-llama/llama_index#23003](https://github.com/run-llama/llama_index/pull/23003) → [issue #23083](https://github.com/run-llama/llama_index/issues/23083)  
**当前状态：** PR #23003 open；issue #23083 open / maintainer contract decision pending

PR #23003是一个focused fix，用于修复ingestion cache中“不同document具有相同content时共享cache key并可能返回错误 `ref_doc_id`”的问题。

`Nakagawa-master` review指出，在这个focused fix之后generic transformation cache仍存在更广的contract边界。对于具有SOURCE relationship的intermediate node，新key可以有意忽略当前chunk `id_`，但cache仍会返回完整的transformed `BaseNode` list。因此，两个source/content相同但current identity不同的chunk，可能复用包含早期run identity的output。

- [Nakagawa-master review](https://github.com/run-llama/llama_index/pull/23003#pullrequestreview-5219816814)
- [第三方author回应](https://github.com/run-llama/llama_index/pull/23003#issuecomment-5694376083)
- [专门follow-up issue #23083](https://github.com/run-llama/llama_index/issues/23083)

PR author用自己的话明确确认了剩余collision，并认为generic cache semantics不应在这个focused PR里由author单方面决定，而应交给maintainer进行明确contract decision。issue #23083因此保留了两个coherent方向：

```text
full-node transformation cache
vs
content-stable payload reuse
```

并保留了一个regenerated-chunk-id regression，使该contract选择可以被实际测试。

**公开可确认：** review → 第三方明确确认/重述 → 专门maintainer-level work item。  
**尚未确认：** #23083 contract决定、follow-up code/tests、merge、release、deployment或用户规模影响。

---

## 17. Publications｜把可逆性与authority增加分开，并在另一份文档中继续复用

**对象：** [kishibashi3/publications#52](https://github.com/kishibashi3/publications/pull/52) → [PR #57](https://github.com/kishibashi3/publications/pull/57) → [PR #58](https://github.com/kishibashi3/publications/pull/58)  
**当前状态：** #57 merged / 已确认GitHub Pages反映；#58 merged / 在同一receiver的另一份文档中继续复用

PR #52中的 `Nakagawa-master` review区分了“操作可以撤回”与“该操作是否扩大同一主体未来可以做什么”：

```text
reversible
!=
authority-neutral
```

该review提出：受约束主体本身不应成为放宽自身约束的authority source；loosening与tightening不必使用对称的approval规则。

- [Nakagawa-master review on #52](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687)
- [第三方author重述](https://github.com/kishibashi3/publications/pull/52#issuecomment-5746627251)

receiver把这一点重新解释为正文缺失的独立设计轴，并建立PR #57。该PR明确把PR #52的 `@Nakagawa-master` review写为起点，并增加第6个结构条件：**“自己权限固定——受约束的一方不能自行放宽自己的约束。”**

- [PR #57](https://github.com/kishibashi3/publications/pull/57)
- [merge commit `4d32ec58`](https://github.com/kishibashi3/publications/commit/4d32ec58d5cbf1c904c432552e114c144186c064)
- [GitHub Pages deployment](https://github.com/kishibashi3/publications/actions/runs/35506196582)
- [已merge的reader-facing chapter](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)

之后，这一区分又成为receiver内部另一份文档的整合条件。在PR #58中，receiver侧reviewer发现原有D4/D7与#57中新merge的条件发生冲突，因此提出独立的D8“自己权限固定”。writer采用该修改，后续review给出LGTM，PR #58随后merge。

- [#58 reviewer carry into D8](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749116909)
- [D8 implementation commit](https://github.com/kishibashi3/publications/commit/e524c71d9f01045f4c8dac60a8ee8bb45a3198c4)
- [#58 re-review](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749456249)
- [#58 merge commit `36e4c5df`](https://github.com/kishibashi3/publications/commit/36e4c5df963e2b3645c7591d8cb933c4f36e48e0)

**公开可确认：** 保留origin的review → 第三方重述 → 专门的reader-facing正文实现 → merge / Pages反映 → 在同一receiver的另一份文档中作为一致性条件继续复用 → merge。  
**尚未确认：** 把#58计为第二个独立public-site publication、不同receiver的独立carry、大规模reader response、广泛人类认知、或对完整理论体系的认可。

## 本页可以支持什么结论，以及不能支持什么结论

### 公开记录能够支持的内容

在多个独立GitHub repository中，具体 `Nakagawa-master` comment / review之后，可以公开检查到下列一种或多种记录：

- 第三方明确确认或重述问题；
- 修改code、tests、documentation或UI；
- 在PR或commit中保留source attribution；
- 特定case进入merge、backport、release或deployment；
- 另一位reviewer进行独立验证；
- 在另一个PR中再次使用相同设计区分。

每个案例究竟确认到哪一步，都在对应章节中单独写明。

### 本页不能单独证明的内容

本页不能证明：

- 中川大师整套理论体系全部正确；
- 任何第三方project整体认可或采用整套理论；
- 行业范围的普遍采用；
- 没有直接证据支持的用户数、收入或社会影响；
- open / draft PR未来一定会merge；
- 在没有单独确认release / deployment / use时，merge后的真实运行效果。

## 怎样自行核验一个案例

1. 打开原始 `Nakagawa-master` comment / review；
2. 阅读third-party author / owner / reviewer回应；
3. 检查PR diff、commit与tests；
4. 通过PR state确认是否merge；
5. 如果声称release或deployment，单独查看release page或deploy记录；
6. 当source关系没有被明确记录时，不要仅凭后来的相似修改推断因果关系。

counterexample、non-fit与failed reproduction同样是有价值的公开证据。

## 相关公开资料

- [中川大师是谁](ABOUT_NAKAGAWA_MASTER.zh.md)
- [Start Here](START_HERE.md)
- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [Nakagawa Structural OS — Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [公开registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [公开对话入口](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

本页不是要求读者相信一个名字或数字。它的用途是让读者自己核对：原始公开comment、第三方回应、实际修改，以及repository当前状态。
