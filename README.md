# Machine Vision Challenge

### Baggage Fitness Index

---

#### Abstract

Solution to this process is a two-phase process i.e finding the object and then calculating the dimensions of the side view and top view of the object.

To detect and localize the object 2 methods can be used

1. Edge Detection
2. Object Localization using Deep Learning.

My solution includes both the methods. Edge detection was helpful in detecting rectangular object but performed poorly sometimes. The second method uses the Yolo-v3 model to detect baggage, backpacks and analyze the bounding box.

To find the dimension, first, a camera is set at a particular distance and calibrated using the reference image. It is used to get pixel per metric (ppm). For every view, the camera needs to be calibrated.

[View Code and Results](https://github.com/Parassharmaa/machine-vision-challenge/tree/master/baggage-fitness-index)

### Floor Cleanliness Detection

---

#### Abstract

This problem gets a little complex as there can be a variety of uncertain scenarios. Therefore a heuristics based algorithm might fail occasionally.

My solutions use a Deep Convolutional Neural Network Based object classifier that classifies floor image to clean or not clean.

The classifier was trained on images available on the web. The classifier reached an accuracy of around 70% when trained on ~250 images per class (plus images were also augmented)

The classifier can be improved on providing more accurate and quality data.

[View Code and Results](https://github.com/Parassharmaa/machine-vision-challenge/tree/master/floor-cleanliness-detection)

### Contact

mail2paras.s@gmail.com
