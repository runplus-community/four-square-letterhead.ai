# Build source

Generate editable DOCX files with:

```sh
python -m pip install -r source/requirements.txt
python source/build_templates.py --output .
```

Render PDFs with LibreOffice and verify the exact page counts and footer before publishing. FSL does not require YAML iteration tracking.
