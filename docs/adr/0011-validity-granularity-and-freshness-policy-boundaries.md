# ADR-0011: Validity Granularity And Freshness Policy Boundaries

## Status
Proposed

## Date
2026-04-23

## Context
The architecture prefers bounded validity and no routine live issuer callbacks, but still allows freshness-sensitive behavior where justified.

## Contradiction being resolved
The repository has not yet decided the allowed validity granularity, freshness triggers, and verifier-class permissions for status-related checks.

## Why the specs cannot safely decide this yet
This decision affects:
- metadata minimisation
- replay protection assumptions
- status privacy
- Profile R deployability

## Options under consideration
- expiry-only common baseline with narrow freshness exceptions
- verifier-class-based freshness permissions
- profile-specific freshness and status rules

## Dependent files and consequences
- claim profile
- verifier policy
- trust model
- metadata minimisation
- conformance checklist
- revocation/status analysis
