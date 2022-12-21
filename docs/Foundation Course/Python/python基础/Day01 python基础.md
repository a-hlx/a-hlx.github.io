# 绪论

## 基础知识

### 计算机的组成
-   硬件系统
    -   主机部分
        -   CPU (中央处理器)
        -   内存(4G, 8G, 16G 32G 64G)
    -   外设部分       
        -   输入设备  
        -   输出设备                        
        -   外存储器            
            -   硬盘              
-   软件系统
    -   系统软件
        -   `操作系统: 控制硬件运行, 支持其他软件运行`
    -   应用软件

计算机最小的单位是 bit(位),  0 或 1 
字节: 是计算机中基本的储存单位 byte 

```
1 byte = 8 bit
1KB = 1024 byte
1MB = 1024 KB
1GB = 1024 MB
1TB = 1024 GB
```


`解释型语言`:边解释边执行

编译型语言：将源代码编译成可执行程序（二进制代码程序.exe）

Python 3.X：python 解释器。

PyCharm：IDE(集成开发环境)，集成了代码书写、运行、调试等功能。

（1）记事本书写

打开 cmd 窗口, 执行代码python +文件名.py

（2）注释

-   单行注释的快捷键/取消单行注释（`Ctrl /`），可以一次选中多行，给其添加单行注释。
- 3个单或双引号多行注释。

## 数据类型

数据类型: int(整型) float(浮点型) complex(复数) string(字符串类型) bool(布尔类型, True False) list(列表) tuple(元组)  dictionary(字典) 

```python
int(1.9)
1
int(-1.9)
-1
```

    type() 函数可以查看变量的数据类型
    
```python
result=True
print(type(result))

```

## 标识符和关键词
`标识符命名规则：由字母、数字和下划线组成，不能以数字开头。`

```python
import keyword
print(keyword.kwlist)

```
或者
```python
help("keywords")
```

```
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not 
```

## Debug 调试

> 1.  可以查看代码的执行过程   
> 2.  可以排查错误 

步骤:
1.  打断点(一般可以在代码的开始打上断点,或者在查看代码的地方打断点)   
2.  右键 debug 运行代码
3.  点击 下一步, 查看代码执行的过程

## print函数的sep

```python
print(1)
print(1, 2)  # 默认中间加空格，step默认空格
print(1, 2, 3)
print(1, 2, 3, 4)
print(1, 2, 3, 4, 5)

print(1)
print(1, 2, sep='*')
print(1, 2, 3, sep='_*_')
print(1, 2, 3, 4, sep='hello')
print(1, 2, 3, 4, 5, sep=' ')  # 默认

```

## PEP 8 规范

1.  单行注释后边应该有一个空格
2.  行内注释需要两个空格
3. Ctrl+Alt+L快速格式化
4. 类定义的前后需要两空行

## 积累

除randint，区间都是向前覆盖，不包括最后

栈是一种先进后出的数据结构，类似我们生活中挤电梯，最后进入的肯定是先出来

队列是一种先进先出的数据结构，类似食堂排队打饭，先入队的元素当然要先出队

## 输出
```python
# 在python中的输出使用print函数  
# 基本输出  
print('hello')   # 会输出 hello  
print(123)   # 会输出 123  
  
# 一次输出多个内容  
print('isaac', 18)  # 会输出 isaac 和18 ,两者之间使用 空格隔开  
  
# 可以书写表达式  
print(1 + 2)  # 会输出 1 +2 的结果 3  
```

### 多行输出

```python
# 将字符串存入变量  
str1 = 'Hello World!'  
str2 = 'Hello Nowcoder!'  
  
# 换行输出  
# 输出1：多个print  
# print(str1)  
# print(str2)  
  
# 输出2：sep参数  
# print(str1, str2, sep=("\n"))  
  
# 输出3：字符串拼接加\n  
print(str1 + "\n" + str2)
```

### 格式化输出
%s 字符串       %d int 整数int                %f  小数浮点数float

`python3.6版本开始支持 f-string ,占位统一使用 {} 占位,填充的数据直接写在 {} 里边`  

```python
print(f"我的名字是{name},年龄是{age}岁, 身高是{height}cm") 
``` 

