## Lab 2

***

PyTorch Recap: [beginner PyTorch](https://github.com/Tensor-Reloaded/AI-Learning-Hub/tree/main/resources/beginner_pytorch).

The exercises from Notebook 4, 5, 6 should be done at home, before/after the lab. They are a good way of learning DL and PyTorch. 

***

Lab Notebook

1. [Complex Yet Simple Training Pipeline](https://github.com/Tensor-Reloaded/AI-Learning-Hub/blob/main/resources/advanced_pytorch/ComplexYetSimpleTrainingPipeline.ipynb)
2. [Inference Optimization And TTA](https://github.com/Tensor-Reloaded/AI-Learning-Hub/blob/main/resources/advanced_pytorch/InferenceOptimizationAndTTA.ipynb)

The exercises from this notebook are a good preparation for homework 2.

<details><summary>Bonus points</summary>
You will get several bonus points (5 to 10) if you do all exercises from "Complex Yet Simple Training Pipeline" and submit them until Lab 4.
<br>
You will get several bonus points (5 to 10) if you do all exercises from "Inference Optimization And TTA" and submit them until Lab 5.
</details>

***

For self-study (for students who want to pass):
* [Neural Networks (chapter 1 - chapter 4)](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (animated introduction to neural networks and backpropagation) - last chance before Homework 1
* Dataset: https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset
* DataLoader: https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader
* TorchVision transforms getting started: https://docs.pytorch.org/vision/main/auto_examples/transforms/plot_transforms_getting_started.html
* TorchVision examples: https://docs.pytorch.org/vision/stable/auto_examples/transforms/plot_transforms_illustrations.html
* Skim over the 2 references, LeCun (98) and Keskar (2017).

***


Advanced (for students who want to learn more):
* Considering following the [roadmap](https://github.com/Tensor-Reloaded/AI-Learning-Hub/blob/main/foundations/roadmap.md) at your own pace. Do the exercises in each notebook.
* Learn how to choose hyperparameters and the influence of batch size:
  * [Gradient Based Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf) (LeCun, 98)
  * [On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima](https://arxiv.org/abs/1609.04836) (Keskar, 2017)
* `pin_memory` & `non_blocking=True`:
   * Pinning memory in DataLoaders: https://pytorch.org/docs/stable/notes/cuda.html#use-pinned-memory-buffers
   * How does pinned memory actually work: https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/ 
* Data Augmentation for CV:
  * [RandAugment: Practical automated data augmentation with a reduced search space](https://arxiv.org/abs/1909.13719)
  * [Regularization Strategy to Train Strong Classifiers with Localizable Features](https://arxiv.org/abs/1905.04899)
  * [mixup: Beyond Empirical Risk Minimization](https://arxiv.org/abs/1710.09412)
