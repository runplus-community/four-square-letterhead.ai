# Four-Square Letterhead (FSL) v1.4 Constitution

## Preamble
FSL is a compact, file-backed project constitution and letterhead for humans and AI. FSL MUST remain small enough to scan quickly; detailed implementation evidence SHOULD live in referenced supporting artifacts rather than expanding the letterhead beyond three pages.

FSL v1.4 preserves the v1.3 constitutional language, traceability, proof and snapshot model, and adds two focused capabilities: explicit development strategies and implementation references.

## Article I - Authority and normative language
**LAW-LANG-001 — MUST.** MUST / MUST NOT define binding requirements and prohibitions. SHALL / SHALL NOT are constitutional aliases; MUST / MUST NOT are preferred for machine-readable clarity.

**LAW-LANG-002 — SHOULD.** SHOULD / SHOULD NOT define strong expectations. A deviation SHOULD have a recorded reason. MAY defines permission.

**LAW-LANG-003 — MUST NOT.** A binding requirement MUST NOT be silently weakened, bypassed, guessed away, or converted into a recommendation.

**LAW-LANG-004 — MUST.** When evidence is absent, the result MUST be NOT YET PROVEN rather than assumed conformant.

**LAW-LANG-005 — MUST.** In rendered FSL pages, normative keywords MUST be CAPITALIZED, bold and underlined. This emphasis MUST NOT be used decoratively where it could be mistaken for normative force.

## Article II - Constitutional forms
FSL uses ARTICLE, LAW, CONTRACT, POLICY, GUARDRAIL, RECOMMENDED PRACTICE and CHECKLIST. The form label alone does not determine force; the normative keyword does. FSL SHOULD NOT add new constitutional categories when an existing form is sufficient.

## Article III - Four-Square structure
**LAW-SQUARE-001 — MUST.** SPEC and MEMORY MUST remain fixed lanes. Two middle lanes are selected per project from durable concerns.

**POLICY-SQUARE-002 — SHOULD.** Middle-lane names SHOULD use the narrowest stable vocabulary and SHOULD remain stable across versions unless a reviewed migration changes the model.

**LAW-MEMORY-001 — MUST NOT.** MEMORY MUST NOT create or amend normative requirements unless those requirements are promoted into SPEC. Design axiom: **MEMORY may remember law; MEMORY cannot make law.**

```text
main1
  ↓
[ spec-vN | <lane-a>-vN | <lane-b>-vN | memory-vN ]
```

`main1` is the first commit / immutable root reference. `main` is accepted integration.

## Article IV - Clause identity and traceability
**LAW-TRACE-001 — MUST.** Every material binding clause MUST have a stable clause ID. Recommended grammar: `FORM-SCOPE-NNN`.

**LAW-TRACE-002 — MUST NOT.** A published clause ID MUST NOT be reused for a different meaning.

**CONTRACT-TRACE-003 — SHOULD.** Each material binding clause SHOULD map to observable verification and evidence.

## Article V - Framework version vs project version
**LAW-VERSION-001 — MUST.** Every generated FSL page MUST identify the FSL template/framework version and the governed project/version separately.

**LAW-VERSION-002 — MUST NOT.** Template version identifies the FSL governance language. Project version identifies the governed system. They MUST NOT be conflated.

## Article VI - Scoped proof
The standard evidence tuple is: `CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT`.

**LAW-PROOF-001 — MUST.** A conformance claim MUST NOT be generalized beyond the artifact, workflow, environment and evidence actually validated.

**CONTRACT-PROOF-002 — SHOULD.** Material binding clauses SHOULD have a proof record using the standard evidence tuple.

## Article VII - Four-Square release snapshot
**LAW-SNAPSHOT-001 — MUST.** An accepted Four-Square release MUST record the exact reviewed commit IDs for SPEC, middle lane A, middle lane B and MEMORY.

**LAW-SNAPSHOT-002 — MUST NOT.** The snapshot MUST NOT replace Git or become an independent registry. Git commit identity remains authoritative.

## Article VIII - Reuse, inheritance and reference
- **REUSE**: use an existing proven capability without automatically adopting its source law or assumptions.
- **INHERIT**: explicitly adopt an existing requirement or contract.
- **REFERENCE**: use knowledge, evidence or prior decisions without adopting their normative authority.

**POLICY-RELATION-001 — SHOULD.** When assumptions could leak across project boundaries, FSL SHOULD distinguish REUSE, INHERIT and REFERENCE explicitly.

## Article IX - AI ambiguity rule
**LAW-AI-001 — MUST NOT.** When normative intent is ambiguous, an agent MUST NOT silently choose the stronger or weaker interpretation.

