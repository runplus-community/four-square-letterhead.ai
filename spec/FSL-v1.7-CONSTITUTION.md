# Four-Square Letterhead (FSL) v1.7 Constitution

## Preamble
FSL is a compact, file-backed project constitution and letterhead for humans and AI. FSL MUST remain small enough to scan quickly; detailed implementation evidence SHOULD live in referenced supporting artifacts rather than expanding the letterhead beyond three pages.

FSL v1.7 retains v1.6 constitutional language, scoped proof and immutable release baselines. It connects concrete square defaults, prospective adoption of existing systems, and stable E2E routes whose touchpoints are visible on every run. Iterations are optional for existing projects; evidence is required for claims. The letterhead is an entry point, not an iteration tracker or a test database.

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

**POLICY-SQUARE-003 — SHOULD.** Projects SHOULD start with `[ SPEC | SYSTEM | AI | MEMORY ]`. SYSTEM and AI MAY be replaced by better-fitting durable concerns. Existing justified lane names need not be renamed to adopt this default.

**LAW-SPEC-001 — MUST.** SPEC MUST present the project's own FSL letterhead as its first item, followed by its supporting specification details. FSL is not a fifth square. The framework supplies the method; the completed project FSL is the project-local contract entry point.

Default content suggestions, not mandatory inventories:
- **SPEC:** FSL; scope; requirements; contracts; guardrails; acceptance; routes. Optional: appendix, errata and amendments.
- **SYSTEM:** code; runtime; data; API; UI; build/deployment; product documentation and checks.
- **AI:** instructions; agents; skills; prompts; AI-facing tools; AI workflows and evaluations.
- **MEMORY:** decisions; rationale; context; limitations; handover and evidence links.

**LAW-OWN-001 — MUST.** Artifacts MUST have a clear authoritative owner according to purpose, not authorship. Agent-generated product code belongs to SYSTEM; a prompt/skill belongs to AI; adopted requirements belong to SPEC; handover belongs to MEMORY. Shared or generated copies MUST NOT become competing independently edited authorities. Tests follow what they verify. Runtime AI dependencies require integrated product evidence; ordinary automation is not automatically AI.

**LAW-REPO-001 — MUST.** Consuming-project specifications, branches, implementation, AI artifacts, memory, evidence and releases MUST remain in the owning project's repository. The FSL repository MUST remain a framework/template/reference repository and MUST NOT hold consuming-project work. Clearly labeled illustrative reference samples and FSL's own framework artifacts are permitted.

The squares are continuing responsibilities, not sequential phases or mandatory runtime hops. AI MAY be inactive for a declared release scope; say so and do not invent execution evidence. SPEC defines. SYSTEM delivers. AI assists. MEMORY remembers.


**LAW-MEMORY-001 — MUST NOT.** MEMORY MUST NOT create or amend normative requirements unless those requirements are promoted into SPEC. Design axiom: **MEMORY may remember law; MEMORY cannot make law.**

```text
main1
  ↓
[ spec-vN | system-vN | ai-vN | memory-vN ]
```

`main1` is the first commit / immutable root reference of the governed project's own repository; `main` is accepted integration. For a new repository, initial lanes start at `main1`; each later lane version continues its matching predecessor. For an existing repository, new adoption lanes MAY start at the reviewed adoption commit; preserve any existing justified lane lineage and record the actual source. Do not move `main1`, rewrite old commits or fabricate historical lanes. Lane suffix vN follows the project release view, not the template version. Repository + exact commit identify a reviewed view; a branch name alone does not.

## Article IV - Clause identity and traceability
**LAW-TRACE-001 — MUST.** Every material binding clause MUST have a stable clause ID. Recommended grammar: `FORM-SCOPE-NNN`.

**LAW-TRACE-002 — MUST NOT.** A published clause ID MUST NOT be reused for a different meaning.

v1.7 clarification: an authorized amendment or new version MAY revise the same identified obligation, while preserving its original baseline and exact delta. An unrelated obligation needs a new ID. Qualify clause references by the applicable SPEC baseline; published IDs are not recycled for unrelated obligations.

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
For a new project, recommend one short initial sequence linked to its primary route, not a record for every iteration:

