# Machine Vision Challenge

### Baggage Fitness Index

---

#### Abstract

Solution to this process is a two phase process i.e finding the object and then calculating the dimensions of side view and top view of the object.

To detect and localize the object 2 methods can be used

1. Edge Dectection
2. Object Localization using Deep Learning.

My solution includes both the methods. Edge dectection was helpful in detecting rectangular object but performed poorly sometimes. Second method uses yolo-v3 model to detect baggages, backpacks and analyse the bounding box.

To find the dimension, first a camera is set at particular distance and calibrated using reference image. It is used to get pixel per metric (ppm). For every view field camera need to be calibrated.

[View Code and Results]()

### Floor Cleanliness Detection

---

#### Abstract

This problem gets little complex as their can be variety of uncertain scenarios. Therefore a heuristics based algorithm might fail occasionally.

My solutions uses a Deep Convolutional Neural Network Based object classifier that classifies floor image to clean or not clean.

The classifier was trained on images available on the web. The classfier reached accuracy of around 70% when trained in ~250 images per class (plus images were also augmented)

Classifier can be improved on providing more accurate and quality data.

[View Code and Results]()

### Contact

mail2paras.s@gmail.com
