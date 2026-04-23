# Schemas

This directory exports machine-readable JSON Schema drafts for the canonical objects defined in `spec/claim-profile/age-threshold-proof-profile.md`.

The schemas are conformance aids, not a complete privacy validator. Implementations MUST also apply the normative prose requirements for metadata minimisation, binding mode eligibility, retention, trust resolution, and exception governance.

The repository validator in `tools/validate_fixtures.py` adds checks that JSON Schema alone cannot express cleanly, including duplicate-key rejection, binding-mode eligibility, conformant-fixture forbidden-field scanning, and fixture coverage.
