# Project Brief

## Working title
Minimal Age Disclosure

## Mission
Design a privacy-preserving age-threshold proof system that lets a holder prove they meet a threshold such as `18+` without disclosing identity, exact date of birth, or a reusable cross-site identifier.

## Strategic aim
Produce a standards-grade project that can serve as:
- an interoperable profile direction for age-threshold proof
- a governance and conformance model for verifier restraint
- a privacy-maximal research track for stronger anti-correlation
- a serious public technical and policy contribution

## Problem statement
Many age-verification systems behave as identity-collection systems with an age check attached. That creates privacy, security, function-creep, and tracking risks.

This project aims to define a narrower and more defensible model:
prove age-threshold facts, not identity.

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

## Success criteria
The project is successful if it demonstrates:
1. threshold-only proof is practical
2. verifier behavior can be constrained by architecture and governance
3. anti-correlation is treated as a first-class technical problem
4. binding, metadata minimisation, recovery, compromise, and exception handling are explicitly designed
5. one common governance model can support both an interoperable profile and a privacy-maximal research track
6. the repository is strong enough to publish and discuss seriously with practitioners, standards groups, and policy stakeholders
