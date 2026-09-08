from pathlib import Path

# FSL v1.4 derives from the verified v1.3 generator and changes only the
# development-strategy/reference content while preserving the compact layout.
base = Path(__file__).resolve().parents[1] / 'v1.3' / 'build_templates.py'
src = base.read_text().replace('v1.3', 'v1.4')

replacements = {
    "'Material work SHOULD use a checklist or equivalent visible plan.'":
        "'Every material iteration MUST declare STRATEGY and TOUCHPOINT SET.'",
    "'Each material binding clause MUST have a stable clause ID and SHOULD map to a verification item and observable evidence.'":
        "'Every declared touchpoint MUST be exercised meaningfully for the claimed path; implementation at a touchpoint MAY be intentionally tiny.'",
    "'Agents MAY perform Discover → Plan → Execute → Observe → Verify → Record with defined responsibilities.'":
        "'Strategy MAY be E2E, E2M, M2E, PARALLEL E2E, MEET-IN-THE-MIDDLE or INCREMENTAL E2E; START / MIDPOINT / END MUST be named where applicable.'",
    "'LAW-AI-001 — When normative intent is ambiguous, agents MUST NOT silently choose a stronger or weaker interpretation; they MUST surface the ambiguity for review.'":
        "'A component test MUST NOT be represented as E2E proof, and an E2E claim MUST NOT bypass any touchpoint declared in its Touchpoint Set.'",
    "'Existing assets SHOULD be classified explicitly as REUSE, INHERIT or REFERENCE when project-boundary assumptions could otherwise leak.'":
        "'Important implementation material SHOULD be recorded as TECHNOLOGY / LIBRARY / REFERENCE / LINK with FORCE, RELATION, PURPOSE and SOURCE; large dependency inventories stay outside FSL.'",
    "'The exact SPEC / lane A / lane B / MEMORY commit IDs MUST identify the reviewed release snapshot.'":
        "'The exact SPEC / lane A / lane B / MEMORY commit IDs MUST identify the reviewed release snapshot. Development strategy and Touchpoint Set SHOULD identify how the release was grown.'",
    "'Every active EXCEPTION MUST be attached to scoped release evidence using CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT.'":
        "'Every active EXCEPTION MUST be attached to scoped release evidence using CLAIM / SCOPE / ENVIRONMENT / EVIDENCE / RESULT. Iteration evidence MUST also state the exit condition.'",
}

for old, new in replacements.items():
    if old not in src:
        raise RuntimeError(f'v1.3 generator changed; missing expected text: {old[:90]}')
    src = src.replace(old, new)

# Add the v1.4 development axiom to the release-law wording without adding pages.
old = "One version, four squares, all green."
new = "One version, four squares, all green. TOUCH EVERYTHING REQUIRED; COMPLETE LITTLE; GROW WHAT IS PROVEN."
src = src.replace(old, new)

namespace = {'__file__': str(Path(__file__).resolve()), '__name__': '__main__'}
exec(compile(src, str(base), 'exec'), namespace)
