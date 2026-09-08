# Build source

This v1.6 generator derives from the verified v1.5 generator already present in the repository.

```sh
python -m pip install -r source/requirements.txt
python source/build_templates.py --output .
```

Render PDFs with LibreOffice and verify page counts, lifecycle wording and footer before publishing. FSL does not require YAML lifecycle tracking.
