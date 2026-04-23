#!/usr/bin/env python3
"""Validate documentation fixtures without external dependencies.

This is intentionally a small conformance harness, not a production protocol
validator. It enforces repository invariants that are easy to regress in docs:
duplicate-key rejection, fixture envelope shape, binding-mode eligibility, and
forbidden-field checks for conformant fixtures.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"
SCHEMAS = ROOT / "schemas"

FORBIDDEN_NORMAL_MARKERS = {
    "exact_dob",
    "legal_name",
    "document_number",
    "document_image",
    "stable_holder_identifier",
    "stable_root_credential_reference",
    "unique_status_callback_uri",
    "reusable_proof_binding_artifact",
}

REQUIRED_ENVELOPE = {
    "fixture_id",
    "kind",
    "profile_ref",
    "expected_conformance",
    "expected_failure_class",
}

REQUIRED_NORMAL_REQUEST = {
    "object_type",
    "object_version",
    "profile_ref",
    "verifier_class",
    "requested_threshold",
    "audience",
    "nonce",
    "purpose",
    "policy_ref",
    "jurisdiction_ref",
    "maximum_assurance_bucket",
    "binding_mode",
    "freshness_requirement",
    "exception_requested",
}

REQUIRED_NORMAL_RESPONSE = {
    "object_type",
    "object_version",
    "profile_ref",
    "threshold_result",
    "assurance_bucket",
    "issuer_class",
    "issuer_trust_ref",
    "validity_window",
    "audience_binding",
    "nonce_binding",
    "binding_mode",
    "possession_proof",
    "status_evidence",
    "proof_format_ref",
}

NONCE_RE = re.compile(r"^[A-Za-z0-9_-]{22,}$")


class ValidationError(ValueError):
    pass


def parse_json_strict(path: Path) -> Any:
    def hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        obj: dict[str, Any] = {}
        for key, value in pairs:
            if key in obj:
                raise ValidationError(f"{path}: duplicate JSON key: {key}")
            obj[key] = value
        return obj

    return json.loads(path.read_text(), object_pairs_hook=hook)


def canonicalize_audience(audience: str) -> str:
    parts = urlsplit(audience)
    if parts.scheme.lower() != "https" or not parts.netloc:
        raise ValidationError("audience must be an https URI with a host")
    if parts.query or parts.fragment or parts.username or parts.password:
        raise ValidationError("audience must not include query, fragment, or userinfo")
    host = (parts.hostname or "").lower()
    if not host:
        raise ValidationError("audience host is required")
    port = parts.port
    netloc = host if port in (None, 443) else f"{host}:{port}"
    path = parts.path or "/"
    return urlunsplit(("https", netloc, path, "", ""))


def assert_has_keys(path: Path, obj: dict[str, Any], keys: set[str]) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        raise ValidationError(f"{path}: missing required keys: {', '.join(missing)}")


def validate_normal_request(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_NORMAL_REQUEST)
    if obj["object_type"] != "age_threshold_request":
        raise ValidationError(f"{path}: wrong object_type")
    if obj["object_version"] != "1.0":
        raise ValidationError(f"{path}: unsupported object_version")
    canonicalize_audience(obj["audience"])
    if not NONCE_RE.match(obj["nonce"]):
        raise ValidationError(f"{path}: nonce must be base64url-like and at least 22 chars")
    if obj["exception_requested"] is not False:
        raise ValidationError(f"{path}: normal requests must set exception_requested=false")
    if obj["verifier_class"] == "V1" and obj["binding_mode"] == "B1":
        raise ValidationError(f"{path}: V1 cannot request B1")
    if obj["profile_ref"] == "Profile P" and obj["binding_mode"] != "B2":
        raise ValidationError(f"{path}: Profile P normal flow must use B2")


def validate_normal_response(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_NORMAL_RESPONSE)
    if obj["object_type"] != "age_threshold_response":
        raise ValidationError(f"{path}: wrong object_type")
    if obj["object_version"] != "1.0":
        raise ValidationError(f"{path}: unsupported object_version")
    if obj["profile_ref"] == "Profile P" and obj["binding_mode"] != "B2":
        raise ValidationError(f"{path}: Profile P responses must use B2")
    if obj["audience_binding"] != "present" or obj["nonce_binding"] != "present":
        raise ValidationError(f"{path}: response must bind audience and nonce")
    if obj.get("status_evidence", {}).get("live_issuer_callback_allowed") is not False:
        raise ValidationError(f"{path}: live issuer callback must not be allowed")


def validate_retention_record(path: Path, obj: dict[str, Any]) -> None:
    serialized = json.dumps(obj, sort_keys=True).lower()
    forbidden = [
        "possession_proof",
        "proof_transcript",
        "raw_proof",
        "fine_grained",
        "unique_status",
        "exact_issuer_identity",
    ]
    hits = [marker for marker in forbidden if marker in serialized]
    if hits:
        raise ValidationError(f"{path}: retention record contains forbidden material: {hits}")


def validate_fixture(path: Path) -> None:
    data = parse_json_strict(path)
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: fixture must be a JSON object")
    assert_has_keys(path, data, REQUIRED_ENVELOPE)
    if "object" not in data and "scenario" not in data:
        raise ValidationError(f"{path}: fixture must include object or scenario")
    if data["expected_conformance"] is True and data["expected_failure_class"] is not None:
        raise ValidationError(f"{path}: conformant fixture cannot have a failure class")
    if data["expected_conformance"] is False and not data["expected_failure_class"]:
        raise ValidationError(f"{path}: non-conformant fixture needs a failure class")

    serialized = json.dumps(data, sort_keys=True).lower()
    if data["expected_conformance"] is True:
        hits = sorted(marker for marker in FORBIDDEN_NORMAL_MARKERS if marker in serialized)
        if hits:
            raise ValidationError(f"{path}: conformant fixture contains forbidden markers: {hits}")

    if data["expected_conformance"] is True and data["kind"] == "request":
        validate_normal_request(path, data["object"])
    if data["expected_conformance"] is True and data["kind"] == "response":
        validate_normal_response(path, data["object"])
    if data["expected_conformance"] is True and data["kind"] == "retention_record":
        validate_retention_record(path, data["object"])


def validate_coverage(files: list[Path]) -> None:
    names = {path.name for path in files}
    required = {
        "profile-r-v1-b0-request.json",
        "profile-r-v2-b1-request.json",
        "profile-p-b2-request.json",
        "profile-r-v1-b0-response.json",
        "profile-r-v2-b1-response.json",
        "profile-p-b2-response.json",
        "non-conformant-overcollection-request.json",
        "non-conformant-exception-request.json",
        "non-conformant-reusable-binding-response.json",
        "non-conformant-metadata-fingerprint-response.json",
        "repeated-transaction-b1-same-verifier.json",
        "repeated-transaction-cross-verifier.json",
        "verifier-retention-default-record.json",
        "exception-thresholds-monthly.json",
        "recovery-scenarios.json",
    }
    missing = sorted(required - names)
    if missing:
        raise ValidationError(f"missing required fixture files: {missing}")


def main() -> int:
    schema_files = sorted(SCHEMAS.glob("*.json"))
    fixture_files = sorted(FIXTURES.glob("**/*.json"))
    if not fixture_files:
        raise ValidationError("no fixture JSON files found")
    for path in schema_files:
        parse_json_strict(path)
    for path in fixture_files:
        validate_fixture(path)
    validate_coverage(fixture_files)
    print(f"Validated {len(schema_files)} schemas and {len(fixture_files)} fixtures")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
