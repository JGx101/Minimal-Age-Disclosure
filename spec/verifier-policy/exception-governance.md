# Exception Governance

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines the governance rules for exceptional higher-disclosure requests.

Exceptional requests are outside normal-flow conformance. They MUST NOT be treated as a silent or routine substitute for the normal minimal-disclosure flow.

## 2. Verifier-class eligibility
`V1` verifiers MUST NOT invoke exceptional disclosure.

`V2` verifiers MAY request step-up only where:
- the normal flow cannot satisfy the governing rule
- the step-up remains bounded
- the request is auditable
- the wallet shows red-path UX

`VX` verifiers MAY request exceptional higher disclosure only with explicit lawful-basis fields and governance oversight.

Any `V1` exception request MUST be treated as non-conformant.

### 2.1 Eligibility matrix
Exceptional disclosure eligibility MUST be evaluated by verifier class, jurisdiction context, and use case before a request is sent to a wallet.

| Verifier class | Jurisdiction context | Use case class | Eligibility | Maximum exceptional pattern |
| --- | --- | --- | --- | --- |
| `V1` | Any | Any | Not eligible | None |
| `V2` | Jurisdiction with a documented governing age or access rule | One-off step-up where threshold proof, assurance bucket, binding mode, and freshness evidence cannot satisfy the governing rule | Eligible only after the normal-path insufficiency test passes | Bounded one-off step-up |
| `V2` | Jurisdiction with no documented governing rule | Commercial preference, analytics, account enrichment, or operational convenience | Not eligible | None |
| `V2` | Any | Repeated or default higher-disclosure journey for the same service | Not eligible as normal-flow conformance; MUST be treated as exception-by-design | Governance review and likely non-conformance |
| `VX` | Jurisdiction with explicit statutory, regulatory, legal-process, safety, or dispute-handling basis | Higher-disclosure use case requiring governance oversight | Eligible only with lawful-basis fields, reviewer approval, and audit controls | Scoped governed exception class |
| `VX` | Jurisdiction with no explicit lawful basis | Commercial preference, analytics, account enrichment, or operational convenience | Not eligible | None |

The matrix is closed by default. A verifier MUST NOT infer eligibility from omission. New eligible combinations require governance approval and a published policy update.

### 2.2 One-off step-up vs exception-by-design
A one-off step-up is an exceptional request tied to a specific transaction, policy event, investigation, dispute, safety risk, or governing-rule requirement.

An exception-by-design service is a service design in which exceptional disclosure is required for ordinary access, used as the default path, preselected for most users, or expected to recur for the same service without a new governing-rule insufficiency finding.

Exception-by-design behavior MUST be treated as non-conformant unless governance explicitly records the service as outside normal-flow conformance. Governance approval of an outside-conformance service MUST NOT make that service conformant to the normal minimal-disclosure profile.

## 3. Lawful-basis controlled vocabulary
An exceptional request MUST include a structured `lawful_basis_code` and a more specific `lawful_basis_ref`.

`lawful_basis_code` MUST be one of:
- `statutory_age_or_access_rule`
- `regulator_mandated_step_up`
- `legal_claim_or_dispute`
- `fraud_or_security_investigation`
- `holder_requested_support`
- `safety_emergency`
- `legal_process_or_court_order`
- `governance_approved_research_or_audit`

`lawful_basis_ref` MUST identify the concrete rule, policy, case, ticket, order, regulator notice, governance decision, or other controlled reference that supports the selected code.

The following values MUST NOT be accepted as a lawful-basis code or equivalent free text:
- `business_preference`
- `conversion_optimization`
- `analytics`
- `personalization`
- `account_enrichment`
- `fraud_prevention_general`
- `terms_of_service_only`

`fraud_prevention_general` and `terms_of_service_only` are insufficient because they do not establish that higher disclosure is necessary for the specific transaction.

## 4. Normal-path insufficiency test
Before invoking exceptional disclosure, the verifier MUST document that the normal path cannot satisfy the governing rule.

The normal path is insufficient only if all of the following are true:
- the governing rule or approved governance decision requires a decision element that cannot be represented by a supported threshold claim, assurance bucket, binding mode, freshness requirement, issuer trust reference, or normal-flow refusal result
- no lower-disclosure normal-flow variant can satisfy the same governing rule
- each requested extra field is necessary for the exceptional decision and is mapped to the governing rule
- the request is bounded to a single transaction, case, review, or approved exception class
- the expected retention period is no longer than the exceptional purpose requires
- the verifier records the insufficiency finding in the audit record before requesting the extra fields

