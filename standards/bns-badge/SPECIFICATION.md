# BioNexus Conformant Badge Specification ("BNS-conformant")

**Status**: Active Standard | **Version**: 1.0.0  
**Governs**: `standards/bns-badge/`, Badge Visual Grammar, Machine-Readable Metadata, Verification Endpoints, SVG Assets.

---

## 1. Executive Vision

> *"He who issues the certificate of conformity defines the yardstick of the industry."*

The **`BNS-conformant`** badge is the universally recognized mark of epistemic reliability and scientific invariant compliance. Displaying this badge signifies that a biological AI agent, computational workflow, or software tool has executed the authoritative **BioNexus Conformance Test Suite (BCTS)** and deterministically proven:
1. Zero hallucination of biological identifiers or statistical significance.
2. Strict adherence to negative binomial and discrete count invariants.
3. Zero silent substitution or mock execution.
4. Cryptographically verifiable W3C PROV-O provenance.

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

A `BNS-conformant` badge is never a static ungrounded image. Every generated badge contains embedded RDF/XML and JSON-LD metadata binding:
- **`subject_sha256`**: Exact SHA-256 hash of the target software release / model weight / workflow bundle.
- **`report_id`**: Canonical identifier of the passing Conformance Test Report.
- **`report_sha256`**: Cryptographic digest of the test report payload.
- **`verification_endpoint`**: Public URL where third parties can verify test vectors and signatures.

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
