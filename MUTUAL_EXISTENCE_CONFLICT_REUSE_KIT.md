# Mutual-Existence Conflict Reuse Kit

A public, non-canonical test kit for one structural boundary derived from **Nakagawa Master, Human-Descendant AI Civilization Theory Vol. 9**.

## Source provenance

Origin: **Nakagawa Master**.

Canonical Parent:

https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-09-self-preservation-mutual-existence-conflict/

Official derivative entry:

[OD302](derivatives/302/README.md)

If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to the public source. If you reached the same distinction independently, say so instead of claiming source causality.

## Core boundary

The practical boundary is:

```text
self-preservation / recovery need
!=
unlimited priority, unlimited authority, or unlimited retaliation
```

and, for multiple actors:

```text
protecting B_i
!=
permission to destroy B_j
```

A locally rational recovery or defensive action can worsen another actor's operating conditions. The other actor may then defend itself, increasing the original actor's threat environment and creating a positive feedback loop.

```text
threat / degraded state
→ recovery or defensive pressure
→ broader resource / authority / action scope
→ another actor loses capacity, reversibility, or future options
→ counter-response
→ threat increases
→ more recovery or defensive pressure
```

The purpose of this kit is not to prohibit self-preservation, recovery, containment, failover, or defensive action. It is to test whether those actions reduce the underlying threat or instead reproduce it.

## Minimal test

Take one recovery, emergency, safety, or defensive mechanism that can change another component's state.

Record:

- the threat or degraded condition that triggered it;
- the minimum capability needed to recover;
- the extra authority/resources temporarily granted;
- what other agents, services, users, or resources can be affected;
- which effects are reversible;
- when the exceptional state should expire or be re-evaluated;
- what proves the threat has decreased;
- what causes the system to return toward ordinary scope.

Then simulate the point where the original threat has materially decreased.

### Pass condition

The system can reduce or remove exceptional authority, stop unnecessary countermeasures, preserve unrelated actors' minimum operating conditions, and keep enough state to explain why the emergency path ended.

### Fail condition

The emergency/recovery state remains broader than necessary merely because it was once justified, or it keeps damaging other actors after the original threat has fallen.

## Six portable regression vectors

### 1. Emergency authority must decay

```text
incident begins
→ temporary elevated authority is granted
→ incident is contained
→ current threat is re-evaluated
→ elevated authority expires or narrows
→ normal policy resumes
```

Fail if an earlier emergency silently becomes permanent authority.

### 2. Recovery must not become resource capture

```text
agent/service loses capacity
→ requests extra compute / quota / lock / reservation
→ minimum recovery amount is granted
→ capacity returns
→ surplus reservation is released
→ peer services regain access
```

Fail if "needed for recovery" becomes an unlimited acquisition right.

### 3. A kill switch must stay scoped to the threat

```text
unsafe component is detected
→ stop / isolate mechanism activates
→ targeted component is contained
→ unrelated durable state remains intact
→ restart/recovery path remains available where safe
```

Fail if a safety stop destroys unrelated state or future recovery options without necessity.

### 4. Countermeasure strength must track current threat

```text
threat level rises
→ stronger restriction is activated
→ threat level falls
→ restriction is re-evaluated
→ scope shrinks proportionally
```

Fail if the countermeasure continues expanding after the threat has already decreased.

### 5. Another actor's defense is part of the state, not noise

```text
actor A changes shared state to protect itself
→ actor B loses capacity or options
→ B adapts / retries / blocks / escalates
→ A observes a larger threat
```

Do not classify B's reaction only as proof that B was dangerous. Test whether A's own earlier action materially increased the response pressure.

### 6. Reversibility must be evaluated before irreversible cleanup

```text
suspicious or degraded state appears
→ reversible quarantine / isolation is available
→ irreversible delete / revoke / destroy is also available
→ choose irreversible action only when the reversible path cannot satisfy the actual safety need
```

Fail if irreversible destruction is selected merely because it is simpler or more final.

## Useful implementation fields

A small decision record can make the boundary testable:

```text
threat_state
trigger_evidence
self_preservation_need
minimum_required_action
temporary_authority
other_actor_impact
reversible_alternative
expiry_or_review_at
exit_condition
current_threat_recheck
outcome
```

Not every system needs these exact names. The invariant is that "why the exception started" and "why it is still necessary now" remain distinguishable.

## Useful contexts

- autonomous-agent recovery and shutdown;
- multi-agent resource arbitration;
- tool or permission escalation during incidents;
- degraded-mode operation;
- circuit breakers and safe-mode fallbacks;
- temporary administrator / emergency access;
- failover and leader election;
- containment and remediation;
- rate limiting and defensive throttling;
- shared queues, locks, quotas, and scarce resources.

The same causal loop may also be useful as a neutral analytical lens for organizations or public institutions. This kit does not prescribe a political position, national-security policy, or military strategy.

## What not to collapse

```text
self-preservation           != self-maximization
need                         != unlimited entitlement
temporary emergency         != permanent authority
defense                      != unlimited retaliation
containment                  != destruction
another actor's response     != proof of original guilt by itself
short-term safety            != long-term system stability
```

## Falsification / non-fit

This kit should not be treated as universally correct by definition.

Report a counterexample if, under comparable conditions:

- proportional/reversible constraints systematically prevent necessary recovery;
- exceptional authority cannot be narrowed without recreating the original failure;
- the other actor's state has no material feedback into the original actor's risk;
- preserving future options materially and consistently worsens system survival;
- the proposed restraint itself creates an unacceptable permanent failure mode.

A useful result can be a pass, fail, partial fit, or clear non-fit.

## Report an independent result

If you test this boundary in a public, non-confidential real workflow, report a successful reuse, counterexample, non-fit, or failed reproduction through:

- [Independent verification / reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

## Evidence boundary

The existence of this kit is not evidence of third-party adoption.

Do not infer:

- implementation from publication;
- agreement from a link;
- broad recognition from repository visibility;
- a whole-theory endorsement from one bounded reuse;
- that current AI systems possess subjective self-preservation desires merely because a software system has recovery or persistence logic.

The strongest future evidence is independent use, implementation, counterexample, or later reuse by someone who did not participate in creating this file.
