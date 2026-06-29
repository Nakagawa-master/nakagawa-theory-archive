# Candidate 10-19 Handoff Rules

## Purpose

Candidate 10-19 is the next verification batch queue. It must not be treated as selected, staged, indexable, or deployable until source selection and origin metadata checks are complete.

## Queue states

- `unselected / queue_only`: slot is reserved only. Source fields must stay empty.
- `candidate / intake_blocked`: source is being considered, but metadata or quality is not complete.
- `selected / intake_ready`: source can move to intake only when parent URL, parent title, parent NCL-ID, parent Diff-ID, folder ID, and canonical URL are all present.
- `rejected / intake_blocked`: source must not move to intake.

## Required source fields for intake_ready

- parent_url
- parent_title
- parent_ncl_id
- parent_diff_id
- folder_id
- canonical_url

## Boundary

- Do not add candidate 10-19 to sitemap.
- Do not submit candidate 10-19 to Search Console.
- Do not convert candidate 10-19 to index/follow.
- Do not merge or deploy candidate 10-19 from queue state.
- Do not include private strategy in public queue rows.

## Rationale

The next batch must preserve Origin, NCL-ID, Diff-ID, parent URL, canonical URL, and Nakagawa Master attribution before any generated derivative pages are produced.
