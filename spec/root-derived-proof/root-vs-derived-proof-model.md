# Root vs Derived Proof Model

## Status
Draft, architecture decisions accepted

## 1. Purpose
This specification defines the normative separation between the wallet-held root credential and the verifier-facing derived proof.

It also defines the canonical binding modes used by the project:
- `B0`: transaction-bound baseline binding for `V1`
- `B1`: verifier-scoped pairwise proof of possession for `V2` and `Profile R`
- `B2`: unlinkable proof of possession for `Profile P`

## 2. Artifact definitions
### Root credential
A root credential is a credential issued after evidence checking and held by the wallet as the basis for derived proof generation.

A root credential MUST NOT be the ordinary verifier-facing artifact.

### Derived proof
A derived proof is a transaction-bound, verifier-facing proof derived from a root credential or equivalent wallet-held authority.

A derived proof MUST be the ordinary verifier-facing artifact in the normal flow.

### Proof transcript
A proof transcript is the verifier-visible material produced during a transaction to demonstrate possession and bind the proof to audience, nonce, policy, and validity conditions.

Proof transcripts MUST NOT be reusable across normal-flow verifier interactions.

## 3. Root credential requirements
A root credential MUST:
- be issued after evidence checking
- be stored wallet-side
- serve as the basis for derived proof generation
- remain outside the ordinary verifier-facing artifact set
- support suspension, renewal, reissuance, or expiry without requiring presentation logs

A root credential MAY contain:
- lifecycle information
- richer assurance context
- issuer-side management context

Such additional information MUST NOT automatically become verifier-visible.

## 4. Derived proof requirements
A derived proof MUST be:
- verifier-facing
- transaction-bound
- policy-scoped
- audience-bound
- nonce-bound
- bounded in validity
- derived from a wallet-held root credential or equivalent wallet-held authority

A derived proof MUST NOT expose:
- the full root credential
- stable verifier-visible root credential references
- stable cross-verifier holder identifiers
- reusable verifier-visible proof-binding artifacts
- disallowed personal or document-level data

## 5. Binding modes
### 5.1 Common binding rule
Every normal-flow derived proof MUST demonstrate rightful possession using one of the binding modes defined in this section.

No binding mode MAY introduce a reusable verifier-visible proof-binding artifact in the normal flow.

### 5.2 `B0`: transaction-bound baseline binding
`B0` is the standard low-friction binding mode for `V1` verifiers.

`B0` MUST include:
- audience binding
- nonce binding
- transaction-bound possession evidence derived from wallet-held authority
- no additional verifier-visible holder binding handle

`B0` MUST NOT expose a pairwise verifier handle, a stable holder key, or a stable root credential reference.

The concrete mechanism shape for `B0` is:
- the root credential or wallet-held authority is bound to a wallet-held holder secret, holder key, or equivalent possession secret
- the wallet produces a transaction proof over a transcript that includes at least the verifier audience, nonce, requested threshold, policy reference, proof validity, and proof format reference
- the verifier-visible transcript contains only fresh transaction evidence, not the underlying holder secret, a reusable public holder key, or a stable credential reference

`B0` MAY be used by `Profile R` for `V1` checks where the governing policy does not require stronger anti-sharing controls.

### 5.3 `B1`: verifier-scoped pairwise proof of possession
`B1` is the high-assurance binding mode for `V2` verifiers and the required binding mode for high-assurance `Profile R` flows.

`B1` MUST:
- scope possession evidence to the verifier audience
- produce a fresh transaction proof transcript for each presentation
- prevent cross-verifier reuse of verifier-visible binding artifacts
- treat any verifier-scoped continuity material as privacy-sensitive

`B1` MUST NOT:
- expose a cross-verifier holder identifier
- expose a reusable proof transcript
- permit verifier-scoped continuity material to be retained as default telemetry
- allow a verifier to use pairwise material outside the declared policy purpose

The concrete mechanism shape for `B1` is:
- the wallet derives a verifier-scoped secret from wallet-held authority using a domain-separated derivation such as `B1_secret = KDF(holder_secret, "B1", canonical_verifier_audience, profile_or_policy_scope)`
- the wallet proves possession of that verifier-scoped secret through a fresh transaction transcript bound to the verifier audience, nonce, requested threshold, policy reference, validity, and proof format reference
- the wallet MUST NOT disclose `B1_secret`, a reusable public key derived from it, or a cross-verifier derivation input
- any continuity value used by the verifier MUST be derived only for the same canonical verifier audience and declared policy scope

