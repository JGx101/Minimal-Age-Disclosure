# Roadmap

## Completed baseline
- [x] publish the layered architecture set under `docs/architecture/`
- [x] align the repository to the governance plane / root credential plane / derived proof plane / verification plane / status and recovery plane / exception plane model
- [x] publish Mermaid diagrams for system context, issuance, presentation, governance, and future-state topology
- [x] replace versioned public drafts with canonical unversioned core specs
- [x] draft the normative core spec set
- [x] draft conformance and privacy-negative test materials
- [x] publish the dual-profile framing for `Profile R` and `Profile P`
- [x] keep the prototype plan documentation-only

## Current work
- [ ] resolve ADR-backed contradictions that block a stable normative baseline
- [ ] tighten profile-specific conformance deltas
- [ ] complete the recovery, compromise, and verifier-retention edge cases
- [ ] refine policy mapping language for UK and EU audiences

## Next milestones
- [ ] decide the minimum Profile R holder-binding mechanism
- [ ] decide exact issuer-resolution requirements for trust validation
- [ ] decide assurance bucket taxonomy and request semantics
- [ ] decide validity granularity and freshness boundaries
- [ ] decide verifier audit-record minimum and exception-abuse thresholds

## Implementation entry criteria
Prototype implementation should begin only when:
- [ ] the ADR-backed interface blockers are resolved
- [ ] proof binding does not depend on a reusable verifier-visible key
- [ ] metadata minimisation constraints are stable
- [ ] recovery and compromise behavior is specified tightly enough for testing
- [ ] exception governance and verifier retention are testable
- [ ] conformance coverage exists for the major privacy failure modes
