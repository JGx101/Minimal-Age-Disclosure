# Age Threshold Proof Profile

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines the canonical abstract verifier request object and the canonical abstract derived-proof response object for minimal age disclosure.

This specification owns canonical object shape. Verifier behavior is constrained by `spec/verifier-policy/minimal-disclosure-verifier-policy.md`.

Exceptional-flow request and response objects are outside normal-flow conformance and are governed by `spec/verifier-policy/exception-governance.md`.

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

### 5.1 Field rules
`object_type` MUST be `age_threshold_request`.

`object_version` MUST use `major.minor` form. This draft defines version `1.0`.

`profile_ref` MUST identify `Profile R`, `Profile P`, or a governed profile derived from one of them.

`verifier_class` MUST be one of `V1`, `V2`, or `VX`.

`requested_threshold` MUST be one supported threshold claim.

`audience` MUST identify the verifier audience for proof binding.

`nonce` MUST be fresh for the verifier transaction.

`purpose` and `policy_ref` MUST describe the public policy or service rule being applied and MUST NOT contain holder-specific, session-specific, or transaction-specific correlation handles.

`policy_ref` MUST resolve through the governed registry discipline defined in `spec/privacy/metadata-minimisation.md`.

`jurisdiction_ref` MUST identify the governing jurisdiction or policy context where required and MUST resolve through a governed public registry or controlled public enumeration.

`maximum_assurance_bucket` MUST be one of `AB1`, `AB2`, or `AB3`.

`binding_mode` MUST be one of `B0`, `B1`, or `B2`.

`freshness_requirement` MUST be one of:
- `none`
- `issuer_trust_state`
- `root_credential_state`
- `wallet_compromise_state`

`exception_requested` MUST be `false` for normal-flow requests.

### 5.2 Versioning strategy
Version evolution rules:
- an implementation MUST reject an object with an unsupported major version
- a minor version MAY add optional fields only where they do not weaken disclosure, retention, or anti-correlation rules
- adding a required field, changing field meaning, widening normal-flow disclosure, or changing retention semantics requires a new major version
- unknown optional fields MUST be ignored unless their names begin with `x_`
- `x_` extension fields MUST be rejected if they request, reveal, or retain data forbidden by this specification

### 5.3 Retention classes
The field tables below use these retention classes:

| Class | Meaning |
| --- | --- |
| `RC0` | Transaction-only. Do not retain after proof validation or refusal handling. |
| `RC1` | Default-retainable only in coarse audit records permitted by verifier-retention rules. |
| `RC2` | Governed-retainable only with explicit policy, audit, access control, and deletion rules. |
| `RC3` | Forbidden for normal-flow retention and forbidden in normal-flow objects unless explicitly listed for exceptional flow. |

### 5.4 Normal-flow request field table
The normal-flow verifier request object MUST contain only the fields listed below. Additional fields are non-conformant unless they are accepted extension fields under the versioning rules.

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `object_type` | string | Yes | `age_threshold_request` | `RC1` |
| `object_version` | string | Yes | `major.minor`; this version is `1.0` | `RC1` |
| `profile_ref` | string | Yes | `Profile R`, `Profile P`, or governed derived profile reference | `RC1` |
| `verifier_class` | string | Yes | `V1`, `V2`, `VX` | `RC1` |
| `requested_threshold` | string | Yes | `over_13`, `over_16`, `over_18`, `over_21`, or governed supported threshold | `RC1` |
| `audience` | string | Yes | Verifier audience URI or governed audience identifier | `RC0` |
| `nonce` | string | Yes | Fresh unpredictable transaction nonce; minimum 128 bits of entropy | `RC0` |
| `purpose` | string | Yes | Public, human-reviewable purpose code or short description | `RC1` |
| `policy_ref` | string | Yes | Public policy, service rule, or governance reference | `RC1` |
| `jurisdiction_ref` | string | Yes | ISO 3166-1 alpha-2 country code, ISO 3166-2 subdivision code, or governed jurisdiction reference | `RC1` |
| `maximum_assurance_bucket` | string | Yes | `AB1`, `AB2`, `AB3` | `RC1` |
| `binding_mode` | string | Yes | `B0`, `B1`, `B2` | `RC1` |
| `freshness_requirement` | string | Yes | `none`, `issuer_trust_state`, `root_credential_state`, `wallet_compromise_state` | `RC1` |
| `exception_requested` | boolean | Yes | `false` | `RC1` |

