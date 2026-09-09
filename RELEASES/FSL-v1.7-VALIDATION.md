# FSL v1.7 - Framework artifact validation

## Scope

Claim: the declared v1.7 framework source/method set produces and packages the expected four editable letterheads and their PDFs, with concrete squares, visible routes, scoped adoption and lifecycle guidance. This does not prove any consuming project's implementation, legal compliance, production safety or Django runtime behavior.

## Completed before integration

All four lane workflows completed successfully:
- SPEC: https://github.com/runplus-community/four-square-letterhead.ai/actions/runs/34289318150
- TEMPLATES: https://github.com/runplus-community/four-square-letterhead.ai/actions/runs/34289548024
- SKILL: https://github.com/runplus-community/four-square-letterhead.ai/actions/runs/34289905967
- MEMORY: https://github.com/runplus-community/four-square-letterhead.ai/actions/runs/34289718732

The template gate generated all four DOCX files using Python 3.12 / python-docx 1.2.0 on the GitHub Ubuntu runner, rendered them with LibreOffice and checked them with Poppler. Exact page counts passed: 1 / 2 / 3 / 2.

Artifact archive 10080804777 was downloaded from the template workflow. All eight canonical PDF pages were rendered at 150 dpi and visually inspected for clipping, overlap, glyphs, tables, header/footer separation and page identities. No such defect was found. The generated DOCX XML/package entries were identical to the independently rendered and visually inspected local DOCX documents. Canonical PDF export is the release reference; byte-identical rebuilding across unrelated renderer versions is not asserted.

Automated document checks passed: version identity on every page, separate project/sample identity, ownership footer, FSL first in SPEC, concrete default system-vN / ai-vN, optional existing-project iterations, R-01, visible NOT RUN states and normative bold/underline. Normative-run counts were 13 / 14 / 19 / 11 across the four DOCX files. The sample explicitly says NOT EXECUTED and keeps all seven runtime touchpoints NOT RUN.

Four negative document tests passed by rejecting a missing R-01, a wrong first SPEC item, a wrong default system branch label, and removed normative underlining. These exercise verifier behavior; they do not establish that every possible malformed document is detectable.

Method gates checked unique/reserved clause IDs, continued old clause IDs, prospective adoption/route/run/amendment anchors, a four-item release checklist, non-normative memory and unmodified v1.6 lane artifacts. Token/structure checks complement the reviewed text; they are not semantic proof of arbitrary project contracts.

## Release assembly gate

The release workflow verifies the four integrated directory identities against the snapshot, verifies the source/documents again, assembles only the declared payload, hashes the manifest and all its files, writes the ZIP, extracts it into a clean directory and runs the shipped verifier on the extracted bytes. The actual assembly run ID, outcome, exact integration revision and package hash are recorded separately beside the distribution ZIP, so the archive does not claim or hash its own future publication.

The per-file manifest excludes MANIFEST.txt and SHA256SUMS.txt; SHA256SUMS.txt covers all listed files plus MANIFEST.txt. The ZIP has its own external SHA-256. No nested ZIP, YAML, font files or symlinks are intended in the payload. Full-payload verification must be run in the clean extracted directory, not the branch directory that also carries the ZIP and external run report.

## Limits and preserved history

No Django execution, browser test, production test or real upstream adoption was performed. Sample route conformance remains NOT YET PROVEN. No claim is made that unrelated projects satisfy the new Constitution. Existing project iterations are optional, but a concrete conformance claim still requires scoped evidence.

Older released baselines and their lane artifacts are preserved. A public branch publication is not an access-private release or a GitHub Releases-page entry. Git commit identity and the verified ZIP checksum identify the final release; branch protection/immutability enforcement is not asserted.
