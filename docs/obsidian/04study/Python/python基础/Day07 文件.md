# 文件读操作

## read()

```python
# 1. 打开文件
f = open('a.txt', 'r', encoding='utf-8')
# 2. 读写文件 文件对象.read(n)  n 一次读取多少字节的内容,默认不写,读取全部内容
buf = f.read(3)
print(buf)  # 123
print('-'*30)
buf = f.read(3)  #继续上次读取的往下读,4\n5
print(buf)
# 3. 关闭文件
f.close()
```

## 按行读取

```python
f = open('a.txt', 'r', encoding='utf-8')
# f.readline()  # 一次读取一行的内容, 返回值是读取到的内容(str)
# buf = f.readline()

# f.readlines()  # 按行读取,一次读取所有行,返回值是列表, 列表中的每一项是一个字符串,即一行的内容
buf = f.readlines()
print(buf)
buf = [i.strip() for i in buf]  #strip去掉字符串前后的空格和换行
print(buf)
f.close()

```

## 模拟读取大文件

```python
f = open('a.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf:  # if len(buf) > 0   容器,可以直接作为判断条件,容器中有内容,为True,没有数据是False
        print(buf, end='')
    else:
        # 文件读完了
        break

f.close()
```

```python
f = open('b.txt', 'r', encoding='utf-8')
while True:
    buf = f.read(5)  # f.read(4096)
    if buf:
        # print(buf, end='')
        print(buf)
    else:
        break

f.close()
```

# 文件打开模式

文本文件: txt, .py .md  能够使用记事本打开的文件
二进制文件: 具有特殊格式的文件, mp3 mp4 rmvb avi png jpg 等

文本文件可以使用 文本方式打开文件,也可以使用二进制的方式打开文件

二进制文件,只能使用二进制的方式打开文件
二进制打开方式如下: 不管读取,还是书写,都需要使用二进制的数据
rb wb  ab
注意点: 不能指定 encoding 参数

```python
f = open('c.txt', 'wb')
f.write('你好'.encode())   # encode() 将str 转换为二进制格式的字符串
f.close()


f1 = open('c.txt', 'rb')
buf = f1.read()
print(buf)
print(buf.decode())
f1.close()
```
| 访问模式 | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| r        | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| w        | 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| a        | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| rb       | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
| wb       | 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| ab       | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| r+       | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| w+       | 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| a+       | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| rb+      | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| wb+      | 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 |
| ab+      | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

# 文件备份

1. 用只读的方式,打开文件
2. 读取文件内容
3. 关闭文件
4. 只写的方式,打开新文件
5. 将 第 2 步读取的内容写入新文件
6. 关闭新文件

思考:
    1. 如果文件比较大,循环读取文件
    2. 复制备份的文件可能是 txt 文件,可能是 二进制文件,  使用二进制方式打开文件较好

```python
# 1. 用只读的方式,打开文件
f = open('a.txt', 'rb')
# 2. 读取文件内容
buf = f.read()
# 3. 关闭文件
f.close()
# 4. 只写的方式,打开新文件
f_w = open('a[备份].txt', 'wb')
# 5. 将 第 2 步读取的内容写入新文件
f_w.write(buf)
# 6. 关闭新文件
f_w.close()
```

优化:

```python
file_name = input('请输入要备份的文件名')

# 1. 用只读的方式,打开文件
f = open(file_name, 'rb')
# 2. 读取文件内容
buf = f.read()
# 3. 关闭文件
f.close()

# 根据原文件名,找到文件后缀和文件名
index = file_name.rfind('.')
# 后缀  file_name[index: ]
# 新文件名
new_file_name = file_name[:index] + '[备份]' + file_name[index:]
print(new_file_name)
# 4. 只写的方式,打开新文件
f_w = open(new_file_name, 'wb')
# 5. 将 第 2 步读取的内容写入新文件
f_w.write(buf)
# 6. 关闭新文件
f_w.close()
```

# 文件和文件夹的操作

```python
# 对文件和目录的操作,需要导入 os 模块
import os

# 1. 文件重命名 os.rename(原文件路径名, 新文件路径名)
# os.rename('a.txt', 'aa.txt')
# 2. 删除文件 os.remove(文件的路径名)
# os.remove('aa.txt')
# 3. 创建目录 os.mkdir(目录路径名)  make directory
# os.mkdir('test')
# os.mkdir('test/aa')

# 4. 删除指定path的空目录  os.rmdir('path')  remove directory
# os.rmdir('test/aa')
# 5. 获取当前所在的目录 os.getcwd()  get current working directory
buf = os.getcwd()
print(buf)
# 6. 修改当前的目录 os.chdir(目录名)  change dir
os.chdir('test')
buf = os.getcwd()
print(buf)
# 7. 获取指定目录中的内容,  os.listdir(目录), 默认不写参数,是获取当前目录中的内容
# 返回值是列表, 列表中的每一项是文件名
buf = os.listdir()   # test
print(buf)
```

## 应用-批量修改文件名

```python
import os


def create_files():
    for i in range(10):
        file_name = 'test/file_' + str(i) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()


def create_files_1():
    os.chdir('test')
    for i in range(10, 20):
        file_name = 'file_' + str(i) + '.txt'
        print(file_name)
        f = open(file_name, 'w')
        f.close()
    os.chdir('../')  # ../ 上一级目录


def modify_filename():
    os.chdir('test')
    buf_list = os.listdir()
    # print(buf_list)
    for file in buf_list:
        new_file = 'py43_' + file
        os.rename(file, new_file)

    os.chdir('../')


def modify_filename_1():
    os.chdir('test')
    buf_list = os.listdir()
    # print(buf_list)
    for file in buf_list:
        num = len('py43_')
        new_file = file[num:]
        os.rename(file, new_file)

    os.chdir('../')


# create_files()
# create_files_1()
# modify_filename()
modify_filename_1()

```

# 学生管理系统文件版

```python
def save():
    # 1. 打开文件
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()
```

```python
def load_file():
    global stu_list
    if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()
```

