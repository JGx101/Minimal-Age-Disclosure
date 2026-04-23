# Backlog And Roadmap

## Status snapshot
- Phase: documentation-first architecture and specification work
- Overall posture: core architecture gaps resolved into accepted ADRs and normative specs
- Implementation state: ready for prototype-interface review, not production build-out
- Main blocker theme: concrete proof constructions and conformance automation remain to be selected

## What is already in place
- [x] publish the layered architecture set under `docs/architecture/`
- [x] align the repository to the governance plane / root credential plane / derived proof plane / verification plane / status and recovery plane / exception plane model
- [x] publish Mermaid diagrams for context, issuance, presentation, binding modes, recovery state, and exception path
- [x] define canonical request and response objects
- [x] define `B0`, `B1`, and `B2` binding modes
- [x] define metadata coarsening rules and prohibited correlators
- [x] define issuer trust, root credential, and wallet compromise states
- [x] define recovery actor responsibilities, state transitions, propagation, stale-state behavior, rebind, appeal, and lifecycle diagrams
- [x] define exception eligibility, lawful-basis fields, red-path UX, audit triggers, and abuse thresholds
- [x] update conformance and privacy-negative tests for the accepted architecture decisions

## Active work
- [ ] review the accepted interfaces against prototype feasibility
- [ ] tighten non-recovery profile-specific conformance deltas for `Profile R` and `Profile P`
- [ ] convert privacy-negative tests into fixture-backed checks
- [ ] refine policy mapping language for UK and EU audiences

## Upcoming milestones
### Milestone 1: prototype-interface review
- [ ] map canonical request and response fields to mock issuer, wallet, verifier, and trust-registry behavior
- [ ] define fixture examples for conformant `Profile R`, conformant `Profile P`, and non-conformant flows
- [ ] define acceptance criteria for `B0`, `B1`, and `B2` demonstrations

### Milestone 2: conformance automation
- [ ] automate request-shape and response-shape checks
- [ ] automate metadata-fingerprinting negative cases
- [ ] automate verifier-retention and exception-threshold checks where feasible

### Milestone 3: policy and standards review
- [ ] update UK/EU mapping against the accepted decisions
- [ ] distinguish implementation assumptions from policy claims
- [ ] prepare focused issues for standards feedback on request/response shape, binding modes, and metadata coarsening

## Implementation entry criteria
Prototype implementation should begin only when:
- [ ] the accepted request and response objects are mapped to prototype fixtures
- [ ] `B0`, `B1`, and `B2` expected behavior is testable
- [ ] metadata minimisation constraints are represented in fixtures
- [ ] recovery and compromise scenarios are selected
- [ ] exception red-path behavior is represented at the interface level

## Definition of roadmap progress
An item counts as meaningfully complete when it produces one or more of:
- a stable normative requirement
- an accepted ADR with downstream document updates
- a testable conformance condition
- a fixture or scenario that makes privacy failure visible
- a clearer boundary against identity disclosure or verifier over-collection
