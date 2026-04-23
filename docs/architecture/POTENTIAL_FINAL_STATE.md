# Potential Final State

## Purpose
This is a target-state concept for a mature ecosystem, not a statement of current implementation.

```mermaid
flowchart LR
    I1[Issuer A0] --> W1[Conformant wallet]
    I2[Issuer A1] --> W1
    I3[Issuer A2] --> W2[Conformant wallet]

    V1[Verifier V1] --> W1
    V2[Verifier V2] --> W2
    VX[Verifier VX] --> W1

    V1 --> T[Trust registry]
    V2 --> T
    VX --> T

    V1 -. optional privacy-preserving freshness .-> S[Status relay]
    V2 -. optional privacy-preserving freshness .-> S

    C[Certifier or auditor] -. conformance and audit .-> I1
    C -. conformance and audit .-> I2
    C -. conformance and audit .-> I3
    C -. conformance and audit .-> V1
    C -. conformance and audit .-> V2
    C -. conformance and audit .-> VX

    P[Published profile and conformance suite] -. reference .-> C
    P -. reference .-> T
```

## Target-state characteristics
- multiple issuers under one governance model
- multiple conformant wallets and verifiers
- trusted-list or registry-based issuer validation
- privacy-preserving status only where justified
- published profile and conformance suite
- audit and sanctions for verifier abuse
