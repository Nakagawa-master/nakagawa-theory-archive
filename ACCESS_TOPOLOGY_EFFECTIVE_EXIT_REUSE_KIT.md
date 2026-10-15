# Access Topology & Effective Exit Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**.

Canonical source:
https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/

Official derivative:
[OD306 — Non-ownership, effective power and non-domination](derivatives/306/README.md)

Human entry:
[OD306 human-readable entry](derivatives/306/human-entry.md)

If this kit materially informs a real decision, implementation, test, policy, architecture review, migration plan, or workflow, preserve a lightweight source route. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.

This kit does **not** say that centralization, dependence, a single provider, or a shared service proves domination. It asks a narrower question:

> **Who can change the set of actions that remains practically available to someone else, through which gates, and what happens when the primary path is removed?**

Three distinctions are especially useful:

```text
non-ownership
!=
non-domination

nominal alternative
!=
viable independent alternative

export available
!=
effective exit proven
```

## Start from the failure you can already see

**Try the distinction on your own architecture, safely.** Suppose a product advertises both cloud and local AI operation. If the cloud-only control service is unavailable, can its local route *actually* start and resume an in-scope task? [The offline route-isolation evidence probe](machine-discovery/access_topology_independence_probe.py) separates a working product operation from a tested independent route, and an explicitly deferred route from a route that has passed.

From a local checkout, with Python 3 and no dependencies:

```sh
python3 machine-discovery/access_topology_independence_probe.py --self-test
python3 machine-discovery/access_topology_independence_probe.py --example > /tmp/route-example.json
python3 machine-discovery/access_topology_independence_probe.py --input /tmp/route-example.json
```

Edit the example's `routes[].requires`, `tests[].unavailable`, `tests[].other_path_gates` and `tests[].observed` to describe **your own controlled test**. The provided Qwen-shaped example intentionally leaves the Hosted isolation run unobserved, marks ordinary Local M6 as deferred, and classifies the [reported experimental package/restart test](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6166254311) as **operation evidence only**, because it did not remove the other route's exclusive gates. This example is not a remotely executed test. A declared shared-gate loss without a run is also labeled untested; an actual failure at an intentionally shared gate is not automatically a violation of path independence.

The evaluator never disables a service, accesses a remote system, or authenticates supplied evidence. Even an `CANDIDATE_PASS_EVIDENCE_NOT_AUTHENTICATED` is a classification of **your supplied** isolation record, not an external certification. Run destructive/fault scenarios only in an environment you control. The canonical [Nakagawa Master non-ownership/effective-power theory](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/) gives the broader distinction; this script is a narrow, falsifiable reuse tool.


| What you are seeing | Test first |
| --- | --- |
| Several providers or routes exist, but they all disappear when one shared auth/catalog/control service fails | Common-upstream independence |
| A user can download data, but restoring service elsewhere is difficult or incomplete | Effective-exit round trip |
| A local/self-hosted option still depends on cloud activation, identity, policy, or metadata | Hidden control-plane dependency |
| An auditor exists, but objections/evidence must pass through the system being audited | Independent audit entry |
| A migration is technically allowed, but history, identity, credentials, compatibility, or continuity are lost | State continuity during exit |
| Temporary emergency control remains after the original reason disappears | Scope, expiry, review and reversibility |

## Six-step access-topology test

### 1. Name the capability that must remain possible

Do not start by counting providers or owners. Name the concrete capability:

- authenticate;
- compute;
- communicate;
- read or move data;
- restart;
- continue a session or identity;
- migrate;
- challenge a decision;
- obtain independent review;
- restore operation.

The unit is an **action the user/actor still needs to be able to perform**.

### 2. Draw the critical gates

For each capability, identify the gate that can allow, deny, delay, rewrite, or withdraw it.

Typical gates include:

```text
identity / authentication
compute
network / communication
model or service discovery
data store
configuration
policy / authorization
restart / recovery
migration / import
billing / allocation
audit / appeal / correction
```

A product can have many visible options while several of them still depend on one hidden gate.

### 3. Trace common upstream dependencies

For every claimed alternative, ask:

- Does it need the same identity provider?
- Does it need the same catalog, broker, control plane, account, network, or policy service?
- Does it fail when the primary route is disabled?
- Can the gate owner change the conditions unilaterally?
- Does one outage or revocation remove several “alternatives” at once?

