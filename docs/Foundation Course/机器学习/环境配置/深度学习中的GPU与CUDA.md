> 对应视频教程：https://www.bilibili.com/video/BV1S5411X7FY/



### 文章目录

-   -   [1\. 显卡（GPU）与驱动](https://tudui.blog.csdn.net/article/details/125708980#1_GPU_3)
    -   [2\. 显卡与CUDA](https://tudui.blog.csdn.net/article/details/125708980#2_CUDA_15)
    -   [3\. 如何查看自己的显卡](https://tudui.blog.csdn.net/article/details/125708980#3__27)

显卡，也称之为 GPU。GPU 的全称是 Graphics [Processing](https://so.csdn.net/so/search?q=Processing&spm=1001.2101.3001.7020) Unit（图形处理单元）。它出现的目的一目了然，就是用来显示图像的。没错，就是用来在电脑显示器上显示图像的。

大家其实只要知道我们的电脑都有显卡这一点就行了。但我们在[深度](https://so.csdn.net/so/search?q=%E6%B7%B1%E5%BA%A6&spm=1001.2101.3001.7020)学习中说的显卡（GPU）一般特指是英伟达（NVIDIA）品牌的显卡，这个我们后面慢慢来说。

除了显卡这个概念之外，还有个概念是驱动。驱动，相信大家都不陌生。我们有的时候给电脑配备一些设备的时候，有可能需要安装对应的驱动，这些设备才能正常运行。

驱动，就是能够让计算机正确识别一些外设（设备）。

显卡，就是外部设备。所以，我们需要安装对应的驱动，这样计算机才能够正确识别对应的显卡，并充分利用显卡的能力。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/b524f7a28a8e41aea1a089ede9ee73e4.png#pic_center)  
大家可以看到，上面这张图中，底部的显卡、鼠标、声卡之类的就是我们的外部设备，是个实打实的硬件，看得见摸得着的东西。中间的 Operating System 就是我们用的操作系统（Windows，Mac，Linux），可以理解为就是我们的电脑。在 Operating System 和 底部的硬件之间，有个 Device Driver，这个就是我们上面讲到的驱动。只有我们在电脑上安装对应的驱动，我们电脑才能正确识别这些实打实的硬件。

## 显卡与CUDA

在深度学习中，我们常说的显卡，只是指英伟达（NVIDIA）品牌的显卡。其它品牌的显卡暂时还不行哦。

至于为什么呢？这都是因为英伟达（NVIDIA）以前的一个英明的决定。英伟达（NVIDIA）开发了一个开发平台，名叫CUDA。开发者/程序员可以使用这个CUDA开发平台来充分利用英伟达的显卡，可以利用这个CUDA平台，让一部分计算可以在GPU上进行。

后来，随着显卡的计算能力得到不到提升，很多程序尝试使用CUDA平台来进行计算。然后大家发现，哎呀，效果真不错。

在开发深度学习库（PyTorch, Tensorflow等）的时候，开发者如果想让深度学习运算放在GPU上运行，自然而然就想到了CUDA这个平台。所以，几乎所有的深度学习库都需要英伟达的显卡。

但随着一些神经网络芯片的出现，比如 Apple M系列芯片的出现，相信深度学习库会支持越来越多的能够加速神经网络运算的芯片。

![在这里插入图片描述](https://img-blog.csdnimg.cn/00c05a053c814e039a1c14de845774d3.png#pic_center)

## 如何查看自己的显卡

在Windows平台上，查看自己的显卡，其实并不难。大家只需要找到 任务管理器**（ctrl+shift+esc)** 或者 设备管理器，然后进行查看就行了。

任务管理器        **ctrl+shift+esc**

对于 任务管理器，找到 性能 选项卡，然后点击其中的GPU，之后就会在旁边的右上角显示对应的显卡名称。

就像下面这张图，显示这台计算机上的GPU型号为NVIDIA GeForce GTX 1060，其中带有NVIDIA字眼，说明是英伟达品牌的显卡。那我们就可以安装GPU版本的PyTorch，GPU版本的PyTorch可以加速神经网络的训练和运算过程。

如果大家有英伟达（NVIDIA）品牌的显卡，大家在安装的时候，记得选择GPU版本的PyTorch，充分利用自己的显卡性能来进行深度学习的学习。

![在这里插入图片描述](https://img-blog.csdnimg.cn/54d4f07895444287a7d797d356c91649.png#pic_center)  
如果看到性能选项卡中GPU型号没有NVIDIA字眼，就说明电脑上没有英伟达品牌的显卡，就像下面这张图一样。

![在这里插入图片描述](https://img-blog.csdnimg.cn/f32db30353224087b3b5edfc6a4c7751.png#pic_center)  
这张图中，GPU的型号为 Intel® UHD Graphics 750，所以不是英伟达品牌的显卡。那大家在后续安装PyTorch的时候，需要选择CPU版本的PyTorch。

CPU版本的PyTorch并不影响学习哦！！！

在设备管理器中的显示适配器中也可以看到自己电脑的显卡型号。

![在这里插入图片描述](https://img-blog.csdnimg.cn/f5211557938a4566b0ef8ef59bc549f8.png#pic_center)  
如果大家确信自己的电脑有对应的显卡，但是在 任务管理器 和 设备管理器 中没有看到，说不定是因为没有安装驱动或者是没有安装正确。所以无法在 任务管理器 和 设备管理器 中看到。这个时候，就得去借助各种驱动软件。

就像下面这样，驱动软件中的主显卡中显示了NVIDIA显卡，但是在任务管理器中没有对应的显卡，这种情况可以利用驱动软件安装或者修复驱动就行了。但这种情况出现的概率还是很低的。

![在这里插入图片描述](https://img-blog.csdnimg.cn/e0ce1d4cd9b642b895cc5e648ac94958.png#pic_center)



