# Contributing

## Purpose
This repository is a documentation-first architecture, governance, and conformance project for privacy-preserving age-threshold proof.

Good contributions improve one or more of:
- minimal disclosure
- anti-correlation
- verifier restraint
- governance and trust clarity
- conformance and testability
- recovery, compromise, and exception handling
- interoperability with current credential rails

## Before contributing
Read these first:
- `README.md`
- `PROJECT_BRIEF.md`
- `REQUIREMENTS.md`
- `THREAT_MODEL_SEED.md`
- the relevant files under `docs/architecture/`, `spec/`, and `docs/adr/`

## Contribution priorities
High-value contributions include:
- clearer normative specifications
- better standards and policy source corrections
- stronger conformance criteria
- stronger privacy-negative tests
- clearer treatment of holder binding, metadata minimisation, recovery, status, and verifier compliance
- clearer diagrams and topology explanations

## Ground rules
Contributions MUST NOT:
- add normal-flow disclosure of exact DOB, legal name, document number, or document image
- add a stable verifier-visible holder identifier to the normal flow
- collapse the root credential and derived proof into one ordinary verifier-facing artifact
- assume that proof binding can disclose a stable holder key without a documented privacy tradeoff
- add token-specific live issuer callbacks to the ordinary verification path without explicit justification
- normalize exceptional handling into the default path

Contributions SHOULD:
- make tradeoffs explicit
- cite primary sources for standards and policy claims
- preserve the distinction between the common baseline, Profile R, and Profile P

## Documentation expectations
Contributions SHOULD:
- keep the tone neutral, technical, and auditable
- back privacy claims with concrete mechanisms
- back security claims with threats, controls, or explicit limitations
- separate normative requirements from open questions and future work
- update related specs, architecture docs, ADRs, and conformance materials together when a change crosses boundaries

## Pull requests
Each pull request should explain:
- the problem being addressed
- affected files or interfaces
- privacy, security, governance, and interoperability implications
- whether conformance or privacy-negative tests were updated
- whether diagrams or ADRs were updated

## Large changes
For major architecture or policy changes:
- update or add an ADR
- update the relevant spec files
- update conformance and privacy-negative tests if pass/fail behavior changed
- update diagrams if actors, flows, trust boundaries, or disclosed data changed
