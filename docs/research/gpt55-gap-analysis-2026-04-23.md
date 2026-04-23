# GPT-5.5 Gap Analysis and Hardening Review

Date: 2026-04-23
Branch: `gpt55-gap-analysis-hardening`

## Executive summary

The project is in a strong documentation-first shape. The main architecture gaps identified earlier have largely been addressed in prose, ADRs, canonical objects, fixtures, and verifier policy. The remaining risk is less about missing ideas and more about enforcement drift: several privacy-critical rules were still easier to state in prose than to validate mechanically.

This review therefore focused on tightening the parts that prevent future regressions:

- machine-readable schemas now enforce more of the accepted object model;
- response nested objects are no longer generic catch-all objects;
- profile and binding-mode compatibility is enforced in schemas and validator logic;
- the fixture validator now tests positive and negative fixtures rather than only checking conformant examples;
- CI now runs the validator automatically on pull requests and pushes.

## Scope reviewed

Reviewed areas:

- README maturity/status and document map;
- canonical request and response object definitions;
- exported JSON Schemas;
- fixture validator;
- conformance and privacy-negative testing approach;
- automation/CI coverage.

This review did not attempt to implement a production wallet, verifier, issuer, trust registry, or cryptographic proof library. The repository remains documentation-first by design.

## Key findings and fixes

### 1. Schema enforcement lagged behind the normative spec

**Finding:** The normative profile defines detailed request and response structures, but the exported response schema left several nested objects as generic `object` fields. That meant a response could pass schema shape while still hiding privacy-relevant drift inside `issuer_trust_ref`, `validity_window`, `status_evidence`, or `proof_format_ref`.

**Fix applied:** `schemas/age-threshold-response.schema.json` now defines nested schema sections for:

- `threshold_result`;
- `issuer_trust_ref`;
- `validity_window`;
- `status_evidence`;
- `proof_format_ref`.

It also validates threshold/result-code consistency and blocks `B2` responses from declaring `verifier_scoped` correlation.

**Residual risk:** JSON Schema still cannot prove cryptographic unlinkability or semantic non-correlation. That remains a fixture, review, and implementation-profile obligation.

### 2. Request schema needed profile/binding conditionals

**Finding:** The prose and validator already treated Profile P as requiring `B2`, and treated `V1` plus `B1` as non-conformant, but the request schema did not encode those compatibility rules.

**Fix applied:** `schemas/age-threshold-request.schema.json` now enforces:

- `Profile P` requires `B2`;
- `V1` must not request `B1`;
- `B1` requires `V2` or `VX`.

**Residual risk:** Deployment profiles may still need more granular verifier-class rules once real jurisdictional or regulator profiles are mapped.

### 3. Negative fixtures were not being actively failed

**Finding:** The previous validator checked conformant fixtures and ensured negative fixtures carried an expected failure class, but it did not consistently run the object validator against negative fixtures to prove that they actually fail.

**Fix applied:** `tools/validate_fixtures.py` now runs supported negative fixture objects through the relevant validator and fails the test if a negative fixture unexpectedly passes.

**Residual risk:** Scenario-only negative fixtures are still reviewed through coverage and envelope checks rather than full semantic validation. Future work should add explicit scenario validators for exception thresholds, repeated transaction correlation, and recovery scenarios.

### 4. Metadata anti-fingerprinting needed sharper validation

**Finding:** The architecture correctly says that metadata combinations can become practical correlators, but the validator only checked a small set of forbidden marker strings.

**Fix applied:** The validator now adds checks for:

- exact DOB and date-of-birth aliases;
- document and passport-style identifiers;
- stable holder or credential identifiers;
- raw evidence and raw proof transcript leakage;
- fine-grained validity/status buckets;
- B2 responses attempting verifier-scoped correlation.

**Residual risk:** Fingerprinting can still occur through rare but individually allowed values. This needs a future cross-field entropy/fingerprint review fixture that scores combinations, not just individual fields.

### 5. Retention leakage rules needed wider coverage

**Finding:** The retention-record check caught obvious proof leakage, but did not explicitly catch some fields that the normal-flow response says must not be retained by default, such as audience/nonce binding material or stable credential references.

**Fix applied:** Retention validation now checks additional leakage markers including:

- `audience_binding`;
- `nonce_binding`;
- stable holder identifiers;
- stable root credential references.

**Residual risk:** Actual retention enforcement will need implementation tests once there is a verifier prototype.

### 6. Validation was not wired into CI

**Finding:** The repository documented `python tools/validate_fixtures.py`, but there was no CI workflow to prevent regressions from being merged.

**Fix applied:** Added `.github/workflows/validate-fixtures.yml` to compile and run the validator on pull requests and pushes to `main`.

**Residual risk:** The CI is intentionally dependency-free. If JSON Schema semantic validation is later required, add a pinned `jsonschema` dependency or a small schema-validation test matrix.

## Architecture status after this pass

### Strong areas

- Clear thesis: prove threshold facts rather than identity.
- Good separation of root credential and derived proof.
- Good distinction between Profile R and Profile P.
- Good use of ADRs to settle previously vague architecture points.
- Good fixture-backed documentation set for requests, responses, metadata, retention, exceptions, and recovery.
- Good emphasis on verifier obligations, not just wallet cryptography.

### Areas still worth improving next

1. **Cross-field fingerprint scoring:** Add a small fixture validator module that treats combinations like issuer class + proof family + validity bucket + status ref as a fingerprint surface.
2. **OpenID4VP mapping:** Add concrete OpenID4VP request/response mapping examples showing exactly where canonical fields sit and what must be omitted.
3. **Exception scenario validator:** Turn exception governance examples into active machine checks rather than mostly documentation coverage.
4. **Recovery state machine:** Add a state transition table and machine-checkable recovery fixtures for issuer compromise, wallet compromise, status outage, and verifier abuse.
5. **Prototype test harness:** Keep implementation narrow, but create a tiny reference verifier that refuses over-collection, bad binding, bad metadata, and retention leakage.

## Acceptance criteria for this hardening branch

The branch should be considered successful if:

- schemas parse as valid JSON;
- `python -m py_compile tools/validate_fixtures.py` succeeds;
- `python tools/validate_fixtures.py` succeeds;
- conformant fixtures pass;
- non-conformant object fixtures fail for the expected class of reasons;
- CI runs the same validator on pull requests.

## Recommended Codex follow-up prompt

Use this prompt next:

```text
Review the Minimal-Age-Disclosure repository after branch gpt55-gap-analysis-hardening. Do not change the core thesis. Focus on making the accepted architecture more testable.

Tasks:
1. Run python -m py_compile tools/validate_fixtures.py and python tools/validate_fixtures.py.
2. If the validator fails, fix only the minimum inconsistent fixture or validation rule.
3. Add a cross-field metadata fingerprinting validator that scores allowed metadata combinations and flags rare or overly specific combinations.
4. Add active validators for exception_scenario fixtures, especially missing lawful basis, missing normal-path insufficiency, excessive requested fields, and V1 exceptional requests.
5. Add OpenID4VP mapping examples under docs/implementation-mapping/ showing canonical request and response fields, forbidden fields, and retention rules.
6. Update docs/research/gpt55-gap-analysis-2026-04-23.md with what changed and any remaining gaps.
7. Open a small PR with test output in the description.
```
