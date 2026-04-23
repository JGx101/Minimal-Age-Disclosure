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

`B1` MAY permit verifier-scoped continuity where the governing rule requires stronger anti-sharing controls, but that continuity MUST remain verifier-scoped and MUST be governed by verifier retention rules.

### 5.4 `B2`: unlinkable proof of possession
`B2` is the privacy-maximal binding mode for `Profile P`.

`B2` MUST:
- provide proof of rightful possession without a verifier-stable holder handle
- avoid verifier-visible reusable proof-binding artifacts
- prevent linking across verifiers by construction
- prevent linking across repeated presentations to the same verifier except where the holder explicitly enters a separate account or exceptional context outside the normal proof

`B2` MAY use anonymous-credential, selective-disclosure, or zero-knowledge style constructions.

This specification does not select the concrete cryptographic construction for `B2`; that choice is implementation-profile work, not an architecture blocker.

## 6. Binding mode eligibility
| Binding mode | Permitted verifier class | Profile use | Normal-flow correlation boundary |
| --- | --- | --- | --- |
| `B0` | `V1` | Common and low-risk `Profile R` | No verifier-visible holder handle |
| `B1` | `V2` | High-assurance `Profile R` | Verifier-scoped only; no cross-verifier reuse |
| `B2` | `V1`, `V2` where supported | `Profile P` | No verifier-stable holder handle |

`VX` exceptional flows MAY use additional binding or identity evidence only under exception governance. Such evidence is outside normal-flow conformance.

## 7. Disclosure boundary
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

## 8. Lifecycle separation
Recovery, suspension, and compromise handling MUST attach primarily to:
- root credential state
- wallet compromise state
- issuer trust state

Such handling MUST NOT, by default, require per-presentation state changes for every normal-flow verifier interaction.

## 9. Non-normal root disclosure
Any direct root credential presentation MUST be treated as non-normal.

Direct root credential disclosure is outside normal-flow conformance and MAY occur only under the exception governance rules in `spec/verifier-policy/exception-governance.md`.

If a verifier requires root credential disclosure for an ordinary threshold check, the flow MUST be treated as non-conformant.

## 10. Profile deltas
### Common baseline
All conformant implementations MUST preserve the root/derived separation in the normal flow.

### Profile R
`Profile R` MUST support `B0` for `V1` checks and `B1` for `V2` high-assurance checks.

`Profile R` MUST NOT permit cross-verifier correlation through binding artifacts.

### Profile P
`Profile P` MUST use `B2` for normal-flow presentations where Profile P conformance is claimed.

`Profile P` MUST treat verifier-stable binding artifacts as non-conformant in the normal flow.
