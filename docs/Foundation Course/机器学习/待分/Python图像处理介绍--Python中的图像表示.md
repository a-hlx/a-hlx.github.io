点击上方“**小白学视觉**”，选择加"**星标**"或“**置顶**”

重磅干货，第一时间送达![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ow6przZuPIENb0m5iawutIf90N2Ub3dcPuP2KXHJvaR1Fv2FnicTuOy3KcHuIEJbd9lUyOibeXqW8tEhoJGL98qOw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

使用Python进行图像处理是理解如何通过数学和代码表示图片的有趣方法，希望这篇文章能让您了解计算机是如何理解图像数据的。

让我们从导入需要的库开始吧！

```
# First import the required Python Libraries
```

一个图像可以被认为是一个矩阵，其中每个像素的颜色是由一个尺度上的数字表示。

```
array_1 = np.array([[255, 0], 
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/oWYZNQOgMwzW1XmsNf9uqLkyiaYT3Pm3CCt1NZmrA6URslC5vfRm2BxC3cnkY7scqPCNpswms4rb2oeNgb56h4w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

上面的输出是我们刚刚创建的矩阵的直观表示。注意，我们不限于简单的2x2矩阵。以下是3x3矩阵的示例

```
array_2 = np.array([[255, 0, 255], 
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/oWYZNQOgMwzW1XmsNf9uqLkyiaYT3Pm3Cbay4GuicGyrRIsne2UA4icnU5PvZpg2iaQN5QYZXOegahUlOXBJHtLQcQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

我们的示例选择的是光谱中最极端的颜色，但我们也可以访问介于两者之间的任何颜色。

```
array_spectrum = np.array([np.arange(0,255,17), 
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/oWYZNQOgMwzW1XmsNf9uqLkyiaYT3Pm3CU8DzntuIKH3Nyiatd5ibR3Ly69DOrDXib7AzEicXmrF2rQgYJJk0G6WJEA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

下面的图像是使用NumPy的arange函数构造的，并通过获取第一个图像的转置来创建了另一个图像。

为了简单起见，我们一直使用灰度，但请记住，计算机实际上理解的颜色是红色，绿色和蓝色的组合。因此，我们可以将图像表示为三维矩阵。每个像素被表示为一个Python列表，用于指定它们的颜色组合。

```
array_colors = np.array([[[255, 0, 0], 
```

让我们尝试处理真实图像，下面是一只可爱的小狗的图片。

```
doggo = imread('doggo.png')
```

```
doggo.shape
```

检查图像的大小，我们看到它是一个390x385x3矩阵。使用Python我们可以对这个矩阵进行切片，并将每个部分表示为它自己的图像。  

```
fig, ax = plt.subplots(1, 3, 
```

而且我们也可以显示图像的任意部分，下面就是小狗的脸部显示。

```
imshow(doggo[95:250, 130:275]);
```

现在让我们做点有意思的事情~

前面我们说过，一个图像可以由一个三维矩阵表示，因此我们可以通过以下操作，将图像分解成红色、绿色和蓝色来分别显示。

```
fig, ax = plt.subplots(1, 3, figsize=(12,4), sharey = True)
```

此外，我们可以将图像从RGB(红，绿，蓝)转换为HSV(色相，饱和度，值)。  

```
doggo_hsv = rgb2hsv(doggo)
```

最后，我们还可以将图像矩阵转换为灰度。通过将图像转换为简单的二维矩阵，这使我们能够轻松地根据每个像素与指定值的关系来过滤图像。  

```
doggo_gray = rgb2gray(doggo)
```

通过本文我们了解了如何使用Python加载和操作图像。为了更好地理解图像在Python中的显示，最好的办法就是动手复现一下上述代码。

使用Python进行图像处理是理解如何通过数学和代码表示图片的有趣方法，希望这篇文章能让您了解计算机是如何理解图像数据的。

让我们从导入需要的库开始吧！

```
# First import the required Python Libraries
```

一个图像可以被认为是一个矩阵，其中每个像素的颜色是由一个尺度上的数字表示。

```
array_1 = np.array([[255, 0], 
```

上面的输出是我们刚刚创建的矩阵的直观表示。注意，我们不限于简单的2x2矩阵。以下是3x3矩阵的示例。

```
array_2 = np.array([[255, 0, 255], 
```

我们的示例选择的是光谱中最极端的颜色，但我们也可以访问介于两者之间的任何颜色。

```
array_spectrum = np.array([np.arange(0,255,17), 
```

下面的图像是使用NumPy的arange函数构造的，并通过获取第一个图像的转置来创建了另一个图像。

为了简单起见，我们一直使用灰度，但请记住，计算机实际上理解的颜色是红色，绿色和蓝色的组合。因此，我们可以将图像表示为三维矩阵。每个像素被表示为一个Python列表，用于指定它们的颜色组合。

```
array_colors = np.array([[[255, 0, 0], 
```

让我们尝试处理真实图像，下面是一只可爱的小狗的图片。

```
doggo = imread('doggo.png')
```

```
doggo.shape
```

检查图像的大小，我们看到它是一个390x385x3矩阵。使用Python我们可以对这个矩阵进行切片，并将每个部分表示为它自己的图像。  

```
fig, ax = plt.subplots(1, 3, 
```

而且我们也可以显示图像的任意部分，下面就是小狗的脸部显示。

```
imshow(doggo[95:250, 130:275]);
```

现在让我们做点有意思的事情~

前面我们说过，一个图像可以由一个三维矩阵表示，因此我们可以通过以下操作，将图像分解成红色、绿色和蓝色来分别显示。

```
fig, ax = plt.subplots(1, 3, figsize=(12,4), sharey = True)
```

此外，我们可以将图像从RGB(红，绿，蓝)转换为HSV(色相，饱和度，值)。  

```
doggo_hsv = rgb2hsv(doggo)
```

最后，我们还可以将图像矩阵转换为灰度。通过将图像转换为简单的二维矩阵，这使我们能够轻松地根据每个像素与指定值的关系来过滤图像。  

```
doggo_gray = rgb2gray(doggo)
```

通过本文我们了解了如何使用Python加载和操作图像。为了更好地理解图像在Python中的显示，最好的办法就是动手复现一下上述代码。

**好消息！**

**小白学视觉知识星球**

开始面向外开放啦👇👇👇

```
下载1：OpenCV-Contrib扩展模块中文版教程在「小白学视觉」公众号后台回复：扩展模块中文教程，即可下载全网第一份OpenCV扩展模块教程中文版，涵盖扩展模块安装、SFM算法、立体视觉、目标跟踪、生物视觉、超分辨率处理等二十多章内容。下载2：Python视觉实战项目52讲在「小白学视觉」公众号后台回复：Python视觉实战项目，即可下载包括图像分割、口罩检测、车道线检测、车辆计数、添加眼线、车牌识别、字符识别、情绪检测、文本内容提取、面部识别等31个视觉实战项目，助力快速学校计算机视觉。下载3：OpenCV实战项目20讲在「小白学视觉」公众号后台回复：OpenCV实战项目20讲，即可下载含有20个基于OpenCV实现20个实战项目，实现OpenCV学习进阶。交流群欢迎加入公众号读者群一起和同行交流，目前有SLAM、三维视觉、传感器、自动驾驶、计算摄影、检测、分割、识别、医学影像、GAN、算法竞赛等微信群（以后会逐渐细分），请扫描下面微信号加群，备注：”昵称+学校/公司+研究方向“，例如：”张三 + 上海交大 + 视觉SLAM“。请按照格式备注，否则不予通过。添加成功后会根据研究方向邀请进入相关微信群。请勿在群内发送广告，否则会请出群，谢谢理解~
```