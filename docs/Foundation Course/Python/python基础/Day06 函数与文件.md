# 递归函数

递归: 函数自己嵌套调用自己.

递归函数的形成条件:
1.  函数自己调用自己
2. 函数必须有一个终止条件

> 已知：A 比 B 大 2 岁，B比 C 大 2 岁，... , F 年龄为 18 岁，
> 求 A 的年龄。
> 知道第一个人的年龄是 18 岁
> 后边每个人比前边那个人大 2 岁
> 后边一个人的年龄 = 前边那个人的年龄 + 2
> num = (num -1) + 2

| A（6） | B（5） | C（4） | D（3） | E（2） | F（1） |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 28     | 26     | 24     | 22     | 20     | 18     |

```python
def get_age(num):
    """
    求第 num 个人的年龄,每相邻的两个人的年龄差两岁, 已知第一个人的年龄是 18岁
    :param num:
    :return:
    """
    if num == 1:
        return 18
    # 求第 num个人的年龄,只需要num-1 这个人的年龄 + 2
    age = get_age(num-1) + 2
    return age


print(get_age(4))
```

## 应用:求阶乘

```python
def func(n):
    num = 1
    for i in range(1, n + 1):
        num = num * i

    print(num)


def func2(n):
    if n == 1:
        return 1
    # 想要求 n! , 只需要(n-1)! * n
    num = func2(n-1) * n
    return num
```

# 匿名函数lambda

使用 `lambda` 关键字定义的函数就是匿名函数

lambda 参数列表：表达式

1.  无参数无返回值
    
    def 函数名()：  
      函数代码  
    ​  
    lambda:函数代码
    
2.  无参数有返回值
    
    def 函数名()：  
        return 1 + 2  
    ​  
    lambda: 1 + 2
    
3.  有参数无返回值
    
    def 函数名(a, b):  
      print(a, b)  
    
    lambda a, b: print(a, b)
       
4.  有参数有返回值
    
    def 函数名(a, b):  
      return a + b  
    ​ 
    lambda a, b: a + b
    

```python
# 1. 无参无返回值
def func1():
    print('hello')


(lambda: print('hello lambda'))()
func1()
f1 = lambda: print('hello lambda')
f1()


# 2. 无参有返回值
def func2():
    return 1 + 2


f2 = lambda: 1 + 2
print(f2())


# 3. 有参无返回值
def func3(name):
    print(name)


f3 = lambda name: print(name)
f3('hwllo')


# 4. 有参有返回值
def func4(*args):
    return args


f4 = lambda *args: args
print(f4(1, 2, 3, 4, 5))
```

## 匿名函数的使用

**匿名函数的应用场景 -- 作为函数的参数使用**

```python
def my_calc(a, b, func):
    """
    进行四则运算
    :param a: 第一个数据
    :param b: 第二个数据
    :param func: 函数,要进行的运算
    :return: 运算的结果
    """
    print('其他的函数代码...')
    num = func(a, b)
    print(num)


def add(a, b):
    return a + b


# 调用
my_calc(10, 20, add)
my_calc(10, 20, lambda a, b: a - b)
my_calc(10, 20, lambda a, b: a * b)
my_calc(10, 20, lambda a, b: a / b)
```

## 列表中字典排序

**lambda 函数作为函数参数(列表中字典排序)(扩展)**

list1 = [{'name': 'd', 'age': 19}, {'name': 'b', 'age': 16}, {'name': 'a', 'age': 16}, {'name': 'c', 'age': 20}]  

```python
# 列表排序, 列表中的数据的类型要保持一致
my_list = [1, 3, 5, 4, 2, 1]
my_list.sort()
print(my_list)

list1 = [{'name': 'd', 'age': 19},
         {'name': 'b', 'age': 16},
         {'name': 'a', 'age': 16},
         {'name': 'c', 'age': 20}]

# list1.sort()  # 程序报错,列表中类型为字典,字典未定义如何比较大小
# 匿名函数的形参是列表中的每一个数据
list1.sort(key=lambda x: x['name'])
print(list1)
list1.sort(key=lambda x: x['age'])
print(list1)

list2 = ['aghdd', 'bc', 'ghlj', 'def', 'ab']
list2.sort()
# print(list2)
# 需求: 根据列表中字符串的长度对列表进行排序
# list2.sort(key=len)
list2.sort(key=lambda x: len(x))
print(list2)

# sort(key= lambda 形参: (排序规则1, 排序规则2, ...))
# 当第一个规则相同,会按照第二个规则排序

# list1.sort(key=lambda x: (x['age'], x['name']))
# list1.sort(key=lambda x: (x['age'], x['name']), reverse=True)
# print(list1)
```

