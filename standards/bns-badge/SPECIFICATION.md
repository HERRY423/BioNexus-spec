# BioNexus Conformant Badge Specification ("BNS-conformant")

**Status**: Draft Proposal | **Version**: 1.0.0  
**Governs**: `standards/bns-badge/`, Badge Visual Grammar, Machine-Readable Metadata, Verification Endpoints, SVG Assets.

---

## 1. Overview & Purpose

The **`BNS-conformant`** badge provides an open, machine-verifiable indicator of diagnostic compliance with the **BioNexus Specifications (BNS)**. Displaying this badge indicates that a biological AI agent, computational workflow, or analysis tool has executed the **BioNexus Conformance Test Suite (BCTS)** and verified that:
1. Biological identifiers and scales conform to defined semantic invariants.
2. Discrete count models reject invalid non-integer or negative inputs (`BN-F001`).
3. Software execution records verifiable backend provenance without silent mock substitution (`BN-F010`).
4. Output claims and error handlers emit structured W3C PROV-O provenance sidecars and refusal records.

> **Conformance Notice (BNS-016 §3 / BNS-022 §7)**:  
> A BNS diagnostic badge certifies technical execution against specific test vectors. It does not constitute formal regulatory clearance (CLIA/CAP/FDA) or third-party accredited CAB certification unless verified under BNS-022.

---

## 2. Badge Anatomy & Visual Grammar

All official BNS badges adhere to standard vector geometry and high-contrast, accessibility-compliant palettes:

```
+-------------------------------------------------------------------------------+
|  [ BioNexus Logo ]  BNS-conformant  |  Full · Gold (98.5%)   [ Verified Mark ] |
+-------------------------------------------------------------------------------+
|  <------------------ Left Pill ------------------> | <----- Right Pill -----> |
```

### Color Codes
- **Master / Full Profile**: `#10B981` (Emerald Green) / `#059669` (Dark Emerald)
- **Core Profile**: `#3B82F6` (Royal Blue) / `#1D4ED8` (Deep Blue)
- **Warrant Profile**: `#8B5CF6` (Purple) / `#6D28D9` (Dark Purple)
- **Provenance Profile**: `#06B6D4` (Cyan) / `#0891B2` (Dark Cyan)
- **Agent Profile**: `#EC4899` (Pink) / `#BE185D` (Dark Pink)
- **Validation Profile**: `#F59E0B` (Amber) / `#D97706` (Dark Amber)
- **Diagnostic / Uncertified**: `#6B7280` (Neutral Gray)

---

## 3. Cryptographic Binding & Tamper Evidence

A `BNS-conformant` badge is designed to be verifiable against an immutable test report. Generated badge files include machine-readable metadata binding:
- **`subject_sha256`**: SHA-256 hash of the target software release, workflow bundle, or model artifact.
- **`report_id`**: Canonical identifier of the corresponding Conformance Test Report.
- **`report_sha256`**: Cryptographic digest of the test report payload.
- **`verification_endpoint`**: Public URI for inspecting test results.

```xml
<metadata id="bns-conformance-metadata">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:bns="https://bionexus.org/ns/conformance#">
    <rdf:Description rdf:about="urn:bionexus:badge:BNS-BADGE-2026-0001">
      <bns:profile>BNS-Full</bns:profile>
      <bns:tier>GOLD</bns:tier>
      <bns:reportDigest>9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca7</bns:reportDigest>
      <bns:targetDigest>4a53cda1efb6487e974e447b973948e71887e59b9772bf29a6604230188686d4</bns:targetDigest>
    </rdf:Description>
  </rdf:RDF>
</metadata>
```

---

## 4. Embedding Formats

### GitHub / Markdown
```markdown
[![BNS-conformant](https://img.shields.io/badge/BNS--conformant-Full%20%7C%20Gold-10B981.svg?logo=dna&logoColor=white)](https://bionexus.org/verify?report=BNS-REP-2026-0001)
```

### HTML / Web Applications
```html
<a href="https://bionexus.org/verify?report=BNS-REP-2026-0001" target="_blank" rel="noopener noreferrer">
  <img src="https://raw.githubusercontent.com/HERRY423/BioNexus-spec/main/standards/bns-badge/assets/bns-conformant-full.svg" alt="BNS-conformant Full Gold" />
</a>
```

### Nextflow / nf-core Pipeline Header
```groovy
// Pipeline verified against BioNexus Conformance Test Suite (BCTS)
// Badge ID: BNS-BADGE-2026-0001 | Profile: BNS-Core
```
