# ADR-0014: Verifier Audit Record Minimum

## Status
Accepted

## Date
2026-04-23

## Context
The governance model requires meaningful audit and sanctions, but the privacy model requires minimal verifier retention.

## Decision
Default verifier retention MAY include only:
- decision outcome
- approved coarse time bucket
- policy reference
- bounded audit reason
- verifier class
- binding mode
- exception flag

Exceptional audit records MUST include the fields defined by exception governance and MUST NOT retain raw proof payloads or unnecessary identity evidence by default.

Raw proof payloads, raw proof transcripts, reusable binding artifacts, unique status references, and fine-grained timestamps MUST NOT be retained by default.

## Consequences
- Verifiers have enough retained evidence for basic governance review.
- Retention remains narrow enough to reduce tracking risk.
- Conformance can test default retention directly.