### 5.5 Normal-flow request JSON Schema fragment
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://minimal-disclosure-age-proof.example/schemas/age-threshold-request-1.0.json",
  "type": "object",
  "additionalProperties": false,
  "required": ["object_type", "object_version", "profile_ref", "verifier_class", "requested_threshold", "audience", "nonce", "purpose", "policy_ref", "jurisdiction_ref", "maximum_assurance_bucket", "binding_mode", "freshness_requirement", "exception_requested"],
  "properties": {
    "object_type": { "const": "age_threshold_request" },
    "object_version": { "type": "string", "pattern": "^[1-9][0-9]*\\.[0-9]+$" },
    "profile_ref": { "type": "string", "minLength": 1 },
    "verifier_class": { "enum": ["V1", "V2", "VX"] },
    "requested_threshold": { "type": "string", "pattern": "^over_[0-9]+$" },
    "audience": { "type": "string", "minLength": 1 },
    "nonce": { "type": "string", "minLength": 22 },
    "purpose": { "type": "string", "minLength": 1 },
    "policy_ref": { "type": "string", "minLength": 1 },
    "jurisdiction_ref": { "type": "string", "minLength": 1 },
    "maximum_assurance_bucket": { "enum": ["AB1", "AB2", "AB3"] },
    "binding_mode": { "enum": ["B0", "B1", "B2"] },
    "freshness_requirement": { "enum": ["none", "issuer_trust_state", "root_credential_state", "wallet_compromise_state"] },
    "exception_requested": { "const": false }
  }
}
```

### 5.6 Forbidden request content
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
- `object_version`
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

`object_version` MUST use `major.minor` form. This draft defines version `1.0`.

`threshold_result` MUST contain only the satisfied threshold result or failure result needed for decisioning.

`assurance_bucket` MUST be one of `AB1`, `AB2`, or `AB3`.

`issuer_class` MUST be one of the issuer classes defined by the trust model.

`issuer_trust_ref` MUST support trust validation and MUST be minimised under the trust-resolution decision tree in the metadata minimisation specification.

`validity_window` MUST be bounded and MUST NOT be retained by the verifier at finer precision than the verifier retention rules allow.

`audience_binding` and `nonce_binding` MUST bind the proof to the request.

`binding_mode` MUST match the request unless the wallet refuses the request or the verifier request explicitly permits an alternative mode allowed by the governing profile.

`possession_proof` MUST follow the selected binding mode and MUST NOT be reusable as a verifier-visible artifact across normal-flow transactions.

`status_evidence` MUST be `none`, batched, cacheable, relayable, or otherwise non-unique. It MUST NOT require a token-specific live issuer callback in normal flow.

`proof_format_ref` MAY identify a proof family, governed profile, or major version but MUST NOT encode holder-specific, transaction-specific, rare implementation-specific, or cross-field correlation handles.

### 6.2 Normal-flow response field table
The normal-flow derived-proof response object MUST contain only the fields listed below. Additional fields are non-conformant unless they are accepted extension fields under the versioning rules.

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `object_type` | string | Yes | `age_threshold_response` | `RC1` |
| `object_version` | string | Yes | `major.minor`; this version is `1.0` | `RC1` |
| `profile_ref` | string | Yes | Request profile or governed compatible profile | `RC1` |
| `threshold_result` | object | Yes | See section 6.3 | `RC1` |
| `assurance_bucket` | string | Yes | `AB1`, `AB2`, `AB3`; not higher than request maximum | `RC1` |
| `issuer_class` | string | Yes | Issuer class from the trust model, for example `A0`, `A1`, or `A2` | `RC1` |
| `issuer_trust_ref` | object | Yes | See section 6.4 | `RC1`; exact issuer data is `RC2` |
| `validity_window` | object | Yes | See section 6.5 | `RC1` at approved granularity; raw timestamps are `RC3` |
| `audience_binding` | string | Yes | `present` | `RC0` |
| `nonce_binding` | string | Yes | `present` | `RC0` |
| `binding_mode` | string | Yes | `B0`, `B1`, `B2`; must match accepted request | `RC1` |
| `possession_proof` | string or object | Yes | Fresh transaction-bound proof artifact for selected binding mode | `RC0`; `B1` continuity material is `RC2` |
| `status_evidence` | object | Yes | See section 6.6 | `RC1`; unique callbacks are `RC3` |
| `proof_format_ref` | object | Yes | See section 6.7 | `RC1` |

### 6.3 `threshold_result`
`threshold_result` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `threshold` | string | Yes | Requested threshold claim, for example `over_18` | `RC1` |
| `satisfied` | boolean | Yes | `true` if the threshold is satisfied; `false` otherwise | `RC1` |
| `result_code` | string | Yes | `threshold_satisfied` or `threshold_not_satisfied` | `RC1` |

`threshold_result` MUST NOT include exact age, age band beyond the requested threshold, date of birth, evidence source, or a reason that lets the verifier infer more than the threshold result.

If `satisfied` is `true`, `result_code` MUST be `threshold_satisfied`. If `satisfied` is `false`, `result_code` MUST be `threshold_not_satisfied`.

### 6.4 `issuer_trust_ref`
`issuer_trust_ref` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `trust_framework_ref` | string | Yes | Public trust framework, governance profile, or trust-list reference | `RC1` |
| `trust_resolution_method` | string | Yes | `trust_list`, `trust_registry`, `cryptographic_accumulator`, or `governance_profile` | `RC1` |
| `trust_list_entry_ref` | string | Optional | Non-holder-specific and non-token-specific trust entry, accumulator, or registry reference | `RC1` |
| `exact_issuer_disclosed` | boolean | Yes | `false` in normal flow unless exact issuer resolution is explicitly justified by trust-validation rules | `RC1`; exact issuer identity is `RC2` |

`issuer_trust_ref` MUST support trust validation without revealing holder-specific, token-specific, or rare issuer-provenance strings.

Exact issuer identity MAY be resolved only as permitted by the trust model and metadata minimisation rules. If exact issuer identity is resolved, it MUST NOT be retained by default.

### 6.5 `validity_window`
`validity_window` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `granularity` | string | Yes | `date` or `hour` | `RC1` |
| `valid_from` | string | Optional | Date bucket if `granularity` is `date`; hour bucket if `granularity` is `hour` | `RC1` |
| `valid_until` | string | Yes | Date bucket if `granularity` is `date`; hour bucket if `granularity` is `hour` | `RC1` |
| `freshness_requirement_satisfied` | boolean | Yes | `true` or `false` | `RC1` |

`validity_window` MUST be bounded and MUST NOT expose or retain raw proof-generation timestamps.

Date buckets MUST use `YYYY-MM-DD`. Hour buckets MUST use `YYYY-MM-DDThh:00Z` or an equivalent governed hour-level bucket. Verifiers MUST retain validity data only at the granularity permitted by verifier-retention rules.

### 6.6 `status_evidence`
`status_evidence` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `status_check_type` | string | Yes | `none`, `batched_status`, `cacheable_status`, `relayable_status`, `issuer_trust_state`, `root_credential_state`, `wallet_compromise_state` | `RC1` |
| `status_ref` | string | Optional | Public, batched, cacheable, relayable, or otherwise non-unique reference | `RC1` |
| `freshness_bucket` | string | Optional | Date or hour bucket sufficient for requested freshness | `RC1` |
| `live_issuer_callback_allowed` | boolean | Yes | `false` | `RC1` |

`status_evidence` MUST NOT require a token-specific live issuer callback in normal flow.

`status_ref` MUST NOT be holder-specific, token-specific, or unique to a single verifier presentation.

### 6.7 `proof_format_ref`
`proof_format_ref` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `proof_family` | string | Yes | `openid4vp`, `sd_jwt_vc`, `mdoc`, `bbs`, `cl_signature`, `zk_profile`, or `other_governed` | `RC1` |
| `profile_id` | string | Yes | Public proof profile identifier | `RC1` |
| `profile_version` | string | Optional | Public profile version | `RC1` |
| `correlation_scope` | string | Yes | `none`, `verifier_transaction`, or `verifier_scoped` | `RC1` |

`proof_format_ref` MUST NOT encode holder-specific, credential-specific, or transaction-specific correlation handles.

`correlation_scope` describes the proof family's designed correlation boundary; it does not authorize retention of proof artifacts beyond the selected binding mode.

### 6.8 Binding mode negotiation
The `binding_mode` field in a normal-flow request is the verifier's required mode for that transaction.

A wallet MUST NOT silently return a different `binding_mode`.

If the wallet cannot satisfy the requested `binding_mode`, it MUST refuse the request or require the verifier to issue a new request that explicitly permits an alternative mode.

Downgrading a `B1` request to `B0` is non-conformant unless the verifier issues a new `V1`/`B0` request whose policy no longer requires high-assurance anti-sharing controls.

Using `B2` in response to a `B1` request is permitted only where the verifier request or governing profile explicitly accepts `B2` as an alternative and the decision does not depend on `B1` same-verifier continuity.

### 6.9 Normal-flow response JSON Schema fragment
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://minimal-disclosure-age-proof.example/schemas/age-threshold-response-1.0.json",
  "type": "object",
  "additionalProperties": false,
  "required": ["object_type", "object_version", "profile_ref", "threshold_result", "assurance_bucket", "issuer_class", "issuer_trust_ref", "validity_window", "audience_binding", "nonce_binding", "binding_mode", "possession_proof", "status_evidence", "proof_format_ref"],
  "properties": {
    "object_type": { "const": "age_threshold_response" },
    "object_version": { "type": "string", "pattern": "^[1-9][0-9]*\\.[0-9]+$" },
    "profile_ref": { "type": "string", "minLength": 1 },
    "threshold_result": { "$ref": "#/$defs/threshold_result" },
    "assurance_bucket": { "enum": ["AB1", "AB2", "AB3"] },
    "issuer_class": { "type": "string", "pattern": "^A[0-9]+$" },
    "issuer_trust_ref": { "$ref": "#/$defs/issuer_trust_ref" },
    "validity_window": { "$ref": "#/$defs/validity_window" },
    "audience_binding": { "const": "present" },
    "nonce_binding": { "const": "present" },
    "binding_mode": { "enum": ["B0", "B1", "B2"] },
    "possession_proof": { "oneOf": [{ "type": "string", "minLength": 1 }, { "type": "object" }] },
    "status_evidence": { "$ref": "#/$defs/status_evidence" },
    "proof_format_ref": { "$ref": "#/$defs/proof_format_ref" }
  },
  "$defs": {
    "threshold_result": {
      "type": "object",
      "additionalProperties": false,
      "required": ["threshold", "satisfied", "result_code"],
      "properties": {
        "threshold": { "type": "string", "pattern": "^over_[0-9]+$" },
        "satisfied": { "type": "boolean" },
        "result_code": { "enum": ["threshold_satisfied", "threshold_not_satisfied"] }
      }
    },
    "issuer_trust_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["trust_framework_ref", "trust_resolution_method", "exact_issuer_disclosed"],
      "properties": {
        "trust_framework_ref": { "type": "string", "minLength": 1 },
        "trust_resolution_method": { "enum": ["trust_list", "trust_registry", "cryptographic_accumulator", "governance_profile"] },
        "trust_list_entry_ref": { "type": "string", "minLength": 1 },
        "exact_issuer_disclosed": { "type": "boolean" }
      }
    },
    "validity_window": {
      "type": "object",
      "additionalProperties": false,
      "required": ["granularity", "valid_until", "freshness_requirement_satisfied"],
      "properties": {
        "granularity": { "enum": ["date", "hour"] },
        "valid_from": { "type": "string", "minLength": 1 },
        "valid_until": { "type": "string", "minLength": 1 },
        "freshness_requirement_satisfied": { "type": "boolean" }
      }
    },
    "status_evidence": {
      "type": "object",
      "additionalProperties": false,
      "required": ["status_check_type", "live_issuer_callback_allowed"],
      "properties": {
        "status_check_type": { "enum": ["none", "batched_status", "cacheable_status", "relayable_status", "issuer_trust_state", "root_credential_state", "wallet_compromise_state"] },
        "status_ref": { "type": "string", "minLength": 1 },
        "freshness_bucket": { "type": "string", "minLength": 1 },
        "live_issuer_callback_allowed": { "const": false }
      }
    },
    "proof_format_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["proof_family", "profile_id", "correlation_scope"],
      "properties": {
        "proof_family": { "enum": ["openid4vp", "sd_jwt_vc", "mdoc", "bbs", "cl_signature", "zk_profile", "other_governed"] },
        "profile_id": { "type": "string", "minLength": 1 },
        "profile_version": { "type": "string", "minLength": 1 },
        "correlation_scope": { "enum": ["none", "verifier_transaction", "verifier_scoped"] }
      }
    }
  }
}
```

