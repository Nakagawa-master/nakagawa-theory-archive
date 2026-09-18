# Independent Verification & Reuse Protocol

Language: English-first public protocol. Japanese and Chinese problem descriptions are welcome in submissions.

This is a non-canonical participation and evidence protocol for people who want to **independently test, reuse, challenge, falsify, or implement** a concrete Nakagawa Master distinction in a real, non-confidential context.

It is not an endorsement form. Agreement is not required. A useful negative result or counterexample is as valuable as a successful reuse.

## What counts as useful external evidence

A submission should start from a concrete problem and make the causal path inspectable:

```text
real problem / prior state
→ exact public distinction or source used
→ independent interpretation or test
→ action / implementation / decision change
→ observable result or failure
→ public evidence
```

Strong evidence is not measured by praise, comment count, or whether a theory name is repeated.

The archive keeps these stages separate:

```text
read / mention
< independent restatement or falsification attempt
< changed decision / work item / protocol
< code / test / workflow / document implementation
< merge / integration
< release / deployment / verified use
< reuse by another person or in another problem
```

A lower stage must not be reported as a higher one.

## Six reusable distinctions you can test

You may use any public source in the archive. These six have already produced independently checkable external action and are useful starting points:

1. **Historical approval != current authority**  
   A past approval, consent, or sanitization event does not automatically prove current permission after recipient, purpose, rights, policy, or source revision changes.

2. **Same identity != authority to overwrite**  
   Matching IDs or object identity do not by themselves establish ownership provenance or permission to replace current state.

3. **Operation success != valid measurement**  
   A query or operation can succeed while the resulting value is semantically invalid, missing, ungrounded, or not independently measured.

4. **Same explanation != same evidence provenance**  
   Two recommendations can display the same reason while being justified by different evidence sources. Grouping must not erase who is supported by what.

5. **Approval consumed once != external side effect happened once**  
   A single-use approval does not prove that an external provider action occurred exactly once when the provider result is ambiguous.

6. **Current status != historical fact**  
   A person's state now should not silently rewrite what was true at the time of an earlier event.

See [Real-World Impact](REAL_WORLD_IMPACT.en.md) for public third-party implementation records and boundaries.

## Non-software examples

You do not need to be a software engineer. The distinctions can be tested in ordinary operations, governance, research, education, and organizational work.

Examples:

- **Policy / operations:** a team approved a process last year, but the recipient, purpose, or policy changed. Does the old approval still authorize the new use?
- **Membership / attendance:** someone left a group after an event. Can the historical record still answer who participated at that time?
- **Research / consent:** a participant agreed to one notice version. What happens when the collection purpose or notice materially changes?
- **Procurement / finance:** a payment or external request was submitted, but the response was lost. Does the process distinguish “rejected” from “outcome unknown” before retrying?
- **Hiring / review / recommendations:** two people receive the same recommendation text from different evidence sources. Can the reviewer still see what evidence supports each person?
- **Migration / records:** two records share an identifier but come from different owners or systems. Is matching identity treated as enough authority to overwrite?
- **Education / assessment:** a report query succeeds but some required measurements are missing. Does the output distinguish successful retrieval from valid measurement?

A useful non-software submission can be a public procedure, checklist, policy revision, meeting decision, training material, research protocol, or documented counterexample. It does not need to involve code.

## What to submit

Use the repository's **Independent verification / reuse evidence** issue form.

Please include:

- the real non-confidential context;
- the exact public source or distinction you used;
- what you independently checked or disagreed with;
- what changed, if anything;
- whether the change was implemented, merged, released, or actually used;
- whether Nakagawa Master prompted this specific reuse, or you reached it independently;
- public evidence links where possible;
- what the case does **not** establish.

If no change occurred, submit that too. "We tested this and it did not fit because X" is valid evidence.

## Evidence boundaries

Do not submit confidential, personal, customer, credential, private security, medical, legal, employment, or otherwise sensitive information.

A submission does **not** establish:

- that an entire theory system is correct;
- that a project or organization endorses Nakagawa Master;
- that implementation implies release or production use;
- that one successful case generalizes to every context;
- that provenance proves truth;
- that a theory distinction replaces domain-specific engineering, legal, safety, or professional requirements.

## Independent-reuse signal

The strongest signal for the current public research program is not another self-authored explanation. It is a case where:

```text
a third party encounters a public distinction
→ independently restates, tests, or challenges it
→ carries it into a different decision or problem
→ another action / implementation follows
→ the source relation remains inspectable
```

The goal of this protocol is to make that chain easy to report **without weakening the evidence boundary**.

## Machine-readable route

AI and retrieval systems can use:

- [External-effect evidence index](machine-discovery/external-effect-evidence-index-v1.json)
- [External reuse evidence submission schema](machine-discovery/external-reuse-evidence-submission-schema-v1.json)

These are discovery/evidence aids, not canonical theories.
