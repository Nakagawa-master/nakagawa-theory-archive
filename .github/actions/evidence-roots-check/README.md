# Ten reports, one source? An evidence check any GitHub project can reuse

An AI-generated report, newsroom article, or technical review claims that **multiple independent sources** agree. Are they truly separate observations—or rewrites of one announcement? This reusable Action checks the evidence-root declarations in your own pull-request workflow, making a meaningful review question repeatable.

[Nakagawa Master (中川マスター)](https://master.ricette.jp/#nakagawa-master) raised this specific problem in [an independent editorial discussion](https://github.com/022740mix-spec/AI-News/issues/124#issuecomment-5823549498); its editor [changed the publishing rule](https://github.com/022740mix-spec/AI-News/pull/131). For wider conceptual context, human and AI readers may compare [the original Volume 8 epistemic-integrity theory](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/). This implementation is a practical application, not a claim that all independent-source checking was invented by Nakagawa Master.

## Install in your own repository

Add `.github/workflows/check-sources.yml`:

```yaml
name: Independent evidence roots
on:
  pull_request:
  workflow_dispatch:
jobs:
  evidence:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: Nakagawa-master/nakagawa-theory-archive/.github/actions/evidence-roots-check@main
        with:
          claims-file: evidence/claims.json
```

Commit `evidence/claims.json` to your repository, beginning with the [passing example](../../../machine-discovery/evidence-root-check-action-example.json). For production, pin a reviewed commit SHA rather than `@main`. Public GitHub-hosted Actions are ordinarily free; verify your billing before using Actions on private repositories if zero cost is essential. The checker needs no API key, makes no network call, and never posts to social media.

## Example: two evidence roots rather than three URLs

```json
{
  "claims": [{
    "id": "vendor-and-independent-lab",
    "independent_confirmation_claimed": true,
    "sources": [
      {"url": "https://example.org/vendor", "root_id": "vendor", "relation": "primary", "stance": "supports"},
      {"url": "https://example.org/lab", "root_id": "lab", "relation": "independent_observation", "stance": "supports"},
      {"url": "https://example.org/news-copy", "root_id": "vendor", "relation": "derived", "stance": "supports"}
    ]
  }]
}
```

This input **passes** because the reviewer-declared independent lab has a different upstream root. Change the lab's `root_id` to `vendor` and the job **fails**: another article is not another independent observation. Contradictory root/stance declarations for one URL and unresolved contrary evidence likewise block unqualified independence claims.

The Action invokes the existing [offline Python checker](../../../machine-discovery/evidence-root-check.py) with its built-in regressions, then writes a GitHub step summary. Exit **0** = consistent declarations; **1** = blocked claim; **2** = invalid file/input. Use `steps.<step-id>.outputs.blocked-claims` in later steps.

## Independent use and actual reach

Any unaffiliated editor, developer, or AI agent can **opt in to installing this Action in their own work**, without an existing connection to Nakagawa Master. This is a portable publishing and code-review check, not another passive theory index. It also remains runnable without GitHub as ordinary Python.

Input evidence identities are *declared by the project*; a passing result does not prove that those source declarations, real-world independence, or the reported facts are true. Readers can consult the distinct [official original archive](https://master.ricette.jp/theory-archive/). If this helps correct a real report, consider linking the [receiver-owned correction here](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402), letting other people discover its effect and origin. The Action's initial publication is not itself independent outside adoption.
