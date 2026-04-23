# ADR-0015: Exception-Path Abuse Thresholds And Enforcement

## Status
Proposed

## Date
2026-04-23

## Context
The repository requires the exceptional path to remain outside normal conformance, but it has not yet defined what counts as repeated abuse or what enforcement follows.

## Contradiction being resolved
Without explicit thresholds and enforcement, the exceptional path can become the commercial default while the repo still claims minimal disclosure.

## Why the specs cannot safely decide this yet
This decision affects:
- verifier governance
- conformance scoring
- policy legitimacy
- public credibility of the minimal-disclosure claim

## Options under consideration
- fixed review threshold for repeated exceptional use
- verifier-class-specific thresholds
- qualitative governance review without numeric threshold

## Dependent files and consequences
- exception governance
- verifier policy
- conformance checklist
- privacy-negative tests
- policy pack outline
