# Four-Square Letterhead (FSL) v1.3 Constitution

## Preamble
FSL is a compact, file-backed project constitution and letterhead for humans and AI. FSL MUST remain small enough to scan quickly; detailed implementation evidence SHOULD live in referenced supporting artifacts rather than expanding the letterhead beyond three pages.

## Article I - Authority and normative language
**LAW-LANG-001 — MUST.** MUST / MUST NOT define binding requirements and prohibitions. SHALL / SHALL NOT are constitutional aliases; MUST / MUST NOT are preferred for machine-readable clarity.

**LAW-LANG-002 — SHOULD.** SHOULD / SHOULD NOT define strong expectations. A deviation SHOULD have a recorded reason. MAY defines permission.

**LAW-LANG-003 — MUST NOT.** A binding requirement MUST NOT be silently weakened, bypassed, guessed away, or converted into a recommendation.

**LAW-LANG-004 — MUST.** When evidence is absent, the result MUST be NOT YET PROVEN rather than assumed conformant.

**LAW-LANG-005 — MUST.** In rendered FSL pages, normative keywords MUST be CAPITALIZED, bold and underlined. This emphasis MUST NOT be used decoratively where it could be mistaken for normative force.

## Article II - Constitutional forms
FSL keeps the v1.2 forms: ARTICLE, LAW, CONTRACT, POLICY, GUARDRAIL, RECOMMENDED PRACTICE and CHECKLIST. The form label alone does not determine force; the normative keyword does. FSL SHOULD NOT add new constitutional categories when an existing form is sufficient.

## Article III - Four-Square structure
**LAW-SQUARE-001 — MUST.** SPEC and MEMORY MUST remain fixed lanes. Two middle lanes are selected per project from durable concerns.

**POLICY-SQUARE-002 — SHOULD.** Middle-lane names SHOULD use the narrowest stable vocabulary and SHOULD remain stable across versions unless a reviewed migration changes the model.

**LAW-MEMORY-001 — MUST NOT.** MEMORY MUST NOT create or amend normative requirements unless those requirements are promoted into SPEC. Design axiom: **MEMORY may remember law; MEMORY cannot make law.**

```text
main1
  ↓
[ spec-v1 | <lane-a>-v1 | <lane-b>-v1 | memory-v1 ]
  ↓
[ spec-v2 | <lane-a>-v2 | <lane-b>-v2 | memory-v2 ]
```

`main1` is the first commit / immutable root reference. `main` is accepted integration.

## Article IV - Clause identity and traceability
**LAW-TRACE-001 — MUST.** Every material binding clause MUST have a stable clause ID. Recommended grammar: `FORM-SCOPE-NNN`, e.g. `LAW-SPEC-001`, `GUARD-WORKSTUDIO-003`, `CONTRACT-AI-002`.

**LAW-TRACE-002 — MUST NOT.** A published clause ID MUST NOT be reused for a different meaning. An amended clause MAY retain its ID when lineage remains clear; a materially different obligation SHOULD receive a new ID.

**CONTRACT-TRACE-003 — SHOULD.** Each material binding clause SHOULD map to observable verification and evidence.

## Article V - Framework version vs project version
**LAW-VERSION-001 — MUST.** Every generated FSL page MUST identify the FSL template/framework version and the governed project/version separately.

**LAW-VERSION-002 — MUST NOT.** Template version identifies the FSL governance language. Project version identifies the governed system. They MUST NOT be conflated.

## Article VI - Scoped proof
The standard evidence tuple is: `CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT`.

**LAW-PROOF-001 — MUST.** A conformance claim MUST NOT be generalized beyond the artifact, workflow, environment and evidence actually validated.

**CONTRACT-PROOF-002 — SHOULD.** Material binding clauses SHOULD have a proof record using the standard evidence tuple. RESULT uses the canonical states: CONFORMANT, CONFORMANT WITH EXCEPTION, NON-CONFORMANT or NOT YET PROVEN.

## Article VII - Four-Square release snapshot
**LAW-SNAPSHOT-001 — MUST.** An accepted Four-Square release MUST record the exact reviewed commit IDs for SPEC, middle lane A, middle lane B and MEMORY.

**LAW-SNAPSHOT-002 — MUST NOT.** The snapshot MUST NOT replace Git or become an independent registry. Git commit identity remains authoritative; the snapshot records the reviewed four-commit view.

A minimal snapshot SHOULD contain FSL version, project, project version, four branch names and four commit IDs.

## Article VIII - Reuse, inheritance and reference
- **REUSE**: use an existing proven capability without automatically adopting its source law or assumptions.
- **INHERIT**: explicitly adopt an existing requirement or contract. Inherited obligations MUST be identified as adopted.
- **REFERENCE**: use knowledge, evidence or prior decisions without adopting their normative authority.

**POLICY-RELATION-001 — SHOULD.** When assumptions could leak across project boundaries, FSL SHOULD distinguish REUSE, INHERIT and REFERENCE explicitly.

## Article IX - AI ambiguity rule
**LAW-AI-001 — MUST NOT.** When normative intent is ambiguous, an agent MUST NOT silently choose the stronger or weaker interpretation.

**LAW-AI-002 — MUST.** The agent MUST surface the ambiguity for review and MUST NOT claim conformance on the unresolved interpretation. Missing proof remains NOT YET PROVEN.

## Article X - Iterative end-to-end development
**LAW-DEV-001 — MUST.** Every material development iteration MUST produce one observable end-to-end outcome and evidence. End-to-end means the complete path for that iteration's small requirement, not the entire final product.

**LAW-DEV-002 — MUST NOT.** An iteration MUST NOT be considered complete at "implemented" alone. The requirement -> implementation -> usable state -> checker -> evidence loop MUST close.

**POLICY-DEV-003 — SHOULD.** Each iteration SHOULD begin from the latest PROVEN baseline and SHOULD preserve previously proven behavior unless the current requirement explicitly changes it.

**LAW-DEV-004 — MUST.** Every iteration MUST inspect its relevant touchpoints and classify them as `CHANGE`, `VERIFY`, or `NOT AFFECTED`.

**LAW-DEV-005 — MUST NOT.** Touchpoints MUST NOT be treated as branches. Branches identify responsibility ownership; touchpoints identify the system surfaces crossed by an iteration.

**POLICY-DEV-006 — SHOULD.** Development SHOULD use one short ordered sequence CSV as its spine. Recommended columns are `Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status`; recommended states are `PLANNED`, `ACTIVE`, `PROVEN`, `BLOCKED`.

**POLICY-DEV-007 — SHOULD.** A change SHOULD touch the smallest number of branches necessary, while all four branches SHOULD be inspected for impact before the iteration is accepted.

**POLICY-DEV-008 — SHOULD.** Later design decisions SHOULD use evidence and learning from earlier proven iterations rather than assuming the final implementation is fully known in advance.

Short development axiom: **ITERATE -> TOUCH -> PROVE -> LEARN -> INCREMENT.**

## Article XI - Amendments and page boundary
Binding constitutional changes MUST be made in SPEC and versioned. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibility.

**LAW-PAGE-001 — MUST NOT.** FSL MUST NOT exceed three pages. Details that outgrow the letterhead SHOULD move to supporting artifacts referenced by clause ID or proof record.

## Release axiom
**One version, four squares, all green.**
