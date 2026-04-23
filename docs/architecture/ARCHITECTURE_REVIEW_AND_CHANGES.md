# Architecture Review and Changes

## Purpose
This document records why the repository architecture was revised and what changed.

## Starting point
The earlier repository pass did several useful things:
- moved the project into a publishable GitHub shape
- made minimal age disclosure the public framing
- adopted a root credential / derived proof model
- centered normal-flow requests on threshold, audience, nonce, and minimal policy context
- pushed for short-lived credentials, no stable holder identifier, and optional batched status

That was a strong baseline, but it still flattened several hard tensions into one clean topology.

## Main architecture gaps found

### 1. Holder binding versus anti-correlation
The earlier model expected verifier-visible binding evidence in the response while also rejecting stable holder identifiers. The current architecture resolves this by defining `B0`, `B1`, and `B2` binding modes, each with explicit anti-correlation boundaries.

### 2. Short-lived credentials versus issuer observability
Short-lived credentials help reduce status lookups, but frequent re-issuance can make the issuer a de facto activity checkpoint. The earlier model did not clearly separate root credential lifecycle from verifier-facing proof lifecycle.

### 3. Narrow metadata versus metadata fingerprinting
Even if identity attributes are removed, assurance references, detailed timestamps, exact issuer identity, proof-binding artifacts, and policy identifiers can still act as correlators. The earlier model did not yet treat metadata minimisation as a full design discipline.

### 4. Wallet refusal versus real verifier restraint
Wallet UX and privacy-negative tests are necessary, but not enough. Without verifier obligations, retention limits, and sanctionable non-conformance, a verifier can still operationally force disclosure.

### 5. Exception separation versus exception normalisation
The earlier model separated the exceptional path conceptually, but did not yet define when exceptions are lawful, how they are audited, or how repeated exception use is treated as abuse.

### 6. Recovery and compromise were too thin
Device loss, wallet compromise, issuer compromise, and re-issuance privacy tradeoffs were acknowledged, but not built into the architecture as first-class concerns.

### 7. One topology was carrying too much
The earlier pass implicitly asked one flat topology to satisfy both deployment-friendly interoperability and stronger privacy-maximal ambitions. The research supports a dual-profile approach under one governance model instead.

## Architecture changes made

## Change 1: move from a flat topology to a layered model
The repository now describes six planes:
1. governance plane
2. root credential plane
3. derived proof plane
4. verification plane
5. status and recovery plane
6. exception plane

This makes it easier to reason about tradeoffs without pretending one diagram solves everything.

## Change 2: harden the root credential / derived proof split
The root credential is now explicitly a wallet-side artifact.
It is not the normal verifier-facing artifact.

The derived proof is transaction-bound and policy-scoped.
This lets the project reason separately about:
- issuer evidence checking
- root credential lifecycle
- verifier-facing proof disclosure
- re-issuance and status tradeoffs

## Change 3: make proof-binding a first-class design problem
The architecture now states plainly that holder binding must not collapse into a reusable verifier-visible key unless that tradeoff is explicitly accepted and documented.

This is now treated as a central open issue rather than an implementation detail.

## Change 4: add metadata minimisation as its own normative area
The repository now treats metadata minimisation as broader than "do not reveal DOB".
It now includes:
- assurance bucketing
- issuer abstraction where possible
- bounded validity information
- timestamp coarsening
- request policy discipline
- proof-binding artifact discipline

## Change 5: strengthen verifier governance
Verifier restraint is no longer treated as wallet UX alone.
The revised model adds:
- verifier classes
- non-conformant request definitions
- compliance and retention rules
- audit expectations
- exception abuse review thresholds

## Change 6: separate common governance from technical profiles
The repository now has:
- one common governance model
- Profile R for regulator-ready and interoperable deployment work
- Profile P for privacy-maximal and research-oriented work

This keeps deployment pragmatism and stronger privacy experimentation in one coherent project without pretending they are identical.

## Change 7: promote recovery and compromise into the core model
Recovery and compromise are now part of the architecture, not just edge notes.
The revised model covers:
- local-first recovery stance
- wallet compromise state
- root credential suspension or renewal
- issuer compromise response
- re-issuance privacy tradeoffs

## Revised architecture stance
The repository now frames the normal flow as:

issuer -> root credential in wallet -> wallet derives transaction-bound threshold proof -> verifier validates minimal result under governed policy

That is a more faithful model of the privacy and governance tensions than the earlier flat formulation.

## Design consequences
The updated repository therefore:
- keeps the project narrow
- keeps GitHub readability
- treats anti-correlation as the main systems problem
- avoids pretending short-lived credentials alone solve privacy
- avoids pretending transport standards alone solve governance
- keeps room for both interoperable and privacy-maximal technical profiles

## What this means for the rest of the repo
Any future architecture, spec, or prototype work should now be checked against this review before being treated as canonical.
