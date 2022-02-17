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
