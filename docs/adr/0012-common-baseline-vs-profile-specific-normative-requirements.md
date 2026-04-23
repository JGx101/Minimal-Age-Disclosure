# ADR-0012: Common Baseline Vs Profile-Specific Normative Requirements

## Status
Proposed

## Date
2026-04-23

## Context
The repository publishes both Profile R and Profile P, but it still needs a clean split between common mandatory rules and profile-specific deltas.

## Contradiction being resolved
Without an explicit split, Profile R allowances may silently weaken the common baseline or Profile P research requirements may be mislabeled as universally mandatory.

## Why the specs cannot safely decide this yet
This decision affects:
- normative text structure
- conformance scope
- policy mapping
- prototype interface assumptions

## Options under consideration
- common baseline with small delta sections in each spec
- separate profile annexes
- separate profile-specific spec overlays

## Dependent files and consequences
- all five core specs
- conformance checklist
- privacy-negative tests
- README
- policy pack outline
