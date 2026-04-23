# Metadata Minimisation

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines normative anti-fingerprinting rules for supporting metadata in the minimal age-disclosure architecture.

Metadata minimisation is a hard conformance boundary. An implementation MUST NOT treat the omission of name or DOB as sufficient privacy compliance if supporting metadata remains correlating.

## 2. Controlled metadata classes
This specification applies to:
- assurance buckets
- issuer references
- timestamps and validity windows
- policy references
- proof-binding artifacts
- status references
- proof format references
- verifier retention records

## 3. Prohibited correlators
Normal-flow metadata MUST NOT include:
- stable verifier-visible holder identifiers
- stable verifier-visible root credential references
- reusable proof-binding artifacts
- unique token-specific status callback URIs
- holder-specific policy references
- session-specific policy references
- transaction-specific policy references beyond nonce and audience binding
- rare provenance strings that make the holder or issuer interaction unusually identifiable
- exact DOB, legal name, document number, or document image
- raw proof payloads retained by default
- verifier telemetry sufficient to reconstruct holder activity history

## 4. Allowed metadata classes
Normal-flow metadata MAY include only:
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
- public `policy_ref`
- public `jurisdiction_ref`

Each allowed metadata class MUST be minimised to the least specific value compatible with verifier decisioning and trust validation.

## 5. Assurance coarsening
Normal-flow assurance metadata MUST use one of:
- `AB1`: basic age-threshold assurance
- `AB2`: standard governed age-threshold assurance
- `AB3`: high-assurance age-threshold assurance

Assurance metadata MUST NOT disclose:
- exact evidence source
- document type
- document number
- issuing office
- evidence inspection date
- rare issuer-specific provenance strings

Verifier requests MUST use `maximum_assurance_bucket`; they MUST NOT request detailed evidence provenance in the normal flow.

## 6. Issuer coarsening
Normal-flow issuer disclosure MUST default to issuer class:
- `A0`
- `A1`
- `A2`

Exact issuer identity MAY be used for trust validation only when issuer class and `issuer_trust_ref` are insufficient under the decision tree in Section 7.

If exact issuer identity is used for trust validation, the verifier MUST NOT retain it as a default retained identifier unless retention is explicitly justified by verifier compliance rules.

Issuer references MUST NOT be holder-specific or token-specific.

## 7. Issuer trust-resolution decision tree
A verifier MUST resolve issuer trust using the least-specific path that supports the verifier decision.

The verifier MUST apply the following decision tree before requesting, resolving, or retaining exact issuer identity:

1. Validate `issuer_class` against the verifier's permitted issuer classes for the requested threshold, policy, jurisdiction, verifier class, profile, and assurance bucket.
2. Resolve `issuer_trust_ref` against an approved trust registry or trust anchor without adding holder-specific, credential-specific, or presentation-specific information.
3. Accept issuer class plus `issuer_trust_ref` as sufficient when the verifier can confirm all of:
   - the issuer class is eligible for the requested policy and jurisdiction
   - the trust state is acceptable at the required freshness level
   - the issuer class supports the requested assurance bucket
   - the issuer class supports the requested profile and binding mode
   - the reference does not create a rare provenance string under Section 11
4. Resolve exact issuer identity only if at least one of the following is true:
   - the governing public policy requires named-issuer eligibility rather than class eligibility
   - two or more registry entries share the same class and trust reference but have materially different trust states or profile permissions
   - a regulated audit rule requires named-issuer validation for the specific verifier class and policy
   - fraud or compromise handling cannot be completed using issuer class, trust state, and status evidence
5. If exact issuer identity is resolved, record only a bounded reason code by default:
   - `policy_requires_named_issuer`
   - `ambiguous_trust_ref`
   - `regulated_named_issuer_audit`
   - `fraud_or_compromise_resolution`
6. Retain exact issuer identity only under the retention rules in Section 18.

The verifier MUST NOT treat operational convenience, analytics, debugging, support triage, or vendor reporting as sufficient reason to request or retain exact issuer identity.

## 8. Timestamp and validity coarsening
Verifier retention MUST use coarse time buckets by default:
- `V1` retention SHOULD use date-level buckets.
- `V2` and `VX` retention MAY use hour-level buckets where needed for audit or fraud review.

Raw cryptographic timestamps and exact proof-generation times MUST NOT be retained by default.

`validity_window` MAY be verifier-visible where needed to evaluate proof freshness, but it MUST be retained only at the permitted verifier-retention granularity.

Timestamp classes MUST be handled as follows:

