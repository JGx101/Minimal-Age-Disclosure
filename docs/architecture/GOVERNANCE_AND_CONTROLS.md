# Governance and Controls

## Issuer classes
- `A0` authoritative issuer
- `A1` registered private issuer
- `A2` derived-attribute issuer

## Verifier classes
- `V1` standard verifier
- `V2` high-assurance verifier
- `VX` exceptional verifier

## Governance principles
- issuers must be trustable under a recognised governance model
- verifiers must be constrained by policy and audit, not only by wallet UX
- trust registries should publish issuer-validation metadata only
- exception use must be separately governed and measurable
- conformance is part of the architecture, not an afterthought

## Key controls
- no stable verifier-visible holder identifier in the normal flow
- no root credential presentation in the normal flow
- no live token-specific issuer callback by default
- metadata minimisation as a formal control domain
- verifier compliance and retention rules
- privacy-negative testing