> I-001: implement the smallest complete R-01 -> run -> verify -> grow.

**POLICY-DEV-013 — SHOULD.** New-project development SHOULD begin with the smallest meaningful end-to-end iteration across the required route touchpoints. Existing projects MAY adopt a reviewed current-state baseline without any iteration plan or reconstructed iteration history. Future iterations are optional for existing projects. Later work MAY grow, parallelize or meet at a named midpoint. No full future-iteration plan, YAML schema or iteration ledger is required by FSL.

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
Lifecycle: `Draft -> Prove -> Release -> Maintain as needed -> Next release`. Appendix, errata and amendments are alternatives used when needed, not mandatory sequential stages.

**LAW-LIFE-001 — MUST.** Once SPEC is part of an accepted release, that released SPEC MUST remain immutable. Post-release material MUST remain separate from the frozen release artifact.

**POLICY-LIFE-002 — MAY.** An APPENDIX MAY add explanation, examples, references, diagrams, evidence or implementation notes. An APPENDIX MUST NOT change normative intent; if it changes normative intent, use an AMENDMENT.

**LAW-LIFE-003 — MUST NOT.** ERRATA MUST NOT change normative intent. ERRATA may correct clerical, factual, reference, formatting or transcription errors. A correction that changes intent MUST be an AMENDMENT.

**LAW-LIFE-004 — MUST.** A post-release change to normative intent MUST be expressed as an AMENDMENT. The AMENDMENT MUST identify the affected released SPEC/version and clause(s), and MUST state the exact change while remaining separate from the frozen release until incorporated into a later release.

**POLICY-LIFE-005 — SHOULD.** The next release SHOULD incorporate adopted ERRATA and AMENDMENT changes so it becomes the new clean baseline. APPENDIX material MAY remain separate supporting material where useful.

**LAW-LIFE-006 — MUST.** A proposed amendment MUST NOT change the effective contract merely because it is committed. Adoption MUST identify an authorized decision, affected SPEC/version and clauses, exact change, effective scope/date, and the adopted record's immutable reference. A conformance review MUST identify its baseline plus applicable adopted changes and resolve overlapping amendments explicitly. Adoption of intent is not proof of implementation or deployment.

Before the first accepted release, reviewed intent MAY be edited directly in draft SPEC. APPENDIX MAY grow during study or development with reverse-engineering notes, diagrams or examples, but MUST NOT hide a new requirement. ERRATA corrects the record without changing intent; a correction that changes the promise is an AMENDMENT. These are useful optional SPEC documents, not mandatory empty files. Keep the frozen baseline and adopted change records addressable. Later decisions supersede explicitly, not by silently rewriting earlier decisions.

Recommended identity: `APPENDIX-A`, `ERRATA-001`, `AMENDMENT-001`. A short Markdown note is sufficient; no YAML, patch registry or separate lifecycle database is required.

Lifecycle axiom: **Release is immutable. Clarify with appendix, correct with errata, change with amendment.**

## Article XIII - Amendments and page boundary
Binding constitutional changes MUST be made in SPEC and versioned. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibility.

**LAW-PAGE-001 — MUST NOT.** FSL MUST NOT exceed three pages. Details that outgrow the letterhead SHOULD move to supporting artifacts referenced by clause ID or proof record. The 1–3 page limit applies to the generated letterhead, not to its supporting Markdown method, source code or evidence files.

## Article XIV - Existing-system adoption

**LAW-ADOPT-001 — MUST.** An existing project adopting FSL MUST identify a reviewed current-state baseline: owning repository, exact implementation commit or artifact identity, scope and known gaps. Separate OBSERVED / AS-IS behavior from ADOPTED / INTENDED requirements. Observed bugs, stale documentation and historical workarounds MUST NOT become law merely because they exist. Unresolved intent remains explicit; conformance on that interpretation is NOT YET PROVEN.

