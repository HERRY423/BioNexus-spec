# RFC-0001: The BioNexus RFC Process and Governance Guidelines

- **Status**: IMPLEMENTED
- **Author(s)**: BioNexus Technical Steering Committee
- **Created**: 2026-08-31
- **Target Specification**: BNS-022, Governance

---

## 1. Executive Summary
This RFC establishes the formal Request for Comments (RFC) process as the mandatory change management protocol for all normative BioNexus Specifications (BNS-001 ~ BNS-023+).

## 2. Motivation
To prevent ad-hoc or uncoordinated mutations of scientific invariants, all changes affecting semantics, claim verification rules, or wire formats must undergo peer review with explicit mathematical rigor.

## 3. Normative Process Rules
1. **Mandatory RFC for Normative Edits**: Any change modifying RFC 2119 keywords (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT) in any BNS document requires an accepted RFC.
2. **Schema Dual-Attestation**: Any schema modification must provide valid JSON Schema Draft 2020-12 definitions and sample conformant / non-conformant test payloads.
3. **Reference Implementation Pre-requisite**: An RFC cannot transition from ACCEPTED to IMPLEMENTED without at least one working reference implementation passing automated test suites.
