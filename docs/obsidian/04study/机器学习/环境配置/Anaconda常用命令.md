## 摘要

本文内容一共三部分，第一部分是通道管理，第二部分是虚拟环境管理，第三部分是包管理，理论上anaconda掌握这三个技巧就足以搭建自己的深度学习环境了，建议大家收藏，方便以后查阅。

## 通道管理

在国内用官方的通道速度会非常慢，所以一般都需要把通道换成国内的，国内有很多镜像源，像清华，中科大等，个人推荐使用清华源。

更换国内通道一般都是用命令行，但命令行模式麻烦，这里不推荐，这里推荐使用Anaconda Navigator软件来管理通道，就是下图所示软件。

![](https://pic2.zhimg.com/v2-72b314b4df22de0ade919d3729023e1d_b.jpg)

此程序在开始菜单，anaconda3文件夹下可以找到。

首先是清华源的五条网址：

```
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
```

复制麻烦，可以直接搜索anaconda清华源。

打开Anaconda Navigator后，找到Channels按钮，打开它，逐条输入五个清华源地址，每条按回车确认。

![](https://pic4.zhimg.com/v2-2bdd127771a4e87505d80b514f13ba6f_b.jpg)

输入完后，按Update Channels按钮，确认后如图所示：

![](https://pic3.zhimg.com/v2-1d9ba3a7d85604f55819f56eb32f48c2_b.jpg)

清华源通道即更换成功，更换其他通道同理，不再赘诉。

### 补充命令行添加清华源通道

查看当前conda配置

```
conda config --show channels
```

设置通道

```
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```

设置搜索时显示通道地址

```
conda config --set show_channel_urls yes
```

持久添加通道：conda config --add channels 通道地址 
删除通道：conda config --remove channels 通道地址

## 虚拟环境

Windows下虚拟环境的操作推荐用Anaconda Prompt来执行。

![](https://pic2.zhimg.com/v2-14058daf28b0c8f6d3d4e1980542aaa5_b.jpg)

### 新建虚拟环境

```
# envname 指代你新建的环境的名称
conda create --name envname
# 后面会让你确认,输入y回车就好

```

### 删除虚拟环境

```
conda remove --name envname --all
删除虚拟环境：conda remove –n 虚拟环境名字 --all
```

### 创建指定python版本,指定包的虚拟环境

```
# 指定python版本
conda create -n envname python=3.6
# 添加镜像加速
conda create –n 虚拟环境名字 python=版本 –c 镜像地址
# 指定包
conda create -n envname scipy
# 指定包版本
conda create -n envname scipy=0.15.0
# 指定python版本,以及多个包
conda create -n envname python=3.6 scipy=0.15.0
```

### 给虚拟环境安装包

```
# 首先需要创建名称为envname的虚拟环境
conda install -n envname scipy
# 指定包版本conda install -n envname scipy=0.15.0
```

### 克隆一个环境

```
# clone_env 代指克隆得到的新环境的名称
# envname 代指被克隆的环境的名称
conda create --name clone_env --clone envname
```

### 查看conda环境信息

```
conda env list
```

### 激活新环境

```
# for windows
activate envname
# for liunx and MACOS 
source activate envname
```

### 退出当前环境

```
# for windows
deactivate
# for linux and MACOS
source deactivate
```

## 包管理

### 搜索包

```
# 在所有添加的仓库以及默认仓库中搜索包 numpy
conda search numpy
```

### 安装包

```
# 向当前环境安装包 scipy
conda install scipy
# 向当前环境安装包 scipy 并指定版本
conda install scipy=0.15.0
# 向当前环境安装多个包
conda install scipy curl
# 向当前环境安装多个包,并指定包版本
conda install scipy=0.15.0 curl=7.26.0
# 向当前环境安装多个包,并指定包版本与python版本,一般情况下不用指定python版本
conda install scipy=0.15.0 curl=7.26.0 -n py34_env
# 向指定虚拟环境中安装指定包
conda install --name myenv scipy
```

### 查看所有安装的包

```
# 查看当前换件中安装的所有包
conda list
# 查看指定虚拟环境中安装的所有包
conda list -n envname
```

### 安装非conda包/conda中使用pip

```
# 可以使用如下命令安装pip到当前虚拟环境
conda install pip
# 使用pip安装numpy
pip install numpy
```

### 更新环境

```
# 更新指定包
conda update unmpy
# 更新所有包
conda update
# 更新python
conda update python
# 更新conda本身
conda update conda
# 更新conda库
conda update conda
# 更新anaconda版本
conda update anaconda
```

### 删除包

```
# 删除当前环境中的scipy包
conda remove scipy
# 删除当前环境中的多个包
conda remove scipy curl
# 删除指定环境中的指定包
conda remove -n myenv scipy
```

![](https://pic3.zhimg.com/v2-fd4262bd772f32939aff83f9dad804de_b.jpg)