```python
num = 3.14

print("%.3f" % num)
# f"{变量:.nf}"
print(f"{num:.3f}")
num1 = 1   
print('%6d' % num1)   #     1
print('%06d' % num1)  #000001
print(f'{num1:06d}')
```

```python
# 格式化输出, 格式化占位符(坑位), %s 字符串 %d int 整数int  %f  小数浮点数float  
name = 'isaac'  
# 需求: 输出 我的名字是xxx,我很开心  
print("我的名字是%s,我很开心." % name)  
  
age = 18  
# 需求: 输出 我的年龄是18岁  
print('我的年龄是%d岁' % age)  
  
height = 170.5  
# %f 输出小数,默认保留6位小数  
print('我的身高是%f cm' % height)  # Ctrl d 快速的复制一行代码, shift enter  在下方新建一行代码  
# %.nf  保留n 位小数  
print('我的身高是%.1f cm' % height)  
print('我的身高是%.2f cm' % height)  
  
# 需求: 我的名字是xx,年龄是xx岁, 身高是xxcm  
print('我的名字是%s,年龄是%d岁, 身高是%fcm' % (name, age, height))  
  
# 输出50%, 使用格式化输出的时候,想要输出一个%, 需要使用两个%  
print('及格人数占比为%d%%' % 50)  

# 输出0123
num = 123
print('%04d' % num)

# zfill()函数

n = "123"  
s = n.zfill(5)  #00123

n = '-123'  
s = n.zfill(5)  
assert s == '-0123'
#Python assert（**断言**）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
```


 ```
# 转义字符 \n  将\和n组合在一块,作为一个字符使用, \n 代表换行  
# print()函数输出之后,默认会添加一个换行, 如果不想要这个换行可以去掉  
print('hello', end=' ')  # hello world
print('hello', end='_*_')  # hello_*_world
print('hello', end='')  # helloworld
print('world')  
print('good good study\nday day up')
 ```

#### 大小写

 .lower() --- 全部小写
 .upper() --- 全部大写
 .title() --- 各个字符的首字母大写
 .capitalize() --- 首字母大写

```python
current_users = ["Niuniu", "Niumei", "GURR", "LOLO"]
new_users = ["GurR", "Niu Ke Le", "LoLo", "Tuo Rui Chi"]
current_users1 = [i.lower() for i in current_users]
for i in new_users:
    if i.lower() in current_users1:
        print(
            "The user name "
            + i
            + " has already been registered! Please change it and try again!"
        )
    else:
        print("Congratulations, the user name " + i + " is available!")
```

#### format

 str.format()，它增强了字符串格式化的功能。
 [Python format 格式化函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python/att-string-format.html)

```python
>>>"{} {}".format("hello", "world") # 不设置指定位置，按默认顺序 'hello world'
>>>"{0} {1}".format("hello", "world") # 设置指定位置 'hello world'
>>>"{1} {0} {1}".format("hello", "world") # 设置指定位置 'world hello world'
```

#### 去空格

.strip() --- 删除两边空格
 .lstrip() --- 删除左边空格
 .rstrip() --- 删除右边空格
 .replace(" ","") --- 删除所有空格
 .split() --- 先切分，.join() --- 再拼接

#### 四舍五入round（）

```python
round(80.23456, 2) :  80.23
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
```

#### 绝对值abs()

#### ASCII码ord()

#### 常用的格式符号

| 格式符号 | 转换 |
| -------- | ---- |
|%c|字符
|%s|通过str() 字符串转换来格式化
|%i|有符号十进制整数
|%d|有符号十进制整数
|%u|无符号十进制整数
|%o|八进制整数
|%x|十六进制整数（小写字母）
|%|X十六进制整数（大写字母）
|%e|索引符号（小写'e'）
|%E|索引符号（大写“E”）
|%f|浮点实数
|%g|％f和％e 的简写
|%G|％f和％E的简写

## 输入
 输入: 从键盘获取输入的内容,存入计算机程序中  
在python中使用的是 input()函数  
input('给用户的提示信息'), 得到用户输入的内容, 遇到回车代表输入结束, 得到的数据都是`字符串`类型    

```python 
password = input('请输入密码:')  
print('你输入的密码是 %s' % password)
```

### 输入多个参数

```python
print("请输入方程的系数：")
    # a,b,c,d代表所求方程的系数
a, b, c, d = map(float, input().split())
print("方程的参数为：" , a, b, c, d)
```

