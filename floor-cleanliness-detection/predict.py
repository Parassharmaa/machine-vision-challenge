from keras.models import load_model
import sys
import numpy as np
from keras.preprocessing import image
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='input image')

args = ap.parse_args()


image_path = args.image


model_path = "model_002.h5"

labels = {0: 'CLEAN', 1: 'NOT CLEAN'}

test_image = image.load_img(image_path, target_size=(150, 150))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

model = load_model(model_path)

preds = model.predict_classes(test_image)

label = labels[preds[0][0]]

print(image_path, label)
