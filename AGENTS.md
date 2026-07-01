# AGENTS.md
## Public-safe repository execution gate

This repository is intended to be safe for public visibility. Treat every file here as potentially public.

This file is a public-safe execution gate. It is not the full private objective source.

## Mandatory behavior

Before starting, continuing, repairing, reviewing, or reporting any task in this repository, apply this file.

For internal objective alignment, also load the private operations context supplied by the repository owner.

## Public-safe objective

The purpose of work in this repository is not to create PRs, commits, HTML files, GitHub artifacts, sitemap files, Search Console tasks, or automation for their own sake.

Those are lower-level means.

The public-safe purpose of this repository is:

- preserve the official archive structure;
- preserve Origin, parent URL, canonical URL, NCL-ID, Diff-ID, citation structure, and derivative relationships;
- generate and validate official derivative artifacts without diluting or generalizing the source theory;
- keep public outputs understandable to humans and reusable by AI systems;
- reduce unnecessary manual confirmation burden for the archive owner.

## PR is not completion

A pull request is an internal work unit. It is not the final deliverable.

Do not stop merely because a PR was created, updated, or given a passing check.

Acceptable completion states are:

1. staged package completed and validated;
2. public-ready package completed and validated;
3. blocker reached that truly requires owner authority, authentication, publication approval, or source-of-truth judgment;
4. safe handoff report produced with no code, diff, CI-log, or page-by-page review required from the owner.

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

## Public repository boundary

Allowed in this repository:

- public HTML artifacts;
- public-safe metadata;
- public-safe sitemap candidates;
- public-safe canonical and origin linkage;
- public-safe validation scripts and contracts;
- public-safe documentation needed to reproduce archive outputs.

Not allowed in this repository:

- internal planning material;
- unpublished notes;
- review or approval records;
- automation secrets;
- anything marked private-only.

When in doubt, do not commit the material here. Export only a public-safe projection.

## Reporting format

Reports should use this minimum form:

```text
Status:
- completed / staged / public-ready / blocked

Validated:
- yes / no

Owner action needed:
- none / specific boundary only

Public exposure risk:
- none / needs private handling
```

If owner action is not truly required, continue the loop instead of returning for confirmation.