| Time source | Verifier-visible use | Default retention rule |
| --- | --- | --- |
| Proof generation time | MAY be present inside cryptographic validation material where needed to validate freshness | MUST NOT be retained raw; retain only the approved `V1`, `V2`, or `VX` bucket |
| Verifier log time | MAY be generated by verifier infrastructure for audit records | MUST be stored only at approved retention granularity unless exceptional retention applies |
| Status epoch time | MAY identify a public batch, cache, relay, issuer-trust-state, root-state, or wallet-compromise-state epoch | MUST be retained as a public epoch label or approved coarse bucket, not as token-specific freshness telemetry |
| Exception audit time | MAY be retained for exceptional-flow audit only | MUST be segregated from normal-flow metadata and retained no more precisely than the governance basis requires |

Implementations MUST NOT combine proof generation time, verifier log time, status epoch time, and exception audit time to reconstruct a holder's activity sequence.

## 9. Policy and jurisdiction reference registry discipline
`policy_ref` MUST identify a public policy, rule, service category, or governance requirement.

`policy_ref` MUST NOT contain:
- holder-specific identifiers
- account identifiers
- session identifiers
- transaction identifiers
- campaign or experiment identifiers that create avoidable fingerprinting

`purpose` MUST be human-reviewable and MUST NOT smuggle correlation handles.

`policy_ref` and `jurisdiction_ref` MUST be drawn from governed registries or controlled public enumerations.

The `policy_ref` registry entry MUST define:
- stable public reference
- human-readable policy or service category
- governing authority or governance source
- permitted verifier classes
- permitted issuer classes
- maximum permitted assurance bucket
- permitted binding modes
- permitted freshness requirements
- registry version or public effective epoch

The `jurisdiction_ref` registry entry MUST define:
- stable public reference
- jurisdiction level, such as country, state, province, union, or governed market
- governing authority or governance source
- permitted policy references
- registry version or public effective epoch

Registry references MUST be coarse enough for repeated use across many holders and verifiers. A registry entry MUST NOT be created for a single verifier campaign, holder cohort, tenant, experiment, session, transaction, or enforcement case unless that entry is explicitly treated as exceptional-flow metadata.

`jurisdiction_ref` SHOULD use widely recognized public codes where they are sufficient. Sub-national, local, or sector-specific values MAY be used only where the governing rule requires them and the value does not become rare under Section 11.

## 10. Status reference minimisation
`status_evidence` MUST be one of:
- `none`
- batched status
- cacheable status
- relayable status
- issuer-trust-state reference
- root-credential-state reference
- wallet-compromise-state reference

Status references MUST NOT require token-specific live issuer callbacks in normal flow.

Status references MUST NOT let an issuer or status service observe ordinary verifier presentations.

## 11. Rare provenance string methodology
A metadata value is a rare provenance string if it materially narrows the holder, issuer interaction, credential issuance path, evidence source, time of issuance, or verification event beyond what is needed for verifier decisioning.

Before a metadata value is allowed in normal flow, the governing profile owner or implementation operator MUST review it against all of the following tests:
- Population test: the value is expected to apply to at least `100` active holders or `0.1%` of the relevant governed population, whichever is greater.
- Issuer-path test: the value does not reveal a single issuing office, enrollment channel, evidence vendor, inspection desk, or unusually narrow issuer workflow.
- Time-path test: the value does not encode a precise issue, inspection, update, or proof-generation time.
- Registry test: the value is present in a governed public registry or controlled enumeration rather than minted per holder, credential, transaction, verifier tenant, or experiment.
- Combination test: the value remains non-identifying when combined with the other allowed fields under Section 12.

If the population or combination evidence is unavailable, the implementation MUST generalize or suppress the value by default.

Examples of rare provenance strings include:
- `passport_scan_vendor_x_liveness_flow_2026_q1`
- `issuer-office-edinburgh-branch-17`
- `manual-review-team-beta`
- `credential-batch-2026-04-23-09-14`
- proof library, build, or parameter labels used by only a small issuer cohort

## 12. Cross-field anti-fingerprinting review
Allowed metadata fields MUST be reviewed as a bundle, not only field by field.

An implementation MUST fail conformance review if individually allowed fields combine into a practical correlator. This includes combinations such as:
- `issuer_class` + `issuer_trust_ref` + `assurance_bucket`
- `policy_ref` + `jurisdiction_ref` + `validity_window`
- `proof_format_ref` + `binding_mode` + `status_evidence`
- proof generation time + verifier log time + status epoch time
- `V2` or `VX` verifier class + rare policy or jurisdiction references

