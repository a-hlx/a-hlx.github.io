[Mitchell, 1997]给出了一个更形式化的定义：假设 用 P (performance)来评估计算机程序在某任务类T(task) 上的性能,若一个程序通过利用经验E (experience)在 T 中任务上获得了性能改善，则我们就说关于T 和尸，该程序对E 进行了学习.

根据训练数据是否拥有标记信息，学习任务可大致划分为两大类：
监督学习“(supervised learning)和 “无 监 督 学 习 "(unsupervised learning)

Classification分类和Regression回归是前者的代表,而聚类clustering 和关联分析assocoation analysis则是后者的代表。

自监督学习 (Self-Supervised Learning)是一种**介于无监督和监督学习之间的一种新范式，旨在减少对大量带注释数据的挑战性需求**。 它通过定义无注释 (annotation-free)的前置任务 (pretext task)，为特征学习提供代理监督信号。

# 资料

[【李宏毅2021机器学习深度学习】作业讲解 & 笔记收藏 & 课程主页 CSDN博客_李宏毅深度学习作业](https://blog.csdn.net/weixin_43154149/article/details/121800840)


# The types of Function

1、Regression回归: The  function outputs a scalar 
输出一个数量
2、Classification分类 :Given options(classes),the funciton outputs the correct one.
输出一个正确的选项
3、Structured Learning(结构化学习)：Create something with structure(输出结构化的东西，如image  ,ducument)

# process

Step 1: function with unknown
Step 2: define loss from training data
Step 3: optimization

# 激活函数

[[../ML储备/激活函数Activation functions]]

# cost function
[[../ML储备/成本函数Cost Function]]

[[../ML储备/损失函数Loss Function]]



# colab and jupyter

[[Library/Google Colab Tutorial]]

https://colab.research.google.com/

[The Jupyter Notebook — Jupyter Notebook 6.4.12 documentation (jupyter-notebook.readthedocs.io)](https://jupyter-notebook.readthedocs.io/en/stable/index.html)

[[Library/Jupyter Notebook]]

# CNN
Convolutional  Neural Network
[[../DeepLearning_LHY21_Notes-master/09_CNN]]

卷积核的channel与输入特征层的channel相同。
输出的特征层矩阵channel与卷积核的个数相同。

**感受野**（receptive field）
深度（depth），步长（stride）和零填充（zero-padding）
有不同补值（padding）方式
==Parameter Sharing权值共享==

滤波器==Filter==就是卷积核

 **Receptive Field 加上 Parameter Sharing,就是 ==Convolutional Layer

 ==Feature Map==

 Pooling（Maxpooling下采样，AveragePooling）：对特征层进行稀疏处理，减少数据运算量。池化核
**实际操作往往是 Convolution 跟 Pooling 交替使用**,就是你可能做几次 Convolution,做一次 Pooling

池化无训练参数；只改变特征矩阵的长宽，不改变channel；一般池化核大小pool size与stride相同。pool默认S应该是同K stride: the stride of the window. Default value is :attr:`kernel_size`

把 Pooling 的 Output 做一件事情,叫做 Flatten,Flatten 的意思就是,把这个影像裡面啊,本来排成矩阵的样子的东西拉直,把所有的数值拉直变成一个向量,再把这个向量,丢进 Fully Connected 的 Layer 裡面

在做影像辨识的时候,往往都要做 ==Data Augmentation==,所谓 Data Augmentation 的意思就是说,你把你的训练资料,每张图片都裡面截一小块出来放大,让 CNN 有看过不同大小的 Pattern,然后把图片旋转,让它有看过说,某一个物件旋转以后长什麼样子,CNN 才会做到好的结果




ground truth
ground-truth bounding box
predicted box