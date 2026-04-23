# Age Threshold Proof Profile

## Status
Draft

## 1. Purpose
This specification defines the normative verifier-facing claim and request contract for minimal age disclosure in the normal flow.

This specification applies to:
- wallets that derive normal-flow proofs
- verifiers that request and evaluate normal-flow proofs
- issuers that implement profile-compatible root credentials

## 2. Conformance
An implementation claiming conformance to this specification MUST implement the common baseline requirements in this document.

Profile-specific behavior:
- `Profile R` implementations MUST satisfy the common baseline and any `Profile R` requirements in this document.
- `Profile P` implementations MUST satisfy the common baseline and any `Profile P` requirements in this document.

## 3. Terms
### Root credential
A wallet-held credential issued after evidence checking and used as the basis for derived proof generation.

### Derived proof
A verifier-facing, transaction-bound proof produced from a root credential or equivalent wallet-held authority.

### Normal flow
The default minimal-disclosure path for age-threshold evaluation.

### Exceptional flow
A separately governed, higher-disclosure path outside normal-flow conformance.

### Assurance bucket
A bounded assurance category intended to provide verifier-relevant confidence information without disclosing detailed provenance.

### Issuer class
A bounded issuer category defined by the trust model.

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

## 5. Request object
This specification is the canonical owner of the normal-flow verifier request object.

### 5.1 Required request fields
A normal-flow verifier request MUST include:
- `requested_threshold`
- `audience`
- `nonce`
- `purpose` or `policy_context`
- `profile_ref`

### 5.2 Optional request fields
A normal-flow verifier request MAY include:
- `maximum_assurance_bucket`
- `freshness_requirement`, where the applicable profile and policy permit it
- `jurisdiction_ref`, where the verifier needs to indicate the governing policy context

### 5.3 Forbidden request fields
A normal-flow verifier request MUST NOT require or request:
- legal name
- exact DOB
- document number
- document image
- stable verifier-visible holder identifier
- stable verifier-visible root credential reference
- direct presentation of the root credential
- unrelated account or identity attributes

### 5.4 Request ownership note
Verifier behavior constraints on the request object are defined by `spec/verifier-policy/minimal-disclosure-verifier-policy.md`.

## 6. Derived proof result
### 6.1 Required disclosures
A normal-flow derived proof MUST contain only the minimum information required for threshold evaluation:
- a satisfied threshold result
- bounded validity information
- audience binding evidence
- nonce binding evidence
- transaction-bound proof of rightful possession

### 6.2 Optional disclosures
A normal-flow derived proof MAY include:
- coarse assurance metadata
- issuer information only to the minimum extent required for trust validation

### 6.3 Forbidden disclosures
A normal-flow derived proof MUST NOT include:
- legal name
- exact DOB
- document number
- document image
- stable verifier-visible holder identifier
- stable verifier-visible root credential reference
- unnecessary detailed provenance
- reusable verifier-visible proof-binding artifacts

## 7. Root credential boundary
The root credential MUST NOT be the ordinary verifier-facing artifact in the normal flow.

The root credential MAY contain richer lifecycle, assurance, or issuer-side management information, but such information MUST NOT automatically become verifier-visible.

## 8. Error and refusal conditions
A wallet MUST reject or refuse a normal-flow request if:
- a required request field is missing
- a forbidden request field is present
- the requested flow would require direct root credential disclosure
- the request exceeds the constraints of the applicable verifier policy

## 9. Common baseline requirements
All conformant implementations MUST satisfy the following:
- the normal verifier path MUST use a derived proof
- the root credential MUST remain outside the ordinary verifier-facing artifact set
- the normal flow MUST disclose only the minimum data required for threshold decisioning
- the normal flow MUST NOT disclose stable verifier-visible holder identifiers
- the normal flow MUST NOT rely on token-specific live issuer callbacks by default

## 10. Profile-specific requirements
### 10.1 Profile R
`Profile R` implementations MUST prioritize:
- deployment fit
- standards-aligned request and presentation behavior
- auditability

`Profile R` implementations MAY disclose exact issuer identity only where the trust-resolution rules require it.

The minimum holder-binding mechanism for `Profile R` remains subject to [ADR-0008](../../docs/adr/0008-minimum-holder-binding-mechanism-for-profile-r.md).

### 10.2 Profile P
`Profile P` implementations MUST preserve the common baseline and SHOULD impose stricter anti-correlation controls than `Profile R`.

`Profile P` implementations MAY use stronger unlinkability-preserving proof constructions, provided they do not weaken the common normal-flow exclusions.

## 11. Open dependencies
This specification depends on further ADR decisions for:
- exact issuer resolution in the normal flow
- assurance bucket taxonomy
- freshness and validity granularity
- conditions for non-normal root credential disclosure
