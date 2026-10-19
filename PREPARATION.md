# Seminar preparation map

**Ready for S4 (19–20 October): [MobileNet lesson pack](Seminars/S04_MobileNet/00_START.md).** Core V1, width/resolution and latency, followed by a V2 introduction. Includes formative exercises, with no additional graded assignment.

This is a preparation checklist for the 2026 course. It does not replace the published Lab 1 or create assignments. Topic placement after Lab 1 is based on the teaching team's planning and may change.

| Topic | Students should be able to explain | Useful demonstration |
|---|---|---|
| MobileNet | Depthwise spatial filtering followed by pointwise channel mixing | Compare `k² × Cin × Cout` with `k² × Cin + Cin × Cout` parameters, excluding biases. Measure latency as well as operation counts. |
| EfficientNet | Joint scaling of depth, width, and resolution | Compare a fixed compute budget spent on one dimension with compound scaling. Distinguish scaling rules from hardware speed. |
| YOLOv1 | Grid cells, box coordinates, object confidence, class prediction | Annotate one image by hand, map a target to its grid cell, and explain what non-maximum suppression removes. Distinguish v1 from later YOLO versions. |
| Variational autoencoder | Latent distributions, reconstruction term, KL regularization, reparameterization | Interpolate latent samples and compare posterior reconstructions with prior samples. |
| Diffusion models | Forward noising and learned denoising | Animate a fixed image's noise schedule, then separate noise prediction from the iterative sampling procedure. |

The revised plan adds graphs/GNNs in S7 and condenses material previously spread across S2–S4. Do not map old archive numbers directly to the new semester.

## Prerequisite check before the architecture seminars

Students should trace `(batch, features)` through an MLP, explain `zero_grad → backward → step`, use class indices with raw logits for `CrossEntropyLoss`, and calculate convolution output shapes. They should distinguish validation choices from final test evaluation.

## First-course clarification notes

Backpropagation computes gradients; the optimizer updates parameters. ReLU has a conventional subgradient at zero. MSE or cross-entropy does not make an arbitrary neural network's objective convex in its parameters. For `CrossEntropyLoss`, probability targets must be valid probability distributions; `[4., 5., 6.]` is not one. A `Dataset` implements `__getitem__`, not `__get_item__`. Check installed package versions instead of relying on dated version claims in slides.

## Sources

- [Current course and Course 1](https://sites.google.com/view/rbenchea/deep-learning-generative-ai)
- [Current Lab 1](https://github.com/Tensor-Reloaded/Deep-Learning-and-Generative-AI-2026/tree/main/Lab01)
- [Shared foundation roadmap](https://github.com/Tensor-Reloaded/AI-Learning-Hub/blob/main/foundations/roadmap.md)
- [2025 archive](https://github.com/Tensor-Reloaded/Advanced-Topics-in-Neural-Networks-Template-2025), historical reference only
