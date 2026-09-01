# BioNexus Specifications (BNS)
### Open Specifications & Implementation Proposals for Epistemic Reliability, Scientific Invariants, and Provenance in Computational Biology

[![BNS-conformant](standards/bns-badge/assets/bns-conformant.svg)](standards/bns-badge/SPECIFICATION.md)
[![Specification Version](https://img.shields.io/badge/spec-v1.0.0--rc.4-blue.svg)](spec/registry.yaml)
[![Conformance Suite](https://img.shields.io/badge/CTS-BCTS--v1.0.0-10B981.svg)](standards/conformance-test-suite/)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](LICENSE)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Governance: Forming Council](https://img.shields.io/badge/governance-neutral%20forming-orange.svg)](governance/)

The **BioNexus Specifications (BNS)** define vendor-neutral, language-independent open specification proposals establishing **deterministic scientific invariants, epistemic evidence verification, and cryptographic provenance** for artificial intelligence agents and computational workflows in the life sciences.

> **Community Standards & Adoption Notice (BNS-016 §3 / BNS-IO-008)**:  
> *BioNexus is not an industry standard and does not claim to be one. The BNS series is an open implementation proposal; standards status is earned by external adoption of its vocabulary, schemas, and tests — never declared. We invite scientific developers, workflow maintainers (e.g., nf-core, GA4GH, Galaxy, Bioconductor), and the research community to review, challenge, and shape these specifications.*

---

## The Core Problem

Large Language Models (LLMs) and autonomous AI agents operating in biology frequently fail silently:
* Hallucinating statistical significance (p-values, effect sizes).
* Feeding pre-normalized data into negative binomial models (e.g. DESeq2).
* Elevating observational expression correlation to unsupported causal drug mechanism claims.
* Producing unreplicable, unversioned analyses without cryptographic proof of execution.

The **BioNexus Specification Proposals** provide a framework to transform AI from an unconstrained generative chatbot into a **rigorous scientific collaborator governed by formal epistemic contracts**.

---

## Specification Index (BNS-001 ~ BNS-023)

| Spec ID | Title | Governs | Lifecycle Status |
|---|---|---|---|
| [**BNS-001**](spec/BNS-001-capability-contract.md) | Capability Contract & Scientific ABI | What a biological capability MUST declare | PROPOSED_STANDARD |
| [**BNS-002**](spec/BNS-002-input-invariants.md) | Input Semantic Invariants | Count matrices, coordinates, cell annotations | PROPOSED_STANDARD |
| [**BNS-003**](spec/BNS-003-execution-fidelity.md) | Execution Fidelity | Gold backends, execution states, degradation honesty | PROPOSED_STANDARD |
| [**BNS-004**](spec/BNS-004-evidence-maturity.md) | Evidence Maturity (EvidenceCard 2.0) | Three-layer epistemic evidence reporting | PROPOSED_STANDARD |
| [**BNS-005**](spec/BNS-005-abstention-and-degradation.md) | Abstention & Degradation | Deterministic refusal and degraded advisory behavior | PROPOSED_STANDARD |
| [**BNS-006**](spec/BNS-006-provenance.md) | Provenance | Reproducibility sidecars and audit trails | PROPOSED_STANDARD |
| [**BNS-007**](spec/BNS-007-cross-method-validation.md) | Cross-Method Validation | Parameter sensitivity and method concordance | DRAFT_STANDARD |
| [**BNS-008**](spec/BNS-008-host-conformance.md) | Host Agent Conformance | What connected AI hosts MUST/MUST NOT assert | PROPOSED_STANDARD |
| [**BNS-009**](spec/BNS-009-capability-lifecycle.md) | Capability Lifecycle | Versioning, graduation tracks, deprecation | DRAFT_STANDARD |
| [**BNS-010**](spec/BNS-010-capability-certification.md) | Capability Certification & CAB Scope | 14 evidence criteria; internal assessment vs CAB | DRAFT_STANDARD |
| [**BNS-011**](spec/BNS-011-failure-taxonomy.md) | Scientific Failure Taxonomy | The BN-Fxxx failure ontology | PROPOSED_STANDARD |
| [**BNS-012**](spec/BNS-012-claim-evidence-ledger.md) | Claim-Evidence Ledger | Graph-structured claim representations (PROV-O JSON-LD) | DRAFT_STANDARD |
| [**BNS-013**](spec/BNS-013-scientific-assertion-firewall.md) | Scientific Assertion Firewall | Preflight / Audit / Verify entry points | PROPOSED_STANDARD |
| [**BNS-014**](spec/BNS-014-biofailurebench.md) | BioFailureBench | Benchmark corpus with empirical ground truth | DRAFT_STANDARD |
| [**BNS-015**](spec/BNS-015-flagship-certification.md) | Flagship Certification Track | Multi-modal empirical validation protocols | DRAFT_STANDARD |
| [**BNS-016**](spec/BNS-016-standards-interop.md) | Standards Interoperability | RO-Crate / Workflow Run Crate / IEEE 2791 BCO exports | PROPOSED_STANDARD |
| [**BNS-017**](spec/BNS-017-claim-semantics-ir.md) | Claim Semantics & Deterministic Warrant IR | Typed Claim IR, epistemic warrant rules | DRAFT_STANDARD |
| [**BNS-018**](spec/BNS-018-rule-calibration-and-challenge-network.md) | Rule Calibration & Peer Challenge | Sensitivity metrics, peer challenge protocol | DRAFT_STANDARD |
| [**BNS-019**](spec/BNS-019-scientific-semantic-conventions.md) | Scientific Semantic Conventions | Language-neutral vocabulary for units, claims, evidence | DEVELOPMENT |
| [**BNS-020**](spec/BNS-020-conformance-test-kit.md) | Conformance Test Kit (BCTK) | Target-bound diagnostics & conformance profiles | DEVELOPMENT |
| [**BNS-021**](spec/BNS-021-evidence-debt.md) | Scientific Evidence Debt | Epistemic DAG amortization & debt scheduling | DEVELOPMENT |
| [**BNS-022**](spec/BNS-022-scientific-semantics-neutral-governance.md) | Neutral Governance & Institutional Adoption | Independent Council, commercial/certification separation | DRAFT / COUNCIL_FORMING |
| [**BNS-023**](spec/BNS-023-validation-transparency-network.md) | Validation Transparency Network | Dual-attested validation events and candidate-slot state | DEVELOPMENT |

---

## Repository Structure

```
BioNexus-spec/
├── spec/            # Normative Markdown Specifications (BNS-001 ~ BNS-023)
├── schemas/         # JSON Schema & YAML language-neutral definitions
├── standards/       # Published machine-readable vocabularies & manifests
├── governance/      # Working Group Charter, Governance, & Deprecation Policy
├── rfcs/            # Request for Comments (RFC) change proposals
├── tools/           # Validation scripts for specifications and schemas
├── CHANGELOG.md     # Standard evolution history
└── IMPLEMENTATION_GUIDE.md # Developer guide for runtime implementers
```

---

## Contributing & RFC Process

Proposed revisions and new specifications MUST follow the [RFC Process](rfcs/). Please refer to [governance/CHARTER.md](governance/CHARTER.md) and [governance/GOVERNANCE.md](governance/GOVERNANCE.md) for details on consensus and voting.
