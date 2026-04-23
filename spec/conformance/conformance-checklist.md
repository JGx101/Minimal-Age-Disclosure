# Conformance Checklist

## Status
Draft, architecture decisions accepted

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
| CC-CORE-03 | Verifier | COMMON | Request inspection | Pass only if the request includes every canonical request field. | Claim profile |
| CC-CORE-04 | Wallet, Verifier | COMMON | Response inspection | Pass only if the response includes every canonical response field and no forbidden response field. | Claim profile |
| CC-CORE-05 | Verifier | COMMON | Request/response inspection | Pass only if audience binding, nonce binding, binding mode, validity, and trust are validated before acceptance. | Verifier policy, trust model |
| CC-CORE-06 | Wallet, Verifier | COMMON | Request/response inspection | Fail if legal name, exact DOB, document number, document image, stable holder identifier, stable root credential reference, unique status callback URI, or reusable proof-binding artifact appears in normal flow. | Claim profile |
| CC-CORE-07 | Verifier | COMMON | Governance review | Fail if token-specific live issuer callbacks are the default normal-flow condition. | Trust model, metadata minimisation |
| CC-CORE-08 | Wallet, Verifier | COMMON | Governance review | Pass only if exceptional flow is kept outside normal-flow conformance. | Verifier policy, exception governance |

## CC-BINDING
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-BIND-01 | Wallet, Verifier | COMMON | Request/response inspection | Pass only if `B0`, `B1`, or `B2` is used according to verifier class and profile. | Root-vs-derived proof model |
| CC-BIND-02 | Wallet, Verifier | COMMON | Repeated-transaction test | Fail if any binding mode exposes a reusable verifier-visible proof transcript. | Root-vs-derived proof model |
| CC-BIND-03 | Wallet, Verifier | R | Cross-verifier test | Fail if `B1` exposes a cross-verifier reusable binding artifact. | Root-vs-derived proof model |
| CC-BIND-04 | Wallet, Verifier | P | Repeated-transaction test | Fail if `B2` exposes any verifier-stable holder handle. | Root-vs-derived proof model |

## CC-WALLET
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-WALLET-01 | Wallet | COMMON | Request inspection | Pass only if requests missing nonce are rejected or refused. | Verifier policy |
| CC-WALLET-02 | Wallet | COMMON | Request inspection | Pass only if requests missing audience are rejected or refused. | Verifier policy |
| CC-WALLET-03 | Wallet | COMMON | Request/response inspection | Pass only if forbidden normal-flow request fields are rejected or refused. | Verifier policy |
| CC-WALLET-04 | Wallet | COMMON | Request/response inspection | Pass only if the wallet derives a transaction-bound proof rather than disclosing the root credential. | Root-vs-derived proof model |
| CC-WALLET-05 | Wallet | COMMON | UX and governance review | Pass only if exceptional requests are rendered as red-path exceptional flows. | Exception governance |

## CC-VERIFIER
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-VERIFIER-01 | Verifier | COMMON | Request inspection | Pass only if the verifier sends only allowed request fields. | Verifier policy |
| CC-VERIFIER-02 | Verifier | COMMON | Request inspection | Fail if the verifier requests identity or document attributes in the normal flow. | Verifier policy |
| CC-VERIFIER-03 | Verifier | COMMON | Retention review | Pass only if retained fields stay within the approved minimum. | Retention spec |
| CC-VERIFIER-04 | Verifier | COMMON | Retention review | Fail if raw proof payloads or raw proof transcripts are retained by default. | Retention spec |
| CC-VERIFIER-05 | Verifier | COMMON | Retention review | Fail if fine-grained metadata or telemetry reconstruct activity history. | Retention spec, metadata minimisation |
| CC-VERIFIER-06 | Verifier | COMMON | Governance review | Fail if the verifier defaults to the exceptional path where the normal path suffices. | Exception governance |
| CC-VERIFIER-07 | Verifier | COMMON | Retention review | Fail if `B1` continuity material is retained as default telemetry. | Retention spec |

