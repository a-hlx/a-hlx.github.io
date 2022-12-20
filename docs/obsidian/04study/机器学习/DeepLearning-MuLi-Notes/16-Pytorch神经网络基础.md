## Pytorch神经网络基础

### 层和块

在之前的内容中，我们认识了一些神经网络，比如：线性回归，Softmax回归，多层感知机；他们有的是整个模型，有的是一层神经网络，有的甚至只是一个单元，他们的功能以及复杂程度也各不相同，但他们都有着如下三个特征：

* 接受一些输入
* 产生对应的输出
* 由一组可调整参数描述

对于一些复杂的网络，研究讨论比层大但比整个模型小的部分很有意义，因为复杂的网络中经常有重复出现的部分，每个部分也常常有自己的功能。考虑到上面的三个特征，这就使得我们思考是否可以对这些部分进行一个抽象，这就得到了块的概念：块指单个层，多个层组成的部分，或者整个模型本身。使用块对整个模型进行描述就简便许多，这一过程是递归的，块的内部还可以划分为多个块，直至满足需要为止。

从编程的角度来看，块由_类_（class）表示。 它的任何子类都必须定义一个将其输入转换为输出的前向传播函数， 并且必须存储任何必需的参数。 注意，有些块不需要任何参数。 最后，为了计算梯度，块必须具有反向传播函数。 在定义我们自己的块时，由于自动微分（在 [2.5节](https://zh-v2.d2l.ai/chapter_preliminaries/autograd.html#sec-autograd) 中引入） 提供了一些后端实现，我们只需要考虑前向传播函数和必需的参数。

#### 自定义块

1.  将输入数据作为其前向传播函数的参数。
    
2.  通过前向传播函数来生成输出。请注意，输出的形状可能与输入的形状不同。例如，我们上面模型中的第一个全连接的层接收一个20维的输入，但是返回一个维度为256的输出。
    
3.  计算其输出关于输入的梯度，可通过其反向传播函数进行访问。通常这是自动发生的。
    
4.  存储和访问前向传播计算所需的参数。
    
5.  根据需要初始化模型参数。

PyTorch帮我们实现了块的大部分所需功能，包括自动求导，我们只需从nn.Module继承并改写其中的一部分就能得到我们需要的块以及模型，具体做法和细节见代码中的注释

### 参数管理

在选择了架构并设置了超参数后，我们就进入了训练阶段。此时，我们的目标是找到使损失函数最小化的模型参数值。经过训练后，我们将需要使用这些参数来做出未来的预测。此外，有时我们希望提取参数，以便在其他环境中复用它们，将模型保存下来，以便它可以在其他软件中执行，或者为了获得科学的理解而进行检查。

此部分主要为代码实现，笔记见代码中的注释

#### 操作

```python
import torch
from torch import nn

net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
X = torch.rand(size=(2, 4))
net(X)
```

##### 参数访问

```python
print(net[2].state_dict())
```

```python
print(type(net[2].bias))
print(net[2].bias)
print(net[2].bias.data)

net[2].weight.grad == None
```

##### 一次性访问所有参数

```python
print(*[(name, param.shape) for name, param in net[0].named_parameters()])
print(*[(name, param.shape) for name, param in net.named_parameters()])

net.state_dict()['2.bias'].data
```



### 延后初始化

有时在建立网络时，我们不会指定网络的输入输出维度，也就不能确定网络的参数形状，深度学习框架支持延后初始化，即当第一次将数据传入模型时自动的得到所有的维度，然后初始化所有的参数。

PyTorch也支持这一点，比如nn.LazyLinear，但本门课程中并未介绍。

### 自定义层

深度学习成功背后的一个因素是神经网络的灵活性：我们可以用创造性的方式组合不同的层，从而设计出适用于各种任务的架构。例如，研究人员发明了专门用于处理图像、文本、序列数据和执行动态规划的层。同样的，对于层而言，深度学习框架并不能满足我们所有的需求，然而，层本身也具有极大的灵活性，我们可以自定义想要的层。

此部分主要为代码实现，笔记见代码中的注释

### 读写文件

到目前为止，我们讨论了如何处理数据，以及如何构建、训练和测试深度学习模型。然而，有时我们希望保存训练的模型，以备将来在各种环境中使用（比如在部署中进行预测）。此外，当运行一个耗时较长的训练过程时，最佳的做法是定期保存中间结果，以确保在服务器电源被不小心断掉时，我们不会损失几天的计算结果。

#### 加载和保存张量

```python
import torch
from torch import nn
from torch.nn import functional as F

x = torch.arange(4)
torch.save(x, 'x-file')

x2 = torch.load('x-file')

y = torch.zeros(4)
torch.save([x, y],'x-files')
x2, y2 = torch.load('x-files')

mydict = {'x': x, 'y': y}
torch.save(mydict, 'mydict')
mydict2 = torch.load('mydict')
```

#### 加载和保存模型参数

保存模型的参数而不是保存整个模型。

```python
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        return self.output(F.relu(self.hidden(x)))

net = MLP()
X = torch.randn(size=(2, 20))
Y = net(X)
```

```python
torch.save(net.state_dict(), 'mlp.params')

clone = MLP()
clone.load_state_dict(torch.load('mlp.params'))
clone.eval()
```