`B1` MAY permit verifier-scoped continuity where the governing rule requires stronger anti-sharing controls, but that continuity MUST remain verifier-scoped and MUST be governed by verifier retention rules.

Same-verifier continuity under `B1` is permitted only when all of the following hold:
- the verifier is the same canonical audience as the original continuity context
- the request purpose and policy reference are compatible with the original continuity purpose
- the continuity material is not placed in the reusable proof transcript or ordinary analytics logs
- the verifier retention period is declared, bounded, and no longer than the governing anti-sharing purpose requires
- the wallet can refuse the request if continuity is requested for an ineligible verifier class, unrelated purpose, or excessive retention period

### 5.4 `B2`: unlinkable proof of possession
`B2` is the privacy-maximal binding mode for `Profile P`.

`B2` MUST:
- provide proof of rightful possession without a verifier-stable holder handle
- avoid verifier-visible reusable proof-binding artifacts
- prevent linking across verifiers by construction
- prevent linking across repeated presentations to the same verifier except where the holder explicitly enters a separate account or exceptional context outside the normal proof

The concrete mechanism shape for `B2` is:
- the wallet proves possession of a valid wallet-held authority and the age-threshold predicate in a selective-disclosure, anonymous-credential, or zero-knowledge style proof
- the proof transcript is bound to the verifier audience, nonce, requested threshold, policy reference, validity, and proof format reference
- the proof transcript does not disclose a verifier-stable holder handle, pairwise pseudonym, static holder public key, stable credential reference, or reusable status handle
- repeated presentations to the same verifier are unlinkable at the proof-binding layer unless the holder separately authenticates to an account or enters an exceptional flow outside normal-flow conformance

`B2` MAY use anonymous-credential, selective-disclosure, or zero-knowledge style constructions, including BBS-style proofs or equivalent unlinkable proof systems.

## 6. Binding mode eligibility
| Binding mode | Permitted verifier class | Profile use | Normal-flow correlation boundary |
| --- | --- | --- | --- |
| `B0` | `V1` | Common and low-risk `Profile R` | No verifier-visible holder handle |
| `B1` | `V2` | High-assurance `Profile R` | Verifier-scoped only; no cross-verifier reuse |
| `B2` | `V1`, `V2` where supported | `Profile P` | No verifier-stable holder handle |

`VX` exceptional flows MAY use additional binding or identity evidence only under exception governance. Such evidence is outside normal-flow conformance.

## 7. Mode negotiation and downgrade handling
A verifier request MUST identify the required binding mode for the transaction.

A wallet MUST NOT silently substitute a different binding mode from the one requested.

If the wallet cannot satisfy the requested binding mode, it MUST refuse the request or require a new verifier request that explicitly permits a different mode.

If a verifier requests `B1` and the wallet can only produce `B0`, the wallet MUST refuse. Downgrading from `B1` to `B0` is non-conformant unless the verifier issues a new `V1`/`B0` request whose policy no longer requires high-assurance anti-sharing controls.

If a verifier requests `B1` and the wallet can produce `B2`, the wallet MAY use `B2` only when the verifier request or governing profile explicitly accepts `B2` as an alternative and the policy decision does not require `B1` same-verifier continuity. Otherwise, the wallet MUST refuse.

If a verifier requests `B0` and the wallet can only produce `B2`, the wallet MAY ask for or respond to a new `B2`-permitted request where the verifier class and profile allow `B2`.

If a verifier requests `B2` and the wallet can only produce `B0` or `B1`, the wallet MUST refuse the normal flow.

A verifier MUST NOT request `B1` merely to force sticky continuity where `B0` or `B2` satisfies the governing policy. A wallet MUST treat such a request as non-conformant or exceptional.

## 8. Disclosure boundary
A derived proof MAY disclose only:
- the satisfied threshold result
- bounded validity information
- audience binding evidence
- nonce binding evidence
- transaction-bound rightful-possession evidence
- bounded assurance information
- issuer information required by the applicable trust path
- the binding mode used

A derived proof MUST NOT disclose:
- the full root credential
- stable verifier-visible root credential references
- reusable verifier-visible holder identifiers
- reusable verifier-visible proof transcripts
- disallowed personal or document-level data

## 9. Lifecycle separation
Recovery, suspension, and compromise handling MUST attach primarily to:
- root credential state
- wallet compromise state
- issuer trust state

Such handling MUST NOT, by default, require per-presentation state changes for every normal-flow verifier interaction.

