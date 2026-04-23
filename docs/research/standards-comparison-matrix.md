# Standards Comparison Matrix

## Purpose
Compare the repository's two technical profiles against the main interoperability and policy directions that matter for minimal age disclosure.

| Model | Main strength | Main limitation | Relevance |
| --- | --- | --- | --- |
| OpenID4VCI + OpenID4VP | strong deployment and interoperability path | privacy depends heavily on profile discipline | foundation for Profile R |
| W3C VC 2.0 + unlinkable derived proof approaches | stronger anti-correlation potential | higher implementation and conformance complexity | foundation for Profile P |
| UK trust-framework style governance | stronger role and assurance governance | does not by itself solve anti-correlation | important governance anchor |
| EU age-verification and wallet direction | clearer threshold-only and wallet-based direction | specific implementation details are still evolving | important interoperability and policy anchor |
| Repository architecture | governance-first, root/derived split, two-profile model | still needs implementation and conformance maturation | target project model |

## Binding mode proof-family note
The normative mapping from `B0`, `B1`, and `B2` to proof families is maintained in `spec/root-derived-proof/root-vs-derived-proof-model.md`.

OpenID4VP and OpenID4VCI are rails for request, issuance, and presentation. They do not by themselves guarantee that verifier-visible binding material is non-correlating.

ISO mdoc, SD-JWT VC, and BBS-style approaches can support different binding modes only when the selected implementation profile preserves the mode-specific correlation boundary.
