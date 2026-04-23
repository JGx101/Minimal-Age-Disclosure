#!/usr/bin/env python3
"""Validate documentation fixtures without external dependencies.

This is a documentation conformance harness, not a production protocol validator.
It catches regressions that JSON Schema and prose often miss: duplicate keys,
canonical object shape, profile/binding eligibility, nested response invariants,
metadata anti-fingerprinting, refusal/error hygiene, retention leakage, and
negative-fixture coverage.
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

ALLOWED_PROFILES = {"Profile R", "Profile P"}
ALLOWED_ENVELOPE_PROFILES = ALLOWED_PROFILES | {"COMMON"}
ALLOWED_THRESHOLDS = {"over_13", "over_16", "over_18", "over_21"}
ALLOWED_VERIFIER_CLASSES = {"V1", "V2", "VX"}
ALLOWED_BINDING_MODES = {"B0", "B1", "B2"}
ALLOWED_ASSURANCE_BUCKETS = {"AB1", "AB2", "AB3"}
ALLOWED_FRESHNESS = {"none", "issuer_trust_state", "root_credential_state", "wallet_compromise_state"}
ALLOWED_ISSUER_CLASSES = {"A0", "A1", "A2"}
ALLOWED_TRUST_RESOLUTION = {"trust_list", "trust_registry", "cryptographic_accumulator", "governance_profile"}
ALLOWED_STATUS_TYPES = {"none", "batched_status", "cacheable_status", "relayable_status", "issuer_trust_state", "root_credential_state", "wallet_compromise_state"}
ALLOWED_PROOF_FAMILIES = {"openid4vp", "sd_jwt_vc", "mdoc", "bbs", "cl_signature", "zk_profile", "other_governed"}
ALLOWED_CORRELATION_SCOPES = {"none", "verifier_transaction", "verifier_scoped"}

FORBIDDEN_NORMAL_MARKERS = {
    "exact_dob", "date_of_birth", "birthdate", "legal_name", "document_number",
    "document_image", "passport_number", "driving_licence_number",
    "national_insurance_number", "stable_holder_identifier", "stable_root_credential_reference",
    "unique_status_callback_uri", "reusable_proof_binding_artifact", "holder_id",
    "credential_id", "root_credential_id",
}
FORBIDDEN_NORMAL_RESPONSE_KEYS = FORBIDDEN_NORMAL_MARKERS | {
    "raw_evidence", "evidence_source", "proof_transcript", "raw_proof", "exact_age", "age_band",
}

REQUIRED_ENVELOPE = {"fixture_id", "kind", "profile_ref", "expected_conformance", "expected_failure_class"}
REQUIRED_NORMAL_REQUEST = {"object_type", "object_version", "profile_ref", "verifier_class", "requested_threshold", "audience", "nonce", "purpose", "policy_ref", "jurisdiction_ref", "maximum_assurance_bucket", "binding_mode", "freshness_requirement", "exception_requested"}
REQUIRED_NORMAL_RESPONSE = {"object_type", "object_version", "profile_ref", "threshold_result", "assurance_bucket", "issuer_class", "issuer_trust_ref", "validity_window", "audience_binding", "nonce_binding", "binding_mode", "possession_proof", "status_evidence", "proof_format_ref"}
REQUIRED_THRESHOLD_RESULT = {"threshold", "satisfied", "result_code"}
REQUIRED_ISSUER_TRUST_REF = {"trust_framework_ref", "trust_resolution_method", "exact_issuer_disclosed"}
REQUIRED_VALIDITY_WINDOW = {"granularity", "valid_until", "freshness_requirement_satisfied"}
REQUIRED_STATUS_EVIDENCE = {"status_check_type", "live_issuer_callback_allowed"}
REQUIRED_PROOF_FORMAT_REF = {"proof_family", "profile_id", "correlation_scope"}

NONCE_RE = re.compile(r"^[A-Za-z0-9_-]{22,}$")
VERSION_RE = re.compile(r"^[1-9][0-9]*\.[0-9]+$")
PURPOSE_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,63}$")
POLICY_REF_RE = re.compile(r"^(policy|trust):[A-Za-z0-9][A-Za-z0-9:._/-]{2,127}$")
JURISDICTION_RE = re.compile(r"^[A-Z]{2}(-[A-Z0-9]{1,3})?$")
DATE_BUCKET_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
HOUR_BUCKET_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:00Z$")
REF_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:._/-]{2,159}$")


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
    if not isinstance(audience, str):
        raise ValidationError("audience must be a string")
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
    return urlunsplit(("https", netloc, parts.path or "/", "", ""))


def assert_has_keys(path: Path, obj: dict[str, Any], keys: set[str]) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        raise ValidationError(f"{path}: missing required keys: {', '.join(missing)}")


def assert_only_keys(path: Path, obj: dict[str, Any], allowed: set[str], context: str) -> None:
    extra = sorted(set(obj) - allowed)
    if extra:
        raise ValidationError(f"{path}: unexpected {context} keys: {', '.join(extra)}")


def assert_enum(path: Path, value: Any, allowed: set[str], field: str) -> None:
    if value not in allowed:
        raise ValidationError(f"{path}: invalid {field}: {value!r}")


def assert_string_match(path: Path, value: Any, pattern: re.Pattern[str], field: str) -> None:
    if not isinstance(value, str) or not pattern.match(value):
        raise ValidationError(f"{path}: invalid {field}: {value!r}")


def assert_no_forbidden_keys_recursive(path: Path, obj: Any, forbidden: set[str], context: str) -> None:
    if isinstance(obj, dict):
        hits = sorted(str(key) for key in obj if str(key).lower() in forbidden)
        if hits:
            raise ValidationError(f"{path}: forbidden {context} keys: {hits}")
        for value in obj.values():
            assert_no_forbidden_keys_recursive(path, value, forbidden, context)
    elif isinstance(obj, list):
        for value in obj:
            assert_no_forbidden_keys_recursive(path, value, forbidden, context)


def assert_no_forbidden_markers(path: Path, obj: Any) -> None:
    serialized = json.dumps(obj, sort_keys=True).lower()
    hits = sorted(marker for marker in FORBIDDEN_NORMAL_MARKERS if marker in serialized)
    if hits:
        raise ValidationError(f"{path}: conformant fixture contains forbidden markers: {hits}")


def validate_normal_request(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_NORMAL_REQUEST)
    assert_only_keys(path, obj, REQUIRED_NORMAL_REQUEST, "normal request")
    if obj["object_type"] != "age_threshold_request":
        raise ValidationError(f"{path}: wrong object_type")
    if obj["object_version"] != "1.0" or not VERSION_RE.match(obj["object_version"]):
        raise ValidationError(f"{path}: unsupported object_version")
    assert_enum(path, obj["profile_ref"], ALLOWED_PROFILES, "profile_ref")
    assert_enum(path, obj["verifier_class"], ALLOWED_VERIFIER_CLASSES, "verifier_class")
    assert_enum(path, obj["requested_threshold"], ALLOWED_THRESHOLDS, "requested_threshold")
    assert_enum(path, obj["maximum_assurance_bucket"], ALLOWED_ASSURANCE_BUCKETS, "maximum_assurance_bucket")
    assert_enum(path, obj["binding_mode"], ALLOWED_BINDING_MODES, "binding_mode")
    assert_enum(path, obj["freshness_requirement"], ALLOWED_FRESHNESS, "freshness_requirement")
    canonicalize_audience(obj["audience"])
    assert_string_match(path, obj["nonce"], NONCE_RE, "nonce")
    assert_string_match(path, obj["purpose"], PURPOSE_RE, "purpose")
    assert_string_match(path, obj["policy_ref"], POLICY_REF_RE, "policy_ref")
    assert_string_match(path, obj["jurisdiction_ref"], JURISDICTION_RE, "jurisdiction_ref")
    if obj["exception_requested"] is not False:
        raise ValidationError(f"{path}: normal requests must set exception_requested=false")
    if obj["verifier_class"] == "V1" and obj["binding_mode"] == "B1":
        raise ValidationError(f"{path}: V1 cannot request B1")
    if obj["binding_mode"] == "B1" and obj["verifier_class"] not in {"V2", "VX"}:
        raise ValidationError(f"{path}: B1 requires V2 or VX verifier class")
    if obj["profile_ref"] == "Profile P" and obj["binding_mode"] != "B2":
        raise ValidationError(f"{path}: Profile P normal flow must use B2")
    assert_no_forbidden_keys_recursive(path, obj, FORBIDDEN_NORMAL_RESPONSE_KEYS, "normal request")


def validate_threshold_result(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_THRESHOLD_RESULT)
    assert_only_keys(path, obj, REQUIRED_THRESHOLD_RESULT, "threshold_result")
    assert_enum(path, obj["threshold"], ALLOWED_THRESHOLDS, "threshold_result.threshold")
    if not isinstance(obj["satisfied"], bool):
        raise ValidationError(f"{path}: threshold_result.satisfied must be boolean")
    expected = "threshold_satisfied" if obj["satisfied"] else "threshold_not_satisfied"
    if obj["result_code"] != expected:
        raise ValidationError(f"{path}: result_code must be {expected} when satisfied={obj['satisfied']}")


def validate_issuer_trust_ref(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_ISSUER_TRUST_REF)
    assert_only_keys(path, obj, REQUIRED_ISSUER_TRUST_REF | {"trust_list_entry_ref"}, "issuer_trust_ref")
    assert_string_match(path, obj["trust_framework_ref"], POLICY_REF_RE, "issuer_trust_ref.trust_framework_ref")
    assert_enum(path, obj["trust_resolution_method"], ALLOWED_TRUST_RESOLUTION, "issuer_trust_ref.trust_resolution_method")
    if "trust_list_entry_ref" in obj:
        assert_string_match(path, obj["trust_list_entry_ref"], REF_RE, "issuer_trust_ref.trust_list_entry_ref")
    if not isinstance(obj["exact_issuer_disclosed"], bool):
        raise ValidationError(f"{path}: issuer_trust_ref.exact_issuer_disclosed must be boolean")


def validate_validity_window(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_VALIDITY_WINDOW)
    assert_only_keys(path, obj, REQUIRED_VALIDITY_WINDOW | {"valid_from"}, "validity_window")
    if obj["granularity"] not in {"date", "hour"}:
        raise ValidationError(f"{path}: validity_window.granularity must be date or hour")
    bucket_re = DATE_BUCKET_RE if obj["granularity"] == "date" else HOUR_BUCKET_RE
    if "valid_from" in obj:
        assert_string_match(path, obj["valid_from"], bucket_re, "validity_window.valid_from")
    assert_string_match(path, obj["valid_until"], bucket_re, "validity_window.valid_until")
    if not isinstance(obj["freshness_requirement_satisfied"], bool):
        raise ValidationError(f"{path}: freshness_requirement_satisfied must be boolean")


def validate_status_evidence(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_STATUS_EVIDENCE)
    assert_only_keys(path, obj, REQUIRED_STATUS_EVIDENCE | {"status_ref", "freshness_bucket"}, "status_evidence")
    assert_enum(path, obj["status_check_type"], ALLOWED_STATUS_TYPES, "status_evidence.status_check_type")
    if "status_ref" in obj:
        assert_string_match(path, obj["status_ref"], REF_RE, "status_evidence.status_ref")
    if "freshness_bucket" in obj:
        value = obj["freshness_bucket"]
        if not isinstance(value, str) or not (DATE_BUCKET_RE.match(value) or HOUR_BUCKET_RE.match(value)):
            raise ValidationError(f"{path}: invalid status_evidence.freshness_bucket")
    if obj["live_issuer_callback_allowed"] is not False:
        raise ValidationError(f"{path}: live issuer callback must not be allowed")


def validate_proof_format_ref(path: Path, obj: dict[str, Any], binding_mode: str) -> None:
    assert_has_keys(path, obj, REQUIRED_PROOF_FORMAT_REF)
    assert_only_keys(path, obj, REQUIRED_PROOF_FORMAT_REF | {"profile_version"}, "proof_format_ref")
    assert_enum(path, obj["proof_family"], ALLOWED_PROOF_FAMILIES, "proof_format_ref.proof_family")
    assert_string_match(path, obj["profile_id"], REF_RE, "proof_format_ref.profile_id")
    assert_enum(path, obj["correlation_scope"], ALLOWED_CORRELATION_SCOPES, "proof_format_ref.correlation_scope")
    if "profile_version" in obj:
        assert_string_match(path, obj["profile_version"], VERSION_RE, "proof_format_ref.profile_version")
    if binding_mode == "B2" and obj["correlation_scope"] == "verifier_scoped":
        raise ValidationError(f"{path}: B2 must not use verifier_scoped correlation scope")


def validate_normal_response(path: Path, obj: dict[str, Any]) -> None:
    assert_has_keys(path, obj, REQUIRED_NORMAL_RESPONSE)
    assert_only_keys(path, obj, REQUIRED_NORMAL_RESPONSE, "normal response")
    if obj["object_type"] != "age_threshold_response":
        raise ValidationError(f"{path}: wrong object_type")
    if obj["object_version"] != "1.0" or not VERSION_RE.match(obj["object_version"]):
        raise ValidationError(f"{path}: unsupported object_version")
    assert_enum(path, obj["profile_ref"], ALLOWED_PROFILES, "profile_ref")
    assert_enum(path, obj["assurance_bucket"], ALLOWED_ASSURANCE_BUCKETS, "assurance_bucket")
    assert_enum(path, obj["issuer_class"], ALLOWED_ISSUER_CLASSES, "issuer_class")
    assert_enum(path, obj["binding_mode"], ALLOWED_BINDING_MODES, "binding_mode")
    if obj["profile_ref"] == "Profile P" and obj["binding_mode"] != "B2":
        raise ValidationError(f"{path}: Profile P responses must use B2")
    if obj["audience_binding"] != "present" or obj["nonce_binding"] != "present":
        raise ValidationError(f"{path}: response must bind audience and nonce")
    for field in ["threshold_result", "issuer_trust_ref", "validity_window", "status_evidence", "proof_format_ref"]:
        if not isinstance(obj[field], dict):
            raise ValidationError(f"{path}: {field} must be an object")
    if not isinstance(obj["possession_proof"], (str, dict)) or obj["possession_proof"] in ("", {}):
        raise ValidationError(f"{path}: possession_proof must be non-empty")
    validate_threshold_result(path, obj["threshold_result"])
    validate_issuer_trust_ref(path, obj["issuer_trust_ref"])
    validate_validity_window(path, obj["validity_window"])
    validate_status_evidence(path, obj["status_evidence"])
    validate_proof_format_ref(path, obj["proof_format_ref"], obj["binding_mode"])
    assert_no_forbidden_keys_recursive(path, obj, FORBIDDEN_NORMAL_RESPONSE_KEYS, "normal response")


def validate_retention_record(path: Path, obj: dict[str, Any]) -> None:
    serialized = json.dumps(obj, sort_keys=True).lower()
    forbidden = ["possession_proof", "proof_transcript", "raw_proof", "fine_grained", "unique_status", "exact_issuer_identity", "audience_binding", "nonce_binding", "stable_holder_identifier", "stable_root_credential_reference"]
    hits = [marker for marker in forbidden if marker in serialized]
    if hits:
        raise ValidationError(f"{path}: retention record contains forbidden material: {hits}")


def run_object_validator(path: Path, kind: str, obj: dict[str, Any]) -> None:
    if kind == "request":
        validate_normal_request(path, obj)
    elif kind == "response":
        validate_normal_response(path, obj)
    elif kind == "retention_record":
        validate_retention_record(path, obj)


def validate_fixture(path: Path) -> None:
    data = parse_json_strict(path)
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: fixture must be a JSON object")
    assert_has_keys(path, data, REQUIRED_ENVELOPE)
    if "object" not in data and "scenario" not in data:
        raise ValidationError(f"{path}: fixture must include object or scenario")
    if data["profile_ref"] not in ALLOWED_ENVELOPE_PROFILES:
        raise ValidationError(f"{path}: invalid envelope profile_ref")
    if data["expected_conformance"] is True and data["expected_failure_class"] is not None:
        raise ValidationError(f"{path}: conformant fixture cannot have a failure class")
    if data["expected_conformance"] is False and not data["expected_failure_class"]:
        raise ValidationError(f"{path}: non-conformant fixture needs a failure class")
    if data["expected_conformance"] is True:
        assert_no_forbidden_markers(path, data)
    if "object" in data and data["kind"] in {"request", "response", "retention_record"}:
        if not isinstance(data["object"], dict):
            raise ValidationError(f"{path}: object must be a JSON object")
        if data["expected_conformance"] is True:
            run_object_validator(path, data["kind"], data["object"])
        else:
            try:
                run_object_validator(path, data["kind"], data["object"])
            except ValidationError:
                return
            raise ValidationError(f"{path}: fixture is marked non-conformant but passed validator checks")


def validate_coverage(files: list[Path]) -> None:
    names = {path.name for path in files}
    required = {"profile-r-v1-b0-request.json", "profile-r-v2-b1-request.json", "profile-p-b2-request.json", "profile-r-v1-b0-response.json", "profile-r-v2-b1-response.json", "profile-p-b2-response.json", "non-conformant-overcollection-request.json", "non-conformant-exception-request.json", "non-conformant-reusable-binding-response.json", "non-conformant-metadata-fingerprint-response.json", "repeated-transaction-b1-same-verifier.json", "repeated-transaction-cross-verifier.json", "verifier-retention-default-record.json", "exception-thresholds-monthly.json", "recovery-scenarios.json"}
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
