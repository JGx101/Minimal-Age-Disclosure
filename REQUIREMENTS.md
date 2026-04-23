# Requirements Specification

## 1. Functional requirements
FR-01. The system SHALL support age-threshold claims for at least:
- `over_13`
- `over_16`
- `over_18`
- `over_21`

FR-02. The system SHALL support issuance of a root credential by a trusted issuer after evidence checking.

FR-03. The system SHALL support local storage of a root credential by a holder wallet.

FR-04. The system SHALL support wallet derivation of a transaction-bound proof for verifier presentation.

FR-05. The normal verifier path SHALL use a derived proof and SHALL NOT require direct presentation of the root credential.

FR-06. The system SHALL support verifier requests for threshold claims without requiring full identity disclosure.

FR-07. The system SHALL support bounded validity and lifecycle handling for root credentials and verifier-facing derived proofs.

FR-08. The system SHALL support status or suspension handling primarily for issuer trust, root credential state, or wallet compromise state, or document an explicit alternative strategy.

FR-09. The system SHALL support multiple issuers within a trust registry model.

FR-10. The system SHALL support a bounded assurance model so a verifier can understand how strongly the threshold was established without receiving detailed provenance.

FR-11. The system SHALL support separate technical profiling for at least:
- a regulator-ready interoperable profile
- a privacy-maximal research profile

FR-12. The system SHALL support conformance testing for verifier, wallet, and ecosystem behavior.

## 2. Privacy requirements
PR-01. The normal verification path SHALL NOT reveal legal name.

PR-02. The normal verification path SHALL NOT reveal exact DOB.

PR-03. The normal verification path SHALL NOT reveal document number.

PR-04. The normal verification path SHALL NOT reveal document image.

PR-05. The normal verification path SHALL avoid a stable verifier-visible holder identifier.

PR-06. The normal verification path SHALL avoid a stable verifier-visible root credential reference.

PR-07. The verifier SHALL receive only the minimum data required to evaluate the requested age-threshold claim.

PR-08. The issuer SHOULD NOT learn where or when a credential is presented in the normal flow.

PR-09. Status handling SHOULD minimise the creation of a centralised presentation log.

PR-10. The system SHOULD support unlinkable or low-linkability presentation where feasible.

PR-11. Metadata minimisation SHALL cover supporting fields as well as core personal attributes, including assurance references, issuer references, timestamps, policy identifiers, and proof-binding artifacts.

PR-12. Any higher-disclosure path MUST be explicit, exceptional, separately governed, and outside normal-flow conformance.

## 3. Security requirements
SR-01. Proofs SHALL be cryptographically verifiable.

SR-02. The verifier SHALL be able to validate issuer trust.

SR-03. The system SHALL mitigate replay and forwarding of captured proof artifacts through audience binding, nonce binding, or equivalent controls.

SR-04. The system SHALL include a documented approach to holder binding, along with the privacy tradeoffs of that approach.

SR-05. The system SHALL include a documented approach to issuer key rotation.

SR-06. The system SHALL include a documented approach to issuer compromise response.

SR-07. The system SHALL document assumptions and limitations regarding credential sharing or transfer.

SR-08. The system SHALL include tamper-evident integrity for credentials and status information where status is used.

SR-09. The repository SHALL include privacy-negative tests for verifier overreach, stable identifier leakage, metadata fingerprinting, replay, and misuse.

## 4. Governance and trust requirements
GR-01. The project SHALL define issuer classes and how issuers are trusted.

GR-02. The project SHALL define verifier classes, obligations, and conformance expectations.

GR-03. The project SHALL define wallet behavior relevant to privacy, binding, disclosure, and exception handling.

GR-04. The project SHALL define non-conformant verifier requests.

GR-05. The project SHALL define the role and data limits of the trust registry.

GR-06. The project SHALL define how assurance buckets are expressed and consumed.

GR-07. The project SHALL define exception governance, exception abuse handling, and audit expectations.

GR-08. The project SHALL define verifier compliance and retention boundaries.

## 5. Compliance and policy requirements
CR-01. The system SHOULD be mappable to UK digital verification concepts.

CR-02. The system SHOULD be mappable to EU age-verification and wallet concepts.

CR-03. The system SHOULD support necessity, proportionality, and metadata minimisation analysis.

CR-04. The project SHALL document where policy assumptions are made.

CR-05. The project SHALL distinguish technical feasibility from regulatory acceptance.

CR-06. The project SHALL distinguish what is normative for the common model from what is profile-specific or research-only.

## 6. Usability requirements
UR-01. The verifier flow SHOULD be simple enough for mainstream service integration.

UR-02. The wallet SHOULD clearly tell the holder what is being disclosed.

UR-03. Exceptional higher-disclosure requests SHOULD be clearly marked as exceptional.

UR-04. The holder SHOULD be able to understand root credential validity, derived proof limitations, and recovery implications.

UR-05. Recovery and device-loss considerations SHALL be documented even if not fully implemented in v1.

UR-06. The design SHOULD avoid forcing ordinary users into frequent re-issuance or repeated high-friction refresh unless that tradeoff is explicitly justified.