### 6.10 Verifier persistence from a normal-flow response
A verifier MAY persist only these values from a normal-flow response by default:
- `threshold_result.threshold`
- `threshold_result.satisfied`
- `threshold_result.result_code`
- `assurance_bucket`
- `issuer_class`
- `issuer_trust_ref.trust_framework_ref`
- `issuer_trust_ref.trust_resolution_method`
- non-unique `issuer_trust_ref.trust_list_entry_ref`, where needed for trust audit
- `validity_window` at the verifier's approved time-bucket granularity
- `binding_mode`
- `status_evidence.status_check_type`
- non-unique `status_evidence.status_ref`, where needed for audit
- `proof_format_ref.proof_family`
- `proof_format_ref.profile_id`
- `proof_format_ref.profile_version`
- `proof_format_ref.correlation_scope`

A verifier MUST NOT persist `audience_binding`, `nonce_binding`, `possession_proof`, raw proof transcripts, raw proof payloads, reusable binding artifacts, unique status references, or exact issuer identity by default.

Retention of exact issuer identity, `B1` continuity material, or any exceptional-flow evidence requires the governed retention conditions in `spec/verifier-policy/verifier-compliance-and-retention.md`.

### 6.11 Forbidden response content
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
- combinations of otherwise allowed metadata fields that become practical correlators under the cross-field review in `spec/privacy/metadata-minimisation.md`