**LAW-ADOPT-002 — MUST NOT.** FSL MUST NOT require existing projects to reconstruct iterations, rewrite repository history or rebuild working capabilities merely to adopt FSL. Adoption is prospective. Genuine historical study MAY be useful, but historical and future iteration plans are optional for existing projects.

Recommended entry: study / reverse-engineer as needed -> identify current baseline -> review intended contracts and critical routes -> run representative checks -> release a scoped governed baseline. A representative pass proves only its declared scope, not the entire existing system. A baseline can be documented while conformance remains NOT YET PROVEN.

Axiom: **Adopt the present. Do not rewrite the past.**

## Article XV - Routes, runs and visible touchpoints

An ITERATION organizes development. A ROUTE defines a stable intended path. A RUN executes/checks a particular route baseline. EVIDENCE supports the result. They are not interchangeable.

**POLICY-ROUTE-001 — SHOULD.** The project FSL SHOULD display its primary E2E route as one line, for example `R-01: input -> required touchpoints -> observable output`. Add only other critical routes when useful. Show the boundary and expected outcome; detailed test cases remain in project-local supporting files.

**LAW-ROUTE-002 — MUST.** An E2E claim MUST identify the applicable SPEC and route baseline, route ID, ordered required touchpoints, input/end boundary and expected observable outcome. R-01 is a route ID, not an iteration counter or proof. Route identity is scoped to the project and version; route definitions MUST NOT be silently changed to fit a passing subset.

**LAW-RUN-001 — MUST.** Each run claiming route coverage MUST show the declared touchpoint list before execution and retain a result for every declared point, including points not reached. A log or short run sheet is sufficient. Record the run identity, actual implementation revision, applicable SPEC/route baseline, environment, expected/observed outcome and evidence references. The evidence MUST connect the points in the same workflow; unrelated unit checks do not prove the integrated route.

Use simple execution labels such as PASS, FAIL and NOT RUN. These describe execution, not new constitutional conformance states. A run proves the declared route only when every required point is evidenced and the expected outcome is verified. A skipped or unreached point leaves the route unproven; a known violation is NON-CONFORMANT. An exception does not turn an unexecuted point into a passed test. Never prefill successful results or inherit a previous run's success automatically.

Existing LAW-DEV-005 / 006 apply: presence in a list is not coverage; fixtures and stubs prove only their disclosed scope; E2M/M2E remain partial until the integrated outcome is demonstrated. Unchanged components may be verified without editing them. Include AI only when it participates in the claimed runtime route. Parallel routes keep separate results; where they interact, verify their shared state/contracts as well.

A route's required ordering may express a named midpoint, a branch condition or an asynchronous completion check; show those boundaries when material. A real negative route can PASS by demonstrating its expected rejection. Do not require production execution when a safe representative environment provides the claimed evidence; label environment and substitutions honestly.

No route database, run-history ledger or prescribed serialization is required. Display critical routes on the letterhead; repeat their touchpoints in the execution output/checklist. The route catalog is not a moving PASS badge. Every evidence reference retains its original baseline and environment.

Axiom: **Iterations are optional. Routes define coverage. Runs produce evidence.** Evidence is required for claims; a run may succeed, fail or remain incomplete.

## Conformance and release
The retained states are CONFORMANT, CONFORMANT WITH EXCEPTION, NON-CONFORMANT and NOT YET PROVEN. Record an explicit exception with its clause ID, scope, authorized owner, rationale, evidence and review/expiry condition as applicable; a mere note does not authorize departure from a binding rule. An exception does not silently amend the original law.

The per-release check remains small: SPEC stable; primary deliverable verified; second project lane usable and aligned or explicitly inactive in scope; MEMORY understandable. Verify the exact combined release view against its applicable SPEC and critical routes, not just four independently green branch histories. Unchanged squares require review, not ceremonial source edits. Package generation alone is not project acceptance or GitHub publication. A released FSL framework does not certify projects that use its blank templates.

## Release axiom
**One version, four squares, all green.**
