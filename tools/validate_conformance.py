#!/usr/bin/env python3
"""Automated Conformance Test Suite & Badge Validation for BioNexus-spec CI."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

from bns_conformance_runner import (
    run_conformance_suite,
    verify_report,
    generate_badge_svg,
    DEFAULT_MANIFEST,
    REPORT_SCHEMA_PATH,
    BADGE_SCHEMA_PATH
)


def validate_conformance_system() -> int:
    print("=== Validating BioNexus Conformance Test Suite (CTS) & Badge Subsystem ===")
    errors = []

    # 1. Validate manifest and test cases schema
    manifest_schema_path = REPO_ROOT / "schemas" / "conformance" / "conformance-suite.schema.json"
    case_schema_path = REPO_ROOT / "schemas" / "conformance" / "conformance-test-case.schema.json"

    if not manifest_schema_path.is_file():
        errors.append("Manifest schema missing: conformance-suite.schema.json")
    if not case_schema_path.is_file():
        errors.append("Case schema missing: conformance-test-case.schema.json")

    if manifest_schema_path.is_file() and case_schema_path.is_file():
        try:
            m_data = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
            c_schema = json.loads(case_schema_path.read_text(encoding="utf-8"))
            case_validator = Draft202012Validator(c_schema)

            # Validate each case individually
            for idx, c in enumerate(m_data.get("cases", [])):
                for err in case_validator.iter_errors(c):
                    errors.append(f"Case {c.get('id', idx)} schema error: {err.message}")

            # Also validate top-level manifest structure without resolving external ref
            m_schema_copy = json.loads(manifest_schema_path.read_text(encoding="utf-8"))
            m_schema_copy["properties"]["cases"] = {"type": "array"}
            manifest_validator = Draft202012Validator(m_schema_copy)
            for err in manifest_validator.iter_errors(m_data):
                errors.append(f"Manifest schema violation at {'.'.join(str(p) for p in err.path)}: {err.message}")

        except Exception as exc:
            errors.append(f"Failed to validate manifest against schema: {exc}")

    # 2. Run test runner
    try:
        report = run_conformance_suite(DEFAULT_MANIFEST)
        if report["summary"]["overall_score"] != 100.0:
            errors.append(f"Expected 100.0% score on reference test suite, got {report['summary']['overall_score']}%")
        if report["summary"]["critical_failures"] != 0:
            errors.append(f"Critical failures detected in reference test suite: {report['summary']['critical_failures']}")
        if report["summary"]["diagnostic_tier"] != "GOLD":
            errors.append(f"Expected GOLD tier, got {report['summary']['diagnostic_tier']}")
    except Exception as exc:
        errors.append(f"Conformance suite execution crashed: {exc}")
        return 1

    # 3. Validate report verification
    valid, v_errors = verify_report(report)
    if not valid:
        errors.extend([f"Report verification failure: {e}" for e in v_errors])

    # 4. Validate badge generation and metadata schema
    try:
        svg_content, badge_meta = generate_badge_svg(report, profile="BNS-Full")
        if "<svg" not in svg_content or "</svg>" not in svg_content:
            errors.append("Generated badge SVG is malformed")

        if BADGE_SCHEMA_PATH.is_file():
            b_schema = json.loads(BADGE_SCHEMA_PATH.read_text(encoding="utf-8"))
            b_val = Draft202012Validator(b_schema)
            for err in b_val.iter_errors(badge_meta):
                errors.append(f"Badge metadata schema violation: {err.message}")
    except Exception as exc:
        errors.append(f"Badge generation failed: {exc}")

    if errors:
        print(f"\n[FAIL] Conformance validation failed with {len(errors)} errors:")
        for err in errors:
            print(f"  [!] {err}")
        return 1

    print("\n[PASS] All Conformance Test Suite (CTS) assertions and 'BNS-conformant' badge checks passed perfectly!")
    return 0


if __name__ == "__main__":
    sys.exit(validate_conformance_system())
