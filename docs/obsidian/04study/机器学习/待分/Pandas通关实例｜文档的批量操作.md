![图片](https://mmbiz.qpic.cn/mmbiz_jpg/LLZEwkd9YqoEaOEbCzTicu02wN2bcFpzr18o2dExxlhV8VyLuBic34HcjOxIlhmoV3XWPLe13KpIliaVcVSuZAJag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

本篇内容是对之前内容的一个阶段性总结与提升应用,在实际工作中应用的频率很高,相当实用与高效。

01

**批量合并同一文件夹中的workbook**

**1**

●

**采用glob库**

导入glob库,合并指定文件夹内的所有Excel文件,代码如下:

```
import glob
```

输出的结果如图7-10所示。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/LLZEwkd9YqoEaOEbCzTicu02wN2bcFpzrXMbQgicggUJp5CPRmNLbFLUrUJOUCGE3Rl1JZsvvic87RThZ9lVzRGkQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

■ 图7-10 数据的合并

**2**

●

**采用os库**

就实际应用而言，采用os模块的频率是很高的，所以os模块可以花一些时间去深入了解一下，代码如下：

```
import os
```

输出的结果与上面采用glob库的结果完全相同。扩展一下: 如果用pd.ExcelWriter()方法,则代码要怎么写呢?

02

**批量合并同一文件**

**工作簿中的worksheet**

在前面讲解pd.concat()时,演示了大量的sheet合并的案例。在此想表达的是: 在DataFrame的concat之前,可以对相关DataFrame做一些事先的加工,然后合并,代码如下:

```
df = pd.DataFrame()
```

输出的结果如图7-11所示。

■ 图7-11 合并后的数据

上面的dfA 和dfB也可以采用循环追加的方式,然后合并到一个DataFrame中,代码如下:

```
import pandas as pd
```

输出的结果如下:

```
City Date Name  Weight
```

上面代码中的append也可以改用列表推导式完成。例如,以下代码与上面的代码实现的效果是完全一致的,代码如下:

```
import pandas as pd
```

再用pd.ExcelWriter()实现相同的效果,代码如下:

```
import pandas as pd
```

即使用pd.ExcelWriter(),也可以用自定义函数实现上述的效果,代码如下:

```
def AA(self):
```

如果读者对微软Excel中的Power Query熟悉,则实现上面的效果也是很轻松的,代码如下:

```
let
```

甚至可以在自定义函数中涵盖更多的操作。例如: 对Date列进行数据类型转换并依此排序,代码如下:

```
def AA(self):
```

呈现的效果如图7-12所示。

■ 图7-12 合并数据

03

**批量更改DataFrame中的列名**

现在有这样一个需求: 先将列名全部小写,然后将列名中的e改为\_。准许备用replace()方法实现,代码演示如下:

```
df = pd.read_excel('demo_.xlsx')
```

输出的结果如下:  

```
dat_ nam_       city  ag_  worky_ars  w_ight    bmi scor_0 2020-12-12  Joe    Beijing   76 35 56.0  18.86     A1 2020-12-12  Kim   Shanghai   32 12 85.0  21.27     A2 2020-12-13  Jim   Shenzhen   55 23 72.0  20.89     B3 2020-12-13  Tom        NaN   87 33 NaN  21.22     C4 2020-12-14  Jim  Guangzhou   93 42 59.0  20.89     B5 2020-12-14  Kim     Xiamen   78 36 65.0    NaN     B6 2020-12-15  Sam     Suzhou   65 32 69.0  22.89     A
```

或者,想将导入的DataFrame从第4列开始,在列名前加上new\_。采用rename()方法实现,代码演示如下:

```
df = pd.read_excel('demo_.xlsx')
```

输出的结果如图7-13所示。

■ 图7-13 批量修改列名

如果需要更改的列名不是很多,则可直接用replace的链式写法完成,代码如下:

```
df = pd.read_excel('demo_.xlsx',nrows=2)
```

输出的结果如图7-14所示。

■ 图7-14 列名修改

04

**批量拆分DataFrame**

现在以Demo\_.xlsx中的第1个表为例,以其中的Name列为依据进行拆分,并且拆分到同一个Excel中的多个Sheets中,本次可采用read\_excel加ExcelWrite的方式来完成, 代码如下:

```
#获取数据
```

代码运行后,会发现在当前代码存储的同一文件夹内新生成了一个name.xlsx文件,Excel文件内有Joe、Jim、Kim、Tom、Sam 5个sheet。

当然,上面的read\_excel可以改用ExcelFile(),df\['Name' \].unique()可以改用set()等。读者可以尝试一下如何完成。

更多的批量拆分DataFrame的案例会放到df.groupby()中讲解。

05

**参考书籍**

**《Pandas通关实战》**

ISBN：978-7-302-60061-9

黄福星  编著

定价：119.00元

**内容简介**

本书系统阐述了Pandas基础知识、应用原理，以及应用流程和应用技巧等实战知识。

全书共分为5篇：第一篇为入门篇（第1和2章），第二篇为基础篇（第3和4章），第三篇为基础强化篇（第5~7章），第四篇为进阶篇（第8~11章）, 第五篇为案例篇（第12章）。书中主要内容包括Python简介、NumPy基础、Pandas入门、数据筛选、数据转换、文本转换、数据获取、数据处理、数据分组、时序分析、数据可视化、通关案例。

本书可作为Python数据分析的入门与进阶书籍，适用于有一定Python基础的读者、对数据分析感兴趣的学生，也可作为数据分析及其它编程爱好者、IT培训机构的参考书籍。

**编辑推荐**

本书秉承Less is more(少即是多)的原则，追求“简约但不简单”的风格。从入门篇到进阶篇的11个章节，主要都是围绕着一个简单的“7行8列的数据”进行有效地讲解，把Pandas中使用频率最高的或效率最高的80%的函数、方法、属性全部有效地串接起来，减少读者浪费时间去理解不同的数据源，让更多的精力聚焦于专业知识的学习。

[](http://mp.weixin.qq.com/s?__biz=MzA4Nzk0MjQ4NA==&mid=2651862773&idx=3&sn=376835d02e2fcb4acba1519cefd1a988&chksm=8bd522cebca2abd8c3c6809bd39dd5a7cf9c0c8536de7334eb0116776535ab9ca1a5b21dcd2e&scene=21#wechat_redirect)

[](http://mp.weixin.qq.com/s?__biz=MzA4Nzk0MjQ4NA==&mid=2651863087&idx=3&sn=9f8a8b8752219f856ec3f384e7b25aa8&chksm=8bd52c14bca2a502018b241805ef2de8deb326329700f3922dfdfb9ddcd1c0a5365e0f3c24a7&scene=21#wechat_redirect)