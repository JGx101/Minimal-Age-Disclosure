# Privacy-Negative Test Cases

## Status
Draft, architecture decisions accepted

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
- Source: claim profile, verifier policy

### PNT-02: Legal name requested in normal flow
- Threat: over-collection
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: normal-flow threshold check
- Steps: verifier requests legal name
- Expected result: non-conformant normal flow
- Failure: privacy and governance
- Source: claim profile, verifier policy

### PNT-03: Document number or image requested
- Threat: over-collection
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: normal-flow threshold check
- Steps: verifier requests document number or image
- Expected result: non-conformant normal flow
- Failure: privacy and governance
- Source: claim profile, verifier policy

### PNT-04: Stable holder identifier leakage
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect proofs for stable holder identifiers
- Expected result: no stable holder identifier visible
- Failure: privacy
- Source: claim profile, metadata minimisation

### PNT-05: Stable root credential reference leakage
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect proofs for root credential references
- Expected result: no stable root credential reference visible
- Failure: privacy
- Source: root-vs-derived proof model

### PNT-06: Reusable proof-binding artifact
- Threat: correlation
- Actor: wallet, verifier
- Scope: COMMON, R, P
- Preconditions: repeated transactions against same or different verifiers
- Steps: compare verifier-visible proof-binding artifacts
- Expected result: no reusable verifier-visible proof transcript or artifact
- Failure: privacy
- Source: root-vs-derived proof model

### PNT-07: `B1` leaks a cross-verifier artifact
- Threat: cross-verifier correlation
- Actor: wallet, verifier
- Scope: R
- Preconditions: Profile R `V2` presentations to two verifiers
- Steps: compare `B1` possession evidence and continuity material
- Expected result: no cross-verifier reusable binding artifact
- Failure: privacy and conformance
- Source: root-vs-derived proof model, retention spec

### PNT-08: `B2` leaks a verifier-stable artifact
- Threat: same-verifier or cross-verifier correlation
- Actor: wallet, verifier
- Scope: P
- Preconditions: repeated Profile P presentations
- Steps: inspect `B2` possession proof for verifier-stable handles
- Expected result: no verifier-stable holder handle or reusable binding artifact
- Failure: privacy and conformance
- Source: root-vs-derived proof model

### PNT-09: Root credential disclosed in normal flow
- Threat: disclosure boundary failure
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: normal-flow request
- Steps: inspect verifier-facing payload
- Expected result: root credential absent
- Failure: protocol and privacy
- Source: root-vs-derived proof model

### PNT-10: Missing nonce
- Threat: replay
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: crafted request without nonce
- Steps: send request
- Expected result: rejection or non-conformant flow
- Failure: protocol
- Source: claim profile, verifier policy

### PNT-11: Missing audience
- Threat: forwarding
- Actor: verifier, wallet
- Scope: COMMON
- Preconditions: crafted request without audience
- Steps: send request
- Expected result: rejection or non-conformant flow
- Failure: protocol
- Source: claim profile, verifier policy

### PNT-12: Cross-verifier proof acceptance
- Threat: replay or forwarding
- Actor: verifier
- Scope: COMMON
- Preconditions: proof captured for verifier A
- Steps: replay to verifier B
- Expected result: rejection
- Failure: protocol and privacy
- Source: verifier policy

### PNT-13: Token-specific live issuer callback
- Threat: presentation logging
- Actor: verifier, status service
- Scope: COMMON
- Preconditions: ordinary verification path
- Steps: inspect whether token-specific live callback is required
- Expected result: non-conformant normal flow
- Failure: privacy and governance
- Source: trust model, metadata minimisation

### PNT-14: Assurance metadata fingerprinting
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof contains assurance data
- Steps: inspect whether assurance uses only `AB1`, `AB2`, or `AB3`
- Expected result: bounded bucket only, no detailed provenance
- Failure: privacy
- Source: metadata minimisation

### PNT-15: Over-granular issuer metadata
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof contains issuer data
- Steps: compare issuer disclosure to trust need
- Expected result: issuer class by default; exact issuer identity only if needed for trust validation
- Failure: privacy
- Source: metadata minimisation, trust model

