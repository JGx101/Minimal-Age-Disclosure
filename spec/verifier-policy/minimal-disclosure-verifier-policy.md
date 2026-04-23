# Minimal-Disclosure Verifier Policy

## Status
Draft

## 1. Purpose
This specification defines normative verifier behavior for the normal minimal age-disclosure flow and the corresponding wallet handling expectations for verifier requests.

This specification constrains the use of the request object defined by `spec/claim-profile/age-threshold-proof-profile.md`.

## 2. Conformance subjects
This specification applies primarily to:
- verifiers
- verifier-integrating relying parties

This specification applies secondarily to wallets insofar as wallets MUST enforce or refuse non-conformant verifier requests.

## 3. Verifier request construction rules
A conformant verifier MUST send a normal-flow request that includes:
- `requested_threshold`
- `audience`
- `nonce`
- `purpose` or `policy_context`
- `profile_ref`

A conformant verifier SHOULD request one threshold unless multiple thresholds are strictly necessary for the governing rule.

A conformant verifier MAY request:
- a bounded assurance bucket requirement
- a freshness requirement, where permitted by the applicable profile and trust model
- a jurisdiction reference, where needed for governing policy interpretation

## 4. Allowed normal-flow requests
A conformant verifier MAY request only:
- supported threshold claims
- the minimum assurance bucket needed for the decision
- issuer information required by the applicable trust-resolution path
- bounded validity evidence
- audience and nonce binding evidence

## 5. Forbidden normal-flow requests
A conformant verifier MUST NOT request in the normal flow:
- legal name
- exact DOB
- document number
- document image
- stable verifier-visible holder identifier
- stable verifier-visible root credential reference
- direct root credential presentation
- unrelated identity or account attributes
- token-specific live issuer callbacks as a default condition of verification

## 6. Wallet handling of verifier requests
A conformant wallet MUST:
- evaluate a verifier request against this policy
- reject or refuse requests missing `audience`
- reject or refuse requests missing `nonce`
- reject or refuse requests containing forbidden normal-flow fields
- derive a verifier-facing proof rather than disclose the root credential

A conformant wallet SHOULD:
- show the holder what fields are being requested
- distinguish clearly between normal flow and exceptional flow
- keep local disclosure records where feasible without creating reusable external correlators

## 7. Verifier obligations
A conformant verifier MUST:
- use the minimum viable request
- validate issuer trust before accepting the derived proof
- validate audience binding and nonce binding
- validate bounded validity information
- remain within the permissions of its verifier class
- keep exceptional handling outside normal-flow conformance

A conformant verifier MUST NOT:
- treat the exceptional path as a default substitute for the normal path
- use telemetry to reconstruct holder activity histories
- retain raw proof material by default

## 8. Data handling boundary
A conformant verifier MAY retain only the minimum retained fields defined in `spec/verifier-policy/verifier-compliance-and-retention.md`.

A conformant verifier MUST treat retention beyond that minimum as either:
- explicitly governed exceptional retention, or
- non-conformant behavior

## 9. Exceptional-flow boundary
Any request outside the allowed normal-flow rules in this specification MUST be treated as exceptional.

Any interaction that depends on exceptional disclosure MUST be treated as outside normal-flow conformance.

## 10. Profile-specific notes
### 10.1 Profile R
`Profile R` verifiers MUST preserve the common normal-flow restrictions and MUST NOT assume that deployment pragmatism removes privacy obligations.

### 10.2 Profile P
`Profile P` verifiers MUST preserve the common normal-flow restrictions and SHOULD accept stricter anti-correlation constraints where required by the applicable proof model.

## 11. Open dependencies
This specification depends on ADR decisions for:
- canonical verifier request ownership confirmation
- exact issuer resolution rules
- freshness and status trigger policy
- verifier audit record minimum
- exceptional-use abuse thresholds
