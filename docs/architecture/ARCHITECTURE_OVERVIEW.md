# Architecture Overview

> This page is the entry point for the architecture set. Start here for the core thesis and system shape, then follow the links into flows, governance, profile strategy, and the target end state.

## In This Document
- [How to read this set](#how-to-read-this-set)
- [Architecture map](#architecture-map)
- [Core thesis](#core-thesis)
- [Layered model](#layered-model)
- [Normal flow](#normal-flow)
- [Disclosure target](#normal-flow-disclosure-target)
- [Normal-flow exclusions](#normal-flow-exclusions)
- [Binding modes](#binding-modes)
- [Overview diagram](#overview-diagram)
- [Related architecture pages](#related-architecture-pages)

## How to Read This Set
- Read this page first for the architecture thesis and the six-plane model.
- Use [Flows and Topology](./FLOWS_AND_TOPOLOGY.md) for the end-to-end interaction sequences and privacy boundaries.
- Use [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md) for issuer or verifier classes and the formal restraint model.
- Use [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md) for the `Profile R` versus `Profile P` split.
- Use [Potential Final State](./POTENTIAL_FINAL_STATE.md) for the mature-ecosystem target picture.

## Architecture Map
| If you want to understand... | Read... |
| --- | --- |
| the overall thesis and planes | [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) |
| who talks to whom and in what order | [Flows and Topology](./FLOWS_AND_TOPOLOGY.md) |
| governance boundaries and controls | [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md) |
| why there are two architectural profiles | [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md) |
| the intended mature ecosystem shape | [Potential Final State](./POTENTIAL_FINAL_STATE.md) |

## Core Thesis
A relying party should be able to decide whether a holder meets an age threshold without learning the holder's identity or receiving a reusable tracking handle.

## Layered Model

### 1. Governance plane
Defines:
- issuer classes
- verifier classes
- trust registry boundaries
- conformance and sanctions
- exception governance

### 2. Root credential plane
Defines:
- evidence checking and issuance
- local wallet storage
- root credential lifecycle
- renewal, suspension, and recovery boundaries

### 3. Derived proof plane
Defines:
- transaction-bound proof generation
- disclosure minimisation
- proof-binding approach
- profile-specific proof options

### 4. Verification plane
Defines:
- verifier request object
- threshold evaluation
- proof validation
- local decisioning
- retention and telemetry boundaries

### 5. Status and recovery plane
Defines:
- issuer trust state
- root credential state
- compromise handling
- recovery and re-issuance
- privacy-preserving status where justified

### 6. Exception plane
Defines:
- higher-disclosure path
- lawful basis requirement
- red-path wallet UX
- audit and sanctions

## Normal Flow
1. Issuer checks evidence once.
2. Issuer issues a root credential to the wallet.
3. Wallet stores the root credential locally.
4. Verifier sends a minimal request with threshold, audience, nonce, and policy context.
5. Wallet derives a transaction-bound proof from the root credential.
6. Wallet applies the selected binding mode: `B0`, `B1`, or `B2`.
7. Verifier validates the proof, trust, binding mode, and policy conditions locally.
8. Verifier retains only minimal decision evidence under policy.

For the step-by-step sequence view, continue to [Flows and Topology](./FLOWS_AND_TOPOLOGY.md#normal-presentation-sequence).

## Normal-Flow Disclosure Target
The verifier should receive only:
- threshold result
- coarse assurance metadata
- coarse issuer information by default
- bounded validity information
- audience binding
- nonce binding
- transaction-bound rightful-possession proof material that is not a stable verifier-visible holder identifier

## Normal-Flow Exclusions
The verifier should not receive:
- legal name
- exact date of birth
- document number
- document image
- a stable holder identifier
- a stable root credential reference
- token-specific live issuer callbacks by default

## Binding Modes
Binding is explicit because anti-sharing and anti-correlation pull against each other.

| Mode | Default use | Verifier class | Correlation boundary |
| --- | --- | --- | --- |
| `B0` | Standard low-friction threshold checks | `V1` | No additional verifier-visible holder handle |
| `B1` | High-assurance `Profile R` checks | `V2` | Verifier-scoped only; no cross-verifier reuse |
| `B2` | Privacy-maximal checks | `Profile P` | No verifier-stable holder handle |

No normal-flow binding mode may expose a reusable verifier-visible proof-binding artifact.

## Overview Diagram
This diagram shows the default interaction pattern across issuer, wallet, verifier, trust, status, and governance actors. Read it as the single-page summary of the architecture thesis before moving into the detailed sequences.

```mermaid
flowchart LR
    I[Issuer] -->|issues root credential| W[Wallet]
    W -->|stores root credential locally| W
    V[Verifier] -->|minimal request: threshold, audience, nonce, policy| W
    W -->|derived proof using B0, B1, or B2| V
    V -->|issuer validation| T[Trust registry]
    V -. optional privacy-preserving status .-> S[Status service or relay]
    A[Auditor or certifier] -. governance and conformance .-> I
    A -. governance and conformance .-> V
```

## Related Architecture Pages
- [Flows and Topology](./FLOWS_AND_TOPOLOGY.md): context, sequence, privacy-boundary, and threat-control diagrams.
- [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md): issuer and verifier classes plus the control baseline.
- [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md): the rationale for the conservative and privacy-maximal profile split.
- [Potential Final State](./POTENTIAL_FINAL_STATE.md): the mature-ecosystem target shape once conformance and governance are established.
