---
name: four-square-letterhead
description: Generate, update, validate or recall FSL v1.3 as a concrete file-backed constitutional project artifact with stable clause IDs, scoped evidence, four-commit release snapshots, separate FSL/project version identities, explicit AI authority boundaries, and ordered end-to-end iteration development.
---

# Four-Square Letterhead Skill - Template v1.3

## Purpose
FSL v1.3 produces a compact project constitution / contract / technical letterhead for humans and AI. It MUST remain 1-3 pages and SHOULD push detailed evidence into referenced supporting artifacts.

## Constitutional vocabulary
Use MUST / MUST NOT, SHOULD / SHOULD NOT, MAY, EXCEPTION / WAIVER and ARTICLE / LAW / CONTRACT / POLICY / GUARDRAIL / RECOMMENDED PRACTICE / CHECKLIST. Do not invent new categories when an existing form is sufficient. Rendered normative keywords MUST be CAPITALIZED, bold and underlined.

## Clause IDs
Every material binding clause MUST have a stable `FORM-SCOPE-NNN` ID, e.g. `LAW-SPEC-001`, `GUARD-WORKSTUDIO-003`, `CONTRACT-AI-002`. A published ID MUST NOT be reused for another meaning.

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
- REUSE = use a proven capability without automatically importing source law/assumptions.
- INHERIT = explicitly adopt a requirement/contract.
- REFERENCE = use evidence/knowledge without adopting its law.

## Scoped proof
Use `CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT`. RESULT is CONFORMANT, CONFORMANT WITH EXCEPTION, NON-CONFORMANT or NOT YET PROVEN. Claims MUST NOT be generalized beyond what was tested.

## Four-commit release snapshot
Accepted releases MUST record the exact commit IDs for SPEC, lane A, lane B and MEMORY. The snapshot MUST NOT replace Git.

## AI ambiguity rule
If normative intent is ambiguous, an agent MUST NOT silently choose the stronger or weaker interpretation. Surface the ambiguity for review.

## Iteration + touchpoint development
Development uses small ordered end-to-end iterations.

**Every material iteration MUST close one small requirement from requirement -> implementation -> usable state -> checker -> evidence -> PROVEN.** `Implemented` alone is not complete.

Each iteration SHOULD start from the latest PROVEN baseline and preserve already-proven behavior unless explicitly changed.

Touchpoints are system surfaces, not branches. A compact project vocabulary may include:

`SPEC | Template | Foundation | Materialization | Runtime | Manager | Access | Checker | AI | Memory | Evidence | Package`

Relevant touchpoints MUST be inspected and classified `CHANGE | VERIFY | NOT AFFECTED`, but this detail does not have to be encoded in the CSV. Keep the CSV readable.

### Ordered sequence CSV
Use one short ordered CSV:

```csv
Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status
```

Statuses: `PLANNED | ACTIVE | PROVEN | BLOCKED`.

Seed only a few kickoff iterations. Do not try to predict the full final roadmap up front. Add later rows as earlier iterations become PROVEN and learning improves the next decision.

Every row is one working vertical slice; the next row grows from the previous PROVEN baseline. Use `FSL-v1.3-ITERATIONS.csv` as the reusable starting template.

Short axiom: **ITERATE -> TOUCH -> PROVE -> LEARN -> INCREMENT**.

A change SHOULD touch the smallest number of branches necessary, but all four branches SHOULD be inspected for impact before acceptance.

## Development governance
Material work SHOULD use visible checklists. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibilities. Existing proven assets SHOULD be evaluated before new core work.

## Page-depth rule
- 1 page: simple identity + core laws + traceability/release essentials.
- 2 pages: add clause-ID rules, proof scope, release snapshot and authority boundaries.
- 3 pages maximum: add evidence ledger, release certification and amendment detail.

Do not exceed three pages or compress unreadably.

## Required content
1. Project/product name and source of truth.
2. Project version separately from FSL template version.
3. `Four-Square Template v1.3` on every page.
4. Mission, core principle and boundary.
5. Four-Square lineage and chosen middle lanes.
6. Canonical workflows/contracts and reuse semantics where relevant.
7. Normative language legend and stable clause IDs.
8. Conformance declaration and scoped proof where needed.
9. Four-commit snapshot for accepted releases.
10. AI ambiguity and MEMORY authority rules.
11. For development work: one short ordered iteration CSV with a few kickoff rows.

## Recall behavior
When the user says FSL or Four-Square Letterhead, retrieve/use the actual v1.3 file-backed templates, sample, constitution, skill, checklist, memory, manifest, iteration CSV, snapshot example and traceability guide first when available. Do not return theory alone.

## Sample rule
Famous open-source samples MUST be marked illustrative unless the upstream project actually uses FSL.

## Output / validation
Normal generation: DOCX + PDF. Reusable pack: 1P/2P/3P templates + sample + constitution + skill + checklist + memory + manifest + iteration CSV + traceability guide + snapshot example + README + checksums. Render and visually inspect every page; verify page count, version separation, clause IDs and normative emphasis before release.
