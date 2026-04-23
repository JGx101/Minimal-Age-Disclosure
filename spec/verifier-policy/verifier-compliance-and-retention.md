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

## 4. Metadata reference retention
`issuer_trust_ref` MAY be retained only as a coarse public registry reference, public trust-set reference, or bounded reason code needed to justify acceptance.

A verifier MUST NOT retain token-specific, holder-specific, credential-specific, or exact issuer-resolved values by default.

`proof_format_ref` MAY be retained only at proof-family, governed-profile, or major-version granularity.

A verifier MUST NOT retain proof library build, implementation vendor, parameter set, or experimental profile values where they are rare provenance strings under `spec/privacy/metadata-minimisation.md`.

`status_evidence` MAY be retained only as status class plus public batch, cache, relay, trust-state, root-state, or wallet-compromise-state epoch.

A verifier MUST NOT retain unique status callback URIs, raw status responses, issuer-visible query artifacts, or token-specific freshness checks by default.

These retained reference fields MUST NOT be combined with timestamp, policy, jurisdiction, or proof-format fields to reconstruct holder activity histories.

## 5. `B1` retention rule
For `B1`, any verifier-scoped continuity material MUST be treated as privacy-sensitive.

A verifier MUST NOT retain `B1` continuity material as default telemetry.

If retention of `B1` continuity material is explicitly justified, it MUST be:
- verifier-scoped
- same-verifier and same-policy-purpose scoped
- purpose-limited
- access-controlled
- time-limited
- auditable

`B1` continuity material MUST NOT be joined into general account analytics, advertising profiles, fraud-score histories, cross-service identity graphs, or unrelated device fingerprinting datasets.

`B1` continuity material MUST be deleted or irreversibly de-linked when the declared anti-sharing purpose or retention period expires.

## 6. Exceptional retention
Exceptional retention MAY occur only where:
- an explicit lawful or governance basis exists
- the retention scope is bounded
- the retention period is declared
- the event is auditable
- the wallet red-path UX was shown

Exceptional retention MUST follow `spec/verifier-policy/exception-governance.md`.

Extra fields collected during an exceptional flow MUST NOT be retained under the default retained-fields rule in Section 2. They MAY be retained only under the `evidence_handling` mode declared in the exceptional request and response.

Exceptional evidence MUST NOT be copied into default telemetry, analytics, product logs, fraud feature stores, model-training datasets, or account profile enrichment.

If exceptional evidence is retained, the verifier MUST retain the relationship between:
- the lawful-basis code and reference
- the jurisdiction reference
- the normal-path insufficiency result
- the requested extra fields
- the declared evidence-handling mode
- the retention period
- the reviewer or appeal reference

If that relationship cannot be reconstructed during audit, the retained exceptional evidence MUST be treated as non-conformant.

## 7. Telemetry rule
For conformance purposes, telemetry includes any recorded fields, analytics, or derived data that can reconstruct holder activity patterns beyond the documented governance need.

Telemetry that reconstructs holder activity histories MUST be treated as non-conformant even if direct identity fields are absent.

## 8. Conformance rule
A verifier MUST be treated as non-conformant if it retains by default:
- raw proof payloads
- raw proof transcripts
- reusable binding artifacts
- unique status references
- fine-grained timestamps
- correlating verifier telemetry
- exceptional-flow evidence without the required lawful-basis fields
- exceptional-flow evidence outside the declared evidence-handling mode or retention period
- exact issuer-resolved values, rare proof-format values, raw status responses, or token-specific freshness artifacts outside explicit exceptional governance

## 9. Fixture-backed retention review
The first retention automation SHOULD inspect fixture records before service code exists.

A default verifier retention fixture MUST contain only:
- decision outcome
- approved coarse time bucket
- policy reference
- bounded audit reason
- verifier class
- binding mode
- exception flag
- non-unique trust or status reference where needed for audit

A default verifier retention fixture MUST NOT contain raw proof payloads, raw proof transcripts, `B1` continuity material, unique status references, exact issuer identity, fine-grained timestamps, root credential references, stable holder data, or reusable proof-binding artifacts.

The fixture `fixtures/conformance/verifier-retention-default-record.json` is the baseline positive example. Negative retention examples MUST identify `over_retention` as their expected failure class.
