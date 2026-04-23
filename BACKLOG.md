# Backlog And Roadmap

## Status snapshot
- Phase: documentation-first architecture and specification work
- Overall posture: baseline published, decision-heavy items still open
- Implementation state: not ready for build-out yet
- Main blocker theme: privacy-critical interfaces still need ADR-backed closure

## What is already in place
- [x] publish the layered architecture set under `docs/architecture/`
- [x] align the repository to the governance plane / root credential plane / derived proof plane / verification plane / status and recovery plane / exception plane model
- [x] publish Mermaid diagrams for system context, issuance, presentation, governance, and future-state topology
- [x] replace versioned public drafts with canonical unversioned core specs
- [x] draft the normative core spec set
- [x] draft conformance and privacy-negative test materials
- [x] publish the dual-profile framing for `Profile R` and `Profile P`
- [x] keep the prototype plan documentation-only

## Active work
These are the highest-value items for moving the project from a credible baseline to a stable implementation candidate.

- [ ] resolve ADR-backed contradictions that block a stable normative baseline
- [ ] tighten profile-specific conformance deltas
- [ ] complete the recovery, compromise, and verifier-retention edge cases
- [ ] refine policy mapping language for UK and EU audiences

## Upcoming milestones
These milestones represent the main decision gates for the next project phase.

### Milestone 1: stabilise the proof model
- [ ] decide the minimum `Profile R` holder-binding mechanism
- [ ] decide which proof-binding artifacts, if any, can be verifier-visible without creating practical correlation risk
- [ ] confirm that normal-flow proof binding does not depend on a reusable verifier-visible key

### Milestone 2: stabilise trust and request semantics
- [ ] decide exact issuer-resolution requirements for trust validation
- [ ] decide assurance bucket taxonomy and request semantics
- [ ] decide which request-object fields are essential versus avoidable correlation surface

### Milestone 3: stabilise operational controls
- [ ] decide validity granularity and freshness boundaries
- [ ] decide verifier audit-record minimum and exception-abuse thresholds
- [ ] finish the recovery and compromise model tightly enough for repeatable testing

## Dependencies and linkage
- Architecture blockers should usually resolve through `docs/adr/` before related specs are treated as stable.
- Open design questions are tracked in `OPEN_QUESTIONS.md`.
- Prototype planning should reflect only decisions that have crossed the implementation entry criteria below.

## Implementation entry criteria
Prototype implementation should begin only when:
- [ ] the ADR-backed interface blockers are resolved
- [ ] proof binding does not depend on a reusable verifier-visible key
- [ ] metadata minimisation constraints are stable
- [ ] recovery and compromise behavior is specified tightly enough for testing
- [ ] exception governance and verifier retention are testable
- [ ] conformance coverage exists for the major privacy failure modes

## Definition of roadmap progress
An item counts as meaningfully complete when it produces one or more of the following:
- a stable normative requirement
- a resolved ADR with downstream document updates
- a testable conformance condition
- a clearer boundary against identity disclosure or verifier over-collection
