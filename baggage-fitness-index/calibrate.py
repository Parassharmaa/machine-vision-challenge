from modules import Calibration
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='path to input image')
ap.add_argument('-l', '--length', required=True,
                help='length of object')
ap.add_argument('-w', '--width', required=True,
                help='width of object')
args = ap.parse_args()


calibration_image = args.image

real_length = args.length
real_width = args.width


c = Calibration(calibration_image, float(real_width), float(real_length))
c.show_image()
c.save_config("ppm_config")
