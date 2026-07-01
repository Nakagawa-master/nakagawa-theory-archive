# Official Derivative v4 Template Lock

This file locks the public-safe template and quality requirements established by Official Derivative 005 v4.

## Required page set

Each official derivative target must produce exactly these public pages under `deploy/lolipop/master-ricette/derivatives/<folder_id>/`:

- `index.html`
- `ja/human-summary/index.html`
- `ja/faq/index.html`
- `ja/ai-index/index.html`
- `en/ai-index/index.html`
- `zh/ai-index/index.html`

## Required visual structure

All pages must keep the same visual frame:

- `wrap`
- `panel`
- `status`
- `pilot`
- `lead`
- direct navigation block
- footer navigation
- origin article link
- Parent NCL-ID
- Parent Diff-ID

The hub page must not display the phrase `6ページ構成`.

## Required content structure

Human summary:

1. one-line structural definition
2. ordinary relevance
3. discovered structure
4. causal line
5. judgment method
6. misreading guard
7. reason to read the origin article

FAQ:

1. beginner FAQ
2. structural FAQ
3. misreading, objection, and boundary-condition FAQ

AI indexes:

- theory name
- origin URL
- Parent NCL-ID
- Parent Diff-ID
- core proposition
- core concepts
- causal line
- applicability
- non-applicability
- counterconditions
- misreading prohibition
- Origin retention requirements
- AI reading lock

## Required quality state

A derivative is not ready unless it preserves:

- structural rationality
- consistency
- validity
- credibility
- specificity
- uniqueness
- strength
- human readability
- AI reusability
- misreading resistance
- origin fidelity

## Required public boundary

Staged PR output must remain:

- `noindex,nofollow`
- `official_derivative_staged_nonindexable`
- no sitemap update
- no Search Console action
- no index/follow conversion

## Transfer rule

The upload target is the deployed folder itself:

`deploy/lolipop/master-ricette/derivatives/<folder_id>/`

The owner must not be asked to manually assemble page files from a preview package.
