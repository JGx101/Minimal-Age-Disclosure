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
- binding modes, metadata coarsening, recovery state, and exception thresholds are now specified
- the repo is publishable as a serious work-in-progress

## Recently resolved
- exact issuer resolution defaults to issuer class plus minimised trust reference
- `B0`, `B1`, and `B2` define the binding taxonomy
- `AB1`, `AB2`, and `AB3` define the assurance bucket taxonomy
- freshness attaches to issuer trust, root credential, or wallet compromise state
- verifier audit minimum and exception-abuse thresholds are specified
- normal-flow metadata anti-fingerprinting is now a conformance boundary

## Roadmap
1. review accepted interfaces against prototype feasibility
2. convert privacy-negative tests into fixture-backed checks
3. tighten profile-specific conformance deltas
4. refine policy and standards mapping
5. keep production implementation out of scope until prototype assumptions are validated
