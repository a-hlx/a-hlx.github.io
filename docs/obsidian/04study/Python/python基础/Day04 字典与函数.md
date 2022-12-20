# 字典
## 字典的定义和访问
字典 dict 定义使用{} 定义, 是由键值对组成(key-value)
变量 = {key1: value1, key2:value2, ...}  一个key:value 键值对是一个元素
字典的key 必须是**不可变类型**,可以是 字符串类型和数字类型(int  float), 不能是 列表
value值可以是任何类型

```python
# 1. 定义空字典
my_dict = {}
my_dict1 = dict()
# 2. 定义带数据的字典
my_dict2 = {'name': 'isaac', 'age': 18, 'like': ['学习', '购物', '游戏'], 1: [2, 5, 8]}
print(my_dict2)

# 3. 访问value 值, 在字典中没有下标的概念, 使用 key值访问对应的value 值
# 18
print(my_dict2['age'])
# '购物'
print(my_dict2['like'][1])

# 如果key值不存在
# print(my_dict2['gender'])  # 代码报错,key值不存在
# 字典.get(key)  如果key值不存在,不会报错,返回的是None
print(my_dict2.get('gender'))

# my_dict2.get(key, 数据值)   如果key存在,返回key对应的value值,如果key不存在,返回书写的数据值值

print(my_dict2.get('gender', '男'))  # 男
print(my_dict2.get('age', 1))  # 18

print(len(my_dict2))  # 4
```

## 生成字典zip()

```python
name=input().split()  
langu=input().split()  
dict1=zip(name,langu)  
print(dict(dict1))

name=list(input().split())
lau=list(input().split())
print({name:lau for name,lau in zip(name,lau)})


# zip () 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的<class 'zip'>.将<class 'zip'>转化为字典
```

```python
grade_dict = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0,
}
grade_list = []
scores_list = []
while True:
    grade = input()
    if grade == "False":
        break
    else:
        scores = int(input())
        grade_list.append(grade_dict[grade] * scores)
        scores_list.append(scores)  
avg_score = sum(grade_list) / sum(scores_list)
print("%.2f" % avg_score)
```

## 字典中添加和修改数据

```python
my_dict = {'name': 'isaac'}
print(my_dict)
# 字典中添加和修改数据,使用key值进行添加和修改
# 字典[key] = 数据值;   如果key值存在,就是修改,如果key值不存在,就是添加

my_dict['age'] = 18  # key值不存在,添加
print(my_dict)

my_dict['age'] = 19  # key值已经存在,就是修改数据
print(my_dict)

# 注意点 key 值 int 的 1 和float的 1.0 代表一个key值
my_dict[1] = 'int'
print(my_dict)
my_dict[1.0] = 'float'
print(my_dict)


word_dict = {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}
letter = input()
word = input()
# 如果新增的字母已经存在，不会新增，找到该字母对应的键，修改它的值
if letter in word_dict:
    # 如果键对应的值是列表形式，直接添加单词到列表中  
    if type(word_dict[letter])==list:
        word_dict[letter].append(word)
 # 如不是列表形式，则需要对值进行处理：加空格添加元素，再split切割str，把字符串类型转换为列表
    else:  
        word_dict[letter]=word_dict[letter]+' '+word
        word_dict[letter]=word_dict[letter].split(' ')
# 新增的字母不在字典中，则字典需要新增键值对
else:
    word_dict[letter]=word
print(word_dict)


# 使用字典计数
# 方法一
ls1 = list(input())
ls2 = [ls1.count(i) for i in ls1]
print(dict(zip(ls1,ls2)))
# 方法二
from collections import Counter
ls1 = input()
print(dict(Counter(ls1)))
# 方法三：
ls1 = list(input())
dict1 = {}
for i in ls1:
    if i in dict1:
        continue
    dict1[i] = ls1.count(i)
print(dict1)
#方法四
ls1 = list(input())
dict1 = {}
for i in ls1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)
# 方法五
ls1 = list(input())
dict1 = {}
for i in ls1:
    dict1[i] = dict1.get(i,0)+1
print(dict1)
```

## 字典中删除数据

