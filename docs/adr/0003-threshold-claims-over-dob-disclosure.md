# ADR-0003: Use threshold claims rather than exact DOB disclosure in the normal flow

## Status
Proposed

## Date
2026-04-21

## Context
The project aims to prove age eligibility, not identity. Disclosing exact DOB is often unnecessary.

## Decision
The normal verification path will use threshold claims such as `over_18 = true` rather than exact DOB.

## Rationale
This supports data minimisation and narrows verifier knowledge to what is actually required.

## Alternatives considered
- exact DOB as the normal claim
- exact age in years
- full identity disclosure

## Consequences
### Positive
- stronger privacy
- clearer project thesis
- easier to explain as proportional

### Negative
- some relying parties may still demand stronger evidence or richer metadata

## Follow-up actions
- define assurance metadata
- define exceptional disclosure path governance
