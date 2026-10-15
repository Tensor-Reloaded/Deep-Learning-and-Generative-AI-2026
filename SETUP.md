# Deep Learning and Generative AI 2026

The current course repository also supports CARN (Capitole avansate de rețele neuronale), the equivalent course name for the older cohort. Cristian and George share the teaching by seminar blocks. Internal staffing and dates are recorded in the teaching administration workspace, not in student assessment instructions.

## Local setup

Tested using Python 3.13.5 on macOS. A CPU is enough for the smoke check:

`requirements-tested.txt` records the exact direct package versions used for validation. Select hardware-specific PyTorch wheels separately when reproducing on another platform.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_environment.py
python -m jupyter lab
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.

For NVIDIA/AMD acceleration, choose the appropriate PyTorch wheel using the [official installation selector](https://pytorch.org/get-started/locally/). CUDA instructions do not apply to macOS. MPS uses the Apple GPU; performance depends on the workload. The check deliberately runs on CPU to stay reproducible and reports accelerator availability separately.

The check verifies tensor shapes, cross-entropy class targets, automatic differentiation, a parameter update, loss reduction, and a `DataLoader`. It does not download datasets or claim to validate every upstream notebook.

## First published laboratory

For a portable starting point, open [Lab01/LocalRecap.ipynb](Lab01/LocalRecap.ipynb) or its [HTML copy](Lab01/LocalRecap.html). It uses small CPU tensors and includes a complete miniature training loop.

Follow [Lab01](Lab01/README.md) in this order:

1. Beginner tensor operations for shape fluency.
2. Advanced operations only after the basics are comfortable.
3. Beginner PyTorch training tutorial and the published assignment link.

The companion checkout is at `../AI-Learning-Hub` in the prepared workspace. Its notebooks remain maintained upstream. Start Jupyter with `python -m jupyter lab --notebook-dir ..` if you want to open the sibling checkout with this environment. Select the environment's kernel.

The upstream beginner and advanced tensor notebooks contain explicit CUDA calls, intentional exercise failures, and large allocations. For example, beginner tensor operations allocate two `(10000,200,300)` float32 tensors (about 4.8 GB combined before GPU copies). The advanced image exercise expects `test_image.jpg`, which is absent from the checked-out Hub, and uses OpenCV. Those sections need preparation and are not covered by the CPU smoke check. Use the local recap on this Mac; use a configured CUDA environment for the GPU sections. The optional upstream timing sections also need `timed-decorator`.

Published Course 1 covers neurons, activations, losses, gradients/backpropagation, convolutions, and a PyTorch recap. Course material being available does not establish that every slide has already been taught.

See [PREPARATION.md](PREPARATION.md) for a topic checklist. Use the course page and Lab 1 for assessment rules; no new deadlines are introduced here.
