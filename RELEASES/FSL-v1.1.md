# Four-Square Letterhead (FSL) v1.1 — Branch Release

**Status:** accepted branch-scoped release snapshot  
**Template:** Four-Square Template v1.1  
**Canonical branch:** `release/fsl-v1.1`  
**Artifact directory:** `release/v1.1/`

This branch is the release mechanism for FSL v1.1 while the current integration does not expose GitHub Release creation/upload. It contains the real DOCX/PDF templates, Django sample, skill, memory, manifest, ZIP package and checksums.

> The repository is public, so this branch is publicly readable. “Branch release” means release-scoped and not merged to `main`; it does not mean access-private.

## Four-Square model

```text
main1
  ↓
[ spec-vN | <lane-a>-vN | <lane-b>-vN | memory-vN ]
```

For FSL v1.1 itself:

```text
spec-v1.1 | templates-v1.1 | skill-v1.1 | memory-v1.1
```

`SPEC` and `MEMORY` are fixed. The two middle lanes are project-selected and remain stable across versions.

## v1.1 contents

- 1-page template — DOCX + PDF
- 2-page template — DOCX + PDF
- 3-page template — DOCX + PDF
- Django illustrative sample — DOCX + PDF
- FSL v1.1 Skill
- FSL v1.1 Memory
- manifest and VERSION
- `SHA256SUMS.txt`
- `FSL-Pack-v1.1.zip`
- `FSL-Pack-v1.1.zip.sha256`

## Validation

The branch build validates:

- DOCX package integrity;
- expected PDF page counts: 1P / 2P / 3P / Django 2P;
- visible `Four-Square Template v1.1` marker on every PDF;
- visible `Django Sample v1.1` marker;
- illustrative Django `code-v1` and `docs-v1` lane markers;
- required SPEC / MEMORY / AI naming guidance in the skill;
- manifest version `1.1`;
- ZIP integrity and SHA-256 checksums.

The authoritative hashes are stored with the artifacts in `release/v1.1/SHA256SUMS.txt` and `release/v1.1/FSL-Pack-v1.1.zip.sha256`; this note intentionally does not duplicate a hash value.
