# Standalone FSL v1.7 build and verification

Preserve the released payload. Generate a separate working copy rather than overwriting frozen artifacts:

```sh
python -m pip install -r source/requirements.txt
python source/build_templates.py --output /tmp/fsl17-rebuild
libreoffice --headless --convert-to pdf --outdir /tmp/fsl17-rebuild /tmp/fsl17-rebuild/*.docx
python -B source/verify_package.py --documents /tmp/fsl17-rebuild
```

Python 3.10+, python-docx 1.2.0, LibreOffice, Poppler CLI tools and installed Liberation Sans are used. No fonts are distributed. Rendering with a different tool version may change PDF bytes or pagination; inspect all pages and rerun verification. Byte-identical documents across unrelated environments are not promised.

For the unchanged, cleanly extracted release ZIP, run from the payload root:

```sh
python -B source/verify_package.py --root .
```

This verifies the manifest, all payload hashes, method anchors, exact 1/2/3/2 page counts, per-page identities/footer, default squares, FSL first in SPEC, route/adoption guidance and normative DOCX emphasis. It does not prove a downstream project's runtime.

MANIFEST.txt lists the payload except itself and SHA256SUMS.txt. SHA256SUMS.txt hashes every listed file and MANIFEST.txt. The distribution ZIP and its checksum are outside that payload; do not add them to the extracted directory before running --root. No YAML iteration or route schema is needed.