**LAW-AI-002 — MUST.** The agent MUST surface the ambiguity for review and MUST NOT claim conformance on the unresolved interpretation.

## Article X - Development strategy
FSL does not prescribe one universal implementation path. A project or iteration declares the strategy that best fits its work while remaining explicit and testable.

Canonical strategy vocabulary:
- **E2E** — END -> END: one complete path across the declared touchpoint set.
- **E2M** — END -> MIDPOINT: develop from an outer boundary toward a declared midpoint.
- **M2E** — MIDPOINT -> END: develop from a proven midpoint toward the final boundary.
- **PARALLEL E2E** — two or more independent end-to-end slices progress in parallel.
- **MEET-IN-THE-MIDDLE** — E2M and M2E progress toward a declared midpoint contract and are then integrated.
- **INCREMENTAL E2E** — repeatedly grow a previously proven end-to-end slice.

**LAW-DEV-001 — MUST.** Every material development iteration MUST declare its development strategy.

**LAW-DEV-002 — MUST.** Every material iteration MUST declare a `TOUCHPOINT SET`. Each touchpoint in that set MUST be exercised in some meaningful way sufficient to establish the claimed path.

**LAW-DEV-003 — MUST.** Where a strategy uses boundaries, the iteration MUST identify START, MIDPOINT and/or END as applicable.

**LAW-DEV-004 — MUST.** Every iteration MUST declare expected evidence and an exit condition.

**LAW-DEV-005 — MUST NOT.** An iteration MUST NOT be called E2E when any touchpoint declared in its Touchpoint Set is bypassed.

**LAW-DEV-006 — MUST NOT.** A green component test MUST NOT be represented as end-to-end proof.

**POLICY-DEV-007 — SHOULD.** An iteration SHOULD prefer the smallest vertically complete path over a larger horizontally incomplete implementation.

**POLICY-DEV-008 — SHOULD.** The implementation at an individual touchpoint MAY be intentionally tiny. The purpose is to prove the path early, not to fully implement every layer in the first iteration.

**POLICY-DEV-009 — SHOULD.** After a path is proven, subsequent iterations SHOULD grow from that path by increasing behavior, data, complexity, integration or scope.

**POLICY-DEV-010 — SHOULD.** Parallel strategies MAY be used when their midpoint or integration contracts are explicit and independently verifiable.

**POLICY-DEV-011 — SHOULD.** Iterations SHOULD begin from the latest PROVEN baseline and SHOULD preserve previously proven behavior unless the current requirement explicitly changes it.

**LAW-DEV-012 — MUST.** Touchpoints MUST NOT be treated as branches. Branches identify responsibility ownership; touchpoints identify system surfaces crossed by an iteration.

Short development axiom: **TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN.**

## Article XI - Implementation references
FSL MAY identify implementation material that a project is expected or permitted to use without turning the letterhead into a dependency catalog.

Canonical reference classes:
- **TECHNOLOGY** — runtime, language, platform, protocol or implementation technology.
- **LIBRARY** — package, SDK, framework or implementation dependency.
- **REFERENCE** — repository, implementation, standard, document, UI, prior work or evidence source to study/use.
- **LINK** — canonical location for the referenced material.

Each material entry SHOULD state `CLASS / ITEM / FORCE / RELATION / PURPOSE / SOURCE`.

**LAW-REF-001 — MUST.** If an implementation reference is binding, its normative force MUST be explicit; category alone MUST NOT imply obligation.

**POLICY-REF-002 — SHOULD.** Each material implementation reference SHOULD declare a relation of REUSE, INHERIT or REFERENCE where relevant.

**POLICY-REF-003 — SHOULD.** Canonical links SHOULD identify the authoritative or intended source rather than an arbitrary mirror.

**LAW-REF-004 — MUST NOT.** Referencing or reusing an implementation MUST NOT silently import unrelated assumptions, policies or law from the referenced source.

**POLICY-REF-005 — SHOULD.** Proven existing technologies, libraries, repositories, tools and reference implementations SHOULD be evaluated before creating equivalent core capability from scratch.

**LAW-REF-006 — MUST NOT.** FSL MUST NOT become a full dependency inventory. Detailed versions, transitive dependencies and implementation notes SHOULD live in supporting artifacts when they exceed the compact letterhead boundary.

## Article XII - Amendments and page boundary
Binding constitutional changes MUST be made in SPEC and versioned. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibility.

**LAW-PAGE-001 — MUST NOT.** FSL MUST NOT exceed three pages. Details that outgrow the letterhead SHOULD move to supporting artifacts referenced by clause ID, iteration record or proof record.

## Release axiom
**One version, four squares, all green.**
