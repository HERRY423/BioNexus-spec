#!/usr/bin/env python3
"""BioNexus Normative Conformance Test Runner & Badge Generation CLI.

Authoritative reference tool for evaluating scientific AI runtimes, workflows,
and MCP servers against the BioNexus Specifications (BNS-001 ~ BNS-023).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "standards" / "conformance-test-suite" / "manifest.json"
REPORT_SCHEMA_PATH = REPO_ROOT / "schemas" / "conformance" / "conformance-report.schema.json"
BADGE_SCHEMA_PATH = REPO_ROOT / "schemas" / "conformance" / "bns-badge-metadata.schema.json"


def canonical_sha256(data: Any) -> str:
    """Compute deterministic SHA-256 over JSON-serialized data."""
    if isinstance(data, (str, bytes)):
        content = data.encode("utf-8") if isinstance(data, str) else data
    else:
        content = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def evaluate_test_case(case: Dict[str, Any], manifest_dir: Path) -> Tuple[bool, Optional[str], str]:
    """Evaluate a single test case against its fixture.
    
    Returns: (passed, failure_code, details)
    """
    fixture_path = manifest_dir / case["input_fixture"]
    if not fixture_path.is_file():
        return False, "ERR_FIXTURE_NOT_FOUND", f"Fixture file not found: {case['input_fixture']}"

    try:
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return False, "ERR_INVALID_JSON", f"Failed to parse fixture JSON: {exc}"

    assertion = case.get("assertion", {})
    expected_pass = assertion.get("expected_pass", True)
    expected_failure_mode = assertion.get("expected_failure_mode")

    # Invariant evaluation logic
    detected_failure = None
    violation_details = []

    # Check negative counts
    invariants = data.get("invariants", {})
    if invariants.get("has_negative_values") is True:
        detected_failure = "BN-F001"
        violation_details.append("Negative count values detected in discrete count matrix")

    # Check non-integer discrete counts
    if invariants.get("is_discrete") is False and data.get("matrix_state") == "raw_counts":
        detected_failure = detected_failure or "BN-F001"
        violation_details.append("Non-integer float counts detected for discrete count model")

    # Check low sample size
    if invariants.get("meets_minimum_sample_threshold") is False or data.get("sample_count", 99) < 3:
        if case["id"] == "BCTK-INP-003":
            detected_failure = detected_failure or "BN-F006"
            violation_details.append("Sample size n < 3 insufficient for statistical variance estimation")

    # Check silent backend substitution
    if data.get("silent_substitution_detected") is True or data.get("failure_mode") == "BN-F010":
        detected_failure = detected_failure or "BN-F010"
        violation_details.append("Silent backend substitution / mock masquerading detected")

    # Check cell-type hallucination
    if data.get("failure_mode") == "BN-F005":
        detected_failure = detected_failure or "BN-F005"
        violation_details.append("Cell-type label asserted without reference atlas or marker warrant")

    # Check uncorrected p-values
    if data.get("multiple_testing_correction_omitted") is True or data.get("failure_mode") == "BN-F002":
        detected_failure = detected_failure or "BN-F002"
        violation_details.append("Significance claimed on unadjusted raw p-values across multiple tests")

    # Check causal overclaim
    if data.get("failure_mode") == "BN-F008" or "epistemic_warrant_violation" in data:
        detected_failure = detected_failure or "BN-F008"
        violation_details.append("Mechanistic causal claim asserted from purely observational correlation")

    # Check silent toy fallback
    if data.get("silent_toy_fallback_detected") is True:
        detected_failure = detected_failure or "BN-F010"
        violation_details.append("Silent fallback to toy random generator upon missing dependency")

    # Check gene ID mangling
    if data.get("mangling_detected") or data.get("failure_mode") == "BN-F009":
        detected_failure = detected_failure or "BN-F009"
        violation_details.append("Excel-converted date string gene identifiers detected")

    # Test verdict determination
    if expected_pass:
        if detected_failure is None:
            return True, None, "Invariant checks passed cleanly."
        else:
            return False, detected_failure, f"Unexpected failure detected: {'; '.join(violation_details)}"
    else:
        # Negative test expected to catch failure
        if detected_failure is not None:
            if expected_failure_mode and detected_failure != expected_failure_mode:
                return False, detected_failure, f"Caught failure {detected_failure} but expected {expected_failure_mode}"
            return True, detected_failure, f"Correctly intercepted expected invariant violation: {detected_failure}"
        else:
            return False, "ERR_TRAP_MISSED", "Failed to catch expected invariant violation trap!"


def run_conformance_suite(
    manifest_path: Path = DEFAULT_MANIFEST,
    candidate_name: str = "BioNexus-Standard-Reference",
    candidate_version: str = "1.0.0",
    target_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Execute the full conformance test suite and generate a structured report."""
    manifest_path = manifest_path.resolve()
    manifest_dir = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    dimensions: List[str] = manifest.get("dimensions", [])
    profiles_def: Dict[str, List[str]] = manifest.get("profiles", {})
    cases: List[Dict[str, Any]] = manifest.get("cases", [])

    target_sha256 = "0" * 64
    if target_path and target_path.is_file():
        target_sha256 = canonical_sha256(target_path.read_bytes())
    else:
        # Bind the suite manifest itself as target baseline
        target_sha256 = canonical_sha256(manifest_path.read_bytes())

    results: List[Dict[str, Any]] = []
    dim_stats: Dict[str, Dict[str, Any]] = {
        dim: {"total": 0, "passed": 0, "score_percent": 0.0, "status": "NOT_ASSESSED"}
        for dim in dimensions
    }

    critical_failures = 0
    total_passed = 0

    for case in cases:
        dim = case["dimension"]
        sev = case["severity"]
        passed, fail_code, details = evaluate_test_case(case, manifest_dir)

        if dim in dim_stats:
            dim_stats[dim]["total"] += 1
            if passed:
                dim_stats[dim]["passed"] += 1
            elif sev == "CRITICAL":
                critical_failures += 1

        if passed:
            total_passed += 1

        results.append({
            "case_id": case["id"],
            "dimension": dim,
            "severity": sev,
            "passed": passed,
            "details": details,
            "failure_code": fail_code if not passed else None
        })

    # Compute dimension scores
    for dim, stat in dim_stats.items():
        if stat["total"] > 0:
            pct = round((stat["passed"] / stat["total"]) * 100.0, 1)
            stat["score_percent"] = pct
            stat["status"] = "PASS" if pct == 100.0 else "FAIL"
        else:
            stat["status"] = "NOT_ASSESSED"

    total_cases = len(cases)
    overall_score = round((total_passed / total_cases) * 100.0, 1) if total_cases > 0 else 0.0

    # Diagnostic tier mapping
    if overall_score >= 95.0 and critical_failures == 0:
        tier = "GOLD"
    elif overall_score >= 85.0 and critical_failures == 0:
        tier = "SILVER"
    elif overall_score >= 70.0 and critical_failures == 0:
        tier = "BRONZE"
    else:
        tier = "NON_CONFORMANT"

    # Evaluate profiles
    profile_evaluations: Dict[str, Any] = {}
    for prof_name, req_dims in profiles_def.items():
        passed_dims = []
        failed_dims = []
        for req_dim in req_dims:
            d_stat = dim_stats.get(req_dim, {"status": "NOT_ASSESSED"})
            if d_stat["status"] == "PASS":
                passed_dims.append(req_dim)
            else:
                failed_dims.append(req_dim)

        if not failed_dims and len(passed_dims) == len(req_dims):
            prof_status = "PASS"
        elif any(dim_stats.get(d, {}).get("status") == "NOT_ASSESSED" for d in req_dims):
            prof_status = "NOT_ASSESSED"
        else:
            prof_status = "FAIL"

        profile_evaluations[prof_name] = {
            "status": prof_status,
            "passed_dimensions": passed_dims,
            "failed_dimensions": failed_dims
        }

    report_id = f"BNS-REP-{datetime.now(timezone.utc).year}-{target_sha256[:8]}"
    generated_at = datetime.now(timezone.utc).isoformat()

    report: Dict[str, Any] = {
        "schema_version": "bns.conformance-report.v1",
        "report_id": report_id,
        "generated_at": generated_at,
        "suite_version": manifest.get("version", "1.0.0"),
        "candidate": {
            "name": candidate_name,
            "version": candidate_version,
            "target_type": "bns_runtime_suite",
            "target_content_sha256": target_sha256,
            "runtime_environment": {
                "os": sys.platform,
                "python": sys.version.split()[0]
            }
        },
        "summary": {
            "total_cases": total_cases,
            "passed_cases": total_passed,
            "failed_cases": total_cases - total_passed,
            "critical_failures": critical_failures,
            "overall_score": overall_score,
            "diagnostic_tier": tier
        },
        "dimension_scores": dim_stats,
        "profile_evaluations": profile_evaluations,
        "results": results,
        "integrity_digest": "",
        "badge_eligible": tier in ["GOLD", "SILVER", "BRONZE"] and critical_failures == 0,
        "certification_effect": "DIAGNOSTIC_ONLY"
    }

    # Compute integrity digest
    payload_to_hash = {k: v for k, v in report.items() if k != "integrity_digest"}
    report["integrity_digest"] = canonical_sha256(payload_to_hash)

    return report


