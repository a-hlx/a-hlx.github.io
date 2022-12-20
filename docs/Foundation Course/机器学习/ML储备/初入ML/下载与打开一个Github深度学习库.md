### 初入[深度](https://so.csdn.net/so/search?q=%E6%B7%B1%E5%BA%A6&spm=1001.2101.3001.7020)学习1——如何下载与打开一个Github深度学习库

-   [学习前言](https://blog.csdn.net/weixin_44791964/article/details/123440488#_2)
-   [下载一个仓库](https://blog.csdn.net/weixin_44791964/article/details/123440488#_5)
-   -   [一、Github](https://blog.csdn.net/weixin_44791964/article/details/123440488#Github_6)
    -   -   [1、Download Zip（不推荐，但可用）](https://blog.csdn.net/weixin_44791964/article/details/123440488#1Download_Zip_7)
        -   -   [a、打开网址](https://blog.csdn.net/weixin_44791964/article/details/123440488#a_9)
            -   [b、下载文件](https://blog.csdn.net/weixin_44791964/article/details/123440488#b_12)
            -   [c、下载与解压文件](https://blog.csdn.net/weixin_44791964/article/details/123440488#c_15)
        -   [2、git clone（推荐）](https://blog.csdn.net/weixin_44791964/article/details/123440488#2git_clone_21)
        -   -   [a、打开网址](https://blog.csdn.net/weixin_44791964/article/details/123440488#a_24)
            -   [b、复制HTTPS信息](https://blog.csdn.net/weixin_44791964/article/details/123440488#bHTTPS_27)
            -   [c、进行git clone](https://blog.csdn.net/weixin_44791964/article/details/123440488#cgit_clone_30)
    -   [二、Gitee（网络不好的情况下可用）](https://blog.csdn.net/weixin_44791964/article/details/123440488#Gitee_36)
    -   -   -   [a、创建仓库](https://blog.csdn.net/weixin_44791964/article/details/123440488#a_38)
            -   [b、仓库下载](https://blog.csdn.net/weixin_44791964/article/details/123440488#b_46)
-   [打开仓库](https://blog.csdn.net/weixin_44791964/article/details/123440488#_50)
-   -   [一、Download Zip](https://blog.csdn.net/weixin_44791964/article/details/123440488#Download_Zip_51)
    -   -   [1、正确示范](https://blog.csdn.net/weixin_44791964/article/details/123440488#1_52)
        -   [2、错误示范](https://blog.csdn.net/weixin_44791964/article/details/123440488#2_59)
    -   [二、git clone](https://blog.csdn.net/weixin_44791964/article/details/123440488#git_clone_64)

## 学习前言

入门深度学习的第一步就是下载一个已经写好的一个库，这个过程难度不大，但比较重要，有几种下载方法，可以参考一下。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190723165901974.jpg#pic_center)

## 下载一个仓库

## 一、[Github](https://so.csdn.net/so/search?q=Github&spm=1001.2101.3001.7020)

### 1、Download Zip（不推荐，但可用）

Download Zip方法其实就是在Github上下载一个压缩包，下载完成后，解压就可以获得深度学习库了。按步骤进行下载与解压就可以。

#### a、打开网址

首先，打开一个深度学习仓库，在这里以yolov5-pytorch版本为例，链接为[https://github.com/bubbliiiing/yolov5-pytorch](https://github.com/bubbliiiing/yolov5-pytorch)。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/10624bf4669a431d9ed300c12a318982.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### b、下载文件

然后点击绿色的code，之后点击里面的Download Zip，然后选择一个路径保存就可以。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6dc869d5646e4113a6626853c63ffb65.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### c、下载与解压文件

打开保存zip的文件夹。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/136f4aaeb19c40ee8fb06a89a4c63fec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
进行解压，就可以获得库的文件夹了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7cf5c237861c47d1b19c547a35f2fe34.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2、git clone（推荐）

Download Zip方法其实就是在Github上下载一个压缩包，下载完成后，解压就可以获得深度学习库了。但这样的话会缺少Git信息，因此不太建议用Download Zip，使用git clone会好很多，修改仓库时会保留Git信息。  
这个方法在windows上需要首先装一下git程序[https://git-scm.com/](https://git-scm.com/)，下载完成直接安装即可。

#### a、打开网址

首先，打开一个深度学习仓库，在这里以yolov5-pytorch版本为例，链接为[https://github.com/bubbliiiing/yolov5-pytorch](https://github.com/bubbliiiing/yolov5-pytorch)。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/10624bf4669a431d9ed300c12a318982.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### b、复制HTTPS信息

然后点击绿色的code，复制其中的Https信息。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6dc869d5646e4113a6626853c63ffb65.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

#### c、进行git clone

打开git bash程序，然后进行git clone。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e20604e35a08457096c9cc4ae51ed54c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_16,color_FFFFFF,t_70,g_se,x_16#pic_center)  
git完成后会出现文件夹。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0ecdbc0d601e469d870be0193f59e762.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

## 二、Gitee（网络不好的情况下可用）

可能有些同学打不开Github，在国内可以选择Gitee替代，Gitee可以从github拉取仓库，然后再进行下载。

#### a、创建仓库

首先打开Gitee码云。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6f738916d4414f06bb41ded2824806d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_12,color_FFFFFF,t_70,g_se,x_16#pic_center)  
点击创建仓库。  
然后点击右上角的 **点击导入**，就可以从其它的网址进行导入了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0615634a55134e258d5f5f737670f571.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16)  
此时选择从URL导入，然后将需要导入的Github路径复制进去就可以。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2e678eea3d7c466d88361fef1bc43888.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16)

#### b、仓库下载

完成仓库创建后，按Github的步骤下载即可。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/cf74ada992b24a4c89d3d4ab6fcbbfe5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16)

## 打开仓库

## 一、Download Zip

### 1、正确示范

打开仓库其实很简单，如果安装VScode的时候有选择**添加到右键菜单栏**，直接进入yolov5-pytorch-main，然后右键**通过Code打开**就可以了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d1602639177640148b38e5370f7c4e92.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
或者直接打开一个新的VScode窗口点击**打开文件夹**，之后选择我们要打开的文件夹就可以了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/7a78ea8249ca44cdb8feabfb852321d8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
此时就正确打开仓库了  
![在这里插入图片描述](https://img-blog.csdnimg.cn/ebd73e4c319f48bdbcc9e32f411fa360.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

### 2、错误示范

有些同学解压后直接在原地打开了，这是错误的，这会导致根目录不正确，就像这样子。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4efc9e49a7874980a24a071509098b45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16)  
此时打开的根目录错误，会导致其中的文件无法正常运行，也会提示如**FileNotFoundError: \[Errno 2\] No such file or directory: 'model\_data/voc\_classes.txt’这样的错误**。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0011577dd390423eae87e139f87136ce.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16)

## 二、git clone

打开仓库的过程并没有变化，首先进入yolov5-pytorch，直接右键打开或者新建一个VScode窗口，打开文件夹即可。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d1602639177640148b38e5370f7c4e92.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
或者直接打开一个新的VScode窗口点击**打开文件夹**，之后选择我们要打开的文件夹就可以了。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/cb288b55a9964470aef06933abca9c1e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)  
此时就正确打开仓库了，此时的仓库是有Git信息的，我们修改文件的过程会被记录下来。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0988bf740c584edb9481cbb863c37b0d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQnViYmxpaWlpbmc=,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)