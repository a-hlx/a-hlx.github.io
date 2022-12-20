_**Cost Function**_

Cost Function叫做损失函数，是用来衡量hypothesis（预测值）正确程度的函数。通常，损失函数会采用根据输入X所得的Hypothesis与真实目标值y的平均差值。
[Cost Function ](https://zhuanlan.zhihu.com/p/120350856)

___

**"Squared error function"（平方误差函数） or "Mean square error"**

常见的损失函数，均方误差：$J(\theta_0,\theta_1)=\frac{1}{2m}\Sigma_{i=1}^m(h_\theta(x^i)-y^i)^2$J

(此处只代表只存在一个特征的情况，所以参数为 $\theta_0 , \theta_1$）

这里，**1/2是为了方便计算和梯度下降**。

___

**怎么使用损失函数：**

我们的目标就是为了让预测值尽可能接近真实值。所以相应的，当预测值hypothesis越接近真实值y，则误差越小，学习的效果越好。我们要做的是就是要让损失函数最小化。

$Minimize \theta_0\theta_1:\frac{1}{2m}\Sigma_{i}^m(h_\theta(x^i)-y^i)^2$

其中 hypothesis 即 $h_\theta(x^i)=\theta^TX^i=\theta_0+\theta_1x^i_1+...+\theta_nx_n^i$

___

**Crousera例子：**

下方的两个图分别是 $\theta_1=1 ,\theta_1=0.5$的情况此处我们姑且让$\theta_0$为0，方便讨论。

PS: $\theta_0$ or bias为直线与y轴的截距，通过hypothesis function可知 $h_\theta(x) = \theta_0+\theta_1x$

![](https://pic3.zhimg.com/v2-4587808d92ae5ae370a87e43bc2516b6_b.jpg)

theta\_1为1的情况，计算误差

![](https://pic1.zhimg.com/v2-bfacdf24560baafbe82a96e1a1913250_b.jpg)

theta\_1为0.5的情况，计算误差

普遍的，当我们取遍所有 $\theta$ ，得到Cost Function

![](https://pic3.zhimg.com/v2-68713154d786dce4def59d86f3853c3a_b.jpg)

显然的，我们看到当 $\theta_1$ = 1时，得到一个全局最小值，他就是我们要的最优解。

___

**例子2：**

上面的例子只考虑到了 $\theta_1$ ，下面的例子将同时考虑 $\theta_0,\theta_1$

![](https://pic4.zhimg.com/v2-e1fb7939ebed8003258111d6cab1b3b3_b.jpg)

当同时考虑 $\theta_0,\theta_1$时，使用等高线图能更好的表示Cost Function。

同样的，我们的目标为使得J最小，从图中可以看出为椭圆的中心。

**结束语：**

显然，要是我们一一列举 $\theta$，太麻烦了，而且不太现实。那么怎么才能以高效的方式得到最优解呢？梯度下降是一种方法。

# loss function VS cost function

对单个样本，你的prediction和ground truth之间的差异是Loss function,这种差异可以用极大似然，均方值等表示。
针对一个整个数据集（m个样本），你的prediction和ground truth之间的差异是Cost function,这种差异可以用极大似然，均方值表示。
也就是Cost function 和Loss function就差在**有没有把预测值和真实值的差异求和再取平均**

Loss Function 是定义在单个样本上的，算的是一个样本的误差。
Cost Function 是定义在整个训练集上的，是所有样本误差的平均，也就是损失函数的平均。
Object Function（目标函数 ）定义为：Cost Function + 正则化项。

机器学习中的监督学习本质上是给定一系列训练样本$\left(x_{i}, y_{i}\right)$，尝试学习$x \rightarrow y$的映射关系，使得给定一个$x$x，即便这个$x$不在训练样本中，也能够输出$\hat{y}$，尽量与真实的$y$接近。损失函数是用来估量模型的输出$\hat{y}$与真实的$y$之间的差距，给模型的优化指引方向。模型的结构风险包括了经验风险和结构风险，损失函数是经验风险函数的核心部分：

$$
\hat{\theta}=\arg \min _{\theta} \frac{1}{N} \sum_{i=1}^{N} L\left(y_{i}, f\left(x_{i} ; \theta\right)+\lambda \Phi(\theta)\right. \\
$$\\hat{\\theta}=\\arg \\min \_{\\theta} \\frac{1}{N} \\sum\_{i=1}^{N} L\\left(y\_{i}, f\\left(x\_{i} ; \\theta\\right)+\\lambda \\Phi(\\theta)\\right. \\\\

式中，前面的均值函数为经验风险，$L\left(y_{i}, f\left(x_{i} ; \theta\right)\right.$为损失函数，后面的项为结构风险，$\Phi(\theta)$衡量模型的复杂度

首先区分损失函数、代价函数和目标函数之间的区别和联系：

-   损失函数（Loss Function）通常是**针对单个训练样本而言**，给定一个模型输出$\hat{y}$和一个真实值$y$y，损失函数输出一个实值损失$L=f\left(y_{i}, \hat{y}_{i}\right)$，比如说：

-   线性回归中的均方差损失：$L(y_{i}, f\left(x_{i} ; \theta\right)=\left(f\left(x_{i} ; \theta\right)-y_{i}\right)^{2}$
L(y\_{i}, f\\left(x\_{i} ; \\theta\\right)=\\left(f\\left(x\_{i} ; \\theta\\right)-y\_{i}\\right)^{2}
-   SVM中的Hinge损失：$L(y_{i}, f\left(x_{i} ; \theta\right)=\max \left(0,1-f\left(x_{i} ; \theta\right) y_{i}\right)$
L(y\_{i}, f\\left(x\_{i} ; \\theta\\right)=\\max \\left(0,1-f\\left(x\_{i} ; \\theta\\right) y\_{i}\\right)
-   精确度定义中的0/1损失：$L(y_{i}, f\left(x_{i} ; \theta\right)=1)\Longleftrightarrow f\left(x_{i} ; \theta\right) \neq y_{i}$
L(y\_{i}, f\\left(x\_{i} ; \\theta\\right)=1)\\Longleftrightarrow f\\left(x\_{i} ; \\theta\\right) \\neq y\_{i}


-   代价函数（Cost Function）通常**是针对整个训练集**（或者在使用mini-batch gradient descent时的一个mini-batch）的总损失$J=\sum_{i=1}^{N} f\left(y_{i}, \hat{y}_{i}\right)$
J=\\sum\_{i=1}^{N} f\\left(y\_{i}, \\hat{y}\_{i}\\right)，
 比如说：
-   均方误差：$M S E(\theta)=\frac{1}{N} \sum_{i=1}^{N}\left(f\left(x_{i} ; \theta\right)-y_{i}\right)^{2}$
M S E(\\theta)=\\frac{1}{N} \\sum\_{i=1}^{N}\\left(f\\left(x\_{i} ; \\theta\\right)-y\_{i}\\right)^{2}
-   SVM的代价函数：$S V M(\theta)=\|\theta\|^{2}+C \sum_{i=1}^{N} \xi_{i}$
S V M(\\theta)=\\|\\theta\\|^{2}+C \\sum\_{i=1}^{N} \\xi\_{i}

-   目标函数（Objective Function）通常**是一个更通用的术语**，表示任意希望被优化的函数，用于机器学习领域和非机器学习领域（比如运筹优化），比如说，最大似然估计中似然函数是一个优化的目标函数
一句话总结三者的关系就是：A loss function is a part of a cost function which is a type of an objective function