## 10. Non-normal root disclosure
Any direct root credential presentation MUST be treated as non-normal.

Direct root credential disclosure is outside normal-flow conformance and MAY occur only under the exception governance rules in `spec/verifier-policy/exception-governance.md`.

If a verifier requires root credential disclosure for an ordinary threshold check, the flow MUST be treated as non-conformant.

## 11. Profile deltas
### Common baseline
All conformant implementations MUST preserve the root/derived separation in the normal flow.

### Profile R
`Profile R` MUST support `B0` for `V1` checks and `B1` for `V2` high-assurance checks.

`Profile R` MUST NOT permit cross-verifier correlation through binding artifacts.

### Profile P
`Profile P` MUST use `B2` for normal-flow presentations where Profile P conformance is claimed.

`Profile P` MUST treat verifier-stable binding artifacts as non-conformant in the normal flow.

## Appendix A. Mechanism layer
This appendix defines the cryptographic mechanism shape required by the binding modes without selecting a single mandatory proof system for every deployment.

### A.1 Common transcript
Every binding mode MUST bind the possession proof to a canonical transaction transcript containing:
- verifier audience
- nonce
- requested threshold
- profile reference
- verifier class
- purpose
- policy reference
- jurisdiction reference where applicable
- maximum assurance bucket
- binding mode
- freshness requirement
- validity window
- proof format reference

The transcript MUST be canonicalised before signing or proving. Semantically equivalent verifier origins MUST NOT produce multiple ambiguous audience values.

### A.2 Holder authority
The wallet-held authority MAY be a root credential, a credential-bound holder secret, a hardware-backed key, a wallet attestation, or another governed construction.

The verifier-facing proof MUST demonstrate possession of that authority without disclosing the authority itself in the normal flow.

### A.3 `B0` instantiation pattern
`B0` uses transaction-only possession evidence.

Acceptable `B0` instantiations include:
- a proof of knowledge of a credential-bound holder secret over the common transcript
- a transaction-specific holder key certified or proven from wallet-held authority without exposing a reusable verifier-visible holder key
- an mdoc-style device/session proof only where the verifier-visible device-binding material is not reusable across normal-flow presentations

Unacceptable `B0` instantiations include:
- a static verifier-visible holder public key reused across presentations
- a stable `cnf` or device key value that lets verifiers correlate presentations
- a proof transcript that can be replayed with a different audience or nonce

### A.4 `B1` instantiation pattern
`B1` uses verifier-scoped possession evidence with optional same-verifier continuity.

The wallet SHOULD derive `B1` material using a domain-separated derivation equivalent to:

```text
B1_secret = KDF(holder_secret, "minimal-age/B1", canonical_verifier_audience, policy_scope)
presentation_secret = KDF(B1_secret, "presentation", nonce, transcript_hash)
```

The verifier-visible proof MUST be fresh per transaction. The verifier MAY learn or store only the minimum continuity material needed for the same verifier and policy scope. That continuity material MUST NOT be usable by another verifier and MUST NOT appear as a reusable possession proof.

A `B1` implementation MAY realise same-verifier continuity through:
- a verifier-scoped pseudonym produced inside a governed continuity subprotocol
- a verifier-local keyed digest or blinded continuity record that is not disclosed to other parties
- a zero-knowledge proof of equality to verifier-held continuity state without revealing the underlying `B1_secret`

The following are non-conformant:
- deriving `B1` from only a global holder identifier
- using the same pairwise value for different verifier audiences
- placing a stable pairwise public key in ordinary proof transcripts
- using `B1` continuity material for unrelated account tracking, advertising, fraud scoring, or analytics

### A.5 `B2` instantiation pattern
`B2` uses unlinkable possession evidence.

Acceptable `B2` instantiations include:
- anonymous-credential proofs where the holder proves possession and the age predicate without a pseudonym
- BBS-style selective-disclosure proofs with proof-specific randomness and no disclosed holder handle
- zero-knowledge proofs that bind the transaction transcript while hiding the holder secret and credential reference

Unacceptable `B2` instantiations include:
- any verifier-stable pseudonym in the normal proof
- a static holder public key visible to the verifier
- a pairwise verifier handle retained as part of the proof-binding layer
- unique status evidence that can be joined with the proof transcript

## Appendix B. Proof-family mapping note
This table is a profile mapping note. It does not assert that every current implementation of a named family already satisfies the binding mode without additional profile constraints.

