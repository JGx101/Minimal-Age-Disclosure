# Dual Profile Overview

> This page explains why the architecture is intentionally split into two profiles. Read it after [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) if you need to understand what stays shared and what changes in emphasis.

## In This Document
- [How to read this page](#how-to-read-this-page)
- [Quick links](#quick-links)
- [Common model](#common-model)
- [Profile R](#profile-r)
- [Profile P](#profile-p)
- [Why split profiles](#why-split-profiles)
- [Related architecture pages](#related-architecture-pages)

## How to Read This Page
- Start with the shared model to see what does not change across profiles.
- Read `Profile R` as the conservative deployment-oriented path.
- Read `Profile P` as the privacy-maximal and research-oriented path.
- Use this page as a lens over the flows and controls, not as a replacement for them.

## Quick Links
| For... | Go to... |
| --- | --- |
| the shared thesis and planes | [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) |
| the interaction sequences both profiles inherit | [Flows and Topology](./FLOWS_AND_TOPOLOGY.md) |
| the governance model both profiles share | [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md) |
| the end-state ecosystem both profiles may inform | [Potential Final State](./POTENTIAL_FINAL_STATE.md) |

## Common Model
Both profiles share:
- one governance model
- one root credential / derived proof separation
- one verifier-restraint model
- one trust-registry boundary model
- one conformance language

## Profile R
Regulator-ready and interoperable profile.

### Goals
- deployment fit
- standards alignment
- auditability
- clear conformance
- policy legibility

### Likely Characteristics
- mainstream issuance and presentation rails
- transaction-bound or short-lived verifier-facing artifacts
- conservative proof and status design
- explicit maturity and deployment assumptions

## Profile P
Privacy-maximal and research-oriented profile.

### Goals
- stronger anti-correlation
- stronger unlinkability
- stronger metadata minimisation
- contribution to future standards and reference implementations

### Likely Characteristics
- more ambitious derived-proof approaches
- stronger anti-correlation expectations
- more open research on proof-binding and revocation
- explicit maturity notes and unresolved implementation tradeoffs

## Why Split Profiles
One profile should not pretend to satisfy every deployment and research ambition at once.

The split keeps the project honest:
- `Profile R` can be conservative and deployable.
- `Profile P` can be bolder without pretending it is already production-ready.

## Related Architecture Pages
- [Architecture Overview](./ARCHITECTURE_OVERVIEW.md): the shared thesis and six-plane architecture both profiles inherit.
- [Flows and Topology](./FLOWS_AND_TOPOLOGY.md): the core issuance and presentation flows that each profile interprets differently.
- [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md): the control language that remains common across profiles.
- [Potential Final State](./POTENTIAL_FINAL_STATE.md): the possible mature ecosystem that could absorb lessons from both profiles over time.