```
[1, 1, 2, 3, 4, 5]
[{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'c', 'age': 20}, {'name': 'd', 'age': 19}]
[{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'd', 'age': 19}, {'name': 'c', 'age': 20}]
['ab', 'bc', 'def', 'ghlj', 'aghdd']

```

# 集合 set

```python
# 集合 set 定义使用 {}  , {数据, 数据}
# 1. 集合中的数据必须是不可变类型
my_set = {1, 3.14, False, 'hello', (1, 2)}
print(my_set, type(my_set))
# my_set = {[1, 2]}   # 代码报错
# 2. 集合是可变类型
my_set.remove(3.14)
print(my_set)
my_set.pop()
print(my_set)
print('----')
my_set.add(100)
print(my_set)
# 修改数据 100 ---> 200
my_set.remove(100)
my_set.add(200)
print(my_set)
my_set.clear()
print(my_set)   #
# 3. 集合是无序的,(数据的添加顺序和输出顺序是否一致), 不支持下标操作
# 4. 集合中的数据没有重复数据(去重)
my_list = [1, 2, 3, 4, 2, 5, 1, 0]
my_list = list(set(my_list))
print(my_list)
# 集合, 列表, 元组 三者之间可以互相转换
```

```
{False, 1, (1, 2), 3.14, 'hello'} <class 'set'>
{False, 1, (1, 2), 'hello'}
{1, (1, 2), 'hello'}
----
{1, (1, 2), 100, 'hello'}
{1, (1, 2), 200, 'hello'}
set()
[0, 1, 2, 3, 4, 5]

```

# 文件操作

文件的作用: 可以永久的保存数据.
文件在硬盘中存储的格式是二进制.
1.  打开文件 
2.  读写文件  
3.  关闭文件

## 读文件-r

```python
# 1. 打开文件, 是文件从硬盘中存到内存中
# open(file, mode='r',  encoding)
# file 要操作的文件名字, 类型是 str
# mode, 文件打开的方式, r(read) 只读打开, w(write) 只写打开  a(append) 追加打开
# encoding  文件的编码格式, 常见的编码格式有两种, 一种是gbk, 一种是utf-8
# 返回值:文件对象, 后续所有的文件操作,都需要通过这个文件对象进行

# 以只读的方式打开当前目录中,1.txt 文件, 文件不存在会报错
f = open('1.txt', 'r')
# 2. 读文件 文件对象.read()
buf = f.read()
print(buf)
# 3. 关闭文件  文件.close()  将内存中三大文件同步到硬盘中
f.close()
```

## 写文件-w

```python
# 1. 打开文件 w 方式打开文件,文件不存在,会创建文件, 文件存在,会覆盖清空原文件
f = open('a.txt', 'w', encoding='utf-8')
# 2. 写文件 文件对象.write(写入文件的内容)
f.write('hello world!\n')
f.write('hello python!\n')
f.write('你好,中国!')
# 3. 关闭文件
f.close()
```

注:
1.open函数打开文件，没有指定文件的编码，windows默认是gbk 
2.write函数将你好，中国写入文件中，使用gbk编码写入
3.在pycharm中双击打开文件，默认使用的编码是utf-8.

使用utf-8编码打开gtk编码的数据，出现乱码
编码：就是如何将中文汉字变为二进制。或者如何将二达制转换为汉字

解决方案：是两种方式的编码统一即可
方案一：open打开文件的时候，指定使用utf-8打开
方案二：pycharm中使用gbk的方式打开

## 追加文件-a

```python
# a 方式打开文件, 追加内容,在文件的末尾写入内容
# 文件不存在,会创建文件
# 注意点: 不管是a 方式打开文件,还是 w 方式打开文件,写内容,都是使用 write()函数
f = open('b.txt', 'a', encoding='utf-8')
# f.write('hello world!\n')
f.write('111\n')
f.close()
```