## 7. Wallet refusal object
A wallet MUST return or surface a refusal object when it rejects a request and the transport or UX flow requires a machine-readable result.

The refusal object MUST NOT disclose whether the holder is under or over a threshold unless the wallet is returning the formal `threshold_result` defined in section 6.3.

### 7.1 Wallet refusal field table
| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `object_type` | string | Yes | `wallet_refusal` | `RC1` |
| `object_version` | string | Yes | `major.minor`; this version is `1.0` | `RC1` |
| `refusal_context` | string | Yes | `normal_request` or `exceptional_request` | `RC1` |
| `refusal_code` | string | Yes | See section 7.2 | `RC1` |
| `retryable` | boolean | Yes | `true` or `false` | `RC1` |
| `policy_ref` | string | Optional | Public wallet, verifier, or governance policy reference | `RC1` |
| `refusal_reason_public` | string | Optional | Generic human-readable reason without holder-specific facts | `RC1` |
| `audience_binding` | string | Optional | `present` if bound to request | `RC0` |
| `nonce_binding` | string | Optional | `present` if bound to request | `RC0` |
| `exception_red_path_shown` | boolean | Optional | `true` or `false`; only for exceptional requests | `RC1` |

### 7.2 Wallet refusal codes
`refusal_code` MUST be one of:
- `missing_required_field`
- `forbidden_field_requested`
- `unsupported_object_version`
- `unsupported_profile`
- `unsupported_verifier_class`
- `unsupported_binding_mode`
- `freshness_unavailable`
- `trust_validation_failed`
- `status_unavailable`
- `exception_not_allowed`
- `lawful_basis_missing`
- `exception_fields_excessive`
- `user_cancelled`
- `wallet_policy_refused`
- `proof_unavailable`

