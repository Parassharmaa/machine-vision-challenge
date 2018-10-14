import json
from .vision_base import VisionBase
import cv2 as cv


class BaggageDim(VisionBase):
    def __init__(self, image_path, config_file):
        super().__init__(image_path)
        self.config_file = "{}.json".format(config_file)
        self.dimensions = []

    def load_file(self):
        data = json.load(open(self.config_file))
        return data

    def get_dim(self):
        contours = self.get_contours()

        pixels_per_metric = self.load_file()['ppm'][0]
        for c in contours:
            pix_dim = self.get_pixel_dim(c)
            if pix_dim is None:
                continue
            d_a, d_b, tr, trbr_x, trbr_y = pix_dim
            dim_a = d_a / pixels_per_metric
            dim_b = d_b / pixels_per_metric            
            self.dimensions.append((dim_a, dim_b, tr, trbr_x, trbr_y))
        return self.dimensions

    def display(self):
        for (dim_a, dim_b, tr, trbr_x, trbr_y) in self.dimensions:
            cv.putText(self.image, "{:.1f}in".format(dim_a),
                       (int(tr[0] - 15), int(tr[1] - 10)
                        ), cv.FONT_HERSHEY_SIMPLEX,
                       2.65, (255, 255, 255), 2)
            cv.putText(self.image, "{:.1f}in".format(dim_b),
                       (int(trbr_x + 10), int(trbr_y)), cv.FONT_HERSHEY_SIMPLEX,
                       .65, (255, 255, 255), 2)
        self.show_image()
