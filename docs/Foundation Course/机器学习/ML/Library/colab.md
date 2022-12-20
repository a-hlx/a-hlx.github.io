[使用google colab训练YOLOv5模型 - 迷途小书童的Note迷途小书童的Note (xugaoxiang.com)](https://xugaoxiang.com/2020/11/01/google-colab-yolov5/)


```
!pwd
!python
```

```
!nvidia-smi

import torch
torch.__version__

```

接下来就把`google drive`挂载过来，这样就可以在`colab`中使用`google drive`中的资源了

```
import os
from google.colab import drive
drive.mount('/content/drive')
```

```
%cd /content/drive/

%ls

%cd MyDrive/nets/yolov7_pose/
```

```
!git clone https://github.com/ultralytics/yolov5.git
```


```
!python detect.py --weights yolov7-w6-pose.pt --kpt-label
```

!python train.py --data ../mask/data.yaml --cfg models/yolov5s.yaml --weights '' --batch-size 64


训练时，出现了`pyyaml`模块的一个错误，这是由于`pyyaml`版本过低的原因，我们升级下就可以解决

```
!pip install -U pyyaml
```




