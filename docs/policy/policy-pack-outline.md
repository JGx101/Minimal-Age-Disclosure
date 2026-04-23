# Policy Pack Outline

## Purpose
Define the policy-facing documentation set that will sit alongside the normative architecture and conformance materials.

## Core outputs
- UK mapping note
- EU mapping note
- DPIA-style analysis
- assurance and issuer-governance note
- standards submission note

## Required themes
All policy outputs SHOULD preserve the following themes:
- purpose limitation
- normal-flow minimal disclosure
- verifier restraint
- anti-correlation and metadata minimisation
- trust-registry data limits
- exception governance
- recovery and compromise handling
- technical feasibility versus regulatory acceptance

## Profile framing
The policy pack MUST distinguish:
- the common baseline
- `Profile R` as the interoperable and deployment-oriented path
- `Profile P` as the research-oriented privacy-maximal path

The policy pack MUST NOT present `Profile P` as current deployment consensus.

## Guardrails
The policy pack SHOULD make clear that:
- privacy claims require concrete technical controls
- governance claims require obligations, audit, and conformance consequences
- UK and EU mapping require legibility on roles, assurance, proportionality, and audit
- technical minimal disclosure alone does not guarantee regulatory acceptance

## Source categories for UK and EU mapping
Policy mapping MUST cite source categories rather than claim regulatory approval.

UK-facing material SHOULD cite and distinguish:
- UK digital identity and attributes trust framework material, including DVS-style certification and role guidance where relevant
- ICO age assurance, data protection, proportionality, and DPIA guidance
- Ofcom Online Safety Act and age assurance guidance where relevant to verifier duties
- UK sector-specific rules only where the use case explicitly depends on them

EU-facing material SHOULD cite and distinguish:
- eIDAS 2.0 and EUDI Wallet architecture, implementing act, and ARF material
- EU age-verification blueprint or equivalent official age-verification reference material
- European Data Protection Board or supervisory authority guidance relevant to data minimisation, purpose limitation, and age assurance
- ETSI, CEN/CENELEC, or other standards material only where it directly constrains the trust or assurance model

Standards-facing material SHOULD cite and distinguish:
- OpenID4VCI and OpenID4VP specifications for interoperable rails
- W3C Verifiable Credentials Data Model material where used for `Profile P`
- selective-disclosure and anonymous-credential proof-family specifications or drafts only as technical candidates, not as policy endorsement

The policy pack MUST NOT imply that the project is certified, regulator-approved, or production-authorised until an appropriate external body confirms that status.

## Exception governance validation
Policy mapping MUST explain that the `5%` review threshold and `10%` conformance-failure threshold are evaluated against monthly verifier age-check volume as defined in `spec/verifier-policy/exception-governance.md`.

Scoped exception approval MUST be described as a time-limited governance control with independent review, evidence package, expiry, and re-review. It MUST NOT be described as a route for making exceptional disclosure normal.
