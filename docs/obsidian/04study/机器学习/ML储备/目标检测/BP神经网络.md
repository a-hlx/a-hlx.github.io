# 正向传播

全连接层，卷积层，采样层

# 反向传播

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212228942.png)


## 误差的计算

### Cross Entropy Loss Function（交叉熵损失函数）

#### 表达式

##### (1) 二分类

在二分的情况下，模型最后需要预测的结果只有两种情况，对于每个类别我们的预测得到的概率为 $p$ 和 $1-p ，此时表达式为（$log 的底数是 $e$）：

$$
L = \frac{1}{N}\sum_{i} L_i = \frac{1}{N}\sum_{i}-[y_i\cdot log(p_i) + (1-y_i)\cdot log(1-p_i)] \\
$$
其中：  
$y_i$—— 表示样本 $i$的label，正类为 $1$ ，负类为 $0$  
 $p_i$ —— 表示样本 $i$预测为正类的概率

##### (2) 多分类

多分类的情况实际上就是对二分类的扩展：

$$
L = \frac{1}{N}\sum_{i} L_i = - \frac{1}{N}\sum_{i} \sum_{c=1}^My_{ic}\log(p_{ic}) \\
$$

其中：  
$M$ ——类别的数量  
$y_{ic}$ ——符号函数（ $0$或 $1$），如果样本 $i$的真实类别等于 $c$取 $1$ ，否则取 $0$
$p_{ic}$ ——观测样本 $i$属于类别 $c$的预测概率


![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212243203.png)


## 误差的反向传播
![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212245306.png)

## 权重的更新

![](https://cdn.jsdelivr.net/gh/HLIX1/pic/lm_ML/202210212245429.png)

### 优化器optimazer

使网络得到更快的收敛,主要关注1，2，3，4

1.SDG优化器（Stochastic Gradient Descent）
缺点：易受样本噪声影响，可能陷入局部最优解

2.SGD+Momentum优化器

3.Adagrad优化器（自适应学习率）

4.RMSProp优化器（自适应学习率）

5.Adam优化器（自适应学习率）

(Adadelta)
