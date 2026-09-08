# FSL v1.3 Traceability Guide

This is a supporting artifact, not a new constitutional category. It operationalizes the v1.3 clause-ID, proof, iteration and release-snapshot laws.

## Clause IDs
Recommended grammar: `FORM-SCOPE-NNN`.

Examples:
- `LAW-SPEC-001`
- `GUARD-WORKSTUDIO-003`
- `CONTRACT-AI-002`
- `LAW-DEV-001`

A clause ID identifies a clause; it does not replace its normative keyword. Published IDs must remain stable and must not be reused for unrelated meanings.

## Proof record
```text
CLAUSE
ITERATION
CLAIM
SCOPE
ENVIRONMENT
EVIDENCE
RESULT
```

Example:
```text
Clause: LAW-SPEC-001
Iteration: I04
Claim: shared RO works
Scope: WorkStudio M1 / Ubuntu
Environment: Ubuntu 26.xx / kernel ...
Evidence: acceptance-017
Result: CONFORMANT
```

The result must not be generalized beyond the stated scope and environment.

## Iteration traceability
The ordered iteration CSV is the development spine, not the evidence store. Its `Proof` field SHOULD point to or summarize observable proof. Detailed logs, receipts, screenshots, hashes or native results remain supporting evidence.

A row SHOULD connect:

```text
Requirement -> clause(s) -> touchpoints -> E2E path -> proof -> result
```

This lets a reviewer move from a small requirement to the law that governs it and the evidence that proved it.

## Release snapshot
The snapshot records which four commits constituted the reviewed release. It is declarative. Git remains the authority. See `FSL-v1.3-SNAPSHOT.example.yaml`.
