# Flows and Topology

> This page turns the architecture thesis into system context and interaction flows. Use it after [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) when you want to see the moving parts in order.

## In This Document
- [How to read this page](#how-to-read-this-page)
- [Quick links](#quick-links)
- [System context](#system-context)
- [Issuance sequence](#issuance-sequence)
- [Normal presentation sequence](#normal-presentation-sequence)
- [Binding-mode matrix](#binding-mode-matrix)
- [Privacy boundary](#privacy-boundary)
- [Recovery and state domains](#recovery-and-state-domains)
- [Exception red-path sequence](#exception-red-path-sequence)
- [Threat-to-control map](#threat-to-control-map)
- [Related architecture pages](#related-architecture-pages)

## How to Read This Page
- Read the diagrams from top to bottom: context first, then issuance, then presentation.
- Use the privacy boundary diagram to separate what stays inside the wallet from what crosses to the verifier.
- Use the threat-to-control map as a bridge into [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md).

## Quick Links
| For... | Go to... |
| --- | --- |
| the thesis behind these flows | [Architecture Overview](./ARCHITECTURE_OVERVIEW.md) |
| control and policy interpretation | [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md) |
| profile-specific reading | [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md) |
| mature ecosystem assumptions | [Potential Final State](./POTENTIAL_FINAL_STATE.md) |

## System Context
This diagram identifies the main actors and the permitted trust and oversight relationships at system level. It is the quickest way to orient yourself before reading the sequences.

```mermaid
flowchart LR
    H[Holder] --> W[Wallet]
    I[Issuer] --> W
    V[Verifier] --> W
    V --> T[Trust registry]
    V -. optional .-> S[Status service or relay]
    R[Regulator or certifier] -. oversight .-> I
    R -. oversight .-> V
```

## Issuance Sequence
This sequence covers the one-time evidence check and root credential issuance path. The key boundary is that evidence checking happens once, while later verifier interactions depend on derived proofs rather than re-presenting the root credential.

```mermaid
sequenceDiagram
    participant H as Holder
    participant I as Issuer
    participant W as Wallet

    H->>I: present evidence once
    I->>I: verify evidence and determine threshold eligibility
    I->>W: issue root credential
    W->>W: store root credential locally
```

## Normal Presentation Sequence
This is the default verification path for minimal disclosure. The verifier asks for a threshold result plus transaction context, and the wallet returns a derived proof rather than identity data or the root credential.

```mermaid
sequenceDiagram
    participant V as Verifier
    participant W as Wallet
    participant T as Trust registry
    participant S as Status service or relay

    V->>W: request threshold, audience, nonce, policy context
    W->>W: evaluate request against disclosure policy
    W->>W: select permitted binding mode B0, B1, or B2
    W->>V: return transaction-bound derived proof
    V->>T: validate issuer trust
    opt if selected profile requires issuer trust, root credential, or wallet compromise freshness
        V->>S: fetch batched or cacheable status
    end
    V->>V: validate proof, audience, nonce, and validity
```

## Binding-Mode Matrix
This diagram shows how binding modes map to verifier classes and profiles. The invariant is that no normal-flow mode creates a reusable verifier-visible proof-binding artifact.

```mermaid
flowchart LR
    V1["V1 standard verifier"] --> B0["B0: nonce + audience + transaction proof"]
    V2["V2 high-assurance verifier"] --> B1["B1: verifier-scoped pairwise proof of possession"]
    PR["Profile R"] --> B0
    PR --> B1
    PP["Profile P"] --> B2["B2: unlinkable proof of possession"]
    B0 --> N["No extra verifier-visible holder handle"]
    B1 --> S["Verifier-scoped only; no cross-verifier reuse"]
    B2 --> U["No verifier-stable holder handle"]
```

## Privacy Boundary
This diagram makes the normal-flow privacy boundary explicit. Root credentials and disclosure logs stay inside the wallet boundary, while only the verifier request and decision artifacts appear on the verifier side.

```mermaid
flowchart TB
    subgraph "Wallet boundary"
        RC[Root credential]
        DP[Derived proof]
        LOG[Local disclosure log]
        BM[Binding mode decision]
    end

    subgraph "Verifier side"
        VR[Verifier request]
        VD[Verifier decision]
    end

    subgraph "Not disclosed in normal flow"
        ND1[Legal name]
        ND2[Exact DOB]
        ND3[Document number]
        ND4[Document image]
        ND5[Stable holder identifier]
        ND6[Stable root credential reference]
    end

    VR --> DP
    RC --> DP
    BM --> DP
    DP --> VD
```

## Recovery and State Domains
Recovery and compromise handling is split into three state domains so that compromise response does not require presentation logs.

```mermaid
flowchart TB
    subgraph "Issuer trust state"
        I1[trusted]
        I2[under_review]
        I3[suspended]
        I4[withdrawn]
        I5[compromised]
        I6[retired]
    end

    subgraph "Root credential state"
        R1[active]
        R2[expiring]
        R3[suspended]
        R4[revoked]
        R5[reissued]
        R6[expired]
    end

    subgraph "Wallet compromise state"
        W1[normal]
        W2[lost_unconfirmed]
        W3[lost_confirmed]
        W4[compromised]
        W5[recovered]
        W6[retired]
    end

    I5 --> R3
    W4 --> R4
    W2 --> R3
    W5 --> R5
```

## Exception Red-Path Sequence
Exceptional disclosure is outside normal-flow conformance. The wallet must make the path explicit and the verifier must supply lawful-basis fields before any higher disclosure is considered.

```mermaid
sequenceDiagram
    participant V as Verifier
    participant W as Wallet
    participant H as Holder
    participant A as Auditor or governance layer

    V->>W: exceptional request with lawful basis fields
    W->>W: validate verifier class and required fields
    W->>H: show red-path UX with extra fields and retention period
    alt holder refuses or fields missing
        W-->>V: refuse exceptional disclosure
    else holder proceeds
        W-->>V: exceptional disclosure outside normal conformance
        V->>A: create bounded audit record
    end
```

## Threat-to-Control Map
Use this as a quick index from common failure modes to the architectural control intended to mitigate them. The control vocabulary is expanded in [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md).

```mermaid
flowchart TD
    T1[Over-collection] --> C1[Verifier policy and wallet rejection]
    T2[Correlation] --> C2[No stable holder identifier and metadata minimisation]
    T3[Revocation surveillance] --> C3[Expiry-first or batched status via cache or relay]
    T4[Replay and forwarding] --> C4[Nonce and audience binding]
    T5[Metadata fingerprinting] --> C5[Assurance, issuer, timestamp, policy, and status coarsening]
    T6[Device compromise] --> C6[Root credential and wallet compromise state]
    T7[Issuer compromise] --> C7[Issuer trust state and trust withdrawal]
    T8[Exception normalization] --> C8[Verifier class eligibility, red-path UX, audit thresholds]
```

## Related Architecture Pages
- [Architecture Overview](./ARCHITECTURE_OVERVIEW.md): the thesis, planes, and normal-flow disclosure objective.
- [Governance and Controls](./GOVERNANCE_AND_CONTROLS.md): the control domains behind the threat map.
- [Dual Profile Overview](./DUAL_PROFILE_OVERVIEW.md): how these flows vary in emphasis between `Profile R` and `Profile P`.
- [Potential Final State](./POTENTIAL_FINAL_STATE.md): the future-state network these flows should fit into.
