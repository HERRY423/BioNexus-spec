# BioNexus Standard Implementation Guide

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

- **Python Reference Runtime**: https://github.com/HERRY423/BioNexus
- **Nextflow nf-core Module**: modules/local/bns019_receipt
- **MCP Server Implementation**: bionexus-local-mcp

