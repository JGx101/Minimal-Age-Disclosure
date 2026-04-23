# Privacy Test Notes

## Purpose
Privacy tests check whether the architecture preserves minimal disclosure and avoids hidden correlation channels.

## Core negative tests
- exact DOB request
- legal-name request
- document-number request
- stable identifier reuse attempt
- missing nonce or audience binding
- presentation-logging status design
- reusable proof-binding leakage
- `B1` cross-verifier binding leakage
- `B2` verifier-stable binding leakage
- metadata fingerprinting through assurance, issuer, timestamps, policy references, or status references
- recovery flows that create issuer-visible presentation history
- exception-path normalization
- exception requests that exceed review or conformance thresholds

## Source of truth
See `spec/conformance/privacy-negative-test-cases.md`.
