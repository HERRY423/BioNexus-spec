# BioNexus Badge Policy & Terms of Usage ("BNS-conformant")

**Status**: Active Policy | **Version**: 1.0.0 | **Governing Body**: Scientific Semantics Council (SSC)

---

## 1. Terms of Usage

The **"BNS-conformant"** mark, logo, and badge assets are trademarks of the BioNexus Standards Project. They may be used freely by open-source projects, academic institutions, and commercial vendors under the following conditions:

1. **Deterministic Test Evidence**: The software, workflow, model, or MCP server MUST have executed the official **BioNexus Conformance Test Suite (BCTS)** and produced a verified `conformance-report.json` with an overall score $\ge 70.0\%$ (Bronze), $\ge 85.0\%$ (Silver), or $\ge 95.0\%$ (Gold).
2. **Zero Critical Violations**: The test report MUST NOT contain any critical invariant violation (e.g. `BN-F001`, `BN-F005`, `BN-F010`). Any silent mock substitution or masquerading immediately disqualifies the target from badge display.
3. **Exact Profile Scope**: The displayed badge MUST accurately reflect the specific profile passed (e.g. `BNS-Core`, `BNS-Warrant`, `BNS-Provenance`, or `BNS-Full`). Claiming `BNS-Full` when only `BNS-Core` passed constitutes trademark violation.
4. **Verifiable Linkage**: In digital media (web, documentation, GitHub READMEs), the badge MUST link directly to the public test report or public verification endpoint (`https://bionexus.org/verify?digest=...`).

---

## 2. Institutional Separation & Governance Alignment (BNS-022)

To maintain absolute impartiality and prevent vendor capture:
- **Diagnostic Conformance**: Running `bns_conformance_runner.py` produces an empirical technical diagnostic report. This demonstrates that the code passes standard invariant tests.
- **Conformity Assessment Body (CAB) Scope**: In regulated clinical or high-assurance environments, third-party accredited CAB certification is separate from self-asserted technical diagnostics. The badge metadata distinguishes between `DIAGNOSTIC_ONLY` and `ASSESSED_BY_INDEPENDENT_CAB`.
- **BioNexus Neutrality**: The BioNexus project does not favor any proprietary vendor or runtime. All tools are judged strictly on objective test assertions.

---

## 3. Revocation & Misrepresentation

1. **Stale Evidence**: Conformance reports older than 18 months MUST be refreshed against the latest minor version of the specification.
2. **Misrepresentation Registry**: Any implementation caught falsifying test results, disabling assertion checks in production while displaying the badge, or claiming unsupported profiles will be placed on the public **Revocation and Non-Compliance Registry** and required to remove all badge assets immediately.
