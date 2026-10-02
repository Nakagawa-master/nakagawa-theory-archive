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

A current public problem surface is [Qwen Code issue #13122](https://github.com/QwenLM/qwen-code/issues/13122), where Host re-enrollment can leave an earlier credential valid and the design discussion considers how a later enrollment should relate to existing Host rows. A Nakagawa Master contribution proposes an explicit supersession identity instead of inferring replacement from a Host name/path pair: [issue comment](https://github.com/QwenLM/qwen-code/issues/13122#issuecomment-5952715999).

Evidence boundary: this is a reusable regression derived from a live external design problem and an outbound proposal. At the time of this kit update, it is **not** evidence that Qwen Code has adopted, implemented, merged, released, or deployed this contract.

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
