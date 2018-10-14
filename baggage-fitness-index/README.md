# Baggage Fitness Index

### Structure

- data/ - contains calibration and testing images
- config/ - contains config like airplan bin dimensions
- model/ - yolo-v3 model weigths, config and class labels
- modules/ - Primary source code
- ./calibrate.py - calibrates camera and calculates pixel per metric
- ./demo1.py - calculates dimension using edge detection module
- ./demo2.py - calculates dimensions using yolo-v3 model.
- ./ppm_config.json - calibrated pixel per mertric configuration

### Setup

- Install OpenCV

- Download Yolo V3 weights and save in model directory.

```
$ cd model/
$ wget https://pjreddie.com/media/files/yolov3.weights
```

- Installing Dependencies

```bash
$ pip3 install -r requirements.txt
```

- Sample calibration data and test data in provided in data/ folder.

### Usage

- Calibrating the camera and calculating PPM

```bash
# image and object length, width is provided
$ python3 calibrate -i data/calibration_1.jpeg -l 3.6 -w 3.6
```

![countours](https://github.com/Parassharmaa/machine-vision-challenge/blob/master/baggage-fitness-index/outputs/Screenshot%202018-10-14%2019:42:09.png)
![calibration](https://github.com/Parassharmaa/machine-vision-challenge/blob/master/baggage-fitness-index/outputs/Screenshot%202018-10-14%2019:42:58.png)

- Run Dimension Detection

```bash
# provide side view and top view of the image
$ python3 demo2.py -s data/bag_side.jpeg -t data/bag_top_2.jpeg

30.46796105289108 27.010371904824137
26.70598053846545 21.55052132727145

```

![Top View](https://github.com/Parassharmaa/machine-vision-challenge/blob/master/baggage-fitness-index/outputs/Screenshot%202018-10-14%2019:48:00.png)

### Conclusion
- Accuracy of the calculation depends on the calibration of the camera and correctness of PPM


### Future Works

- Using depth measurement and stereo camera, this process cab be made more accurate, real time and efficient.
