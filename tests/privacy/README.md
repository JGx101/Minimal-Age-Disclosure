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
- reusable holder-binding leakage
- exception-path normalization

## Source of truth
See `spec/conformance/privacy-negative-test-cases.md`.
