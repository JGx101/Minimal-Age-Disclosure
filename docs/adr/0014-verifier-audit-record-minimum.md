# ADR-0014: Verifier Audit Record Minimum

## Status
Proposed

## Date
2026-04-23

## Context
The governance model requires meaningful audit and sanctions, but the privacy model requires minimal verifier retention.

## Contradiction being resolved
The repository has not yet fixed the smallest retained evidence set that still supports audit and enforcement.

## Why the specs cannot safely decide this yet
This decision affects:
- verifier retention limits
- telemetry boundaries
- exception audit records
- conformance pass/fail behavior

## Options under consideration
- decision outcome plus bounded audit reason only
- decision outcome plus coarse time bucket plus policy reference
- class-dependent audit minimums

## Dependent files and consequences
- verifier compliance and retention
- exception governance
- conformance checklist
- privacy-negative tests
- prototype implementation plan
