# Conformance Test Notes

## Purpose
Conformance tests check whether issuer, wallet, verifier, and ecosystem behavior matches the repository's canonical governance and profile rules.

## Core focus areas
- root credential stays local in the normal flow
- derived proof is transaction-bound
- verifier request object is conformant
- trust, nonce, and audience binding are enforced
- retention rules are respected
- exception handling remains outside normal conformance

## Source of truth
See `spec/conformance/conformance-checklist.md`.
