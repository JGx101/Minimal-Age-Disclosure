# Open Questions

This file tracks unresolved decisions that still shape the public project roadmap. These are not minor polish items. Most of them affect privacy guarantees, verifier restraint, or whether the repository is ready to move from documentation into a prototype.

## How to use this list
- Treat Priority 1 as implementation blockers.
- Treat Priorities 2 and 3 as design-closure work needed for a stable public baseline.
- Treat Priority 4 as scope control, so the project stays focused on minimal age disclosure rather than drifting into a broader identity product.

## Priority 1: architecture-critical
These questions decide whether the normal flow remains minimal-disclosure and anti-correlation by design.

1. What is the minimum acceptable holder-binding approach for `Profile R` without exposing a reusable verifier-visible key?
2. Which exact proof-binding artifacts, if any, can be verifier-visible without creating practical correlation risk?
3. Where is exact issuer identity required, and where is issuer class sufficient?
4. How coarse must assurance buckets be to avoid acting as fingerprints?
5. Which fields in the request object are essential, and which create avoidable correlation or logging risk?

## Priority 2: status, recovery, and compromise
These questions determine how the system behaves when credentials age, wallets fail, or compromise handling introduces pressure to over-collect data.

6. When is root-state status genuinely needed instead of expiry alone?
7. Which verifier classes, if any, may request online freshness?
8. How should wallet compromise state be represented without creating a holder-tracking surface?
9. What recovery model best balances privacy, usability, and deployability for root credentials?
10. How should re-issuance be handled without turning the issuer into a de facto activity checkpoint?

## Priority 3: governance and conformance
These questions determine whether verifier restraint can be governed, audited, and tested rather than stated only as a principle.

11. What audit thresholds should trigger verifier review for repeated exceptional requests?
12. What sanctions or trust-list consequences are realistic for repeated over-collection or exception abuse?
13. How should verifier telemetry limits be tested without invasive inspection of deployed systems?
14. Which metadata-fingerprinting tests can be made repeatable across implementations?
15. What profile-specific conformance differences belong in `Profile R` versus `Profile P`?

## Priority 4: productisation boundaries
These questions keep the repository scoped as a serious public architecture and standards project rather than an accidental consumer-product build.

16. What level of wallet UX can realistically be prototyped without drifting into a full consumer product build?
17. Which parts of the exception plane should remain design-only in v1 rather than simulated in a prototype?
18. Which deployment assumptions are safe for the public repo, and which belong only in research notes?

## What a good answer looks like
A question should usually move out of this file only when the answer is reflected in one or more of:
- an ADR
- a normative spec update
- a conformance condition or privacy-negative test
- a documented governance boundary
