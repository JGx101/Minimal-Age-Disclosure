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

## 3. Required exception fields
An exceptional request MUST include:
- `exception_requested`
- `verifier_class`
- `lawful_basis_ref`
- `jurisdiction_ref`
- `purpose`
- `requested_extra_fields`
- `necessity_explanation`
- `retention_period`
- `audit_contact`
- `review_or_appeal_ref`

If any required field is missing, vague, or internally inconsistent, the request MUST be treated as non-conformant.

`requested_extra_fields` MUST be bounded to the minimum data needed for the lawful exceptional purpose.

## 4. Wallet red-path UX
A conformant wallet MUST present exceptional requests as a red-path flow.

The red-path UX MUST show:
- that the request is exceptional
- the verifier identity
- the verifier class
- the extra requested fields
- the lawful basis
- the necessity explanation
- the retention period
- the review or appeal path
- a cancel or refuse option

The wallet MUST NOT render exceptional disclosure as if it were a normal threshold proof.

## 5. Exceptional audit record
An exceptional event MUST produce a bounded audit record containing:
- verifier identity
- verifier class
- lawful basis reference
- jurisdiction reference
- purpose
- requested extra fields
- necessity explanation
- retention period
- time bucket
- wallet red-path confirmation state
- review or appeal reference

The audit record MUST NOT retain raw proof payloads or unnecessary identity evidence by default.

## 6. Abuse thresholds
Exceptional use above `5%` of a verifier's age-check volume in a calendar month MUST trigger governance review.

Exceptional use above `10%` of a verifier's age-check volume in a calendar month MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Repeated review triggers across two consecutive months MUST be treated as a conformance failure unless governance explicitly approves a scoped exception class.

Any missing lawful-basis field MUST be treated as non-conformant regardless of volume.

## 7. Default-use prohibition
No verifier class MAY treat exceptional flow as a default unless that condition is explicitly approved by governance and documented as outside normal-flow conformance.

Absent such approval, exceptional-default behavior MUST be treated as non-conformant.