A useful representation is:

```text
Alternative A -> Gate X
Alternative B -> Gate X
Alternative C -> Gate X
```

Three labels do not create three independent alternatives if one unavailable Gate X removes all three.

### 4. Run the viable-alternative failure test

Disable or simulate loss of the primary gate under a safe test condition.

A viable alternative should remain able to complete the minimum required action without silently returning to the failed gate.

Example:

```text
configured provider A unavailable
-> provider B can still be selected
-> provider B authenticates through an independent path
-> a known valid model/service can actually execute
-> no hidden dependency on A is needed to discover or authorize B
```

A fallback that exists only on a settings screen but cannot complete the action is a nominal alternative, not yet a viable one.

### 5. Run the effective-exit round trip

“Export” is only one step.

Test the complete path:

```text
source system
-> export / transfer
-> independent destination
-> import / reconstruct
-> authenticate / restart
-> continue the minimum required state or function
```

Record what is lost:

- history;
- identifiers;
- credentials;
- permissions;
- links/references;
- compatibility;
- state needed to continue;
- recovery ability;
- audit history.

### Pass condition

The actor can leave the primary path and restore the minimum required capability through an alternative whose load-bearing gates are sufficiently independent for the tested failure.

### Partial condition

Data can be exported, but important state/function cannot yet be restored. Report “portability exists; effective exit remains incomplete.”

### Fail condition

The claimed exit requires the same unavailable gate, loses the minimum required state, or cannot restore practical operation.

### 6. Test objection, scope and reversibility

If exit is weak or impossible, the remaining relationship may still become more contestable when:

- authority is explicitly scoped;
- exceptional access expires;
- decisions can be appealed;
- evidence can reach an independent reviewer;
- corrections can be implemented;
- alternative investment/re-entry remains possible;
- temporary concentration is re-evaluated when conditions change.

An “independent auditor” is not enough if the same gate controls whether evidence or objections can reach that auditor.

## Portable regression vectors

### A. Provider discovery becomes a hidden chokepoint

```text
direct provider endpoint accepts model M
+ shared catalog/listing does not contain M
-> user enters provider-native model id explicitly
-> request can still execute
-> unknown metadata stays unknown rather than becoming false
```

The catalog may control what the system can describe confidently without becoming the sole authority over what an already configured independent route may reach.

### B. Multiple clouds share one identity gate

```text
workload can run on cloud A or cloud B
-> shared identity/control account is revoked
-> both routes stop
```

The infrastructure is multi-provider, but the tested access topology still contains one common gate.

### C. “Self-hosted” still requires a remote control plane

```text
local runtime is installed
-> remote account/control service becomes unavailable
-> local runtime cannot authenticate, discover required state, or restart
```

Test whether the self-hosted path is independently operable for the promised scope.

### D. Export works, restore does not

```text
user downloads data
-> source service disappears
-> destination cannot import or reconstruct required state
```

Report export/portability separately from effective exit.

### E. Independent audit exists only behind the audited gate

```text
actor disputes a decision
-> evidence submission requires approval from the original decision path
-> access is denied
-> external auditor never receives the evidence
```

Nominal reviewer independence does not prove independent audit entry.

### F. Emergency concentration never decays

```text
emergency creates temporary centralized authority
-> emergency ends
-> scope, privileges and dependency remain unchanged
```

Test expiry, review and reversibility rather than treating the original emergency as permanent justification.


### G. Enrollment authority is mistaken for replacement authority

A credential or token that authorizes creation of a new endpoint does not automatically identify which existing endpoint may be destroyed or replaced.

```text
authorized to enroll a new endpoint
!=
authorized to choose an existing endpoint to supersede
```

This matters when existing endpoints have caller-supplied or locally derived attributes such as a display name, hostname, checkout path, workspace path, or label. Similar attributes are useful for presentation and duplicate detection, but they are not necessarily a safe identity oracle.

A portable regression is:

