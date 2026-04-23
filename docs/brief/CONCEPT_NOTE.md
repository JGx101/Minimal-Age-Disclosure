# Concept Note

## Working title
Minimal Age Disclosure

## Core proposition
This project defines a privacy-preserving age-threshold proof architecture in which a holder can prove a threshold fact such as `over_18 = true` without disclosing identity, exact date of birth, or a reusable cross-site identifier.

## Problem
Many age-assurance deployments still collect more identity data than the transaction requires. This creates unnecessary privacy, security, and governance risk.

## Architectural response
The project uses a root credential / derived proof split:
- an issuer verifies evidence once and issues a root credential
- the wallet stores the root credential locally
- the wallet derives a transaction-bound proof for each verifier interaction
- the verifier receives only the minimal threshold result and bounded supporting metadata

## Governance stance
The project is not only a protocol profile. It is also:
- a verifier-restraint model
- a conformance model
- an exception-governance model

## Technical profiles
The repository publishes:
- `Profile R`: a regulator-ready / interoperable profile
- `Profile P`: a privacy-maximal / research profile

## Core claim
The main technical problem is anti-correlation, not just transport selection. The design therefore treats metadata minimisation, verifier retention limits, and exception governance as first-class requirements.
