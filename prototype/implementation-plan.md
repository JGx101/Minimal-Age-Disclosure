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

## Out of scope
- production mobile wallet
- polished onboarding
- broad identity or KYC features
- production cryptographic integration
