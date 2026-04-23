# Verifier Compliance and Retention

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines verifier retention, prohibited telemetry, audit records, and conformance consequences for the minimal age-disclosure architecture.

## 2. Default retained fields
By default, a verifier MAY retain only:
- decision outcome
- approved coarse time bucket
- policy reference
- bounded audit reason
- verifier class
- binding mode
- exception flag

The default time bucket MUST be:
- date-level for `V1`
- date-level for `V2`, unless hour-level granularity is needed for audit or fraud review
- hour-level for `VX` exceptional records where needed for audit

## 3. Forbidden default retention
By default, a verifier MUST NOT retain:
- raw proof payload
- raw proof transcript
- stable holder data
- stable root credential references
- reusable proof-binding artifacts
- unique status callback references
- fine-grained timestamps beyond approved granularity
- exact issuer identity unless explicitly justified by trust-validation need
- telemetry sufficient to recreate holder activity history

## 4. `B1` retention rule
For `B1`, any verifier-scoped continuity material MUST be treated as privacy-sensitive.

A verifier MUST NOT retain `B1` continuity material as default telemetry.

If retention of `B1` continuity material is explicitly justified, it MUST be:
- verifier-scoped
- purpose-limited
- access-controlled
- time-limited
- auditable

## 5. Exceptional retention
Exceptional retention MAY occur only where:
- an explicit lawful or governance basis exists
- the retention scope is bounded
- the retention period is declared
- the event is auditable
- the wallet red-path UX was shown

Exceptional retention MUST follow `spec/verifier-policy/exception-governance.md`.

## 6. Telemetry rule
For conformance purposes, telemetry includes any recorded fields, analytics, or derived data that can reconstruct holder activity patterns beyond the documented governance need.

Telemetry that reconstructs holder activity histories MUST be treated as non-conformant even if direct identity fields are absent.

## 7. Conformance rule
A verifier MUST be treated as non-conformant if it retains by default:
- raw proof payloads
- raw proof transcripts
- reusable binding artifacts
- unique status references
- fine-grained timestamps
- correlating verifier telemetry
- exceptional-flow evidence without the required lawful-basis fields
