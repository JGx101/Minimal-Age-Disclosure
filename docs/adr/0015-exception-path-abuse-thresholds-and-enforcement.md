# ADR-0015: Exception-Path Abuse Thresholds And Enforcement

## Status
Accepted

## Date
2026-04-23

## Context
The exceptional path must remain outside normal conformance and must not become the commercial default.

## Decision
`V1` verifiers MUST NOT invoke exceptional disclosure.

Any exceptional request missing required lawful-basis fields MUST be treated as non-conformant.

Exceptional use above `5%` of a verifier's age-check volume in a calendar month MUST trigger governance review.

Exceptional use above `10%` of a verifier's age-check volume in a calendar month MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Repeated review triggers across two consecutive months MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

## Consequences
- Exception normalization is directly testable.
- Verifier classes have concrete eligibility rules.
- Governance review and conformance failure are separated by explicit thresholds.
