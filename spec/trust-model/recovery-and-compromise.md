# Recovery and Compromise

## Purpose
Define how loss, theft, compromise, and re-issuance are handled without quietly rebuilding central tracking.

## Working stance
- local-first storage is the default
- optional backup, if any, should minimise operator visibility
- ordinary verification should not depend on recovery infrastructure

## Recovery considerations
- device loss
- wallet compromise
- root credential suspension or renewal
- issuer compromise
- key rotation
- privacy cost of re-issuance

## Design goals
- avoid forcing ordinary live callbacks
- avoid turning recovery into routine usage telemetry
- separate issuer trust state from holder activity state
- make compromise response auditable

## Open implementation note
The repository treats recovery design as a first-class architecture concern, but not yet as a settled implementation decision.
