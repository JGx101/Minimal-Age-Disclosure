# Project Brief

## Working title
Minimal Age Disclosure

## One-paragraph summary
This repository defines a privacy-preserving age-threshold proof model in which a holder proves a fact such as `18+` without routinely disclosing identity, exact date of birth, or a reusable cross-site identifier. The design goal is narrow disclosure: prove age threshold facts, not identity.

## Current project status
- Status: documentation-first architecture, policy, and conformance project
- Maturity: strong baseline published, several architecture decisions still open before implementation
- Build posture: prototype remains intentionally documentation-only until privacy-critical interfaces stabilise
- Primary framing: minimal age disclosure with anti-correlation and verifier restraint treated as first-class requirements

## Why this repo exists
Many age-checking systems drift into identity collection. That creates privacy, security, function-creep, and tracking risk that is not required for the core user need.

This project is a narrower alternative:
- prove threshold eligibility
- minimise routine disclosure
- constrain verifier behaviour
- keep exceptional disclosure outside the normal path and under governance

## What this project is trying to produce
The repository is intended to become a credible public project for practitioners, standards groups, and policy stakeholders. It aims to provide:
- an interoperable profile direction for age-threshold proof
- a governance and conformance model for verifier restraint
- a privacy-maximal research track for stronger anti-correlation
- a clear public record of open tradeoffs and unresolved decisions

## Core architectural stance
The project uses a layered model rather than a single flat topology:
- governance plane
- root credential plane
- derived proof plane
- verification plane
- status and recovery plane
- exception plane

The normal flow is:
issuer -> root credential in wallet -> wallet derives transaction-bound proof -> verifier validates minimal result under governed policy

Normal flow does not imply routine disclosure of exact DOB, legal name, document number, document image, or a stable verifier-visible holder identifier.

## Repository guide for newcomers
Start here if you are new to the project:

1. `PROJECT_BRIEF.md`
2. `REQUIREMENTS.md`
3. `THREAT_MODEL_SEED.md`
4. `docs/architecture/README.md`
5. `spec/claim-profile/age-threshold-proof-profile.md`
6. `spec/verifier-policy/minimal-disclosure-verifier-policy.md`
7. `BACKLOG.md`
8. `OPEN_QUESTIONS.md`

Useful supporting areas:
- `docs/adr/` for major design decisions and unresolved tradeoffs
- `spec/conformance/` for baseline checklist and privacy-negative tests
- `docs/policy/` for governance and external-facing policy material
- `prototype/` for implementation planning only

## Primary outputs
- architecture overview and topology diagrams
- normative claim profile
- normative verifier policy
- trust model
- root-vs-derived proof model
- metadata minimisation rules
- recovery and compromise model
- conformance checklist and privacy-negative tests
- policy and governance materials
- prototype implementation plan

## Non-goals
- a general identity wallet
- a broad KYC platform
- a production mobile wallet
- strong biometric person-binding in v1
- a public-blockchain-centric design
- treating technical feasibility as identical to regulatory acceptance

## What counts as progress
Progress in this repo means moving toward a publishable, testable, privacy-defensible baseline. In practice that means:
- reducing ambiguity in normal-flow data disclosure
- documenting governance boundaries for verifier behaviour
- resolving ADR-backed blockers
- converting open questions into stable normative requirements
- improving conformance coverage for privacy failure modes

## Success criteria
The project is successful if it demonstrates:
1. threshold-only proof is practical
2. verifier behaviour can be constrained by architecture and governance
3. anti-correlation is treated as a first-class technical problem
4. binding, metadata minimisation, recovery, compromise, and exception handling are explicitly designed
5. one common governance model can support both an interoperable profile and a privacy-maximal research track
6. the repository is strong enough to publish and discuss seriously with practitioners, standards groups, and policy stakeholders
