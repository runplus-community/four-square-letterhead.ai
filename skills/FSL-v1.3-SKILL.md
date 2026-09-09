---
name: four-square-letterhead
description: Generate, update, validate or recall FSL v1.3 as a concrete file-backed constitutional project artifact with stable clause IDs, scoped evidence, four-commit release snapshots, separate FSL/project version identities, explicit AI authority boundaries, and ordered end-to-end iteration development.
---

# Four-Square Letterhead Skill - Template v1.3

## Purpose
FSL v1.3 produces a compact project constitution / contract / technical letterhead for humans and AI. It MUST remain 1-3 pages and SHOULD push detailed evidence and development records into referenced supporting artifacts.

## Preserve the v1.2 constitutional vocabulary
Use MUST / MUST NOT, SHOULD / SHOULD NOT, MAY, EXCEPTION / WAIVER and the existing ARTICLE / LAW / CONTRACT / POLICY / GUARDRAIL / RECOMMENDED PRACTICE / CHECKLIST forms. Do not invent new categories when an existing form is sufficient.

Rendered normative keywords MUST be CAPITALIZED, bold and underlined.

## Clause IDs
Every material binding clause MUST have a stable ID. Use `FORM-SCOPE-NNN`, e.g. `LAW-SPEC-001`, `GUARD-WORKSTUDIO-003`, `CONTRACT-AI-002`. A published ID MUST NOT be reused for another meaning.

## Version identity
Every page MUST show both identities separately:
- `Four-Square Template v1.3` = FSL governance language
- project / contract / sample version = governed system

They MUST NOT be conflated.

## Four-Square branch model
SPEC and MEMORY are fixed. Two middle lanes are project-defined and SHOULD remain stable across versions.

```text
main1
  ↓
[ spec-vN | <lane-a>-vN | <lane-b>-vN | memory-vN ]
```

MEMORY may remember law; MEMORY cannot make law. MEMORY MUST NOT create or amend normative requirements unless promoted into SPEC.

## Reuse semantics
Distinguish when relevant:
- REUSE = use a proven capability; do not automatically import source law/assumptions.
- INHERIT = explicitly adopt a requirement/contract.
- REFERENCE = use evidence/knowledge without adopting its law.

## Scoped proof
For material conformance claims, use:
`CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT`.

RESULT must be one of CONFORMANT, CONFORMANT WITH EXCEPTION, NON-CONFORMANT or NOT YET PROVEN. Claims MUST NOT be generalized beyond what was tested.

## Four-commit release snapshot
Accepted Four-Square releases MUST record the exact commit IDs for SPEC, lane A, lane B and MEMORY in a lightweight snapshot. The snapshot MUST NOT replace Git. Prefer a YAML file based on `FSL-v1.3-SNAPSHOT.example.yaml`.

## AI ambiguity rule
If normative intent is ambiguous, an agent MUST NOT silently choose the stronger or weaker interpretation. Surface the ambiguity for review. Until resolved, do not claim conformance on that interpretation; use NOT YET PROVEN where evidence is missing.

## Iteration + touchpoint development
Development uses small ordered end-to-end iterations.

**Every material iteration MUST close an end-to-end loop for one small requirement and produce observable evidence.** Do not stop at "implemented".

End-to-end means the complete path for that iteration, not the whole final product:

```text
requirement -> rule -> implementation -> usable state -> checker -> evidence -> PROVEN
```

Each iteration SHOULD start from the latest PROVEN baseline and SHOULD preserve already-proven behavior unless its requirement explicitly changes it.

### Touchpoints
Touchpoints are system surfaces, not branches. Projects keep a small durable touchpoint vocabulary, for example:

`SPEC | Template | Foundation | Materialization | Runtime | Manager | Access | Checker | AI | Memory | Evidence | Package`

For each iteration, classify relevant touchpoints as:

`CHANGE | VERIFY | NOT AFFECTED`

Branches answer **who owns responsibility**. Touchpoints answer **where the iteration crosses the system**.

### Ordered sequence CSV
Use one short ordered CSV as the development spine:

```csv
Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status
```

Recommended statuses:

`PLANNED | ACTIVE | PROVEN | BLOCKED`

Every row SHOULD represent one working vertical slice. The sequence SHOULD be cumulative: the next row grows from the previous PROVEN baseline.

Use `FSL-v1.3-ITERATIONS.csv` as the reusable starting template when available.

### Development loop

```text
SELECT SMALL REQUIREMENT
-> MAP TOUCHPOINTS
-> BUILD END TO END
-> CHECK EACH TOUCHPOINT
-> VERIFY + RECORD EVIDENCE
-> ACCEPT ITERATION
-> LEARN
-> NEXT ITERATION
```

Short axiom: **ITERATE -> TOUCH -> PROVE -> LEARN -> INCREMENT**.

A change SHOULD touch the smallest number of branches necessary, but all four branches SHOULD be inspected for impact before the iteration is accepted.

## Development governance
Material work SHOULD use visible checklists. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibilities. Existing proven assets SHOULD be evaluated before new core work.

## Page-depth rule
- 1 page: simple identity + core laws + traceability/release essentials.
- 2 pages: add clause-ID rules, proof scope, release snapshot and authority boundaries.
- 3 pages maximum: add evidence ledger, release certification and amendment detail.

Do not exceed three pages. Do not compress unreadably.

## Required content
1. Project/product name and source of truth.
2. Project version separately from FSL template version.
3. `Four-Square Template v1.3` on every page.
4. Mission, core principle and boundary.
5. Four-Square lineage and chosen middle lanes.
6. Canonical workflows/contracts and REUSE/INHERIT/REFERENCE semantics where relevant.
7. Normative language legend.
8. Stable clause IDs for material binding clauses.
9. Conformance declaration.
10. Proof tuple for material claims when space/complexity requires it.
11. Four-commit release snapshot for accepted releases.
12. AI ambiguity and MEMORY authority rules.
13. For development work: ordered iteration CSV, end-to-end path, touchpoints and proof.

## Recall behavior
When the user says FSL, Four-Square Letterhead, recall FSL, or use the FSL template, retrieve/use the actual v1.3 file-backed templates, sample, skill, memory, manifest, development strategy, iteration CSV, snapshot example and traceability guide first when available. Do not return theory alone.

## Sample rule
Famous open-source samples MUST be marked illustrative unless the upstream project actually uses FSL. Do not imply endorsement or upstream governance.

## Output / validation
Normal generation: DOCX + PDF. Reusable pack: 1P/2P/3P templates + sample + constitution + skill + memory + manifest + development strategy + iteration CSV + traceability guide + snapshot example + README + checksums. Render and visually inspect every page. Verify exact page counts, template version, project/sample version separation, clause IDs and normative emphasis before release.
