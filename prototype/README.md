# Prototype Overview

## Purpose
The prototype is intended to demonstrate the repository's root credential / derived proof architecture, not to act as a production identity system.

## Intended components
- mock issuer
- wallet simulator
- verifier demo
- trust-registry mock
- optional batched status mock for issuer or root state

## Required properties
- root credential remains local in the normal flow
- wallet derives a transaction-bound proof per verifier request
- verifier receives only the bounded normal-flow disclosure set
- forbidden requests and exception flows are visible in the demo

## Main reference
See [implementation-plan.md](implementation-plan.md).
