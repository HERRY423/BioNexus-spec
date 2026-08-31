# BioNexus Specification Deprecation & Versioning Policy

## 1. Monotonic Numbering Rule (BNS-ID Invariant)

- **Permanent ID Allocation**: Specification numbers (BNS-001, BNS-002, ..., BNS-nnn) are strictly monotonic and permanent.
- **No Recycling**: A deprecated or withdrawn BNS ID is NEVER recycled for a different topic.
- **Supersession**: When a specification is fundamentally revised, a new BNS number is allocated, and the old specification is marked SUPERSEDED_BY BNS-xxx with an explicit migration chapter.

---

## 2. Specification Versioning Schema

BioNexus Specifications follow Semantic Versioning (SemVer 2.0.0):
\text{MAJOR}.\text{MINOR}.\text{PATCH}

1. **MAJOR ($\Delta \text{MAJOR}$)**: Breaking changes to normative invariants, protocol packet formats, or mandatory claim schemas.
2. **MINOR ($\Delta \text{MINOR}$)**: Backward-compatible additions of new capability contracts, optional evidence grades, or semantic vocabulary extensions.
3. **PATCH ($\Delta \text{PATCH}$)**: Non-normative errata, editorial clarifications, and documentation corrections.

---

## 3. Deprecation Timelines & Compatibility Windows

1. **Deprecation Notice**: A specification intended for deprecation MUST enter the DEPRECATION_PENDING state for at least **180 days** prior to formal retirement.
2. **Migration Guide**: Any deprecating RFC MUST supply a machine-readable transform or compatibility wrapper schema.
3. **Archival Preservation**: Retired specifications remain permanently accessible in the spec/ archive with their final checksums.
