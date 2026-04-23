# Source Pack and Research Corpus

Use this file to guide research and keep the project grounded in the right source material.

## A. Core standards and specifications
1. OpenID4VP
   - purpose: presentation protocol between holder and verifier

2. OpenID4VCI
   - purpose: credential issuance protocol between issuer and holder

3. W3C Verifiable Credentials Data Model 2.0
   - purpose: credential data model and semantic baseline

4. W3C VC Bitstring Status List or equivalent status models
   - purpose: status and revocation pattern analysis

5. Relevant selective disclosure or privacy-preserving credential profiles
   - purpose: evaluate minimal disclosure and anti-correlation options

6. OpenID or related subject and identifier minimisation material
   - purpose: assess pairwise, ephemeral, and no-identifier presentation options

## B. UK policy and trust material
1. UK Digital Verification Services Trust Framework
   - purpose: roles, governance, conformance expectations

2. UK digital identity and attribute service guidance
   - purpose: attribute-oriented proofing context

3. Ofcom age assurance guidance and Online Safety Act materials
   - purpose: what counts as effective age checks in practice

4. ICO age assurance and privacy guidance
   - purpose: minimisation, necessity, proportionality, data protection alignment

5. OfDIA and related UK digital verification ecosystem materials
   - purpose: certification and market structure awareness

## C. EU policy and implementation material
1. EU age-verification blueprint and ageverification.dev materials
   - purpose: current Commission-backed approach

2. EUDI Wallet architecture, implementing acts, and technical references
   - purpose: interoperability context

3. ETSI age-verification requirements and standards mapping
   - purpose: European standardisation landscape

4. eIDAS 2.0 and related wallet-attestation materials
   - purpose: ecosystem and governance context

## D. Research themes
1. unlinkability and correlation resistance
2. privacy-preserving revocation and status
3. pairwise, ephemeral, or absent verifier-visible identifiers
4. short-lived credentials vs revocation lists
5. person-binding tradeoffs
6. verifier conformance and anti-abuse controls
7. assurance levels for age attributes
8. wallet UX for transparent disclosure
9. metadata minimisation and anti-fingerprinting
10. recovery and compromise without presentation logging

## E. Research note template
For each source, capture:
- title
- organisation or author
- date
- source type
- why it matters
- direct relevance to this project
- maturity or authority
- implications for the common model
- implications for Profile R
- implications for Profile P
- open questions raised

## F. Research discipline rules
- distinguish standards from vendor marketing
- distinguish live regulation from consultation-stage material
- distinguish technical capability from likely political acceptance
- do not assume "privacy-preserving" claims are actually anti-correlation-safe
- do not treat transport standards as proof that privacy policy is solved
- record disagreements between sources explicitly
- track where a source helps with governance, cryptography, recovery, or verifier restraint

## G. Initial comparison questions
- What is already solved by current rails?
- What privacy gaps remain in real deployments?
- What is the narrowest viable profile for age-threshold proof?
- Where do UK and EU approaches differ materially?
- Which features belong in v1 vs future versions?
- Which metadata fields are still dangerous even after identity attributes are removed?
- What are the strongest recovery and compromise patterns that do not recreate central tracking?
