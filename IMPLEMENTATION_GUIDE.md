# BioNexus Specification Implementation Guide

This guide provides technical instructions for engineers and software architects implementing standard-conforming runtimes, MCP servers, or agent wrappers against the **BioNexus Specifications (BNS)**.

---

## 1. Conformance Profiles & Core Responsibilities

An implementation may declare conformance to one or more **BNS Conformance Profiles** (defined in BNS-020):
- **BNS-SCIENTIFIC-CORE**: Input invariant checks (BNS-002), Fail-Closed execution (BNS-005), and failure taxonomy (BNS-011).
- **BNS-EVIDENCE-TRANSPARENCY**: EvidenceCard 2.0 (BNS-004), Provenance and RO-Crate (BNS-006, BNS-016), and Claim Semantics IR (BNS-017).
- **BNS-HOST-AGENT-GUARD**: Host Agent Conformance (BNS-008) and Overclaim Interception (BNS-017).
- **BNS-VALIDATION-NETWORK-NODE**: Dual attestation (BNS-023) and calibration freezes (BNS-018).

---

## 2. Implementing the Scientific Assertion Firewall (BNS-002, BNS-013)

### Step 1: Pre-Execution Invariant Verification
Before executing any statistical or bioinformatics routine, your runtime MUST inspect the raw input matrix or sequence to ensure count non-negativity and integer constraints.

### Step 2: Epistemic Evidence Generation (BNS-004)
Outputs MUST be wrapped in a structured EvidenceCard containing execution envelopes, empirical warrant status, and authority disclaimers.

---

## 3. Reference Implementations

The specifications are strictly decoupled from any runtime implementation. The official reference implementations are maintained in the BioNexus runtime repository:

- **BioNexus Python Reference Runtime**: https://github.com/HERRY423/BioNexus
- **Nextflow nf-core Receipt Module (Reference)**: https://github.com/HERRY423/BioNexus/tree/main/modules/local/bns019_receipt
- **MCP Server Reference Implementation**: https://github.com/HERRY423/BioNexus/tree/main/src/bionexus/mcp

---

## 4. Passing the Conformance Test Suite & Displaying "BNS-conformant" Badges

To verify and certify that your runtime, agent, or workflow adheres to BioNexus invariants:

### Step 1: Run the Normative Conformance Test Suite (BCTS)
```bash
python tools/bns_conformance_runner.py run \
  --manifest standards/conformance-test-suite/manifest.json \
  --name "MyAgentRuntime" \
  --version "1.2.0" \
  --output-report bns-report.json
```

### Step 2: Verify Report Cryptographic Integrity
```bash
python tools/bns_conformance_runner.py verify --report bns-report.json
```

### Step 3: Generate and Embed Your "BNS-conformant" Badge
```bash
python tools/bns_conformance_runner.py badge \
  --report bns-report.json \
  --profile BNS-Full \
  --output bns-conformant.svg
```

In your repository `README.md`, embed the badge linked to your verifiable report:
```markdown
[![BNS-conformant](https://raw.githubusercontent.com/HERRY423/BioNexus-spec/main/standards/bns-badge/assets/bns-conformant.svg)](https://bionexus.org/verify?report=bns-report.json)
```
