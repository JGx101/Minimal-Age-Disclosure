# ADR-0007: Exact Issuer Resolution For Trust Validation

## Status
Accepted

## Date
2026-04-23

## Context
The architecture prefers coarse issuer disclosure by default, but verifiers MUST validate issuer trust before accepting a proof.

## Decision
Normal-flow issuer disclosure MUST default to issuer class plus a minimised `issuer_trust_ref`.

Exact issuer identity MAY be resolved only where issuer class and `issuer_trust_ref` are insufficient for the applicable trust-validation path.

If exact issuer identity is used for trust validation, the verifier MUST NOT retain it as a default verifier identifier unless retention is explicitly justified by verifier compliance rules.

## Consequences
- The trust model can support deployable trust validation without making exact issuer identity the default disclosure.
- Metadata minimisation treats exact issuer identity as privacy-sensitive.
- Conformance tests must check whether exact issuer disclosure is necessary and whether default retention is justified.
