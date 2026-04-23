# ADR-0011: Validity Granularity And Freshness Policy Boundaries

## Status
Accepted

## Date
2026-04-23

## Context
The architecture prefers bounded validity and no routine live issuer callbacks, but still allows freshness-sensitive behavior where justified.

## Decision
The canonical freshness requirement values are:
- `none`
- `issuer_trust_state`
- `root_credential_state`
- `wallet_compromise_state`

Token-specific live issuer callbacks MUST NOT be used in normal flow.

Verifier retention MUST use coarse time buckets by default:
- date-level for `V1`
- date-level for `V2`, unless hour-level granularity is needed for audit or fraud review
- hour-level for `VX` exceptional records where needed for audit

Raw cryptographic timestamps MUST NOT be retained by default.

## Consequences
- Freshness is explicit without reopening issuer-observability risk.
- Status checks attach to trust/root/wallet state, not ordinary presentations.
- Metadata tests can evaluate timestamp and freshness granularity.
