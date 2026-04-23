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

## What to contribute
Useful contributions include:
- normative specification clarifications
- architecture corrections or tighter trust-boundary definitions
- stronger conformance criteria and privacy-negative tests
- primary-source corrections for standards, regulation, or policy claims
- ADRs that resolve open design choices or document tradeoffs
- clearer diagrams, terminology, and cross-document consistency fixes

## Before you start
Read these first:
- `README.md`
- `PROJECT_BRIEF.md`
- `REQUIREMENTS.md`
- `THREAT_MODEL_SEED.md`
- the relevant files under `docs/architecture/`, `spec/`, and `docs/adr/`

Before opening a PR, check whether the change should begin as:
- a bug report for a contradiction, defect, or broken workflow
- a proposal for a material architectural, standards, or governance change
- a direct PR for a scoped editorial or consistency fix

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
- keep terminology consistent across specs, diagrams, ADRs, and conformance materials

## Working style
Contributions should be serious, specific, and reviewable.

When making a change:
- explain the problem first, then the proposed fix
- prefer small, focused PRs over broad mixed-purpose edits
- separate normative requirements from explanatory guidance
- identify affected profiles, actors, and trust boundaries
- call out open questions instead of hiding them in vague wording

## Documentation expectations
Contributions SHOULD:
- keep the tone neutral, technical, and auditable
- back privacy claims with concrete mechanisms
- back security claims with threats, controls, or explicit limitations
- separate normative requirements from open questions and future work
- update related specs, architecture docs, ADRs, and conformance materials together when a change crosses boundaries
- define terms before relying on them normatively
- avoid product marketing language and unsupported implementation claims

## Pull requests
Each pull request should explain:
- the problem being addressed
- affected files or interfaces
- privacy, security, governance, and interoperability implications
- whether conformance or privacy-negative tests were updated
- whether diagrams or ADRs were updated

Use the PR template completely. If a section does not apply, say so explicitly.

## Large changes
For major architecture or policy changes:
- update or add an ADR
- update the relevant spec files
- update conformance and privacy-negative tests if pass/fail behavior changed
- update diagrams if actors, flows, trust boundaries, or disclosed data changed

## Review criteria
Maintainers will generally review contributions for:
- correctness and internal consistency
- privacy and security impact
- verifier-restraint implications
- interoperability and implementability
- conformance testability
- clarity for future reviewers and implementers

## Security and privacy reporting
Do not open a public issue for a newly discovered security or privacy flaw if early disclosure could cause harm. Follow `SECURITY.md` instead.
