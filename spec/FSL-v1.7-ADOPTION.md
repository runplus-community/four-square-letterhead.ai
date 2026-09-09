# FSL v1.7 - New projects and existing systems

**Adopt the present. Do not rewrite the past.**

## Start concrete

`[ SPEC | SYSTEM | AI | MEMORY ]`

SPEC starts with the project's completed FSL letterhead, then scope, requirements, contracts, guardrails, acceptance and important routes. Appendix, errata and amendments are useful optional SPEC documents. SYSTEM delivers the product. AI supplies project instructions and AI capabilities. MEMORY retains decisions, context and evidence links.

Only SPEC and MEMORY are fixed. SYSTEM and AI are recommended defaults, not compulsory renames. FSL's own TEMPLATES / SKILL specialization remains appropriate. A non-AI project can retain a meaningful DOCS concern or explicitly declare AI inactive; neither choice permits fabricated execution evidence.

Ownership follows purpose, not author. Agent-written product code belongs to SYSTEM; an adopted requirement belongs to SPEC; prompts/skills belong to AI; handover belongs to MEMORY. Use one authoritative owner and references or generated copies, not independently edited competing sources.

## New project

Draft the minimum useful contract and primary route. Recommend one short initial sequence: `I-001: tiny R-01 -> verify -> grow`. Future iterations need not be predicted. Parallel E2E, E2M and M2E are useful options, not additional mandatory fields. The primary route states the required touchpoints and observable outcome.

## Existing project

Use study or reverse engineering as needed: inspect actual code, documentation, tests, runtime behavior, deployment and stakeholder intent. Identify a reviewed adoption baseline rather than reconstructing its development history.

A concise adoption note can state:

`Repository/commit: [...] / Scope: [...] / Intended SPEC: [...] / Critical route: R-01 / Known gaps: [...] / Evidence: [...]`

This is guidance, not a new schema or required file. Its information can live in the project FSL and existing evidence notes.

Separate **OBSERVED / AS-IS** behavior from **ADOPTED / INTENDED** requirements. An accidental quirk, historical workaround or old bug is not automatically an obligation. Record the gap, seek the responsible decision and scope any conformance claim to actual evidence. A reviewed baseline can be documented before all its claims are proven; mark unresolved claims NOT YET PROVEN.

Historical iterations, reconstructed iterations and future iteration plans are optional. FSL must not require rewriting history or rebuilding a working capability merely to adopt the method. A representative run proves only the chosen boundary and environment, not the entire existing system.

## Repository lineage

For a new repository, `main1` points at the original first commit, initial lanes begin there, and matching lane versions continue their predecessors. For an existing repository, new adoption lanes may begin at the reviewed current-state adoption commit. Preserve existing justified lineage. Do not move `main1` to the adoption point or claim old commits used FSL.

Record repository plus exact reviewed commits. A branch name is neither a repository identifier nor a frozen snapshot. `main` is accepted integration; verify the four reviewed squares together. Keep consuming-project work in its own repository, never in the FSL reference repository.

## Let supporting documents grow only when useful

Before release, update reviewed draft intent directly. An appendix may hold discovery maps, reverse-engineering notes, diagrams, examples or migration reasoning. No empty appendix, errata or amendment files are required.

After release, keep its SPEC frozen. Explanation goes in appendix; a correction that preserves intent goes in errata; a new or changed promise needs an explicitly adopted amendment. The next release incorporates the applicable adopted changes and remains traceable to the preceding baseline.

Authority: Constitution POLICY-SQUARE-003, LAW-SPEC-001, LAW-OWN-001, LAW-ADOPT-001 / 002 and Article XII.
