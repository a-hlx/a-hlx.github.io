## 一、环境配置

opencv 是用于快速处理图像处理、计算机视觉问题的工具，支持多种语言进行开发如c++、python、java等。本教程所有示例基于opencv-python，使用python语言对数字图像进行处理和研究。

首先我们需要安装一下环境  
1、 python3  
2、 numpy  
3、 opencv-python

安装python3： 廖雪峰python教程有详细的说明，网址[安装python](https://link.zhihu.com/?target=https%3A//www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)  
安装numpy：`pip install numpy`  
安装opencv-python： `pip install opencv-python`

安装完opencv-python后命令行打开python交互式环境：`import cv2` 成功，便说明成功安装了opencv-python

## 二、opencv-python读取、展示和存储图像

### imread函数

imread函数读取数字图像，先看一下官网对于该函数的定义

```
cv2.imread(path_of_image, intflag)
```

函数参数一： 需要读入图像的完整的路径  
函数参数二： 标志以什么形式读入图像，可以选择一下方式：  
**·** _cv2.IMREAD\_COLOR：_ 加载彩色图像。任何图像的透明度都将被忽略。它是默认标志  
**·** _cv2.IMREAD\_GRAYSCALE：_以灰度模式加载图像  
**·** _cv2.IMREAD\_UNCHANGED：_保留读取图片原有的颜色通道

**·** _1 ：_等同于cv2.IMREAD\_COLOR  
**·** _0 ：_等同于cv2.IMREAD\_GRAYSCALE  
**·** _\-1 ：_等同于cv2.IMREAD\_UNCHANGED

来个示例更清楚：

```
import numpy as np
import cv2

gray_img = cv2.imread('img/cartoon.jpg', 0)  #加载灰度图像
rgb_img = cv2.imread('img/cartoon.jpg', 1)   #加载RGB彩色图像
```

### namedWindow()

None = cv2.namedWindow( winname )

### imshow函数

imshow函数作用是在窗口中显示图像，窗口自动适合于图像大小，我们也可以通过imutils模块调整显示图像的窗口的大小。函数官方定义如下：

```
cv2.imshow(windows_name, image)
```

函数参数一： 窗口名称(字符串)  
函数参数二： 图像对象，类型是numpy中的ndarray类型，注：这里可以通过imutils模块改变图像显示大小，下面示例展示

上示例：

```
cv2.imshow('origin image', rgb_img)   #显示原图
cv2.imshow('origin image', imutils.resize(rgb_img, 800))  #利用imutils模块调整显示图像大小
cv2.imshow('gray image', imutils.resize(gray_img, 800))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
```

### waitKey()

retval = cv2.waitKey( [delay] )

retval 表示返回值。如果没有按键被按下，则返回−1；如果有按键被按下，则返回该按
键的 ASCII 码。
delay 表示等待键盘触发的时间，单位是 ms。当该值是负数或者零时，表示无限等待。
该值默认为 0。

cv2.waitKey函数， 首先产看函数定义：

```
cv2.waitKey(time_of_milliseconds)
```

唯一参数 time\_of\_milliseconds是整数，可正可负也可是零，含义和操作也不同，分别对应上面说的两种情况

(1) time\_of\_milliseconds > 0 ：此时time\_of\_milliseconds表示时间，单位是毫秒，含义表示等待 time\_of\_milliseconds毫秒后图像将自动销毁，看以下示例

```
#表示等待10秒后，将销毁所有图像
if cv2.waitKey(10000):
    cv2.destroyAllWindows()

#表示等待10秒，将销毁窗口名称为'origin image'的图像窗口
if cv2.waitKey(10000):
    cv2.destroyWindow('origin image')
```

  
(2) time\_of\_milliseconds <= 0 ： 此时图像窗口将等待一个键盘敲击，接收到指定的键盘敲击便会进行窗口销毁。我们可以自定义等待敲击的键盘，通过下面的例子进行更好的解释

```
#当指定waitKey(0) == 27时当敲击键盘 Esc 时便销毁所有窗口
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

#当接收到键盘敲击A时，便销毁名称为'origin image'的图像窗口
if cv2.waitKey(-1) == ord('A'):
    cv2.destroyWindow('origin image')
```


```python
lena=cv2.imread("lena.bmp")
cv2.imshow("demo",lena)
key=cv2.waitKey()
if key==ord('A'):
    cv2.imshow("PressA",lena)
    cv2.waitKey()
elif key==ord('B'):
    cv2.imshow("PressB",lena)
    cv2.waitKey()
```

```
import cv2
lena=cv2.imread("lena.bmp")
cv2.imshow("demo", lena )
key=cv2.waitKey()
if key!=-1:
	print("触发了按键")
```

### destroyWindow()

函数 cv2.destroyWindow()用来释放（销毁）指定窗口，其语法格式为：
None = cv2.destroyWindow( winname )
其中，winname 是窗口的名称。
在实际使用中，该函数通常与函数 cv2.waitKey()组合实现窗口的释放。

```PYTHON
import cv2
lena=cv2.imread("lena.bmp")
cv2.imshow("demo", lena )
cv2.waitKey()
cv2.destroyWindow("demo")
```

### destroyAllWindows()

函数 cv2.destroyAllWindows()用来释放（销毁）所有窗口，其语法格式为：
None = cv2.destroyAllWindows( )



### imwrite函数

imwrite函数检图像保存到本地，官方定义：

```
retval = cv2.imwrite( filename, img[, params] )
```

retval 是返回值。如果保存成功，则返回逻辑值真（True）；如果保存不成功，则返回逻
辑值假（False）。
filename 是要保存的目标文件的完整路径名，包含文件扩展名。
img 是被保存图像的名称。
params 是保存类型参数，是可选的。

```
cv2.imwrite('rgb_img.jpg', rgb_img)   #将图像保存成jpg文件
cv2.imwrite('gray_img.png', gray_img) #将图像保存成png文件
```


下面给出一个完整读取、展示、保存和图像销毁示例：

```
import cv2
import imutils
import numpy as np

rgb_img = cv2.imread('E:/peking_rw/ocr_project/base_prehandle/img/cartoon.jpg')
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('origin image', imutils.resize(rgb_img, 800))
cv2.imshow('gray image', imutils.resize(gray_img, 800))
cv2.imwrite('rgb_img.jpg', rgb_img)
cv2.imwrite('gray_img.png', gray_img)

#等待一定时间自动销毁图像窗口
#if cv2.waitKey(10000):
#    cv2.destroyAllWindows()
#if cv2.waitKey(10000):
#    cv2.destroyWindow('origin image')

#接收特定键盘销毁图像窗口
#if cv2.waitKey(-1) == ord('A'):
#    cv2.destroyWindow('origin image')
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
```

## 三、图像处理基础

### 图像的基本表示方法

#### 二值图像

白色像素点（白色小方块区域）处理为“1”，将黑色像素点（黑色小方块区域）处理为“0”

只使用一个比特位（0或者 1）就能表示

#### 灰度图像

灰度处理为 256 个灰度级，用数值区间[0, 255]来表示。其中，数值“255”表示纯白色，数值“0”表示纯黑色，其余的数值表示从纯白到纯黑之间不同级别的灰度。

可以用一个字节（8 位二进制值）来表示

有些情况下，也会使用 8 位二进制值来表示一幅二值图像。这种情况下，使用灰度值 255表示白色、灰度值 0 表示黑色。此时，该二值图像内仅有数值 0 和数值 255 两种类型的灰度值（灰度级），不存在其他灰度值的像素点。

#### 彩色图像

在 RGB 色彩空间中，存在 R（red，红色）通道、G（green，绿色）通道和 B（blue，蓝色）通道，共三个通道。每个色彩通道值的范围都在[0, 255]之间，我们用这三个色彩通道的组合表示颜色。

OpenCV 中，通道的顺序是 B→G→R

### 像素处理

像素是图像构成的基本单位，像素处理是图像处理的基本操作，可以通过位置索引的形式对图像内的元素进行访问、处理。

#### 二值图像及灰度图像

可以将二值图像理解为特殊的灰度图像

一个 OpenCV 灰度图像是一个二维数组，可以使用表达式访问其中的像素值。

```python
import cv2
import numpy as np
img=np.zeros((8,8),dtype=np.uint8)
print("img=\n",img)
cv2.imshow("one",img)
print("读取像素点 img[0,3]=",img[0,3])
img[0,3]=255
print("修改后 img=\n",img)
print("读取修改后像素点 img[0,3]=",img[0,3])
cv2.imshow("two",img)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
import cv2
img=cv2.imread("lena.bmp",0)
cv2.imshow("before",img)
for i in range(10,100):
	for j in range(80,100):
		img[i,j]=255
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
```

#### 彩色图像

image[0,0,0]访问图像 image 的 B 通道内的第 0 行第 0 列上的像素点

 第 1 个索引表示第 0 行。
 第 2 个索引表示第 0 列。
 第 3 个索引表示第 0 个颜色通道。

根据上述分析可知，假设有一个红色（其 R 通道值为 255，G 通道值为 0，B 通道值为 0）图像，不同的访问方式得到的值如下。
 img[0,0]：访问图像 img 第 0 行第 0 列像素点的 BGR 值。图像是 BGR 格式的，得到的数值为[0,0,255]。
 img[0,0,0]：访问图像 img 第 0 行第 0 列第 0 个通道的像素值。图像是 BGR 格式的，所以第 0 个通道是 B 通道，会得到 B 通道内第 0 行第 0 列的位置所对应的值 0。
 img[0,0,1]：访问图像 img 第 0 行第 0 列第 1 个通道的像素值。图像是 BGR 格式的，所以第 1 个通道是 G 通道，会得到 G 通道内第 0 行第 0 列的位置所对应的值 0。
 img[0,0,2]：访问图像 img 第 0 行第 0 列第 2 个通道的像素值。图像是 BGR 格式的，所以第 2 个通道是 R 通道，会得到 R 通道内第 0 行第 0 列的位置所对应的值 255。

### 使用 numpy.array 访问像素

numpy.array 提供了 item()和 itemset()函数来访问和修改像素值，而且这两个函数都是经过优化处理的，能够更大幅度地提高处理效率。在访问及修改像素点的值时，利用 numpy.array提供的函数比直接使用索引要快得多，同时，这两个函数的可读性也更好。

#### 二值图像及灰度图像

函数 item()能够更加高效地访问图像的像素点，该函数的语法格式为：
item(行,列)
函数 itemset()可以用来修改像素值，其语法格式为：
itemset(索引值,新值)

img.itemset((3,2),255)将图像第 3 行第 2 列位置上的像素值修改为 255

```python
import numpy as np
img=np.random.randint(10,99,size=[5,5],dtype=np.uint8)
print("img=\n",img)
print("读取像素点 img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改后 img=\n",img)
print("修改后像素点 img.item(3,2)=",img.item(3,2))
```

#### 彩色图像

函数 item()访问 RGB 模式图像的像素值时，其语法格式为：
item(行,列,通道)
函数 itemset()修改（设置）RGB 模式图像的像素值时，其语法格式为：
itemset(三元组索引值,新值)
需要注意，针对 RGB 图像的访问，必须同时指定行、列以及行列索引（通道），例如img.item(a,b,c)。仅仅指定行和列是不可以的。

```python
import cv2
import numpy as np
img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()
```

### 感兴趣区域（ROI）

（Region of Interest，ROI）

a=img[200:400,200:400]
img[200:400,600:800]=a

ROI可复制，局部打码，将一幅图像内的 ROI 复制到另一幅图像内

```python
import cv2
import numpy as np
a=cv2.imread("lenacolor.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("original",a)
face=np.random.randint(0,256,(180,100,3))
a[220:400,250:350]=face
cv2.imshow("result",a)
cv2.waitKey()
cv2.destroyAllWindows()
```

```python
import cv2
lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
cv2.imshow("lena",lena)
cv2.imshow("dollar",dollar)
face=lena[220:400,250:350]
dollar[160:340,200:300]=face
cv2.imshow("result",dollar)
cv2.waitKey()
cv2.destroyAllWindows()
```

### 通道操作

在图像处理过程中，可以根据需要对通道进行拆分和合并。

#### 通过索引拆分

b = img[ : , : , 0 ]
g = img[ : , : , 1 ]
r = img[ : , : , 2 ]

```python
import cv2
lena=cv2.imread("lenacolor.png")
cv2.imshow("lena1",lena)
b=lena[:,:,0]
g=lena[:,:,1]
r=lena[:,:,2]
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
lena[:,:,0]=0
cv2.imshow("lenab0",lena)
lena[:,:,1]=0
cv2.imshow("lenab0g0",lena)
cv2.waitKey()
cv2.destroyAllWindows()
```

#### 通过函数拆分cv2.split()

b=cv2.split(a)[0]
g=cv2.split(a)[1]
r=cv2.split(a)[2]

#### 通道合并cv2.merge()

bgr=cv2.merge([b,g,r])

```python
import cv2
lena=cv2.imread("lenacolor.png")
b,g,r=cv2.split(lena)
bgr=cv2.merge([b,g,r])
rgb=cv2.merge([r,g,b])
cv2.imshow("lena",lena)
cv2.imshow("bgr",bgr)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.destroyAllWindows()
```

### 获取图像属性

 shape：如果是彩色图像，则返回包含行数、列数、通道数的数组；如果是二值图像或者灰度图像，则仅返回行数和列数。通过该属性的返回值是否包含通道数，可以判断一幅图像是灰度图像（或二值图像）还是彩色图像。
 size：返回图像的像素数目。其值为“行×列×通道数”，灰度图像或者二值图像的通道数为 1。
 dtype：返回图像的数据类型。



## 三、图像色彩空间变换函数cv2.cvtColor

本节将图像色彩空间变换函数单独拉出来说，原因：

1、该函数十分常用； 2、应明白为什么需要做图像色彩空间的处理

首先展示一下图像色彩空间变换函数定义：

```
cv2.cvtColor(input_image, flag)
```

参数一： input\_image表示将要变换色彩的图像ndarray对象  
参数二： 表示图像色彩空间变换的类型，以下介绍常用的两种：  
**·** _cv2.COLOR\_BGR2GRAY：_ 表示将图像从BGR空间转化成灰度图，最常用  
**·** _cv2.COLOR\_BGR2HSV：_ 表示将图像从RGB空间转换到HSV空间

如果想查看参数flag的全部类型，请执行以下程序便可查阅，总共有274种空间转换类型：

```
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
```

在之后的图像特征提取和识别学习中，我们经常使用的是将彩色图像转化成灰度图像， 这里解释一下为什么我么总是对灰度图进行处理，增强对以后图像处理操作的理解

图像的颜色主要是由于图像受到外界光照影响随之产生的不同颜色信息，同一个背景物的图像在不同光源照射下产生的不同颜色效果的图像，因此在我们做图像特征提取和识别过程时，我们要的是图像的梯度信息，也就是图像的本质内容，而颜色信息会对我们对梯度信息提取造成一定的干扰，因此我们会在做图像特征提取和识别前将图像转化为灰度图，这样同时也降低了处理的数据量并且增强了处理效果。

## 四、绘制自定义数字图像

  
本小节目的主要是跟着大家通过自定义数字图像来理解什么是数字图像？ 为什么前面提到的图像对象是numpy中的ndarray对象

**1、绘图简单图像**

对于一个长宽分别为w、h的RGB彩色图像来说，它的每个像素值是由(B、G、R)的一个tuple组成，opencv-python中每个像素三个值的顺序是B、G、R，而对于灰度图像来说，每个像素对应的便只是一个整数，如果要把像素缩放到0、1，则灰度图像就是二值图像，0便是黑色，1便是白色。我们通过下面的例子来理解一下

```
import cv2
#这里图像采用的仍旧是上面那个卡通美女啦
rgb_img = cv2.imread('E:/peking_rw/ocr_project/base_prehandle/img/cartoon.jpg')
print(rgb_img.shape)     #(1200, 1600, 3)
print(rgb_img[0, 0])     #[137 124  38]
print(rgb_img[0, 0, 0])  #137

gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)    #(1200, 1600)
print(gray_img[0, 0])    #100
```

从上面我们可以看到彩色图像的高度height = 1200， 宽度w=1600且通道数为3， 像素(0， 0)的值是(137 124 38)，即R=137, G=124, B=38， 对于灰度图像来说便只是单通道的了

因此(0, 0, 0)便是代表一个黑色像素，(255, 255, 255)便是代表一个白色像素。这么想，B=0, G=0, R=0相当于关闭了颜色通道也就相当于无光照进入，所以图像整个是黑的，而(255, 255, 255)即B=255, G=255, R=255， 相当于打开了B、G、R所有通道光线全部进入，因此便是白色。

  
明白了上面的原理我们便可以通过创建numpy的ndarray对象来创建任意的彩色图像和灰度图像了，例如：

```
import cv2
import numpy as np

white_img = np.ones((512,512,3), np.uint8)
white_img = 255*white_img
cv2.imshow('white_img', white_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
```

效果图：

![](https://pic1.zhimg.com/v2-9dceb56747edd899ff4c04d4d010a6d8_b.jpg)

  
接下来我们先来熟悉一下opencv中一些简单几何图像基本绘制函数，然后我们尝试着在上面白色的图像上进行添加新的图像物体，是不是还挺有趣的，我们将介绍直线cv2.line、长方形cv2.rectangle、圆cv2.circle、椭圆cv2.ellipse、多边形cv2.polylines等集合图像绘制函数

  
先介绍一下它们的公共参数：  
**·** _img：_ 表示需要进行绘制的图像对象ndarray  
**·** _color：_ 表示绘制几何图形的颜色，采用BGR即上述说的(B、G、R)  
**·** _thickness：_ 表示绘制几何图形中线的粗细，默认为1，对于圆、椭圆等封闭图像取-1时是填充图形内部  
**·** _lineType ：_ 表示绘制几何图形线的类型，默认8-connected线是光滑的，当取cv2.LINE\_AA时线呈现锯齿状

  
(1) cv2.line函数

直线绘制函数， 函数官方定义为：

```
cv2.line(image, starting, ending, color, thickness, lineType)
```

参数image、color、thickness、lineType分别是上述公共定义，参数starting、ending分别表示线的起点像素坐标、终点像素坐标

  
(2) cv2.rectangle函数

长方形绘制函数，函数官方定义：

```
cv2.rectangle(image, top-left, bottom-right, color, thickness, lineType)
```

参数image、color、thickness、lineType分别是上述公共定义，参数top-left、bottom-right分别表示长方形的左上角像素坐标、右下角像素坐标

  
(3) cv2.circle函数  
圆形绘制函数，官方定义函数为：

```
cv2.circle(image, center, radius, color, thickness, lineType)
```

参数image、color、thickness、lineType分别是上述公共定义，参数center、radius分别表示圆的圆心像素坐标、圆的半径长度，圆绘制函数中当参数thickness = -1 时绘制的是实心圆，当thickness >= 0 时绘制的是空心圆

  
(4) cv2.ellipse函数  
椭圆绘制函数，官方定义为：

```
cv2.circle(image, center, (major-axis-length, minor-axis-length), angle, startAngle, endAngle, color, thickness, lineType)
```

椭圆的参数较多，首先参数image、color、thickness、lineType分别是上述公共定义，椭圆绘制函数中当参数thickness = -1 时绘制的是实心椭圆，当thickness >= 0 时绘制的是空心椭圆，其他参数如下

**·** _center：_ 表示椭圆中心像素坐标  
**·** _major-axis-length：_ 表示椭圆的长轴长度  
**·** _minor-axis-length：_ 表示椭圆的短轴长度  
**·** _angle：_ 表示椭圆在逆时针方向旋转的角度  
**·** _startAngle：_ 表示椭圆从主轴向顺时针方向测量的椭圆弧的起始角度  
**·** _endAngle：_ 表示椭圆从主轴向顺时针方向测量的椭圆弧的终止时角度

  
(5) cv2.polylines函数  
多边形绘制函数，官方定义函数为：

```
cv2.polylines(image, [point-set], flag, color, thickness, lineType)
```

参数image、color、thickness、lineType分别是上述公共定义，其他参数如下：

**·** _\[point-set\]：_ 表示多边形点的集合，如果多边形有m个点，则便是一个m\*1\*2的数组，表示共m个点  
**·** _flag：_ 当flag = True 时，则多边形是封闭的，当flag = False 时，则多边形只是从第一个到最后一个点连线组成的图像，没有封闭

  
现在我们将上面五种几何图像绘制到开始的白色图像上，观看效果：

```
import cv2
import numpy as np

img = np.ones((512,512,3), np.uint8)
img = 255*img
img = cv2.line(img, (100,100), (400,400),(255, 0, 0), 5)
img = cv2.rectangle(img,(200, 20),(400,120),(0,255,0),3)
img = cv2.circle(img,(100,400), 50, (0,0,255), 2)
img = cv2.circle(img,(250,400), 50, (0,0,255), 0)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(0, 255, 255), -1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
img = cv2.polylines(img,[pts],True,(0, 0, 0), 2)

cv2.imshow('img', img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
```

  
自定义图像效果图：  

![](https://pic3.zhimg.com/v2-37c3e0653291eafc7d16ce071fdf9db6_b.jpg)

**2、对图像的简单像素操作**

除了根据数字图像特点绘制特定图像，我们还可以对已有的图像像素进行操作然后得到很多神奇的效果，也就是对图像的像素进行变换

(1) 对图像取反

```
reverse_img = 255 - gray_img  
```

图像取反效果图：

![](https://pic1.zhimg.com/v2-0459df578469c08301c2bc02c2c86928_b.jpg)

  
(2) 对图像像素线性变换

```
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        random_img[i, j] = gray_img[i, j]*1.2
```

图像像素线性变换效果图：

![](https://pic4.zhimg.com/v2-8fca4ea068a45033056e89236ae1644b_b.jpg)

上述两个图像变换完整示例代码：

```
import cv2
import imutils
import numpy as np

rgb_img = cv2.imread('E:/peking_rw/ocr_project/base_prehandle/img/cartoon.jpg')
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
reverse_img = 255 - gray_img

random_img = np.zeros((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        random_img[i, j] = gray_img[i, j]*1.2
cv2.imshow('reverse_img', imutils.resize(reverse_img, 800))
cv2.imshow('random_img', imutils.resize(random_img, 800))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
```

## 五、结语

相信认真一起看完上述知识点，opencv-python已经对于图像的基本操作可以熟练掌握了，同时对数字图像有了一定的理解，在接下来的教程中我还将陆续和大家一起学习诸如：  
**·** 基本概念：亮度、对比度、分辨率、饱和度、尖锐化等基础概念  
**·** 图像灰度变换：线性、分段线性、对数、反对数、幂律(伽马)变换等  
**·** 图像滤波：线性滤波和非线性滤波、空间滤波和频率域滤波，均值滤波、中值滤波、高斯滤波、逆滤波、维纳滤波等各种图像的基本操作

在上述学习完之后然后我们在和大家一起学习一些高级的图像操作如:  
**·** 文本图像的倾斜矫正方法：霍夫变换、透视变换等  
**·** 图像边缘检测：canny算子、sobel算子、Laplace算子、Scharr滤波器等。。。

  
更多资源

CSDN博客可访问： [feilong\_csdn的博客 - 第 1 页 - CSDN博客](https://link.zhihu.com/?target=https%3A//blog.csdn.net/feilong_csdn)

机器学习更多资源请关注公众号： **AI机器学习与知识图谱，作者：CHEONG**