# ADR-0013: Conditions For Non-Normal Root Credential Disclosure

## Status
Proposed

## Date
2026-04-23

## Context
The repository treats direct root credential disclosure as non-normal, but it has not yet defined whether any such disclosure is ever permitted and under what governance rules.

## Contradiction being resolved
The architecture needs a clear boundary between “never allowed” and “allowed only under separately governed exceptional conditions.”

## Why the specs cannot safely decide this yet
This decision affects:
- exceptional governance
- verifier policy
- root-vs-derived proof model
- prototype interface assumptions

## Options under consideration
- root credential disclosure prohibited in all profiles
- root credential disclosure permitted only in exceptional flow
- profile-specific non-normal disclosure rules with explicit sanctions

## Dependent files and consequences
- root-vs-derived proof model
- verifier policy
- exception governance
- conformance checklist
- prototype implementation plan
