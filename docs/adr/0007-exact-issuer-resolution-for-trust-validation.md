# ADR-0007: Exact Issuer Resolution For Trust Validation

## Status
Proposed

## Date
2026-04-23

## Context
The architecture prefers coarse issuer disclosure by default, but verifiers MUST validate issuer trust before accepting a proof.

## Contradiction being resolved
The repository has not yet decided when issuer class is sufficient and when exact issuer identity becomes mandatory in the normal flow.

## Why the specs cannot safely decide this yet
This decision affects:
- anti-correlation
- verifier trust validation
- Profile R deployability
- metadata minimisation conformance

## Options under consideration
- issuer class is sufficient in the common baseline
- exact issuer identity is always disclosed in Profile R
- exact issuer identity is disclosed only where the applicable trust path requires it

## Dependent files and consequences
- claim profile
- trust model
- metadata minimisation
- conformance checklist
- privacy-negative tests
