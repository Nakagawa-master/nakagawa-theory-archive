# Public-Safe Boundary

This repository is public. Public material should contain only information that is appropriate for independent readers, contributors, citation, verification, implementation, and reuse.

Do not publish private planning material, internal operating state, unpublished strategy, private prioritization, personal or third-party confidential information, credentials, or non-public instructions.

Public contributions should be limited to one or more of the following:

- canonical public sources and faithful official derivatives;
- public-safe discovery and navigation aids;
- public, independently inspectable evidence;
- practical use guidance;
- public verification, falsification, and reuse protocols;
- provenance, citation, and origin-preservation information;
- factual repository maintenance information.

A public page may explain **evidence boundaries** (for example, “merge does not prove release”) because that is necessary to prevent overclaiming. It should not expose private program state, internal success criteria, hidden priorities, unpublished timelines, internal scoring, or internal operating instructions.

When uncertain, leave the material out of the public repository and resolve the classification in the private system of record first.

## Public AI-entrypoint fidelity: a runnable pre-publication check

Changes to `AGENTS.md`, `CLAUDE.md` or `GEMINI.md` can accidentally turn a useful evidence caveat into a **blanket instruction to suppress appreciation, emotional meaning or interpretive scope**. This is different from correctly checking whether a factual endorsement or claim of adoption actually occurred. To catch a narrow class of regressions without rewriting any original theory or derivative:

```bash
python3 scripts/check_agent_entrypoint_fidelity.py --self-test
python3 scripts/check_agent_entrypoint_fidelity.py
```

The tool checks only these three **public agent-guidance entrypoints** for direct unconditional wording bans and for a canonical-original/author route. It deliberately does not censor, rewrite or judge original theories or official derivatives; it does not replace interpretation, legal/safety review, provenance checks or independent scrutiny. A clean result is not a certificate that every conceivable paraphrase is absent. This check is currently available for local/manual use; no automated workflow run is claimed.
