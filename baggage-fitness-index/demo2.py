from modules import DeepVision
import argparse
from config import airplane_bin

ap = argparse.ArgumentParser()
ap.add_argument('-s', '--image_s', required=True,
                help='path to side input image')


ap.add_argument('-t', '--image_t', required=True,
                help='path to top input image')

args = ap.parse_args()

dv_s = DeepVision("model/yolov3.weights", "model/yolov3.cfg",
                  "model/yolov3.txt", "ppm_config.json", args.image_s)

dv_t = DeepVision("model/yolov3.weights", "model/yolov3.cfg",
                  "model/yolov3.txt", "ppm_config.json", args.image_t)

length_a = 0
length_b = 0
width = 0
height = 0
for ds in dv_s.detect():
    length_a, height = ds[0], ds[1]
    print(length_a, height)

for dt in dv_t.detect():
    length_b, width = dt[0], dt[1]
    print(length_b, width)

length = (length_a + length_b) * 0.5

volume = length * width * height

volume_bin = airplane_bin['length'] * \
    airplane_bin['width'] * airplane_bin['height']

fitness_index = volume / volume_bin

# print("Baggage Fitness Index: {}".format(fitness_index))
