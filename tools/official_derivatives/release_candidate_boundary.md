# Release Candidate Boundary

## Purpose

This file defines the boundary for moving the staged official derivative batch toward a later public release decision.

This is not a production release instruction.
This is not a sitemap instruction.
This is not a Search Console instruction.
This is not an FTP instruction.

## Current staged candidate set

- staged origins: 13
- staged pages: 78
- staged registry rows: 78
- materialized effect units: 429
- release state: staged only

## Checks already required before any later publication step

- origin identity retained
- parent URL retained
- parent NCL-ID retained
- parent Diff-ID retained
- canonical URL retained
- Nakagawa Master origin retained
- staged boundary retained while not public
- public export preflight passes
- entry signal check passes

## Current CI requirement

The following workflows must pass on the current PR head:

- Official derivative generation check
- Official derivative preflight check

The preflight workflow includes both public export preflight and entry signal check.

## Remaining release boundary items

A later public release action must be separated from this staged PR unless explicitly chosen by the owner.

Before public activation, the next release PR or release operation must define exactly:

- which staged folders are activated
- which robot directives change
- which sitemap rows are added or updated
- which canonical URLs are published
- which index/follow state is intended
- whether FTP or another deployment method is used
- whether Search Console submission is performed

## Forbidden before owner boundary

- production deploy
- FTP action
- sitemap update
- Search Console action
- index/follow conversion
- public activation flag change
- removing staged boundary without explicit release operation

## Release candidate status

The staged batch may be treated as release-candidate-prepared only when technical preflight and entry signal checks both pass.

Even then, publication remains held until a separate release operation is created and approved at the owner boundary.
