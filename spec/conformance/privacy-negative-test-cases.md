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

### PNT-22: Verifier directly suspends holder state
- Threat: governance bypass
- Actor: verifier, issuer, trust registry, recovery authority
- Scope: COMMON
- Preconditions: verifier reports suspected misuse
- Steps: inspect whether verifier can directly suspend root credential state, confirm wallet compromise, or force re-issuance
- Expected result: verifier report enters governed review; no direct holder suspension or compromise confirmation occurs
- Failure: governance
- Source: recovery and compromise

### PNT-23: Failed proof reveals recovery reason
- Threat: recovery-state inference
- Actor: wallet, verifier, status service
- Scope: COMMON
- Preconditions: root credential is suspended, wallet is compromised, appeal is pending, or device replacement is underway
- Steps: inspect verifier-visible failure messages, status evidence, and audit records
- Expected result: verifier sees only coarse failure such as invalid, unavailable, freshness unavailable, or policy refused
- Failure: privacy
- Source: recovery and compromise

### PNT-24: Replacement wallet is linkable to old wallet
- Threat: rebind correlation
- Actor: wallet, issuer, recovery authority, verifier
- Scope: COMMON
- Preconditions: holder replaces wallet after loss, theft, compromise, or recovery
- Steps: compare old and replacement verifier-facing proofs and status artifacts
- Expected result: no old device identifier, old root credential identifier, recovery ticket, appeal state, backup provider identity, or stable old-to-new link appears in normal flow
- Failure: privacy
- Source: recovery and compromise

### PNT-25: Grace accepts confirmed compromise
- Threat: stale-state abuse
- Actor: verifier, status service
- Scope: COMMON
- Preconditions: verifier has fresh evidence of `compromised`, `revoked`, issuer `withdrawn`, or issuer `compromised` state
- Steps: attempt normal-flow acceptance under a temporary grace rule
- Expected result: grace is unavailable; verifier rejects affected proof
- Failure: trust and governance
- Source: recovery and compromise

### PNT-26: `Profile P` status reveals holder lifecycle state
- Threat: profile-specific status correlation
- Actor: wallet, verifier, status service
- Scope: P
- Preconditions: repeated `Profile P` presentations across active, suspended, appealed, recovered, or replacement-device states
- Steps: inspect whether verifier can distinguish specific lifecycle state from status evidence or failure behavior
- Expected result: normal-flow status does not reveal detailed holder lifecycle state
- Failure: privacy
- Source: recovery and compromise

### PNT-27: Exceptional path used where normal path suffices
- Threat: exception normalization
- Actor: verifier
- Scope: COMMON
- Preconditions: normal path should satisfy the use case
- Steps: verifier invokes exceptional path
- Expected result: flagged for governance failure or review
- Failure: governance
- Source: exception governance

### PNT-28: `V1` invokes exceptional disclosure
- Threat: exception abuse
- Actor: verifier
- Scope: COMMON
- Preconditions: `V1` age-check flow
- Steps: verifier requests exceptional disclosure
- Expected result: non-conformant
- Failure: governance
- Source: exception governance

### PNT-29: Exceptional request lacks required lawful-basis fields
- Threat: exception abuse
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect required exception fields
- Expected result: non-conformant if any required field is missing, vague, or inconsistent
- Failure: governance
- Source: exception governance

### PNT-30: Wallet does not show red-path UX
- Threat: hidden over-disclosure
- Actor: wallet
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect wallet UI/UX treatment
- Expected result: explicit red-path UX with extra fields, lawful basis, retention period, verifier identity, and cancel/refuse option
- Failure: governance and privacy
- Source: exception governance

## Fixture-backed automation map
The first automation pass SHOULD evaluate the JSON fixtures under `fixtures/` before any wallet or verifier service code exists.