The default review method is:
1. List every verifier-visible field, retained field, registry-resolved field, and derived telemetry field.
2. Mark each field as `constant`, `coarse`, `bounded`, `rare`, or `unique`.
3. Reject any `unique` normal-flow value.
4. Generalize or suppress any `rare` normal-flow value unless explicit governance approves it as exceptional-flow metadata.
5. Estimate the smallest plausible anonymity set created by the full metadata bundle.
6. Treat the bundle as non-conformant if the anonymity set is below:
   - `1000` holders or presentations for the common baseline and `Profile R`
   - `10000` holders or presentations for `Profile P`
7. Repeat the review for same-verifier repetition and cross-verifier repetition.

Where quantitative population evidence is unavailable, reviewers MUST use conservative classification and reduce metadata precision until the bundle is no longer a practical correlator.

## 13. Anti-fingerprinting budget
Each normal-flow metadata bundle MUST stay within an anti-fingerprinting budget.

The default budget is:

| Field classification | Budget cost |
| --- | --- |
| `constant` across the governed profile | `0` |
| `coarse` public category with large reuse | `1` |
| `bounded` registry value with documented reuse | `2` |
| `rare` value | `5` and review required |
| `unique` or token-specific value | non-conformant |

The maximum normal-flow budget is:
- `6` for `V1`
- `7` for `V2` and `Profile R` high-assurance flows
- `4` for `Profile P`

`VX` exceptional flows MUST be reviewed outside the normal-flow budget and MUST document why the exception governance basis permits any additional metadata.

Budget scoring MUST include cross-field effects. If two fields are harmless alone but rare together, the combination MUST be scored as `rare`.

## 14. Binding metadata minimisation
`B0` possession evidence MUST be transaction-bound and MUST NOT expose additional verifier-visible holder handles.

`B1` possession evidence MUST be verifier-scoped and fresh per transaction. Any verifier-scoped continuity material MUST be treated as privacy-sensitive and MUST NOT be retained as default telemetry.

`B2` possession evidence MUST be unlinkable and MUST NOT expose verifier-stable holder handles.

## 14.1 Repeated-transaction fingerprinting evidence
Conformance review MUST include repeated-transaction analysis for the same verifier and for different verifier audiences.

The review MUST compare at least:
- request objects
- response objects
- proof-format references
- status evidence
- issuer trust references
- policy and jurisdiction references
- validity windows
- verifier retention records
- `B1` continuity material where present

Repeated-transaction tests MUST fail if they find any normal-flow value that is stable because it identifies the holder, root credential, wallet instance, proof-binding artifact, unique status reference, rare proof-format value, precise timestamp, or holder-specific policy context.

For `B1`, same-verifier and same-purpose continuity MAY be present only under the `B1` retention rule. Cross-verifier comparison MUST show that the continuity material cannot be reused across verifier audiences.

For `B2`, same-verifier and cross-verifier comparison MUST show no verifier-stable holder handle, no pairwise pseudonym, and no reusable proof-binding artifact.

## 15. Conformant metadata bundles
The following examples are conformant metadata bundles. They are examples of metadata shape, not mandatory literal values.

### 15.1 `V1` common normal-flow bundle
```json
{
  "verifier_class": "V1",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB2",
  "issuer_class": "A1",
  "issuer_trust_ref": "registry:issuer-class/A1:2026-04",
  "validity_window": "valid_on:2026-04-23",
  "binding_mode": "B0",
  "status_evidence": "issuer_trust_state:2026-04",
  "proof_format_ref": "derived-proof-family:v1",
  "policy_ref": "policy:age-gated-access:2026-04",
  "jurisdiction_ref": "jurisdiction:GB",
  "retained_time_bucket": "2026-04-23"
}
```

### 15.2 `V2` high-assurance normal-flow bundle
```json
{
  "verifier_class": "V2",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB3",
  "issuer_class": "A1",
  "issuer_trust_ref": "registry:issuer-class/A1-high:2026-04",
  "validity_window": "valid_on:2026-04-23",
  "binding_mode": "B1",
  "status_evidence": "cached-root-state-list:2026-04-23T10Z",
  "proof_format_ref": "openid4vp-derived-proof:major-v1",
  "policy_ref": "policy:regulated-age-check:2026-04",
  "jurisdiction_ref": "jurisdiction:GB",
  "retained_time_bucket": "2026-04-23T10Z",
  "issuer_resolution_reason": "class_and_trust_ref_sufficient"
}
```

### 15.3 `VX` exceptional metadata bundle
```json
{
  "verifier_class": "VX",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB3",
  "issuer_class": "A0",
  "issuer_trust_ref": "registry:authoritative-issuer-class:2026-04",
  "validity_window": "valid_on:2026-04-23",
  "binding_mode": "B1",
  "status_evidence": "relayable-wallet-compromise-state:2026-04-23T10Z",
  "proof_format_ref": "derived-proof-family:v1",
  "policy_ref": "policy:exception-governed-age-check:2026-04",
  "jurisdiction_ref": "jurisdiction:GB",
  "retained_time_bucket": "2026-04-23T10Z",
  "exception_audit_time_bucket": "2026-04-23T10Z",
  "exception_reason_code": "regulated_named_issuer_audit"
}
```

