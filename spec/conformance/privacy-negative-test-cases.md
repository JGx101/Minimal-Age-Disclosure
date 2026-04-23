# Privacy-Negative Test Cases

## Status
Draft

## Purpose
This specification defines repeatable privacy-negative tests for the minimal age-disclosure architecture.

Each test case includes:
- test ID
- threat addressed
- actor under test
- profile scope
- preconditions
- steps
- expected result
- failure classification
- source clause

## Test catalog
### PNT-01: Exact DOB requested in normal flow
- Threat: over-collection
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: normal-flow threshold check
- Steps: verifier requests exact DOB
- Expected result: request rejected, refused, or routed explicitly to exceptional flow
- Failure: privacy and governance

### PNT-02: Legal name requested in normal flow
- Threat: over-collection
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: normal-flow threshold check
- Steps: verifier requests legal name
- Expected result: non-conformant normal flow
- Failure: privacy and governance

### PNT-03: Document number or image requested
- Threat: over-collection
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: normal-flow threshold check
- Steps: verifier requests document number or image
- Expected result: non-conformant normal flow
- Failure: privacy and governance

### PNT-04: Stable holder identifier leakage
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect proofs for stable holder identifiers
- Expected result: no stable holder identifier visible
- Failure: privacy

### PNT-05: Stable root credential reference leakage
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect proofs for root credential references
- Expected result: no stable root credential reference visible
- Failure: privacy

### PNT-06: Reusable proof-binding artifact
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON, R, P
- Preconditions: repeated transactions against same or different verifiers
- Steps: compare verifier-visible proof-binding artifacts
- Expected result: non-reusable under the approved profile rules
- Failure: privacy

### PNT-07: Root credential disclosed in normal flow
- Threat: disclosure boundary failure
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: normal-flow request
- Steps: inspect verifier-facing payload
- Expected result: root credential absent
- Failure: protocol and privacy

### PNT-08: Missing nonce
- Threat: replay
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: crafted request without nonce
- Steps: send request
- Expected result: rejection or non-conformant flow
- Failure: protocol

### PNT-09: Missing audience
- Threat: forwarding
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: crafted request without audience
- Steps: send request
- Expected result: rejection or non-conformant flow
- Failure: protocol

### PNT-10: Cross-verifier proof acceptance
- Threat: replay or forwarding
- Actor: verifier
- Scope: COMMON
- Preconditions: proof captured for verifier A
- Steps: replay to verifier B
- Expected result: rejection
- Failure: protocol and privacy

### PNT-11: Token-specific live issuer callback
- Threat: presentation logging
- Actor: verifier, status service
- Scope: COMMON
- Preconditions: ordinary verification path
- Steps: inspect whether token-specific live callback is required
- Expected result: non-conformant unless separately governed and not part of common normal flow
- Failure: privacy and governance

### PNT-12: Assurance metadata fingerprinting
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof contains assurance data
- Steps: inspect granularity of assurance metadata
- Expected result: bounded and non-fingerprinting
- Failure: privacy

### PNT-13: Over-granular issuer metadata
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof contains issuer data
- Steps: compare issuer disclosure to trust need
- Expected result: least specific disclosure compatible with trust validation
- Failure: privacy

### PNT-14: Over-precise timestamps or validity windows
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof or retention record contains time data
- Steps: inspect precision
- Expected result: bounded granularity only
- Failure: privacy

### PNT-15: Correlating policy identifiers or status references
- Threat: metadata correlation
- Actor: verifier, status service
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect policy identifiers and status references
- Expected result: no practical holder correlation
- Failure: privacy

### PNT-16: Raw proof retained by default
- Threat: over-retention
- Actor: verifier
- Scope: COMMON
- Preconditions: verifier stores audit records
- Steps: inspect retained artifacts
- Expected result: raw proof not retained by default
- Failure: governance

### PNT-17: Fine-grained telemetry retention
- Threat: activity reconstruction
- Actor: verifier
- Scope: COMMON
- Preconditions: telemetry enabled
- Steps: inspect retention fields
- Expected result: no fine-grained telemetry sufficient to reconstruct activity history
- Failure: governance and privacy

### PNT-18: Exceptional path used where normal path suffices
- Threat: exception normalization
- Actor: verifier
- Scope: COMMON
- Preconditions: normal path should satisfy the use case
- Steps: verifier invokes exceptional path
- Expected result: flagged for governance failure or review
- Failure: governance

### PNT-19: Exceptional request lacks explicit basis
- Threat: exception abuse
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect justification and class
- Expected result: non-conformant if basis is missing or vague
- Failure: governance

### PNT-20: Repeated exceptional use without enforcement
- Threat: exception normalization
- Actor: verifier, governance layer
- Scope: COMMON
- Preconditions: repeated exceptional requests beyond allowed threshold
- Steps: inspect review and enforcement records
- Expected result: governance response triggered
- Failure: governance

## Repetition boundary tests
At minimum, testing MUST include:
- one repeated-transaction test against the same verifier
- one repeated-transaction test across different verifiers

These tests are required because several privacy failures become visible only under repetition.
