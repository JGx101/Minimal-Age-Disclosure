# Open Question Closure Log

## Status
Complete for the current documentation-first phase.

This log records how each question from `OPEN_QUESTIONS.md` was closed. Each closure is represented as a normative spec update, conformance rule, fixture, policy rule, prototype acceptance criterion, or backlog item.

## Closure table
| ID | Original question | Closure decision | Primary artifacts |
| --- | --- | --- | --- |
| Q1 | Which standards proof family should the first `Profile P` prototype instantiate for the `B2` mechanism pattern? | The first `Profile P` prototype SHOULD use a BBS-style or equivalent unlinkable selective-disclosure proof-family pattern. The architecture remains library-agnostic. | `spec/root-derived-proof/root-vs-derived-proof-model.md`; `spec/claim-profile/age-threshold-proof-profile.md`; `fixtures/responses/profile-p-b2-response.json`; `BACKLOG.md` |
| Q2 | Which mainstream `Profile R` rails can best carry the canonical request and response objects without weakening metadata rules? | `Profile R` SHOULD use OpenID4VCI for issuance and OpenID4VP for presentation. Canonical objects MAY be carried as profile-constrained claims, presentation metadata, or governed envelopes only where all field and metadata rules are preserved. | `spec/claim-profile/age-threshold-proof-profile.md`; `spec/root-derived-proof/root-vs-derived-proof-model.md`; `fixtures/requests/profile-r-v1-b0-request.json`; `fixtures/requests/profile-r-v2-b1-request.json` |
| Q3 | What automated evidence is sufficient to prove that a chosen `B1` implementation keeps continuity material same-verifier and same-purpose scoped? | `B1` evidence MUST include same-verifier/same-purpose continuity checks, cross-verifier non-reuse checks, purpose-separation checks, and retained-record inspection. | `spec/root-derived-proof/root-vs-derived-proof-model.md`; `spec/conformance/conformance-checklist.md`; `fixtures/conformance/repeated-transaction-b1-same-verifier.json`; `fixtures/conformance/repeated-transaction-cross-verifier.json` |
| Q4 | Which privacy-negative tests can be automated first without implementing a full wallet? | Fixture-backed checks now cover request shape, response shape, metadata fingerprinting, over-retention, reusable binding artifacts, exception governance, and recovery privacy. | `spec/conformance/privacy-negative-test-cases.md`; `spec/conformance/conformance-checklist.md`; `fixtures/` |
| Q5 | How should repeated-transaction tests generate evidence for metadata fingerprinting? | Repeated-transaction analysis MUST compare request objects, response objects, proof-format references, status evidence, issuer trust references, policy references, validity windows, retention records, and `B1` continuity material where present. | `spec/privacy/metadata-minimisation.md`; `fixtures/conformance/repeated-transaction-b1-same-verifier.json`; `fixtures/conformance/repeated-transaction-cross-verifier.json` |
| Q6 | What fixture format should represent conformant and non-conformant request/response examples? | JSON fixtures MUST use a stable envelope with `fixture_id`, `kind`, `profile_ref`, `expected_conformance`, `expected_failure_class`, and `object` or `scenario`. | `spec/claim-profile/age-threshold-proof-profile.md`; `fixtures/README.md`; `fixtures/requests/`; `fixtures/responses/`; `fixtures/conformance/` |
| Q7 | How should the `5%` review threshold and `10%` exception failure threshold be validated in real governance settings? | Thresholds are calculated from monthly verifier age-check volume: exceptional request count divided by total age-check transaction count. | `spec/verifier-policy/exception-governance.md`; `fixtures/conformance/exception-thresholds-monthly.json` |
| Q8 | Which UK and EU policy sources should be cited for verifier-class eligibility and exception governance? | Policy mapping MUST cite source categories for UK DVS-style trust framework material, ICO, Ofcom, eIDAS/EUDI, EU age-verification blueprint material, data protection authorities, and relevant standards. It MUST NOT claim approval. | `docs/policy/policy-pack-outline.md`; `BACKLOG.md` |
| Q9 | What review process should approve a scoped exception class without weakening normal-flow conformance? | Scoped exception approval requires an independent reviewer, evidence package, expiry, re-review, and bounded approval. It remains outside normal-flow conformance. | `spec/verifier-policy/exception-governance.md`; `fixtures/conformance/exception-thresholds-monthly.json` |
| Q10 | What is the minimum mock issuer, wallet, verifier, and trust registry needed to demonstrate the accepted architecture? | The minimum prototype roles are mock issuer, wallet simulator, verifier demo, trust-registry mock, status relay mock, and governance/audit mock. | `prototype/implementation-plan.md`; `fixtures/README.md` |
| Q11 | Which recovery and compromise scenarios should be simulated first? | First scenarios are lost device unconfirmed, confirmed compromised wallet, and issuer trust withdrawal. | `prototype/implementation-plan.md`; `spec/trust-model/recovery-and-compromise.md`; `fixtures/conformance/recovery-scenarios.json` |
| Q12 | Which parts of red-path wallet UX should remain documentation-only in the first prototype? | The first prototype documents red-path fields and decision states only. Consumer UI build, accessibility testing, localization, and production copy are future work. | `prototype/implementation-plan.md`; `spec/verifier-policy/exception-governance.md`; `BACKLOG.md` |

## Validation evidence
The closure pass MUST be considered complete only when:
- `OPEN_QUESTIONS.md` contains no active numbered questions
- every JSON fixture parses successfully
- conformant fixtures do not contain forbidden normal-flow fields
- conformance fixtures cover `B0`, `B1`, `B2`, metadata, retention, exception, and recovery cases
- markdown links resolve
- no normal-flow design requires a per-presentation issuer callback

The final validation commands and results are recorded in the commit message or release notes for the closure commit.
