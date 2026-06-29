# Activation Flow Contract

This contract fixes the operating path from origin intake to activation-ready validation.

## Flow

1. origin_intake
2. origin_identity_check
3. derivative_generation
4. derivative_registry_update
5. quality_gate_check
6. effect_surface_check
7. effect_readiness_check
8. activation_ready_check
9. owner_boundary_action

## Required boundaries

- no_owner_boundary_skip: true
- no_quality_gate_skip: true
- no_origin_identity_skip: true
- no_registry_skip: true
- no_publication_before_ready: true

## Meaning

The system is useful only if it can move in this order without redesign, manual page-by-page repair, or weakened origin preservation.
