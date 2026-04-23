# ADR-0001: Use OpenID4VCI and OpenID4VP on standards-aligned VC rails for v1

## Status
Proposed

## Date
2026-04-21

## Context
The project needs a credible and interoperable foundation. A custom protocol would increase scope and reduce regulator and implementer confidence.

## Decision
Use the following as the default standards basis for v1:
- OpenID4VCI for issuance
- OpenID4VP for presentation
- a standards-aligned verifiable credential data model and proof format compatible with the selected ecosystem profile

## Rationale
This keeps the project grounded in existing ecosystem patterns and focuses innovation on:
- the privacy profile
- verifier constraints
- assurance semantics
- trust and conformance

rather than transport novelty.

## Alternatives considered
- custom protocol
- blockchain-native protocol
- pure conceptual documentation with no protocol assumptions

## Consequences
### Positive
- better interoperability story
- stronger standards credibility
- narrower project scope

### Negative
- inherits some ecosystem complexity
- requires careful profiling to preserve strict privacy goals
- does not by itself prevent over-disclosure or correlation

## Follow-up actions
- define exact v1 profile constraints
- map required claims and metadata
- document where current rails are insufficient
- keep verifier policy and conformance requirements explicit
