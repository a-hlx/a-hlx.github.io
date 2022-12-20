[详解激活函数（Sigmoid/Tanh/ReLU/Leaky ReLu等） ](https://zhuanlan.zhihu.com/p/427541517)

## 激活函数简述

**激活函数是向神经网络中引入非线性因素，通过激活函数神经网络就可以拟合各种曲线。激活函数主要分为饱和激活函数（Saturated Neurons）和非饱和函数（One-sided Saturations）**。Sigmoid和Tanh是饱和激活函数，而ReLU以及其变种为非饱和激活函数。非饱和激活函数主要有如下优势：

1.非饱和激活函数可以解决梯度消失问题。

2.非饱和激活函数可以加速收敛。

![](https://pic2.zhimg.com/v2-9bede9b4cd7bba5cce65d6d83404681d_b.jpg)

各激活函数图像

## 梯度消失(Vanishing Gradients)

Sigmoid的函数图像和Sigmoid的梯度函数图像分别为(a)、(e)，从图像可以看出，函数两个边缘的梯度约为0，梯度的取值范围为(0,0.25)。求解方程为：

$y=1/(1+e^{-x})$
y=1/(1+e^{-x})

$y^{'}=y(1-y)$
y^{'}=y(1-y)

1\. Sigmoid极容易导致梯度消失问题。饱和神经元会使得梯度消失问题雪上加霜，**假设神经元输入Sigmoid的值特别大或特别小，对应的梯度约等于0，即使从上一步传导来的梯度较大，该神经元权重(w)和偏置(bias)的梯度也会趋近于0，导致参数无法得到有效更新。**

2\. 计算费时。 在神经网络训练中，常常要计算Sigmid的值进行幂计算会导致耗时增加。

3\. Sigmoid函数不是关于原点中心对称的（zero-centered)。

Tanh激活函数解决了原点中心对称问题。

**ReLU解决梯度消失问题**

**ReLU激活函数的提出就是为了解决梯度消失问题。**ReLU的梯度只可以取两个值：0或1，当输入小于0时，梯度为0；当输入大于0时，梯度为1。好处就是：ReLU的梯度的连乘不会收敛到0，连乘的结果也只可以取两个值：0或1 。如果值为1，梯度保持值不变进行前向传播；如果值为0 ,梯度从该位置停止前向传播。

Sigmoid函数是双侧饱和的，即朝着正负两个方向函数值都会饱和；但ReLU函数是单侧饱和的，即只有朝着负方向，函数值才会饱和。严格意义上来说，将ReLU函数值为0的部分称作饱和是不正确的(饱和应该是取值趋近于0)，但效果和饱和是一样的。

假设神经元为检测某种特定特征的开关，高层神经元负责检测高级的/抽象的特征(有着更丰富的语义信息)，例如眼睛或者轮胎；低层神经元负责检测低级的/具象的特征(曲线或者边缘)。当开关处于开启状态，说明在输入范围内检测到了对应的特征，且正值越大代表特征越明显。加入某个神经元负责检测边缘，则正值越大代表边缘区分越明显(sharp)。假设一个负责检测边缘的神经元，激活值为1相对于激活值为0.5来说，检测到的边缘区分地更明显；但激活值-1相对于-0.5来说就没有意义了，因为低于0的激活值都代表没有检测到边缘。**所以用一个常量值0来表示检测不到特征是更为合理的，像ReLU这样单侧饱和的神经元就满足要求。**

**单侧饱和还能使得神经元对于噪声干扰更具鲁棒性**。假设一个双侧都不饱和的神经元，正侧的不饱和导致神经元正值的取值各不相同，这是所希望的，因为正值的大小代表了检测特征信号的强弱。但负值的大小引入了背景噪声或者其他特征信息，这会给后续的神经元带来无用的干扰且可能导致神经元之间的相关性，相关性是容易造成模型病态的。例如检测直线的神经元和检测曲线的神经元可能有负相关性。在负值区域单侧饱和的神经元则不会有上述问题，噪声的程度大小被饱和区域都截断为0,避免了无用信息的干扰。

使用ReLU激活函数在计算上也是高效的。相对于Sigmoid函数梯度的计算，ReLU函数梯度取值只有0或1。且ReLU将负值截断为0 ，为网络引入了稀疏性，进一步提升了计算高效性。

## 神经元死亡

ReLU尽管稀疏性可以提升计算高效性，但同样也可能阻碍训练过程。通常，激活函数的输入值有一偏置项(bias)，假设bias变得太小，以至于输入激活函数的值总是负的，那么反向传播过程经过该处的梯度恒为0,对应的权重和偏置参数此次无法得到更新。如果对于所有的样本输入，**该激活函数的输入都是负的，那么该神经元再也无法学习，称为神经元”死亡“问题。**

**Leaky ReLU可以解决神经元”死亡“问题**

Leaky ReLU的提出就是为了解决神经元”死亡“问题，Leaky ReLU与ReLU很相似，仅在输入小于0的部分有差别，ReLU输入小于0的部分值都为0，而LeakyReLU输入小于0的部分，值为负，且有微小的梯度。函数图像为(d)。

**使用Leaky ReLU的好处就是：在反向传播过程中，对于Leaky ReLU激活函数输入小于零的部分，也可以计算得到梯度(而不是像ReLU一样值为0)，这样就避免了梯度方向锯齿问题。**

α的分布满足均值为0,标准差为1的正态分布，该方法叫做随机Leaky ReLU(Randomized Leaky ReLU)。原论文指出随机Leaky ReLU相比Leaky ReLU能得更好的结果，且给出了参数α的经验值1/5.5(好于0.01)。至于为什么随机Leaky ReLU能取得更好的结果，解释之一就是随机Leaky ReLU小于0部分的随机梯度，为优化方法引入了随机性，这些随机噪声可以帮助参数取值跳出局部最优和鞍点。将α作为了需要学习的参数，该激活函数为PReLU(Parametrized ReLU)。

## ELU(Exponential Linear Unit)

理想的激活函数应满足两个条件：

1.输出的分布是零均值的，可以加快训练速度。

2.激活函数是单侧饱和的，可以更好的收敛。

LeakyReLU和PReLU满足第1个条件，不满足第2个条件；而ReLU满足第2个条件，不满足第1个条件。两个条件都满足的激活函数为ELU(Exponential Linear Unit)，函数图像如图（e）。其表达式如下：

\\begin{equation} f(x)= \\left\\{ \\begin{array}{lr} x,& x>0. \\\\ \\alpha(e^{x}-1), & x\\leq 0.\\\\ \\end{array} \\right. \\end{equation}

## 梯度爆炸

梯度误差是在神经网络训练期间计算的方向和梯度，神经网络以正确的方向和数值更新网络权重。在深度网络或递归神经网络中，梯度误差可能在更新过程中累积，造成非常大的梯度。这反过来会导致网络权重的大量更新，进而导致网络不稳定。在极端情况下，权重值可能变得太大，以至于溢出并导致NaN值现成梯度爆炸现象。

梯度爆炸是通过指数增长发生的，通过在网络层（其值大于1.0）中重复乘以梯度。

**梯度爆炸现象**

比较明显的现象：

1.模型无法“加入”训练数据，比如损失函数很差。

2.模型不稳定，每次更新的损失变化很大。

3.模型损失在训练过程中变为NaN

另外还有一些不太明显的现象：

1.模型权重在训练期间很快变化很大。

2.模型权重在训练过程中变为NaN.

3.训练期间每个节点和层的梯度误差始终高于1.0。

**如何解决梯度爆炸**

1.重现设计神经网络

减少网络层数、减小batch szie、截断。

2.使用LSTM

3.使用梯度裁剪

clipnorm=1.0 clipvalue=0.5

4.使用权重正则

L1 & L2



## 如何选择激活函数

1.除非在二分类问题中，否则请小心使用Sigmoid函数。

2.可以试试Tanh，不过大多数情况下它的效果会比不上 ReLU 和 Maxout。

3.如果你不知道应该使用哪个激活函数， 那么请优先选择ReLU。

4.如果你使用了ReLU， 需要注意一下Dead ReLU问题， 此时你需要仔细选择 Learning rate， 避免出现大的梯度从而导致过多的神经元 “Dead” 。

5.如果发生了Dead ReLU问题， 可以尝试一下leaky ReLU，ELU等ReLU变体， 说不定会有很好效果。

## 常见相关面试题

**1.什么是激活函数，为什么需要激活函数？**

激活函数是在神经网络层间输入与输出之间的一种函数变换，目的是为了加入非线性因素，增强模型的表达能力。

**2.了解那些激活函数以及应用？**回答主要分两类（饱和/非饱和），以及应用场景等。有时候可能特定到具体经典模型，比如LSTM用到Tanh,Transfromer中用到的ReLU,Bert中的GeLU,YOLO的Leaky ReLU等。

**3.梯度消失与梯度爆炸现象与原因以及解决办法？**参看梯度消失与梯度爆炸部分。

**4.ReLU激活函数为什么会出现死神经元，解决办法？**

除上文提到输入为负值时，ReLU的梯度为0造成神经元死亡。还有Learning rate太高导致在训练过程中参数更新太大 。

解决办法主要有：1.优化参数。 2.避免将learning rate设置太大，或者使用Adam等自动调节learning rate的方法。3.更换激活函数。

**5.如何选择激活函数？**参看激活函数选择部分，亦可加入特定模型的使用分析。

参考文献：

\[1\].[How to chose an activation function for your network](https://link.zhihu.com/?target=https%3A//blog.paperspace.com/vanishing-gradients-activation-function/).

\[2\].[ELU](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/1511.07289.pdf).

\[3\].[四月亭：算法面试问题二（激活函数相关）【这些面试题你都会吗】](https://zhuanlan.zhihu.com/p/354013996)

附代码：

```
%matplotlib inline
#import pandas as pd
#from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)
##### 绘制sigmoid图像
fig = plt.figure()
y_sigmoid = 1/(1+np.exp(-x))
ax = fig.add_subplot(321)
ax.plot(x,y_sigmoid,color='blue')
ax.grid()
ax.set_title('(a) Sigmoid')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

##### 绘制Tanh图像
ax = fig.add_subplot(322)
y_tanh = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
ax.plot(x,y_tanh,color='blue')
ax.grid()
ax.set_title('(b) Tanh')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

##### 绘制Relu图像
ax = fig.add_subplot(323)
y_relu = np.array([0*item  if item<0 else item for item in x ])
ax.plot(x,y_relu,color='darkviolet')
ax.grid()
ax.set_title('(c) ReLu')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

##### 绘制Leaky Relu图像
ax = fig.add_subplot(324)
y_relu = np.array([0.2*item  if item<0 else item for item in x ])
ax.plot(x,y_relu,color='darkviolet')
ax.grid()
ax.set_title('(d) Leaky Relu')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

##### 绘制ELU图像
ax = fig.add_subplot(325)
y_elu = np.array([2.0*(np.exp(item)-1)  if item<0 else item for item in x ])
ax.plot(x,y_elu,color='darkviolet')
ax.grid()
ax.set_title('(d) ELU alpha=2.0')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax = fig.add_subplot(326)
y_sigmoid_dev = y_sigmoid*(1-y_sigmoid)
ax.plot(x,y_sigmoid_dev,color='green')
ax.grid()
ax.set_title('(e) Sigmoid Dev')
ax.spines['right'].set_color('none') # 去除右边界线
ax.spines['top'].set_color('none') # 去除上边界线
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.tight_layout()
plt.savefig('Activation.png')
plt.show()
```

## softmax激活函数

[三分钟读懂Softmax函数 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/168562182)

> Softmax是一种激活函数，它可以将一个数值向量归一化为一个概率分布向量，且各个概率之和为1。Softmax可以用来作为神经网络的最后一层，用于多分类问题的输出。Softmax层常常和交叉熵损失函数一起结合使用。

### 从二分类到多分类

对于二分类问题，我们可以使用Sigmod函数（又称Logistic函数）。将$(-\infty, +\infty)$范围内的数值映射成为一个$(0,1)$区间的数值，一个$(0,1)$区间的数值恰好可以用来表示概率。

$g(z)= \frac 1 {1+e^{-z}}$

比如，在互联网广告和推荐系统中，曾广泛使用Sigmod函数来预测某项内容是否有可能被点击。Sigmoid函数输出值越大，说明这项内容被用户点击的可能性越大，越应该将该内容放置到更加醒目的位置。

除了二分类，现实世界往往有其他类型的问题。比如我们想识别手写的阿拉伯数字0-9，这就是一个**多分类**问题，需要从10个数字中选择一个概率最高的作为预测结果。

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212305318.jpeg)

手写体识别数据集mnist

对于多分类问题，一种常用的方法是Softmax函数，它可以预测每个类别的概率。对于阿拉伯数字预测问题，选择预测值最高的类别作为结果即可。Softmax的公式如下，其中$z$是一个向量，$z_i$和$z_j$是其中的一个元素。

$\text{Softmax}(z_{i}) = \frac{\exp(z_i)}{\sum_j \exp(z_j)}$

下图中，我们看到，Softmax将一个$[2.0, 1.0, 0.1]$的向量转化为了$[0.7, 0.2, 0.1]$，而且各项之和为1。

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212305319.jpeg)

Softmax可以将数值向量转换为概率分布

Softmax函数可以将上一层的原始数据进行归一化，转化为一个$(0,1)$之间的数值，这些数值可以被当做概率分布，用来作为多分类的目标预测值。Softmax函数一般作为神经网络的最后一层，接受来自上一层网络的输入值，然后将其转化为概率。

下图为VGG16网络，是一个图像分类网络，原始图像中的数据经过卷积层、池化层、全连接层后，最终经过Softmax层输出成概率。

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212305320.jpeg)

VGG16是一个图像分类网络，Softmax是VGG16的最后一层，Softmax层的前面是全连接层，Softmax层也是整个VGG16神经网络的输出，输出的是多分类的概率分布

实际上，Sigmod函数是Softmax函数的一个特例，Sigmod函数只能用于预测值为0或1的二元分类。

### 指数函数

Softmax函数使用了指数，对于每个输入$z_i$，需要计算$z_i$的指数。在深度学习进行反向传播时，我们经常需要求导，指数函数求导比较方便：$(e^z)' = e^z$。

我们可以用NumPy实现一个简单的Softmax：

```
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)
```

对于下面的输入，可以得到：

```
a = np.asarray([2, 3, 5]) 
softmax(a)
array([0.04201007, 0.1141952 , 0.84379473])
```

如果不使用指数，单纯计算百分比：

```
def percentile(x):
    return x / np.sum(x, axis=0)
```

得到的结果为：

```
percentile(a)
array([0.2, 0.3, 0.5])
```

指数函数在x轴正轴的变化非常明显，斜率越来越大。x轴上一个很小的变化都会导致y轴非常大的变化。相比求和计算百分比的方式：$\frac{z_i}{\sum_j{z_j}}$，指数能把一些数值差距拉大。

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212305321.jpeg)

指数函数

但正因为指数在x轴正轴爆炸式地快速增长，如果$z_i$比较大，$\exp(z_i)$也会非常大，得到的数值可能会溢出。溢出又分为下溢出（Underflow）和上溢出（Overflow）。计算机用一定长度的二进制表示数值，数值又被称为浮点数。当数值过小的时候，被四舍五入为0，这就是下溢出；当数值过大，超出了最大界限，就是上溢出。

比如，仍然用刚才那个NumPy实现的简单的Softmax：

```
b = np.array([20, 300, 5000])
softmax(b)
```

会报错：

```
RuntimeWarning: overflow encountered in exp return np.exp(x) / np.sum(np.exp(x), axis=0)
```

一个简单的办法是，先求得输入向量的最大值，然后所有向量都减去这个最大值：

$$
M = max(z)  \\
$$$$
\text{Softmax}(z_{i}) = \frac{\exp(z_i - M)}{\sum_j \exp(z_j -M)} \\
$$\\text{Softmax}(z\_{i}) = \\frac{\\exp(z\_i - M)}{\\sum\_j \\exp(z\_j -M)} \\\\

**参考资料**

1.  **[https://medium.com/data-science\-bootcamp/understand-the-softmax-function-in-minutes-f3a59641e86d](https://link.zhihu.com/?target=https%3A//medium.com/data-science-bootcamp/understand-the-softmax-function-in-minutes-f3a59641e86d)**
2.  **[https://zhuanlan.zhihu.com/p/105722023](https://zhuanlan.zhihu.com/p/105722023)**
3.  **[https://en.wikipedia.org/wiki/Softmax\_function](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Softmax_function)**
4.  **[http://deanhan.com/2018/07/26/vgg16/](https://link.zhihu.com/?target=http%3A//deanhan.com/2018/07/26/vgg16/)**











