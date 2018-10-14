import cv2 as cv
import imutils
from imutils import perspective
from imutils import contours
import numpy as np
from scipy.spatial import distance as dist
import json


class VisionBase:
    def __init__(self, image_path):
        self.image_path = image_path
        self.pixels_per_metric_w = None
        self.pixels_per_metric_l = None
        self.image = None

    def midpoint(self, point_a, point_b):
        return ((point_a[0] + point_b[0]) * 0.5, (point_a[1] + point_b[1]) * 0.5)

    def get_contours(self):

        self.image = cv.imread(self.image_path)
        gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (7, 7), 2)

        # edge detection
        edged = cv.Canny(gray, 50, 100)
        edged = cv.dilate(edged, None, iterations=2)
        edged = cv.erode(edged, None, iterations=1)

        cv.imshow("Image", edged)
        cv.waitKey(0)
        cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)

        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        (cnts, _) = contours.sort_contours(cnts)
        return cnts

    def get_pixel_dim(self, c, calibrate=False):
        if cv.contourArea(c) < 8000 and not calibrate:
            return None
        
        if cv.contourArea(c) < 20:
            return None
        box = cv.minAreaRect(c)
        box = cv.cv.BoxPoints(
            box) if imutils.is_cv2() else cv.boxPoints(box)
        box = np.array(box, dtype="int")

        box = perspective.order_points(box)
        cv.drawContours(self.image, [box.astype("int")], -1, (0, 255, 0), 2)

        for (x, y) in box:
            cv.circle(self.image, (int(x), int(y)), 5, (0, 0, 255), -1)

        (tl, tr, br, bl) = box
        (tltr_x, tltr_y) = self.midpoint(tl, tr)
        (blbr_x, blbr_y) = self.midpoint(bl, br)

        (tlbl_x, tlbl_y) = self.midpoint(tl, bl)
        (trbr_x, trbr_y) = self.midpoint(tr, br)

        cv.circle(self.image, (int(tltr_x), int(tltr_y)),
                  5, (255, 0, 0), -1)
        cv.circle(self.image, (int(blbr_x), int(blbr_y)),
                  5, (255, 0, 0), -1)
        cv.circle(self.image, (int(tlbl_x), int(tlbl_y)),
                  5, (255, 0, 0), -1)
        cv.circle(self.image, (int(trbr_x), int(trbr_y)),
                  5, (255, 0, 0), -1)

        cv.line(self.image, (int(tr[0]), int(tr[1])), (int(bl[0]), int(bl[1])),
                (0, 0, 255), 3)
        cv.line(self.image, (int(tlbl_x), int(tlbl_y)), (int(trbr_x), int(trbr_y)),
                (0, 0, 255), 3)

        d_a = dist.euclidean((tr[0], tr[1]), (bl[0], bl[1]))
        d_b = dist.euclidean((tlbl_x, tlbl_y), (trbr_x, trbr_y))
        return (d_a, d_b, tr, trbr_x, trbr_y)

    def show_image(self):
        if self.image is not None:
            imS = cv.resize(self.image, (800, 600))
            cv.imshow("Image", imS)
            cv.waitKey(0)
