# 异常

## 异常的概念

异常: 程序运行过程中,代码遇到错误,给出错误的提示

异常的组成:
异常类型: 异常具体的描述信息

## 捕获单个异常

异常: 程序代码在运行过程中遇到的错误, 程序会报错,会终止程序代码的运行.
异常捕获: 是指在程序代码运行过程中,遇到错误, 不让程序代码终止,让其继续运行, 同时可以给使用者一个提示信息
并记录这个错误, 便于后期改进

ry:
    可能发生异常的代码
except 异常的类型:
    发生异常执行的代码

```python
print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    num = 10 / int(num)
    print('计算得到的结果是:', num)
except ZeroDivisionError:
    print('你输入有误,请再次输入')

print('其他的代码......')
```

## 捕获多个异常

try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    发生异常执行的代码

try:
    可能发生异常的代码
except 异常类型1:
    发生异常1,执行的代码
except 异常类型2:
    发生异常2,执行的代码
except ...:
    pass

```python
print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
except ZeroDivisionError:
    print('你输入有误,请再次输入')
except ValueError:
    print('输入有误,请输入数字')

print('其他的代码......')

```

## 打印异常信息

try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量名:
    发生异常执行的代码
    print(变量名)

```python
print('其他的代码......')
num = input('请输入一个数字:')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'
try:
    a = int(num)
    num = 10 / a
    print('计算得到的结果是:', num)
except (ZeroDivisionError, ValueError) as e:
    print('你输入有误,请再次输入', e)

print('其他的代码......')
```

```python
其他的代码......
请输入一个数字:0
你输入有误,请再次输入 division by zero
其他的代码......
```

## 捕获所有的异常

try:
    可能发生异常的代码
except:   # 缺点, 不能获取异常的描述信息
    发生异常执行的代码

==============
try:
    可能发生异常的代码
except Exception as e:
    发生异常执行的代码
    print(e)
    pass

Exception 是常见异常类的父类,
ZeroDivisionError --> ArithmeticError --> Exception --> BaseException  ---> object
ValueError --> Exception --> BaseException  ---> object

## 异常的完整结构

try:
    可能发生异常的代码
except Exception as e:
    发生异常执行的代码
    print(e)
else:
    代码没有发生异常,会执行
finally:
    不管有没有发生异常,都会执行

## 异常的传递

是 python 异常处理的底层机制,是原理层面上的,不需要我们自己写代码实现,是 python 已经实现好的.

异常传递: 当一行代码发生异常之后,会向外层将这个异常进行传递,指导被捕获或者程序报错为止.
1. try 嵌套
2. 函数嵌套

**内层try代码中发生的异常,未被捕获会向外层传递**

```python
print('其他的功能代码.....')
num = input('请输入数字:')
try:
    try:
        a = int(num)  # ValueError
    except ZeroDivisionError:
        print('发生异常')
    finally:
        print('我都执行了....')

    num = 10 / a
    print(f'计算的结果<<{num}>>')
except Exception as e:
    print(e)


print('其他的功能代码.....')
```

```python
def func1():
    print('-------1---------')
    num = input('请输入数字')  # 0
    num = 10 / int(num)  # 假设0 是计算的出来的
    print(num)
    print('-------2---------')


def func2():
    print('-------3---------')
    func1()
    print('-------4---------')


try:
    print('-------5---------')
    func2()
    print('-------6---------')
except Exception as e:
    print('-------7---------')
    print(e)
```

```python
-------5---------
-------3---------
-------1---------
请输入数字0
-------7---------
division by zero
```

## 抛出自定义异常

程序代码为什么会报错?
因为不符合语法, 因为 python 的作者在代码中使用了 if 判断,如果除数为 0 ,就会在代码中抛出异常错误,
抛出异常:
    raise 异常对象  # 当程序代码遇到 raise 的时候,程序就报错了
    
异常对象 = 异常类(参数)  

抛出自定义异常:
    1. 自定义异常类,继承 Exception 或者 BaseException 
    2. 选择书写,定义 __init__方法,定义__str__ 方法
    3. 在合适的时机抛出异常对象即可

```python
# 1. 定义异常类, 密码长度不足的异常
class PasswordLengthError(Exception):
    # def __str__(self):
    #     return 'xxxxxx'
    pass


def get_password():  # 等同于系统定义函数
    password = input('请输入密码:')
    if len(password) >= 8:
        print('密码长度合格')
    else:
        # 抛出异常
        raise PasswordLengthError('密码长度不足8位')
        # print('密码长度不足8位')

try:
    get_password()  # 调用系统的函数
except PasswordLengthError as e:
    print(e)

print('其他代码.....')

```

```python
请输入密码:123
密码长度不足8位
其他代码.....
```

# 模块

import random
random.randint(a, b)  产生[a,b] 之间的随机整数, 包含 b
import os
 
python 就是一个 python 代码文件,是别人已经写好的代码文件,文件中的函数类以及变量,我们都可以使用.

使用模块的好处:  直接使用别人已经实现好的功能,

