## Lab 5

---

Homework 3: https://www.kaggle.com/t/38b93f788de44b69a3d7d2a754b500a4

---

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