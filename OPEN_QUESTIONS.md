# Open Questions

## Priority 1: architecture-critical
1. What is the minimum acceptable holder-binding approach for Profile R without exposing a reusable verifier-visible key?
2. Which exact proof-binding artifacts, if any, can be verifier-visible without creating practical correlation risk?
3. Where is exact issuer identity required, and where is issuer class sufficient?
4. How coarse must assurance buckets be to avoid acting as fingerprints?
5. Which fields in the request object are essential, and which create avoidable correlation or logging risk?

## Priority 2: status, recovery, and compromise
6. When is root-state status genuinely needed instead of expiry alone?
7. Which verifier classes, if any, may request online freshness?
8. How should wallet compromise state be represented without creating a holder-tracking surface?
9. What recovery model best balances privacy, usability, and deployability for root credentials?
10. How should re-issuance be handled without turning the issuer into a de facto activity checkpoint?

## Priority 3: governance and conformance
11. What audit thresholds should trigger verifier review for repeated exceptional requests?
12. What sanctions or trust-list consequences are realistic for repeated over-collection or exception abuse?
13. How should verifier telemetry limits be tested without invasive inspection of deployed systems?
14. Which metadata-fingerprinting tests can be made repeatable across implementations?
15. What profile-specific conformance differences belong in Profile R versus Profile P?

## Priority 4: productisation boundaries
16. What level of wallet UX can realistically be prototyped without drifting into a full consumer product build?
17. Which parts of the exception plane should remain design-only in v1 rather than simulated in a prototype?
18. Which deployment assumptions are safe for the public repo, and which belong only in research notes?
