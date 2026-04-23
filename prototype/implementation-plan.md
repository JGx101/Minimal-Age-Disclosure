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
- canonical verifier request fields
- canonical normal-flow proof payload
- exact issuer-resolution rules
- approved Profile R holder-binding mechanism
- status subject and freshness boundaries
- minimum verifier audit record
- recovery and compromise interface assumptions

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
