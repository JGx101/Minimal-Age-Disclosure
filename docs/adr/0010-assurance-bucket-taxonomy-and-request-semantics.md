# ADR-0010: Assurance Bucket Taxonomy And Request Semantics

## Status
Proposed

## Date
2026-04-23

## Context
The architecture requires bounded assurance metadata, but the taxonomy and verifier consumption rules are not yet fixed.

## Contradiction being resolved
The repository has not decided how coarse assurance may be while remaining useful for verifier policy and standards legibility.

## Why the specs cannot safely decide this yet
This decision affects:
- metadata minimisation
- verifier requests
- UK/EU mapping
- conformance repeatability

## Options under consideration
- small common assurance bucket set
- profile-specific assurance buckets
- coarse baseline plus profile-specific extension semantics

## Dependent files and consequences
- claim profile
- trust model
- metadata minimisation
- conformance checklist
- privacy-negative tests