## 模块的制作

模块就是一个 python 文件
制作一个模块,其实就是定义一个 python 代码文件
注意点: 模块的名字要遵循标识符的规则(由字母,数字和下划线组成,不能以数字开头)
模块中可以定义变量,定义函数,定义类

## 模块的导入

想要使用模块中的内容,必须先导入模块 
注意点: 如果导入的是自己书写的模块,使用的模块和代码文件需要在一个目录中

```python
# 想要使用模块中的内容,必须先导入模块
# 方法一  import 模块名
# 使用:  模块名.功能名
import my_module1
print(my_module1.num)  # 使用my_module1中的变量num
my_module1.func()   # 调用my_module1中 func函数
dog = my_module1.Dog()  # 调用my_module1中的类创建对象
dog.show_info()

# 方法二  from 模块名 import 功能名1, 功能名2, ....
# 使用: 功能名
# 注意点: 如果存在同名的方法名,则会被覆盖
from my_module2 import func, num #2
from my_module1 import num  #1
func()
print(num)  #1

# 方法三  from 模块名 import *   # 将模块中所有的功能进行导入
# 使用: 功能名
from my_module2 import *
print(num)
func()
dog = Dog()
dog.show_info()

```

### as 起别名
可以对模块和功能起别名,
注意: 如果使用as别名,就不能再使用原来的名字
```python
import my_module1 as mm1
from my_module1 import func as m1_func
from my_module2 import func as m2_func
mm1.func()
m1_func()
m2_func()
```

## 模块中的变量 `__all__`

`__all__`变量,可以在每个代码文件中(模块中)定义, 类型可以是元组或者列表
作用: 影响 form 模块名 import * 导入行为,另外两种导入行为不受影响
1. 如果没有定义__all__ 变量, 模块中的所有功能,都可以被导入
2. 如果定义__all__ 变量,只能导入 变量中定义的内容

## 模块中的变量 `__name__`

```python
def add(a, b):
    print(a + b)


if __name__ == '__main__':
    add(10, 20)
    # __name__ 变量,在每个模块即代码文件中都有,是系统自己定义的
    # 1. 直接运行当前代码, 值为 __main__
    # 2. 把文件作为模块导入时,运行,结果是 my_calc(文件名)
    print(__name__)
```

## 模块的注意点

自己定义的模块名字,不要和系统中你要使用的模块名字相同

import sys
模块的搜索顺序, 当前目录  ---> 系统目录 ---> 程序报错
print(sys.path)

# 包

包: 功能相近或者相似的模块放在一个目录中,并在目录中定义一个 `__init__.py` 文件,这个目录就是包

```python
# 方法一  import 包名.模块名
import my_package.my_module1
import my_package.my_module2 as mm2

my_package.my_module1.func()
mm2.func()

# 方法2  from 包名.模块名 import 功能名
from my_package.my_module1 import func
from my_package.my_module2 import *
func()

# 方法三 from 包名 import *  # 导入的是__init__.py中的内容
from my_package import *
func()
```

# 学生管理系统-面向对象版

1. 一个类作为一个 python 文件 
2. 定义一个 main.py 作为程序代码的启动文件

=====
代码文件的组成:
    student.py   # 定义 Student 类
    student_manager_system.py  # 定义管理系统类
    main.py  # 作为程序的启动代码

```python
class Student(object):
    def __init__(self, stu_id, name, age, gender):
        self.stu_id = stu_id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.stu_id},{self.name},{self.age},{self.gender}"


if __name__ == '__main__':
    stu = Student(1, 'aa', 18, 'm')
    print(stu)
```

