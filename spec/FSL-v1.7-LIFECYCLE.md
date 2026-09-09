# FSL v1.7 - Connected specification lifecycle

**Draft -> Prove -> Release -> Maintain as needed -> Next release**

For an existing system, first study and select a reviewed current-state adoption baseline. Do not invent old iterations. A lifecycle state is not a substitute for evidence: adopted intent, implementation, verification and publication are separate claims.

## Before first release

Reviewed intent can be edited directly in draft SPEC. Optional APPENDIX material may grow during discovery and development: diagrams, current-state study, examples, research and reverse-engineering notes. An appendix does not automatically adopt a new requirement.

## After release

| Document | Purpose | Boundary |
|---|---|---|
| APPENDIX-A | Explain and support | No change to normative intent |
| ERRATA-001 | Correct the released record | No change to normative intent |
| AMENDMENT-001 | Explicitly change normative intent | Names baseline, clauses, exact delta and adoption |

These are optional tools, not mandatory stages or empty files. A released SPEC and its associated reviewed artifacts remain addressable at their immutable references. New material is separate. A correction that changes the promise is an amendment, even if it is described as a bug fix.

## Proposed is not adopted

A committed amendment proposal has no automatic authority. A short Markdown note is sufficient:

`AMENDMENT-001 / Base SPEC: [version + ref] / Clauses: [...] / Status: PROPOSED`

Then state the exact change, rationale and affected verification or migration. Upon adoption, identify the authorized decision, effective scope/date and exact adopted record reference. Preserve that decision; later decisions supersede it explicitly rather than silently rewriting the past.

For a conformance review, identify the base SPEC plus the particular adopted changes that apply. Do not read all amendment files as effective law. Resolve overlapping changes explicitly. Keep the same clause ID only when revising the same obligation with a preserved version/delta; use a new ID for an unrelated obligation.

## Reassess evidence and integrate

Adopting a new promise does not make an old executable conformant. Review affected SYSTEM and AI artifacts, rerun affected routes as needed, and keep evidence scoped to its original baseline and environment. Missing evidence remains NOT YET PROVEN; known violations remain NON-CONFORMANT. A scoped exception is not an amendment or a test PASS.

The next planned release should incorporate applicable adopted errata/amendments, list what it incorporates and become the next clean baseline. Appendix material can remain separate when useful. No YAML, amendment database, patch registry or lifecycle ledger is required.

**Release is immutable. Clarify with appendix, correct with errata, change with amendment.**

Authority: Constitution Article XII, LAW-TRACE-002 clarification and scoped-proof clauses.
