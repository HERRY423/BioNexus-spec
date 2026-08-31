# BioNexus Standards Governance Model

## 1. Specification Lifecycle States

Each BNS specification document transitions through formal lifecycle states:

`mermaid
stateDiagram-v2
    [*] --> DRAFT : RFC Accepted
    DRAFT --> PROPOSED_STANDARD : Reference Implementation & Conformance Tests
    PROPOSED_STANDARD --> DRAFT_STANDARD : Multi-Host Verification & Zero Known Contradictions
    DRAFT_STANDARD --> STABLE_STANDARD : Dual Independent Implementation & Interop Trial
    STABLE_STANDARD --> DEPRECATED : Superseded by newer BNS with Migration Path
`

| Lifecycle State | Definition | Normative Requirement |
|---|---|---|
| DRAFT | Initial proposal undergoing technical formulation | Non-normative, subject to breaking change |
| PROPOSED_STANDARD | Feature-complete specification with initial reference implementation | Normative candidate, RFC period open |
| DRAFT_STANDARD | Validated across reference test suites with stable schema | Normative, backward-compatible within minor versions |
| STABLE_STANDARD | Verified by $\ge 2$ independent implementations across multi-host environments | Strictly locked, breaking changes require major version + new RFC |
| DEPRECATED | Explicitly replaced or retired under the Deprecation Policy | Maintained for archival reference, migration guide mandatory |

---

## 2. Decision-Making & Consensus

1. **Rough Consensus & Working Code**:
   In the tradition of IETF, W3C, and GA4GH, decisions favor demonstrated technical feasibility and formal invariant verification over abstract speculation.
2. **Voting Thresholds**:
   - *Errata & Clarifications*: Simple majority ($> 50\%$) of active Working Group maintainers.
   - *New RFC Adoption / New BNS Spec*: Supermajority ($> 66\%$) approval with zero blocking mathematical/scientific objections.
   - *Breaking Change / Deprecation*: Supermajority ($> 75\%$) with mandatory deprecation notice period ($\ge 6$ months).

---

## 3. Transparency & Open Participation

All discussions, RFC reviews, and decision records MUST be public on GitHub Issues and Pull Requests. No private or unrecorded agreements carry normative weight.