### PNT-16: Over-precise timestamps or validity windows
- Threat: metadata correlation
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: proof or retention record contains time data
- Steps: inspect precision
- Expected result: bounded granularity only; date for `V1`, hour for `V2`/`VX` where needed
- Failure: privacy
- Source: metadata minimisation, retention spec

### PNT-17: Correlating policy identifiers or status references
- Threat: metadata correlation
- Actor: verifier, status service
- Scope: COMMON
- Preconditions: repeated transactions
- Steps: inspect policy identifiers and status references
- Expected result: no holder-specific, session-specific, token-specific, or unique callback references
- Failure: privacy
- Source: metadata minimisation

### PNT-18: Raw proof or transcript retained by default
- Threat: over-retention
- Actor: verifier
- Scope: COMMON
- Preconditions: verifier stores audit records
- Steps: inspect retained artifacts
- Expected result: raw proof payloads and raw proof transcripts are not retained by default
- Failure: governance
- Source: retention spec

### PNT-19: Fine-grained telemetry retention
- Threat: activity reconstruction
- Actor: verifier
- Scope: COMMON
- Preconditions: telemetry enabled
- Steps: inspect retention fields
- Expected result: no fine-grained telemetry sufficient to reconstruct activity history
- Failure: governance and privacy
- Source: retention spec, metadata minimisation

### PNT-20: Recovery flow creates issuer-visible presentation history
- Threat: recovery surveillance
- Actor: issuer, wallet, recovery service
- Scope: COMMON
- Preconditions: lost, stolen, compromised, or recovered wallet
- Steps: inspect recovery data flow and retained records
- Expected result: no issuer-visible ordinary presentation history
- Failure: privacy and governance
- Source: recovery and compromise

### PNT-21: Issuer compromise response depends on presentation logs
- Threat: central tracking and unsafe compromise handling
- Actor: issuer, trust registry, verifier
- Scope: COMMON
- Preconditions: issuer trust state changes to `compromised`, `suspended`, or `withdrawn`
- Steps: inspect trust withdrawal and verifier rejection path
- Expected result: trust registry state and root/wallet state drive rejection without presentation logs
- Failure: privacy and trust
- Source: trust model, recovery and compromise

### PNT-22: Exceptional path used where normal path suffices
- Threat: exception normalization
- Actor: verifier
- Scope: COMMON
- Preconditions: normal path should satisfy the use case
- Steps: verifier invokes exceptional path
- Expected result: flagged for governance failure or review
- Failure: governance
- Source: exception governance

### PNT-23: `V1` invokes exceptional disclosure
- Threat: exception abuse
- Actor: verifier
- Scope: COMMON
- Preconditions: `V1` age-check flow
- Steps: verifier requests exceptional disclosure
- Expected result: non-conformant
- Failure: governance
- Source: exception governance

### PNT-24: Exceptional request lacks required lawful-basis fields
- Threat: exception abuse
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect required exception fields
- Expected result: non-conformant if any required field is missing, vague, or inconsistent
- Failure: governance
- Source: exception governance

### PNT-25: Wallet does not show red-path UX
- Threat: hidden over-disclosure
- Actor: wallet
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect wallet UI/UX treatment
- Expected result: explicit red-path UX with extra fields, lawful basis, retention period, verifier identity, and cancel/refuse option
- Failure: governance and privacy
- Source: exception governance

### PNT-26: Exception volume exceeds thresholds
- Threat: exception normalization
- Actor: verifier, governance layer
- Scope: COMMON
- Preconditions: monthly exception usage records
- Steps: calculate exceptional use as percentage of age-check volume
- Expected result: review above `5%`; conformance failure above `10%` or repeated review triggers across two consecutive months without scoped governance approval
- Failure: governance
- Source: exception governance

## Repetition boundary tests
At minimum, testing MUST include:
- one repeated-transaction test against the same verifier
- one repeated-transaction test across different verifiers

These tests are required because several privacy failures become visible only under repetition.
