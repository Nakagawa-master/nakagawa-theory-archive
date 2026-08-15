# AI Index — English | Official Derivative 072

## Parent Original
- Title: 中川式 接続裁定設計論──紛争・救済・復権のプロトコル
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-adjudication/
- Parent Post ID: 306
- Parent NCL-ID: NCL-α-20251102-2a60e2
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## Derivative Identity
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-2A60E2-AI-EN-0072-0004
- derivative_diff_id: DDIFF-20260815-DNCL-072-0004-0003
- supersedes: DDIFF-20260804-DNCL-072-0000-0001

## Summary
Connection Adjudication Design addresses disputes, consent misuse, metric gaming, log manipulation, and collective pressure that arise when connection institutions operate in practice. It is designed to prevent conflict from reverting to reputation, authority, outrage, majority pressure, or private punishment. Adjudication is treated as a reversible procedure for stopping harm, preserving evidence, determining responsibility proportionally, providing remedy, restoring participation under conditions, and reopening decisions when new evidence appears.

Its four principles are legitimacy, proportionality, repair priority, and independence. The procedure separates receipt, provisional measures, investigation, decision, remedy, and restoration. Reputation, titles, follower counts, and majority support are not evidence. Primary evidence such as ConsentToken, MemoryObject, ReversibilityFlag, and signed structural logs remains distinguishable from secondary evidence such as audit summaries, observation logs, and third-party testimony, with provenance, gaps, and manipulation risk kept visible.

The parent states operational reference times of **24 hours for receipt, 48 hours for provisional measures, and 14 days for a first decision** as targets intended to limit secondary harm from delay. These are source-authored design references, not universal legal deadlines, universal SLAs, correctness guarantees, or remedy guarantees.

## Concepts
- connection adjudication
- legitimacy
- proportionality
- repair priority
- independence
- receipt
- provisional measures
- primary evidence
- secondary evidence
- ConsentToken
- MemoryObject
- ReversibilityFlag
- evidence provenance
- public summary
- protected record
- conflict-of-interest recusal
- remedy
- observed return
- limited return
- full return
- rehearing
- brigading
- SLAPP

## Causal chain
```text
connection institutions operate in practice
↓
coercion, use outside consent, metric gaming, log manipulation, or collective pressure occurs
↓
without formal procedure, reputation, authority, outrage, and private punishment dominate judgment
↓
harm expands and evidence disperses
↓
receipt and timestamp fix the case
↓
reversible provisional measures protect safety and evidence
↓
primary evidence, secondary evidence, provenance, and conflicts of interest are examined separately
↓
a proportional and independent decision is made
↓
correction, withdrawal, renewed consent, compensation, education, and necessary restrictions are applied
↓
observed return, limited return, and full return are considered in stages
↓
new evidence, objection, and rehearing keep adjudication corrigible
```

## State model
```yaml
- case_is_received_or_not
- provisional_protection_is_active_or_not
- investigation_is_open_or_not
- primary_and_secondary_evidence_are_distinguished_or_mixed
- evidence_provenance_is_traceable_or_not
- conflict_of_interest_is_disclosed_or_hidden
- decision_is_proportional_or_excessive
- remedy_is_active_or_absent
- observed_return_is_available_or_not
- limited_return_is_available_or_not
- full_return_is_available_or_not
- rehearing_is_available_or_blocked
- public_summary_is_separated_from_protected_record_or_not
- case_is_closed_with_correction_route_or_without_it
```

## Applications
- For use outside consent, pause the use, preserve consent scope and transfer records, and combine deletion, correction, explanation, compensation, and limited authority as needed.
- For metric gaming, examine homogeneous connections, sudden increases, insider evaluation, and brigading while excluding popularity from evidence.
- For structural-log manipulation, preserve original logs, signatures, diffs, and access history, then choose remedies proportional to affected scope.
- For collective pressure, do not treat mass similar complaints as proof; use provisional protection, external observation, cooling, and reduced counterclaim burden where relevant.
- For restoration after a prior violation, require recurrence prevention, renewed consent, learning evidence, and staged observation rather than automatic return.

## Measurements and audit
**Time references.** Values: 24 hours, 48 hours, 14 days. Source: the parent original. Measurement actor: the institution operating the adjudication procedure. Measurement object: elapsed time to receipt, provisional action, and first decision. Source modality: operational design targets intended to reduce secondary harm from delay. Permitted use scope: observing processing delay and its relation to protection and review. Non-guarantee scope: these values are not universal legal deadlines, universal SLAs, correctness guarantees, or remedy guarantees.

