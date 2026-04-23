# Fixtures

This directory contains documentation-first conformance fixtures. They are examples for review and future automation; they are not production wire formats.

Run the local fixture and schema checks with:

```bash
python tools/validate_fixtures.py
```

## Directories
- `requests/`: canonical verifier request examples.
- `responses/`: canonical derived-proof response examples.
- `conformance/`: scenario and retained-record examples used by checklist and privacy-negative tests.

## Fixture envelope
Each JSON fixture MUST include:
- `fixture_id`
- `kind`
- `profile_ref`
- `expected_conformance`
- `expected_failure_class`
- `object` or `scenario`

Conformant fixtures MUST avoid exact DOB, legal name, document number, document image, stable holder identifier, stable root credential reference, unique status callback URI, and reusable verifier-visible proof-binding artifact.

Non-conformant fixtures deliberately include one or more forbidden fields or patterns and MUST identify the expected failure class.

The validator rejects duplicate JSON keys, checks the fixture envelope, verifies conformant normal request and response invariants, checks conformant fixtures for forbidden normal-flow markers, and confirms that the required fixture coverage exists.
