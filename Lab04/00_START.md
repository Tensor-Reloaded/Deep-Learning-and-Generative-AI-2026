# S4 · MobileNet + EfficientNet — open from GitHub

**19–20 October 2026.** Next session: Object Detection / YOLOv1. S6 is reserved for RL or SSL, choice pending.

## Presentation order

Keep one browser window. These links open online; reading the saved notebook outputs requires no Python installation.

| Order | Open | What to present |
|---|---|---|
| 1 | [Google Slides: Advanced CV Architectures, slide 26](https://docs.google.com/presentation/d/1CC_V5M96L_mL8SM5QTSosanvxInGQk0xGMfn9tNbQZQ/edit#slide=id.g239cc5d2af6_1_10) | Slides 27–31: MobileNet. Slides 33–34: SE. Slides 35–38: EfficientNetV2. |
| 2 | [01 · MobileNet notebook on GitHub](01_MobileNet.ipynb) | Spatial/channel filtering, weight-count exercise, V1 block, V2 inverted residual. |
| 3 | [03 · EfficientNet notebook on GitHub](03_EfficientNet.ipynb) | SE, compound scaling, B0 implementation, V2. |
| 4 | [04 · Paper index](04_Papers.md) | Open the matching arXiv PDF when the guide calls for it; figure/table and page links included. |

The Slides link opens the instructor's Drive copy; existing Google sharing permissions apply. [Shared source deck](https://docs.google.com/presentation/d/1khoyPFJStL3nJAqiqCLTZ1cvvjiq_62ifgIaywVESl0/edit) is an alternative; slide navigation above refers to the instructor copy.

## Two-hour route

| Minutes | Topic | Material |
|---|---|---|
| 0–8 | Motivation; NCHW and 1×1 recap | Slides 26, optionally 17–18 |
| 8–23 | Standard → depthwise → pointwise | MobileNet §1–2; V1 Figure 2 |
| 23–35 | Calculate 216 vs 51, then 32→64 | MobileNet §3–4 |
| 35–50 | Inverted residual and linear projection | MobileNet §8; V2 Figure 3 |
| 50–55 | MAC counts versus measured latency | MobileNet §7, saved output |
| 55–60 | Short break | — |
| 60–70 | Squeeze-and-Excitation | EfficientNet §3; SE Figure 1 |
| 70–90 | Compound scaling + calculation | EfficientNet §1–2; original paper Figure 2 / equation 3 |
| 90–102 | Inspect B0 | EfficientNet §4; Table 1 |
| 102–113 | Fused-MBConv and progressive learning | EfficientNet §5; V2 Figure 2 / Table 3 |
| 113–120 | Exit questions | EfficientNet Checks |

Skip MobileNet §5 and §9 if time is tight. The original EfficientNet paper is from 2019; the later slide section covers EfficientNetV2. Do not conflate them. Skip the unqualified 10× speed comparison on slide 32; hardware measurements need context.

## Run code online, if needed

- [Open MobileNet in Colab](https://colab.research.google.com/github/Tensor-Reloaded/Deep-Learning-and-Generative-AI-2026/blob/main/Lab04/01_MobileNet.ipynb)
- [Open EfficientNet in Colab](https://colab.research.google.com/github/Tensor-Reloaded/Deep-Learning-and-Generative-AI-2026/blob/main/Lab04/03_EfficientNet.ipynb)

Use a CPU runtime. The notebooks were executed in the course environment; Colab execution itself has not been verified. Inputs are synthetic and models untrained; no datasets or weights need downloading. No new graded task or deadline.

## Optional downloadable files

The `.html` files in this folder are downloadable exports/playground sources. GitHub's file viewer does not run their JavaScript. They are **not required for the online presentation route above**; the notebook outputs supply the diagrams and worked demonstrations.

For local regeneration only, see [SETUP.md](../SETUP.md) and `scripts/execute_s04_mobilenet.py`. The execution script runs both notebooks and exports HTML. The MobileNet builder overwrites edits and clears outputs; use only for source regeneration.
