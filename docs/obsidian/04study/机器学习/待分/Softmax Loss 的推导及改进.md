Softmax Loss是深度学习中最常见的损失函数，完整的叫法是 Cross-entropy loss with softmax，其由三部分组成：Fully Connected Layer, Softmax Function（） 和 Cross-entropy Loss。使用softmax loss的pipline为：先使用一个encoder来学习数据的特征，再经过一个全连接层、softmax 函数，最后使用交叉熵计算损失。

![](https://pic4.zhimg.com/v2-6d4b572dc75067bb0da164b40c579aeb_b.jpg)

### 1.1、Softmax Loss的推导

### 1.1.1、 从概率分布说起

设真实分布为 $y=(0,\cdots,0,1,0,\cdots,0)$y=(0,\\cdots,0,1,0,\\cdots,0) ，其中第 $k$k 个label为1，预测分布为 $z=(z_1,\cdots,z_C)$z=(z\_1,\\cdots,z\_C) ， $C$C 为总类别数。用交叉熵衡量两个分布之间的距离，可得如下损失函数：  
$$
\mathcal{l}_{z}=-\sum_{i=1}^{C}y_i \log z_i=- \log z_k \\
$$\\mathcal{l}\_{z}=-\\sum\_{i=1}^{C}y\_i \\log z\_i=- \\log z\_k \\\\  
现在的问题是，给定全连接层的特征 $x$x ，如何表达出 $z=(z_1,\cdots,z_C)$z=(z\_1,\\cdots,z\_C) 。假设有两个样本 $x_i,x_j$x\_i,x\_j ，一个自然的想法是 $x_i$x\_i 和 $x_j$x\_j 之间相差的越远，属于同一个类 $k$k 的概率就越小。用 $\omega_k$\\omega\_k 表示样本 $x$x 属于第 $k$k 个类的参数，概率可以表达为：

$$
F(x_i-x_j,\omega_k)=F((x_i-x_j)^T·\omega_k)=\frac{p(x_i|k)}{p(x_j|k)} \\
$$F(x\_i-x\_j,\\omega\_k)=F((x\_i-x\_j)^T·\\omega\_k)=\\frac{p(x\_i|k)}{p(x\_j|k)} \\\\  
这里其实暗含了一个习惯，我们常常使用 $L_2$L\_2 距离比较特征之间的差异，而使用比例来比较概率的差异。进一步要求 $F$F 是特征 $x$x 构成的加法群 $(R,+)$(R,+) 和概率构成的乘法群 $(R_{>0},\times)$(R\_{>0},\\times) 之间的同态映射可得：

$$
F((x_i-x_j)^T·\omega_k)=\frac{F(x_i^T·\omega_k)}{F(x_j^T·\omega_k)} \\
$$F((x\_i-x\_j)^T·\\omega\_k)=\\frac{F(x\_i^T·\\omega\_k)}{F(x\_j^T·\\omega\_k)} \\\\

不难得出， $F$F 是指数函数。增加常数项 $b_k$b\_k ,就可以得到：

$$
F(x|k)= e^{x^T·\omega_k+b_k}=e^{l_k} \\
$$F(x|k)= e^{x^T·\\omega\_k+b\_k}=e^{l\_k} \\\\  
归一化预测分布，可得：  
$$
z_k= \frac{e^{l_k}}{\sum_{i=1}^{C}{e^{l_i}}} \\
$$z\_k= \\frac{e^{l\_k}}{\\sum\_{i=1}^{C}{e^{l\_i}}} \\\\

从而，损失函数为：  
$$
l= -\log z_k=-\log \frac{e^{l_k}}{\sum_{i=1}^{C}{e^{l_i}}}=-\log \frac{e^{x^T·\omega_k+b_k}}{\sum_{i=1}^{C}{e^{x^T·\omega_i+b_i}}} \\
$$l= -\\log z\_k=-\\log \\frac{e^{l\_k}}{\\sum\_{i=1}^{C}{e^{l\_i}}}=-\\log \\frac{e^{x^T·\\omega\_k+b\_k}}{\\sum\_{i=1}^{C}{e^{x^T·\\omega\_i+b\_i}}} \\\\

这就是我们熟知的 softmax loss，推导过程借鉴了[glove](https://link.zhihu.com/?target=https%3A//www.aclweb.org/anthology/D14-1162.pdf)。下面，我们从优化的角度推导softmax loss。和softmax这个名字相呼应，我们把softmax loss理解为“max loss”的“soft版本”。

### 1.1.2、先从SVM说起

svm的损失函数为：

$\min_{\omega,b} \frac{1}{2}\Vert\omega\Vert^2+C\sum_{i=1}^{m}\mathcal{l}_{0/1}(y_i(\omega^Tx_i+b)-1) \\$\\min\_{\\omega,b} \\frac{1}{2}\\Vert\\omega\\Vert^2+C\\sum\_{i=1}^{m}\\mathcal{l}\_{0/1}(y\_i(\\omega^Tx\_i+b)-1) \\\\  
其中 $C>0$C>0 是一个常数， $\mathcal{l}_{0/1}$\\mathcal{l}\_{0/1} 是"0/1"损失函数：  
$$
\mathcal{l}_{0/1}(z)=\begin{cases} 1, ~~if~z<0;\\ 0, ~~otherwise.\\ \end{cases} \\
$$\\mathcal{l}\_{0/1}(z)=\\begin{cases} 1, ~~if~z<0;\\\\ 0, ~~otherwise.\\\\ \\end{cases} \\\\

然而 $\mathcal{l}_{0/1}$\\mathcal{l}\_{0/1} 非凸、非连续，数学性质不好，使得损失函数不好优化。于是人们通常使用一些其他函数来替代 $\mathcal{l}_{0/1}$\\mathcal{l}\_{0/1} ，称为“替代损失”，常见的替代损失有：

> Hinge 损失： $\mathcal{l}_{hinge}(z)=max(0,1-z)$\\mathcal{l}\_{hinge}(z)=max(0,1-z)  
> 指数损失： $\mathcal{l}_{exp}(z)=exp(-z))$\\mathcal{l}\_{exp}(z)=exp(-z))  
> 对率损失： $\mathcal{l}_{log}(z)=log(1+exp(-z))$\\mathcal{l}\_{log}(z)=log(1+exp(-z))