`refusal_reason_public` MUST NOT include exact age, date of birth, legal name, document data, root credential identifiers, or wallet-internal state beyond the generic refusal code.

### 7.3 Wallet refusal JSON Schema fragment
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://minimal-disclosure-age-proof.example/schemas/wallet-refusal-1.0.json",
  "type": "object",
  "additionalProperties": false,
  "required": ["object_type", "object_version", "refusal_context", "refusal_code", "retryable"],
  "properties": {
    "object_type": { "const": "wallet_refusal" },
    "object_version": { "type": "string", "pattern": "^[1-9][0-9]*\\.[0-9]+$" },
    "refusal_context": { "enum": ["normal_request", "exceptional_request"] },
    "refusal_code": { "enum": ["missing_required_field", "forbidden_field_requested", "unsupported_object_version", "unsupported_profile", "unsupported_verifier_class", "unsupported_binding_mode", "freshness_unavailable", "trust_validation_failed", "status_unavailable", "exception_not_allowed", "lawful_basis_missing", "exception_fields_excessive", "user_cancelled", "wallet_policy_refused", "proof_unavailable"] },
    "retryable": { "type": "boolean" },
    "policy_ref": { "type": "string", "minLength": 1 },
    "refusal_reason_public": { "type": "string", "minLength": 1 },
    "audience_binding": { "const": "present" },
    "nonce_binding": { "const": "present" },
    "exception_red_path_shown": { "type": "boolean" }
  }
}
```

## 8. Exceptional request and response objects
Exceptional request and response objects are outside normal-flow conformance. They are defined here so wallets and verifiers can distinguish governed exceptional disclosure from normal-flow objects.

Where an exception-governance transport or audit envelope uses additional governance fields, it MUST map those fields to the canonical profile objects below or identify the envelope as outside this canonical object profile.

### 8.1 Exceptional request field table
| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `object_type` | string | Yes | `age_threshold_exception_request` | `RC1` |
| `object_version` | string | Yes | `major.minor`; this version is `1.0` | `RC1` |
| `profile_ref` | string | Yes | `Profile R`, `Profile P`, or governed derived profile reference | `RC1` |
| `verifier_class` | string | Yes | `V2` or `VX`; `V1` is non-conformant | `RC1` |
| `requested_threshold` | string | Optional | Supported threshold claim, where threshold proof remains part of the flow | `RC1` |
| `audience` | string | Yes | Verifier audience URI or governed audience identifier | `RC0` |
| `nonce` | string | Yes | Fresh unpredictable transaction nonce; minimum 128 bits of entropy | `RC0` |
| `purpose` | string | Yes | Public, human-reviewable exceptional purpose | `RC1` |
| `policy_ref` | string | Yes | Public policy, service rule, or governance reference | `RC1` |
| `jurisdiction_ref` | string | Yes | Governing jurisdiction or policy context | `RC1` |
| `exception_requested` | boolean | Yes | `true` | `RC1` |
| `lawful_basis_ref` | string | Yes | Public lawful-basis or governance reference | `RC1` |
| `requested_extra_fields` | array of strings | Yes | Minimum fields needed for the exceptional purpose | `RC2`; values forbidden in normal flow are `RC3` there |
| `necessity_explanation` | string | Yes | Human-reviewable explanation for why normal flow is insufficient | `RC1` |
| `retention_period` | object | Yes | See section 8.3 | `RC1` |
| `audit_contact` | string | Yes | Public audit contact URI, email, or governance endpoint | `RC1` |
| `review_or_appeal_ref` | string | Yes | Public review, appeal, or redress reference | `RC1` |
| `normal_flow_unavailable_reason` | string | Yes | See section 8.2 | `RC1` |
| `exception_class_ref` | string | Optional | Governance-approved scoped exception class | `RC1` |

### 8.2 Exceptional request field rules
`normal_flow_unavailable_reason` MUST be one of:
- `governing_rule_requires_extra_data`
- `normal_proof_failed_governed_step_up`
- `fraud_or_safety_governed_review`
- `manual_review_required`
- `other_governed`

`requested_extra_fields` MUST be bounded to the minimum data needed for the lawful exceptional purpose. Allowed values MUST come from a governed vocabulary. The baseline vocabulary is:
- `legal_name`
- `exact_dob`
- `document_number`
- `document_image`
- `issuer_identity`
- `root_credential_disclosure`
- `identity_evidence`
- `account_linkage_evidence`
- `other_governed`

Any `V1` exceptional request is non-conformant.

An exceptional request with missing, vague, internally inconsistent, or non-public lawful-basis fields MUST be refused by the wallet.

### 8.3 `retention_period`
`retention_period` MUST be an object with this structure:

| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `duration` | string | Yes | ISO 8601 duration or governed legal-retention reference | `RC1` |
| `justification_ref` | string | Yes | Public policy or legal justification for the duration | `RC1` |
| `disposal_action` | string | Yes | `delete`, `anonymise`, `return_to_holder`, or `governed_archive` | `RC1` |

### 8.4 Exceptional response field table
| Field | Type | Required | Allowed values or structure | Retention class |
| --- | --- | --- | --- | --- |
| `object_type` | string | Yes | `age_threshold_exception_response` | `RC1` |
| `object_version` | string | Yes | `major.minor`; this version is `1.0` | `RC1` |
| `normal_flow_conformance` | boolean | Yes | `false` | `RC1` |
| `profile_ref` | string | Yes | Request profile or governed compatible profile | `RC1` |
| `audience_binding` | string | Yes | `present` | `RC0` |
| `nonce_binding` | string | Yes | `present` | `RC0` |
| `lawful_basis_ref` | string | Yes | Echoes accepted exceptional request | `RC1` |
| `jurisdiction_ref` | string | Yes | Echoes accepted exceptional request | `RC1` |
| `purpose` | string | Yes | Echoes accepted exceptional request | `RC1` |
| `retention_period` | object | Yes | Echoes accepted exceptional request | `RC1` |
| `red_path_confirmation` | object | Yes | `shown: true`, `holder_action: approved`, and confirmed field names | `RC1` |
| `disclosed_fields` | object | Yes | Only approved exceptional fields and values | `RC2`; raw root credential material is `RC3` unless explicitly approved |
| `disclosure_scope` | array of strings | Yes | Names of disclosed fields | `RC1` |
| `review_or_appeal_ref` | string | Yes | Echoes accepted exceptional request | `RC1` |
| `audit_event_ref` | string | Optional | Verifier-local or governance audit reference, not holder-specific across verifiers | `RC1` |

An exceptional response MUST NOT claim normal-flow conformance.

An exceptional response MUST NOT include fields beyond the approved `requested_extra_fields`.

### 8.5 Exceptional object JSON Schema fragments
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://minimal-disclosure-age-proof.example/schemas/age-threshold-exception-request-1.0.json",
  "type": "object",
  "additionalProperties": false,
  "required": ["object_type", "object_version", "profile_ref", "verifier_class", "audience", "nonce", "purpose", "policy_ref", "jurisdiction_ref", "exception_requested", "lawful_basis_ref", "requested_extra_fields", "necessity_explanation", "retention_period", "audit_contact", "review_or_appeal_ref", "normal_flow_unavailable_reason"],
  "properties": {
    "object_type": { "const": "age_threshold_exception_request" },
    "object_version": { "type": "string", "pattern": "^[1-9][0-9]*\\.[0-9]+$" },
    "profile_ref": { "type": "string", "minLength": 1 },
    "verifier_class": { "enum": ["V2", "VX"] },
    "requested_threshold": { "type": "string", "pattern": "^over_[0-9]+$" },
    "audience": { "type": "string", "minLength": 1 },
    "nonce": { "type": "string", "minLength": 22 },
    "purpose": { "type": "string", "minLength": 1 },
    "policy_ref": { "type": "string", "minLength": 1 },
    "jurisdiction_ref": { "type": "string", "minLength": 1 },
    "exception_requested": { "const": true },
    "lawful_basis_ref": { "type": "string", "minLength": 1 },
    "requested_extra_fields": { "type": "array", "minItems": 1, "uniqueItems": true, "items": { "enum": ["legal_name", "exact_dob", "document_number", "document_image", "issuer_identity", "root_credential_disclosure", "identity_evidence", "account_linkage_evidence", "other_governed"] } },
    "necessity_explanation": { "type": "string", "minLength": 1 },
    "retention_period": { "$ref": "#/$defs/retention_period" },
    "audit_contact": { "type": "string", "minLength": 1 },
    "review_or_appeal_ref": { "type": "string", "minLength": 1 },
    "normal_flow_unavailable_reason": { "enum": ["governing_rule_requires_extra_data", "normal_proof_failed_governed_step_up", "fraud_or_safety_governed_review", "manual_review_required", "other_governed"] },
    "exception_class_ref": { "type": "string", "minLength": 1 }
  },
  "$defs": {
    "retention_period": {
      "type": "object",
      "additionalProperties": false,
      "required": ["duration", "justification_ref", "disposal_action"],
      "properties": {
        "duration": { "type": "string", "minLength": 1 },
        "justification_ref": { "type": "string", "minLength": 1 },
        "disposal_action": { "enum": ["delete", "anonymise", "return_to_holder", "governed_archive"] }
      }
    }
  }
}
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://minimal-disclosure-age-proof.example/schemas/age-threshold-exception-response-1.0.json",
  "type": "object",
  "additionalProperties": false,
  "required": ["object_type", "object_version", "normal_flow_conformance", "profile_ref", "audience_binding", "nonce_binding", "lawful_basis_ref", "jurisdiction_ref", "purpose", "retention_period", "red_path_confirmation", "disclosed_fields", "disclosure_scope", "review_or_appeal_ref"],
  "properties": {
    "object_type": { "const": "age_threshold_exception_response" },
    "object_version": { "type": "string", "pattern": "^[1-9][0-9]*\\.[0-9]+$" },
    "normal_flow_conformance": { "const": false },
    "profile_ref": { "type": "string", "minLength": 1 },
    "audience_binding": { "const": "present" },
    "nonce_binding": { "const": "present" },
    "lawful_basis_ref": { "type": "string", "minLength": 1 },
    "jurisdiction_ref": { "type": "string", "minLength": 1 },
    "purpose": { "type": "string", "minLength": 1 },
    "retention_period": { "type": "object" },
    "red_path_confirmation": {
      "type": "object",
      "additionalProperties": false,
      "required": ["shown", "holder_action", "confirmed_fields"],
      "properties": {
        "shown": { "const": true },
        "holder_action": { "const": "approved" },
        "confirmed_fields": { "type": "array", "minItems": 1, "uniqueItems": true, "items": { "type": "string", "minLength": 1 } }
      }
    },
    "disclosed_fields": { "type": "object" },
    "disclosure_scope": { "type": "array", "minItems": 1, "uniqueItems": true, "items": { "type": "string", "minLength": 1 } },
    "review_or_appeal_ref": { "type": "string", "minLength": 1 },
    "audit_event_ref": { "type": "string", "minLength": 1 }
  }
}
```

