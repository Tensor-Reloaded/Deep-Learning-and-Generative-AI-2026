## Lab 5

---

Homework 3: https://www.kaggle.com/t/38b93f788de44b69a3d7d2a754b500a4

---

### Practical lab · Build and fine-tune a pedestrian detector (2 hours)


[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tensor-Reloaded/Deep-Learning-and-Generative-AI-2026/blob/main/Lab05/ObjectDetection.ipynb)

**[Student notebook: ObjectDetection.ipynb](ObjectDetection.ipynb)** — save a copy in Drive, select a GPU runtime if available, then work through the seven TODO blocks in order. CPU is also supported. The notebook downloads the dataset and ImageNet weights automatically; no Kaggle token or Drive mount is needed.

Following the Object Detection presentation, this session implements a **simplified Fast R-CNN-style detector** on Penn-Fudan pedestrians. The supplied **ResNet-18 is pretrained for ImageNet classification**, not object detection. You first train a new detection head on its frozen features, then **fine-tune `layer3` and the head together on detection images**. The second stage recomputes features and uses horizontal-flip augmentation.

| Time | Your implementation | Supplied scaffolding |
|---|---|---|
| 0–10 min | Inspect the pipeline and data | Download, seeded train/validation/test split, pretrained backbone |
| 10–25 min | Resize/normalize images and transform bounding boxes | Instance masks → boxes, visualization |
| 25–40 min | Match proposals by IoU; assign foreground/background/ignore labels | Multi-scale geometric proposals and balanced region sampling |
| 40–55 min | Shared MLP, classification branch and box-regression branch | RoI pooling on the shared feature map |
| 55–70 min | Cross-entropy + positive-only Smooth L1; optimization step | Detection data and model interfaces |
| 70–85 min | Write the epoch loop and train the head (experiment A) | Feature caching, decoding, NMS and validation evaluation |
| 85–110 min | Implement end-to-end fine-tuning on full images (experiment B) | Augmentation and differential learning rates |
| 110–120 min | Compare A/B on validation, test once, explain failures | Loss plots, matched-image comparisons and full detector checkpoint |

**Deliverable:** your completed notebook with loss curves for both training stages, head-only versus fine-tuned predictions, held-out precision/recall and answers to the discussion questions. This is an **in-class exercise, separate from Homework 3** above.

We use geometric region proposals and fine-tune only the last backbone block to fit the session. This preserves Fast R-CNN's shared-feature/RoI-pooling/two-head pipeline, but is not an exact reproduction: the original uses selective search and a different backbone/head. There is no RPN here; implementing one is an optional longer extension. Ground-truth boxes are used for training targets and evaluation, never to generate validation/test predictions.