### map()函数

map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map(function, iterable, ...)

参数
-   function -- 函数
-   iterable -- 一个或多个序列

```python
def square(x) :         # 计算平方数
    return x ** 2
map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
# map object at 0x100d3d550     # 返回迭代器
list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
# [1, 4, 9, 16, 25]
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]


x,y=map(int,input().split())
print(x**y,y**x,sep='\n')

```

```python
class Coordinate:
    def __init__(self, x, y=None) -> None:  # 重载 __init__ 函数
        self.x, self.y = list(map(int, x.split())) if y is None else [int(x), int(y)]
        pass 
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
        pass
    def __add__(self, coor) -> None:
        return Coordinate(self.x + coor.x, self.y + coor.y)
        pass

c1 = Coordinate(input())
c2 = Coordinate(input())
print(c1 + c2)
```

## 类型转换
```python
# 1. 使用input函数获取苹果的价格  
price = input('请输入苹果价格:')  # str  
# 2. 使用input函数获取购买的重量  
weight = input('请输入重量:')  # str  
# 3. 输出想要的结果  
result = float(price) * float(weight)  # 类型转换  
print(f'苹果单价为{price}元/斤,购买了{weight}斤, 需要支付{result}元')  
  
# 类型转换,将原始数据转换为我们需要的数据类型,在这个过程中,不会改变原始的数据,会生成一个新的数据  
# 1. 转换为int类型  int(原始数据)  
# 1.1 float类型的数据 转换为int  
pi = 3.14  
num = int(3.14)  
# print(type(pi))   # float  
# print(type(num))  # int  
  
# 1.2 整数类型的字符串, "10"  
my_str = '10'  
num1 = int(my_str)  
# print(type(my_str))  # str  
# print(type(num1))  # int  
  
# 2. 转换为 float类型 float()  
# 2.1 int ---> float  
num2 = 10  
num3 = float(num2)  
# print(type(num2))  # int  
# print(type(num3))  # float  
  
# 2.2 将数字类型字符串转换为 float  "10"  "3.14"  
num4 = float("3.14")  
num5 = float("10")  
# print(type(num4))  # float  
# print(type(num5))  # float  
  
# eval()  还原原来的数据类型,  去掉字符串的引号  
num6 = eval('100')  # 100 int  
num7 = eval('3.14')  # 3.14 float  
print(type(num6))  
print(type(num7))  
  
num8 = eval('num7')  # num7  是已经定义好的变量,可以使用,不会报错  
print(num8, type(num8))  
# num8 = eval('hello')   # 代码报错,hello 变量没有定义,不能使用
```

## bool类型

False,None

只有空字符串、序列和集合为False,其他都为True

直有等值为0的结果为False,如bool(0),bool(0.0),bool(0j)，bool(Decimal(0)),bool(Fraction(0,1))

