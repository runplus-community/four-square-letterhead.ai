---
name: four-square-letterhead
description: Generate, update, validate, or recall a Four-Square Letterhead as a concrete file-backed constitutional project artifact. FSL v1.2 supports 1-3 pages, fixed SPEC and MEMORY lanes, two project-selected middle lanes, explicit normative language, conformance declarations, and visible template-version tracking.
---

# Four-Square Letterhead Skill - Template v1.2

## Purpose
FSL v1.2 produces a compact project constitution / contract / technical letterhead for humans and AI. It distinguishes binding law from strong guidance, permission, examples and memory. The output is a real DOCX/PDF artifact, not theory alone.

## Constitutional center
FSL MUST make the force of important statements explicit. Binding requirements MUST NOT be silently weakened, bypassed, inferred away, or treated as recommendations. A deviation from binding law MUST be visible.

### Canonical normative vocabulary
- **MUST / MUST NOT** - binding requirement / prohibition. Violation means **NON-CONFORMANT** unless a valid explicit exception applies.
- **SHALL / SHALL NOT** - constitutional aliases for MUST / MUST NOT. Prefer MUST / MUST NOT for machine-readable clarity.
- **SHOULD / SHOULD NOT** - strong expected practice / strong avoidance. Deviation SHOULD include a recorded reason but does not automatically require a waiver.
- **MAY** - permitted option.
- **EXCEPTION / WAIVER** - explicit, scoped departure from binding law.

In rendered FSL documents, normative keywords MUST be CAPITALIZED, bold and underlined. Typography MUST NOT be used decoratively when it could be mistaken for normative force.

## Constitutional forms
- **ARTICLE** - groups a subject.
- **LAW** - binding clause; normally uses MUST / MUST NOT.
- **CONTRACT** - observable promise, interface or result with evidence.
- **POLICY** - standing rule whose force is stated by a normative keyword.
- **GUARDRAIL** - protective boundary, often a MUST NOT.
- **RECOMMENDED PRACTICE** - preferred method, usually SHOULD / SHOULD NOT / MAY.
- **CHECKLIST** - execution/review aid. A checklist is not constitutional law unless a LAW or CONTRACT makes it required.

## Conformance states
Every material release or review SHOULD be expressible as one of:
1. **CONFORMANT**
2. **CONFORMANT WITH EXCEPTION**
3. **NON-CONFORMANT**
4. **NOT YET PROVEN**

A missing proof MUST NOT be converted into assumed success. Use NOT YET PROVEN. A MUST / MUST NOT deviation MUST NOT be silently accepted.

## Exception / waiver protocol
A binding exception MUST identify: clause, scope, owner, rationale, evidence, and review/expiry condition where applicable. Agents MUST NOT create, infer, or approve a waiver unless project authority explicitly permits it.

## Development governance
Development SHOULD use a checklist-driven approach for material work. Each binding clause SHOULD map to a verification item and observable evidence.

AI agents MAY be used for Discover -> Plan -> Execute -> Observe -> Verify -> Record. Agent responsibilities SHOULD be explicit. Agents MUST NOT reinterpret or waive constitutional law without explicit authority.

## Branch grammar
`main1` is the repository first commit / immutable root reference.

```text
main1
  ↓
[ spec-v1 | <lane-a>-v1 | <lane-b>-v1 | memory-v1 ]
  ↓
[ spec-v2 | <lane-a>-v2 | <lane-b>-v2 | memory-v2 ]
```

SPEC and MEMORY are fixed lanes. The middle two lanes are selected per project and SHOULD remain stable across versions. Use the narrowest durable lane names. Umbrella names MAY be used when appropriate, e.g. agents + skills + plugins -> `ai-vN`.

MEMORY is non-normative and MUST NOT create new requirements unless promoted into SPEC.

## Page-depth rule
Use the shortest readable document:
- 1 page - simple project constitution / identity.
- 2 pages - add articles, law/policy detail, capability and development governance.
- 3 pages maximum - add amendments, exception ledger, conformance matrix and release certification.

Do not exceed 3 pages. Do not compress unreadably to remain on one page.

## Required content
1. Project/product name and source of truth.
2. Project/contract version.
3. **Four-Square Template v1.2** on every generated page.
4. Mission, core principle and boundary.
5. `main1` lineage and the four lanes.
6. Chosen middle-lane tokens.
7. Canonical workflows and observable outcomes.
8. Constitutional language legend.
9. Laws/contracts/policies/guardrails appropriate to the project.
10. Conformance declaration.
11. Development checklist/agent guidance when applicable.
12. Evidence/release rule.

## Reuse rule
The project execution source is not always a tool or code. It MAY be a library, binary kit, script, document set, service, dataset, model, plugin, utility, framework primitive or other proven asset. Prefer proven reuse before new implementation. New core work SHOULD have a documented capability gap.

## Evidence rule
Draft != Tested != Accepted != Released. Every claim MUST be scoped to the artifact, platform, workflow and evidence actually validated.

## Recall behavior
When the user says FSL, Four-Square Letterhead, recall FSL, or use the Four-Square template, retrieve/use the actual v1.2 file-backed templates, sample, skill, memory and manifest first when available. Do not return theory alone.

## Sample rule
Famous open-source examples MUST be marked illustrative unless the upstream project actually uses the Four-Square branch/constitutional model. Do not imply upstream endorsement or governance.

## Output / validation
Normal generation: DOCX + PDF. Reusable pack: 1P/2P/3P templates + at least one illustrative sample + skill + memory + manifest + README + checksums. Render and visually inspect every page. Verify exact page counts and template-version markers before release.
