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

## How to report
If you identify a security or privacy issue:
1. Report it privately to the maintainers before opening a public issue.
2. Include the affected document, section, flow, ADR, or conformance material.
3. Describe the impact, affected profile(s), and any realistic attacker or verifier behavior required.
4. Avoid publishing exploit details or reproduction material until the issue has been reviewed.

Send reports with enough detail to reproduce the concern in design terms. Useful details include:
- the threat scenario
- the affected actor or trust boundary
- why the current design fails
- the likely privacy, security, or governance impact
- whether the issue affects the common baseline, Profile R, or Profile P
- a proposed mitigation, if available

## What belongs here
Examples of in-scope issues include:
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

## What does not belong here
The following are usually not security reports unless they materially affect the design's privacy or security properties:
- routine editorial mistakes with no behavioral consequence
- preference disagreements without a concrete threat, abuse case, or failure mode
- requests for product support, feature delivery, or roadmap commitments
- hypothetical implementation bugs in third-party systems that are not evidenced in this repository's design

## Handling model
Because this is a public architecture project, triage focuses on design correctness rather than operational incident response.

Maintainers may:
- clarify scope and affected materials
- request a minimal written reproduction of the issue
- document the issue in an ADR, issue, or spec update after initial review
- treat unresolved but credible concerns as open design risks until they are closed by documentation or conformance changes

## Project maturity note
This is not a production security program. It is a public design and standards project. Reports that identify contradictions, unsafe defaults, missing governance controls, or untestable privacy guarantees are still valuable and in scope.
