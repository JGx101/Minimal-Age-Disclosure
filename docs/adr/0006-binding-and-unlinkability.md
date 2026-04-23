# ADR-0006: Use transaction-bound proof of rightful possession without a verifier-visible stable holder identifier

## Status
Accepted

## Date
2026-04-23

## Context
The repository needs to address two requirements that pull against each other:
- the verifier should gain confidence that the presenter rightfully controls a valid wallet-bound credential
- the normal flow should not expose a stable verifier-visible public key, subject identifier, or proof artifact that enables cross-site correlation

If the same holder key or reusable proof artifact is disclosed to multiple verifiers, the privacy model collapses.

## Decision
Use a root credential plus derived proof model in which holder binding is demonstrated through **transaction-bound proof of rightful possession**.

The normal flow will:
- keep the root credential local to the wallet
- derive a proof per transaction
- bind that proof to verifier audience and nonce
- avoid disclosing a reusable verifier-visible holder key or subject handle

## Rationale
This approach best balances:
- replay resistance
- basic anti-sharing support
- anti-correlation requirements
- compatibility with both an interoperable and a privacy-maximal profile

## Alternatives considered
- verifier-visible stable wallet public key
- verifier-visible stable subject identifier
- root credential sent directly to verifiers
- no holder binding beyond possession of a copyable artifact

## Consequences
### Positive
- stronger anti-correlation posture
- cleaner separation between issuer trust and verifier-visible proof data
- room for both Profile R and Profile P

### Negative
- binding language and conformance tests must be more explicit
- some stronger anti-sharing goals remain out of scope for v1

## Follow-up actions
- keep root and derived proof roles aligned with the core specs
- keep verifier policy aligned with audience, nonce, and binding-mode rules
- keep metadata minimisation and retention rules aligned with `B0`, `B1`, and `B2`
- keep conformance tests checking that no reusable holder binding data leaks in the normal flow
