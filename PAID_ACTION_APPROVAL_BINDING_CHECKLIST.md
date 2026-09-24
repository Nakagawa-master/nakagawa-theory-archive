# Paid-Action Approval Binding Checklist

Use this checklist when a command can create a billed, externally visible, destructive, or otherwise consequential action.

The core distinction is simple:

```text
approval of a command or plan reference
!=
approval of the exact consequential action that will execute
```

## Minimum contract

Before the consequential API call:

1. **Assemble the exact action snapshot**
   - exact item set
   - destination / provider
   - frozen model or execution settings
   - relevant limits
   - estimated cost when available

2. **Canonicalize it**
   - serialize the consequential fields deterministically
   - compute a stable digest

3. **Show a human-readable summary**
   - what will happen
   - how many items
   - where it will happen
   - what settings are frozen
   - estimated cost and known uncertainty

4. **Bind approval to the snapshot**
   - persist the approved digest with the approval record
   - do not treat approval of a file path, command string, or old plan version as equivalent

5. **Revalidate immediately before execution**
   - reassemble or re-hash the consequential snapshot
   - confirm current policy / permissions / provider state where relevant

6. **Fail closed on material drift**
   - exact match: execute once
   - changed item set, destination, settings, cost-relevant inputs, or policy state: approval is stale
   - require fresh review instead of silently reusing the old approval

## Focused regression test

```text
prepare snapshot A
→ approve A
→ change plan/settings to snapshot B
→ attempt execution
→ old approval must not authorize B
```

Also test replay and response-loss paths so the same approval cannot accidentally create the action twice.

## Why a cost limit is not enough

A maximum-cost gate answers:

> “Is the estimate below this threshold?”

It does not necessarily answer:

> “Did the person review and approve this exact set of actions?”

Both controls can be useful, but they protect different boundaries.

## Public implementation case

A concrete discussion of this boundary is visible in Qwen Code's Batch API PR:

- [QwenLM/qwen-code#12492](https://github.com/QwenLM/qwen-code/pull/12492)
- [Nakagawa-master proposal](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552)
- [third-party closeout preserving it as a product decision](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817836928)
- [bounded follow-up](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817960767)

The public record currently confirms independent recognition of the boundary. It does **not** yet confirm adoption or implementation in Qwen Code.

## Related reusable checks

- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)
- [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md)
- [Real-World Impact](REAL_WORLD_IMPACT.md)
