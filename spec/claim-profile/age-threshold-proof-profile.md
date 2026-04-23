# Age Threshold Proof Profile

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines the canonical abstract verifier request object and the canonical abstract derived-proof response object for minimal age disclosure.

This specification owns object shape. Verifier behavior is constrained by `spec/verifier-policy/minimal-disclosure-verifier-policy.md`.

## 2. Conformance
An implementation claiming conformance to this specification MUST implement the common baseline requirements in this document.

Profile-specific behavior:
- `Profile R` implementations MUST satisfy the common baseline and the `Profile R` requirements in this document.
- `Profile P` implementations MUST satisfy the common baseline and the `Profile P` requirements in this document.

## 3. Terms
### Root credential
A wallet-held credential issued after evidence checking and used as the basis for derived proof generation.

### Derived proof
A verifier-facing, transaction-bound proof produced from a root credential or equivalent wallet-held authority.

### Binding mode
One of `B0`, `B1`, or `B2` as defined in `spec/root-derived-proof/root-vs-derived-proof-model.md`.

### Assurance bucket
One of `AB1`, `AB2`, or `AB3`, representing bounded assurance without detailed provenance.

### Normal flow
The default minimal-disclosure path for age-threshold evaluation.

### Exceptional flow
A separately governed, higher-disclosure path outside normal-flow conformance.

## 4. Supported threshold claims
Conformant implementations MUST support at least the following threshold claims:
- `over_13`
- `over_16`
- `over_18`
- `over_21`

Additional threshold claims MAY be supported only if:
- their semantics are documented clearly
- they do not weaken the normal-flow disclosure boundary
- they are mapped to verifier policy and conformance requirements

## 5. Canonical abstract verifier request object
The normal-flow verifier request object MUST contain:
- `object_type`
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

### 5.1 Field rules
`object_type` MUST be `age_threshold_request`.

`profile_ref` MUST identify `Profile R`, `Profile P`, or a governed profile derived from one of them.

`verifier_class` MUST be one of `V1`, `V2`, or `VX`.

`requested_threshold` MUST be one supported threshold claim.

`audience` MUST identify the verifier audience for proof binding.

`nonce` MUST be fresh for the verifier transaction.

`purpose` and `policy_ref` MUST describe the public policy or service rule being applied and MUST NOT contain holder-specific, session-specific, or transaction-specific correlation handles.

`jurisdiction_ref` MUST identify the governing jurisdiction or policy context where required.

`maximum_assurance_bucket` MUST be one of `AB1`, `AB2`, or `AB3`.

`binding_mode` MUST be one of `B0`, `B1`, or `B2`.

`freshness_requirement` MUST be one of:
- `none`
- `issuer_trust_state`
- `root_credential_state`
- `wallet_compromise_state`

`exception_requested` MUST be `false` for normal-flow requests.

### 5.2 Forbidden request content
A normal-flow verifier request MUST NOT require or request:
- legal name
- exact DOB
- document number
- document image
- stable verifier-visible holder identifier
- stable verifier-visible root credential reference
- direct presentation of the root credential
- unique status callback URI
- unrelated account or identity attributes

## 6. Canonical abstract derived-proof response object
The normal-flow derived-proof response object MUST contain:
- `object_type`
- `profile_ref`
- `threshold_result`
- `assurance_bucket`
- `issuer_class`
- `issuer_trust_ref`
- `validity_window`
- `audience_binding`
- `nonce_binding`
- `binding_mode`
- `possession_proof`
- `status_evidence`
- `proof_format_ref`

### 6.1 Field rules
`object_type` MUST be `age_threshold_response`.

`threshold_result` MUST contain only the satisfied threshold result or failure result needed for decisioning.

`assurance_bucket` MUST be one of `AB1`, `AB2`, or `AB3`.

`issuer_class` MUST be one of the issuer classes defined by the trust model.

`issuer_trust_ref` MUST support trust validation and MUST be minimised under the metadata minimisation specification.

`validity_window` MUST be bounded and MUST NOT be retained by the verifier at finer precision than the verifier retention rules allow.

`audience_binding` and `nonce_binding` MUST bind the proof to the request.

