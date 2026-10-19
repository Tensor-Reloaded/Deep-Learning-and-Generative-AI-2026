# S4 · MobileNet + EfficientNet

Updated 19 October: both architectures are covered today. Next session is Object Detection; S6 remains open for RL or SSL. Folder name is retained so existing links keep working.

1. **[01_MobileNet.ipynb](01_MobileNet.ipynb)** — first half; core sections 1–4 and 8. Section 5 and detailed benchmark are optional.
2. **[02_Playground.html](02_Playground.html)** — open during the cost/shape exercises.
3. **[03_EfficientNet.ipynb](03_EfficientNet.ipynb)** — second half: SE, scaling, B0, V2.
4. **[04_Papers.html](04_Papers.html)** — ordered arXiv/PDF index for projection ([Markdown](04_Papers.md)).

Use one VS Code window with the two notebooks and one Brave window. HTML exports [01_MobileNet.html](01_MobileNet.html) and [03_EfficientNet.html](03_EfficientNet.html) are fallbacks with saved outputs, not extra lessons.

CPU, synthetic inputs, no model/data downloads. No new graded task or deadline. Instructor answers are stored separately.

## Re-execute from repository root

```sh
.venv/bin/python -m ipykernel install --prefix "$PWD/.venv" --name dl-2026 --display-name 'DL 2026 (local)'
.venv/bin/python scripts/execute_s04_mobilenet.py
```

The execution script runs both notebooks and exports HTML. The MobileNet builder overwrites edits and clears outputs; use only for source regeneration, then re-execute.
