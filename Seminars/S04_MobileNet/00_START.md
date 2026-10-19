# S4 · MobileNet

1. Open **[01_MobileNet.ipynb](01_MobileNet.ipynb)** in VS Code/Jupyter with the course `.venv`.
2. Open **[02_Playground.html](02_Playground.html)** in a browser when prompted by the notebook.
3. **[01_MobileNet.html](01_MobileNet.html)** is a fallback with saved outputs, not an extra lesson.

Core: spatial/channel factorization, parameter and MAC accounting, a V1 block. Then width/resolution, measured latency, and V2 inverted residuals. Exercises are formative; no new graded task or deadline.

All examples are synthetic or randomly initialized, run on CPU and require no downloads. Run all cells from the notebook directory. Figure files are recreated in `figures/`.

Primary sources are linked in the notebook. Instructor-only notes and prior teaching history are stored separately in the private teaching workspace.

## Regenerate (optional, from the repository root)

Saved outputs are ready to present. To re-execute with the course environment:

```sh
.venv/bin/python -m ipykernel install --prefix "$PWD/.venv" --name dl-2026 --display-name 'DL 2026 (local)'
.venv/bin/python scripts/execute_s04_mobilenet.py
```

The authoring scripts `scripts/build_s04_mobilenet.py` and `scripts/build_s04_playground.py` regenerate the lesson sources. The notebook builder overwrites notebook edits and clears outputs; re-execute afterwards.
