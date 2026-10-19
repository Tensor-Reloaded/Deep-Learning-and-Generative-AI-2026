"""Execute the S4 notebook and export a static HTML fallback with embedded plots.

Run with the course .venv after registering its dl-2026 ipykernel (see 00_START).
"""
from pathlib import Path
import re

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

root = Path(__file__).resolve().parents[1]
lesson = root / 'Seminars' / 'S04_MobileNet'
path = lesson / '01_MobileNet.ipynb'
notebook = nbformat.read(path, as_version=4)
NotebookClient(
    notebook, timeout=180, kernel_name='dl-2026',
    resources={'metadata': {'path': str(lesson)}},
).execute()
nbformat.validate(notebook)
nbformat.write(notebook, path)
html, _ = HTMLExporter(template_name='lab').from_notebook_node(notebook)
# The fallback is static: saved plots and outputs do not need remote scripts.
html = re.sub(r'<script\b[^>]*\bsrc=[^>]*>.*?</script>', '', html,
              flags=re.DOTALL | re.IGNORECASE)
html = html.replace('</head>', '<style>.jp-RenderedHTMLCommon{font-size:19px;line-height:1.55}</style></head>')
(lesson / '01_MobileNet.html').write_text(html)
print(f'Executed {sum(c.cell_type == "code" for c in notebook.cells)} code cells; saved notebook and HTML.')
