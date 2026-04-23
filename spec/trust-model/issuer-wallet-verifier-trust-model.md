# Issuer, Wallet, and Verifier Trust Model

## Status
Draft

## 1. Purpose
This specification defines the trust roles, trust classes, trust-registry limits, and trust-resolution rules for minimal age disclosure.

## 2. Trust roles
The common trust model includes:
- issuer
- wallet
- verifier
- trust registry
- status publisher or relay
- auditor or certifier

## 3. Issuer classes
The common governance model MUST support the following issuer classes:
- `A0` authoritative issuer
- `A1` registered private issuer
- `A2` derived-attribute issuer

The exact assurance semantics of these classes remain subject to [ADR-0010](../../docs/adr/0010-assurance-bucket-taxonomy-and-request-semantics.md).

## 4. Verifier classes
The common governance model MUST support the following verifier classes:
- `V1` standard verifier
- `V2` high-assurance verifier
- `VX` exceptional verifier

Verifier class permissions and abuse thresholds remain subject to:
- [ADR-0011](../../docs/adr/0011-validity-granularity-and-freshness-policy-boundaries.md)
- [ADR-0015](../../docs/adr/0015-exception-path-abuse-thresholds-and-enforcement.md)

## 5. Wallet trust responsibilities
A conformant wallet MUST:
- protect the root credential
- enforce disclosure policy in the normal flow
- derive transaction-bound proofs for verifier-facing operation
- support recovery and compromise handling according to the applicable trust and governance rules

## 6. Trust registry data limits
A trust registry MAY expose:
- issuer-validation metadata
- verification material or trust anchors
- issuer class
- supported profile references
- status-method references where needed

A trust registry MUST NOT expose:
- holder data
- presentation histories
- verifier telemetry
- data that turns the registry into a holder or verifier tracking service

## 7. Trust resolution rules
A verifier MUST validate issuer trust before accepting a derived proof.

The exact minimum disclosure required for normal-flow trust resolution remains subject to [ADR-0007](../../docs/adr/0007-exact-issuer-resolution-for-trust-validation.md).

Until that decision is made:
- coarse issuer class SHOULD be the default disclosure target
- exact issuer identity MAY be disclosed only where the applicable trust path requires it

## 8. Status model boundary
Status handling MUST apply primarily to:
- issuer trust state
- root credential state
- wallet compromise state

Per-presentation live issuer callbacks SHOULD be excluded by default and MUST NOT be treated as the common normal-flow baseline.

Freshness and status trigger boundaries remain subject to [ADR-0011](../../docs/adr/0011-validity-granularity-and-freshness-policy-boundaries.md).

## 9. Recovery, rotation, and compromise hooks
This trust model MUST support the following linked controls:
- issuer key rotation
- issuer compromise response
- root credential suspension or invalidation
- wallet compromise handling
- recovery and re-issuance boundaries

Detailed lifecycle choices remain subject to:
- `spec/trust-model/recovery-and-compromise.md`
- [ADR-0013](../../docs/adr/0013-conditions-for-non-normal-root-credential-disclosure.md)

## 10. Common baseline trust requirements
All conformant implementations MUST satisfy the following:
- issuer trust MUST be resolvable before a verifier accepts a proof
- the trust registry MUST remain limited to issuer-validation functions
- the root credential MUST remain outside ordinary verifier-facing disclosure
- verifier class and issuer class semantics MUST be documented and auditable

## 11. Profile-specific trust notes
### 11.1 Profile R
`Profile R` MUST prioritize trust validation that is deployable and auditable on mainstream rails.

### 11.2 Profile P
`Profile P` SHOULD preserve stronger anti-correlation guarantees and MAY use stricter trust-disclosure constraints where technically feasible.