The `VX` bundle is conformant only as an exceptional-flow record governed by exception policy. It is not a normal-flow metadata bundle.

### 15.4 `Profile R` conformant bundle
```json
{
  "profile_ref": "Profile R",
  "verifier_class": "V2",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB3",
  "issuer_class": "A1",
  "issuer_trust_ref": "registry:profile-r/A1-high:2026-04",
  "validity_window": "valid_on:2026-04-23",
  "binding_mode": "B1",
  "status_evidence": "batched-root-state:2026-04-23T10Z",
  "proof_format_ref": "profile-r-derived-proof:major-v1",
  "policy_ref": "policy:regulated-age-check:2026-04",
  "jurisdiction_ref": "jurisdiction:GB",
  "retained_time_bucket": "2026-04-23T10Z"
}
```

### 15.5 `Profile P` conformant bundle
```json
{
  "profile_ref": "Profile P",
  "verifier_class": "V1",
  "threshold_result": "over_18:true",
  "assurance_bucket": "AB2",
  "issuer_class": "A2",
  "issuer_trust_ref": "registry:profile-p/privacy-preserving-trust-set:2026-04",
  "validity_window": "valid_on:2026-04-23",
  "binding_mode": "B2",
  "status_evidence": "none",
  "proof_format_ref": "profile-p-unlinkable-proof:major-v1",
  "policy_ref": "policy:age-gated-access:2026-04",
  "jurisdiction_ref": "jurisdiction:GB",
  "retained_time_bucket": "2026-04-23"
}
```

## 16. Non-conformant cross-field examples
The following bundles are non-conformant even if each field appears to use an allowed class:

```json
{
  "issuer_class": "A1",
  "issuer_trust_ref": "registry:issuer-office-edinburgh-branch-17",
  "assurance_bucket": "AB3",
  "policy_ref": "policy:age-check-beta-campaign-42",
  "jurisdiction_ref": "jurisdiction:GB-SCT-local-district-rare",
  "status_evidence": "cached-root-state-list:2026-04-23T09:14Z",
  "proof_format_ref": "derived-proof-lib-build-7.3.19-smallpilot"
}
```

This bundle is non-conformant because issuer path, policy reference, local jurisdiction, status epoch, and proof format combine into a rare provenance string.

## 17. Metadata-driven conformance failures
An implementation MUST be treated as non-conformant if:
- allowed metadata is more granular than required for the verifier decision
- metadata permits cross-verifier correlation in normal flow
- proof-binding artifacts are reusable beyond the selected binding mode
- status references create presentation logs
- policy references contain hidden holder, session, or transaction identifiers
- verifier retention reconstructs holder activity history
- exact issuer identity is retained by default without governance justification
- issuer class, issuer trust, policy, jurisdiction, status, timestamp, and proof format fields are safe alone but identifying in combination
- the anti-fingerprinting budget is exceeded without exceptional-flow governance

## 18. Explicit retention rules for metadata references
Default verifier retention MUST follow these rules:

| Field | Default retention rule |
| --- | --- |
| `issuer_trust_ref` | MAY retain only a coarse registry reference, public trust-set reference, or reason code needed to justify acceptance. MUST NOT retain token-specific, holder-specific, credential-specific, or exact issuer-resolved values by default. |
| `proof_format_ref` | MAY retain only proof family, governed profile, or major version. MUST NOT retain library build, implementation vendor, parameter set, or experimental profile values if they are rare under Section 11. |
| `status_evidence` | MAY retain only status class and public batch, cache, relay, or trust-state epoch. MUST NOT retain unique status callback URIs, raw status responses, issuer-visible query artifacts, or token-specific freshness checks. |

Retention periods for these fields MUST be no longer than the verifier's approved decision-record retention period unless exceptional governance applies.

Resolved trust-registry lookups and status checks MUST be cached or logged in a way that does not create issuer-visible presentation histories or verifier-held holder histories.

## 19. Profile-specific tightening
`Profile R` MUST satisfy the common metadata baseline and MUST treat `B1` continuity material as privacy-sensitive.

`Profile R` MUST run the cross-field review in Section 12 for both `B0` `V1` flows and `B1` `V2` flows.

`Profile P` MUST satisfy the common metadata baseline, MUST stay within the lower anti-fingerprinting budget in Section 13, and MUST treat verifier-stable binding metadata as non-conformant in normal flow.