## 9. Conformant examples
### 9.1 Profile R `V1` request using `B0`
```json
{
  "object_type": "age_threshold_request",
  "object_version": "1.0",
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

### 9.2 Profile R `V2` response using `B1`
```json
{
  "object_type": "age_threshold_response",
  "object_version": "1.0",
  "profile_ref": "Profile R",
  "threshold_result": {
    "threshold": "over_18",
    "satisfied": true,
    "result_code": "threshold_satisfied"
  },
  "assurance_bucket": "AB3",
  "issuer_class": "A1",
  "issuer_trust_ref": {
    "trust_framework_ref": "uk-age-trust-framework",
    "trust_resolution_method": "trust_list",
    "trust_list_entry_ref": "non-unique-trust-list-entry",
    "exact_issuer_disclosed": false
  },
  "validity_window": {
    "granularity": "date",
    "valid_from": "2026-04-23",
    "valid_until": "2026-04-24",
    "freshness_requirement_satisfied": true
  },
  "audience_binding": "present",
  "nonce_binding": "present",
  "binding_mode": "B1",
  "possession_proof": "fresh-verifier-scoped-transcript",
  "status_evidence": {
    "status_check_type": "cacheable_status",
    "status_ref": "cached-root-state-list",
    "freshness_bucket": "2026-04-23",
    "live_issuer_callback_allowed": false
  },
  "proof_format_ref": {
    "proof_family": "openid4vp",
    "profile_id": "openid4vp-derived-proof-profile",
    "profile_version": "1.0",
    "correlation_scope": "verifier_scoped"
  }
}
```

### 9.3 Profile P response using `B2`
```json
{
  "object_type": "age_threshold_response",
  "object_version": "1.0",
  "profile_ref": "Profile P",
  "threshold_result": {
    "threshold": "over_18",
    "satisfied": true,
    "result_code": "threshold_satisfied"
  },
  "assurance_bucket": "AB2",
  "issuer_class": "A2",
  "issuer_trust_ref": {
    "trust_framework_ref": "privacy-preserving-trust-framework",
    "trust_resolution_method": "cryptographic_accumulator",
    "trust_list_entry_ref": "non-unique-accumulator-state",
    "exact_issuer_disclosed": false
  },
  "validity_window": {
    "granularity": "date",
    "valid_until": "2026-04-24",
    "freshness_requirement_satisfied": true
  },
  "audience_binding": "present",
  "nonce_binding": "present",
  "binding_mode": "B2",
  "possession_proof": "unlinkable-possession-proof",
  "status_evidence": {
    "status_check_type": "none",
    "live_issuer_callback_allowed": false
  },
  "proof_format_ref": {
    "proof_family": "zk_profile",
    "profile_id": "unlinkable-derived-proof-profile",
    "profile_version": "1.0",
    "correlation_scope": "none"
  }
}
```

### 9.4 Wallet refusal for forbidden normal-flow field
```json
{
  "object_type": "wallet_refusal",
  "object_version": "1.0",
  "refusal_context": "normal_request",
  "refusal_code": "forbidden_field_requested",
  "retryable": false,
  "policy_ref": "minimal-disclosure-normal-flow",
  "refusal_reason_public": "The request asks for data that is not permitted in normal flow.",
  "audience_binding": "present",
  "nonce_binding": "present"
}
```

### 9.5 Exceptional request
```json
{
  "object_type": "age_threshold_exception_request",
  "object_version": "1.0",
  "profile_ref": "Profile R",
  "verifier_class": "VX",
  "requested_threshold": "over_18",
  "audience": "https://exceptional-verifier.test",
  "nonce": "fresh-random-exception-nonce",
  "purpose": "manual-regulatory-review",
  "policy_ref": "regulated-service-manual-review",
  "jurisdiction_ref": "GB",
  "exception_requested": true,
  "lawful_basis_ref": "gb-regulated-review-basis",
  "requested_extra_fields": ["legal_name", "exact_dob"],
  "necessity_explanation": "Normal threshold proof cannot satisfy this governed manual review.",
  "retention_period": {
    "duration": "P30D",
    "justification_ref": "regulated-service-retention-rule",
    "disposal_action": "delete"
  },
  "audit_contact": "mailto:audit@example-verifier.test",
  "review_or_appeal_ref": "https://example-verifier.test/review",
  "normal_flow_unavailable_reason": "manual_review_required"
}
```

### 9.6 Exceptional response
```json
{
  "object_type": "age_threshold_exception_response",
  "object_version": "1.0",
  "normal_flow_conformance": false,
  "profile_ref": "Profile R",
  "audience_binding": "present",
  "nonce_binding": "present",
  "lawful_basis_ref": "gb-regulated-review-basis",
  "jurisdiction_ref": "GB",
  "purpose": "manual-regulatory-review",
  "retention_period": {
    "duration": "P30D",
    "justification_ref": "regulated-service-retention-rule",
    "disposal_action": "delete"
  },
  "red_path_confirmation": {
    "shown": true,
    "holder_action": "approved",
    "confirmed_fields": ["legal_name", "exact_dob"]
  },
  "disclosed_fields": {
    "legal_name": "Jane Example",
    "exact_dob": "2000-01-01"
  },
  "disclosure_scope": ["legal_name", "exact_dob"],
  "review_or_appeal_ref": "https://example-verifier.test/review"
}
```

## 10. Non-conformant examples
### 10.1 Request for exact DOB
```json
{
  "object_type": "age_threshold_request",
  "object_version": "1.0",
  "requested_threshold": "over_18",
  "requested_extra_fields": ["exact_dob"]
}
```

This request is non-conformant because exact DOB is forbidden in normal flow.

### 10.2 Response with a stable holder identifier
```json
{
  "object_type": "age_threshold_response",
  "object_version": "1.0",
  "threshold_result": {
    "threshold": "over_18",
    "satisfied": true,
    "result_code": "threshold_satisfied"
  },
  "holder_id": "stable-user-123"
}
```

This response is non-conformant because stable verifier-visible holder identifiers are forbidden in normal flow.

### 10.3 Response with a unique status callback URI
```json
{
  "object_type": "age_threshold_response",
  "object_version": "1.0",
  "threshold_result": {
    "threshold": "over_18",
    "satisfied": true,
    "result_code": "threshold_satisfied"
  },
  "status_evidence": {
    "status_check_type": "root_credential_state",
    "status_ref": "https://issuer.example/status/token-specific/abc123",
    "live_issuer_callback_allowed": true
  }
}
```

This response is non-conformant because unique status callback URIs create issuer-visible presentation telemetry.

## 11. Error and refusal conditions
A wallet MUST reject or refuse a normal-flow request if:
- a required request field is missing
- a forbidden request field is present
- the requested binding mode is not permitted for the verifier class or profile
- the requested binding mode is not supported by the wallet and no explicitly permitted alternative can be used
- the verifier attempts to downgrade, upgrade, or substitute a binding mode without a new conformant request
- a `B1` request attempts to force same-verifier continuity for an ineligible verifier class, unrelated purpose, or excessive retention period
- the requested flow would require direct root credential disclosure
- the request exceeds the constraints of the applicable verifier policy

Where a machine-readable refusal is returned, the wallet MUST use the wallet refusal object defined in section 7.

## 12. Profile-specific requirements
### 12.1 Profile R
`Profile R` implementations MUST support `B0` for `V1` and `B1` for `V2`.

`Profile R` implementations MUST NOT permit `B1` pairwise material to become cross-verifier correlation material.

### 12.2 Profile P
`Profile P` implementations MUST use `B2` for normal-flow presentations.

`Profile P` implementations MUST NOT expose verifier-stable proof-binding artifacts in the normal flow.
