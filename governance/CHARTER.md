# BioNexus Standards Working Group Charter

## 1. Mission & Purpose
The **BioNexus Standards Working Group (BNS-WG)** is an open, vendor-neutral standards initiative dedicated to establishing **epistemic reliability, deterministic scientific invariant enforcement, and reproducible provenance standards for AI-assisted computational biology and bioinformatics**.

Artificial intelligence models (LLMs, generative models, multi-agent frameworks) operating in biological domains face structural failure modes:
1. **Hallucinated statistical significance** ($-values, effect sizes, counterfeit cross-validation).
2. **Methodological misuse** (e.g., applying negative-binomial count models like DESeq2 to log-normalized or non-integer matrices).
3. **Causal overclaim** (attributing direct drug target causation to observational gene expression correlation).
4. **Counterfeit provenance** (untraceable data lineages and black-box code generation).

The purpose of the BioNexus Specifications (BNS) is to define **machine-verifiable contracts, semantic conventions, and conformance profiles** that any AI system, workflow engine, or laboratory runtime MUST adhere to before claiming scientific validity.

---

## 2. Core Operating Principles

1. **Epistemic Humility & Deterministic Abstention**:
   A standard-conforming agent MUST fail closed and refuse execution or claim promotion when statistical invariants or requisite evidence are absent.
2. **Language & Runtime Neutrality**:
   All BNS specifications are specified through formal mathematical invariants, JSON Schema / YAML definitions, and protocol state machines independent of any single programming language or commercial platform.
3. **Separation of Standard from Implementation**:
   The BNS specifications exist independently of any reference implementation (such as BioNexus-Python). Any runtime in Python, Rust, Go, TypeScript, C++, or Nextflow can claim BNS conformance by passing the standard Conformance Test Kit (BNS-020).
4. **Monotonicity & Non-Regressive Versioning**:
   Specification IDs (BNS-001 through BNS-023+) are assigned monotonically and never reassigned or mutated retroactively.
5. **No Counterfeit Certification**:
   Compliance with BNS rules verifies *internal evidence completeness and invariant satisfaction*. The standard explicitly forbids misrepresenting internal evidence completeness as third-party regulatory accreditation (CAB/FDA/NMPA).

---

## 3. Working Group Structure

* **Technical Steering Committee (TSC)**: Oversees architectural integrity, monotonic spec registration, and RFC approvals.
* **Domain Subcommittees**:
  - *Invariants & Execution Semantics* (BNS-001 ~ BNS-005, BNS-011, BNS-013)
  - *Provenance & Interoperability* (BNS-006, BNS-012, BNS-016, BNS-019)
  - *Claim Semantics & Calibration* (BNS-004, BNS-017, BNS-018, BNS-021)
  - *Conformance & Transparency Network* (BNS-020, BNS-022, BNS-023)
