# ADR-0009: Canonical Ownership Of The Verifier Request Object

## Status
Proposed

## Date
2026-04-23

## Context
The current docs describe request fields in both the claim profile and verifier policy.

## Contradiction being resolved
The repository needs one canonical owner of the request object schema and one separate owner of request-behavior constraints.

## Why the specs cannot safely decide this yet
Duplicate ownership creates drift across request semantics, conformance mapping, and prototype interface planning.

## Options under consideration
- claim profile owns schema, verifier policy constrains usage
- verifier policy owns schema, claim profile references it
- separate request-object spec

## Dependent files and consequences
- claim profile
- verifier policy
- conformance checklist
- prototype implementation plan
