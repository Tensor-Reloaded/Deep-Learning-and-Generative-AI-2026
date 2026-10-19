# S4 · Papers to project

Open PDFs in the same Brave window. Page numbers below count PDF pages from 1; some browser viewers ignore `#page`, so use the named figure/table as a fallback. Start with the five core papers; background links are optional.

## Today, in teaching order

| Order | Paper / arXiv | Direct PDF and what to show |
|---|---|---|
| 1 | [MobileNets (V1)](https://arxiv.org/abs/1704.04861) | [PDF, p.3](https://arxiv.org/pdf/1704.04861#page=3): Figure 2, factorization; §3.1 cost ratio. Figure 3 / Table 1 continue the block/network story. |
| 2 | [MobileNetV2](https://arxiv.org/abs/1801.04381) | [PDF, p.3](https://arxiv.org/pdf/1801.04381#page=3): Figure 3, inverted residual; Table 1 for block shapes. |
| 3 | [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) | [PDF, p.2](https://arxiv.org/pdf/1709.01507v4#page=2): Figure 1, channel gating. |
| 4 | [EfficientNet](https://arxiv.org/abs/1905.11946) | [Figure 2, p.2](https://arxiv.org/pdf/1905.11946v5#page=2) → [equation 3, p.4](https://arxiv.org/pdf/1905.11946v5#page=4) → [B0 Table 1, p.5](https://arxiv.org/pdf/1905.11946v5#page=5). Optional: Figure 8, p.8, measured scaling comparison. |
| 5 | [EfficientNetV2](https://arxiv.org/abs/2104.00298) | [PDF, p.3](https://arxiv.org/pdf/2104.00298v3#page=3): Figure 2 and Table 3, fused blocks versus throughput; §4 progressive learning. |

## Optional background for today's concepts

| Paper | PDF | When useful |
|---|---|---|
| [ResNet](https://arxiv.org/abs/1512.03385) | [PDF](https://arxiv.org/pdf/1512.03385) | Contrast the residual connection with an inverted residual. |
| [Batch Normalization](https://arxiv.org/abs/1502.03167) | [PDF](https://arxiv.org/pdf/1502.03167) | Explain BN in the blocks; distinguish training/evaluation statistics. |
| [Searching for Activation Functions / Swish](https://arxiv.org/abs/1710.05941) | [PDF](https://arxiv.org/pdf/1710.05941) | The activation seen in the B0 implementation. |
| [MnasNet](https://arxiv.org/abs/1807.11626) | [PDF](https://arxiv.org/pdf/1807.11626) | Architecture search and hardware-aware objectives. |
| [Searching for MobileNetV3](https://arxiv.org/abs/1905.02244) | [PDF](https://arxiv.org/pdf/1905.02244) | Optional later development; do not mix V3 changes into V1/V2. |

## Next session: Object Detection / YOLOv1

These are reading links, not a claim that the full S5 lesson is already prepared.

| Paper | PDF | Role |
|---|---|---|
| [R-CNN](https://arxiv.org/abs/1311.2524) | [PDF](https://arxiv.org/pdf/1311.2524) | Region proposals and per-region processing. |
| [Fast R-CNN](https://arxiv.org/abs/1504.08083) | [PDF](https://arxiv.org/pdf/1504.08083) | Shared feature extraction. |
| [Faster R-CNN](https://arxiv.org/abs/1506.01497) | [PDF](https://arxiv.org/pdf/1506.01497) | Learned region proposals. |
| [YOLOv1](https://arxiv.org/abs/1506.02640) | [PDF](https://arxiv.org/pdf/1506.02640) | Core reading; distinguish the original grid/output formulation from later anchor-based versions. |

S6 is reserved for RL or SSL; no choice between those topics has been made yet.