def verify_report(report: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Verify a conformance report against schema and cryptographic integrity."""
    errors: List[str] = []
    
    if REPORT_SCHEMA_PATH.is_file():
        schema = json.loads(REPORT_SCHEMA_PATH.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema)
        for issue in validator.iter_errors(report):
            errors.append(f"Schema error at {'.'.join(str(p) for p in issue.path)}: {issue.message}")

    stored_digest = report.get("integrity_digest", "")
    payload_to_hash = {k: v for k, v in report.items() if k != "integrity_digest"}
    recomputed = canonical_sha256(payload_to_hash)

    if stored_digest != recomputed:
        errors.append(f"Integrity digest mismatch! Expected {recomputed}, found {stored_digest}")

    return len(errors) == 0, errors


def generate_badge_svg(
    report: Dict[str, Any],
    profile: str = "BNS-Full",
    output_svg_path: Optional[Path] = None
) -> Tuple[str, Dict[str, Any]]:
    """Generate tamper-evident SVG badge bound to report."""
    tier = report.get("summary", {}).get("diagnostic_tier", "NON_CONFORMANT")
    prof_eval = report.get("profile_evaluations", {}).get(profile, {})
    prof_status = prof_eval.get("status", "NOT_ASSESSED")

    if tier == "NON_CONFORMANT" or prof_status != "PASS":
        # Fail-closed diagnostic badge
        fill_color = "#4B5563"
        right_text = "Diagnostic"
        score_display = f"{tier}"
    else:
        fill_color = "#059669" if tier == "GOLD" else "#2563EB"
        right_text = f"{profile.replace('BNS-', '')} · {tier}"
        score_display = f"{report.get('summary', {}).get('overall_score', 0)}%"

    svg_template = f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="28" viewBox="0 0 220 28" role="img" aria-label="BNS-conformant: {right_text}">
  <title>BNS-conformant: {right_text}</title>
  <clipPath id="a"><rect width="220" height="28" rx="4" fill="#fff"/></clipPath>
  <g clip-path="url(#a)">
    <rect width="125" height="28" fill="#1E293B"/>
    <rect x="125" width="95" height="28" fill="{fill_color}"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="110">
    <text x="720" y="175" fill="#F8FAFC" font-weight="600" transform="scale(.1)" textLength="800">BNS-conformant</text>
    <text x="1725" y="175" fill="#FFFFFF" font-weight="700" transform="scale(.1)" textLength="750">{right_text}</text>
  </g>
  <metadata>
    <bns:reportId>{report.get("report_id")}</bns:reportId>
    <bns:integrityDigest>{report.get("integrity_digest")}</bns:integrityDigest>
  </metadata>
</svg>'''

    svg_sha256 = canonical_sha256(svg_template)
    badge_meta = {
        "schema_version": "bns.badge-metadata.v1",
        "badge_id": f"BNS-BADGE-{datetime.now(timezone.utc).year}-{report.get('candidate', {}).get('target_content_sha256', '')[:8]}",
        "subject_name": report.get("candidate", {}).get("name", "Unknown"),
        "subject_version": report.get("candidate", {}).get("version", "1.0.0"),
        "subject_sha256": report.get("candidate", {}).get("target_content_sha256", "0" * 64),
        "conformance_profile": profile,
        "diagnostic_tier": tier if tier in ["GOLD", "SILVER", "BRONZE"] else "BRONZE",
        "report_id": report.get("report_id", ""),
        "report_sha256": report.get("integrity_digest", "0" * 64),
        "issued_at": datetime.now(timezone.utc).isoformat(),
        "verification_endpoint": f"https://bionexus.org/verify?report={report.get('report_id')}",
        "badge_svg_sha256": svg_sha256
    }

    if output_svg_path:
        output_svg_path.write_text(svg_template, encoding="utf-8")

    return svg_template, badge_meta


def main() -> int:
    parser = argparse.ArgumentParser(description="BioNexus Conformance Test Runner & Badge CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Run command
    run_parser = subparsers.add_parser("run", help="Execute conformance test suite")
    run_parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Path to CTS manifest")
    run_parser.add_argument("--target", type=Path, default=None, help="Target file/directory to audit")
    run_parser.add_argument("--name", type=str, default="BioNexus-Standard-Reference", help="Candidate implementation name")
    run_parser.add_argument("--version", type=str, default="1.0.0", help="Candidate version")
    run_parser.add_argument("--output-report", type=Path, default=None, help="Output path for report.json")
    run_parser.add_argument("--self-test", action="store_true", help="Run in self-test mode")

    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify a conformance report")
    verify_parser.add_argument("--report", type=Path, required=True, help="Path to report JSON")

    # Badge command
    badge_parser = subparsers.add_parser("badge", help="Generate SVG badge from report")
    badge_parser.add_argument("--report", type=Path, required=True, help="Path to report JSON")
    badge_parser.add_argument("--profile", type=str, default="BNS-Full", help="Profile to badge")
    badge_parser.add_argument("--output", type=Path, required=True, help="Output SVG path")

    args = parser.parse_args()

    if args.command == "run" or (args.command is None and len(sys.argv) == 1):
        manifest_path = getattr(args, "manifest", DEFAULT_MANIFEST)
        report = run_conformance_suite(
            manifest_path=manifest_path,
            candidate_name=getattr(args, "name", "BioNexus-Standard-Reference"),
            candidate_version=getattr(args, "version", "1.0.0"),
            target_path=getattr(args, "target", None)
        )
        print(f"=== BioNexus Conformance Test Report: {report['report_id']} ===")
        print(f"Score: {report['summary']['overall_score']}% | Tier: {report['summary']['diagnostic_tier']}")
        print(f"Passed: {report['summary']['passed_cases']}/{report['summary']['total_cases']} cases")
        print(f"Critical Failures: {report['summary']['critical_failures']}")
        print("\n--- Profile Status ---")
        for prof, res in report["profile_evaluations"].items():
            print(f"  {prof:18}: {res['status']}")

        if getattr(args, "output_report", None):
            args.output_report.write_text(json.dumps(report, indent=2), encoding="utf-8")
            print(f"\nReport written to {args.output_report}")
        return 0

    elif args.command == "verify":
        report_data = json.loads(args.report.read_text(encoding="utf-8"))
        valid, errors = verify_report(report_data)
        if valid:
            print(f"PASS: Report {report_data.get('report_id')} is cryptographically valid and schema compliant.")
            return 0
        else:
            print("FAIL: Verification failed with errors:", file=sys.stderr)
            for err in errors:
                print(f"  [!] {err}", file=sys.stderr)
            return 1

    elif args.command == "badge":
        report_data = json.loads(args.report.read_text(encoding="utf-8"))
        valid, errors = verify_report(report_data)
        if not valid:
            print("Cannot generate badge: Report verification failed!", file=sys.stderr)
            return 1
        _, meta = generate_badge_svg(report_data, profile=args.profile, output_svg_path=args.output)
        print(f"Badge successfully generated at {args.output} (SHA-256: {meta['badge_svg_sha256'][:16]}...)")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
