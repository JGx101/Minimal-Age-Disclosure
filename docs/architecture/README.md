# Architecture Docs

This section contains the canonical visual and narrative architecture for the repository.

## Contents
- [Architecture Overview](ARCHITECTURE_OVERVIEW.md)
- [Flows and Topology](FLOWS_AND_TOPOLOGY.md)
- [Governance and Controls](GOVERNANCE_AND_CONTROLS.md)
- [Dual Profile Overview](DUAL_PROFILE_OVERVIEW.md)
- [Potential Final State](POTENTIAL_FINAL_STATE.md)

## Diagram conventions
- Mermaid is the source format for all diagrams.
- The normal flow always separates the root credential plane from the derived proof plane.
- The exceptional path is always shown as a distinct governance boundary.
- No normal-flow diagram should imply disclosure of exact DOB, legal name, document number, document image, or a stable verifier-visible identifier.
