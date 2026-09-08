# Four-Square Letterhead (FSL) v1.7

**Concrete squares. Prospective adoption. Visible E2E routes.**

FSL is a compact project identity and constitutional letterhead for humans and AI. Start with one page; use two or three only when essential detail needs room. The completed project letterhead is the first item inside SPEC, not a fifth square.

> **FSL owns the method. The project owns the work.**

## Start concrete

`[ SPEC | SYSTEM | AI | MEMORY ]`

| Square | Main responsibility |
|---|---|
| SPEC | FSL first; scope, requirements, contracts, guardrails, acceptance and routes. Optional appendix, errata and amendments. |
| SYSTEM | Product implementation, runtime, data, API/UI, build material and product checks. |
| AI | Instructions, agents, skills, prompts, AI workflows and evaluations where applicable. |
| MEMORY | Decisions, rationale, context, limitations, handover and evidence links. |

SPEC and MEMORY are fixed. SYSTEM and AI are recommended defaults, not forced renames. FSL itself keeps its TEMPLATES / SKILL specialization. Ownership follows purpose, not the author; agent-generated product code is still product code.

## One route, visible on every run

`R-01: input -> required touchpoints -> observable output`

The route declares its expected outcome and SPEC/version boundary. Every run shows every declared point before execution, then retains PASS / FAIL / NOT RUN plus connected evidence and actual revision/environment. A skipped point, stubbed integration or component pass is not proof of the wider route. Never prefill success. R-01 is a route ID, not an iteration or run number.

New project: `I-001: tiny R-01 -> verify -> grow`.

Existing project: `study / reverse-engineer as needed -> reviewed adoption baseline -> verify critical routes`. Historical and future iteration plans are optional. Distinguish observed behavior from adopted promises; do not rewrite history or rebuild a working capability just to adopt FSL.

## Lifecycle

`Draft -> Prove -> Release -> Maintain as needed -> Next release`

Appendix supports understanding; errata corrects without changing intent; an explicitly adopted amendment changes released intent. A committed proposal is not adopted law. The released baseline stays addressable and unchanged. The next release incorporates applicable adopted changes.

No YAML payload, mandatory iteration ledger, route database, lifecycle registry or empty support documents. Detailed evidence stays in the project repository.

## Files and quick start

Use `FSL-v1.7-Template-1P.docx` as the editable starting point and its PDF as the visual reference. The 2P template adds a route/run-sheet and adoption guidance; the 3P template adds release identity and lifecycle detail. The Django 2P sample is illustrative: runtime NOT RUN, not an upstream adoption or test claim.

In the repository, documents and standalone build/check scripts are under `templates/v1.7/`; method files are under `spec/`, `skills/` and `memory/`. In the release ZIP, documents and method files are at the root, with build/check scripts under `source/`. Start with the Constitution, then the ROUTES and ADOPTION guides as needed. The ROUTES guide contains a blank run sheet; it does not prescribe a storage format.

Verify an unpacked release from its root with `python -B source/verify_package.py --root .` after installing Poppler command-line tools. Do not run full-payload verification on the repository artifact directory that also contains the distribution ZIP; unpack the ZIP to a clean directory first. Build instructions are in `source/README.md` inside the pack. No fonts are distributed.

## This framework release

The exact four reviewed commits and lane CI evidence are recorded in `FSL-v1.7-SNAPSHOT.md` in the pack and `RELEASES/FSL-v1.7-SNAPSHOT.md` in Git. The validation report scopes the completed checks. A checksum verifies bytes, not project behavior or authority by itself.

FSL's release-assembly route R-01 is: `reviewed integration -> exact source/document identities -> payload assembly -> ZIP -> clean extraction -> payload verification`. Its expected outcome is a complete, hash-verified v1.7 document/method pack. Document generation is separately evidenced by the linked template build; the assembly run consumes those exact artifacts rather than claiming it regenerated them. Publication is a separate action recorded by the successful branch push and final commit.

The established publication channel is the public branch `release/fsl-v1.7`, not a GitHub Releases-page entry. A branch can move; use the exact final commit and ZIP checksum to identify the published snapshot. Previous release files remain unchanged.

**One version, four squares, all green.**
