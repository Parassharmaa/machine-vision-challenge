from modules import BaggageDim

bd = BaggageDim("data/bag_top_5.jpeg", "ppm_config")
dims = bd.get_dim()
print("Length: {}, Width: {}".format(dims[0][0], dims[0][1]))
bd.display()
