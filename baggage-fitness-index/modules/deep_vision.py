import cv2 as cv
import numpy as np
import json
from scipy.spatial import distance as dist


class DeepVision:
    def __init__(self, model_path, model_config, classes_path, config_file, image):
        with open(classes_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.colors = np.random.uniform(
            0, 255, size=(len(self.classes), 3))

        self.model_config = model_config
        self.model = model_path
        self.image = cv.imread(image)
        self.config_file = config_file
        self.scale = 0.00392
        self.conf_threshold = 0.5
        self.nms_threshold = 0.4

    def get_output_layers(self, net):

        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1]
                         for i in net.getUnconnectedOutLayers()]

        return output_layers

    def detect(self):
        net = cv.dnn.readNet(self.model, self.model_config)
        image = self.image
        Width = image.shape[1]

        Height = image.shape[0]
        scale = 0.00392
        blob = cv.dnn.blobFromImage(
            image, self.scale, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)

        outs = net.forward(self.get_output_layers(net))

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indices = cv.dnn.NMSBoxes(
            boxes, confidences, self.conf_threshold, self.nms_threshold)

        for i in indices:
            i = i[0]
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            class_id = class_ids[i]
            # get dimension of bounding box with ppm
            yield self.get_dimensions(box, class_id)

    def get_label(self, class_id):
        return str(self.classes[class_id])

    def draw_box(self, class_id, x, y, x_plus_w, y_plus_h, dim_meta):
        label = self.get_label(class_id)
        color = self.colors[class_id]
        (dim_a, dim_b, tr, trbr_x, trbr_y) = dim_meta
        cv.rectangle(self.image, (x, y), (x_plus_w, y_plus_h), color, 2)

        cv.putText(self.image, "{:.1f}in".format(dim_a),
                   (int(tr[0] - 15), int(tr[1] - 10)
                    ), cv.FONT_HERSHEY_SIMPLEX,
                   0.65, (255, 255, 255), 2)
        cv.putText(self.image, "{:.1f}in".format(dim_b),
                   (int(trbr_x + 10), int(trbr_y)), cv.FONT_HERSHEY_SIMPLEX,
                   0.65, (255, 255, 255), 2)
        ims = cv.resize(self.image, (800, 600))
        cv.imshow("Image", ims)
        cv.waitKey()

        cv.destroyAllWindows()

    def load_file(self):
        data = json.load(open(self.config_file))
        return data

    def get_dimensions(self, box, class_id):

        pixels_per_metric = self.load_file()["ppm"][0]
        (x, y, w, h) = box

        tl = (x, y)
        tr = (x+w, y)
        bl = (x, y+h)
        br = (x+w, y+h)
        (tltr_x, tltr_y) = self.midpoint(tl, tr)
        (blbr_x, blbr_y) = self.midpoint(bl, br)

        (tlbl_x, tlbl_y) = self.midpoint(tl, bl)
        (trbr_x, trbr_y) = self.midpoint(tr, br)

        d_a = dist.euclidean((tr[0], tr[1]), (bl[0], bl[1]))
        d_b = dist.euclidean((tlbl_x, tlbl_y), (trbr_x, trbr_y))
        dim_a = d_a / pixels_per_metric
        dim_b = d_b / pixels_per_metric

        dim_meta = (dim_a, dim_b, tr, trbr_x, trbr_y)

        self.draw_box(class_id, round(
            x), round(y), round(x+w), round(y+h), dim_meta)

        return dim_a, dim_b

    def midpoint(self, point_a, point_b):
        return ((point_a[0] + point_b[0]) * 0.5, (point_a[1] + point_b[1]) * 0.5)
