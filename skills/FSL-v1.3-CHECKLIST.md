# FSL v1.3 Recommended Development Checklist

This checklist is RECOMMENDED. It becomes binding only when a LAW or CONTRACT explicitly requires an item.

## Constitution / clause identity
- [ ] Material binding clauses use stable `FORM-SCOPE-NNN` IDs.
- [ ] Published clause IDs are not reused for unrelated meanings.
- [ ] MUST / MUST NOT / SHOULD / SHOULD NOT / MAY force remains explicit.

## Version / Four-Square
- [ ] `Four-Square Template v1.3` and project version are separately visible.
- [ ] SPEC and MEMORY remain fixed lanes.
- [ ] Middle-lane names remain stable or have an explicit migration.
- [ ] Accepted snapshot records branch + commit for all four lanes.

## Iteration / touchpoints
- [ ] One short ordered CSV is the development spine.
- [ ] Only a few kickoff iterations are seeded initially.
- [ ] Later rows are added from learning as earlier rows become PROVEN.
- [ ] Every row contains one small useful requirement and an end-to-end path to proof.
- [ ] No iteration is complete at `implemented` alone.
- [ ] Relevant touchpoints are inspected as `CHANGE`, `VERIFY`, or `NOT AFFECTED`; the CSV itself may stay concise.
- [ ] Touchpoints are system surfaces, not branches.
- [ ] The iteration starts from the latest PROVEN baseline when applicable.
- [ ] Previously proven behavior is preserved unless explicitly changed.
- [ ] All four branches are inspected for impact before acceptance.
- [ ] Status is `PLANNED`, `ACTIVE`, `PROVEN`, or `BLOCKED`.

## Evidence / proof
- [ ] Material claims use CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT.
- [ ] Claims do not exceed proven scope/environment.
- [ ] Missing evidence is NOT YET PROVEN.

## Reuse / authority
- [ ] REUSE does not silently import source-project law.
- [ ] INHERIT is explicit; REFERENCE does not adopt authority.
- [ ] MEMORY may remember law; MEMORY cannot make law.
- [ ] Agents do not invent missing law or silently resolve normative ambiguity.

## Document / release
- [ ] Page count is 1, 2 or 3 only.
- [ ] DOCX/PDF render without clipping or broken tables.
- [ ] Normative keywords are CAPITALIZED, bold and underlined.
- [ ] ZIP and per-file checksums are generated.
- [ ] One version, four squares, all green.
