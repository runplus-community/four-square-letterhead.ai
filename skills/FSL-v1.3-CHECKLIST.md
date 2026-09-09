# FSL v1.3 Recommended Development Checklist

This checklist is RECOMMENDED. It becomes binding only when a LAW or CONTRACT explicitly requires an item.

## Constitution / clause identity
- [ ] Material binding clauses use stable `FORM-SCOPE-NNN` IDs.
- [ ] Published clause IDs are not reused for unrelated meanings.
- [ ] MUST / MUST NOT / SHOULD / SHOULD NOT / MAY force remains explicit.
- [ ] No new constitutional categories were added when an existing form was sufficient.

## Version identity
- [ ] `Four-Square Template v1.3` appears on every page.
- [ ] Project/contract/sample version is separately visible.
- [ ] Template and project versions are not conflated.

## Four-Square / snapshot
- [ ] SPEC and MEMORY remain fixed lanes.
- [ ] Middle-lane names remain stable or have an explicit migration.
- [ ] Accepted release snapshot records branch + commit for all four lanes.
- [ ] Snapshot is declarative and does not replace Git.

## Iteration / touchpoints
- [ ] One short ordered sequence CSV is the development spine.
- [ ] CSV rows are in explicit `Seq` order.
- [ ] Each row contains one small useful requirement.
- [ ] Every row has an end-to-end path that closes at observable proof.
- [ ] No iteration is marked complete at `implemented` alone.
- [ ] Relevant touchpoints are identified and classified `CHANGE`, `VERIFY`, or `NOT AFFECTED`.
- [ ] Touchpoints are treated as system surfaces, not branches.
- [ ] The iteration starts from the latest PROVEN baseline when applicable.
- [ ] Previously proven behavior is preserved unless explicitly changed.
- [ ] All four branches were inspected for impact before acceptance.
- [ ] Status is one of `PLANNED`, `ACTIVE`, `PROVEN`, `BLOCKED`.

## Evidence / proof
- [ ] Material conformance claims use CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT.
- [ ] Result is one of the four canonical conformance states.
- [ ] Claims do not exceed the proven scope/environment.
- [ ] Missing evidence is NOT YET PROVEN.

## Reuse / inheritance / reference
- [ ] Reused capabilities are not assumed to import source-project law.
- [ ] Inherited requirements/contracts are explicitly identified.
- [ ] Referenced evidence/knowledge is not accidentally treated as adopted law.

## AI / MEMORY authority
- [ ] MEMORY may remember law; MEMORY cannot make law.
- [ ] Agents do not invent missing law.
- [ ] Ambiguous normative intent is surfaced for review rather than silently strengthened or weakened.

## Document / release
- [ ] Page count is 1, 2 or 3 only.
- [ ] DOCX/PDF render without clipping or broken tables.
- [ ] Normative keywords are CAPITALIZED, bold and underlined.
- [ ] ZIP and per-file checksums are generated.
- [ ] One version, four squares, all green.
