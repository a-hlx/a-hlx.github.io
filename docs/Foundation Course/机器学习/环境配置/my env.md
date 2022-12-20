[深度学习环境配置超详细教程【Anaconda+PyTorch(GPU版)+CUDA+cuDNN】_傲寒。的博客-CSDN博客_深度学习环境配置](https://blog.csdn.net/qq_43874102/article/details/123164105)

```
E:\programming\anaconda  
E:\programming\anaconda\Scripts  
E:\programming\anaconda\Library\mingw-w64\bin  
E:\programming\anaconda\Library\bin
```

https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
http://mirrors.aliyun.com/anaconda/pkgs/main

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

conda create -n envname python=3.11 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

conda update conda
conda update anaconda
conda update python

持久添加通道：conda config --add channels 通道地址 
删除通道：conda config --remove channels 通道地址

### packag
```
pytorch          pandas 
pip install labelimg
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
scipy
numpy
matplotlib
opencv_python
torch
torchvision
tqdm
Pillow
h5py
pip install tensorboard
pip install pyyaml


pip install pyqt
pip install pillow
pip install labelme


```

[(15条消息) Labelme安装及使用教程_Marlowee的博客-CSDN博客_labelme安装教程](https://blog.csdn.net/weixin_43427721/article/details/107122775)

#### 更新
sudo python3 -m pip install --upgrade pip

pip list --outdated

pip3 install --upgrade 库名

pip3 install pip-review
pip-review --local --interactive

### GPU

1. 确定显卡算力 – 确定显卡型号 
2. 确定自己的可选择CUDA Runtime Version 
3. 确保自己的 CUDA Driver 版本 >= CUDA Runtime 版本

Cuda runtime version <= cuda driver version 
Cuda runtime version 支持 显卡对应的算力

NVIDIA GeForce GTX 1050   算力6.1

CUDA SDK 9.0 – 9.2 support for compute capability 3.0 – 7.2
CUDA SDK 10.0 – 10.2 support for compute capability 3.0 – 7.5
CUDA SDK 11.0 support for compute capability 3.5 – 8.0
CUDA SDK 11.1 – 11.7 support for compute capability 3.5 – 8.6 

查看驱动，命令行窗口nvidia-smi                   ,CUDA Version: 11.7

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 517.40       Driver Version: 517.40       CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ... WDDM  | 00000000:01:00.0 Off |                  N/A |
| N/A   40C    P0    N/A /  N/A |      0MiB /  2048MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

CUDA官网：
https://developer.nvidia.com/cuda-downloads

cuDNN
下载地址：
https://developer.nvidia.com/rdp/cudnn-download
cudnn有三个文件夹，把这些文件夹中的东西分别放进cuda对应的文件夹中

[PyTorch](https://pytorch.org/)
stable（1.13.0）
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117


```python
import torch
print(torch.__version__)
print(torch.cuda.is_available())
```


### jupyter

```text
pip install jupyter
```

jupyter notebook --generate-config

通过搜索关键词：c.NotebookApp.notebook_dir
修改成以下你自己的“notebook工作文件夹”

jupyter notebook
