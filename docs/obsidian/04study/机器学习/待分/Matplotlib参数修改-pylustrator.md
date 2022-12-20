-   Matplotlib功能强大，但是默认出图不够美观，需要一行一行代码调整参数美化图表；
    
-   本次分享一个工具**pylustrator**，可通过`点击鼠标修改图表配置参数，大大提高Matplotlib的使用效率。`
    

![图片](https://mmbiz.qpic.cn/mmbiz_png/UGxk62Z8n3RBLRk5KhqFxqiblibpVicTyEC4SBB0pw6fTPbKGQaYmibTHEUR3h6eRoeGer1icyWm1m4uJkLV35ia2DtA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

___

## pylustrator安装

```
pip install pylustrator
```

___

## pylustrator使用

只需要导入pylustrator，开启pylustrator即可，添加两行代码：

```
# 导入pylustrator import pylustrator # 开启pylustrator pylustrator.start()
```

举个例子，

```
import numpy as npimport matplotlib.pyplot as plt import pylustrator  pylustrator.start() #开启pylustratordef f(t):    return np.exp(-t) * np.cos(2 * np.pi * t)t1 = np.arange(0.0, 5.0, 0.1)t2 = np.arange(0.0, 5.0, 0.02)plt.style.use('ggplot')plt.subplot(211)plt.plot(t1, f(t1), color='tab:blue', marker='o')plt.plot(t2, f(t2), color='black')plt.subplot(212)plt.plot(t2, np.cos(2 * np.pi * t2), color='tab:orange', linestyle='--')plt.show()
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/UGxk62Z8n3RBLRk5KhqFxqiblibpVicTyEC8WF6aIFKiaOKq1icXjFEvYu8IDfBJG9N5v0o5y8juaHjxtS8Pibkh55zg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)会出现以上界面，鼠标点击即可修改参数，`点击右上角File可保存代码或者修改后的图片。`

进一步学习：https://github.com/rgerum/pylustrator

```
往期精彩回顾适合初学者入门人工智能的路线及资料下载(图文+视频)机器学习入门系列下载机器学习及深度学习笔记等资料打印《统计学习方法》的代码复现专辑机器学习交流qq群955171419，加入微信群请扫码
```