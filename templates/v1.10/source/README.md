# Local build and verification

The Markdown files at the package root are the editable wording sources. The Python builder generates Word reading copies and renders only the four-square descriptions as a grid. All other material is prose. It does not access the network, create repositories, dispatch agents or start CI.

Install the packages in requirements.txt in a suitable local Python environment. Run `python source/build.py --root .` to regenerate DOCX. Render each DOCX to PDF locally using LibreOffice. Then run `python source/verify.py --root .` and `python source/self_test.py --root .`. After final edits, inspect every rendered page and regenerate the manifest and checksums before distributing changed files.

The declared page counts are 3 for the method, 1 for the template, 1 for the skill, 2 for the worked example and 2 for the optional appendix. Fonts and renderer versions can affect pagination; do not distribute an unchecked regeneration. No font files are bundled.

Use `python source/verify.py --root . --checksums` to check the unchanged distributed package. The checks validate source/document correspondence and payload integrity, not real-world adoption, automatic permission enforcement or biological correctness. This kit installs no monitor or rate limiter.
