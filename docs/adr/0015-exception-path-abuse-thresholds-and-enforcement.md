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

Exceptional requests MUST use a controlled lawful-basis vocabulary and MUST include a concrete lawful-basis reference.

Exceptional requests MUST pass a normal-path insufficiency test before higher disclosure is requested.

Exceptional use above `5%` of a verifier's age-check volume in a calendar month MUST trigger governance review.

Exceptional use above `10%` of a verifier's age-check volume in a calendar month MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Repeated review triggers across two consecutive months MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Governance review MUST record the trigger, independent reviewer, outcome, remediation, and sanction state.

Sanctions MUST escalate from warning, to formal review, to temporary non-conformance, to trust withdrawal recommendation.

Services designed to use exceptional disclosure as the ordinary access path MUST be treated as exception-by-design and MUST NOT be presented as conformant normal flow.

## Consequences
- Exception normalization is directly testable.
- Verifier classes have concrete eligibility rules.
- Governance review and conformance failure are separated by explicit thresholds.
- Exception-by-design services are distinguishable from one-off step-up.
- Evidence retention is governed by the exceptional request and verifier-retention relationship.