**指数损失和对率损失可以看做hinge损失的smooth近似，也就是max损失的soft版本。**  

![](https://pic3.zhimg.com/v2-c286e08b364aef8880de14de1b121dd2_b.jpg)

### 1.1.3、说回Softmax Loss  

softmax针对的是多分类，假设有 $C$C 个类别，预测分布为 $z=(z_1,z_2,\cdots,z_c)$z=(z\_1,z\_2,\\cdots,z\_c) ，其中 $z_y$z\_y 为真实类别的logit。仿照svm定义 $\mathcal{l}_{0/1}$\\mathcal{l}\_{0/1} 为：  
$$
\mathcal{l}_{0/1}(z)=\begin{cases} 0, ~~if~z_y\gt max_{i,i\neq y}(z_i);\\ 1, ~~otherwise.\\ \end{cases} \\
$$\\mathcal{l}\_{0/1}(z)=\\begin{cases} 0, ~~if~z\_y\\gt max\_{i,i\\neq y}(z\_i);\\\\ 1, ~~otherwise.\\\\ \\end{cases} \\\\  
即: 如果 $z_y$z\_y 比其它logits都大，则分类准确，损失为0，不然损失为1。借鉴svm，不难想出一个替代损失为：

$$
l(z)=\sum_{i,i \neq y}max(z_i-z_y,0) \\
$$l(z)=\\sum\_{i,i \\neq y}max(z\_i-z\_y,0) \\\\  
我们可以继续添加一个margin参数 $m$m ，让 $z_y$z\_y 比 $z_i$z\_i 大一些的时候才停止更新(即：梯度为0），以此拉开真实类别和其它类别的间隔：

$$
l(z)=\sum_{i,i \neq y}max(z_i-z_y+m,0) \\
$$l(z)=\\sum\_{i,i \\neq y}max(z\_i-z\_y+m,0) \\\\

直接把hinge loss应用在多分类上的话，当类别数 $C$C 特别大时，会有大量非目标logit得到优化（这些logit都会获得-1的梯度），这样每次优化时的梯度模长不等，极易梯度爆炸。  
其实， $z_y$z\_y 比其它logits都大时分类正确，可以换一种说法： $z_y$z\_y 比最大的非目标logtis大时分类正确、损失为0，即：

$$
l(z)=\max(\max_{i \neq y} z_i-z_y,0) \\
$$l(z)=\\max(\\max\_{i \\neq y} z\_i-z\_y,0) \\\\

但在优化这个损失函数时，每次最多只会有一个+1的梯度和一个-1的梯度进入网络，这样每次优化的分数过少，会使得网络收敛极其缓慢。**如何能尽可能多的优化非目标分数，但又限制每次参数更新的幅度？**我们可以使用 [LogSumExp](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/LogSumExp) 函数近似max函数，即max函数的soft版本：

$$
\max_{i}{z_i} \approx \log(\sum_{i}e^{z_i}), when~z_i > 0 \\
$$\\max\_{i}{z\_i} \\approx \\log(\\sum\_{i}e^{z\_i}), when~z\_i > 0 \\\\  
从而损失函数为：

$$
l_{lse}(z)=\max(log(\sum_{i \neq y} e^{z_i} )-z_y,0) \\
$$l\_{lse}(z)=\\max(log(\\sum\_{i \\neq y} e^{z\_i} )-z\_y,0) \\\\  
$l_{lse}$l\_{lse} 的导数为:

$$
\frac{\partial l_{lse}(z)} {\partial z_i}=\begin{cases} -1 ,~~if~ i =y,\\ \frac{e^{z_i}}{{\sum_{j \neq y}e^{z_j}}},~otherwise. \end{cases} \\
$$\\frac{\\partial l\_{lse}(z)} {\\partial z\_i}=\\begin{cases} -1 ,~~if~ i =y,\\\\ \\frac{e^{z\_i}}{{\\sum\_{j \\neq y}e^{z\_j}}},~otherwise. \\end{cases} \\\\  
可以看到，目标logit的梯度为-1，非目标logits的梯度之和为1，给予非目标logits的梯度1将会通过LogSumExp函数传播给所有非目标logits，各个非目标logits得到的梯度是通过softmax函数进行分配的，较大的非目标logits会得到更大的梯度使其更快地下降。并且，梯度绝对值和为2，这样我们就有效地限制住了梯度的总幅度。

**这样的近似其实还有一个问题，目标logit的梯度始终为-1。即使参数接近最优参数，目标logit的梯度仍为1，这会导致优化参数时在最优目标参数附近发生抖动，不利于收敛。**  
其实， $max(x,0)$max(x,0) 也有一个的smooth近似 [softplus function](https://link.zhihu.com/?target=https%3A//pytorch.org/docs/stable/generated/torch.nn.Softplus.html%23%3A~%3Atext%3DSoftPlus%2520is%2520a%2520smooth%2520approximation%2Cmachine%2520to%2520always%2520be%2520positive.)：

$$
\max(0, z) \approx \log(1+e^x) \\
$$\\max(0, z) \\approx \\log(1+e^x) \\\\  
从而，我们得到一个double soft的损失函数：

$$
\begin{aligned}  l_{softmax} & = log(1+e^{log(\sum_{i \neq y} e ^{z_i})-z_y})\\ & =\log(1+\frac{\sum_{i \neq y}e^{z_i}}{e^{z_y}})\\ & =\log\frac{\sum_i e^{z_i}}{e^{z_y}}\\ & =-log \frac{e^{z_y}}{\sum_i e^{z_i}} \end{aligned} \\
$$\\begin{aligned} l\_{softmax} & = log(1+e^{log(\\sum\_{i \\neq y} e ^{z\_i})-z\_y})\\\\ & =\\log(1+\\frac{\\sum\_{i \\neq y}e^{z\_i}}{e^{z\_y}})\\\\ & =\\log\\frac{\\sum\_i e^{z\_i}}{e^{z\_y}}\\\\ & =-log \\frac{e^{z\_y}}{\\sum\_i e^{z\_i}} \\end{aligned} \\\\

通过两次smooth近似，就得到我们熟知的softmax loss。

### 1.2、Softmax Loss的性质

### 1.2.1、良好的收敛性

$l_{softmax}$l\_{softmax} 的导数为：  
$$
\frac{\partial l_{softmax}(z)} {\partial z_i}=\begin{cases} -1+\frac{e^{z_y}}{\sum_{j}{e^{z_j}}} ,~~if~ i =y,\\ \frac{e^{z_j}}{\sum_{j}{e^{z_j}}} ,~otherwise. \end{cases} \\
$$\\frac{\\partial l\_{softmax}(z)} {\\partial z\_i}=\\begin{cases} -1+\\frac{e^{z\_y}}{\\sum\_{j}{e^{z\_j}}} ,~~if~ i =y,\\\\ \\frac{e^{z\_j}}{\\sum\_{j}{e^{z\_j}}} ,~otherwise. \\end{cases} \\\\  
**可以看到，相比于** $l_{lse}$l\_{lse} **，目标分数的梯度多了一项** $\frac{z_y}{\sum_{i}{e^{z_i}}}$\\frac{z\_y}{\\sum\_{i}{e^{z\_i}}} **。目标logit和非目标logit拉的越开，即** $\frac{z_y}{\sum_{i}{e^{z_i}}}$\\frac{z\_y}{\\sum\_{i}{e^{z\_i}}} **越大的时候，** $-1+\frac{z_y}{\sum_{i}{e^{z_i}}}$\-1+\\frac{z\_y}{\\sum\_{i}{e^{z\_i}}} **越接近于0，目标logit的梯度越小。同时，非目标logits的梯度也越小。即越接近于最优参数，梯度的模长越小，这当然有利于参数收敛。**

### 1.2.2、表征向量

设进入softmax的全连接层的特征为 $x$x ，全连接层的参数为 $(\omega_1^T,\omega_2^T,\cdots,\omega_C^T),(b_1,b_2,\cdots,b_C)$(\\omega\_1^T,\\omega\_2^T,\\cdots,\\omega\_C^T),(b\_1,b\_2,\\cdots,b\_C) ，则logit可以写成：

$$
log_i = \frac{e^{x^T·\omega_i+b_i}}{\sum_{j=1}^{C}{e^{x^T·\omega_j+b_j}}} \\
$$log\_i = \\frac{e^{x^T·\\omega\_i+b\_i}}{\\sum\_{j=1}^{C}{e^{x^T·\\omega\_j+b\_j}}} \\\\  
**从而，** $x^T·\omega_i+b_i$x^T·\\omega\_i+b\_i **最大的那一项就是模型的预测值。从贝叶斯的观点出发，我们可以把** $\frac{\omega_i}{\Vert\omega_i\Vert}$\\frac{\\omega\_i}{\\Vert\\omega\_i\\Vert} **理解为每个类的中心,** $\Vert \omega_i \Vert$\\Vert \\omega\_i \\Vert **理解为每个类的先验概率，** $x$x **就是每个样本的表征向量，通过cosin来衡量表征向量和类向量的相似度。**

## 2、Softmax loss的改进

## 2.1、Large-Margin Softmax Loss(2016)

> [Large-Margin Softmax Loss for Convolutional Neural Networks](https://link.zhihu.com/?target=https%3A//www.jmlr.org/proceedings/papers/v48/liud16.pdf)  
> In this paper, we propose a generalized large-margin softmax (L-Softmax) loss which explicitly encourages **intra-class compactness and inter-class separability** between learned features.

### 2.1.1、Motivation

The original softmax is to force $W_1^T x > W_2^T x (i.e. ∥W_1∥∥x∥ cos(θ_1) > ∥W_2∥∥x∥ cos(θ_2))$W\_1^T x > W\_2^T x (i.e. ∥W\_1∥∥x∥ cos(θ\_1) > ∥W\_2∥∥x∥ cos(θ\_2)) in order to classify x correctly. However, we want to make the classification more rigorous in order to produce a decision margin. So we instead require $∥W_1∥∥x∥ cos(mθ_1) > ∥W_2∥∥x∥cos(θ_2) (0 ≤ θ_1 ≤ mπ )$∥W\_1∥∥x∥ cos(mθ\_1) > ∥W\_2∥∥x∥cos(θ\_2) (0 ≤ θ\_1 ≤ mπ ) where m is a positive integer. Because the following inequality holds:  
$$
∥W_1∥∥x∥cos(θ_1) ≥ ∥W_1∥∥x∥cos(mθ_1) > ∥W_2∥∥x∥cos(θ_2) \\
$$ ∥W\_1∥∥x∥cos(θ\_1) ≥ ∥W\_1∥∥x∥cos(mθ\_1) > ∥W\_2∥∥x∥cos(θ\_2) \\\\

### 2.1.2、Formulation

![](https://pic4.zhimg.com/v2-848c1a11b70debd7e8c268efd9439bb7_b.jpg)

### 2.1.3、Visualization  

![](https://pic2.zhimg.com/v2-2a45bb1c51d4e0357ddf1d2a96a6bfe1_b.jpg)

  
这张图显示的是softmax loss和L-Softmax loss学习到的特征分布。第一列是softmax，第2,3,4列是L-Softmax loss在参数 m 不同取值时的学到的特征。如图所示，softmax loss学习到的类间的特征比较明显，但是类内特征比较分散，而L-Softmax loss的类内特征很紧凑。

### 2.2、Angular softmax loss(2017)

[SphereFace: Deep Hypersphere Embedding for Face Recognition](https://link.zhihu.com/?target=https%3A//openaccess.thecvf.com/content_cvpr_2017/papers/Liu_SphereFace_Deep_Hypersphere_CVPR_2017_paper.pdf)

### 2.2.1、Motivation

> ideal face features are expected to have smaller maximal intra-class distance than minimal inter-class distance under a suitably chosen metric space. However, few existing algorithms can effectively achieve this criterion. To this end, we propose the angular softmax (A-Softmax) loss that enables convolutional neural networks (CNNs) to learn angularly discriminative features.

在large margin softmax loss的基础上添加了限制条件 \\Vert W \\Vert=1,b=0 ，使得预测仅取决于 W 和 x 之间的角度 θ ，则得到了angular softmax loss，简称A-softmax loss。

### 2.2.2、Visualization  

![](https://pic1.zhimg.com/v2-8133779499c2d00617ce8f26e5b66f5c_b.jpg)

### 2.3、L2-constrained softmax loss(2018)

[CosFace: Large margin cosine loss for deep face recognition](https://link.zhihu.com/?target=http%3A//openaccess.thecvf.com/content_cvpr_2018/papers/Wang_CosFace_Large_Margin_CVPR_2018_paper.pdf)

与L-softmax loss和A-softmax loss不同，CosineFace直接在余弦空间中最大化分类界限，即对余弦值添加一个margin项 m ，定义如下：

![](https://pic3.zhimg.com/v2-19640d1d770a224739fb7a44b96206fe_b.jpg)

### 2.4、Additive angular margin loss (2018)

[ArcFace: Additive Angular Margin Loss for Deep Face Recognition](https://link.zhihu.com/?target=https%3A//openaccess.thecvf.com/content_CVPR_2019/papers/Deng_ArcFace_Additive_Angular_Margin_Loss_for_Deep_Face_Recognition_CVPR_2019_paper.pdf)

Additive angular margin loss在角度空间中增加了一个margin项 m ，并乘以一个scale参数 s ：

![](https://pic3.zhimg.com/v2-90bf17287f2c446e8745159dd2bb1b96_b.jpg)

至此，L-softmax loss, A-softmax loss, L2-softmax loss, additive-softmax loss 可以统一的表达为：  

![](https://pic4.zhimg.com/v2-128e2f8b9738e6eb7bb62c3f54799ebb_b.jpg)

## 3、Conclusion

本文从softmax loss出发，分别从概率角度和优化角度推导了softmax loss的表达式，并且指出softmax loss的全连接层输入特征可以作为样本的向量化表达。

针对softmax loss类内特征不紧凑，本文介绍了L-softmax loss, A-softmax loss, L2-constrained softmax loss等改进版本。**这些损失函数可以把原始样本映射到一个超球空间/表面，得到样本表征。例如，L-softmax loss使用内积度量距离，样本在空间中呈现散射状分布。 L2-constrained softmax loss将样本映射到球面上，使用cosine度量距离，样本呈球面分布。**

softmax loss及其改进版本其实是一种度量学习，其目标是使样本特征在度量空间中具有更好的性质：类内紧致性(intra-class compactness)和类间差异性(inter-class discrepancy)。

参考文献

1.  **[Glove](https://link.zhihu.com/?target=https%3A//www.aclweb.org/anthology/D14-1162.pdf)**[: Global vectors for word representation](https://link.zhihu.com/?target=https%3A//www.aclweb.org/anthology/D14-1162.pdf)
2.  [从最优化的角度看待Softmax损失函数](https://zhuanlan.zhihu.com/p/45014864)