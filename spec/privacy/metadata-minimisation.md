# Metadata Minimisation

## Status
Draft

## 1. Purpose
This specification defines the normative anti-correlation rules for supporting metadata in the minimal age-disclosure architecture.

## 2. Controlled metadata classes
This specification applies to:
- assurance references
- issuer references
- timestamps
- policy identifiers
- proof-binding artifacts
- validity windows
- status references

## 3. Core minimisation rule
Supporting metadata MUST be minimised even where direct identity attributes are absent.

An implementation MUST NOT treat the omission of name or DOB as sufficient proof of privacy compliance if supporting metadata remains correlating.

## 4. Assurance metadata rules
Normal-flow assurance metadata MUST use bounded assurance buckets rather than detailed provenance unless the applicable profile and governing policy require more.

The approved assurance bucket taxonomy remains subject to [ADR-0010](../../docs/adr/0010-assurance-bucket-taxonomy-and-request-semantics.md).

## 5. Issuer information rules
Normal-flow issuer disclosure SHOULD use the least specific information compatible with trust validation.

Coarse issuer class SHOULD be the default disclosure.

Exact issuer identity MAY be disclosed only where the applicable trust-resolution rule requires it.

The exact boundary remains subject to [ADR-0007](../../docs/adr/0007-exact-issuer-resolution-for-trust-validation.md).

## 6. Time and validity rules
Fine-grained timestamps MUST be avoided where bounded validity information is sufficient.

Validity granularity and freshness semantics remain subject to [ADR-0011](../../docs/adr/0011-validity-granularity-and-freshness-policy-boundaries.md).

## 7. Proof-binding metadata rules
Proof-binding artifacts MUST NOT be reusable across verifier interactions by default.

Implementations MUST treat reusable verifier-visible proof-binding artifacts as privacy-significant and, unless explicitly governed by a profile-specific tradeoff, non-conformant.

## 8. Status and reference rules
Status references SHOULD be batched or cacheable where possible.

Token-specific unique callback references MUST NOT be the common normal-flow design.

Status and freshness trigger details remain subject to [ADR-0011](../../docs/adr/0011-validity-granularity-and-freshness-policy-boundaries.md).

## 9. Policy identifier rules
Policy identifiers MUST be bounded and SHOULD avoid unnecessary fingerprinting value.

Implementations MUST NOT use policy identifiers to smuggle holder-specific or transaction-specific correlation handles into the normal flow.

## 10. Conformance consequences
Metadata minimisation failures MUST be treated as conformance failures even where direct identity fields are absent.

Profile-specific tightening:
- `Profile R` MUST satisfy the common baseline.
- `Profile P` SHOULD impose stricter anti-correlation controls than `Profile R`.
