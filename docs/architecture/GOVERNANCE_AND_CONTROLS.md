# Governance and Controls

> This page defines the policy and control layer that keeps the minimal-disclosure architecture enforceable. It complements the interaction views in [Flows and Topology](./FLOWS_AND_TOPOLOGY.md).

## In This Document
- [How to read this page](#how-to-read-this-page)
- [Quick links](#quick-links)
- [Issuer classes](#issuer-classes)
- [Verifier classes](#verifier-classes)
- [Binding modes](#binding-modes)
- [State domains](#state-domains)
- [Exception controls](#exception-controls)
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

## Binding Modes
| Mode | Allowed use | Control purpose |
| --- | --- | --- |
| `B0` | `V1` standard checks | baseline transaction binding without an extra holder handle |
| `B1` | `V2` / high-assurance `Profile R` | verifier-scoped anti-sharing without cross-verifier reuse |
| `B2` | `Profile P` | unlinkable proof of possession |

No binding mode may expose a reusable verifier-visible proof-binding artifact in the normal flow.

## State Domains
| Domain | Values |
| --- | --- |
| Issuer trust state | `trusted`, `under_review`, `suspended`, `withdrawn`, `compromised`, `retired` |
| Root credential state | `active`, `expiring`, `suspended`, `revoked`, `reissued`, `expired` |
| Wallet compromise state | `normal`, `lost_unconfirmed`, `lost_confirmed`, `compromised`, `recovered`, `retired` |

State changes must support recovery and compromise response without presentation logs.

## Exception Controls
- `V1` must not invoke exceptional disclosure.
- `V2` may request bounded step-up only where normal flow cannot satisfy the governing rule.
- `VX` may request exceptional higher disclosure only with explicit lawful-basis fields.
- Exception use above `5%` of monthly age-check volume triggers review.
- Exception use above `10%` or repeated review triggers across two consecutive months is a conformance failure unless governance approves a scoped exception class.

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
- `B1` verifier-scoped continuity material cannot be retained as default telemetry
- `B2` cannot expose verifier-stable holder handles
- metadata minimisation as a formal control domain
- verifier compliance and retention rules
- privacy-negative testing

## Related Architecture Pages
- [Architecture Overview](./ARCHITECTURE_OVERVIEW.md): where the governance plane and exception plane sit in the layered model.
- [Flows and Topology](./FLOWS_AND_TOPOLOGY.md): where these controls appear as concrete mitigations.
- [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md): how the same governance language supports both profiles.
- [Potential Final State](./POTENTIAL_FINAL_STATE.md): how governance scales to multi-issuer and multi-verifier deployment.
