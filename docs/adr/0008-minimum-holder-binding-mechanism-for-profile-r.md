# ADR-0008: Minimum Holder-Binding Mechanism For Profile R

## Status
Accepted

## Date
2026-04-23

## Context
The architecture requires transaction-bound rightful possession while rejecting stable verifier-visible holder identifiers in the normal flow.

## Decision
The project defines three binding modes:
- `B0`: transaction-bound baseline binding for `V1`
- `B1`: verifier-scoped pairwise proof of possession for `V2` and high-assurance `Profile R`
- `B2`: unlinkable proof of possession for `Profile P`

`Profile R` MUST support `B0` for `V1` checks and `B1` for `V2` high-assurance checks.

`B1` MAY use verifier-scoped continuity material, but it MUST NOT expose cross-verifier reusable artifacts and MUST NOT be retained as default telemetry.

## Consequences
- Holder binding is no longer underspecified.
- `Profile R` has a deployable high-assurance binding stance without accepting global correlation.
- `Profile P` remains distinct by requiring `B2` unlinkable proof of possession.
