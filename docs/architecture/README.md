# Architecture Docs

This directory contains the canonical architecture set for the repository. If you want to understand how the project turns minimal age disclosure into concrete system boundaries, start here.

## What this section explains
- the planes used to separate governance, credentials, proofs, verification, status, and exception handling
- the normal transaction flow for proving an age threshold such as `18+`
- where policy controls constrain verifier behaviour
- how the repository distinguishes the common baseline from profile-specific work

## Recommended reading order
1. [Architecture Overview](ARCHITECTURE_OVERVIEW.md)
2. [Flows and Topology](FLOWS_AND_TOPOLOGY.md)
3. [Governance and Controls](GOVERNANCE_AND_CONTROLS.md)
4. [Dual Profile Overview](DUAL_PROFILE_OVERVIEW.md)
5. [Potential Final State](POTENTIAL_FINAL_STATE.md)

## Quick map
- `ARCHITECTURE_OVERVIEW.md`: high-level system shape and design intent
- `FLOWS_AND_TOPOLOGY.md`: issuance, proof, verification, trust-resolution, retention, and recovery boundaries
- `GOVERNANCE_AND_CONTROLS.md`: policy, oversight, and verifier-restraint mechanisms
- `DUAL_PROFILE_OVERVIEW.md`: split between interoperable and privacy-maximal tracks
- `POTENTIAL_FINAL_STATE.md`: target end-state direction after the accepted architecture decisions are implemented consistently

## How this fits the rest of the repo
- Read `../../PROJECT_BRIEF.md` first for project scope and status.
- Use `../../BACKLOG.md` for milestone status and implementation gates.
- Use `../../OPEN_QUESTIONS.md` to see which implementation-profile questions remain.
- Use `../adr/README.md` and the ADR set when an architecture point was recently accepted or needs historical context.

## Architecture rules that should stay invariant
- The normal flow separates the root credential plane from the derived proof plane.
- The ordinary verifier path is driven by minimal disclosure and transaction-bound proof generation.
- Trust resolution starts from issuer class plus a minimised trust reference; exact issuer identity is exceptional to the trust path, not the default disclosure surface.
- Verifier retention is narrower than verifier validation and must not store raw proof payloads or reusable binding artifacts by default.
- The exceptional path is represented as a distinct governance boundary, not as the default behaviour.
- Normal flow should not imply routine disclosure of exact DOB, legal name, document number, document image, or a stable verifier-visible identifier.

## Diagram conventions
- Mermaid is the source format for all diagrams.
- Diagrams should make disclosure boundaries legible to newcomers.
- If a diagram changes actors, trust boundaries, or data disclosure, related specs, ADRs, and conformance materials should usually change with it.
