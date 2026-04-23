# ADR-0010: Assurance Bucket Taxonomy And Request Semantics

## Status
Accepted

## Date
2026-04-23

## Context
The architecture requires bounded assurance metadata that remains useful to verifiers without becoming a fingerprinting surface.

## Decision
Normal-flow assurance metadata MUST use:
- `AB1`: basic age-threshold assurance
- `AB2`: standard governed age-threshold assurance
- `AB3`: high-assurance age-threshold assurance

Verifier requests MUST use `maximum_assurance_bucket`.

Normal-flow assurance metadata MUST NOT disclose evidence details, exact evidence source, document type, document number, issuing office, inspection date, or rare provenance strings.

## Consequences
- Assurance is coarse enough for anti-fingerprinting.
- Verifier requests remain policy-readable without over-requesting provenance.
- Conformance can test bucket usage directly.
