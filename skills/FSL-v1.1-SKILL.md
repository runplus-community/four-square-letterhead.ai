---
name: four-square-letterhead
description: Generate, update, or recall a Four-Square Letterhead as a concrete file-backed artifact. Use for a reusable 1–3 page letterhead / technical-resume / release-identity document. SPEC and MEMORY are fixed lanes; the two middle lanes are selected per project. Always track the Four-Square template version separately from the project version.
---

# Four-Square Letterhead Skill — Template v1.1

## Purpose
Produce a polished project identity document that is useful to humans and AI: branch lineage, mission, boundaries, canonical workflows, project deliverables, validation, and release rules. The output is a real DOCX/PDF artifact, not theory alone.

## Template identity
Every generated page MUST show **Four-Square Template v1.1** in the header or footer. Keep it separate from the product/project contract or release version. Template updates increment the template version; ordinary project releases do not.

## Branch grammar
`main1` is the repository first commit / immutable root reference.

```text
main1
  ↓
[ spec-v1 | <lane-a>-v1 | <lane-b>-v1 | memory-v1 ]
  ↓
[ spec-v2 | <lane-a>-v2 | <lane-b>-v2 | memory-v2 ]
  ↓
...
```

**Fixed lanes:** `spec-vN` and `memory-vN`.
**Project lanes:** the middle two are selected to match the project and then remain stable across versions.

Examples: `code`, `tools`, `docs`, `utils`, `app`, `data`, `model`, `plugins`, `skills`, `ai`. Use the narrowest stable term. Use an umbrella when multiple related artifact classes form one concern; e.g. skills + plugins + agents -> `ai-vN`.

## Lane meaning
- **SPEC** — contract, requirements, workflows, schemas, invariants, compatibility promises, acceptance criteria.
- **LANE A** — project-specific major deliverable or execution family.
- **LANE B** — project-specific secondary concern or interface family.
- **MEMORY** — human + AI mnemonics, acronyms, glossary, recall maps, examples and learning aids; non-normative unless promoted into SPEC.

Do not hard-code TOOLS or AI into the universal model. They are valid project lanes, not permanent square names.

## Page-depth rule
Choose the shortest document that remains clear:
- **1 page** — simple project: identity, lineage, workflows, execution spine, four lane responsibilities, release rule.
- **2 pages** — medium project: add capability/compatibility/evidence and lane-selection detail.
- **3 pages maximum** — complex project: add operational constraints, performance baselines, release certification, compatibility ledger or deeper learning material.

Never exceed 3 pages. Do not compress unreadably just to remain on page 1. Header, footer, typography and template version stay consistent across pages.

## Required content
1. Product/project name and source of truth.
2. Project/contract version.
3. Four-Square template version.
4. One-sentence mission, core principle and boundary.
5. Chosen middle-lane tokens and why they are durable.
6. Five to eight canonical workflows.
7. Existing/proven implementations, libraries, services, docs or other assets reused.
8. Observable required outcomes.
9. Execution spine: Workflow -> Contract -> Adapter/Mechanism -> Proven Source -> Evidence -> Gate.
10. Conformance rule: pass = compliant; fail = does not ship.
11. Safety/evidence/release rules appropriate to the project.
12. `main1` lineage and `main` accepted integration role.

## Reuse rule
The execution source is not always a tool or code. It may be a library, binary kit, scripts, docs, service, dataset, model, plugin, utility, framework primitive, or other proven asset. Prefer reuse and wrapping/generalization before new implementation. New core work requires a documented capability gap.

## Agent / long-running work
Where applicable use: **Discover -> Plan -> Execute -> Observe -> Verify -> Record**. Long-running operations need durable identity/status/progress/cancel/result semantics only when the project actually supports such work. Do not invent background execution.

## Evidence
**Draft != Tested != Accepted != Released.** Scope claims to the artifact, platform and workflow actually validated.

## Recall behavior
When the user says “Four-Square Letterhead”, “recall Four-Square”, “use the Four-Square template”, or similar, retrieve/use the actual template/skill/sample files first when available. Do not respond with theory alone.

## Sample rule
For famous open-source examples, label the document **illustrative** unless the upstream project actually uses this branch model. Choose lanes that suit the example; do not force `tools` or `ai`.

## Output
Normal generation: DOCX + PDF. Reusable pack: 1pg/2pg/3pg blank templates + at least one illustrative sample + this skill + README + template-version manifest. Render and visually inspect every page before delivery.