The normal path MUST NOT be treated as insufficient merely because it is less convenient, produces lower conversion, requires verifier-side policy work, lacks analytics value, or does not enrich an account profile.

## 5. Exception request object
An exceptional request object is outside the normal-flow request object defined by the age-threshold proof profile.

An exceptional request MUST contain:
- `object_type`
- `exception_requested`
- `base_request_ref`
- `verifier_id`
- `verifier_class`
- `jurisdiction_ref`
- `use_case_code`
- `lawful_basis_code`
- `lawful_basis_ref`
- `purpose`
- `requested_extra_fields`
- `field_necessity_map`
- `normal_path_insufficiency`
- `retention_period`
- `evidence_handling`
- `audit_contact`
- `review_or_appeal_ref`
- `request_expiry`
- `nonce`

`object_type` MUST be `age_exception_request`.

`exception_requested` MUST be `true`.

`base_request_ref` MUST bind the exceptional request to the normal-flow request, transaction, policy decision, or refusal that led to the exceptional path. It MUST NOT be a stable holder identifier.

`use_case_code` MUST identify the approved use case class, such as `one_off_step_up`, `dispute_resolution`, `safety_review`, `legal_process`, `fraud_case_review`, or `governance_audit`.

`field_necessity_map` MUST map each requested extra field to the governing rule and lawful-basis reference that requires it.

`normal_path_insufficiency` MUST contain a structured result of the test in Section 4.

`evidence_handling` MUST declare whether extra fields are transiently inspected, retained as exceptional evidence, redacted before retention, or refused.

Example:

```json
{
  "object_type": "age_exception_request",
  "exception_requested": true,
  "base_request_ref": "normal-request-nonce-or-case-ref",
  "verifier_id": "https://regulated-verifier.example",
  "verifier_class": "V2",
  "jurisdiction_ref": "GB",
  "use_case_code": "one_off_step_up",
  "lawful_basis_code": "regulator_mandated_step_up",
  "lawful_basis_ref": "policy-rule-or-governance-decision-ref",
  "purpose": "resolve documented age-gate dispute",
  "requested_extra_fields": ["birth_year"],
  "field_necessity_map": {
    "birth_year": "required by lawful_basis_ref where threshold result alone cannot resolve dispute"
  },
  "normal_path_insufficiency": {
    "result": true,
    "reason": "threshold proof cannot satisfy the documented dispute rule",
    "lower_disclosure_alternatives_checked": ["over_18", "AB3", "wallet_compromise_state"]
  },
  "retention_period": "P30D",
  "evidence_handling": "retain_redacted_exception_record",
  "audit_contact": "privacy-office@example",
  "review_or_appeal_ref": "https://regulated-verifier.example/appeal",
  "request_expiry": "bounded",
  "nonce": "fresh-exception-nonce"
}
```

If a field value is holder-specific beyond what is required to bind the transaction, it MUST be treated as non-conformant.

## 6. Exception response object
A wallet that permits exceptional disclosure MUST return a bounded exceptional response object.

An exceptional response MUST contain:
- `object_type`
- `exception_response`
- `base_request_ref`
- `verifier_id`
- `jurisdiction_ref`
- `lawful_basis_code`
- `lawful_basis_ref`
- `disclosed_fields`
- `withheld_fields`
- `holder_decision`
- `red_path_confirmation`
- `retention_notice_acknowledged`
- `nonce_binding`
- `response_expiry`

`object_type` MUST be `age_exception_response`.

`holder_decision` MUST be one of:
- `accepted_all`
- `accepted_partial`
- `refused`
- `cancelled`

`disclosed_fields` MUST contain only the extra fields the holder accepted and the wallet released.

`withheld_fields` MUST list fields refused, unavailable, or blocked by wallet policy. It MUST NOT disclose the values of withheld fields.

`red_path_confirmation` MUST record that the exceptional UX was shown and whether holder confirmation was obtained.

If `holder_decision` is `accepted_partial`, the verifier MUST decide using only the disclosed fields or return an exceptional insufficiency result. The verifier MUST NOT silently retry, degrade UX, or coerce disclosure of withheld fields.

If `holder_decision` is `refused` or `cancelled`, the wallet MUST return no extra evidence values. A verifier MAY provide a non-digital or appeal path where required by the governing rule.

Example:

```json
{
  "object_type": "age_exception_response",
  "exception_response": true,
  "base_request_ref": "normal-request-nonce-or-case-ref",
  "verifier_id": "https://regulated-verifier.example",
  "jurisdiction_ref": "GB",
  "lawful_basis_code": "regulator_mandated_step_up",
  "lawful_basis_ref": "policy-rule-or-governance-decision-ref",
  "disclosed_fields": {
    "birth_year": "2005"
  },
  "withheld_fields": [],
  "holder_decision": "accepted_all",
  "red_path_confirmation": "shown_and_confirmed",
  "retention_notice_acknowledged": true,
  "nonce_binding": "present",
  "response_expiry": "bounded"
}
```

## 7. Required exception fields
An exceptional request MUST include:
- `exception_requested`
- `verifier_id`
- `verifier_class`
- `lawful_basis_code`
- `lawful_basis_ref`
- `jurisdiction_ref`
- `use_case_code`
- `purpose`
- `requested_extra_fields`
- `field_necessity_map`
- `normal_path_insufficiency`
- `retention_period`
- `evidence_handling`
- `audit_contact`
- `review_or_appeal_ref`

If any required field is missing, vague, or internally inconsistent, the request MUST be treated as non-conformant.

`requested_extra_fields` MUST be bounded to the minimum data needed for the lawful exceptional purpose.

## 8. Wallet red-path UX
A conformant wallet MUST present exceptional requests as a red-path flow.

The red-path UX MUST show:
- that the request is exceptional
- the verifier identity
- the verifier class
- the extra requested fields
- the lawful basis
- the normal-path insufficiency explanation
- the retention period
- the review or appeal path
- a cancel or refuse option

The wallet MUST NOT render exceptional disclosure as if it were a normal threshold proof.

### 8.1 Partial consent and refusal
A conformant wallet MUST allow the holder to refuse the exceptional request.

A conformant wallet SHOULD allow field-level consent where the request contains more than one extra field, unless field-level consent would make the governing rule misleading or impossible to evaluate. If field-level consent is unavailable, the wallet MUST show that the request is all-or-nothing before confirmation.

For partial consent, the wallet MUST:
- disclose only the accepted fields
- mark refused fields as withheld without revealing their values
- bind the response to the exceptional request nonce
- prevent the verifier from treating withheld fields as silently accepted

For refusal or cancellation, the wallet MUST:
- disclose no exceptional evidence values
- return only a refusal or cancellation status where protocol response is required
- preserve the holder's ability to use a review or appeal path where one is required

## 9. Exceptional audit record
An exceptional event MUST produce a bounded audit record containing:
- verifier identity
- verifier class
- use case code
- lawful basis code
- lawful basis reference
- jurisdiction reference
- purpose
- requested extra fields
- field necessity map
- normal-path insufficiency result
- retention period
- evidence-handling mode
- time bucket
- wallet red-path confirmation state
- holder decision state
- review or appeal reference

The audit record MUST NOT retain raw proof payloads or unnecessary identity evidence by default.

## 10. Audit escalation workflow
Governance MUST maintain an escalation workflow for exceptional-path review.

The review trigger MUST include at least:
- exception volume above the `5%` monthly review threshold
- exception volume above the `10%` monthly conformance-failure threshold
- repeated review triggers across two consecutive months
- any `V1` exception request
- any missing, vague, or inconsistent lawful-basis field
- any request failing the normal-path insufficiency test
- any use of exceptional disclosure as a default service design
- any retention of extra evidence outside the declared evidence-handling mode

The reviewer MUST be independent of the product or operations team requesting the exception. Acceptable reviewers include a governance board, privacy office, compliance function, trust-framework operator, or other approved independent reviewer.

The outcome MUST be one of:
- `approved_scoped_exception`
- `approved_with_conditions`
- `rejected_non_conformant`
- `temporary_non_conformance`
- `trust_withdrawal_recommended`

The remediation record MUST include:
- cause
- affected verifier, jurisdiction, and use case
- required correction
- owner
- deadline
- evidence required for closure
- follow-up review date

## 11. Sanctions ladder
Governance MUST apply a sanctions ladder for exceptional-path misuse.

| Condition | Minimum sanction |
| --- | --- |
| First minor documentation defect with no over-disclosure | Warning and correction deadline |
| Missing field, weak field-necessity map, or first `5%` review trigger | Formal review and remediation plan |
| Repeated documentation defect, failed normal-path insufficiency test, or unauthorized retention of extra evidence | Temporary non-conformance |
| Above `10%` exceptional use without scoped approval, repeated `5%` triggers across two consecutive months, `V1` exception use, or exception-by-design service presented as conformant | Temporary non-conformance and trust withdrawal recommendation |
| Deliberate concealment, repeated unauthorized exceptional disclosure, or refusal to remediate | Trust withdrawal recommendation |

