# ADR-0009: Canonical Ownership Of The Verifier Request Object

## Status
Accepted

## Date
2026-04-23

## Context
Earlier docs described request fields in both the claim profile and verifier policy.

## Decision
`spec/claim-profile/age-threshold-proof-profile.md` owns the canonical abstract request and response object shapes.

`spec/verifier-policy/minimal-disclosure-verifier-policy.md` constrains verifier behavior and wallet handling of those objects.

No separate request-object spec is introduced in this pass.

## Consequences
- Object drift is reduced.
- Conformance can test object shape against the claim profile and request behavior against the verifier policy.
- Prototype planning can reference one canonical object owner.
