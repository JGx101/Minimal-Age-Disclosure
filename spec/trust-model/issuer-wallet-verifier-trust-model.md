# Issuer, Wallet, and Verifier Trust Model

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines the trust roles, trust classes, trust-registry limits, trust-resolution rules, state domains, and status boundaries for minimal age disclosure.

## 2. Trust roles
The common trust model includes:
- issuer
- wallet
- verifier
- trust registry
- status publisher or relay
- auditor or certifier

## 3. Issuer classes
The common governance model MUST support:
- `A0`: authoritative issuer
- `A1`: registered private issuer
- `A2`: derived-attribute issuer

Issuer class is the default normal-flow issuer disclosure.

Exact issuer identity MAY be used only where issuer class and `issuer_trust_ref` are insufficient for trust validation.

## 4. Verifier classes
The common governance model MUST support:
- `V1`: standard verifier
- `V2`: high-assurance verifier
- `VX`: exceptional verifier

`V1` MUST use normal-flow disclosure and MUST NOT invoke exceptional disclosure.

`V2` MAY request `B1` binding and bounded step-up only where the governing rule requires it.

`VX` MAY request exceptional higher disclosure only under exception governance.

## 5. Wallet trust responsibilities
A conformant wallet MUST:
- protect the root credential
- enforce disclosure policy in the normal flow
- derive transaction-bound proofs for verifier-facing operation
- enforce binding mode eligibility
- support recovery and compromise handling according to the state model
- refuse non-conformant normal-flow requests

## 6. Trust registry data limits
A trust registry MAY expose:
- issuer-validation metadata
- verification material or trust anchors
- issuer class
- issuer trust state
- supported profile references
- status-method references where needed

A trust registry MUST NOT expose:
- holder data
- root credential identifiers
- presentation histories
- verifier telemetry
- data that turns the registry into a holder or verifier tracking service

## 7. Trust resolution rules
A verifier MUST validate issuer trust before accepting a derived proof.

Normal-flow trust validation MUST use the least specific issuer information compatible with the applicable trust path.

Issuer class plus `issuer_trust_ref` SHOULD be sufficient by default.

Exact issuer identity MAY be resolved only when needed for trust validation and MUST NOT become a default verifier-retained identifier.

## 8. Status model boundary
Status handling MUST apply only to:
- issuer trust state
- root credential state
- wallet compromise state

Per-presentation live issuer callbacks MUST NOT be used in normal flow.

Status evidence MUST be batched, cacheable, relayable, or otherwise non-unique where status is needed.

## 9. State domains
Issuer trust state MUST use:
- `trusted`
- `under_review`
- `suspended`
- `withdrawn`
- `compromised`
- `retired`

Root credential state MUST use:
- `active`
- `expiring`
- `suspended`
- `revoked`
- `reissued`
- `expired`

Wallet compromise state MUST use:
- `normal`
- `lost_unconfirmed`
- `lost_confirmed`
- `compromised`
- `recovered`
- `retired`

Detailed flows are defined in `spec/trust-model/recovery-and-compromise.md`.

## 10. Common baseline trust requirements
All conformant implementations MUST satisfy the following:
- issuer trust MUST be resolvable before a verifier accepts a proof
- the trust registry MUST remain limited to issuer-validation functions
- root credential state MUST NOT require presentation logs
- wallet compromise state MUST NOT create holder activity logs
- verifier class and issuer class semantics MUST be documented and auditable

## 11. Profile-specific trust notes
### 11.1 Profile R
`Profile R` MUST prioritize trust validation that is deployable and auditable on mainstream rails while preserving the metadata minimisation baseline.

### 11.2 Profile P
`Profile P` MUST preserve stronger anti-correlation guarantees and SHOULD avoid exact issuer disclosure where a privacy-preserving trust reference is sufficient.
