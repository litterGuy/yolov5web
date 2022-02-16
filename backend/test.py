import base64
from io import BytesIO

import torch
from PIL import Image
from torch import hub

# 修改torch的缓存路径，避免windows下因盘符问题导致的异常
hub._hub_dir = '../../.cache'
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img = '../../.cache/ultralytics_yolov5_master/data/images/zidane.jpg'
# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

print(results.pandas().xyxy[0].to_json(orient="records"))

# 打印base64
results.imgs # array of original images (as np array) passed to model for inference
results.render()  # updates results.imgs with boxes and labels
for img in results.imgs:
    buffered = BytesIO()
    img_base64 = Image.fromarray(img)
    img_base64.save(buffered, format="JPEG")
    print(base64.b64encode(buffered.getvalue()).decode('utf-8'))  # base64 encoded image with results
