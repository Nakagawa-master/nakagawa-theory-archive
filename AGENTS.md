# AGENTS.md
## Public-safe persistent execution gate

This repository is intended to function as a public or public-safe archive repository. Therefore, do not place private strategy, internal roadmaps, influence targets, comparison-target names, unpublished plans, prompts, queues, review ledgers, Zapier payloads, or approval workflows in this repository.

Private operational strategy belongs in:

- `Nakagawa-master/nakagawa-archive-tools`
- especially under `private-derivatives/`

## Mandatory behavior for Codex / Agent work

Before starting, continuing, repairing, reviewing, or reporting any task in this repository, apply this file as the repository-level execution gate.

## Public-safe objective

The purpose of work in this repository is not to create PRs, commits, HTML files, GitHub artifacts, sitemap files, Search Console tasks, or automation for their own sake.

Those are lower-level means.

The public-safe purpose of this repository is:

- preserve the official archive structure;
- preserve Origin, parent URL, canonical URL, NCL-ID, Diff-ID, citation structure, and derivative relationships;
- generate and validate official derivative artifacts without diluting or generalizing the source theory;
- keep public outputs understandable to humans and reusable by AI systems;
- prevent accidental exposure of private operational strategy;
- reduce the archive owner’s manual confirmation burden.

## PR is not completion

A pull request is an internal work unit. It is not the final deliverable.

Do not stop merely because a PR was created, updated, or given a passing check.

Acceptable completion states are:

1. staged package completed and validated;
2. public-ready package completed and validated;
3. blocker reached that truly requires owner authority, authentication, publication approval, or private/source judgment;
4. safe handoff report produced with no code/diff review required from the owner.

## Loop rule

For every task, run the loop:

1. detect the problem;
2. inspect the source files;
3. implement the fix;
4. run validation;
5. repair failures;
6. re-run validation;
7. package the result;
8. report only completion state, validation result, and unavoidable owner-boundary items.

Do not ask the owner to review code, diffs, CI logs, every generated page, or routine technical details.

## Public / private boundary

Allowed in this repository:

- public HTML artifacts;
- public-safe metadata;
- public-safe sitemap candidates;
- public-safe canonical and origin linkage;
- public-safe validation scripts and contracts;
- public-safe documentation needed to reproduce archive outputs.

Not allowed in this repository:

- private strategy;
- recognition roadmaps;
- influence acceleration plans;
- comparison-target names;
- unpublished planning;
- prompts that expose internal strategy;
- Zapier payloads or secrets;
- review queues and approval ledgers;
- anything marked private-only.

When in doubt, put the material in `nakagawa-archive-tools/private-derivatives/` and export only a public-safe projection here.

## Reporting format

Reports should use this minimum form:

```text
Status:
- completed / staged / public-ready / blocked

Validated:
- yes / no

Owner action needed:
- none / specific boundary only

Private material exposure risk:
- none / needs private-repo handling
```

If owner action is not truly required, continue the loop instead of returning for confirmation.
