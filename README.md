# Four-Square Letterhead (FSL)

**Current integrated version: FSL v1.3**  
**Template identity: Four-Square Template v1.3**

FSL is a compact, file-backed project constitution / contract / technical letterhead for humans and AI. It remains deliberately small: **1–3 pages maximum**.

## Constitutional language
FSL preserves the v1.2 vocabulary: **MUST / MUST NOT**, **SHOULD / SHOULD NOT**, **MAY**, **EXCEPTION / WAIVER**. Binding law MUST NOT be silently weakened, and missing proof is **NOT YET PROVEN**.

## Four-Square model

```text
main1
  ↓
[ spec-vN | <project-lane-a>-vN | <project-lane-b>-vN | memory-vN ]
```

`SPEC` and `MEMORY` are fixed. The two middle lanes are project-defined and SHOULD remain stable across versions. `main1` is the immutable first-commit root; `main` is accepted integration.

For FSL v1.3 itself:

```text
spec-v1.3 | templates-v1.3 | skill-v1.3 | memory-v1.3
```

## v1.3 traceability
- Material binding clauses MUST carry stable IDs such as `LAW-SPEC-001`.
- Proof records use `CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT`.
- Accepted Four-Square releases MUST record the exact four reviewed lane commits; Git remains authority.
- `Four-Square Template v1.3` identifies the governance language; project version identifies the governed system. They MUST NOT be conflated.
- REUSE, INHERIT and REFERENCE distinguish capability reuse from adopted law and evidence-only reference.
- **MEMORY may remember law; MEMORY cannot make law.**
- Agents MUST NOT silently strengthen or weaken ambiguous normative intent.

## Release rule
**One version, four squares, all green.**
