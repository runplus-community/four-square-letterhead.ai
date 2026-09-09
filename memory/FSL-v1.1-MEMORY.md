# FSL Memory — v1.1

**FSL = Four-Square Letterhead.**

## Current canonical recall
When the user says **FSL**, **Four-Square Letterhead**, **recall FSL**, **use the FSL template**, or similar, retrieve/use the actual **v1.1 files first**. Do not answer with theory alone when the files are available.

Canonical file-backed set:
- `FSL-v1.1-Template-1P.docx/pdf`
- `FSL-v1.1-Template-2P.docx/pdf`
- `FSL-v1.1-Template-3P.docx/pdf`
- `FSL-v1.1-Sample-Django-2P.docx/pdf`
- `FSL-v1.1-SKILL.md`
- `FSL-v1.1-MANIFEST.yaml`

## Template identity
Every generated page must visibly carry **Four-Square Template v1.1**. Project/sample version is separate and must also be visible, e.g. **Django Sample v1.1**.

## Branch model
`main1` is the repository first commit / immutable root reference.

```text
main1
  ↓
[ spec-v1 | <lane-a>-v1 | <lane-b>-v1 | memory-v1 ]
  ↓
[ spec-v2 | <lane-a>-v2 | <lane-b>-v2 | memory-v2 ]
```

- Fixed lanes: `spec-vN`, `memory-vN`.
- Middle two lanes are project-selected and remain stable across versions.
- Examples: code, tools, docs, utils, plugins, skills, ai.
- Use `ai` as an umbrella when agents/skills/plugins belong together.

## Page depth
Use 1 page for simple projects, 2 for medium complexity, and 3 pages maximum for complex projects.
