# YOLOv5 web演示

基于开源项目[yolov5](https://github.com/ultralytics/yolov5)构建。

在其基础上提供了http调用的接口，便于你在其他的项目中调用。

并且提供了易于使用的web页面，便于调试或日常使用。


## 注意

因希望运行时获取最新的代码，所以提交代码时，把.cache目录下的yolov5和模型pt文件删除掉了。

项目运行时，为了启动速度又使用的本地缓存yolov5代码。文件[yolov5_model_init.py](backend/yolov5_model_init.py):
```python
# 因为下载实在太慢，从本地加载yolov5
if os.path.exists('../.cache/ultralytics_yolov5_master'):
    model = torch.hub.load('../.cache/ultralytics_yolov5_master', 'custom', path='yolov5s.pt',
                       source='local')  # or yolov5m, yolov5l, yolov5x, custom
else:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
```

所以建议，docker打包前、最好本地先运行一下项目。会自动把上述两个文件下载到本地，节约构建时间和镜像的运行时间。

> 构建镜像很慢，大概花了45分钟。
>
> 镜像很大，最终大小为4.46GB
>
> dockerhub上传的镜像是amd64下构建

## 安装需求  
 
### 运行平台  
* ✔ Python 3.6+  
* ✔ Ubuntu 16.04
* ✔ ️Ubuntu 18.04
* ✔ CentOS 7   
* ✔ Docker   

Windows和MacOS系统下可通过构建Docker镜像来使用，暂不支持直接部署使用  
其他Linux平台暂未测试，可自行安装测试  

### 最低配置要求  
* CPU:    1核  
* 内存:    2G  
* SWAP:   2G  

## 安装说明  
### 服务器部署
1. 安装python3.7  
    推荐使用miniconda
    
2. 安装依赖包  
``` shell script
pip install -r requirements.txt
```  

3. 运行  
项目默认运行在8091端口：  
``` shell script
python backend/main.py [--port=8091]
# --port 指定运行时端口号 默认是8091
```

看到以下输出则代表安装成功： 
```shell script
Server is running: http://192.168.0.18:8091
```   

> 需要注意，启动项目时加载模型所需时间较长。请耐心等待一会

### Docker部署  
使用 Dockerfile 构建 或者直接 Pull镜像  
```shell script
# dockerfile 构建
docker build -t yolov5web:latest .

# 运行镜像
docker run -itd --rm -p 8091:8091 --name yolov5web yolov5web:latest 
```  

```shell script
# 从 dockerhub pull
docker pull litterguy/yolov5web:latest

# 运行镜像
docker run -itd --rm -p 8091:8091 --name yolov5web litterguy/yolov5web:latest 
```  
这里把容器的8091端口映射到了物理机的8091上，但如果你不喜欢映射，去掉run后面的`-p 8091:8091` 也可以使用docker的IP加`8091`来访问  

参考项目：

   - [yolov5](https://github.com/ultralytics/yolov5)
   - [TrWebOCR](https://github.com/alisen39/TrWebOCR)