References: [Fast R-CNN paper](https://arxiv.org/abs/1504.08083) · [PDF](https://arxiv.org/pdf/1504.08083) · [ResNet paper](https://arxiv.org/abs/1512.03385) · [Penn-Fudan data](https://www.cis.upenn.edu/~jshi/ped_html/) · [RoI pooling documentation](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.roi_pool.html).

### Object Detection



Classification and localization, bounding boxes, IoU, R-CNN, Fast R-CNN, Faster R-CNN, YOLO, non-maximum suppression and anchor boxes.

### Slides

**[Open the complete presentation — Deep Learning for Object Detection, ML@B / Berkeley Deep Learning](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.p)**

This is the presentation linked in the 2025 Lab05. The table follows all **35 slides** in this copy; click a range to jump to the section. Papers and PDFs are linked directly alongside each topic.

### Slides and papers

| Slides | Topic | Papers / direct PDFs | What to look at |
|---|---|---|---|
| [1–3](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.p) | Introduction and outline | — | Title, original announcements and lecture outline. |
| [4–5](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_7) | Classification → localization → detection | — | What is in the image, where it is, and how to handle several objects. |
| [6–9](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_75) | Landmarks and bounding boxes | — | Add position and size outputs to a classifier; identify the coordinate convention. |
| [10–11](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_312) | Training objectives and IoU | [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) · [PDF](https://arxiv.org/pdf/1506.02640) | IoU = intersection / union. Use YOLO §2.2 to distinguish overlap evaluation from the original training loss. |
| [12–13](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_511) | Multiple objects and sliding windows | [R-CNN: Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation](https://arxiv.org/abs/1311.2524) · [PDF](https://arxiv.org/pdf/1311.2524) | Motivation for region proposals and shared computation. |
| [14–17](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_617) | R-CNN and selective search | [R-CNN: Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation](https://arxiv.org/abs/1311.2524) · [PDF](https://arxiv.org/pdf/1311.2524)<br>[Selective Search for Object Recognition](https://ivi.fnwi.uva.nl/isis/publications/2013/UijlingsIJCV2013/) · [PDF](https://ivi.fnwi.uva.nl/isis/publications/2013/UijlingsIJCV2013/UijlingsIJCV2013.pdf) | Proposal generation, crop/warp, per-region CNN features; compare with the pipeline in the R-CNN paper. |
| [18–19](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_661) | Fast R-CNN | [Fast R-CNN](https://arxiv.org/abs/1504.08083) · [PDF](https://arxiv.org/pdf/1504.08083) | Shared convolutional feature map, RoI pooling, classification and box regression. |
| [20–22](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g25f3ead114f_0_139) | Faster R-CNN | [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497) · [PDF](https://arxiv.org/pdf/1506.01497) | Replace external proposal generation with a region proposal network (RPN); shared features and anchors. |
| [23–27](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g25f3ead114f_0_160) | YOLO: one-stage detection and the grid | [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) · [PDF](https://arxiv.org/pdf/1506.02640) | [Figure 2, PDF p.2](https://arxiv.org/pdf/1506.02640#page=2): grid and predictions; [Figure 3, p.3](https://arxiv.org/pdf/1506.02640#page=3): original architecture. |
| [28–29](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_841) | Non-maximum suppression | [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) · [PDF](https://arxiv.org/pdf/1506.02640) | Rank detections by score and suppress overlapping lower-scoring boxes per class; distinguish NMS threshold from evaluation matching threshold. |
| [30–31](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_989) | Anchor boxes | [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242) · [PDF](https://arxiv.org/pdf/1612.08242)<br>[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497) · [PDF](https://arxiv.org/pdf/1506.01497) | Later YOLO / anchor-based formulation. YOLOv1 predicts boxes directly and does not use predefined anchor boxes. |
| [32–33](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g23ab59ea0ea_0_1428) | YOLO output and summary | [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) · [PDF](https://arxiv.org/pdf/1506.02640)<br>[YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242) · [PDF](https://arxiv.org/pdf/1612.08242) | Compare versions explicitly; use the original paper for YOLOv1 tensor shape and architecture. |
| [34–35](https://docs.google.com/presentation/d/1E4DPhSEGXd9ZnIGzbhnpaPxfqzStpL3xtz5Y0jz5P98/edit#slide=id.g286f16b1f7a_0_5) | Original attendance slide and contributors | — | ML@B closing material and credits. |

### YOLOv1 versus later versions

The deck combines an introductory YOLO explanation with later anchor-based conventions. When presenting the original YOLO paper:

- **Slide 27:** x/y are offsets within a grid cell; width/height are normalized by the full image dimensions in YOLOv1.
- **Slides 30–31:** predefined anchor boxes belong to later YOLO versions, covered by the YOLO9000 paper; multiple box predictors in YOLOv1 are not predefined anchors.
- **Slide 32:** YOLOv1 outputs **S × S × (5B + C)**, with one class-probability vector per cell. For VOC: S=7, B=2, C=20 → **7 × 7 × 30**. Its original architecture has 24 convolutional and 2 fully connected layers, so it is not fully convolutional. S is the number of grid cells along each image dimension, not a fixed 16×16-pixel cell size.
- **Slides 10–11:** IoU measures overlap; the original YOLOv1 training objective uses a weighted sum-squared-error formulation, not simply `1 − IoU`.

Slide 2's quizzes/homework and slide 34's attendance instructions belong to the original ML@B course.

---

***
For self-study (all students):
* https://paperswithcode.co/
* https://d2l.ai/chapter_computer-vision/rcnn.html
* R-CNN vs Fast R-CNN vs Faster R-CNN vs YOLO: https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e

---

Advanced (for students who want to learn more):
* R-CNN: https://arxiv.org/abs/1311.2524v5
* Faster R-CNN: https://arxiv.org/pdf/1506.01497.pdf
* YOLO: https://arxiv.org/abs/1506.02640
* U-Net: https://arxiv.org/abs/1505.04597
* 3D U-Net: https://arxiv.org/abs/1606.06650
* Model Soup: https://arxiv.org/abs/2203.05482