```text
existing endpoint A has credential A
existing endpoint B happens to share A's display name/path
operator receives one valid enrollment capability

generic enroll
-> creates a new endpoint
-> revokes neither A nor B

explicit replace of A
-> replacement request names A's stable identity
-> server verifies A is in the authorized scope
-> new credential/identity is created
-> durable bindings migrate A -> replacement
-> in-flight ownership is settled according to the replacement contract
-> A's old credential is rejected after the transaction
-> B remains unchanged
```

Also test a stale or missing replacement target:

```text
explicit replace references missing/stale endpoint
-> fail closed
-> zero credential revocation
-> zero binding migration
-> zero run/lease mutation
```

The design question is not whether replacement should always be supported. The boundary is narrower: if the system chooses replacement semantics, bind the authority to replace to the exact identity being superseded rather than silently deriving destructive authority from attributes that can collide.

A useful independent contrast is [Microsoft PilotSwarm issue #27](https://github.com/microsoft/PilotSwarm/issues/27). Its public relay design does **not** need to identify an old Host by a colliding display attribute in order to make ordinary re-enrollment safe. The proposed authority is already bound to the exact Entra owner + exact private session + one-use invitation + Host key; connection credentials are short-lived, re-enrollment requires a new invitation and new local consent, and old-attempt or revoked-grant results are specified not to commit. Sharing or ownership change ends the binding.

That is a concrete non-fit case for an over-broad reading of this regression:

```text
fresh enrollment is always a new exact grant
+ old authority cannot be recreated from name/path similarity
+ no API claims to "replace whichever existing endpoint looks like this one"
→ a separate supersession selector may add no information to ordinary enrollment
```

If such a system later adds an operation that **does** revoke or migrate an existing endpoint as part of replacement, the destructive target still needs an exact authority-bearing identity. The contrast therefore narrows the test rather than weakening it: challenge inferred replacement authority only where replacement actually exists.

This PilotSwarm issue is independent public design evidence, not evidence that it used this kit, not an implementation result, and not proof that the proposed relay contract has shipped.

A current public problem surface is [Qwen Code issue #13122](https://github.com/QwenLM/qwen-code/issues/13122), where Host re-enrollment can leave an earlier credential valid and the design discussion considers how a later enrollment should relate to existing Host rows. A Nakagawa Master contribution proposes an explicit supersession identity instead of inferring replacement from a Host name/path pair: [issue comment](https://github.com/QwenLM/qwen-code/issues/13122#issuecomment-5952715999).

The access-topology test above asks whether the caller has authority to revoke a particular endpoint. The temporal identity layer is separate: even when the replacement target is exact, the new endpoint's relation to the old one still has to be classified and audited.

```text
explicit supersession target
→ old/new transition is identifiable
→ preserved and changed bindings are visible
→ old authority does not silently survive merely because lineage exists
→ current authority is revalidated for the replacement
```

For that companion layer, see [OD307 — Self-Modification Identity and Kernel Lineage](derivatives/307/README.md). Its relevant boundary is `Lineage continuity ≠ automatic authority inheritance`; an inherited credential, binding, name, function, or historical relationship is not by itself proof that current authority should continue. OD306 remains the access-topology source for the creation-vs-destruction authority distinction.

Evidence boundary: this is a reusable regression derived from a live external design problem and an outbound proposal. At the time of this kit update, it is **not** evidence that Qwen Code has adopted, implemented, merged, released, or deployed this contract.

## Receiver return: Qwen dual-path independence gate

[Qwen Code issue #12380](https://github.com/QwenLM/qwen-code/issues/12380) now contains a bounded receiver-side return on the path-independence distinction.

Nakagawa Master first separated:

```text
two configured paths
!=
two viable independent alternatives
```

and proposed an A/B/C/D acceptance shape that removes the other path's exclusive gate, inventories intentionally shared gates, and keeps independence separate from failover: [origin comment](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-5921364520).

On 2026-10-07, Qwen's collaborator-owned triage explicitly re-read that comment, named **Nakagawa-master**, and kept the path-independence gate as one of the issue's unresolved next decisions. The triage distinguished:

```text
no cross-engine fallback
!=
path independence
```

and recommended either adopting the A/B matrix or explicitly recording which gates the two paths intentionally share: [receiver triage return](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035602677).

A bounded follow-up then adapted the test to the repository's current asymmetry: Hosted delivery is active while ordinary/local Managed M6 activation remains deferred, so the acceptance record should allow Hosted independence to be proven for its current scope without pretending the local half already passes: [follow-up](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035698005).

On 2026-10-08, external developer `wenshao` [explicitly replied to @Nakagawa-master and the triage](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6045681161). They agreed that **no cross-engine fallback is not independent operability**, edited the umbrella issue body to record the staged gate as **open proposed decision 4**, and left the final adoption choice to the issue's proposal owner. Hosted can be tested within its actual scope; ordinary/local M6 activation is deferred, and the shared dependency inventory is not a passed runtime test. That was the **2026-10-08 state**, not the present disposition. On 2026-10-12 the proposal owner `doudouOUC` [explicitly adopted Nakagawa Master's staged acceptance matrix](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998); the receiver's [live proposal body](https://github.com/QwenLM/qwen-code/issues/12380) now includes it in both the **Acceptance criteria** and Decision 4. This is a real, independent decision/requirements change, not proof that either runtime arm has passed the test.

For a practical review, the distinction becomes an acceptance table rather than a slogan:

| Claimed route | Disable safely | Demand evidence | Current verified disposition |
| --- | --- | --- | --- |
| Hosted Managed | local-only Managed owner/state/paired-host dependencies | create a bounded Hosted Session, run and recover without local-only authority | adopted release gate; actual Hosted independence evidence still owed |
| Ordinary/local Managed | Hosted-only Java authority, catalog, storage and migration endpoints | create/select local Session, execute and recover without Hosted-only calls | M6 deferred; **not testable as shipped** |
| Shared services | deliberately common identity, config, inference, runtime and storage layers | name the shared point and test the real failure scope | required pre-gate inventory; actual dependency-failure proof not yet verified |

**Current receiver evidence (2026-10-15, primary sources):** The [Qwen proposal owner formally adopted this staged route-independence gate](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998), after the [specific Nakagawa Master review](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035698005). That receiver-owned decision is a concrete design/acceptance change. It does **not** mean either Hosted or ordinary Local has passed its path-isolation test.

Qwen's [experimental Java reference-distribution PR #14176](https://github.com/QwenLM/qwen-code/pull/14176) subsequently **merged on 2026-10-15** as [`a750166bec`](https://github.com/QwenLM/qwen-code/commit/a750166becd7455be084827857714e1a11329730). The [final candidate's Ubuntu archive/boot dry run](https://github.com/QwenLM/qwen-code/actions/runs/38677487570) passed, while its release-publication step was **SKIPPED**. The earlier failing Ubuntu tar job described in the October 14 snapshot is historical, not this merged revision. Separately, [Nakagawa Master's exact source review](https://github.com/QwenLM/qwen-code/pull/14176#pullrequestreview-5516750288) identified that the final uploaded draft assets were being checked by filename and size without verifying the content after upload; the developer [implemented the final remote SHA-256 check](https://github.com/QwenLM/qwen-code/commit/dc6ea3b4601707ceef4b41f0c064fa490b13a2da) before tag creation or publication. This source-specific repair and the staged path-independence requirement are **distinct contributions and distinct stages**.

An [independent Qwen engineer's post-merge Linux report](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6185267437) rebuilt the merged commit, verified archive reproducibility from identical jars, completed real Java/MySQL + controlled-model restart-and-follow-up operations, and exercised nine **simulated GitHub publish** negative cases including same-length altered assets. The same report separately found **operator-guide prerequisites missing from the archive**: mandatory Session Store/workspace settings and MySQL `performance_schema.user_variables_by_thread` read permission. Those documentation findings belong to that independent engineer, not to Nakagawa's digest review. Actual GitHub reference-release publication, deployment by external users, and real cloud-object or full live-distribution validation were not established by these checks.

**What to test next:** (1) complete and document the Hosted route's own bounded create/Turn/recovery when *local-only* state and paired-host gates are demonstrably unreachable; (2) keep the ordinary Local route **NOT YET PASSABLE** until M6 is enabled, then test it with Hosted-only authority removed; (3) separately try the documented reference package on the exact supported operator configuration and permissions, record a real published asset if one exists, and compare what runs to what the guide claims. These are different tests: `no fallback` does not certify independent operability; a successful archive does not certify the path-isolation gate; a PR merge is not a published release. The [offline independence probe](machine-discovery/access_topology_independence_probe.py) offers a source-linked, user-supplied evidence classification without causing any remote outage or claiming third-party theory adoption.

### A short, reproducible acceptance record for any dual-route system

The same question is useful outside Qwen Code. An engineer or AI-assisted reviewer may independently choose a **nonconfidential local test** with a disposable test environment. Before attempting it, record the advertised routes, the capability and exact exclusive gates. Do not disable live services or modify other users' permissions.

| Controlled case | Positive evidence | Negative/control outcome to record |
| --- | --- | --- |
| Route A with B-only machinery unreachable | A creates one valid scoped session, performs its bounded action and recovers it under A's own authority | “No fallback happened” alone does **not** pass if an A action still required B-only identity or storage |
| Route B with A-only machinery unreachable | B independently selects, executes, restarts and recovers within the scope actually shipped | If B is not implemented or enabled, report **NOT YET PASSABLE**, not PASS or FAIL |
| Intentionally shared gate removed | Dependency inventory predicts which routes stop at that layer; observe and disclose actual failure scope | A shared failure is not automatically a violation of a gate that explicitly permits that shared dependency |

Record actual build and route versions, which dependencies were truly made unreachable, the executing actor, primary action/restore result, negative-control outcome and any missing evidence. If only the acceptance *decision* exists, the result is **specification adopted; execution unverified**. An AI may summarize or challenge the publicly cited design, but that is not proof it ran the receiver's infrastructure or adopted the canonical theory.

For the wider conceptual source, return to [Nakagawa Master's canonical non-ownership/effective-power theory](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/) and [OD306](derivatives/306/human-entry.md); this test kit is an application, not a claim that the Qwen implementation originated from that entire Parent.

## Independent public example: Freenet hosted-to-own-peer migration

[Freenet issue #4381](https://github.com/freenet/freenet-core/issues/4381) is a useful **independent problem surface**, not evidence that Freenet adopted this Nakagawa-derived kit.

The issue itself identifies a concrete tension: a public hosted proxy lowers onboarding friction while the hosted node becomes a trusted intermediary for private delegate state.

The public implementation history then separates several layers:

1. generic encrypted export/import support — [PR #4506](https://github.com/freenet/freenet-core/pull/4506);
2. hosted disclosure — [PR #4530](https://github.com/freenet/freenet-core/pull/4530);
3. live hosted export — [PR #4531](https://github.com/freenet/freenet-core/pull/4531);
4. browser export wiring — [PR #4562](https://github.com/freenet/freenet-core/pull/4562);
5. the remaining import-friction problem is made explicit in [issue #4592](https://github.com/freenet/freenet-core/issues/4592);
6. live import into a running receiving peer merges in [PR #4603](https://github.com/freenet/freenet-core/pull/4603);
7. a one-time magic-link migration path with a mint -> pull -> import integration test merges in [PR #4724](https://github.com/freenet/freenet-core/pull/4724).

That supports a bounded observation:

```text
export exists
-> technical portability improves
-> receiving-side live import removes one exit barrier
-> migration path becomes lower-friction
-> mint/pull/import is integration-tested
```

It does **not** by itself prove that real users have completed a hosted-to-own-peer migration at meaningful scale, or that every dependency has become independent. Implementation evidence and real-world effective exit are different evidence layers.

## What to record

A useful public result can be short:

- capability tested;
- primary gate;
- alternative route;
- common upstream dependencies;
- failure injected or observed;
- what state survived migration;
- what state was lost;
- pass / partial / fail / non-fit;
- evidence link;
- source relation if this kit materially informed the test.

Do not include credentials, private customer data, sensitive security details, or confidential infrastructure information.

## Decision rule

```text
count alternatives
-> map their load-bearing gates
-> fail the primary/common gate safely
-> verify which alternatives still complete the action
-> run export-to-restore round trip
-> test objection/review/reversibility
-> report only the highest evidenced state
```

The goal is not mandatory decentralization. The goal is to distinguish **visible plurality** from **practical independence**, and **permission to leave** from **an exit that actually works**.

## Report an independent result

- [Independent verification & reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)

Counterexamples and non-fit results are useful evidence.
