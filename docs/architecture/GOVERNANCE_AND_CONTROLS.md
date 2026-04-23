# Governance and Controls

> This page defines the policy and control layer that keeps the minimal-disclosure architecture enforceable. It complements the interaction views in [Flows and Topology](./FLOWS_AND_TOPOLOGY.md).

## In This Document
- [How to read this page](#how-to-read-this-page)
- [Quick links](#quick-links)
- [Issuer classes](#issuer-classes)
- [Verifier classes](#verifier-classes)
- [Governance principles](#governance-principles)
- [Key controls](#key-controls)
- [Related architecture pages](#related-architecture-pages)

## How to Read This Page
- Use the class definitions to understand who is allowed to issue or verify under the model.
- Read the governance principles as design constraints, not implementation afterthoughts.
- Read the key controls alongside the [Threat-to-Control Map](./FLOWS_AND_TOPOLOGY.md#threat-to-control-map).

## Quick Links
| For... | Go to... |
| --- | --- |
| the architecture thesis these controls protect | [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) |
| the threat model and interaction flows | [Flows and Topology](./FLOWS_AND_TOPOLOGY.md) |
| profile-level tradeoffs | [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md) |
| the mature governance target | [Potential Final State](./POTENTIAL_FINAL_STATE.md) |

## Issuer Classes
- `A0` authoritative issuer
- `A1` registered private issuer
- `A2` derived-attribute issuer

## Verifier Classes
- `V1` standard verifier
- `V2` high-assurance verifier
- `VX` exceptional verifier

## Governance Principles
- issuers must be trustable under a recognised governance model
- verifiers must be constrained by policy and audit, not only by wallet UX
- trust registries should publish issuer-validation metadata only
- exception use must be separately governed and measurable
- conformance is part of the architecture, not an afterthought

## Key Controls
- no stable verifier-visible holder identifier in the normal flow
- no root credential presentation in the normal flow
- no live token-specific issuer callback by default
- metadata minimisation as a formal control domain
- verifier compliance and retention rules
- privacy-negative testing

## Related Architecture Pages
- [Architecture Overview](./ARCHITECTURE_OVERVIEW.md): where the governance plane and exception plane sit in the layered model.
- [Flows and Topology](./FLOWS_AND_TOPOLOGY.md): where these controls appear as concrete mitigations.
- [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md): how the same governance language supports both profiles.
- [Potential Final State](./POTENTIAL_FINAL_STATE.md): how governance scales to multi-issuer and multi-verifier deployment.
