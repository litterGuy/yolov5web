# 修改torch的缓存路径，避免windows下因盘符问题导致的异常
import os

import torch

torch.hub._hub_dir = '../.cache'
# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# 因为下载实在太慢，从本地加载yolov5
if os.path.exists('../.cache/ultralytics_yolov5_master'):
    model = torch.hub.load('../.cache/ultralytics_yolov5_master', 'custom', path='yolov5s.pt',
                       source='local')  # or yolov5m, yolov5l, yolov5x, custom
else:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom


# Inference Settings
# YOLOv5 models contain various inference attributes such as confidence threshold, IoU threshold, etc. which can be set by:

# model.conf = 0.25  # NMS confidence threshold
#       iou = 0.45  # NMS IoU threshold
#       agnostic = False  # NMS class-agnostic
#       multi_label = False  # NMS multiple labels per box
#       classes = None  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
#       max_det = 1000  # maximum number of detections per image
#       amp = False  # Automatic Mixed Precision (AMP) inference
#
# results = model(im, size=320)  # custom inference size
