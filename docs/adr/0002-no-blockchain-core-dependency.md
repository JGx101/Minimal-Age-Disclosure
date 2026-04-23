# ADR-0002: Do not make blockchain a core dependency in v1

## Status
Proposed

## Date
2026-04-21

## Context
The initial idea included blockchain as a possible trust or proof layer. Public ledgers can increase transparency and auditability, but they can also introduce permanence and correlation risks.

## Decision
Do not make blockchain a core dependency for v1. Any blockchain use must be justified in a later ADR with a narrow and privacy-compatible purpose.

## Rationale
The primary value of the project is minimum-disclosure age proof, not tokenisation or public-ledger anchoring. Standards-aligned credential systems do not require blockchain to function.

## Alternatives considered
- public blockchain trust registry
- private consortium blockchain
- blockchain-free trust registry and key distribution

## Consequences
### Positive
- clearer privacy story
- lower complexity
- less ideological distraction

### Negative
- loses a potential auditability or transparency mechanism unless reintroduced narrowly

## Follow-up actions
- document non-blockchain trust registry options
- revisit only if a compelling narrow use case appears