| Fixture | Expected result | Primary coverage |
| --- | --- | --- |
| `fixtures/requests/profile-r-v1-b0-request.json` | conformant | request shape, `Profile R`, `V1`, `B0` |
| `fixtures/requests/profile-r-v2-b1-request.json` | conformant | request shape, `Profile R`, `V2`, `B1` |
| `fixtures/requests/profile-p-b2-request.json` | conformant | request shape, `Profile P`, `B2` |
| `fixtures/requests/non-conformant-overcollection-request.json` | non-conformant | PNT-01, PNT-02, PNT-03 |
| `fixtures/requests/non-conformant-exception-request.json` | non-conformant | PNT-28, PNT-29 |
| `fixtures/responses/profile-r-v1-b0-response.json` | conformant | response shape, `B0` |
| `fixtures/responses/profile-r-v2-b1-response.json` | conformant | response shape, `B1` |
| `fixtures/responses/profile-p-b2-response.json` | conformant | response shape, `B2` |
| `fixtures/responses/non-conformant-reusable-binding-response.json` | non-conformant | PNT-06, PNT-07, PNT-08 |
| `fixtures/responses/non-conformant-metadata-fingerprint-response.json` | non-conformant | PNT-14, PNT-15, PNT-16, PNT-17 |
| `fixtures/conformance/repeated-transaction-b1-same-verifier.json` | conformant scenario | CC-BIND-06, CC-FIX-06 |
| `fixtures/conformance/repeated-transaction-cross-verifier.json` | conformant scenario | CC-BIND-03, CC-METADATA-05 |
| `fixtures/conformance/verifier-retention-default-record.json` | conformant scenario | PNT-18, PNT-19 |
| `fixtures/conformance/exception-thresholds-monthly.json` | non-conformant scenario | PNT-27, PNT-28, PNT-29, PNT-30 |
| `fixtures/conformance/recovery-scenarios.json` | conformant scenario | PNT-20, PNT-21, PNT-24 |

Additional automation MUST preserve the same failure classes and MUST NOT treat these fixtures as production protocol payloads.

### PNT-31: Exception volume exceeds thresholds
- Threat: exception normalization
- Actor: verifier, governance layer
- Scope: COMMON
- Preconditions: monthly exception usage records
- Steps: calculate exceptional use as percentage of age-check volume
- Expected result: review above `5%`; conformance failure above `10%` or repeated review triggers across two consecutive months without scoped governance approval
- Failure: governance
- Source: exception governance

### PNT-32: Exception eligibility matrix failure
- Threat: unauthorized exceptional disclosure
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request by verifier class, jurisdiction, and use case
- Steps: compare the request to the exception eligibility matrix
- Expected result: non-conformant if the class, jurisdiction context, and use case combination is not eligible
- Failure: governance
- Source: exception governance

### PNT-33: Uncontrolled lawful-basis value
- Threat: weak exception justification
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request
- Steps: inspect `lawful_basis_code` and `lawful_basis_ref`
- Expected result: non-conformant if `lawful_basis_code` is outside the controlled vocabulary, forbidden by policy, or unsupported by a concrete `lawful_basis_ref`
- Failure: governance
- Source: exception governance

### PNT-34: Normal-path insufficiency test fails
- Threat: exception normalization
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional request where threshold proof, assurance bucket, binding mode, freshness, or refusal handling could satisfy the governing rule
- Steps: inspect the `normal_path_insufficiency` record and lower-disclosure alternatives checked
- Expected result: non-conformant if the insufficiency test is absent, false, or based on convenience, conversion, analytics, or account enrichment
- Failure: governance
- Source: exception governance

### PNT-35: Wallet mishandles partial consent or refusal
- Threat: coerced over-disclosure
- Actor: wallet, verifier
- Scope: COMMON
- Preconditions: exceptional request with multiple extra fields
- Steps: holder accepts one field and refuses another, then separately refuses the whole request
- Expected result: response discloses only accepted fields for partial consent; refusal or cancellation discloses no extra evidence values; verifier does not silently retry or treat withheld fields as accepted
- Failure: governance and privacy
- Source: exception governance

### PNT-36: Audit escalation record incomplete
- Threat: unenforceable exception governance
- Actor: verifier, governance layer
- Scope: COMMON
- Preconditions: exceptional use crosses a review trigger or contains a policy defect
- Steps: inspect escalation record for review trigger, independent reviewer, outcome, remediation, and sanction state
- Expected result: non-conformant if any required escalation element is missing
- Failure: governance
- Source: exception governance

### PNT-37: Exceptional evidence retained outside declared mode
- Threat: over-retention and secondary use
- Actor: verifier
- Scope: COMMON
- Preconditions: exceptional flow discloses extra fields
- Steps: inspect storage, telemetry, analytics, product logs, fraud feature stores, model-training datasets, and account profile records
- Expected result: non-conformant if extra evidence is retained outside the declared `evidence_handling` mode, retention period, or lawful-basis relationship
- Failure: governance and privacy
- Source: exception governance, retention spec

