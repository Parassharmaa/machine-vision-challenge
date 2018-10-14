import json

from .vision_base import VisionBase


class Calibration(VisionBase):
    def __init__(self, image_path, real_width, real_length):
        super().__init__(image_path)
        self.real_length = real_length
        self.real_width = real_width

        self.ppm_list = []

        self.calibrate_ref()

    def calibrate_ref(self):
        contours = self.get_contours()
        for c in contours:
            if c is None:
                break
            d_a, d_b, _, _, _ = self.get_pixel_dim(c, True)

            pixels_per_metric_w = d_b / self.real_width
            pixels_per_metric_l = d_a / self.real_length
            self.ppm_list.append(pixels_per_metric_l/2 +
                                 pixels_per_metric_w/2)

    def save_config(self, config_file):
        data = {
            "ppm": self.ppm_list,
            "width": self.real_width,
            "length": self.real_length,
            "ref_image": self.image_path
        }
        json.dump(data, open("{}.json".format(config_file), "w"))