```python
import student


class StudentManagerSystem(object):
    def __init__(self):
        self.stu_dicts = {}

    @staticmethod
    def __show_menu():
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改学生信息')
        print('4. 查询单个学生信息')
        print('5. 查询所有的学生信息')
        print('6. 退出系统')

    def __insert_student(self):
        # 1. 使用 input 获取学生的信息
        stu_id = input('请输入学生学号:')
        # 代码优化, 判断学生信息是否存在, 学号是否存在. 判断字典的key是否存在
        if stu_id in self.stu_dicts:  # key存在返回True
            print('学生信息已经存在, 不需要再次添加.........')
            return
        name = input('请输入学生名字:')
        age = input('请输入学生年龄:')
        gender = input('请输入学生性别:')

        # 2. 使用学生信息,创建学生对象  学生类(参数)
        stu = student.Student(stu_id, name, age, gender)
        # 3. 将学生对象添加的字典中 字典['key'] = 数据值
        self.stu_dicts[stu_id] = stu

    def __remove_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 3. 存在进行操作, 删除字典中的数据,  del 变量[key]
            del self.stu_dicts[stu_id]
            print('学生已经删除')
        else:
            print('学生信息不存在,无法删除.....')

    def __modify_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 修改对象的属性  对象.属性名 = 属性值
            stu = self.stu_dicts[stu_id]  # 字典[key]
            stu.age = input('请输入新的年龄:')
            print('信息已经修改完毕.....')
        else:
            print('学生信息不存在,无法删除.....')

    def __search_student(self):
        # 1. 使用 input 输入学生学号
        stu_id = input('请输入学号:')
        # 2. 判断学生信息是否存在
        if stu_id in self.stu_dicts:
            # 修改对象的属性  对象.属性名 = 属性值
            stu = self.stu_dicts[stu_id]  # 字典[key]
            print(stu)
        else:
            print('学生信息不存在,无法删除.....')

    def __show_all_info(self):
        for stu in self.stu_dicts.values():
            print(stu)

    def __save(self):
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')  # str(stu) 调用 student类中的__str__ 方法
        f.close()

    def __load_info(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # 去重\n
                info_list = buf.split(',')  # 列表
                # 创建对象
                # stu = student.Student(info_list[0], info_list[1], info_list[2], info_list[3])
                stu = student.Student(*info_list)
                #  将对象添加到字典中
                stu_id = info_list[0]
                self.stu_dicts[stu_id] = stu
            f.close()
        except Exception:
            pass

    def start(self):
        self.__load_info()
        while True:
            self.__show_menu()
            opt = input('请输入用来选择的操作编号:')
            if opt == '1':
                # print('1. 添加学生')
                self.__insert_student()
            elif opt == '2':
                # print('2. 删除学生')
                self.__remove_student()
            elif opt == '3':
                # print('3. 修改学生信息')
                self.__modify_student()
            elif opt == '4':
                # print('4. 查询单个学生信息')
                self.__search_student()
            elif opt == '5':
                # print('5. 查询所有的学生信息')
                self.__show_all_info()
            elif opt == '6':
                self.__save()
                print('欢迎下次使用本系统......')
                break
            else:
                print('输入有误,请再次输入')
                continue

            input('...... 回车键继续操作.......')

```

```python
import student_manager_system as sms


if __name__ == '__main__':
    stu_sms = sms.StudentManagerSystem()
    stu_sms.start()
```

# 正则表达式

```python
# 匹配正则表达式匹配有多少位
# re.match()函数从字符串的开头开始匹配
# re.search()函数从任意位置开始匹配 
# re.compile()函数将规则编译后使用findall()函数匹配所有的结果
# re.sub(pattern,rep,string,max)函数用来替换符合的串
# match().span()返回匹配的字符串范围

# 1.常用方法：直接写逐位匹配记录长度
# while True:
#     try:
#         s = input()
#         s1 = 'https://www'
#         countNum = 0
#         for i in range(0,len(s1),1):
#             if s1[i] == s[i]:
#                 countNum += 1
#         print("(0, "+str(countNum)+')')
#     except:
#         break

# 2.使用自带函数库re的match()函数从开始匹配字符串，span()函数输出匹配的范围
import re
while True:
    try:
        print(re.match('https://www',input(),flags=True).span())
    except:
        break

```

re.IGNORECASE/re.I 区分大小写    
re.match函数尝试从字符串的开头开始匹配一个模式，如果匹配成功，返回一个匹配成功的对象，否则返回None。 

re.match(pattern, string, flags = 0)
pattern：匹配的正则表达式  
string：要匹配的字符串  
flags：标志位，用于控制正则表达式的匹配方式。如是否区分大小写、是否多行匹配等。  

正则表达式常见的几种函数:
1. re.match()函数 如果想要从源字符串的起始位置匹配一个模式  
2. re.search()函数 会扫描整个字符串并进行对应的匹配。  
 该函数与re.match()函数最大的不同是，re.match()函数从源字符串的开头进行匹配，而re.search()函数会在全文中进行检索匹配。  
3. re.compile()  在以上两个函数中，即便源字符串中有多个结果符合模式，也只会匹配一个结果，那么我们如何将符合模式的内容全部都匹配出来呢？

```python
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")#预编译
result = pattern.findall(string)#找出符合模式的所有结果
```

4. re.sub(pattern,rep,string,max) 如果，想根据正则表达式来实现替换某些字符串的功能，我们可以使用re.sub()函数来实现。

```python
# 清理电话簿
# 1.使用findall()函数找出所有数字后拼接成新的字符串
import re
# while True:
#     try:
#         print(''.join(re.findall(r'\d',input())))
#     except:
#         break

# 2.使用re.sub()替换函数
while True:
    try:
        s = input()
        print(re.sub('[a-z]+|[A-Z]+|-','',s,flags=False))
    except:
        break


# [\d]=[0-9]  但是\d与|搭配使用的时候可以没有+号，0-9格式的时候必须加上+
# 当出现多个匹配条件的时候，需要将条件都列出来，比如:[0-9|-]+ 表示数字或者-符号可以出现一次或者多次，
# [a-z+|A-Z+|0-9+|-]+表示中括号里面的内容可能出现一次或者多次，中间使用|分隔
# [a-z]+|[A-Z]+|-分开方便表示各种情况可能出现的次数

import re
s = input()
r = re.match('[0-9-]+',s)
print(r.group())
```