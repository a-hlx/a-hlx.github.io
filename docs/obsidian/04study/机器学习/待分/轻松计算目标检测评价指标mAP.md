[轻松计算目标检测评价指标mAP - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/139073511)

**mAP（均值平均精度）**是目标检测中的最常用的评价指标，详细理解其计算方式有助于我们评估算法的有效性，并针对评测指标对算法进行调整。

## 二、相关知识点介绍<sup data-text="" data-url="https://blog.csdn.net/hsqyc/article/details/81702437#comments_10227172" data-numero="1" data-draft-node="inline" data-draft-type="reference" data-tooltip="https://blog.csdn.net/hsqyc/article/details/81702437#comments_10227172" data-tooltip-preset="white" data-tooltip-classname="ztext-referene-tooltip"><a id="ref_1_0" href="https://zhuanlan.zhihu.com/p/139073511#ref_1" data-reference-link="true" aria-labelledby="ref_1" pcked="1">[1]</a></sup>

### **1\. IOU（交并比）**

它是模型所**预测**的检测框(bbox)和**真实**的检测框(ground truth)的**交集和并集之间的比例**。

![](https://pic3.zhimg.com/v2-2f7217561bf49f419445c0dc94cbba5e_b.jpg)

图一 IOU

```
def Iou(rec1,rec2):
  x1,x2,y1,y2 = rec1 #分别是第一个矩形左右上下的坐标
  x3,x4,y3,y4 = rec2 #分别是第二个矩形左右上下的坐标
  area_1 = (x2-x1)*(y1-y2)
  area_2 = (x4-x3)*(y3-y4)
  sum_area = area_1 + area_2
  w1 = x2 - x1#第一个矩形的宽
  w2 = x4 - x3#第二个矩形的宽
  h1 = y1 - y2
  h2 = y3 - y4
  W = min(x1,x2,x3,x4)+w1+w2-max(x1,x2,x3,x4)#交叉部分的宽
  H = min(y1,y2,y3,y4)+h1+h2-max(y1,y2,y3,y4)#交叉部分的高
  Area = W*H#交叉的面积
  Iou = Area/(sum_area-Area)
  return Iou
```

### **2\. TP TN FP FN**

T或者N代表的是该样本是否被分类分对？P或者N代表的是该样本被分为什么？

-   TP（True Positives）意思我们倒着来翻译就是“被分为正样本，并且分对了”，
-   TN（True Negatives）意思是“被分为负样本，而且分对了”，
-   FP（False Positives）意思是“被分为正样本，但是分错了”，
-   FN（False Negatives）意思是“被分为负样本，但是分错了”

为方便记忆，我们引入下图：

![](https://pic4.zhimg.com/v2-2bc0d7649dc54e60fa5d2c42fb3ef56f_b.jpg)

图二

**左半矩形是正样本，右半矩形是负样本。**一个2分类器，在图上画了个圆，分类器认为圆内是正样本，圆外是负样本。

-   那么左半圆分类器认为是正样本，同时它确实是正样本，那么就是“被分为正样本，并且分对了”，也就是**TP**。
-   左半矩形扣除左半圆的部分就是分类器认为它是负样本，但是它本身却是正样本，就是“被分为负样本，但是分错了”，也就是**FN**。
-   右半圆分类器认为它是正样本，但是本身却是负样本，那么就是“被分为正样本，但是分错了”，也就是**FP**。
-   右半矩形扣除右半圆的部分就是分类器认为它是负样本，同时它本身确实是负样本，那么就是“被分为负样本，而且分对了”，也就是**TN**。

### **3\. Precision（精度）和Recall（召回率）**

根据图二，可以用下面的计算方式去说明：

![](https://pic2.zhimg.com/v2-e33c1f4ad92f9100a9f2bf7f191c6d15_b.jpg)

图三

![](https://pic2.zhimg.com/v2-a3c2b5e0f33a7710d7afde918e2ec961_b.jpg)

分类器认为是正类并且确实是正类的部分占所有分类器认为是正类的比例

![](https://pic3.zhimg.com/v2-6f98e5bd7bcff6e6bd5c54a7adde40f2_b.jpg)

分类器认为是正类并且确实是正类的部分占所有确实是正类的比例

## 三、举例计算mAP

有3张图如下，要求算法找出face。蓝色框代表标签label，绿色框代表算法给出的结果pre，旁边的红色小字代表置信度。

设定第一张图的预测框叫pre1，第一张的真实框叫label1。第二张、第三张同理。

![](https://pic1.zhimg.com/v2-2fbf0828ab789605f5a73cdd18d680ac_b.jpg)

![](https://pic2.zhimg.com/v2-cb70e4ad4cb7533d81c9c588616069f5_b.jpg)

### **1.根据IOU计算TP,FP**

首先我们计算每张图的pre和label的IOU，根据IOU是否大于0.5来判断该pre是属于TP还是属于FP。显而易见，pre1是TP，pre2是FP，pre3是TP。

### 2.置信度排序

根据每个pre的置信度进行从高到低排序，这里pre1、pre2、pre3置信度刚好就是从高到低。

### **3.在不同置信度阈值下获得Precision和Recall**

-   首先，设置阈值为0.9，无视所有小于0.9的pre。那么检测器检出的所有框pre即TP+FP=1，并且pre1是TP，那么Precision=1/1。因为所有的label=3，所以Recall=1/3。这样就得到一组P、R值。
-   然后，设置阈值为0.8，无视所有小于0.8的pre。那么检测器检出的所有框pre即TP+FP=2，因为pre1是TP，pre2是FP，那么Precision=1/2=0.5。因为所有的label=3，所以Recall=1/3=0.33。这样就又得到一组P、R值。
-   再然后，设置阈值为0.7，无视所有小于0.7的pre。那么检测器检出的所有框pre即TP+FP=3，因为pre1是TP，pre2是FP，pre3是TP，那么Precision=2/3=0.67。因为所有的label=3，所以Recall=2/3=0.67。这样就又得到一组P、R值。

### 4.绘制PR曲线并计算AP值

根据上面3组PR值绘制PR曲线如下。然后每个“峰值点”往左画一条线段直到与上一个峰值点的垂直线相交。这样画出来的红色线段与坐标轴围起来的面积就是AP值。

![](https://pic4.zhimg.com/v2-4bca2079016dce0eab97dded6ca458cb_b.jpg)

![](https://pic3.zhimg.com/v2-8a606e9830bb4ecf0a2cee8c5dce3e8e_b.jpg)

### 5.计算mAP<sup data-text="" data-url="https://www.cnblogs.com/Tom-Ren/p/11054605.html" data-numero="2" data-draft-node="inline" data-draft-type="reference" data-tooltip="https://www.cnblogs.com/Tom-Ren/p/11054605.html" data-tooltip-preset="white" data-tooltip-classname="ztext-referene-tooltip"><a id="ref_2_0" href="https://zhuanlan.zhihu.com/p/139073511#ref_2" data-reference-link="true" aria-labelledby="ref_2" pcked="1">[2]</a></sup>

AP衡量的是对一个类检测好坏，mAP就是对多个类的检测好坏。就是简单粗暴的把所有类的AP值取平均就好了。比如有两类，类A的AP值是0.5，类B的AP值是0.2，那么mAP=（0.5+0.2）/2=0.35

```
# AP的计算
def _average_precision(self, rec, prec):
    """
    Params:
    ----------
    rec : numpy.array
            cumulated recall
    prec : numpy.array
            cumulated precision
    Returns:
    ----------
    ap as float
    """
    if rec is None or prec is None:
        return np.nan
    ap = 0.
    for t in np.arange(0., 1.1, 0.1):  #十一个点的召回率，对应精度最大值
        if np.sum(rec >= t) == 0:
            p = 0
        else:
            p = np.max(np.nan_to_num(prec)[rec >= t])
        ap += p / 11.  #加权平均
    return ap
```

## 参考

1.  [^](https://zhuanlan.zhihu.com/p/139073511#ref_1_0)[https://blog.csdn.net/hsqyc/article/details/81702437#comments\_10227172](https://blog.csdn.net/hsqyc/article/details/81702437#comments_10227172)
2.  [^](https://zhuanlan.zhihu.com/p/139073511#ref_2_0)[https://www.cnblogs.com/Tom-Ren/p/11054605.html](https://www.cnblogs.com/Tom-Ren/p/11054605.html)