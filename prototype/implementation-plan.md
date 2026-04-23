# Prototype Implementation Plan

## Purpose
Plan a narrow demonstration of the architecture without committing to prototype code or stable wire formats prematurely.

## Prototype scope
The prototype plan remains documentation-only in this pass.

Its purpose is to demonstrate:
- root credential issuance after evidence checking
- local wallet storage of the root credential
- derivation of a transaction-bound verifier-facing proof
- trust validation, nonce binding, audience binding, and bounded validity
- rejection or warning on over-broad verifier requests
- at least one recovery, compromise, or suspension scenario

## Planned components
- issuer mock
- wallet simulator
- verifier demo
- trust-registry mock
- optional batched status mock where justified
- status relay mock
- governance or audit role mock

## Minimum mock responsibilities
The first prototype MAY remain fixture-driven, but any later service prototype MUST include the following roles:

| Component | Minimum responsibility | Must not do |
| --- | --- | --- |
| Mock issuer | Issue a wallet-held root credential or authority and publish root state through a non-unique status path. | Receive ordinary presentation history or handle per-presentation verifier callbacks. |
| Wallet simulator | Store root authority, evaluate request conformance, derive `B0`, `B1`, or `B2` proof-shaped responses, and refuse over-broad requests. | Disclose the root credential, stable holder identifier, stable root reference, or reusable proof-binding artifact in normal flow. |
| Verifier demo | Send canonical request objects, validate derived-proof responses, apply retention limits, and reject non-conformant examples. | Retain raw proof payloads, proof transcripts, unique status references, or fine-grained telemetry by default. |
| Trust-registry mock | Publish issuer trust state and permitted issuer or verifier classes. | Act as a holder registry or presentation log. |
| Status relay mock | Provide batched, cacheable, relayable, or otherwise non-unique state evidence for issuer trust, root credential, or wallet compromise state. | Provide token-specific live issuer callbacks in normal flow. |
| Governance or audit mock | Evaluate exception thresholds, scoped exception approvals, and conformance outcomes. | Approve exceptional disclosure as normal-flow conformance. |

## Interface assumptions that MUST be settled before prototype implementation
- canonical verifier request fields are defined in the claim profile
- canonical normal-flow proof payload is defined in the claim profile
- exact issuer-resolution rules are accepted in ADR-0007
- `Profile R` holder binding uses `B0` for `V1` and `B1` for `V2`
- status subject and freshness boundaries are accepted in ADR-0011
- minimum verifier audit record is accepted in ADR-0014
- recovery and compromise state domains are defined in the recovery spec

## Demo scenarios
- threshold proof demonstration
- verifier over-collection attempt
- replay or forwarding attempt
- metadata-fingerprinting check
- exception-path warning flow
- recovery or compromise review scenario

## First recovery scenarios
The first prototype acceptance set SHOULD include:
- lost device unconfirmed: wallet or holder reports loss, root state may become `suspended`, verifier receives only generic unavailable or invalid outcome
- confirmed compromised wallet: wallet compromise state becomes `compromised`, affected root state becomes `suspended` or `revoked`, derived proofs fail after state propagation
- issuer trust withdrawal: issuer trust state becomes `withdrawn` or `compromised`, verifiers reject affected derived proofs from trust registry evidence without presentation logs

Each recovery scenario MUST show that issuers and status services do not receive ordinary verifier presentation history.

## Red-path UX boundary
The first prototype MUST document the red-path exceptional flow fields and decision states, but SHOULD NOT build a polished consumer UI.

The documentation-level red path MUST cover:
- exception status
- verifier identity
- verifier class
- extra requested fields
- lawful-basis code and reference
- normal-path insufficiency explanation
- retention period
- audit contact
- review or appeal reference
- holder decision states: `accepted_all`, `accepted_partial`, `refused`, `cancelled`

Consumer UI polish, accessibility testing, localization, and production wallet copy are future implementation work.

## Out of scope
- production mobile wallet
- polished onboarding
- broad identity or KYC features
- production cryptographic integration
