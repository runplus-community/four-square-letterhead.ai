# Four-Square Letterhead (FSL) v1.1

Status: release-ready
Template: Four-Square Template v1.1
Target: main

## What changed
- SPEC and MEMORY are fixed lanes.
- The two middle lanes are project-defined and remain stable across versions.
- Supports 1, 2, or 3 pages depending on project complexity.
- Every generated page visibly carries the Four-Square template version.
- Includes a Django v1.1 illustrative sample.
- Includes a file-backed skill, memory definition, manifest, templates, and checksum.

## Branch model

```text
main1
  ↓
[ spec-vN | <lane-a>-vN | <lane-b>-vN | memory-vN ]
```

For FSL v1.1 itself:

```text
spec-v1.1 | templates-v1.1 | skill-v1.1 | memory-v1.1
```

## Release assets
- FSL-Pack-v1.1.zip
- FSL-Pack-v1.1.zip.sha256

SHA-256:
`4cb6360267028d77c777dcc953e5e246531a8394be6273ad22f3e6a4fbc7ecd3`

## Release rule
One version, four squares, all accepted into `main` before release.
