# Backlog And Roadmap

## Status snapshot
- Phase: documentation-first architecture and specification work
- Overall posture: core architecture gaps resolved into accepted ADRs and normative specs
- Implementation state: ready for prototype-interface review, not production build-out
- Main blocker theme: no active architecture blockers remain; future work is prototype validation, standards review, and automation depth

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
- [x] close open implementation-profile and validation questions through specs, policy, prototype planning, and fixtures
- [x] add fixture-backed examples for conformant and non-conformant request, response, retention, exception, recovery, and repeated-transaction cases
- [x] export initial JSON Schemas for canonical request, response, and exception objects
- [x] add a standard-library fixture validator and GitHub Actions workflow for schema and fixture checks

## Non-blocking future research and validation
- [ ] select and evaluate concrete libraries for the `Profile P` `B2` proof-family pattern
- [ ] map the canonical objects to specific OpenID4VCI and OpenID4VP payload profiles
- [ ] expand JSON Schema validation into full schema evaluation rather than repository-invariant checks only
- [ ] implement repeated-transaction metadata fingerprinting checks against generated fixture batches
- [ ] run external UK/EU policy review against the policy source categories
- [ ] run standards feedback on the request/response object shape, binding modes, and metadata coarsening

## Upcoming milestones
### Milestone 1: prototype-interface review
- [x] map canonical request and response fields to mock issuer, wallet, verifier, trust-registry, status relay, and governance/audit behavior
- [x] define fixture examples for conformant `Profile R`, conformant `Profile P`, and non-conformant flows
- [x] define acceptance criteria for `B0`, `B1`, and `B2` demonstrations

### Milestone 2: conformance automation
- [x] add first request-shape and response-shape checks from fixtures
- [ ] automate metadata-fingerprinting negative cases from repeated-transaction fixtures
- [x] add first verifier-retention fixture checks
- [ ] automate exception-threshold checks from fixture scenarios

### Milestone 3: policy and standards review
- [x] define UK/EU source categories for verifier class and exception-governance mapping
- [ ] distinguish implementation assumptions from policy claims
- [ ] prepare focused issues for standards feedback on request/response shape, binding modes, and metadata coarsening

## Implementation entry criteria
Prototype implementation should begin only when:
- [x] the accepted request and response objects are mapped to prototype fixtures
- [x] `B0`, `B1`, and `B2` expected behavior is testable
- [x] metadata minimisation constraints are represented in fixtures
- [x] recovery and compromise scenarios are selected
- [x] exception red-path behavior is represented at the interface level

Prototype code remains gated on a separate implementation decision and review.

## Definition of roadmap progress
An item counts as meaningfully complete when it produces one or more of:
- a stable normative requirement
- an accepted ADR with downstream document updates
- a testable conformance condition
- a fixture or scenario that makes privacy failure visible
- a clearer boundary against identity disclosure or verifier over-collection
