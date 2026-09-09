# FSL v1.6 — Release Lifecycle

**Draft -> Prove -> Release -> Appendix / Errata / Amendment -> Next Release**

A released SPEC is a frozen baseline. Post-release work is separate and small:

- **APPENDIX** — supporting clarification, examples, references, diagrams, evidence or implementation notes. It does not change normative intent.
- **ERRATA** — correction of an error without changing normative intent.
- **AMENDMENT** — an explicit post-release change to normative intent; it identifies the released SPEC/version, affected clause IDs and the exact change.

Recommended identity: `APPENDIX-A`, `ERRATA-001`, `AMENDMENT-001`.

Adopted errata and amendments should be incorporated into the next release, which becomes the next clean baseline. Appendices may remain separate when they are still useful. No YAML, patch registry or lifecycle ledger is required.

**Release is immutable. Clarify with appendix, correct with errata, change with amendment.**
