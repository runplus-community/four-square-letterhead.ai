# FSL Memory - v1.3

**FSL = Four-Square Letterhead. Canonical development version: v1.3.**

## File-backed recall
When FSL is recalled, retrieve/use the actual v1.3 files first, not theory alone. Canonical set includes 1P/2P/3P DOCX+PDF templates, Django v1.3 sample, Constitution, Skill, Checklist, Development Strategy, Iterations CSV, Traceability Guide, Snapshot example, Manifest, README and checksums.

## Fixed model
SPEC and MEMORY are fixed. Two middle lanes are project-defined and version-stable unless a reviewed migration changes them. `main1` is immutable first-commit root; `main` is accepted integration.

## v1.3 traceability
Material binding clauses have stable IDs using `FORM-SCOPE-NNN`, such as `LAW-SPEC-001`, `GUARD-WORKSTUDIO-003`, `CONTRACT-AI-002`. A published ID is not reused for a different meaning.

Proof tuple: CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT. Claims do not extend beyond proven scope/environment.

Accepted Four-Square releases record the exact four reviewed commits in a lightweight YAML snapshot. The snapshot never replaces Git.

## Version identity
`Four-Square Template v1.3` identifies the FSL governance language. Project/contract/sample version identifies the governed system. They are separate and MUST NOT be conflated.

## Iteration development
FSL develops through **small ordered end-to-end iterations**.

Every iteration closes one useful requirement from rule to implementation to usable state to checker to evidence. `Implemented` alone is not complete.

Canonical short axiom:

**ITERATE -> TOUCH -> PROVE -> LEARN -> INCREMENT**

Use one short sequence CSV:

`Seq,Iteration,Requirement,Touchpoints,E2E Path,Proof,Status`

Statuses: `PLANNED | ACTIVE | PROVEN | BLOCKED`.

Each next iteration grows from the latest PROVEN baseline and should preserve previously proven behavior unless explicitly changed.

## Touchpoints
Touchpoints are system surfaces, not branches. Typical vocabulary:

`SPEC | Template | Foundation | Materialization | Runtime | Manager | Access | Checker | AI | Memory | Evidence | Package`

Relevant touchpoints are classified `CHANGE | VERIFY | NOT AFFECTED`.

**Branches say who owns responsibility. Touchpoints say where an iteration crosses the system.**

## Reuse semantics
REUSE = use proven capability without automatically importing source law. INHERIT = explicitly adopt a requirement/contract. REFERENCE = use knowledge/evidence without adopting its authority.

## Authority axioms
**MEMORY may remember law; MEMORY cannot make law.**

Agents MUST NOT invent missing law or silently choose the stronger/weaker interpretation when normative intent is ambiguous. Surface ambiguity for review.

## Page depth
1 page simple, 2 pages medium, 3 pages maximum. Supporting artifacts hold detail that would otherwise bloat FSL.
