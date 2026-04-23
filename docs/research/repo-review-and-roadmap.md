# Repo Review and Roadmap

## Current baseline
The repository now has:
- a layered architecture
- a root credential / derived proof separation
- one governance model with issuer and verifier classes
- a dual-profile structure with `Profile R` and `Profile P`
- explicit conformance, metadata minimisation, recovery, and exception-governance work

## What is solid
- project scope is narrow and coherent
- normal-flow disclosure target is clear
- governance is treated as part of the system
- the repo is publishable as a serious work-in-progress

## What remains open
- exact issuer resolution in the normal flow
- minimum holder-binding mechanism for `Profile R`
- assurance bucket taxonomy
- freshness and validity granularity
- verifier audit minimum
- exception-abuse thresholds

## Roadmap
1. finish normative spec text
2. land ADR stubs for unresolved contradictions
3. tighten conformance and privacy-negative tests
4. refine policy and standards mapping
5. keep prototype planning narrow until interfaces are stable
