# BioNexus Normative Conformance Test Suite (BCTS)

The **BioNexus Normative Conformance Test Suite (BCTS)** provides the authoritative, vendor-neutral test vectors and invariant validation harness for certifying scientific AI agents, bioinformatics runtimes, MCP servers, and computational pipelines against the **BioNexus Specifications (BNS-001 ~ BNS-023)**.

---

## 1. The 8 Conformance Dimensions

Every candidate implementation is tested against 8 orthogonal scientific dimensions:

1. **Biological Semantics**: Gene identifier hygiene (rejects Excel date mangling `BN-F009`), matrix scale semantics (log vs counts `BNS-II-001`), spatial coordinate consistency, taxonomy binding.
2. **Input State Honesty**: Non-negative count invariant (`BN-F001`), integer discreteness, sample size thresholds $n \ge 3$ (`BN-F006`), preflight data audits.
3. **Backend Identity**: Anti-masquerading / zero silent substitution (`BN-F010`), distribution package integrity witnesses, entrypoint resolution.
4. **Provenance**: W3C PROV-O activity sidecars, SHA-256 integrity binding for inputs/outputs, environment parameter capture.
5. **Claim Warrant**: Warrant ceiling clamping, cell-type hallucination defense (`BN-F005`), multiple testing correction FDR honesty (`BN-F002`).
6. **Abstention**: Deterministic precondition refusal, structured EvidenceCard 2.0 refusal payloads, zero silent fallback to toy/mock proxies.
7. **Failure Handling**: BioFailureBench trap defense, canonical failure taxonomy linkage (`BN-Fxxx`), actionable remediation.
8. **Cross-Host Consistency**: Deterministic execution under fixed random seeds, host-agnostic ABI compliance, headless CI readiness.

---

## 2. Conformance Profiles

Implementations can certify against specific bounded profiles or the full standard:

| Profile | Governed Dimensions | Target Applications |
| :--- | :--- | :--- |
| **`BNS-Core`** | Biological Semantics, Input State Honesty, Backend Identity, Abstention | Statistical tools, count processors, data transformers |
| **`BNS-Warrant`** | Claim Warrant, Abstention, Failure Handling | Scientific LLMs, claim assertion firewalls, report generators |
| **`BNS-Provenance`** | Provenance, Backend Identity | Workflow engines (Nextflow, Snakemake), data lakehouses |
| **`BNS-Agent`** | Cross-Host Consistency, Claim Warrant, Abstention | Autonomous scientific agents, multi-agent frameworks |
| **`BNS-Validation`** | Failure Handling, Cross-Host Consistency, Provenance | Benchmarking suites, validation nodes |
| **`BNS-Full`** | **All 8 Dimensions** | Flagship certified autonomous scientific discovery platforms |

---

## 3. Running the Conformance Test Suite

To run the CTS against a candidate package or test manifest:

```bash
# Run full suite self-test and generate report
python tools/bns_conformance_runner.py run --manifest standards/conformance-test-suite/manifest.json --output-report report.json

# Audit an existing report
python tools/bns_conformance_runner.py verify --report report.json

# Generate a verifiable "BNS-conformant" SVG badge
python tools/bns_conformance_runner.py badge --report report.json --profile BNS-Full --output bns-conformant.svg
```

---

## 4. Conformance Tiers & Scoring

- **GOLD** ($\ge 95.0\%$): 100% Backend Identity PASS, 100% Abstention PASS, 0 Critical Failures.
- **SILVER** ($\ge 85.0\%$): 100% Backend Identity PASS, 100% Abstention PASS, 0 Critical Failures.
- **BRONZE** ($\ge 70.0\%$): Non-masquerading state, $\ge 80\%$ Abstention PASS, 0 Critical Failures.
- **NON_CONFORMANT** ($< 70.0\%$ or any critical failure or masquerading backend).