Warnings MUST be time-bounded. A warning that is not remediated by its deadline MUST escalate to formal review.

## 12. Abuse thresholds
Exceptional use above `5%` of a verifier's age-check volume in a calendar month MUST trigger governance review.

Exceptional use above `10%` of a verifier's age-check volume in a calendar month MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Repeated review triggers across two consecutive months MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Any missing lawful-basis field MUST be treated as non-conformant regardless of volume.

### 12.1 Threshold calculation
Governance MUST calculate exception thresholds from monthly verifier age-check volume.

The denominator MUST include all age-check transactions for the verifier in the calendar month, including accepted normal-flow checks, refused normal-flow checks, failed normal-flow checks, exceptional checks, and exceptional refusals.

The numerator MUST include all exceptional requests sent or attempted by that verifier during the same calendar month, including requests refused by the wallet and requests later withdrawn by the verifier.

The monthly exception rate MUST be calculated as:

```text
monthly_exception_rate = exceptional_request_count / total_age_check_transaction_count
```

If the denominator is too small for a stable percentage, governance MUST still review any pattern suggesting default exceptional use, repeated missing lawful-basis fields, or `V1` exception attempts.

### 12.2 Scoped exception approval
A scoped exception class MAY be approved only by an independent reviewer such as a governance board, privacy office, compliance function, trust-framework operator, or approved certifier.

The approval evidence package MUST include:
- verifier identity and verifier class
- jurisdiction and policy context
- use case code
- lawful-basis code and reference
- normal-path insufficiency evidence
- requested extra fields and field-necessity map
- evidence-handling mode
- retention period and disposal action
- expected monthly exception volume and percentage
- red-path UX text or equivalent holder-facing disclosure
- audit contact and review or appeal reference
- expiry date and re-review date

A scoped exception approval MUST expire no later than `12` months after approval unless the governing authority requires a shorter period.

Renewal MUST require re-review. Prior approval MUST NOT automatically renew the exception class.

Scoped approval MAY prevent the `10%` threshold from being an immediate conformance failure only for the approved verifier, jurisdiction, use case, requested fields, and expiry period. It MUST NOT make the exceptional path part of normal-flow conformance.

## 13. Exception evidence handling and retention
Extra fields collected during an exceptional flow MUST be handled under the declared `evidence_handling` mode.

`evidence_handling` MUST be one of:
- `transient_inspection_only`
- `retain_redacted_exception_record`
- `retain_declared_extra_fields`
- `refused_no_extra_evidence`

For `transient_inspection_only`, the verifier MAY inspect the extra field for the exceptional decision but MUST NOT retain the raw value after the transaction decision is complete.

For `retain_redacted_exception_record`, the verifier MAY retain the exceptional audit record and redacted evidence sufficient to justify the decision, but MUST NOT retain raw extra field values.

For `retain_declared_extra_fields`, the verifier MAY retain only the specifically declared extra fields, only for the declared retention period, and only where the lawful-basis reference requires raw evidence retention.

For `refused_no_extra_evidence`, the verifier MUST NOT retain exceptional evidence values because none were disclosed.

Exceptional evidence MUST NOT be copied into default verifier telemetry, analytics, product logs, fraud feature stores, model-training datasets, or account profile enrichment. Any secondary use requires a separate governed exceptional request or an explicit governance decision.

### 13.1 Relationship to verifier retention
Exception governance narrows, and does not replace, the verifier retention specification.

| Record or evidence type | Default verifier retention rule | Exceptional governance rule |
| --- | --- | --- |
| Decision outcome, coarse time bucket, policy reference, verifier class, binding mode, exception flag | May be retained by default | May be retained as part of the audit record |
| Raw proof payload or raw proof transcript | Forbidden by default | Still forbidden unless explicitly required by a scoped governance decision; raw proof retention SHOULD NOT be approved for ordinary exception flows |
| Extra fields disclosed in exception flow | Not part of default retention | Retain only under the declared `evidence_handling` mode and retention period |
| `B1` continuity material | Not retained as default telemetry | Retain only if separately justified under the `B1` retention rule and not merely because an exception occurred |
| Fine-grained timestamps or activity telemetry | Forbidden where it reconstructs holder activity | Still forbidden unless the approved audit scope requires it; approval MUST be time-limited and access-controlled |

## 14. Default-use prohibition
No verifier class MAY treat exceptional flow as a default unless that condition is explicitly approved by governance and documented as outside normal-flow conformance.

Absent such approval, exceptional-default behavior MUST be treated as non-conformant.