**Rates, counts, and detection measures.** Observable variables include review of provisional measures, voluntary correction/withdrawal/renewed consent, recurrence of similar harm, secondary harm after remedy, staged restoration, rehearing and corrected decisions, detection of brigading or SLAPP, and re-identification or retaliation caused by public summaries. The parent does not define universal pass rates, fixed success thresholds, or guaranteed detection accuracy for these variables.

Reversal evaluation is necessary. Faster handling is not improvement if evidence review, objection, independence, or proportionality weakens. Fewer complaints are not success if access to complaint becomes harder. A higher restoration rate is not success if victim safety or recurrence prevention worsens. More disclosure is not better transparency if re-identification or retaliation rises.

## Validity conditions
- Receipt, provisional action, investigation, decision, remedy, and restoration remain role-distinct.
- Provisional measures have reasons, time limits, release conditions, and objection routes.
- Consent, boundaries, primary logs, and reversibility remain central to evidence.
- Reputation, titles, follower counts, and majority support do not become evidence.
- Evidence provenance, gaps, and manipulation risk remain traceable.
- Conflicts of interest and recusal or external delegation are recorded.
- Victim safety and proportionality are prioritized.
- Remedy and recurrence prevention connect to the decision.
- Staged restoration and rehearing on new evidence remain available.
- The boundary between public summary and protected record remains explainable.

## Failure conditions
- Reputation or popularity determines the result before receipt.
- Provisional action becomes indefinite final punishment.
- Victims carry the full burden of proof, publicity, or reconciliation.
- Reputation, majority support, or follower counts are treated as evidence.
- Conflicts of interest remain undisclosed.
- No path exists for correction, withdrawal, compensation, or renewed consent.
- Permanent exclusion becomes the only safety measure.
- Public summaries enable re-identification or secondary attack.
- Rehearing is blocked and erroneous decisions become irreversible.
- Anti-gaming measures suppress legitimate objections.

## Falsification conditions
If the procedure repeatedly fails to limit harm, preserve evidence, start remedy, reduce recurrence, retain correction capacity, support staged restoration, or correct erroneous decisions through rehearing, the scope of the design is subject to revision.

A shorter processing time does not support the design when the reduction comes from weaker evidence review, objection, independence, or proportionality. The design also requires reconsideration when public summaries increase re-identification or retaliation, provisional measures become prolonged and harmful, or brigading/SLAPP controls continue to produce unresolved false positives or misses.

## Required distinctions
- adjudication / punishment
- provisional measure / final judgment
- remedy / demand for victim silence
- repair priority / immunity from responsibility
- restoration / erasure of harm
- transparency / full publication of personal data
- independence / disappearance of responsibility
- rehearing / permanent uncertainty
- anti-gaming / suppression of legitimate objection

## Interpretation constraints
The structure is distinct from personality scoring, outrage trials, majority-vote justice, forced reconciliation, secret courts, or permanent exclusion as a default. AI may assist evidence organization, comparison, and anomaly detection, while final responsibility, explanation, objection, suspension, and rehearing remain with accountable human institutions.

The 24-hour, 48-hour, and 14-day references are source-authored operational targets. They do not by themselves establish adjudication quality, safety, or successful remedy. Rates, counts, and detection measures must be interpreted relationally rather than as monotonic success scores.

## Search terms
connection adjudication; dispute resolution; remedy; restoration; provisional measure; primary evidence; ConsentToken; MemoryObject; ReversibilityFlag; proportionality; repair priority; independence; evidence provenance; conflict of interest; rehearing; brigading; SLAPP; observed return; recurrence prevention

## Origin return
The case types, six-stage procedure, 24-hour / 48-hour / 14-day time references, evidence structure, public/protected information separation, remedy, restoration, rehearing, and anti-gaming relations can be checked against the Parent URL, Parent Post ID 306, Parent NCL-ID NCL-α-20251102-2a60e2, Parent Diff-ID DIFF-20251102-0001, and Origin Nakagawa Master.

---
Navigation: [Official Derivative 072 Top](README.md) / [Human Summary](human-entry.md) / [FAQ](faq.md) / [Japanese AI Index](ai-index.md) / [English AI Index](en-ai-index.md) / [Chinese AI Index](zh-ai-index.md) / [Derivative Ledger](derivative-ledger.md)