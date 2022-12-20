[Google Colab Tutorial_软耳朵DONG的博客-CSDN博客](https://blog.csdn.net/m0_52650517/article/details/121708879)


## Google Colab Tutorial

-   [一、Colab 简介](https://blog.csdn.net/m0_52650517/article/details/121708879#Colab__1)
-   -   [1.1 Colab 是什么？](https://blog.csdn.net/m0_52650517/article/details/121708879#11_Colab__2)
    -   [1.2 Jupyter 和 Colab 有什么区别？](https://blog.csdn.net/m0_52650517/article/details/121708879#12_Jupyter__Colab__4)
-   [二、Colab 使用](https://blog.csdn.net/m0_52650517/article/details/121708879#Colab__6)
-   -   [2.1 进入 Google 云端硬盘](https://blog.csdn.net/m0_52650517/article/details/121708879#21__Google__7)
    -   [2.2 关联更多应用](https://blog.csdn.net/m0_52650517/article/details/121708879#22__10)
    -   [2.3 安装 colaboratory](https://blog.csdn.net/m0_52650517/article/details/121708879#23__colaboratory_13)
    -   [2.4 新建 Google Colaboratory](https://blog.csdn.net/m0_52650517/article/details/121708879#24__Google_Colaboratory_24)
    -   [2.5 必要的配置内容](https://blog.csdn.net/m0_52650517/article/details/121708879#25__26)
    -   -   [（1）更改文件名称](https://blog.csdn.net/m0_52650517/article/details/121708879#1_27)
        -   [（2）连接到托管的运行时](https://blog.csdn.net/m0_52650517/article/details/121708879#2_32)
        -   [（3）选择 GPU](https://blog.csdn.net/m0_52650517/article/details/121708879#3_GPU_35)
-   [三、常用操作](https://blog.csdn.net/m0_52650517/article/details/121708879#_42)
-   -   [3.1 挂载](https://blog.csdn.net/m0_52650517/article/details/121708879#31__43)
    -   [3.2 文件夹的切换](https://blog.csdn.net/m0_52650517/article/details/121708879#32__58)
-   [参考链接](https://blog.csdn.net/m0_52650517/article/details/121708879#_61)

## 1.1 Colab 是什么？

\\qquad `Colaboratory` 简称 “`Colab`”，是 `Google Research` 团队开发的一款产品。在 `Colab` 中，任何人都可以通过浏览器编写和执行任意 `Python` 代码。它尤其适合机器学习、数据分析和教育目的。从技术上说，`Colab` 是一种托管式 `Jupyter` 笔记本服务。用户无需进行设置，就可以直接使用，同时还能获得 `GPU` 等计算资源的免费使用权限。

## 1.2 Jupyter和 Colab 有什么区别？

\\qquad `Jupyter` 是一个开放源代码项目，而 `Colab` 是在 `Jupyter` 基础之上开发的。通过 Colab，您无需下载、安装或运行任何软件，就可以使用 Jupyter 笔记本并与他人共享。

## 二、Colab 使用

## 2.1 进入 Google 云端硬盘

\\qquad [https://drive.google.com/drive/my-drive](https://drive.google.com/drive/my-drive)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0d0548db75fa43e8ba3574611c1fd0f1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6L2v6ICz5py1RE9ORw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 2.2 关联更多应用

\\qquad 新建 ⇒ \\pmb{\\Rightarrow} ⇒⇒⇒ 更多 ⇒ \\pmb{\\Rightarrow} ⇒⇒⇒ 关联更多应用  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4896cc3ebcf14638b9a12db5e13d4a73.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6L2v6ICz5py1RE9ORw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 2.3 安装 colaboratory

## 2.4 新建 Google Colaboratory

![在这里插入图片描述](https://img-blog.csdnimg.cn/f421f056e7ba42d49b8ef29c560acb7e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6L2v6ICz5py1RE9ORw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 2.5 必要的配置内容

### （1）更改文件名称

### （2）连接到托管的运行时

-   连接到托管的运行时  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/9b8145e71c2945d0ab84f428c7777094.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6L2v6ICz5py1RE9ORw==,size_13,color_FFFFFF,t_70,g_se,x_16)

### （3）选择 GPU

## 三、常用操作

## 3.1 挂载

\\qquad 默认情况下，运行的程序文件、数据集和模型文件存放在虚拟的硬盘中，一旦断开，任何数据都将无情的消失。而我们在运行代码的时候往往需要向模型提供外部来源中的训练和测试数据集，保存最终的训练结果，这些操作我们可以利用Google 云端硬盘来实现。以下示例展示了如何使用授权代码在您的运行时上装载 Google 云端硬盘，以及如何在那里写入和读取文件。一旦执行，您便可以在 [https://drive.google.com/](https://drive.google.com/) 中看到相应的新文件。

## 3.2 文件夹的切换

-   `os.chdir` 命令可以实现对当前文件夹的切换  
    ![在这里插入图片描述](https://img-blog.csdnimg.cn/cae4d599572f4b74a40dafc9c63861f2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6L2v6ICz5py1RE9ORw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 参考链接

-   官网介绍：[https://colab.research.google.com/notebooks/intro.ipynb](https://colab.research.google.com/notebooks/intro.ipynb)
-   官网常见问题解答：[https://research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)