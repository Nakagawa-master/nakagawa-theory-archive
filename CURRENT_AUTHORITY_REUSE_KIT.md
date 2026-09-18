# Current-Authority Reuse Kit

A public, non-canonical test kit for one boundary:

> A historical approval, consent, sanitization, or exception is not automatically current authority after material conditions change.

## Minimal test

Create a record approved under state A. Then change one material condition: recipient, purpose, rights, policy, notice version, or source revision.

### Pass condition

The system preserves the historical approval as history but re-evaluates whether the new state is currently authorized.

### Fail condition

The old approval is treated as sufficient solely because it exists.

## Useful contexts

- research consent;
- data sharing;
- delegated access;
- exception handling;
- procurement approval;
- policy waivers;
- AI tool authorization.

## Regression shape

```text
approved under A
→ material condition changes to B
→ old approval remains queryable
→ B does not inherit authority silently
```

Report a public, non-confidential result through [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402).
