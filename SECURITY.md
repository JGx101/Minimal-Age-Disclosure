# Security Policy

## Scope
This repository is primarily a documentation, architecture, and conformance project. It may also contain prototype-planning materials, example flows, and test fixtures.

Security and privacy issues are in scope where they affect:
- verifier over-collection
- correlation and metadata fingerprinting
- replay and forwarding resistance
- holder-binding leakage
- trust validation
- status privacy
- recovery and compromise handling
- issuer observability
- exceptional-path abuse

## Reporting
If you identify a security or privacy issue:
- report it privately to the repository maintainer where possible
- avoid publishing exploit details before the issue is understood
- include the affected document, flow, subsystem, ADR, or conformance test

Useful report details include:
- the threat scenario
- the affected actor or trust boundary
- why the current design fails
- the likely privacy, security, or governance impact
- whether the issue affects the common baseline, Profile R, or Profile P
- a proposed mitigation, if available

## What counts as a security or privacy issue here
Examples include:
- leakage of exact DOB, legal name, document number, or document image in the normal flow
- a stable verifier-visible holder identifier or stable root-credential reference in the normal flow
- proof binding that exposes a reusable verifier-visible holder key or artifact
- verifier requests that silently force over-disclosure
- missing nonce or audience binding that enables replay or forwarding
- status, telemetry, or callback designs that create presentation logs
- metadata choices that become practical correlators
- verifier retention beyond the documented minimum
- recovery or compromise handling that breaks the privacy model
- exceptional-path governance that becomes the default commercial path
- trust-registry or issuer metadata exposure beyond the stated design boundaries

## Project maturity note
This is not a production security program. It is a public design and standards project. Reports that identify contradictions, unsafe defaults, missing governance controls, or untestable privacy guarantees are still valuable and in scope.
