# Glossary

## Minimal age disclosure
A model in which the verifier receives only the threshold result and tightly bounded supporting metadata, rather than identity or document-level data.

## Root credential
The issuer-originated credential stored locally by the wallet after evidence checking. It is not normally shown to verifiers.

## Derived proof
A transaction-bound verifier-facing proof derived from the root credential for a specific request.

## Governance plane
The layer that defines issuer roles, verifier obligations, trust anchors, conformance, sanctions, and exception handling.

## Root credential plane
The layer that covers issuance, local storage, renewal, suspension, compromise response, and recovery of the root credential.

## Derived proof plane
The layer that covers transaction-bound verifier-facing proof generation, disclosure minimisation, and proof-binding.

## Verification plane
The layer that covers verifier request objects, proof validation, trust validation, local decisioning, and retention boundaries.

## Status and recovery plane
The layer that covers issuer trust status, root credential state, compromise handling, refresh, recovery, and any privacy-preserving status mechanism.

## Exception plane
The higher-disclosure layer outside the normal minimal-disclosure flow, requiring separate justification, governance, and audit.

## Issuer class
A coarse category of issuer used for governance and normal-flow disclosure:
- `A0` authoritative issuer
- `A1` registered private issuer
- `A2` derived-attribute issuer

## Verifier class
A coarse verifier category used for obligations and exception rules:
- `V1` standard verifier
- `V2` high-assurance verifier
- `VX` exceptional verifier

## Assurance bucket
A bounded assurance category intended to be less fingerprinting-prone than highly specific provenance details.

## Metadata minimisation
The practice of constraining not only identity attributes, but also timestamps, assurance values, issuer references, request policy identifiers, and other side-channel fields that can become correlators.

## Transaction-bound proof of rightful possession
A per-transaction proof that the presenter rightfully controls the wallet-bound secret or artifact needed to derive a valid proof, without exposing a reusable verifier-visible key.

## Audience binding
Binding a proof to the intended verifier or relying party so that forwarding the proof elsewhere is ineffective.

## Nonce binding
Binding a proof to a verifier-provided fresh challenge so that replay of a previously captured proof is ineffective.

## Privacy-negative test
A deliberate test case designed to confirm that the system rejects or exposes an unwanted privacy outcome such as over-collection, stable identifier leakage, or presentation logging.

## Exception path
A higher-disclosure path outside the normal minimal-disclosure flow, requiring separate justification, audit, and conformance handling.

## Profile R
The regulator-ready and interoperable technical profile. It prioritises deployment fit and standards alignment.

## Profile P
The privacy-maximal and research-oriented technical profile. It prioritises stronger anti-correlation and unlinkability, while being more explicit about maturity and deployment tradeoffs.
