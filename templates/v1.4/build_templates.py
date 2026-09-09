from pathlib import Path

# FSL v1.4 derives directly from the canonical v1.2 renderer while applying
# both the v1.3 traceability layer and the v1.4 development-strategy layer.
base = Path(__file__).resolve().parents[1] / 'v1.2' / 'build_templates.py'
src = base.read_text().replace('v1.2', 'v1.4')

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

    "'Material work SHOULD use a checklist or equivalent visible plan.'":
        "'Every material iteration MUST declare STRATEGY and TOUCHPOINT SET.'",
    "'Each binding clause SHOULD map to a verification item and observable evidence.'":
        "'Every declared touchpoint MUST be exercised meaningfully for the claimed path; implementation at a touchpoint MAY be intentionally tiny.'",
    "'Agents MAY perform Discover → Plan → Execute → Observe → Verify → Record with defined responsibilities.'":
        "'Strategy MAY be E2E, E2M, M2E, PARALLEL E2E, MEET-IN-THE-MIDDLE or INCREMENTAL E2E; START / MIDPOINT / END MUST be named where applicable.'",
    "'Agents MUST NOT reinterpret or waive constitutional law without explicit authority.'":
        "'A component test MUST NOT be represented as E2E proof, and an E2E claim MUST NOT bypass any touchpoint declared in its Touchpoint Set.'",
    "'Proven libraries, binaries, scripts, documents, services, datasets, models, plugins and utilities SHOULD be evaluated before new core work.'":
        "'Important implementation material SHOULD be recorded as TECHNOLOGY / LIBRARY / REFERENCE / LINK with FORCE, RELATION, PURPOSE and SOURCE; REUSE / INHERIT / REFERENCE SHOULD be explicit where assumptions could leak.'",

    "norm(p,'A MUST / MUST NOT deviation MUST be visible. An EXCEPTION / WAIVER MUST identify clause, scope, owner, rationale, evidence and review/expiry condition where applicable.',6.0)":
        "norm(p,'A MUST / MUST NOT deviation MUST be visible. An EXCEPTION / WAIVER MUST identify clause ID, scope, owner, rationale, evidence and review/expiry condition where applicable.',6.0)",

    "norm(p,'Draft ≠ Tested ≠ Accepted ≠ Released. Claims MUST be scoped to evidence actually validated. A release MUST NOT hide unresolved binding violations. One version, four squares, all green.',6.2,True)":
        "norm(p,'Draft ≠ Tested ≠ Accepted ≠ Released. Claims MUST be scoped to evidence actually validated. An accepted release MUST record the exact four reviewed lane commits. The snapshot MUST NOT replace Git. TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN. One version, four squares, all green.',6.2,True)",

    "['ID','CLAUSE','FORCE','EVIDENCE','RESULT']":
        "['CLAUSE ID','CLAIM / SCOPE','ENVIRONMENT','EVIDENCE','RESULT']",
    "[f'[{ri}]','[REQUIREMENT]','[MUST / SHOULD]','[TEST / REVIEW / HASH]','[STATE]']":
        "[f'[LAW-{ri:03d}]','[CLAIM / ARTIFACT / WORKFLOW]','[HOST / VERSION]','[TEST / LOG / HASH]','[STATE]']",

    "'Four lane versions MUST align to the declared release view.'":
        "'The exact SPEC / lane A / lane B / MEMORY commit IDs MUST identify the reviewed release snapshot. Development strategy and Touchpoint Set SHOULD identify how the release was grown.'",
    "'No unresolved MUST / MUST NOT violation MAY be hidden.'":
        "'The release snapshot MUST NOT replace Git; Git commit identity remains authoritative.'",
    "'Every active EXCEPTION MUST be attached to release evidence.'":
        "'Every active EXCEPTION MUST be attached to scoped release evidence using CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT. Iteration evidence MUST state its exit condition.'",
    "'Every generated page MUST show Four-Square Template v1.4 separately from the project version.'":
        "'Every generated page MUST show Four-Square Template v1.4 separately from the governed project version; the two MUST NOT be conflated.'",
}

for old, new in replacements.items():
    if old not in src:
        raise RuntimeError(f'canonical generator changed; missing expected text: {old[:90]}')
    src = src.replace(old, new)

namespace = {'__file__': str(Path(__file__).resolve()), '__name__': '__main__'}
exec(compile(src, str(base), 'exec'), namespace)
