#!/usr/bin/env python3
from pathlib import Path

# FSL v1.6 deliberately derives from the verified standalone v1.5 generator.
# It changes only lifecycle/version wording while preserving the compact layout.
base = Path(__file__).resolve().parents[1] / 'v1.5' / 'build_templates.py'
src = base.read_text()
src = src.replace('VERSION = "1.5"', 'VERSION = "1.6"')
src = src.replace('v1.5', 'v1.6')

old = '    label(d,"RELEASE CHECK  /  ONE VERSION, FOUR SQUARES, ALL GREEN",before=7)\n'
new = '''    label(d,"LIFECYCLE  /  RELEASE CHECK",before=7)\n    paragraph(d,"Draft → Prove → Release → Appendix / Errata / Amendment → Next Release.",size=7.8,bold=True,after=2)\n'''
if old not in src:
    raise RuntimeError('v1.5 generator changed: release-check anchor missing')
src = src.replace(old, new, 1)

old = '''    label(d,"AMENDMENT & HANDOVER")\n    paragraph(d,"Change: [clause IDs / project version]. Compatibility or migration impact: [brief impact or NONE]. Supporting decisions and evidence: [MEMORY paths].",size=9,after=5)\n    paragraph(d,"Change binding intent in SPEC; align both project lanes and MEMORY. Preserve published clause IDs and the frozen release view. MEMORY may remember law; MEMORY cannot make law.",size=9,after=3)\n'''
new = '''    label(d,"POST-RELEASE LIFECYCLE")\n    paragraph(d,"Released SPEC stays immutable. APPENDIX clarifies/supports without changing intent; ERRATA corrects without changing intent; AMENDMENT changes intent and identifies the released version plus affected clauses.",size=8.7,after=5)\n    paragraph(d,"Identity: APPENDIX-A / ERRATA-001 / AMENDMENT-001. The next release SHOULD absorb adopted errata/amendments. Release is immutable. Clarify with appendix, correct with errata, change with amendment.",size=8.5,color=MUTED,after=3)\n'''
if old not in src:
    raise RuntimeError('v1.5 generator changed: amendment anchor missing')
src = src.replace(old, new, 1)

namespace = {'__file__': str(Path(__file__).resolve()), '__name__': '__main__'}
exec(compile(src, str(base), 'exec'), namespace)
