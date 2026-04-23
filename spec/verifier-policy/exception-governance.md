# Exception Governance

## Status
Draft

## 1. Purpose
This specification defines the governance rules for exceptional higher-disclosure requests.

Exceptional requests are outside normal-flow conformance.

## 2. Core rule
A verifier MUST NOT treat the exceptional path as a silent or routine substitute for the normal minimal-disclosure flow.

## 3. Exceptional request requirements
An exceptional request MUST:
- be explicitly flagged as exceptional
- include a reviewable justification field
- identify the verifier class invoking it
- identify the governing legal or policy basis

## 4. Wallet behavior
A wallet MUST:
- present an explicit red-path warning
- distinguish the exceptional request from the normal flow
- show the additional requested disclosure before consent

## 5. Audit requirements
An exceptional event MUST produce a bounded audit record sufficient for review.

The exact minimum exceptional audit record remains subject to [ADR-0014](../../docs/adr/0014-verifier-audit-record-minimum.md).

## 6. Repeated use and enforcement
Repeated exceptional use MUST trigger review.

The quantitative threshold, review trigger, and enforcement consequence remain subject to [ADR-0015](../../docs/adr/0015-exception-path-abuse-thresholds-and-enforcement.md).

## 7. Default-use prohibition
No verifier class MAY treat exceptional flow as a default unless that condition is explicitly approved by governance and documented as outside normal-flow conformance.

Absent such approval, exceptional-default behavior MUST be treated as non-conformant.
