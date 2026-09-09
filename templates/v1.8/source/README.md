# FSL v1.8 document build

The method words come only from the adopted English Markdown source. The small native Word layout data preserves the approved typography, ownership grid and authoring/example text; it is internal build data, not a required FSL authoring, iteration or lifecycle schema. No font files are included.

Install requirements.txt, then run `python build.py --method /path/to/FSL-v1.8-SKILL.md --output /path/to/output`. Convert the three DOCX files to PDF with LibreOffice, then run `python verify.py /path/to/output --method /path/to/FSL-v1.8-SKILL.md --selftest`.

The verifier checks the exact adopted method hash, method paragraph correspondence, original template/sample text hashes, 3/1/1 pages, per-page identity/footer and normative bold/underline. Visual review remains necessary. Rebuilds need not have identical PDF or archive metadata; the published package has its own exact checksums.
