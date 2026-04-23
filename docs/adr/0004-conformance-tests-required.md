# ADR-0004: Require privacy-negative and conformance tests

## Status
Proposed

## Date
2026-04-21

## Context
A privacy-preserving profile is weak if verifiers can ignore minimisation principles in practice.

## Decision
The project will include privacy-negative tests and verifier conformance requirements from the beginning.

## Rationale
This pushes the project beyond theory and makes verifier abuse or overreach visible and testable.

## Alternatives considered
- documentation only
- prototype only
- conformance as a later-stage deliverable

## Consequences
### Positive
- stronger credibility
- better demonstration of practical enforceability

### Negative
- more work earlier in the project

## Follow-up actions
- define forbidden requests
- design test cases for overreach and correlation risk