```python
my_dict = {'name': 'isaac', 'age': 19, 1: 'float', 2: 'aa'}

# 根据key值删除数据  del 字典名[key]
del my_dict[1]
print(my_dict)

# 字典.pop(key)  根据key值删除, 返回值是删除的key对应的value值
result = my_dict.pop('age')
print(my_dict)
print(result)

# 字典.clear()  清空字典, 删除所有的键值对
my_dict.clear()
print(my_dict)


# del 字典名   直接将这个字典删除了,不能使用这个字典了
del my_dict  # 后边的代码不能再直接使用这个变量了,除非再次定义

# print(my_dict)  代码报错, 变量未定义
```

## 字典中遍历数据
### 1. for 循环直接遍历字典, 遍历的是字典的 key 值

```python
my_dict = {'name': 'isaac', 'age': 18, 'gender': '男'}

# for循环体直接遍历字典, 遍历的字典的key值
for key in my_dict:
    print(key, my_dict[key])
```

### 2. 字典.keys()
字典.keys() 获取字典中所有的key值, 得到的类型是 dict_keys, 该类型具有的特点是
	 1. 可以使用list() 进行类型转换,即将其转换为列表类型
	 2. 可以使用for循环进行遍历

```python
result = my_dict.keys()
print(result, type(result))
for key in result:
     print(key)
```

### 字典.values()
字典.values() 获取所有的value值, 类型是 dict_values
	1. 可以使用list() 进行类型转换,即将其转换为列表类型
	2. 可以使用for循环进行遍历

```python
result = my_dict.values()
print(result, type(result))
for value in my_dict.values():
     print(value)
```

### 字典.items()
字典.items()  获取所有的键值对, 类型是 dict_items, key,value 组成元组类型
	 1. 可以使用list() 进行类型转换,即将其转换为列表类型
	 2. 可以使用for循环进行遍历

```python
result = my_dict.items()
print(result, type(result))
for item in my_dict.items():
    print(item[0], item[1])

print('=' * 30)

for k, v in my_dict.items():  # k 是元组中的第一个数据, v 是元组中的第二个数据
    print(k, v)

```

```python
result_dict = {
    'Allen': ['red', 'blue', 'yellow'],
    'Tom': ['green', 'white', 'blue'],
    'Andy': ['black', 'pink']
}

for m, n in sorted(result_dict.items()):
    print("%s's favorite colors are:" % m)
    for o in n:
        print(o)

```

## 字典推导式 

```python
# 变量 = {生成字典的规则 for 临时变量 in xx}
# my_dict = {key: value for i in range(3)}
my_dict = {f"name{i}": i for i in range(3)}
print(my_dict)

my_dict = {f"name{i}": j for i in range(3) for j in range(3)}
print(my_dict)  # 3个数据
my_dict = {f"name{i}{j}": j for i in range(3) for j in range(3)}
print(my_dict)
```

```
{'name0': 0, 'name1': 1, 'name2': 2}
{'name0': 2, 'name1': 2, 'name2': 2}
{'name00': 0, 'name01': 1, 'name02': 2, 'name10': 0, 'name11': 1, 'name12': 2, 'name20': 0, 'name21': 1, 'name22': 2}
```

## 字典题

```python
operators_dict={'<' :'less than','==':'equal'}
print('Here is the original dict:')
for i in sorted(operators_dict):
    print(f'Operator {i} means {operators_dict[i]}.')
operators_dict['>']='greater than'
print()
print('The dict was changed to:')
for j in sorted(operators_dict):
    print(f'Operator {j} means {operators_dict[j]}.')


notebook = {'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}
print(' '.join(notebook[input()]))



```

# 公共方法
-   `+` 支持 字符串、列表、元组进行操作， 得到一个新的容器
    
-   `* 整数` 复制， 支持 字符串、列表、元组进行操作， 得到一个新的容器
    
-   `in/not in` 判断存在或者是不存在，支持 字符串、列表、元组、字典进行操作， 注意： ==如果是字典的话，判断的是 key 值是否存在或不存在==
    
-   `max/min` 对于字典来说，比较的字典的 key值的大小