## 常用的数据类型转换
常见的[类型转换](https://so.csdn.net/so/search?q=%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2&spm=1001.2101.3001.7020)函数如下所示：

| 函数| 描述 |
|-----|---|
| int(x, [base]) |将 x 转换成一个整数
|float(x)|将 x 转换成一个浮点数
|complex(real[,imag])|创建一个复数
|str(x)|将对象 x 转换成字符串
|repr(x)|将对象 x 转换为表达式字符串
|eval(str)|用来计算在字符串中的有效 Python 表达式，并返回一个对象
|tuple(s)|将序列 s 转换为一个元组
|list(s)|将序列 s 转换为一个列表
|set(s)|将序列 s 转换为可变集合
|dict(d)|创建一个字典。d 必须是一个序列 (key, value) 元组
|frozenset(s)|转换为不可变集合
|chr(x)|将一个整数转换为一个 Unicode 字符
|ord(x)|将一个 Unicode 字符转换为它的整数值
|hex(x)|将一个整数转换为一个十六进制字符串
|oct(x)|将一个整数转换为一个八进制字符串
|bin(x)|将一个整数转换为一个二进制字符串

## 进制转换

 **int(x,base)函数，其中不给base赋值，默认为10**
```python
使用int()函数，第一个参数是要转换的数字，类型为字符串，第二个参数是该数几进制的数，转化结果为一个十进制的数。  
  二进制转十进制：  
 　　 >>> int('0b1111',2)  
  　　15  
  八进制转十进制：  
  　　>>> int('67',8)  
  　　55  
 十六进制转十进制：  
  　　>>> int('0x1f',16)  
  　　31
```

## 运算符
## 算术运算符
| 运算符   | 描述      | 实例         |
| -------- | -------| ------------ |
| //       | 取整除                                                         | 返回除法的整数部分（商） 9 // 2 输出结果 4 |
| % | 取余数     |  返回除法的余数 9 % 2 = 1            |
| **     | 幂        |  又称次方、乘方，2 ** 3 = 8            |

==eN==: 10的N次方
1e2 =1 * 10^2 =100

```
import math
math.exp( x )
```

> 注意：混合运算时，优先级顺序为： `**` 高于 `*` `/` `%` `//` 高于 `+` `-` ，为了避免歧义，建议使用 `()` 来处理[运算符](https://so.csdn.net/so/search?q=%E8%BF%90%E7%AE%97%E7%AC%A6&spm=1001.2101.3001.7020)优先级。
> 
> 并且，不同类型的数字在进行混合运算时，整数将会转换成浮点数进行运算。

```python
def Add_Sub(x,y):
    sum = x+y
    substract = x - y
    return sum,substract

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    sum,substract = Add_Sub(x,y)
    print(sum,substract,sep='\n')
```

## 赋值运算符

> =：将等号右边的结果 赋值给 等号左边的变量。等号左边，必须是变量，不能是具体的数字。

### 复合赋值运算符
```html
| 运算符 | 描述           | 实例                      |
| :----- | :------------- | :------------------------ |
| +=     | 加法赋值运算符 | a += b 等价于 a = a + b   |
| -=     | 减法赋值运算符 | a -= b 等价于 a = a - b   |
| *=     | 乘法赋值运算符 | a *= b 等价于 a = a * b   |
| /=     | 除法赋值运算符 | a /= b 等价于 a = a / b   |
| //=    | 整除赋值运算符 | a //= b 等价于 a = a // b |
| %=     | 取余赋值运算符 | a %= b 等价于 a = a % b   |
| **=    | 幂赋值运算符   | a **= b 等价于 a = a ** b |
```

## 比较运算符
 比较运算符的结果是 bool 类型，即 True，或者是 False。

| 比较运算符 | 描述                                                        | 例     |
| :--------: | :---------------------------------------------------------- | :----- |
|     ==     | 如果两个操作数相等，则返回True，否则返回False。             | a == b |
|    ！=     | 如果两个操作数不相等，则返回True，否则返回False。           | a！= b |
|     >      | 如果左操作数大于右操作数，则返回True，否则返回False。       | a> b   |
|     <      | 如果左操作数小于右操作数，则返回True，否则返回False。       | a <b   |
|    > =     | 如果左操作数大于或等于右操作数，则返回True，否则返回False。 | a> b   |
|     <=     | 如果左操作数小于或等于右操作数，则返回True，否则返回False。 | a <b   |

## 逻辑运算符

| 运算符 | 描述                                    | 实例                  | 试一试                                                                  |
|:------:|:--------------------------------------- |:--------------------- |:----------------------------------------------------------------------- |
|  and   | 如果两个语句都为真，则返回 True。       | x > 3 and x < 10      | [试一试](https://www.w3school.com.cn/tiy/t.asp?f=python_oper_logical_1) |
|   or   | 如果其中一个语句为真，则返回 True。     | x > 3 or x < 4        | [试一试](https://www.w3school.com.cn/tiy/t.asp?f=python_oper_logical_2) |
|  not   | 反转结果，如果结果为 true，则返回 False | not(x > 3 and x < 10) | [试一试](https://www.w3school.com.cn/tiy/t.asp?f=python_oper_logical_3) |

### 短路原则
and 和 or 遵从短路逻辑
3 and 4 为4,3 or 4 为3

## 二进制位运算

```python
x,y=[int(i) for i in input().split()]
print(x & y)  # 位与
print(x | y)  # 位或
```

```
输入：
1 2
输出：
0
3
说明：
1 = 0001，2 = 0010
0001 & 0010 = 0000 = 0
0001 ｜0010 = 0011 = 3
```

