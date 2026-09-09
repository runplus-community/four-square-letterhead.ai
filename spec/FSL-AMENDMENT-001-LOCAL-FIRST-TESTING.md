# FSL Amendment 001 — Local-first testing; minimal external CI

**Clause:** FSL-TEST-001  
**Adopted:** 2026-09-09, by explicit owner instruction  
**Status:** Adopted development policy for subsequent testing decisions; carry into the next reviewed FSL baseline  
**Baseline:** FSL v1.8 English method, `skills/FSL-v1.8-SKILL.md` at skill commit `b28a616ae7292913c9f7e3c10095e73c74b9019b`, adopted by `spec/FSL-v1.8-ADOPTION.md` at SPEC commit `e3e76b2bac4b228d9e8a41b31c96342376181e97`  
**Affected sections:** Route, iteration, run and evidence; Show the full path on each run; Make claims no stronger than their evidence

## Adopted clause

Development and verification <u>**MUST**</u> use available local or internal execution first whenever it can safely produce the required evidence. GitHub Actions or another external CI service **MAY** be used only when a required validation cannot be adequately and safely completed using the available internal capabilities. Each such run <u>**MUST**</u> identify the missing capability, why external execution is necessary, and the smallest sufficient scope.

**Test internally first. Use external CI only when necessary. Keep the proof complete.**

## Applying the clause

**Choose by capability, not habit.** Perform code checks, unit tests, fixture tests, document checks, package checks and supported integration scenarios internally. A real mount, multi-user test, reboot or separate-host test does not automatically require GitHub Actions: use a suitable internal environment when available. Do not bypass safety checks, impersonate a CI environment or run destructive tests on a personal or production system merely to avoid external execution.

**Keep external runs exceptional and bounded.** Run only the checks needed by the current change or outstanding proof, together with their necessary prerequisites. Routine pushes, documentation edits and bookkeeping are not by themselves reasons to rerun all workflows. Automatic triggers <u>**SHOULD NOT**</u> launch broad or unrelated suites on every development commit. Record the reason and scope in existing run notes; no new approval database or planning document is required.

**Reuse evidence without inventing a new pass.** Prior evidence **MAY** support a review after checking that its code, dependencies, environment assumptions and claim remain applicable. Reference its original run and revision. For a new end-to-end run, retain the declared touchpoints and report the actual results; do not prefill PASS from an earlier run or silently remove a required touchpoint to reduce execution.

**Preserve evidence quality.** Internal results <u>**MUST**</u> record the relevant revision, environment, scope and observed outcome. Simulated clocks, mocked permissions and ordinary-file fixtures are not proof of an actual reboot, native access enforcement or mounted filesystem. Unavailable required proof remains **NOT YET PROVEN**. Minimizing external CI <u>**MUST NOT**</u> weaken safety, acceptance criteria or release gates.

## Adoption and carry-forward boundary

This amendment adds verification-routing policy; it does not replace the English method, revise historical results or alter the released v1.8 artifacts. Consuming projects adopt the identified clause explicitly in their own SPEC; adoption alone does not migrate their FSL version.

Incorporate the clause into the next reviewed method revision while preserving this adoption record. Runtime changes, workflow-trigger changes, new tests, iteration acceptance and release publication remain separate actions. This document does not claim that existing workflows have already been reconfigured.
