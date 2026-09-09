# Four-Square Letterhead (FSL) v1.6 Constitution

## Preamble
FSL is a compact, file-backed project constitution and letterhead for humans and AI. FSL MUST remain small enough to scan quickly; detailed implementation evidence SHOULD live in referenced supporting artifacts rather than expanding the letterhead beyond three pages.

FSL v1.6 retains the compact v1.5 method, ownership boundary, initial development sequence and essential-reference model. It adds a small release lifecycle so a released SPEC stays immutable while later clarification, correction and normative change remain explicit.

Footer axiom, on every generated page: **FSL owns the method. The project owns the work.**

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

`main1` is the first commit / immutable root reference of the governed project's own repository. `main` is accepted integration. Initial lane branches start from that project's `main1`; each later lane version continues its corresponding prior lane. Lane suffix vN tracks the project release view, not the FSL template version. A branch name alone does not identify a repository or a reviewed commit.

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
Use one short initial sequence, not a required record for every iteration:

> I-001: tiny [input] -> [required touchpoints] -> [observable output] -> prove -> grow.

**POLICY-DEV-013 — SHOULD.** Development SHOULD begin with the smallest meaningful end-to-end iteration across the required touchpoints. Later work MAY grow, run in parallel, proceed toward a midpoint, or proceed from a midpoint as appropriate. The initial sequence is sufficient on the letterhead; no full future-iteration plan, YAML schema or iteration ledger is required by FSL.

E2E crosses the selected complete path. E2M crosses an endpoint-to-midpoint segment. M2E crosses a midpoint-to-endpoint segment. Parallel E2E permits independent complete paths. Meet-in-the-middle joins separately developed segments at a shared contract. Incremental E2E grows a proven path. These names guide work; they are not additional mandatory fields.

**LAW-DEV-005 — MUST NOT.** An iteration MUST NOT be called E2E when any touchpoint declared in its Touchpoint Set is bypassed.

**LAW-DEV-006 — MUST NOT.** A green component test MUST NOT be represented as end-to-end proof.

Coverage clarification for these existing laws: naming a touchpoint is not proof that it was exercised. E2M, M2E and fixture/stub-based checks establish only their declared scope; they do not prove a real integration they replace. An unmodified touchpoint can be verified without changing its implementation.

**POLICY-DEV-007 — SHOULD.** An iteration SHOULD prefer the smallest vertically complete path over a larger horizontally incomplete implementation.

**POLICY-DEV-008 — MAY.** Implementation at a touchpoint MAY be intentionally tiny. Prove the path early; do not attempt to finish every layer in the initial iteration.

**POLICY-DEV-009 — SHOULD.** After a path is proven, subsequent iterations SHOULD grow from that path by increasing behavior, data, complexity, integration or scope.

**POLICY-DEV-010 — MAY.** Parallel strategies MAY be used when their midpoint or integration contracts are explicit and independently verifiable. A midpoint is a named contract or observable interface, not just the word "middle".

**POLICY-DEV-011 — SHOULD.** Iterations SHOULD begin from the latest PROVEN baseline and SHOULD preserve previously proven behavior unless the current requirement explicitly changes it.

**LAW-DEV-012 — MUST NOT.** Touchpoints MUST NOT be treated as branches. Branches identify responsibility ownership; touchpoints identify system surfaces crossed by an iteration.

LAW-DEV-001 through LAW-DEV-004 are retired in v1.5. Their per-iteration declaration obligations are not carried forward. Their IDs remain reserved; they have not been reassigned to the simpler guidance above.

Development axiom: **TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN.**

## Article XI - Implementation references
FSL MAY identify implementation material that a project is expected or permitted to use without turning the letterhead into a dependency catalog.

Canonical reference classes:
- **TECHNOLOGY** — runtime, language, platform, protocol or implementation technology.
- **LIBRARY** — package, SDK, framework or implementation dependency.
- **REFERENCE** — repository, implementation, standard, document, UI, prior work or evidence source to study/use.
- **LINK** — canonical location for the referenced material.

