# FSL v1.6 — Release Notes

FSL v1.6 adds one compact concept to v1.5: the lifecycle of a released specification.

## Lifecycle

`Draft -> Prove -> Release -> Appendix / Errata / Amendment -> Next Release`

- Released SPEC remains immutable.
- APPENDIX adds supporting clarification without changing normative intent.
- ERRATA corrects an error without changing normative intent.
- AMENDMENT expresses a post-release normative change and identifies the affected released version and clause IDs.
- The next release SHOULD absorb adopted errata and amendments and become the new clean baseline.

Recommended identities: `APPENDIX-A`, `ERRATA-001`, `AMENDMENT-001`.

No YAML, patch registry or lifecycle ledger is added.

Retained unchanged: 1–3 page boundary, fixed SPEC/MEMORY lanes, project-defined middle lanes, tiny initial E2E strategy, essential references, exact four-commit release view, scoped proof, ownership footer and AI ambiguity guardrails.

**FSL owns the method. The project owns the work.**

**Release is immutable. Clarify with appendix, correct with errata, change with amendment.**