## CC-TRUST-AND-RECOVERY
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-TRUST-01 | Trust registry | COMMON | Document inspection | Pass only if the trust registry is limited to issuer-validation metadata. | Trust model |
| CC-TRUST-02 | Trust registry | COMMON | Governance review | Fail if the trust registry acts as holder registry, presentation log, or verifier telemetry sink. | Trust model |
| CC-TRUST-03 | Verifier | COMMON | Request/response inspection | Pass only if trust validation succeeds using disclosures allowed by the applicable profile. | Trust model |
| CC-TRUST-04 | Verifier, Status service | COMMON | Status flow review | Pass only if status checks apply only to issuer trust, root credential state, or wallet compromise state. | Trust model |
| CC-REC-01 | Issuer, Wallet, Trust registry | COMMON | State-flow review | Pass only if issuer trust, root credential, and wallet compromise states use the defined state values. | Recovery and compromise |
| CC-REC-02 | Issuer, Wallet, Trust registry | COMMON | Recovery-flow review | Fail if lost, stolen, compromised, or issuer-withdrawal flows create issuer-visible presentation histories. | Recovery and compromise |

## CC-METADATA
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-METADATA-01 | Wallet, Verifier | COMMON | Response inspection | Pass only if assurance metadata uses `AB1`, `AB2`, or `AB3`. | Metadata minimisation |
| CC-METADATA-02 | Wallet, Verifier | COMMON | Response inspection | Pass only if issuer information uses issuer class by default and exact issuer identity only where needed for trust validation. | Metadata minimisation, trust model |
| CC-METADATA-03 | Wallet, Verifier | COMMON | Response and retention review | Fail if timestamps exceed approved granularity. | Metadata minimisation |
| CC-METADATA-04 | Wallet, Verifier | COMMON | Repeated-transaction test | Fail if proof-binding artifacts are reusable across verifier interactions in the normal flow. | Root-vs-derived proof model, metadata minimisation |
| CC-METADATA-05 | Wallet, Verifier | COMMON | Repeated-transaction test | Fail if policy identifiers, status references, proof format references, or validity fields become practical correlators. | Metadata minimisation |
| CC-METADATA-06 | Verifier | COMMON | Retention review | Fail if exact issuer identity is retained by default without governance justification. | Metadata minimisation, retention spec |

## CC-EXCEPTION
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-EXC-01 | Verifier | COMMON | Request inspection | Fail if `V1` invokes exceptional disclosure. | Exception governance |
| CC-EXC-02 | Verifier | COMMON | Request inspection | Fail if any required exceptional field is missing, vague, or inconsistent. | Exception governance |
| CC-EXC-03 | Wallet | COMMON | UX review | Pass only if wallet red-path UX shows exception status, verifier identity, extra fields, lawful basis, retention period, and cancel/refuse option. | Exception governance |
| CC-EXC-04 | Verifier, Governance layer | COMMON | Audit review | Review required if exceptional use exceeds `5%` of monthly age-check volume. | Exception governance |
| CC-EXC-05 | Verifier, Governance layer | COMMON | Audit review | Fail if exceptional use exceeds `10%` of monthly volume or repeats review triggers across two consecutive months without scoped governance approval. | Exception governance |

## CC-PROFILE-R
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-R-01 | Wallet, Verifier | R | Request/response inspection | Pass only if `Profile R` supports `B0` for `V1` and `B1` for `V2`. | Root-vs-derived proof model |
| CC-R-02 | Wallet, Verifier | R | Repeated-transaction test | Pass only if `B1` remains verifier-scoped and does not become cross-verifier correlation material. | Root-vs-derived proof model |

## CC-PROFILE-P
| ID | Actor | Scope | Evidence | Pass/Fail Rule | Source |
| --- | --- | --- | --- | --- | --- |
| CC-P-01 | Wallet, Verifier | P | Repeated-transaction test | Pass only if `Profile P` uses `B2` and satisfies stricter anti-correlation expectations than the common baseline. | Claim profile, metadata minimisation |
| CC-P-02 | Wallet, Verifier | P | Proof review | Pass only if verifier-visible artifacts satisfy `B2` non-reusability constraints. | Root-vs-derived proof model |
