# CV Summary

## 1-line version
Designed a privacy-preserving age-threshold proof architecture that uses root credentials and transaction-bound derived proofs to avoid identity disclosure and stable cross-site identifiers.

## 3-line version
Designed a minimal age-disclosure architecture focused on threshold proof, verifier restraint, and anti-correlation. Structured the project around a root credential / derived proof split, dual technical profiles, and governance-first conformance rules. Produced the architecture, claim profile, verifier policy, trust model, recovery model, conformance suite outline, and publication-ready documentation.

## Case-study version
- Problem: many age-verification flows collect identity data that exceeds what is needed for threshold checks.
- Architecture: split issuance and presentation into a root credential held locally in the wallet and a transaction-bound derived proof shown to the verifier.
- Privacy model: prohibited exact DOB, legal name, document number, document image, and stable verifier-visible identifiers in the normal flow.
- Governance model: defined issuer classes, verifier classes, exception governance, retention limits, and privacy-negative conformance tests.
- Standards direction: documented a primary interoperable profile using OpenID4VCI/OpenID4VP and a research-grade privacy-maximal profile for stronger unlinkability.
