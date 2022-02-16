# 修改torch的缓存路径，避免windows下因盘符问题导致的异常
import torch

torch.hub._hub_dir = '../.cache'
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
