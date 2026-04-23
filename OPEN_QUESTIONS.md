# Open Questions

This file tracks genuinely remaining questions after the accepted architecture decisions for binding modes, request/response objects, metadata coarsening, recovery state, verifier retention, and exception thresholds.

## How to use this list
- Treat these as implementation-profile and validation questions, not reopened direction-of-travel decisions.
- Do not reopen the root credential / derived proof split, the `B0` / `B1` / `B2` taxonomy, or the no per-presentation issuer callback baseline.
- Move a question out of this file when it is reflected in an ADR, a normative spec update, a conformance condition, or a prototype acceptance criterion.

## Priority 1: proof construction and implementation profile
1. Which standards proof family should the first `Profile P` prototype instantiate for the `B2` mechanism pattern?
2. Which mainstream `Profile R` rails can best carry the canonical request and response objects without weakening the metadata rules?
3. What automated evidence is sufficient to prove that a chosen `B1` implementation keeps continuity material same-verifier and same-purpose scoped?

## Priority 2: conformance automation
4. Which privacy-negative tests can be automated first without implementing a full wallet?
5. How should repeated-transaction tests generate evidence for metadata fingerprinting?
6. What fixture format should represent conformant and non-conformant request/response examples?

## Priority 3: policy and governance validation
7. How should the `5%` review threshold and `10%` exception failure threshold be validated in real governance settings?
8. Which UK and EU policy sources should be cited for verifier-class eligibility and exception governance?
9. What review process should approve a scoped exception class without weakening normal-flow conformance?

## Priority 4: prototype boundaries
10. What is the minimum mock issuer, wallet, verifier, and trust registry needed to demonstrate the accepted architecture?
11. Which recovery and compromise scenarios should be simulated first?
12. Which parts of red-path wallet UX should remain documentation-only in the first prototype?
