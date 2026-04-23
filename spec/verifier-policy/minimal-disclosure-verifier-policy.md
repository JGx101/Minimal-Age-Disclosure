# Minimal-Disclosure Verifier Policy

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines normative verifier behavior for the normal minimal age-disclosure flow and the corresponding wallet handling expectations for verifier requests.

This specification constrains the use of the canonical request and response objects defined by `spec/claim-profile/age-threshold-proof-profile.md`.

## 2. Conformance subjects
This specification applies primarily to:
- verifiers
- verifier-integrating relying parties

This specification applies secondarily to wallets insofar as wallets MUST enforce or refuse non-conformant verifier requests.

## 3. Verifier request construction rules
A conformant verifier MUST send a normal-flow request containing the canonical request fields:
- `object_type`
- `object_version`
- `profile_ref`
- `verifier_class`
- `requested_threshold`
- `audience`
- `nonce`
- `purpose`
- `policy_ref`
- `jurisdiction_ref`
- `maximum_assurance_bucket`
- `binding_mode`
- `freshness_requirement`
- `exception_requested`

A conformant verifier SHOULD request one threshold unless multiple thresholds are strictly necessary for the governing rule.

A conformant verifier MUST set `exception_requested` to `false` for normal-flow requests.

## 4. Binding mode policy
`V1` verifiers MUST use `B0` unless a stricter profile requires `B2`.

`V2` verifiers MAY use `B1` where the governing policy requires stronger anti-sharing controls.

`Profile R` high-assurance requests MUST use `B1`.

`Profile P` normal-flow requests MUST use `B2`.

A verifier MUST NOT request a binding mode that creates cross-verifier correlation in normal flow.

A verifier MUST NOT request `B1` solely to force sticky same-verifier continuity where the governing rule can be satisfied by `B0` or `B2`.

A verifier MUST NOT treat `B0` as a silent fallback for `B1`.

A verifier MAY accept `B2` instead of `B1` only where the governing policy does not require `B1` same-verifier continuity and the request or profile explicitly allows that alternative.

## 5. Freshness policy
`freshness_requirement` MUST be one of:
- `none`
- `issuer_trust_state`
- `root_credential_state`
- `wallet_compromise_state`

A verifier MUST NOT require token-specific live issuer callbacks as a freshness mechanism in normal flow.

## 6. Allowed normal-flow requests
A conformant verifier MAY request only:
- supported threshold claims
- the minimum assurance bucket needed for the decision
- issuer information required by the applicable trust-resolution path
- bounded validity evidence
- audience and nonce binding evidence
- the binding mode required by verifier class and profile
- permitted freshness evidence

A conformant verifier MUST use `policy_ref` and `jurisdiction_ref` values from governed registries or controlled public enumerations.

A conformant verifier MUST run the metadata cross-field review in `spec/privacy/metadata-minimisation.md` before deploying a normal-flow request profile.

## 7. Forbidden normal-flow requests
A conformant verifier MUST NOT request in the normal flow:
- legal name
- exact DOB
- document number
- document image
- stable verifier-visible holder identifier
- stable verifier-visible root credential reference
- direct root credential presentation
- unrelated identity or account attributes
- unique status callback URI
- token-specific live issuer callbacks
- exceptional disclosure fields
- policy, jurisdiction, issuer, status, proof-format, or timestamp values that become practical correlators in combination

## 8. Wallet handling of verifier requests
A conformant wallet MUST:
- evaluate a verifier request against this policy
- reject or refuse requests missing `audience`
- reject or refuse requests missing `nonce`
- reject or refuse requests containing forbidden normal-flow fields
- reject or refuse requests with impermissible binding modes
- reject or refuse unsupported binding modes unless a new conformant request explicitly permits an alternative mode
- reject or refuse attempts to force `B1` continuity for ineligible or unrelated purposes
- derive a verifier-facing proof rather than disclose the root credential
- route exceptional requests to the red-path UX defined by exception governance

A conformant wallet SHOULD:
- show the holder what fields are being requested
- distinguish clearly between normal flow and exceptional flow
- keep local disclosure records where feasible without creating reusable external correlators

## 9. Verifier obligations
A conformant verifier MUST:
- use the minimum viable request
- validate issuer trust before accepting the derived proof
- validate audience binding and nonce binding
- validate bounded validity information
- validate binding mode eligibility
- validate that the response binding mode matches the request or an explicitly permitted alternative
- remain within the permissions of its verifier class
- keep exceptional handling outside normal-flow conformance

A conformant verifier MUST NOT:
- treat the exceptional path as a default substitute for the normal path
- use telemetry to reconstruct holder activity histories
- retain raw proof material by default
- retain `B1` verifier-scoped continuity material as default telemetry

## 10. Data handling boundary
A conformant verifier MAY retain only the minimum retained fields defined in `spec/verifier-policy/verifier-compliance-and-retention.md`.

A conformant verifier MUST treat retention beyond that minimum as either:
- explicitly governed exceptional retention, or
- non-conformant behavior

## 11. Exceptional-flow boundary
Any request outside the allowed normal-flow rules in this specification MUST be treated as exceptional.

Any interaction that depends on exceptional disclosure MUST be treated as outside normal-flow conformance and MUST satisfy `spec/verifier-policy/exception-governance.md`.

A verifier MUST NOT invoke exceptional disclosure unless the normal-path insufficiency test in the exception-governance specification passes.

A service that requires exceptional disclosure for ordinary access, or uses exceptional disclosure as the default journey, MUST be treated as exception-by-design and MUST NOT be presented as conformant normal flow.

## 12. Profile-specific notes
### 12.1 Profile R
`Profile R` verifiers MUST preserve the common normal-flow restrictions and MUST NOT assume that deployment pragmatism removes privacy obligations.

### 12.2 Profile P
`Profile P` verifiers MUST preserve the common normal-flow restrictions and MUST use `B2` for normal-flow proof of possession.
