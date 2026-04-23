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

## Open dependency
The exact freshness and validity boundaries remain subject to [ADR-0011](../adr/0011-validity-granularity-and-freshness-policy-boundaries.md).
