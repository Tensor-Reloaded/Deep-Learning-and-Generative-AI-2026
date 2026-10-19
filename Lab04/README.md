## Lab 4 — MobileNet and EfficientNet

### Slides

[Advanced CV Architectures — ML@B / Berkeley Deep Learning](https://docs.google.com/presentation/d/1CC_V5M96L_mL8SM5QTSosanvxInGQk0xGMfn9tNbQZQ/edit#slide=id.g239cc5d2af6_1_10)

- Slides 27–31: MobileNet.
- Slides 33–34: Squeeze-and-Excitation.
- Slides 35–38: EfficientNetV2. For the original EfficientNet and compound scaling, see the 2019 paper below.

[Alternative shared copy of the presentation](https://docs.google.com/presentation/d/1khoyPFJStL3nJAqiqCLTZ1cvvjiq_62ifgIaywVESl0/edit)

***

### Papers

| Topic | Paper on arXiv | PDF / useful figures |
|---|---|---|
| MobileNetV1 | [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) | [PDF, page 3](https://arxiv.org/pdf/1704.04861#page=3) — Figure 2: depthwise + pointwise; §3.1: computational cost. |
| MobileNetV2 | [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381) | [PDF, page 3](https://arxiv.org/pdf/1801.04381#page=3) — Figure 3: residual versus inverted residual. |
| Squeeze-and-Excitation | [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) | [PDF, page 2](https://arxiv.org/pdf/1709.01507v4#page=2) — Figure 1: SE block. |
| EfficientNet | [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946) | [Figure 2, page 2](https://arxiv.org/pdf/1905.11946v5#page=2): scaling; [equation 3, page 4](https://arxiv.org/pdf/1905.11946v5#page=4); [Table 1, page 5](https://arxiv.org/pdf/1905.11946v5#page=5): B0 architecture. |
| EfficientNetV2 | [EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298) | [PDF, page 3](https://arxiv.org/pdf/2104.00298v3#page=3) — Figure 2 and Table 3: MBConv / Fused-MBConv; §4: progressive learning. |

***

### Further reading

- [ResNet](https://arxiv.org/abs/1512.03385) · [PDF](https://arxiv.org/pdf/1512.03385)
- [Batch Normalization](https://arxiv.org/abs/1502.03167) · [PDF](https://arxiv.org/pdf/1502.03167)
- [Searching for Activation Functions (Swish)](https://arxiv.org/abs/1710.05941) · [PDF](https://arxiv.org/pdf/1710.05941)
- [MnasNet](https://arxiv.org/abs/1807.11626) · [PDF](https://arxiv.org/pdf/1807.11626)
- [Searching for MobileNetV3](https://arxiv.org/abs/1905.02244) · [PDF](https://arxiv.org/pdf/1905.02244)
