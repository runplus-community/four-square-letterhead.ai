# Four-Square Letterhead (FSL) v1.2 Constitution

## Preamble
FSL is a compact, file-backed project constitution and letterhead for humans and AI. It exists to make project identity, obligations, boundaries, evidence, development practice and release status visible without turning every implementation detail into law.

## Article I - Authority and normative language
1. **MUST / MUST NOT** define binding requirements and prohibitions.
2. **SHALL / SHALL NOT** are constitutional aliases for MUST / MUST NOT; MUST / MUST NOT are preferred for machine-readable clarity.
3. **SHOULD / SHOULD NOT** define strong expectations. A deviation SHOULD have a recorded reason.
4. **MAY** defines permission.
5. A binding requirement MUST NOT be silently weakened, bypassed, guessed away, or converted into a recommendation.
6. When evidence is absent, the state MUST be **NOT YET PROVEN**, not assumed conformant.
7. In rendered FSL pages, normative keywords MUST be CAPITALIZED, bold and underlined. This emphasis MUST NOT be used decoratively where it could be mistaken for normative force.

## Article II - Constitutional forms
- **ARTICLE** groups a constitutional subject.
- **LAW** is a binding clause and normally uses MUST / MUST NOT.
- **CONTRACT** is an observable promise, interface or outcome and SHOULD identify evidence or a gate.
- **POLICY** is a standing rule whose force is stated by its normative keyword.
- **GUARDRAIL** is a protective boundary, commonly expressed as MUST NOT / SHALL NOT.
- **RECOMMENDED PRACTICE** is preferred but non-binding guidance, normally using SHOULD / SHOULD NOT / MAY.
- **CHECKLIST** is an execution/review aid. A checklist is not law unless a LAW or CONTRACT requires it.

The form label alone does not determine force; the normative keyword does.

## Article III - Four-Square structure
1. `SPEC` and `MEMORY` are fixed lanes.
2. Two middle lanes are selected per project from its durable concerns.
3. Middle-lane names SHOULD use the narrowest stable vocabulary.
4. Umbrella names MAY be used when multiple related artifacts form one concern, e.g. agents + skills + plugins -> `ai-vN`.
5. Once selected, middle-lane names SHOULD remain stable across versions unless a reviewed migration changes the model.
6. MEMORY MUST NOT create new normative requirements unless those requirements are promoted into SPEC.

```text
main1
  ↓
[ spec-v1 | <lane-a>-v1 | <lane-b>-v1 | memory-v1 ]
  ↓
[ spec-v2 | <lane-a>-v2 | <lane-b>-v2 | memory-v2 ]
```

`main1` is the first commit / immutable root reference. `main` is accepted integration.

## Article IV - Conformance
The canonical states are:
- **CONFORMANT**
- **CONFORMANT WITH EXCEPTION**
- **NON-CONFORMANT**
- **NOT YET PROVEN**

A MUST / MUST NOT violation makes the declared scope NON-CONFORMANT unless a valid explicit EXCEPTION / WAIVER applies. A SHOULD / SHOULD NOT deviation does not automatically require a waiver, but SHOULD record its reason.

## Article V - Exceptions and waivers
A binding EXCEPTION / WAIVER MUST identify the clause, scope, owner, rationale, evidence and review/expiry condition where applicable. Agents MUST NOT create, infer or silently approve an exception unless project authority explicitly permits it.

## Article VI - Development governance
1. Development SHOULD use a checklist-driven approach for material work.
2. Each binding clause SHOULD map to a verification item and observable evidence.
3. Agents MAY perform Discover -> Plan -> Execute -> Observe -> Verify -> Record with defined responsibilities.
4. Agents MUST NOT reinterpret or waive constitutional law without explicit authority.
5. Proven libraries, binaries, scripts, documents, services, datasets, models, plugins, utilities and framework primitives SHOULD be reused before new core work when they satisfy the contract.
6. New core work SHOULD identify the capability gap it closes.

## Article VII - Evidence and release
1. Draft != Tested != Accepted != Released.
2. Claims MUST be scoped to the artifact, platform, workflow and evidence actually validated.
3. A release MUST NOT claim conformance while an unresolved binding violation is hidden.
4. Active exceptions MUST be visible in release evidence.
5. One version, four squares, all green remains the release rule.

## Article VIII - Amendments
Binding constitutional changes MUST be made in SPEC and versioned. MEMORY MUST NOT amend the constitution. A project-selected middle-lane rename MUST be handled as a reviewed migration rather than an incidental rename.
