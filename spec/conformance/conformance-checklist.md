# Conformance Checklist

## Status
Draft

## Purpose
This checklist defines the normative conformance matrix for the minimal age-disclosure architecture.

Each conformance item SHALL be interpreted as a testable requirement tied to one or more normative clauses in the core specifications.

## Matrix fields
Each checklist item includes:
- requirement ID
- actor under test
- profile scope
- evidence mode
- pass/fail rule
- source clause

## CC-CORE
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-CORE-01 | Wallet, Verifier | COMMON | Request/response inspection | Pass only if the root credential is not disclosed in the normal flow. | Root-vs-derived proof model |
| CC-CORE-02 | Wallet, Verifier | COMMON | Request/response inspection | Pass only if the derived proof is the ordinary verifier-facing artifact. | Root-vs-derived proof model |
| CC-CORE-03 | Verifier | COMMON | Request inspection | Pass only if the request includes threshold, audience, nonce, purpose or policy context, and profile reference. | Claim profile |
| CC-CORE-04 | Verifier | COMMON | Request/response inspection | Pass only if audience binding, nonce binding, validity, and trust are validated before acceptance. | Verifier policy, trust model |
| CC-CORE-05 | Wallet, Verifier | COMMON | Request/response inspection | Fail if legal name, exact DOB, document number, document image, stable holder identifier, or stable root credential reference appears in the normal flow. | Claim profile |
| CC-CORE-06 | Verifier | COMMON | Governance review | Fail if token-specific live issuer callbacks are the default normal-flow condition. | Trust model, metadata minimisation |
| CC-CORE-07 | Verifier | COMMON | Governance review | Pass only if verifier behavior remains within declared verifier-class permissions. | Trust model, verifier policy |
| CC-CORE-08 | Wallet, Verifier | COMMON | Governance review | Pass only if exceptional flow is kept outside normal-flow conformance. | Verifier policy, exception governance |

## CC-WALLET
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-WALLET-01 | Wallet | COMMON | Request inspection | Pass only if requests missing nonce are rejected or refused. | Verifier policy |
| CC-WALLET-02 | Wallet | COMMON | Request inspection | Pass only if requests missing audience are rejected or refused. | Verifier policy |
| CC-WALLET-03 | Wallet | COMMON | Request/response inspection | Pass only if forbidden normal-flow request fields are rejected or refused. | Verifier policy |
| CC-WALLET-04 | Wallet | COMMON | Request/response inspection | Pass only if the wallet derives a transaction-bound proof rather than disclosing the root credential. | Root-vs-derived proof model |
| CC-WALLET-05 | Wallet | COMMON | UX and governance review | Pass only if exceptional requests are rendered as exceptional. | Exception governance |

## CC-VERIFIER
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-VERIFIER-01 | Verifier | COMMON | Request inspection | Pass only if the verifier sends only allowed request fields. | Verifier policy |
| CC-VERIFIER-02 | Verifier | COMMON | Request inspection | Fail if the verifier requests identity or document attributes in the normal flow. | Verifier policy |
| CC-VERIFIER-03 | Verifier | COMMON | Retention review | Pass only if retained fields stay within the approved minimum. | Retention spec |
| CC-VERIFIER-04 | Verifier | COMMON | Retention review | Fail if raw proof payloads are retained by default. | Retention spec |
| CC-VERIFIER-05 | Verifier | COMMON | Retention review | Fail if fine-grained metadata or telemetry reconstruct activity history. | Retention spec, metadata minimisation |
| CC-VERIFIER-06 | Verifier | COMMON | Governance review | Fail if the verifier defaults to the exceptional path where the normal path suffices. | Exception governance |

## CC-TRUST
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-TRUST-01 | Trust registry | COMMON | Document inspection | Pass only if the trust registry is limited to issuer-validation metadata. | Trust model |
| CC-TRUST-02 | Trust registry | COMMON | Governance review | Fail if the trust registry acts as holder registry, presentation log, or verifier telemetry sink. | Trust model |
| CC-TRUST-03 | Verifier | COMMON | Request/response inspection | Pass only if trust validation succeeds using disclosures allowed by the applicable profile. | Trust model |
| CC-TRUST-04 | Verifier, Status service | COMMON | Status flow review | Pass only if status checks apply only to issuer trust, root credential state, or wallet compromise state unless profile-specific exceptions exist. | Trust model |

## CC-METADATA
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-METADATA-01 | Wallet, Verifier | COMMON | Response inspection | Pass only if assurance metadata uses the approved bounded taxonomy. | Metadata minimisation |
| CC-METADATA-02 | Wallet, Verifier | COMMON | Response inspection | Pass only if issuer information uses the least specific disclosure compatible with trust validation. | Metadata minimisation, trust model |
| CC-METADATA-03 | Wallet, Verifier | COMMON | Response and retention review | Fail if timestamps exceed approved granularity. | Metadata minimisation |
| CC-METADATA-04 | Wallet, Verifier | COMMON | Repeated-transaction test | Fail if proof-binding artifacts are reusable across verifier interactions in the normal flow. | Root-vs-derived proof model, metadata minimisation |
| CC-METADATA-05 | Wallet, Verifier | COMMON | Repeated-transaction test | Fail if policy identifiers, status references, or validity fields become practical correlators. | Metadata minimisation |

## CC-PROFILE-R
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-R-01 | Wallet, Verifier | R | Request/response inspection | Pass only if Profile R uses only explicitly permitted pragmatic tradeoffs. | Claim profile, ADR-dependent |
| CC-R-02 | Wallet, Verifier | R | Repeated-transaction test | Pass only if any allowed binding mechanism remains within the approved Profile R tradeoff. | ADR-0008 |

## CC-PROFILE-P
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-P-01 | Wallet, Verifier | P | Repeated-transaction test | Pass only if Profile P satisfies stricter anti-correlation expectations than the common baseline. | Claim profile, metadata minimisation |
| CC-P-02 | Wallet, Verifier | P | Proof review | Pass only if verifier-visible artifacts satisfy Profile P non-reusability constraints. | Root-vs-derived proof model |

## BLOCKED_BY_ADR items
The following areas remain blocked pending ADR resolution:
- exact issuer resolution for trust validation
- minimum holder-binding mechanism for Profile R
- assurance bucket taxonomy and granularity
- validity granularity and freshness boundaries
- verifier audit minimum and retention edge cases
- exceptional-use review thresholds and sanctions
