## 摘要

本文主要介绍几个机器学习中常用的损失函数，解释其原理，性能优缺点和适用范围。

[损失函数（Loss Function）](https://zhuanlan.zhihu.com/p/261059231)
___

目录：

1.  什么是损失函数？
2.  为什么要用损失函数？
3.  有哪些损失函数？
	1.  基于距离度量的损失函数
		1.  均方误差损失函数（MSE）
		2.  L2损失函数
		3.  L1损失函数
		4.  Smooth L1损失函数
		5.  huber损失函数
	2.  基于概率分布度量的损失函数
		1.  KL散度函数（相对熵）
		2.  交叉熵损失
		3.  softmax损失函数
		4.  Focal loss
4.  如何选择损失函数？
5.  参考资料

___

## 损失函数介绍

一言以蔽之，损失函数（loss function）就是用来度量模型的预测值f(x)与真实值Y的差异程度的运算函数，它是一个非负实值函数，通常使用L(Y, f(x))来表示，损失函数越小，模型的鲁棒性就越好。

## 损失函数使用原因

损失函数使用主要是在模型的训练阶段，每个批次的训练数据送入模型后，通过前向传播输出预测值，然后损失函数会计算出预测值和真实值之间的差异值，也就是损失值。得到损失值之后，模型通过反向传播去更新各个参数，来降低真实值与预测值之间的损失，使得模型生成的预测值往真实值方向靠拢，从而达到学习的目的。

## 损失函数类型

###  基于距离度量的损失函数

基于距离度量的损失函数通常将输入数据映射到基于距离度量的特征空间上，如欧氏空间、汉明空间等，将映射后的样本看作空间上的点，采用合适的损失函数度量特征空间上样本真实值和模型预测值之间的距离。特征空间上两个点的距离越小，模型的预测性能越好。

#### 均方误差损失函数（MSE）

> 公式： $L(Y|f(x))=\frac{1}{n}\sum_{i=1}^{N}{(Y_{i}-f(x_{i}))^{2}}$

在回归问题中，**均方误差损失函数**用于度量样本点到回归曲线的距离，通过最小化平方损失使样本点可以更好地拟合回归曲线。均方误差损失函数（MSE）的值越小，表示预测模型描述的样本数据具有越好的精确度。由于无参数、计算成本低和具有明确物理意义等优点，MSE已成为一种优秀的距离度量方法。尽管MSE在图像和语音处理方面表现较弱，但它仍是评价信号质量的标准，在回归问题中，MSE常被作为模型的经验损失或算法的性能指标。

代码实现：

```
import numpy as np
# 自定义实现
def MSELoss(x:list,y:list):
    """
    x:list，代表模型预测的一组数据
    y:list，代表真实样本对应的一组数据
    """
    assert len(x)==len(y)
    x=np.array(x)
    y=np.array(y)
    loss=np.sum(np.square(x - y)) / len(x)
    return loss

#计算过程举例
x=[1,2]
y=[0,1]
loss=（（1-0）**2 + （2-1）**2）÷2=（1+1）÷2=1

# Tensorflow2.0版
y_true=tf.convert_to_tensor(y)
y_pred=tf.convert_to_tensor(x)
mse_loss = tf.keras.losses.MSE(y_true, y_pred) # y_true, y_pred都是张量格式

# pytorch版本
y_true=torch.tensor(y)
y_pred=torch.tensor(x)
mse_fc = torch.nn.MSELoss(y_true, y_pred)
mse_loss = mse_fc(x,y)
```

#### L2损失函数

李宏毅：均方差（Mean Squared Error，MSE）损失是机器学习、深度学习回归任务中最常用的一种损失函数，也称为 L2 Loss

> L2损失函数： $L(Y|f(x))=\sqrt{\frac{1}{n}\sum_{i=1}^{N}{(Y_{i}-f(x_{i}))^{2}}}$

L2损失又被称为欧氏距离，是一种常用的距离度量方法，通常用于度量数据点之间的相似度。由于L2损失具有凸性和可微性，且在独立、同分布的高斯噪声情况下，它能提供最大似然估计，使得它成为回归问题、模式识别、图像处理中最常使用的损失函数。

代码实现：

```
import numpy as np
# 自定义实现
def L2Loss(x:list,y:list):
    """
    x:list，代表模型预测的一组数据
    y:list，代表真实样本对应的一组数据
    """
    assert len(x)==len(y)
    x=np.array(x)
    y=np.array(y)
    loss=np.sqrt(np.sum(np.square(x - y)) / len(x))
    return loss
```

#### L1损失函数（MAE）

> L1损失函数： $L(Y|f(x))=\sum_{i=1}^{N}{|Y_{i}-f(x_{i})|}$

L1损失又称为曼哈顿距离，表示残差的绝对值之和。L1损失函数对离群点有很好的鲁棒性，但它在残差为零处却不可导。另一个缺点是更新的梯度始终相同，也就是说，即使很小的损失值，梯度也很大，这样不利于模型的收敛。针对它的收敛问题，一般的解决办法是在优化算法中使用变化的学习率，在损失接近最小值时降低学习率。

代码实现：

```
import numpy as np
# 自定义实现
def L1Loss(x:list,y:list):
    """
    x:list，代表模型预测的一组数据
    y:list，代表真实样本对应的一组数据
    """
    assert len(x)==len(y)
    x=np.array(x)
    y=np.array(y)
    loss=np.sum(np.abs(x - y)) / len(x)
    return loss

```

#### Smooth L1损失函数

> 公式： $$
> L(Y|f(x)) =  \begin{cases}     \frac{1}{2}(Y-f(x))^{2} & \text{  |Y-f(x)|<1}  \\    |Y-f(x)|-\frac{1}{2}       & \text{ |Y-f(x)|>=1}  \end{cases}\\
> $$

Smooth L1损失是由Girshick R在Fast R-CNN中提出的，主要用在目标检测中防止梯度爆炸。

代码实现：

```
def Smooth_L1(x,y):
    assert len(x)==len(y)
    loss=0
    for i_x,i_y in zip(x,y):
        tmp = abs(i_y-i_x)
        if tmp<1:
            loss+=0.5*(tmp**2)
        else:
            loss+=tmp-0.5
    return loss
```

#### huber损失函数

> 公式： $$
> L(Y|f(x)) =  \begin{cases}     \frac{1}{2}(Y-f(x))^{2} & \text{  |Y-f(x)|}  <= \delta \\    \delta|Y-f(x)|-\frac{1}{2}    \delta^{2}  & \text{ |Y-f(x)|} > \delta \end{cases}\\
> $$

huber损失是平方损失和绝对损失的综合，它克服了平方损失和绝对损失的缺点，不仅使损失函数具有连续的导数，而且利用MSE梯度随误差减小的特性，可取得更精确的最小值。尽管huber损失对异常点具有更好的鲁棒性，但是，它不仅引入了额外的参数，而且选择合适的参数比较困难，这也增加了训练和调试的工作量。

代码实现：

```
delta=1.0  # 先定义超参数

def huber_loss(x,y):
    assert len(x)==len(y)
    loss=0
    for i_x,i_y in zip(x,y):
        tmp = abs(i_y-i_x)
        if tmp<=delta:
            loss+=0.5*(tmp**2)
        else:
            loss+=tmp*delta-0.5*delta**2
    return loss
```

### 基于概率分布度量的损失函数

基于概率分布度量的损失函数是将样本间的相似性转化为随机事件出现的可能性，即通过度量样本的真实分布与它估计的分布之间的距离，判断两者的相似度，一般用于涉及概率分布或预测类别出现的概率的应用问题中，在分类问题中尤为常用。

#### KL散度函数（相对熵）

> 公式： $L(Y|f(x))=\sum_{i=1}^{n}{Y_{i}\times log(\frac{Y_{i}}{f(x_{i})})}$

公式中Y代表真实值，f(x)代表预测值。

KL散度（ Kullback-Leibler divergence）也被称为相对熵，是一种非对称度量方法，常用于度量两个概率分布之间的距离。KL散度也可以衡量两个随机分布之间的距离，两个随机分布的相似度越高的，它们的KL散度越小，当两个随机分布的差别增大时，它们的KL散度也会增大，因此KL散度可以用于比较文本标签或图像的相似性。基于KL散度的演化损失函数有JS散度函数。JS散度也称JS距离，用于衡量两个概率分布之间的相似度，它是基于KL散度的一种变形，消除了KL散度非对称的问题，与KL散度相比，它使得相似度判别更加准确。

相对熵是恒大于等于0的。当且仅当两分布相同时，相对熵等于0。

代码实现：

```
def kl_loss(y_true:list,y_pred:list):
    """
    y_true,y_pred，分别是两个概率分布
    比如：px=[0.1,0.2,0.8]
          py=[0.3,0.3,0.4]
    """
    assert len(y_true)==len(y_pred)
    KL=0
    for y,fx in zip(y_true,y_pred):
        KL+=y*np.log(y/fx)
    return KL
```

#### 交叉熵损失

> 公式： $L(Y|f(x))=-\sum_{i=1}^{N}{Y_{i}log f(x_{i})}$
>
L(Y|f(x))=-\\sum\_{i=1}^{N}{Y\_{i}log f(x\_{i})}

交叉熵是信息论中的一个概念，最初用于估算平均编码长度，引入机器学习后，用于评估当前训练得到的概率分布与真实分布的差异情况。为了使神经网络的每一层输出从线性组合转为非线性逼近，以提高模型的预测精度，在以交叉熵为损失函数的神经网络模型中一般选用tanh、sigmoid、softmax或ReLU作为激活函数。

交叉熵损失函数刻画了实际输出概率与期望输出概率之间的相似度，也就是交叉熵的值越小，两个概率分布就越接近，特别是在正负样本不均衡的分类问题中，常用交叉熵作为损失函数。目前，交叉熵损失函数是卷积神经网络中最常使用的分类损失函数，它可以有效避免梯度消散。在二分类情况下也叫做对数损失函数。

代码实现：

```
def CrossEntropy_loss(y_true:list,y_pred:list):
    """
    y_true,y_pred，分别是两个概率分布
    比如：px=[0.1,0.2,0.8]
          py=[0.3,0.3,0.4]
    """
    assert len(y_true)==len(y_pred)
    loss=0
    for y,fx in zip(y_true,y_pred):
        loss+=-y * np.log(fx)
    return loss
```

当正负样本不均衡的时候，通常会在交叉熵损失函数类别前面加个参数α

> $$
> CE =  \begin{cases}     -\alpha log(p) & \text{   y = 1}  \\    -(1-\alpha )log(1-p)       & \text{ y = 0}  \end{cases}\\
> $$CE = \\begin{cases} -\\alpha log(p) & \\text{ y = 1} \\\\ -(1-\\alpha )log(1-p) & \\text{ y = 0} \\end{cases}\\\\

#### softmax损失函数

> 公式： $L(Y|f(x))=-\frac{1}{n}\sum_{i=1}^{n}{log\frac{e^{f_{Y_{i}}}}{\sum_{j=1}^{c}{e^{f_{j}}}}}$
> 
> L(Y|f(x))=-\\frac{1}{n}\\sum\_{i=1}^{n}{log\\frac{e^{f\_{Y\_{i}}}}{\\sum\_{j=1}^{c}{e^{f\_{j}}}}}

从标准形式上看，softmax损失函数应归到对数损失的范畴，在监督学习中，由于它被广泛使用，所以单独形成一个类别。softmax损失函数本质上是逻辑回归模型在多分类任务上的一种延伸，常作为CNN模型的损失函数。softmax损失函数的本质是将一个k维的任意实数向量x映射成另一个k维的实数向量，其中，输出向量中的每个元素的取值范围都是(0,1)，即softmax损失函数输出每个类别的预测概率。由于softmax损失函数具有类间可分性，被广泛用于分类、分割、人脸识别、图像自动标注和人脸验证等问题中，其特点是类间距离的优化效果非常好，但类内距离的优化效果比较差。

softmax损失函数具有类间可分性，在多分类和图像标注问题中，常用它解决特征分离问题。在基于卷积神经网络的分类问题中，一般使用softmax损失函数作为损失函数，但是softmax损失函数学习到的特征不具有足够的区分性，因此它常与对比损失或中心损失组合使用，以增强区分能力。

代码实现：

```
def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    s = x_exp / x_sum
    return s

# Tensorflow2.0版
softmax_fc = tf.keras.activations.softmax(x)
# pytorch版
softmax_fc = torch.nn.Softmax()
output = softmax_fc(x)
```

#### Focal loss

focal loss的引入主要是为了解决难易样本不均衡的问题，注意有区别于正负样本不均衡的问题。难易样本分为四个类型：

|  | 难 | 易 |
| --- | --- | --- |
| 正 | 正难 | 正易 |
| 负 | 负难 | 负易 |

易分样本虽然损失很低，但是数量太多，对模型的效果提升贡献很小，模型应该重点关注那些难分样本，因此需要把置信度高的损失再降低一些

> $$
> FE =  \begin{cases}     -\alpha(1-p)^{\gamma} log(p) & \text{   y = 1}  \\    -(1-\alpha )p^{\gamma} log(1-p)       & \text{ y = 0}  \end{cases}\\
> $$FE = \\begin{cases} -\\alpha(1-p)^{\\gamma} log(p) & \\text{ y = 1} \\\\ -(1-\\alpha )p^{\\gamma} log(1-p) & \\text{ y = 0} \\end{cases}\\\\

## 选择损失函数

通常情况下，损失函数的选取应从以下方面考虑：

（1） 选择最能表达数据的主要特征来构建基于距离或基于概率分布度量的特征空间。

（2）选择合理的特征归一化方法，使特征向量转换后仍能保持原来数据的核心内容。

（3）选取合理的损失函数，在实验的基础上，依据损失不断调整模型的参数，使其尽可能实现类别区分。

（4）合理组合不同的损失函数，发挥每个损失函数的优点，使它们能更好地度量样本间的相似性。

（5）将数据的主要特征嵌入损失函数，提升基于特定任务的模型预测精确度。

## 参考资料：

\[1\] [监督学习中的损失函数及应用研究](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s%3Fsubscene%3D23%26__biz%3DMzAxOTQ2NzUxOQ%3D%3D%26mid%3D2651912913%26idx%3D1%26sn%3D68f62cb548b35ec93f18027458352434%26chksm%3D8022c741b7554e57616ac8dcd80a11acd7a8a6ada181f4584c602c9f242815f5863ed96b4529%26scene%3D7%26key%3D9c1744d1bffeab4b0c8d19d08eff803bc5bf556e7dad290931316859107869eae11c8d2ef08d1c445c32f9564b88b15a7ddefa9ecba47e9f30595d3194cb93202f018216f272734d0502965e5172c528b84d6f7ee4a2970563bd1594a1ee84cb78bedc97a8d73b1f2c1c8b796374470272fd4c44a5a5badebefe79f797dd9006%26ascene%3D0%26uin%3DNzY2MzMyNDAx%26devicetype%3DWindows%2B10%2Bx64%26version%3D62090538%26lang%3Dzh_CN%26exportkey%3DAbDFP%252Fy90lQvupKLsin%252BqIY%253D%26pass_ticket%3DxXJHSvXALrdXBNLifG37ggdjbeqxXtSOQYVggNqQRRey1Vm1lBPWCAlvlwRUGwZW%26wx_header%3D0)

\[2\] [邓建国, 张素兰, 张继福, 荀亚玲, 刘爱琴.监督学习中的损失函数及应用研究. 大数据\[J\], 2020, 6(1）：60-80](https://link.zhihu.com/?target=http%3A//gb.oversea.cnki.net/KCMS/detail/detail.aspx%3Ffilename%3DDSJU202001006%26dbcode%3DCJFD%26dbname%3DCJFDTEMP)