Use a short line or compact table: `ITEM | INTENT / USE | CANONICAL SOURCE`.
A class label is optional when the item is clear. Put MUST, SHOULD or MAY in the intent only when it expresses the project's adopted choice. Use REUSE, INHERIT or REFERENCE where their distinction matters. A mandatory choice is a binding project requirement and therefore has a stable SPEC clause ID under LAW-TRACE-001. Add a version/date/commit only when the exact source affects meaning; no new reference-authority taxonomy or dependency inventory is required.

**LAW-REF-001 — MUST.** If an implementation reference is binding, its normative force MUST be explicit; category alone MUST NOT imply obligation.

**POLICY-REF-002 — SHOULD.** Each material implementation reference SHOULD declare a relation of REUSE, INHERIT or REFERENCE where relevant.

**POLICY-REF-003 — SHOULD.** Canonical links SHOULD identify the authoritative or intended source rather than an arbitrary mirror.

**LAW-REF-004 — MUST NOT.** Referencing or reusing an implementation MUST NOT silently import unrelated assumptions, policies or law from the referenced source.

**POLICY-REF-005 — SHOULD.** Proven existing technologies, libraries, repositories, tools and reference implementations SHOULD be evaluated before creating equivalent core capability from scratch.

**LAW-REF-006 — MUST NOT.** FSL MUST NOT become a full dependency inventory. Detailed versions, transitive dependencies and implementation notes SHOULD live in supporting artifacts when they exceed the compact letterhead boundary.

## Article XII - Release lifecycle
Lifecycle: `Draft -> Prove -> Release -> Appendix / Errata / Amendment -> Next Release`.

**LAW-LIFE-001 — MUST.** Once SPEC is part of an accepted release, that released SPEC MUST remain immutable. Post-release material MUST remain separate from the frozen release artifact.

**POLICY-LIFE-002 — MAY.** An APPENDIX MAY add explanation, examples, references, diagrams, evidence or implementation notes. An APPENDIX MUST NOT change normative intent; if it changes normative intent, use an AMENDMENT.

**LAW-LIFE-003 — MUST NOT.** ERRATA MUST NOT change normative intent. ERRATA may correct clerical, factual, reference, formatting or transcription errors. A correction that changes intent MUST be an AMENDMENT.

**LAW-LIFE-004 — MUST.** A post-release change to normative intent MUST be expressed as an AMENDMENT. The AMENDMENT MUST identify the affected released SPEC/version and clause(s), and MUST state the exact change while remaining separate from the frozen release until incorporated into a later release.

**POLICY-LIFE-005 — SHOULD.** The next release SHOULD incorporate adopted ERRATA and AMENDMENT changes so it becomes the new clean baseline. APPENDIX material MAY remain separate supporting material where useful.

Recommended identity: `APPENDIX-A`, `ERRATA-001`, `AMENDMENT-001`. No YAML, patch registry or separate lifecycle database is required.

Lifecycle axiom: **Release is immutable. Clarify with appendix, correct with errata, change with amendment.**

## Article XIII - Amendments and page boundary
Binding constitutional changes MUST be made in SPEC and versioned. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibility.

**LAW-PAGE-001 — MUST NOT.** FSL MUST NOT exceed three pages. Details that outgrow the letterhead SHOULD move to supporting artifacts referenced by clause ID or proof record. The 1–3 page limit applies to the generated letterhead, not to its supporting Markdown method, source code or evidence files.

## Conformance and release
The retained states are CONFORMANT, CONFORMANT WITH EXCEPTION, NON-CONFORMANT and NOT YET PROVEN. Record an explicit exception with its clause ID, scope, authorized owner, rationale, evidence and review/expiry condition as applicable; a mere note does not authorize departure from a binding rule. An exception does not silently amend the original law.

The per-release check remains small: SPEC stable; primary deliverable verified; second project lane usable and aligned; MEMORY understandable. Evidence covers the declared release view. Package generation alone is not project acceptance or GitHub publication.

## Release axiom
**One version, four squares, all green.**