# 函数

## 函数的定义和调用

函数,能够实现一个具体的功能, 是多行代码的整合
函数的定义: 使用关键字 def ,
`def 函数名():`   # 函数名要遵循标识符的规则, 见名知意

## 函数的文档说明

函数的文档说明本质就是注释,告诉别人,这个函数怎么使用的,是干什么事的。
只不过这个注释，有特定的位置书写要求，要写在函数名字的下方。

查看函数的文档注释可以使用help(函数名)
help(函数名)

## 函数的参数

```python
# 定义一个函数,实现两个数的和
def add(a, b):  # a和b称为是形式参数, 简称形参.
    c = a + b
    print(f"求和的结果是{c}")


# 函数调用, 如果函数在定义的时候有形参,那么在函数调用的时候,必须传递参数值
# 这个参数称为 实际参数,简称实参
# 在函数调用的时候,会将实参的值传递给形参
add(1, 2)
add(100, 200)
```

## 局部变量

局部变量的作用域（作用范围）： 当前函数的内部
局部变量的生存周期：在函数调用的时候被创建，函数调用结束之后，被销毁（删除）
局部变量只能在当前函数的内部使用，不能在函数的外部使用。

## 全局变量

全局变量： 就是在函数外部定义的变量。
在函数内部可以访问全局变量的值，如果想要修改全局变量的值，需要使用 global 关键字声明

```python
def func2():
    # g_num = 200  # 这里不是修改全局变量的值,是定义一个局部变量,和全局变量的名字一样而已
    # 想要在函数内部修改全局变量的值,需要使用 global 关键字声明这个变量为全局变量
    global g_num
    g_num = 300
```

## 返回值

在函数中定义的局部变量，或者通过计算得出的局部变量， 想要在函数外部访问和使用，此时就可以使用 return 关键字，将这个返回值返回

函数想要返回一个数据值,给调用的地方,需要使用关键字 return
return关键字的作用: ①, 将return 后边的数据值进行返回；②程序代码遇到return, 会终止(结束)执行。
注意点: return 关键字必须写在函数中。

```python
def add(a, b):
    c = a + b
    # 将求和的结果c返回,即函数外部使用求和的结果（不在函数内部打印结果）
    return c
    # 函数遇到return就结束了,不会执行return之后的代码

result = add(100, 200)
print(f'函数外部获得了求和的结果{result}！')  # 函数外部获得了求和的结果300！

print(add(10, 30))  # 40
```

## return 返回多个数据值

```python
def func(a, b):
    c = a + b
    d = a - b
    # 需求: 想要将 c 和 d 都进行返回
    # 思考: 容器可以保存多个数据值, 那就可以将 c  和 d 放到容器中进行返回
    # return [c, d]  # 列表
    # return (c, d)  # 元组
    # return {'c': c, 'd': d}
    # return {0: c, 1: d}
    return c, d  # 默认是组成元组进行返回的


result = func(10, 20)
print(f"a+b的结果是{result[0]}, a-b的结果是{result[1]}！")
```

1. return 关键字后边可以不写数据值， 默认返回 None
def func():
    xxx
    return   # 返回 None，终止函数的运行的

2. 函数可以不写 return，返回值默认是 None

def func():
    xxx
    pass

## 函数的嵌套调用

```python
def func1():
    print('     func1 start ... ')
    print('     函数的其他代码')
    print('     func1 end ...')


def func2():
    print('func2 start ....')
    func1()  # 函数调用
    print('func2 end....')


# 调用func1()
func1()

# 调用func2()
func2()

```

## 函数应用

```python
# 1. 定义一个函数,打印一条横线
def print_line():
    print('-' * 30)


# 2. 定义一个函数,打印任意条数的横线
def print_lines(n):
    for i in range(n):
        print_line()
```

```python
def my_sum(a, b, c):
    return a + b + c


def average(a, b, c):
    res = my_sum(a, b, c)
    return res / 3  # 除法运算得到的数据是float类型


result = my_sum(1, 2, 3)
print(result)  # 6

result = average(1, 2, 3)
print(result)  # 2.0
```
