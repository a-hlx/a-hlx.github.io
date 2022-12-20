# 09-softmax回归

### 本节目录：
- [09-softmax回归](#09-softmax回归)
    - [本节目录：](#本节目录)
    - [1.回归VS分类：](#1回归vs分类)
      - [1.1 从回归到多类分类：](#11-从回归到多类分类)
        - [回归：](#回归)
        - [分类：](#分类)
        - [均方损失：](#均方损失)
        - [无校验比例](#无校验比例)
        - [校验比例](#校验比例)
      - [1.2 Softmax和交叉熵损失](#12-softmax和交叉熵损失)
    - [2.损失函数](#2损失函数)
      - [2.1 L2 Loss](#21-l2-loss)
      - [2.2 L1 Loss](#22-l1-loss)
      - [2.3Huber's Robust Loss](#23hubers-robust-loss)
    - [3.图片分类数据集](#3图片分类数据集)
      - [3.1 Fashion-MNIST数据集：](#31-fashion-mnist数据集)
    - [4.从零实现softmax回归](#4从零实现softmax回归)
      - [softmax:](#softmax)
    - [5.softmax的简洁实现](#5softmax的简洁实现)
    - [6.softmax回归Q&A](#6softmax回归qa)

### 1.回归VS分类：

- 回归估计一个连续值
- 分类预测一个离散类别
MNIST:手写数字识别（10类）
ImageNet:自然物体分类（1000类）

#### 1.1 从回归到多类分类：

##### 回归：

- 单连续数值输出
- 自然区间R
- 跟真实值的区别作为损失

##### 分类：

- 通常多个输出

- 输出i是预测为第i类的置信度

###### 网络架构
我们需要一个有**多个输出**的模型，每个类别对应一个输出。 为了解决线性模型的分类问题，我们需要和输出一样多的_仿射函数_（affine function）。 每个输出对应于它自己的仿射函数。 在我们的例子中，由于我们有4个特征和3个可能的输出类别， 我们将需要12个标量来表示权重（带下标的w）， 3个标量来表示偏置（带下标的b）。 下面我们为每个输入计算三个_未规范化的预测_（logit）：o1、o2和o3

$o1=x1w11+x2w12+x3w13+x4w14+b1$
$o2=x1w21+x2w22+x3w23+x4w24+b2$
$o3=x1w31+x2w32+x3w33+x4w34+b3$

softmax回归的输出层也是全连接层

![](https://zh-v2.d2l.ai/_images/softmaxreg.svg)


###### softmax运算

输出  $hat(y)_{j}$  可以视为属于类j的概率， 然后选择具有最大输出值的类别argmaxjyj作为我们的预测。 例如，如果y^1、y^2和y^3分别为0.1、0.8和0.1， 那么我们预测的类别是2，在我们的例子中代表“鸡”。

##### 均方损失：

- 对类别进行一位有效编码
  $y=[y_{1},y_{2},...,y_{n}]^{T}$
  
  $y_{i}=\begin{cases} 1&i=y\\ 2&otherwise \end{cases}$
  
- 使用均方损失训练

- 最大值为预测

$hat{y}=\underset {i}{argmax}\quad o^{i}$

##### 无校验比例

- 对类别进行一位有效编码

- 最大值为预测

$hat{y}=\underset {i}{argmax}\quad o^{i}$
  
- 需要更置信的识别正确类（大余量）

$o_y-o_i\geq\Delta(y,i)$

##### 校验比例

- 输出匹配概率（非负，和为1）

$hat{y}=softmax(o)$

$hat{y_i}=\frac{exp(o_i)}{\sum_{k} exp(o_k)}$

- 概率y和$\hat{y}$的区别作为损失

#### 1.2 Softmax和交叉熵损失

- 交叉熵用来衡量两个概率的区别$H(p,q)=\sum_{i} -p_{i}log(q_i)$

- 将它作为损失

$l(y,\hat{y})=-\sum_{i}y_{i}log\hat{y_{i}}=-log\hat{y_y}$
  
- 其梯度是真实概率和预测概率的区别
 $partial_{o_{i}}l(y,\hat{y})=softmax(o)_{i}-y_{i}$

> Softmax回归是一个多类分类模型
>
> 使用Softmax操作子得到每个类的预测置信度
>
> 使用交叉熵来衡量和预测标号的区别

### 2.损失函数

#### 2.1 L2 Loss

![[../ML储备/损失函数Loss Function#均方误差损失函数（MSE）]]

![[../ML储备/损失函数Loss Function#L2损失函数]]

> 梯度会随着结果逼近而下降

#### 2.2 L1 Loss

![[../ML储备/损失函数Loss Function#L1损失函数（MAE）]]

> 梯度保持不变，但在0处梯度随机

#### 2.3Huber's Robust Loss

![[../ML储备/损失函数Loss Function#huber损失函数]]

### 3.图片分类数据集

#### 3.1 Fashion-MNIST数据集：

- 读取数据集

  ```python
  trans=transforms.ToTensor()
  mnist_train=torchvision.datasets.FashionMNIST(root="../data",train=True,                                              transform=trans,download=True)
  mnist_test=torchvision.datasets.FashionMNIST(root="../data",train=False,                                             transform=trans,download=True)
  ```

- 数据集内图片大小

  ```python
  mnist_train[0][0].shape
  torch.Size([1, 28, 28])
  ```

  表示图片为单通道（黑白）的28X28的图片

- 显示数据集图像

  ```
  X,y = next(iter(data.DataLoader(mnist_train,batch_size=18)))
  show_images(X.reshape(18,28,28),2,9,titles=get_fashion_mnist_labels(y))
  ```

### 4.从零实现softmax回归

#### softmax:

$$
softmax(X)_{ij}=\frac{exp(X_{ij})}{\sum_{k} exp(X_{ik})}
$$

```python
def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1, keepdim=True)
    return X_exp / partition
```

##### 1. 初始化模型参数
将图像展平，每个图像看做长度为784的向量，因为数据集有十个类别，所以网络输出维度为10。以此设定参数大小并初始化：

   ```python
   num_inputs = 784
   num_outputs = 10
   
   W = torch.normal(0, 0.01, size=(num_inputs, num_outputs), requires_grad=True)
   b = torch.zeros(num_outputs, requires_grad=True)
   ```

2. 实现softmax回归模型：

下面的代码定义了输入如何通过网络映射到输出。 注意，将数据传递到模型之前，我们使用`reshape`函数将每张原始图像展平为向量

   ```python
   def net(X):
       return softmax(torch.matmul(X.reshape((-1, W.shape[0])), W) + b)
   ```

3. 实现交叉熵损失函数：

   ```python
   def cross_entropy(y_hat, y):
       return - torch.log(y_hat[range(len(y_hat)), y])
   ```

4. 计算正确率：

给定预测概率分布`y_hat`，当我们必须输出硬预测（hard prediction）时， 我们通常选择预测概率最高的类。

分类精度即正确预测数量与总预测数量之比。

 首先，如果`y_hat`是矩阵，那么假定第二个维度存储每个类的预测分数。 我们使用`argmax`获得每行中最大元素的索引来获得预测类别。 然后我们将预测类别与真实`y`元素进行比较。 由于等式运算符“= =”对数据类型很敏感， 因此我们将`y_hat`的数据类型转换为与`y`的数据类型一致。 结果是一个包含0（错）和1（对）的张量。 最后，我们求和会得到正确预测的数量。
 

   ```python
   def accuracy(y_hat, y):  
       """计算预测正确的数量"""
       if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
           y_hat = y_hat.argmax(axis=1)
       cmp = y_hat.type(y.dtype) == y
       return float(cmp.type(y.dtype).sum())
   
   ```

5. 评估net精度

   ```python
   def evaluate_accuracy(net, data_iter):  
       """计算在指定数据集上模型的精度"""
       if isinstance(net, torch.nn.Module):
           net.eval()
       metric = Accumulator(2)
       with torch.no_grad():
           for X, y in data_iter:
               metric.add(accuracy(net(X), y), y.numel())
       return metric[0] / metric[1]
   ```

这里定义一个实用程序类`Accumulator`，用于对多个变量进行累加。 在上面的`evaluate_accuracy`函数中， 我们在`Accumulator`实例中创建了2个变量， 分别用于存储正确预测的数量和预测的总数量。 当我们遍历数据集时，两者都将随着时间的推移而累加。

   ```python
   class Accumulator:  
       """在n个变量上累加"""
       def __init__(self, n):
           self.data = [0.0] * n
   
       def add(self, *args):
           self.data = [a + float(b) for a, b in zip(self.data, args)]
   
       def reset(self):
           self.data = [0.0] * len(self.data)
   
       def __getitem__(self, idx):
           return self.data[idx]
   ```

6. 定义训练模型：

首先，我们定义一个函数来训练一个迭代周期。 请注意，`updater`是更新模型参数的常用函数，它接受批量大小作为参数。 它可以是`d2l.sgd`函数，也可以是框架的内置优化函数。

```python
def train_epoch_ch3(net, train_iter, loss, updater):  #@save
    """训练模型一个迭代周期（定义见第3章）"""
    # 将模型设置为训练模式
    if isinstance(net, torch.nn.Module):
        net.train()
    # 训练损失总和、训练准确度总和、样本数
    metric = Accumulator(3)
    for X, y in train_iter:
        # 计算梯度并更新参数
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # 使用PyTorch内置的优化器和损失函数
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            # 使用定制的优化器和损失函数
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    # 返回训练损失和训练精度
    return metric[0] / metric[2], metric[1] / metric[2]
```
定义一个在动画中绘制数据的实用程序类`Animator`， 它能够简化本书其余部分的代码。

```python
class Animator:  #@save
    """在动画中绘制数据"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # 增量地绘制多条线
        if legend is None:
            legend = []
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用lambda函数捕获参数
        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        # 向图表中添加多个数据点
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)
```

实现一个训练函数， 它会在`train_iter`访问到的训练数据集上训练一个模型`net`。 该训练函数将会运行多个迭代周期（由`num_epochs`指定）。 在每个迭代周期结束时，利用`test_iter`访问到的测试数据集对模型进行评估。 我们将利用`Animator`类来可视化训练进度。

   ```python
   def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):  
       """训练模型（定义见第3章）"""
       animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                           legend=['train loss', 'train acc', 'test acc'])
       for epoch in range(num_epochs):
           train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
           test_acc = evaluate_accuracy(net, test_iter)
           animator.add(epoch + 1, train_metrics + (test_acc,))
       train_loss, train_acc = train_metrics
       assert train_loss < 0.5, train_loss
       assert train_acc <= 1 and train_acc > 0.7, train_acc
       assert test_acc <= 1 and test_acc > 0.7, test_acc
   ```

小批量随机梯度下降来优化模型的损失函数，设置学习率为0.1。

```python
lr = 0.1

def updater(batch_size):
    return d2l.sgd([W, b], lr, batch_size)
```

现在，我们训练模型10个迭代周期。 请注意，迭代周期（`num_epochs`）和学习率（`lr`）都是可调节的超参数。 通过更改它们的值，我们可以提高模型的分类精度。

```python
num_epochs = 10
train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, updater)
```

7. 预测：

   ```python
   def predict_ch3(net, test_iter, n=6):  
       """预测标签（定义见第3章）"""
       for X, y in test_iter:
           break
       trues = d2l.get_fashion_mnist_labels(y)
       preds = d2l.get_fashion_mnist_labels(net(X).argmax(axis=1))
       titles = [true +'\n' + pred for true, pred in zip(trues, preds)]
       d2l.show_images(
           X[0:n].reshape((n, 28, 28)), 1, n, titles=titles[0:n])
   
   predict_ch3(net, test_iter)
   ```

### 5.softmax的简洁实现

使用Fashion-MNIST数据集，并保持批量大小为256。

在`Sequential`中添加一个带有10个输出的全连接层。 同样，在这里`Sequential`并不是必要的， 但它是实现深度模型的基础。 我们仍然以均值0和标准差0.01随机初始化权重。

> 调用torch内的网络层

```python
import torch
from torch import nn
from d2l import torch as d2l
batch_size=256
train_iter,test_iter=d2l.load_data_fashion_mnist(batch_size)
# PyTorch不会隐式地调整输入的形状。因此，
# 我们在线性层前定义了展平层（flatten），来调整网络输入的形状

net=nn.Sequential(nn.Flatten(),nn.Linear(784,10))

def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight,std=0.01)

net.apply(init_weights)


loss=nn.CrossEntropyLoss()


# 优化算法,使用学习率为0.1的小批量随机梯度下降作为优化算法。
# 与线性回归例子中的相同，这说明了优化器的普适性。
trainer=torch.optim.SGD(net.parameters(),lr=0.1)


num_epochs=10
d2l.train_ch3(net,train_iter,test_iter,loss,num_epochs,trainer)
```

### 6.softmax回归Q&A

**Q1:softlabel训练策略以及为什么有效？**

> softmax用指数很难逼近1，softlabel将正例和负例分别标记为0.9和0.1使结果逼近变得可能，这是一个常用的小技巧。

##### Q2:softmax回归和logistic回归？

> logistic回归为二分类问题，是softmax回归的特例

##### Q3:为什么使用交叉熵，而不用相对熵，互信息熵等其他基于信息量的度量？

> 实际上使用哪一种熵的效果区别不大，所以哪种简单就用哪种

##### Q4:![](http://latex.codecogs.com/gif.latex?\\y*log\hat{y})   为什么我们只关心正确类，而不关心不正确的类呢？

> 并不是不关心，而是不正确的的类标号为零，所以算式中不体现，如果使用softlabel策略，就会体现出不正确的类。

##### Q5:似然函数曲线是怎么得出来的？有什么参考意义？

> 最小化损失函数也意味着最大化似然函数，似然函数表示统计概率和模型的拟合程度。

##### Q6:在多次迭代之后欧如果测试精度出现上升后再下降是过拟合了吗？可以提前终止吗？

> 很有可能是过拟合，可以继续训练来观察是否持续下降

##### Q7:cnn网络主要学习到的是纹理还是轮廓还是所有内容的综合？

> 目前认为主要学习到的是纹理信息

##### Q8:softmax可解释吗？

> 单纯softmax是可解释的，可以在统计书籍中找到相关的解释。
