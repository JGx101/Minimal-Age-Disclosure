# ADR-0005: Keep v1 as a narrow age-threshold proof profile

## Status
Proposed

## Date
2026-04-21

## Context
The repository's goals are privacy-preserving and standards-oriented, but the design space is large. Scope expansion would quickly pull the project toward:
- general identity wallet design
- broad KYC feature sets
- rich assurance taxonomies
- strong person-binding mechanisms
- multiple status architectures

That would dilute the central thesis and make the documentation and prototype less auditable.

## Decision
Keep v1 narrow.

V1 will focus on:
- age-threshold claims for `over_13`, `over_16`, `over_18`, and `over_21`
- threshold-only disclosure in the normal flow
- narrow assurance metadata
- OpenID4VCI issuance and OpenID4VP presentation
- explicit verifier policy and conformance requirements
- bounded derived proofs and state-based status as the default validity strategy
- a documentation-first reference prototype

V1 will not treat the following as core requirements:
- routine exact DOB disclosure
- routine legal-name or document-level disclosure
- verifier-stable global subject identifiers
- strong person-binding
- blockchain dependencies
- advanced privacy-preserving status mechanisms as mandatory

## Rationale
The narrow profile keeps the project aligned with its stated purpose:
prove threshold eligibility, not identity.

It also improves:
- privacy legibility
- auditability
- conformance testability
- standards contribution value

## Alternatives considered
- broader identity-attribute profile in v1
- multi-sector, multi-assurance, multi-status design in v1
- prototype-first expansion before profile decisions are stable

## Consequences
### Positive
- clearer project thesis
- lower implementation and documentation risk
- easier conformance story
- stronger regulator-legible scope boundaries

### Negative
- some sectors will require features that fall outside v1
- some concrete proof-construction and assurance implementation details remain future work
- future ADRs will be needed for some extensions

## Follow-up actions
- define the canonical claim profile and verifier policy as narrow interfaces
- keep trust-model and conformance documents aligned to that scope
- treat broader features as later ADR candidates rather than implicit v1 drift
