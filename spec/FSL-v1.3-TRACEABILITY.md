# FSL v1.3 Traceability Guide

This is a supporting artifact, not a new constitutional category. It operationalizes the v1.3 clause-ID, proof and release-snapshot laws.

## Clause IDs
Recommended grammar: `FORM-SCOPE-NNN`.

Examples:
- `LAW-SPEC-001`
- `GUARD-WORKSTUDIO-003`
- `CONTRACT-AI-002`

A clause ID identifies a clause; it does not replace its normative keyword. Published IDs must remain stable and must not be reused for unrelated meanings.

## Proof record
```text
CLAIM
SCOPE
ENVIRONMENT
EVIDENCE
RESULT
```

Example:
```text
Clause: LAW-SPEC-001
Claim: shared RO works
Scope: WorkStudio M1 / Ubuntu
Environment: Ubuntu 26.xx / kernel ...
Evidence: acceptance-017
Result: CONFORMANT
```

The result must not be generalized beyond the stated scope and environment.

## Release snapshot
The snapshot records which four commits constituted the reviewed release. It is declarative. Git remains the authority. See `FSL-v1.3-SNAPSHOT.example.yaml`.