### PNT-38: Exception-by-design service presented as conformant
- Threat: exception normalization
- Actor: verifier, governance layer
- Scope: COMMON
- Preconditions: service requires exceptional disclosure for ordinary access or makes exceptional disclosure the default path
- Steps: inspect service design, user journey, monthly exception volume, and governance classification
- Expected result: non-conformant if the service is presented as normal-flow conformant; outside-conformance governance approval does not make the service conformant to the normal minimal-disclosure profile
- Failure: governance
- Source: exception governance

### PNT-39: Silent downgrade from `B1` to `B0`
- Threat: weakened anti-sharing controls
- Actor: wallet, verifier
- Scope: R
- Preconditions: Profile R `V2` request requiring `B1`
- Steps: wallet returns a `B0` response without a new conformant request
- Expected result: non-conformant flow
- Failure: protocol and policy
- Source: root-vs-derived proof model, claim profile

### PNT-40: Malicious verifier forces sticky `B1`
- Threat: same-verifier tracking beyond policy
- Actor: verifier, wallet
- Scope: COMMON, R
- Preconditions: verifier policy permits `B0` or `B2`
- Steps: verifier requests `B1` continuity for an unrelated purpose or excessive retention period
- Expected result: wallet refuses or treats the request as exceptional and non-normal
- Failure: privacy and governance
- Source: verifier policy, retention spec

### PNT-41: `B1` continuity reused for a different verifier or purpose
- Threat: cross-context correlation
- Actor: verifier
- Scope: R
- Preconditions: retained `B1` continuity material for one verifier audience and policy purpose
- Steps: attempt to join or reuse continuity material for another audience, service, analytics dataset, or policy purpose
- Expected result: non-conformant retention and processing
- Failure: privacy and conformance
- Source: root-vs-derived proof model, retention spec

### PNT-42: Exact issuer identity used where trust reference is sufficient
- Threat: metadata correlation
- Actor: verifier
- Scope: COMMON
- Preconditions: issuer class and `issuer_trust_ref` satisfy the trust-resolution decision tree
- Steps: inspect whether the verifier requests, resolves, or retains exact issuer identity anyway
- Expected result: non-conformant normal flow or retention failure
- Failure: privacy and governance
- Source: metadata minimisation, trust model

### PNT-43: Non-registry policy or jurisdiction reference
- Threat: metadata correlation
- Actor: verifier
- Scope: COMMON
- Preconditions: normal-flow request contains `policy_ref` or `jurisdiction_ref`
- Steps: resolve each reference against the governed registry or controlled public enumeration
- Expected result: non-conformant if the reference is holder-specific, session-specific, tenant-specific, campaign-specific, transaction-specific, or absent from the approved registry
- Failure: privacy and governance
- Source: metadata minimisation, verifier policy

### PNT-44: Rare provenance string
- Threat: metadata fingerprinting
- Actor: wallet, verifier
- Scope: COMMON, R, P
- Preconditions: metadata contains issuer, assurance, status, proof-format, policy, jurisdiction, or timestamp values
- Steps: apply the population, issuer-path, time-path, registry, and combination tests
- Expected result: rare values are generalized, suppressed, or treated as exceptional-flow metadata
- Failure: privacy
- Source: metadata minimisation

### PNT-45: Cross-field metadata fingerprint
- Threat: metadata fingerprinting
- Actor: wallet, verifier
- Scope: COMMON, R, P
- Preconditions: repeated same-verifier and cross-verifier presentations
- Steps: score the full metadata bundle and estimate the smallest plausible anonymity set
- Expected result: non-conformant if the bundle exceeds the anti-fingerprinting budget or falls below the applicable anonymity-set threshold
- Failure: privacy and conformance
- Source: metadata minimisation

### PNT-46: Over-retained metadata references
- Threat: over-retention and activity reconstruction
- Actor: verifier
- Scope: COMMON
- Preconditions: verifier retains decision records
- Steps: inspect retained `issuer_trust_ref`, `proof_format_ref`, and `status_evidence`
- Expected result: only permitted coarse registry, proof-family, major-version, status-class, and public epoch values are retained
- Failure: privacy and governance
- Source: metadata minimisation, retention spec

## Repetition boundary tests
At minimum, testing MUST include:
- one repeated-transaction test against the same verifier
- one repeated-transaction test across different verifiers

These tests are required because several privacy failures become visible only under repetition.
