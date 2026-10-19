## Lab 3

***

Lab Notebook

1. [Using C++ Modules in PyTorch](https://github.com/Tensor-Reloaded/AI-Learning-Hub/blob/main/resources/advanced_pytorch/UsingCppModules.ipynb)


<details><summary>Bonus points</summary>
1. Bonus points will be awarded for creating an open-source Python library published on PyPI that implements unweighted and sample-weighted F1 score kernels in C++ using the PyTorch Tensor API. 
It must support CPU and CUDA tensors, provide wheels for common platforms, and fall back to compilation during <code>pip install</code> when no compatible wheel is available. 
Custom CUDA kernels are not required.
Interested students should contact me for all requirements.
<br>
2. Bonus points will be awarded for contributing significant improvements to <a href="https://github.com/fii-optim-lab/label-metrics" target="_blank" rel="noopener noreferrer">label-metrics</a>: adding surface-distance metrics, improving tests and documentation (creating gh-docs using mkdocs), enhancing the metrics reporting and formatting, providing text-, Markdown-, and HTML-based reports.
Interested students should contact me for additional requirements.
</details>

***

Homework 2: https://www.kaggle.com/t/14f94a9ff05649f79daa9dc8d02ca655

***

For self-study (for students who want to pass):
* Convolutions:
  * [But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) (convolution example; convolutions in image processing; convolutions and polynomial multiplication; FFT)
  * [CNN Explainer](https://poloclub.github.io/cnn-explainer/) (convolutions applied in neural networks)
* Foundational CNN papers:
  * AlexNet:
     - https://www.cs.toronto.edu/~hinton/absps/imagenet.pdf
     - [[Classic] ImageNet Classification with Deep Convolutional Neural Networks](https://youtu.be/Nq3auVtvd9Q)
  * ResNet:
     - https://arxiv.org/abs/1512.03385
     - [[Classic] Deep Residual Learning for Image Recognition](https://www.youtube.com/watch?v=GWt6Fu05voI)
  * BatchNorm: https://arxiv.org/abs/1502.03167
* Advanced optimizers:
  * SAM Optimizer: https://github.com/davda54/sam
  * Muon Optimizer: https://kellerjordan.github.io/posts/muon/
* Hyperparameter tuning / experiment tracking:
  * Tensorboard: https://pytorch.org/docs/stable/tensorboard.html
  * Weights and Biases: https://docs.wandb.ai/guides/integrations/pytorch
* Parallelism: https://docs.pytorch.org/tutorials/beginner/dist_overview.html
  * Tensor parallelism: https://docs.pytorch.org/docs/stable/distributed.tensor.parallel.html
  * Distributed Data Parallel: https://docs.pytorch.org/tutorials/beginner/ddp_series_theory.html

  
***


Advanced (for students who want to learn more):
* C++ & CUDA:
    * Introduction to CUDA: https://developer.nvidia.com/blog/even-easier-introduction-cuda
    * Optimizing preprocessing pipelines with C++ modules: https://medium.com/data-science/how-to-optimize-your-dl-data-input-pipeline-with-a-custom-pytorch-operator-7f8ea2da5206
    * https://docs.pytorch.org/tutorials/advanced/cpp_custom_ops.html
    * https://mlc.ai/modern-gpu-programming-for-mlsys/
    * https://developer.nvidia.com/blog/kernel-fusion-in-nvidia-cuda-optimizing-memory-traffic-and-launch-overhead/
* SAM Optimizer:
  * Sharpness-Aware Minimization for Efficiently Improving Generalization: https://arxiv.org/abs/2010.01412
* Muon Optimizer:
  * PyTorch implementation: https://docs.pytorch.org/docs/stable/generated/torch.optim.Muon.html
  * Muon is Scalable for LLM Training: https://arxiv.org/pdf/2502.16982
  * SOAP, Muon, and Beyond: https://arxiv.org/pdf/2607.20548
  * Use the Muon implementation from timm if you have >2D weight matrices in your network.
* Parallelism tutorials:
  * https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html
  * https://huggingface.co/blog/huseinzol05/tensor-parallelism
  * https://lightning.ai/docs/pytorch/stable/advanced/model_parallel/tp.html
