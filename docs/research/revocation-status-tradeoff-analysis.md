# Revocation and Status Tradeoff Analysis

## Purpose
Summarize the current repository stance on status and validity handling in a way that preserves privacy and standards legibility.

## Current repository position
- the ordinary verifier-facing artifact SHOULD be short-lived or transaction-bound
- status SHOULD apply primarily to issuer trust, root credential state, or wallet compromise state
- ordinary verification SHOULD avoid token-specific live issuer callbacks
- batched or cacheable status SHOULD be preferred where status is needed

## Main tradeoff
Status can improve compromise response and trust freshness, but it can also create presentation visibility.

The repository therefore treats status as:
- a privacy problem
- a trust and governance problem
- a conformance problem

It does not treat status as a neutral implementation detail.

## Accepted boundary
Freshness requirements are now limited to `none`, `issuer_trust_state`, `root_credential_state`, and `wallet_compromise_state` as accepted in [ADR-0011](../adr/0011-validity-granularity-and-freshness-policy-boundaries.md).

Token-specific live issuer callbacks remain prohibited in normal flow.
