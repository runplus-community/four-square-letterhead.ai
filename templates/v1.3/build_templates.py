from pathlib import Path

# FSL v1.3 deliberately derives from the canonical v1.2 generator rather than
# patching previously rendered DOCX structure. This keeps the 1-3 page layout
# reproducible while advancing only the agreed traceability semantics.
base = Path(__file__).resolve().parents[1] / 'v1.2' / 'build_templates.py'
src = base.read_text()

# Framework version advances; governed project/sample identity remains separate.
src = src.replace('v1.2', 'v1.3')

replacements = {
    "('L1','LAW','MUST','Binding requirements MUST be explicit and observable.')":
        "('LAW-TRACE-001','LAW','MUST','Material binding clauses MUST carry stable FORM-SCOPE-NNN identifiers and SHOULD map to observable evidence.')",
    "('L2','GUARDRAIL','MUST NOT','A binding requirement MUST NOT be silently weakened, bypassed or guessed away.')":
        "('LAW-VERSION-001','LAW','MUST NOT','FSL template version and governed project version MUST NOT be conflated.')",
    "('L3','POLICY','SHOULD','Material SHOULD deviations SHOULD have a recorded reason.')":
        "('LAW-PROOF-001','LAW','MUST NOT','A conformance claim MUST NOT be generalized beyond the scope and environment actually proven.')",
    "('L4','CONTRACT','MUST','Missing evidence MUST result in NOT YET PROVEN, not assumed success.')":
        "('LAW-SNAPSHOT-001','CONTRACT','MUST','An accepted Four-Square release MUST record the exact reviewed commits for SPEC, lane A, lane B and MEMORY.')",
    "('L5','MEMORY','MUST NOT','MEMORY MUST NOT create new law unless promoted into SPEC.')":
        "('LAW-MEMORY-001','LAW','MUST NOT','MEMORY MUST NOT create or amend law unless promoted into SPEC. MEMORY may remember law; MEMORY cannot make law.')",

    "('D1','LAW','MUST','Declared public behavior MUST have implementation evidence and aligned developer guidance.')":
        "('LAW-DJANGO-001','LAW','MUST','Declared public behavior MUST have scoped implementation evidence and aligned developer guidance.')",
    "('D2','GUARDRAIL','MUST NOT','DOCS MUST NOT knowingly describe behavior unsupported by accepted CODE.')":
        "('GUARD-DJANGO-002','GUARDRAIL','MUST NOT','DOCS MUST NOT knowingly describe behavior unsupported by accepted CODE.')",
    "('D3','POLICY','SHOULD','Compatibility changes SHOULD record affected versions and migration guidance.')":
        "('POLICY-DJANGO-003','POLICY','SHOULD','Compatibility changes SHOULD record affected versions, migration guidance and scoped evidence.')",
    "('D4','CONTRACT','MUST','Release evidence MUST distinguish proven behavior from illustrative material.')":
        "('CONTRACT-DJANGO-004','CONTRACT','MUST','Release evidence MUST distinguish proven behavior from illustrative material and MUST state its scope.')",
    "('D5','MEMORY','MUST NOT','MEMORY MUST NOT create new framework law unless promoted into SPEC.')":
        "('LAW-MEMORY-005','LAW','MUST NOT','MEMORY MUST NOT create new framework law unless promoted into SPEC.')",

    "'Each binding clause SHOULD map to a verification item and observable evidence.'":
        "'Each material binding clause MUST have a stable clause ID and SHOULD map to a verification item and observable evidence.'",
    "'Agents MUST NOT reinterpret or waive constitutional law without explicit authority.'":
        "'LAW-AI-001 — When normative intent is ambiguous, agents MUST NOT silently choose a stronger or weaker interpretation; they MUST surface the ambiguity for review.'",
    "'Proven libraries, binaries, scripts, documents, services, datasets, models, plugins and utilities SHOULD be evaluated before new core work.'":
        "'Existing assets SHOULD be classified explicitly as REUSE, INHERIT or REFERENCE when project-boundary assumptions could otherwise leak.'",

    "norm(p,'A MUST / MUST NOT deviation MUST be visible. An EXCEPTION / WAIVER MUST identify clause, scope, owner, rationale, evidence and review/expiry condition where applicable.',6.0)":
        "norm(p,'A MUST / MUST NOT deviation MUST be visible. An EXCEPTION / WAIVER MUST identify clause ID, scope, owner, rationale, evidence and review/expiry condition where applicable.',6.0)",

    "norm(p,'Draft ≠ Tested ≠ Accepted ≠ Released. Claims MUST be scoped to evidence actually validated. A release MUST NOT hide unresolved binding violations. One version, four squares, all green.',6.2,True)":
        "norm(p,'Draft ≠ Tested ≠ Accepted ≠ Released. Claims MUST be scoped to evidence actually validated. An accepted release MUST record the exact four reviewed lane commits. The snapshot MUST NOT replace Git. One version, four squares, all green.',6.2,True)",

    "['ID','CLAUSE','FORCE','EVIDENCE','RESULT']":
        "['CLAUSE ID','CLAIM / SCOPE','ENVIRONMENT','EVIDENCE','RESULT']",
    "[f'[{ri}]','[REQUIREMENT]','[MUST / SHOULD]','[TEST / REVIEW / HASH]','[STATE]']":
        "[f'[LAW-{ri:03d}]','[CLAIM / ARTIFACT / WORKFLOW]','[HOST / VERSION]','[TEST / LOG / HASH]','[STATE]']",

    "'Four lane versions MUST align to the declared release view.'":
        "'The exact SPEC / lane A / lane B / MEMORY commit IDs MUST identify the reviewed release snapshot.'",
    "'No unresolved MUST / MUST NOT violation MAY be hidden.'":
        "'The release snapshot MUST NOT replace Git; Git commit identity remains authoritative.'",
    "'Every active EXCEPTION MUST be attached to release evidence.'":
        "'Every active EXCEPTION MUST be attached to scoped release evidence using CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT.'",
    "'Every generated page MUST show Four-Square Template v1.3 separately from the project version.'":
        "'Every generated page MUST show Four-Square Template v1.3 separately from the governed project version; the two MUST NOT be conflated.'",
}

for old, new in replacements.items():
    if old not in src:
        raise RuntimeError(f'canonical v1.2 generator changed; missing expected clause: {old[:80]}')
    src = src.replace(old, new)

# Keep the constitutional taxonomy small: no new forms are introduced here.
# REUSE / INHERIT / REFERENCE are relation semantics, not constitutional forms.
namespace = {'__file__': str(Path(__file__).resolve()), '__name__': '__main__'}
exec(compile(src, str(base), 'exec'), namespace)
