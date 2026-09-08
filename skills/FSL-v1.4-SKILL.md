---
name: four-square-letterhead
version: "1.4"
description: Generate, update, validate and recall FSL v1.4 constitutional project artifacts with explicit development strategies, touchpoint sets and implementation references.
---

# Four-Square Letterhead Skill - v1.4

## Purpose
FSL v1.4 produces a compact 1-3 page project constitution / contract / technical letterhead. It preserves v1.3 traceability and adds two focused sections: DEVELOPMENT STRATEGY and IMPLEMENTATION REFERENCES.

## Non-negotiable model
- SPEC and MEMORY are fixed lanes.
- Two middle lanes are project-defined.
- Template version and governed project version MUST be shown separately.
- Binding clauses use stable IDs.
- Evidence uses CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT.
- MEMORY may remember law; MEMORY cannot make law.
- Do not exceed three pages.

## Development Strategy section
For each material iteration, capture:

```text
ITERATION
STRATEGY
TOUCHPOINT SET
START / MIDPOINT / END (where applicable)
EXPECTED EVIDENCE
EXIT CONDITION
```

Supported strategy tokens:
- `E2E`
- `E2M`
- `M2E`
- `PARALLEL E2E`
- `MEET-IN-THE-MIDDLE`
- `INCREMENTAL E2E`

Rules:
- Every material iteration MUST declare a strategy.
- Every material iteration MUST declare a Touchpoint Set.
- Every touchpoint in the declared set MUST be exercised meaningfully for the claimed path.
- An iteration MUST NOT be called E2E if a declared touchpoint is bypassed.
- A component test MUST NOT be represented as E2E proof.
- A tiny implementation at each touchpoint MAY be sufficient when it proves the path.
- The next iteration SHOULD grow from a proven path.
- Parallel paths MAY be used when their midpoint/integration contract is explicit.

Preferred development axiom:

**TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN.**

## Implementation References section
Use these classes only:
- `TECHNOLOGY`
- `LIBRARY`
- `REFERENCE`
- `LINK`

Recommended shape:

```text
CLASS | ITEM | FORCE | RELATION | PURPOSE | SOURCE
```

`RELATION` uses the v1.3 meanings:
- `REUSE`
- `INHERIT`
- `REFERENCE`

A class never implies force. If a technology/library/reference is mandatory or recommended, state MUST / SHOULD / MAY explicitly.

Do not turn FSL into a dependency inventory. Detailed versions, transitive dependencies and large reference lists SHOULD be placed in supporting artifacts and linked from FSL.

## Generation flow
1. Determine governed project identity and version.
2. Select 1P, 2P or 3P depth.
3. Determine project-selected middle lanes.
4. Extract constitutional requirements and assign stable IDs to material binding clauses.
5. Determine current development strategy and Touchpoint Set.
6. Capture key implementation references only.
7. Preserve traceability and conformance states.
8. Render DOCX/PDF.
9. Verify page count, version identity, normative emphasis and no clipping.
10. Package with memory, manifest, snapshot and checksums.

## Page depth guidance
- 1P: simple project; compact strategy line + essential references.
- 2P: medium project; explicit iteration strategy/touchpoint table + references table.
- 3P: complex project; detailed strategy map, proof/exit conditions and scoped references while remaining within three pages.

## Agent behavior
When development intent is ambiguous, the agent MUST NOT silently choose a stronger/weaker strategy or normative interpretation. Surface the ambiguity. Missing proof remains NOT YET PROVEN.