| Proof family or rail | `B0` mapping | `B1` mapping | `B2` mapping | Required caution |
| --- | --- | --- | --- | --- |
| OpenID4VCI | Issues the wallet-held authority, holder-secret commitment, or root credential used later by `B0`. | Issues or provisions material from which verifier-scoped `B1` derivations can be made. | Issues anonymous-credential-capable or ZK-capable authority where the selected credential format supports it. | Issuance identifiers, credential IDs, and holder-binding metadata MUST NOT become verifier-visible correlators. |
| OpenID4VP | Carries the audience, nonce, request object, and verifier-facing presentation for `B0`. | Carries a fresh verifier-scoped presentation and, where governed, continuity negotiation metadata. | Carries unlinkable presentations where the underlying proof format supports unlinkability. | OpenID4VP is a presentation rail, not by itself an unlinkability guarantee. |
| ISO mdoc | Maps to session transcript and device engagement binding where device-binding material is not verifier-reusable. | Requires pairwise or verifier-scoped device/holder binding and tight reader-auth audience scoping. | Requires an unlinkable mdoc-derived proof profile or equivalent ZK/anonymous presentation layer. | Plain static device-key exposure can violate `B0`, `B1`, or `B2` depending on reuse. |
| SD-JWT VC | Maps to selective disclosure plus transaction key binding only when stable `cnf` material is not verifier-visible or reusable. | Requires pairwise/verifier-scoped holder binding and fresh KB proof transcripts. | Requires an unlinkable extension or different proof layer; ordinary SD-JWT VC key binding is usually not enough. | A reused holder `cnf` key is a correlator. |
| BBS-style selective disclosure | Supports `B0` through proof of possession over the transcript with fresh proof randomness. | Supports `B1` where a verifier-scoped pseudonym or equality proof is explicitly governed. | Strong fit where proofs disclose no pseudonym and use proof-specific randomness. | Any optional pseudonym feature MUST be disabled or governed according to the selected mode. |

## Appendix C. Adversarial analysis
### C.1 `B0`
Relay and replay: `B0` mitigates replay and simple forwarding through nonce and audience binding. A real-time relay can still cause the wallet to participate in a live transaction, so `B0` is not a strong anti-sharing mode.

Shared-device use: `B0` proves control of wallet-held authority for a transaction, not that the same natural person is using the device. Local wallet unlock, device policy, or exceptional controls are outside the verifier-facing proof.

Colluding verifiers: `B0` must not expose a stable holder key, root credential reference, status URL, or reusable transcript. Colluding verifiers may still compare coarse metadata, so metadata minimisation remains part of conformance.

Malicious verifier forcing sticky continuity: A `V1` verifier requesting `B1` without policy eligibility is non-conformant. The wallet must refuse rather than emit continuity material.

### C.2 `B1`
Relay and replay: `B1` inherits nonce and audience binding and adds verifier-scoped derivation. It reduces cross-verifier relay value but does not prove the holder is physically present unless combined with local wallet controls.

Shared-device use: `B1` same-verifier continuity can detect recurrence of the same wallet-held authority for the same verifier and policy scope. It MUST NOT be represented as biometric or person-binding proof.

Colluding verifiers: `B1` prevents direct cross-verifier matching by deriving pairwise material from the canonical verifier audience. Colluding verifiers must not be able to force a shared audience value, shared policy scope, or reusable continuity artifact.

Malicious verifier forcing sticky continuity: `B1` continuity is allowed only for eligible `V2` or high-assurance `Profile R` purposes. Retention, reuse, and analytics use are separately constrained. Wallets must refuse unrelated, excessive, or undeclared continuity requests.

### C.3 `B2`
Relay and replay: `B2` remains transaction-bound by nonce and audience even though it hides holder continuity. It prevents replay of a captured proof transcript but does not by itself stop a live relay attack.

Shared-device use: `B2` intentionally avoids verifier-visible continuity, so it cannot provide same-verifier anti-sharing evidence in the normal proof. Any stronger person-binding belongs in an exceptional or separate account-authentication context.

Colluding verifiers: `B2` is designed to prevent verifier-stable and cross-verifier proof-binding correlation. The main residual risks are metadata fingerprinting, unique status evidence, rare proof formats, and account-layer identifiers outside the proof.

Malicious verifier forcing sticky continuity: A `Profile P` verifier must not request `B1` or a pseudonymous `B2` variant in the normal flow. Wallets must refuse requests that add pairwise handles, static holder keys, or unique status callbacks.
