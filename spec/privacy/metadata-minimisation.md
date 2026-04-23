# Metadata Minimisation

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines normative anti-fingerprinting rules for supporting metadata in the minimal age-disclosure architecture.

Metadata minimisation is a hard conformance boundary. An implementation MUST NOT treat the omission of name or DOB as sufficient privacy compliance if supporting metadata remains correlating.

## 2. Controlled metadata classes
This specification applies to:
- assurance buckets
- issuer references
- timestamps and validity windows
- policy references
- proof-binding artifacts
- status references
- proof format references
- verifier retention records

## 3. Prohibited correlators
Normal-flow metadata MUST NOT include:
- stable verifier-visible holder identifiers
- stable verifier-visible root credential references
- reusable proof-binding artifacts
- unique token-specific status callback URIs
- holder-specific policy references
- session-specific policy references
- transaction-specific policy references beyond nonce and audience binding
- rare provenance strings that make the holder or issuer interaction unusually identifiable
- exact DOB, legal name, document number, or document image
- raw proof payloads retained by default
- verifier telemetry sufficient to reconstruct holder activity history

## 4. Allowed metadata classes
Normal-flow metadata MAY include only:
- `threshold_result`
- `assurance_bucket`
- `issuer_class`
- `issuer_trust_ref`
- `validity_window`
- `audience_binding`
- `nonce_binding`
- `binding_mode`
- `possession_proof`
- `status_evidence`
- `proof_format_ref`
- public `policy_ref`
- public `jurisdiction_ref`

Each allowed metadata class MUST be minimised to the least specific value compatible with verifier decisioning and trust validation.

## 5. Assurance coarsening
Normal-flow assurance metadata MUST use one of:
- `AB1`: basic age-threshold assurance
- `AB2`: standard governed age-threshold assurance
- `AB3`: high-assurance age-threshold assurance

Assurance metadata MUST NOT disclose:
- exact evidence source
- document type
- document number
- issuing office
- evidence inspection date
- rare issuer-specific provenance strings

Verifier requests MUST use `maximum_assurance_bucket`; they MUST NOT request detailed evidence provenance in the normal flow.

## 6. Issuer coarsening
Normal-flow issuer disclosure MUST default to issuer class:
- `A0`
- `A1`
- `A2`

Exact issuer identity MAY be used for trust validation only when issuer class and `issuer_trust_ref` are insufficient.

If exact issuer identity is used for trust validation, the verifier MUST NOT retain it as a default retained identifier unless retention is explicitly justified by verifier compliance rules.

Issuer references MUST NOT be holder-specific or token-specific.

## 7. Timestamp and validity coarsening
Verifier retention MUST use coarse time buckets by default:
- `V1` retention SHOULD use date-level buckets.
- `V2` and `VX` retention MAY use hour-level buckets where needed for audit or fraud review.

Raw cryptographic timestamps and exact proof-generation times MUST NOT be retained by default.

`validity_window` MAY be verifier-visible where needed to evaluate proof freshness, but it MUST be retained only at the permitted verifier-retention granularity.

## 8. Policy reference coarsening
`policy_ref` MUST identify a public policy, rule, service category, or governance requirement.

`policy_ref` MUST NOT contain:
- holder-specific identifiers
- account identifiers
- session identifiers
- transaction identifiers
- campaign or experiment identifiers that create avoidable fingerprinting

`purpose` MUST be human-reviewable and MUST NOT smuggle correlation handles.

## 9. Status reference minimisation
`status_evidence` MUST be one of:
- `none`
- batched status
- cacheable status
- relayable status
- issuer-trust-state reference
- root-credential-state reference
- wallet-compromise-state reference

Status references MUST NOT require token-specific live issuer callbacks in normal flow.

Status references MUST NOT let an issuer or status service observe ordinary verifier presentations.

## 10. Binding metadata minimisation
`B0` possession evidence MUST be transaction-bound and MUST NOT expose additional verifier-visible holder handles.

`B1` possession evidence MUST be verifier-scoped and fresh per transaction. Any verifier-scoped continuity material MUST be treated as privacy-sensitive and MUST NOT be retained as default telemetry.

`B2` possession evidence MUST be unlinkable and MUST NOT expose verifier-stable holder handles.

## 11. Metadata-driven conformance failures
An implementation MUST be treated as non-conformant if:
- allowed metadata is more granular than required for the verifier decision
- metadata permits cross-verifier correlation in normal flow
- proof-binding artifacts are reusable beyond the selected binding mode
- status references create presentation logs
- policy references contain hidden holder, session, or transaction identifiers
- verifier retention reconstructs holder activity history
- exact issuer identity is retained by default without governance justification

## 12. Profile-specific tightening
`Profile R` MUST satisfy the common metadata baseline and MUST treat `B1` continuity material as privacy-sensitive.

`Profile P` MUST satisfy the common metadata baseline and MUST treat verifier-stable binding metadata as non-conformant in normal flow.
