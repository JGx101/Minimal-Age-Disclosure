# Verifier Compliance and Retention

## Status
Draft

## 1. Purpose
This specification defines minimum verifier retention, prohibited retention, and telemetry limits for the minimal age-disclosure architecture.

## 2. Default retained fields
By default, a verifier MAY retain only:
- decision outcome
- an approved coarse time bucket, where needed
- policy reference
- bounded audit reason

## 3. Forbidden default retention
By default, a verifier MUST NOT retain:
- raw proof payload
- stable holder data
- reusable proof-binding artifacts
- fine-grained timestamps beyond approved granularity
- telemetry sufficient to recreate holder activity history

## 4. Exceptional retention
Retention beyond the default minimum MAY occur only where:
- an explicit legal or governance basis exists
- the retention scope is bounded
- the event is auditable

The exact minimum audit record and exceptional-retention boundary remain subject to [ADR-0014](../../docs/adr/0014-verifier-audit-record-minimum.md).

## 5. Telemetry rule
For conformance purposes, telemetry includes any recorded fields or derived analytics that can reconstruct holder activity patterns beyond the documented governance need.

## 6. Conformance rule
A verifier that retains raw proof payloads, reusable binding artifacts, or correlating telemetry by default MUST be treated as non-conformant.
