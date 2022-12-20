[FCOS:一阶全卷积目标检测 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/63868458)
[FCOS：全卷积一阶段Anchor Free物体检测器，多种视觉任务的统一框架 (qq.com)](https://mp.weixin.qq.com/s/5-zXv7QgWpjSVEKtgKA2Lw)


> 本文介绍一下近期比较热门的一个目标检测算法FCOS(FCOS: Fully Convolutional One-Stage Object Detection)，该算法是一种基于FCN的逐像素目标检测算法，实现了无锚点（anchor-free）、无提议（proposal free）的解决方案，并且提出了中心度（Center—ness）的思想，同时在召回率等方面表现接近甚至超过目前很多先进主流的基于锚框目标检测算法。此外，本算法目前已开源。

现在的各种计算机视觉的任务，比如分割，深度预测，关键点加测，计数等等，都是全卷积的结构，就物体检测是个例外。那么，很自然的就有了一个问题：我们能不能把物体检测也变成类似分割那样的逐像素的预测问题呢？这样的话，这些视觉相关的任务就都统一成了一个架构了，所以说，这篇文章就是干了这么个事情。

# **摘要**

![](https://pic3.zhimg.com/v2-75a00559139b3fe35fa433d156984256_b.jpg)

本文提出一种基于像素级预测一阶全卷积目标检测(FCOS)来解决目标检测问题，类似于语音分割。目前大多数先进的目标检测模型，例如RetinaNet、SSD、YOLOv3、Faster R-CNN都依赖于预先定义的锚框。相比之下，本文提出的FCOS是anchor box free，而且也是proposal free，就是不依赖预先定义的锚框或者提议区域。通过去除预先定义的锚框，FCOS完全的避免了关于锚框的复杂运算，例如训练过程中计算重叠度，而且节省了训练过程中的内存占用。更重要的是，本文避免了和锚框有关且对最终检测结果非常敏感的所有超参数。由于后处理只采用非极大值抑制(NMS)，所以本文提出的FCOS比以往基于锚框的一阶检测器具有更加简单的优点。

___

# **锚框：Anchor box**

## **锚框介绍**

锚框首先在Faster R-CNN这篇文章中提出，后续再很多知名的目标检测模型中得到应用，例如SSD、YOLOv2、YOLOv3(YOLOv1是anchor free的)，在这里不多赘述，想要了解锚框相关内容，请查看我的另一篇文章【[Jackpop：锚框：Anchor box综述](https://zhuanlan.zhihu.com/p/63024247)】。

## **锚框缺点**

1.  检测表现效果对于锚框的尺寸、长宽比（aspect ratio）、数目非常敏感，因此锚框相关的超参数需要仔细的调节。
2.  锚框的尺寸和长宽比是固定的，因此，检测器在处理形变较大的候选对象时比较困难，尤其是对于小目标。预先定义的锚框还限制了检测器的泛化能力，因为，它们需要针对不同对象大小或长宽比进行设计。
3.  为了提高召回率，需要在图像上放置密集的锚框。而这些锚框大多数属于负样本，这样造成了正负样本之间的不均衡。
4.  大量的锚框增加了在计算交并比时计算量和内存占用。

基于anchor的物体检测器的缺点
1.  检测性能依赖于anchor的尺寸，比例，数量，这些都需要非常精细的设计。
    
2.  一旦anchor设计好了，尺寸，比例就固定了，在物体的尺寸和比例多样性非常大的时候会有困难，特别是小物体。预设的anchor的泛化能力也有限，对于新的任务，需要重新去设计anchor。
    
3.  为了有高recall，需要设计非常密集的anchor，FPN中的anchor数量就超过了160k，而且大部分都是负样本，正负样本非常的不均衡。
    
4.  在计算的时候需要计算IOU，非常的复杂。
___

## **FCOS优势**

1.  FCOS与许多基于FCN的思想是统一的，因此可以更轻松的重复使用这些任务的思路。
2.  检测器实现了proposal free和anchor free，显著的减少了设计参数的数目。设计参数通常需要启发式调整，并且设计许多技巧。另外，通过消除锚框，新探测器完全避免了复杂的IOU计算以及训练期间锚框和真实边框之间的匹配，并将总训练内存占用空间减少了2倍左右。
3.  FCOS可以作为二阶检测器的区域建议网络(RPN)，其性能明显优于基于锚点的RPN算法。
4.  FCOS可以经过最小的修改便可扩展到其他的视觉任务，包括实例分割、关键点检测。

# **算法详细介绍**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190412200418676.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1daWjE4MTkxMTcxNjYx,size_16,color_FFFFFF,t_70#pic_center)  
FCOS算法的整体框图如上所示：映入我们眼帘的是什么？对没错是**FPN特征金字塔和三分支的头检测网络**。  
FPN特征金字塔在提出之后，已经得到了广泛的使用，在多个领域中都可以看到它的身影，如语义分割、细粒度分类等等，它的主要思路是结合了网络的浅层特征和深层特征，然后在多个分支同时输出不同大下的目标。充分的使用了网络的浅层特征和深层特征，浅层特征更关注一些细节信息，适合用来定位；而深层特征更关注于语义信息，适合用来分类等。具体的细节可以看我的这篇博客[FPN链接](https://blog.csdn.net/WZZ18191171661/article/details/79494534)。  

整个算法的实现步骤如下所示：  
**步骤1-对输入的图片进行预处理操作；  
步骤2-搭建如图所示的网络架构，将输入数据送入backbone网络中获取输入数据的feature_map，在feature_map的每一点上面进行回归操作，进行网络训练获取网络模型；  
步骤3-将预训练的网络模型应用到测试图片中，从特征金字塔的多个Head中获得预测的结果；  
步骤4-使用NMS等后处理操作获得最终的结果。**

FPN是Feature Parymid Network的缩写。

目标检测任务中，像是在YOLO1中那种，对一个图片使用卷积来提取特征，经过了多个池化层或者stride为2的卷积层之后，输出了一个小尺度的特征图。然后再这个特征图中来做**目标检测**。

换句话说，最后得到的目标检测的结果，完全是依赖于这一个特征图，这种方法叫做**单stage物体检测算法**。

可想而知，这种方法很难有效的识别出不同大小的目标，所以产生了**多stage检测算法**，其实就是要用到了特征金字塔FPN。

简单的说就是：**一个图片同样是经过卷积网络来提取特征，本来是经过多个池化层输出一个特征图，现在是经过多个池化层，每经过一个池化层都会输出一个特征图，这样其实就提取出了多个尺度不同的特征图。**

**然后尺度不同的特征图，丢进特征金字塔网络FPN，做目标检测。**


### FPN结构概述

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/756957fb0b8849e4baf88af0eb627a68~tplv-k3u1fbpfcp-watermark.image)

从图中可以看到：

-   左边的c1，c2表示不同尺度的特征图。原始的图像input的尺寸经过一个池化层或者stride为2的卷积层之后，尺寸减少一半，这样就变成了C1特征图；如果又经过一个池化层，那么就变成C2特征图。
-   C3,C4,C5,C6,C7这个四个尺度不同的特征图，进入FPN特征金字塔网络进行特征融合，然后再用检测头预测候选框。
-   **这里说一些个人的理解（如果有错误，请指正呀）：** 这里刚好区分一下**多stage检测算法**和特征金字塔网络的区别。
    -   多stage检测算法：从上图中我们可以看到P3,P4,P5,P6,P7这五个不同尺度的特征图进入一个检测头预测候选框，这个检测头其实就是一个检测算法，不过这个神经网络的输入是多个不同尺度的特征图，输出则是候选框，所以这是多sgtage检测算法；
    -   特征金字塔网络：这个其实是让不同尺度的特征图之间互相融合，来增强特征图表征能力的一种手段。这个过程不是预测候选框，应该是特征提取的过程。FPN神经网络的输入也是多个不同尺度的特征图，输出也是多个不同尺度的特征图，和输入的特征图是相同的。

**所以呢，一个多stage检测算法其实是可以没有FPN结构，直接用卷积网络输出的C3,C4,C5,C6,C7放进检测头输出候选框的。**


### **1.全卷积一阶检测器**

FCOS首先使用Backone CNN(用于提取特征的主干架构CNN)，另s为feature map之前的总步伐。

**_与anchor-based检测器的区别_**

**_第一点_**

-   anchor-based算法将输入图像上的位置作为锚框的中心点，并且对这些锚框进行回归。
-   FCOS直接对feature map中每个位置对应原图的边框都进行回归，换句话说FCOS直接把每个位置都作为训练样本，这一点和FCN用于语义分割相同。

> FCOS算法feature map中位置与原图对应的关系，如果feature map中位置为$(x,y)$ ,映射到输入图像的位置是 $(\lfloor \frac{s}{2} \rfloor+xs,\lfloor \frac{s}{2} \rfloor+ys)$。

**_第二点_**

-   在训练过程中，anchor-based算法对样本的标记方法是，如果anchor对应的边框与真实边框(ground truth)交并比大于一定阈值，就设为正样本，并且把交并比最大的类别作为这个位置的类别。
-   在FCOS中，如果位置 $(x,y)$ 落入**任何**真实边框，就认为它是一个正样本，它的类别标记为这个真实边框的类别。

> 这样会带来一个问题，如果标注的真实边框重叠，位置 $(x,y)$ 映射到原图中落到多个真实边框，这个位置被认为是模糊样本，后面会讲到用**多级预测**的方式解决的方式解决模糊样本的问题。  

**_第三点_**

-   以往算法都是训练一个多元分类器
-   FCOS训练 $C$C 个二元分类器(_C_是类别的数目)

**_与anchor-based检测器相似之处_**

与anchor-based算法的相似之处是FCOS算法训练的目标同样包括两个部分：位置和类别。

FCOS算法的损失函数为：

$\begin{aligned} L\left(\left\{\boldsymbol{p}_{x, y}\right\},\left\{\boldsymbol{t}_{x, y}\right\}\right) &=\frac{1}{N_{\text { pos }}} \sum_{x, y} L_{\text { cls }}\left(\boldsymbol{p}_{x, y}, c_{x, y}^{*}\right) \\ &+\frac{\lambda}{N_{\text { pos }}} \sum_{x, y} \mathbb{1}_{\left\{c_{x, y}>0\right\}} L_{\operatorname{reg}}\left(\boldsymbol{t}_{x, y}, \boldsymbol{t}_{x, y}^{*}\right) \end{aligned}$

其中 $L_{cls}$是类别损失， $L_{reg}$是交并比的损失。

### **2.用FPN对FCOS进行多级预测**

首先明确两个问题：

1.  基于锚框的检测器由于大的步伐导致低召回率，需要通过降低正的锚框所需的交并比分数来进行补偿：在FCOS算法中表明，及时是大的步伐(stride)，也可以获取较好的召回率，甚至效果可以优于基于锚框的检测器。
2.  真实边框中的重叠可能会在训练过程中造成难以处理的歧义，这种模糊性导致基于fcn的检测器性能下降：在FCOSzhong ，采用多级预测方法可以有效地解决模糊问题，与基于锚框的模糊检测器相比，基于模糊控制器的模糊检测器具有更好的性能。

前面提到，为了解决真实边框重叠带来的模糊性和低召回率，FCOS采用类似FPN中的多级检测，就是在不同级别的特征层检测不同尺寸的目标。

**_与基于锚框不同的地方_**

-   基于锚框的检测器将不同尺寸的锚框分配到不同级别的特征层
-   FCOS通过直接限定不同特征级别的边界框的回归范围来进行分配

此外，FCOS在不同的特征层之间共享信息，不仅使检测器的参数效率更高，而且提高了检测性能。

### **3.Center-ness**

![](https://pic2.zhimg.com/v2-6300c9570dcb7196aa07a012443345bd_b.jpg)

通过多级预测之后发现FCOS和基于锚框的检测器之间仍然存在着一定的距离，主要原因是距离目标中心较远的位置产生很多低质量的预测边框。

在FCOS中提出了一种简单而有效的策略来抑制这些低质量的预测边界框，而且不引入任何超参数。具体来说，FCOS添加单层分支，与分类分支并行，以预测"Center-ness"位置。

$cenerness^{*}=\sqrt{\frac{\min \left(l^{*}, r^{*}\right)}{\max \left(l^{*}, r^{*}\right)} \times \frac{\min \left(t^{*}, b^{*}\right)}{\max \left(t^{*}, b^{*}\right)}}$

center-ness(可以理解为一种具有度量作用的概念，在这里称之为"中心度")，中心度取值为0,1之间，使用交叉熵损失进行训练。并把损失加入前面提到的损失函数中。测试时，将预测的中心度与相应的分类分数相乘，计算最终得分(用于对检测到的边界框进行排序)。因此，中心度可以降低远离对象中心的边界框的权重。因此，这些低质量边界框很可能被最终的非最大抑制（NMS）过程滤除，从而显着提高了检测性能。

## **实验结果**

**1.召回率**

![](https://pic3.zhimg.com/v2-c08e8187b7dc3a55c9bbe31e7a410afe_b.jpg)

在召回率方便表现接近目前最先进的基于锚框的检测器。

**2\. 有无Center-ness的结果对比**

![](https://pic3.zhimg.com/v2-79e962686343f8731e25cd8c00c33aee_b.jpg)

“None”表示没有使用中心。“中心度”表示使用预测回归向量计算得到的中心度。“中心度”是指利用提出的中心度分支预测的中心度。中心度分支提高了所有指标下的检测性能。

**3.与先进的一阶、二阶检测器效果对比**

![](https://pic2.zhimg.com/v2-c0f9e5b89236ef1a6cc0ad12dbd109b9_b.jpg)

与目前最主流的一些一阶、二阶检测器对比，在检测效率方面FCOS优于Faster R-CNN、YOLO、SSD这些经典算法。

## 开源代码

目前FCOS算法代码已经开源，

FCOS的实现基于Mask R-CNN，因此它的安装与原始的Mask R-CNN相同。安装的主要依赖如下：

-   Pytorch 1.0
-   torchvision
-   cocoapi
-   yacs
-   matplotlib
-   GCC >= 4.9
-   OpenCV(可选)

安装方式有两种：

-   通过pip、conda、编译等一步一步安装
-   通过docker镜像安装

## 参考文献

### 2.1 全卷积一阶段物体检测

我们把第i层的特征图记做Fi，它相对于输入图像的stride为s，输入图像的groundtruth bbox记为{Bi}，Bi=(x0,y0,x1,y1,c)，其中(x0,y0)和(x1,y1)分别为左上角和右下角的坐标，c为物体的类别。对于Fi的每个位置(x,y)，我们可以映射会输入图像中，映射成一个范围(s/2+xs, s/2+ys)，对于基于anchor的物体检测方法，我们把这个位置作为anchor box的中心点，然后去回归目标box相对于这些anchor box的偏差。而我们这里直接在这个位置上回归目标box，换句话说，我们在训练中是把这些位置当成是样本，而不是anchor box，这个和分割是一样。

如果位置(x,y)落入到某个groundtruth box中，而且类别也和groundtruth box的类别一样，那它就是正样本，否则就是负样本，而且c=0（背景）。除了类别标签之外，我们在这个位置上还会回归一个4D的向量，**t**=(l,t,r,b)，其中，l，t，r，b分别是这个位置点到bbox的4个边的距离，如图1（左）所示。如果这个位置同时落入到好几个bbox中，那这种就认为是模糊样本。我们简单的选择一个面积最小的bbox作为它回归的目标。下面，我们会展示一个多level的预测方法，这种模糊样本的数量会大大的减少，这样几乎不会影响检测的性能。这样，如果位置(x,y)和一个bbox Bi相关联起来，那么在训练的时候，我们的回归目标可以这样来表示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGJp257icVjaT4gZxGGLb8hlOAyUn5mZKI6xHdg36m87ic1BGfibXehMcWQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**这里值得注意的是，FCOS可以利用任意多的前景样本来训练这个回归，而基于anchor的方法只选取哪些和groundtruth box的IOU大于一定阈值的anchor作为正样本进行训练。我们认为这也许是FCOS效果比anchor based的模型好的原因之一。**  

**网络的输出** 对于coco的数据集，有80个类，我们需要输出一个80维的分类向量和一个4维的**t**=(l,t,r,b)，分类的时候，我们没有用多分类的方法，而是训练了C个二分类器，参考了RetinaNet，我们主干feature map后面对于分类和回归分别加了4个卷积层，作为两个不同分支。由于回归的目标值永远是正的，我们用exp(x)将输出映射到(0, ∞)。值得注意的是，FCOS的输出要比基于anchor的方法（使用9个anchor）小了9倍。

**损失函数** 定义如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGj7dZ1R2Bg2kj1mAdNruV8jErmX0lHo2qc5ibdyaY09co56hXNvW1K5g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

其中Lcls是focal loss，Lreg是UnitBox中使用的IOU loss，Npos表示正样本的数量，λ用来做loss之间的平衡，文中用的值是1。  

**推理** 推理的时候很直接，我们可以每个位置的类别预测pxy和每个位置的回归预测txy，我们选择p>0.05的作为正样本，将其回归值转化为bbox的预测。

### 2.2 使用FPN进行多level的预测

这里我们解决了FCOS的两个问题：

-   在最后的特征图中，大的stride，比如16，对于anchor based检测器，这样会导致较低的best possible recall（BPR），但是对于FCOS，大的stride不会降低BPR，而且，使用了multi-level FPN来预测的话，还可以进一步提升BPR。
    
-   重叠的物体会导致模糊匹配，这也可以通过multi-level FPN来很好的解决。
    

我们用FPN在不同的level上检测不同尺寸的物体，具体结构如图2，

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGx0oGzVMW5GRBJibHhEEFrM5relmyPmiaRm3t0AKAicb6sicSxKVpA0fn1g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

和基于anchor的方法通过在不同的level上设置不同尺寸的anchor的方式，将不同尺寸的物体分配到不同level的特征图上去检测。我们这里更加直接一点，直接对每个level限制物体尺寸的范围。具体来说，我们首先在每个位置上都计算出目标的l，t，r，b，如果max(l，t，r，b) > mi，或者max(l, t, r, b) < mi-1的话，就将这个位置设置为负样本。这里mi是在第i个level上需要去回归的最大距离。这里，我们将m2,m3,m4,m5,m6,m7设置为0,64,128,256,512和∞。这样一来，不同尺寸的物体就被分配到了不同的level的特征图上去进行检测了，由于大部分overlap的都是不一样的尺寸，所以不会出现模糊匹配的问题。如果还是有某个位置匹配到多个groundtruth的情况，那么我们就匹配面积最小的那个。  

最后，我们对于不同level的特征图，共享同一个检测头，如图2，但是，由于不同的level回归的是不同的尺寸，共享同一个检测头貌似不是很合理，所以我们又做了点修改，将exp(x)修改为exp(six)，加入了一个可训练的尺度参数si，自动的调整exp的输出大小，这个改动对检测性能有小的提升。

### 2.3 FCOS的Center-ness

我们发现，在训练的时候，会出现大量的距离物体中心点很远的低质量的预测框。这会降低模型的性能。我们用了一个简单有效的方法来抑制这种低质量的预测框。我们加了一个分支来预测位置的center-ness，这个center-ness描述了负责检测这个物体的位置到这个物体的中心的归一化的距离，计算方式如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGm2u3wIXWPJTFnccns35eBVVYo2vOuLnW5PHCMxskfRcCwSLMMyQjlw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

用sqrt来减慢center-ness的衰减，center-ness的范围是0~1，用二分类交叉熵来训练。测试的时候，通过它乘上类别得分来对检测出的bbox进行排序，这样，远离中心的那些预测框的分数会减小，这样做nms的时候，就可以去过滤掉这些检测框，显著提升检测性能。  

还有种center-ness的替代方案，就是只使用中心区域作为groundtruth，但是这样需要一个超参数，将这两种方式结合起来，可以得到更好的结果。

## 3. 实验

### 3.1 消融实验

#### 3.1.1 使用FPN进行Multi-level的预测

对于BRP的效果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGQRvnVSqScPianR4Jng6r3Vbd9AYKRQzue4RFZtpmdHDNkqAnD5aMMVQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

对模糊样本的影响：  

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvG25rTzB8eozJcmBhBeHbjf04a85To8Uwj3dUIfjMdEibjAqfEl2Hr9Bg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

#### 3.1.2 是否使用Center-ness  

使用了Center-ness前后的效果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGB8ADKbh1yfWxibUvmzDNpvhKlAWdM4u8vK3X8Pgz8xkFLWAcU1F3wpg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

anchor base的检测器RetinaNet使用了2个阈值来进行正负样本的选择，如果同时使用center-ness和阈值的话，还能提升性能，下面给出了一些额外的优化方法及其效果：  

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGLW04DBPfRj17d8v38AIVMWoPt1sicrTC5XAhWNf1ASRDgvyO6rUFSAQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

#### 3.1.3 和anchor based的检测器的比较  

和RetinaNet的比较见上面的图3。

### 3.2 和其他的检测器的比较

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvG4tt5NYTTHqdQl90MceLeDOdxG1EMeSibNjDH8jiawWqZibrQ3lZlXfU5A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 4. 扩展到RPN上  

用FCOS来代替FPN中的RPN网络的效果：

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/KYSDTmOVZvp2ickCTLAWKiaLofZfqTcVvGBnuUwgEPyGVibIOU5zRicC0ZSBHnyAK3NBvTw7kZ4eHAVI3VOHribfPFQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
___

## 更多我的作品

[Jackpop：PinSage：GCN在商业推荐系统首次成功应用](https://zhuanlan.zhihu.com/p/63214411)

[Jackpop：锚框：Anchor box综述](https://zhuanlan.zhihu.com/p/63024247)