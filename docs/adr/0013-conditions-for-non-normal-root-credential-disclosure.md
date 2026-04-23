# ADR-0013: Conditions For Non-Normal Root Credential Disclosure

## Status
Accepted

## Date
2026-04-23

## Context
The repository treats direct root credential disclosure as non-normal.

## Decision
Direct root credential disclosure is prohibited in normal flow.

Any direct root credential disclosure MUST be treated as exceptional, outside normal-flow conformance, and governed by `spec/verifier-policy/exception-governance.md`.

If a verifier requires root credential disclosure for an ordinary threshold check, the flow MUST be treated as non-conformant.

## Consequences
- The root/derived proof boundary remains hard in normal flow.
- Exceptional root disclosure cannot be used to claim normal-flow conformance.
- Conformance tests can fail ordinary flows that request the root credential.
