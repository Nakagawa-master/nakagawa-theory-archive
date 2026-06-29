# Activation Runbook

This runbook converts the flow tables into an executable order of judgment.

## Source tables

- activation_flow_contract.md
- stage_io.tsv
- stage_conditions.tsv

## Execution order

1. Read stage_io.tsv.
2. Read stage_conditions.tsv.
3. Confirm both files use the same stage order.
4. For each stage, confirm the required artifact exists or is intentionally pending.
5. Move forward only when the stage ok_key is satisfied.
6. Stop when the stage stop_key is present.
7. Keep owner_boundary_action as the final boundary before external action.

## Fixed principle

The runbook must reduce manual judgment, protect origin identity, preserve quality gates, and prevent page-by-page repair from becoming the operating model.
