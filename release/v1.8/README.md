# FSL v1.8 — Plain-English Method

Read FSL-v1.8-SKILL.md, the single editable English method. SPEC adopts that exact source in FSL-v1.8-ADOPTION.md. Repository paths in the adoption record map to the same basenames in this flat consumer pack. PDF/DOCX method copies derive from the source; the template and Django example are authoring aids, not competing specifications.

Documents: three-page method, one-page project template and one-page illustration, each DOCX/PDF. Extend project letterheads to two or three pages only when needed. No blank continuation forms, touchpoint tables or required iteration schema are introduced.

The original FSL-v1.8-COMPLETION.md is the unchanged 40-item local content review. Its local-status statements describe that earlier step. Current source adoption, reviewed commits and branch publication are identified by the snapshot, release notes and accompanying assembly run record. The release pack has its own checksum and is not byte-identical to the original local candidate; publication metadata and build/evidence files were added, while core method and template/sample body wording were preserved.

To verify, extract FSL-Pack-v1.8.zip into an empty directory, install source/requirements.txt, and run `python -B source/verify.py . --selftest --hashes`. SHA256SUMS.txt covers every other file inside this ZIP, including the manifest and build source. The sibling ZIP checksum covers the archive. The accompanying run record is outside the ZIP so it can identify that exact archive without a self-referential hash.

The optional source directory rebuilds the documents from the approved native Word layout and authoritative English. Its layout JSON is internal build data, not a form FSL users fill. No font files are distributed.

Publication location: runplus-community/four-square-letterhead.ai, branch release/fsl-v1.8, directory release/v1.8. This is a public branch-scoped release, not a GitHub Releases-page entry. The final artifact commit establishes publication. Django runtime: NOT RUN. Consuming-project conformance: NOT YET PROVEN.

**FSL owns the method. The project owns the work.**