`binding_mode` MUST match the request unless the wallet refuses the request.

`possession_proof` MUST follow the selected binding mode and MUST NOT be reusable as a verifier-visible artifact across normal-flow transactions.

`status_evidence` MUST be `none`, batched, cacheable, relayable, or otherwise non-unique. It MUST NOT require a token-specific live issuer callback in normal flow.

`proof_format_ref` MAY identify a proof family or profile but MUST NOT encode holder-specific or transaction-specific correlation handles.

### 6.2 Forbidden response content
A normal-flow response MUST NOT include:
- exact DOB
- legal name
- document number
- document image
- stable holder identifier
- stable root credential reference
- unique status callback URI
- reusable proof-binding artifact
- raw evidence details
- rare issuer or assurance provenance strings beyond the governed metadata rules

## 7. Conformant examples
### 7.1 Profile R `V1` request using `B0`
```json
{
  "object_type": "age_threshold_request",
  "profile_ref": "Profile R",
  "verifier_class": "V1",
  "requested_threshold": "over_18",
  "audience": "https://example-verifier.test",
  "nonce": "fresh-random-nonce",
  "purpose": "age-gated-access",
  "policy_ref": "uk-online-age-check-policy",
  "jurisdiction_ref": "GB",
  "maximum_assurance_bucket": "AB2",
  "binding_mode": "B0",
  "freshness_requirement": "issuer_trust_state",
  "exception_requested": false
}
```

### 7.2 Profile R `V2` response using `B1`
```json
{
  "object_type": "age_threshold_response",
  "profile_ref": "Profile R",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB3",
  "issuer_class": "A1",
  "issuer_trust_ref": "trust-list-entry",
  "validity_window": "bounded",
  "audience_binding": "present",
  "nonce_binding": "present",
  "binding_mode": "B1",
  "possession_proof": "fresh-verifier-scoped-transcript",
  "status_evidence": "cached-root-state-list",
  "proof_format_ref": "openid4vp-derived-proof-profile"
}
```

### 7.3 Profile P response using `B2`
```json
{
  "object_type": "age_threshold_response",
  "profile_ref": "Profile P",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB2",
  "issuer_class": "A2",
  "issuer_trust_ref": "privacy-preserving-trust-reference",
  "validity_window": "bounded",
  "audience_binding": "present",
  "nonce_binding": "present",
  "binding_mode": "B2",
  "possession_proof": "unlinkable-possession-proof",
  "status_evidence": "none",
  "proof_format_ref": "unlinkable-derived-proof-profile"
}
```

## 8. Non-conformant examples
### 8.1 Request for exact DOB
```json
{
  "object_type": "age_threshold_request",
  "requested_threshold": "over_18",
  "requested_extra_fields": ["exact_dob"]
}
```

This request is non-conformant because exact DOB is forbidden in normal flow.

### 8.2 Response with a stable holder identifier
```json
{
  "object_type": "age_threshold_response",
  "threshold_result": "over_18:true",
  "holder_id": "stable-user-123"
}
```

This response is non-conformant because stable verifier-visible holder identifiers are forbidden in normal flow.

### 8.3 Response with a unique status callback URI
```json
{
  "object_type": "age_threshold_response",
  "threshold_result": "over_18:true",
  "status_evidence": "https://issuer.example/status/token-specific/abc123"
}
```

This response is non-conformant because unique status callback URIs create issuer-visible presentation telemetry.

## 9. Error and refusal conditions
A wallet MUST reject or refuse a normal-flow request if:
- a required request field is missing
- a forbidden request field is present
- the requested binding mode is not permitted for the verifier class or profile
- the requested flow would require direct root credential disclosure
- the request exceeds the constraints of the applicable verifier policy

## 10. Profile-specific requirements
### 10.1 Profile R
`Profile R` implementations MUST support `B0` for `V1` and `B1` for `V2`.

`Profile R` implementations MUST NOT permit `B1` pairwise material to become cross-verifier correlation material.

### 10.2 Profile P
`Profile P` implementations MUST use `B2` for normal-flow presentations.

`Profile P` implementations MUST NOT expose verifier-stable proof-binding artifacts in the normal flow.
