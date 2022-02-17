FROM python:3.7-slim
COPY . ./yolov5web
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list \
    && apt update && apt install -y libglib2.0-dev libsm6 libxrender1 libxext-dev supervisor libgl1-mesa-glx build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install -r ./yolov5web/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 8091
CMD ["supervisord","-c","/yolov5web/supervisord.conf"]
