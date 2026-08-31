# BioNexus RFC Process (Request for Comments)

The BioNexus RFC process provides a structured, collaborative, and consensus-driven mechanism to evolve the **BioNexus Specifications (BNS)**.

## How to Propose an RFC

1. **Copy the Template**: Copy [
fc-template.md](rfc-template.md) to RFC-xxxx-your-feature-name.md.
2. **Draft the Proposal**: Detail the problem, mathematical invariants, schema changes, backward compatibility, and reference implementation plan.
3. **Submit a Pull Request**: Open a PR against ionexus-spec titled RFC: <Your Title>.
4. **Community Review**: The proposal undergoes public review and Technical Steering Committee evaluation.
5. **Disposition**: Once consensus is reached, the RFC is assigned a sequential number and marked ACCEPTED, REJECTED, or WITHDRAWN.

---

## RFC Lifecycle States

- **DRAFT**: Author is writing the proposal.
- **UNDER_REVIEW**: Open for community discussion ($\ge 14$ days).
- **ACCEPTED**: Approved for implementation as a BNS specification or revision.
- **IMPLEMENTED**: Fully realized in normative specification documents and verified by reference implementations.
- **REJECTED / WITHDRAWN**: Closed without standard adoption.
- **SUPERSEDED**: Replaced by a newer RFC.
