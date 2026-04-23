# Root vs Derived Proof Model

## Status
Draft

## 1. Purpose
This specification defines the normative separation between the wallet-held root credential and the verifier-facing derived proof.

## 2. Artifact definitions
### Root credential
A credential issued after evidence checking and held by the wallet as the basis for derived proof generation.

### Derived proof
A transaction-bound, verifier-facing proof derived from a root credential or equivalent wallet-held authority.

## 3. Root credential requirements
A root credential MUST:
- be issued after evidence checking
- be stored locally by the wallet
- serve as the basis for derived proof generation
- remain outside the ordinary verifier-facing artifact set

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
- bounded in validity
- derived from a wallet-held root credential or equivalent wallet-held authority

## 5. Binding requirements
A derived proof MUST demonstrate rightful possession.

The common baseline MUST NOT rely on reusable verifier-visible binding artifacts by default.

The minimum acceptable `Profile R` holder-binding mechanism remains subject to [ADR-0008](../../docs/adr/0008-minimum-holder-binding-mechanism-for-profile-r.md).

## 6. Disclosure boundary
A derived proof MAY disclose only:
- the satisfied threshold result
- bounded validity information
- audience binding evidence
- nonce binding evidence
- transaction-bound rightful-possession evidence
- bounded assurance information
- issuer information required by the applicable trust path

A derived proof MUST NOT disclose:
- the full root credential
- stable verifier-visible root credential references
- reusable verifier-visible holder identifiers
- disallowed personal or document-level data

## 7. Lifecycle separation
Recovery, suspension, and compromise handling MUST attach primarily to:
- root credential state
- wallet trust state
- issuer trust state

Such handling MUST NOT, by default, require per-presentation state changes for every normal-flow verifier interaction.

## 8. Non-normal root disclosure
Any direct root credential presentation MUST be treated as non-normal.

Any non-normal root credential disclosure MUST:
- be explicitly classified as exceptional
- be separately governed
- be outside normal-flow conformance

The conditions for such disclosure remain subject to [ADR-0013](../../docs/adr/0013-conditions-for-non-normal-root-credential-disclosure.md).

## 9. Common baseline and profile deltas
### Common baseline
All conformant implementations MUST preserve the root/derived separation in the normal flow.

### Profile R
`Profile R` MAY use conservative proof constructions provided they do not collapse the common boundary between root credential and derived proof.

### Profile P
`Profile P` SHOULD impose stronger unlinkability constraints on derived proof construction and MAY require stronger non-reusability properties than `Profile R`.
