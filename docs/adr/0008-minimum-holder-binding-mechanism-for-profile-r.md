# ADR-0008: Minimum Holder-Binding Mechanism For Profile R

## Status
Proposed

## Date
2026-04-23

## Context
The architecture requires transaction-bound rightful possession while rejecting stable verifier-visible holder identifiers in the normal flow.

## Contradiction being resolved
The repository has not yet chosen the minimum acceptable Profile R holder-binding mechanism.

## Why the specs cannot safely decide this yet
This decision affects:
- replay resistance
- anti-correlation
- conformance pass/fail rules
- prototype interface planning

## Options under consideration
- pairwise verifier-bound holder key
- one-time or transaction-specific holder proof artifact
- another bounded pragmatic mechanism documented as a Profile R tradeoff

## Dependent files and consequences
- claim profile
- root-vs-derived proof model
- metadata minimisation
- conformance checklist
- privacy-negative tests
- prototype implementation plan
