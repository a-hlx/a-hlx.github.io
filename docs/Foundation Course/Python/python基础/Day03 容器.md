## 字符串定义

带引号(单,双,三引号都可)的内容就是字符串.

如果字符串本身包含单引号，使用双引号定义; 如果字符串包含双引号可以使用单引号定义; 或者统一使用三引号定义

```python
print('Happy Programmers\' Day to everyone!')
```

```python
print('*'*3)
***
'*'*3
'***'
```

## 字符串的输出和输出
输入 input()
input() 函数得到的内容就是字符串

输出 print() 函数 %s 或者f-string 

## 下标
my_str[num]
python中正数下标从 0 开始
负数下标从-1开始,表示最后一个字符
`len()函数`
字符串长度
print(len(my_str))

## 切片
切片语法：
变量［start：end：step］，**会得到一个新的字符串**
start 开始位置的下标
end 结束位置的下标，不包含end 对应的下标
step 步长，下标之间的间隔，默认是1

my_str[:]  得到和原来一样的字符串  
my_str[::-1]  字符串的逆置

## 查找方法

### find() & rfind()
find（）在字符串中查找是否存在某个字符中
my_str.find(sub_str,start,end)
sub＿str：要在字符串中查找的内容，类型str 
start：开始位置，从哪里开始查找，默认是0
end：结束的位置，查找到哪里结束，不包含end 对应的下标,默认是Len（）
返回值：即方法执行的结果是什么，如果找到 sub＿str，返回的sub＿str 在my str 中的位置的正数下标
如果没有找到返回-1

rfind即right find,从右查找,返回正数下标

### index & rindex()
同find,没有找到报错

### count()
count（sub＿str，start，end）统计出现的次数

### 检测字母、数字、空格

```python
s=input()
print(s.isalpha())
print(s.isdigit())
print(s.isspace())
```

### set()

```python
a = set(input().split())  
print(sorted(a))  
#本题考试set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
```

## 替换方法 replace
my＿str.replace（old＿str，new＿str，count）
count：替换的次数，默认是全部替换
返回值：得到一个新的字符串，不会改变原来的字符串

```python
s=input()
print(s.replace('a*','ab'))
```

## 字符串分隔 split()
my_str.split(sub_str， count))
将my_str字符串按照sub_str进行切割
sub_str：按照什么内容切割字符串， 默认是空白字符， 空格， tab键
count：切割几次，默认是全部切割
返回值：列表[]

## 字符串连接 join()
my_str.join(可选代对象)
可选代对象, str
列表(需要列表中的每一个数据都是字符串类型)
将my_str这个字符串添加到可选代对象的两个元素之间
返回值:一个新的字符串,不会改变原字符串的值

```python
i=1
list=[]
while i:
    s=input()
    if s=='0':
        i=0
    else:
        list.append(s)
l=' '
print(l.join(list))
```

## 列表list
求列表中数据元素的个数，即列表的长度
num=len(my_list 2)
print(num)

下标列表和字符串不同的是：字符串不能使用下标修改其中的数据，但是列表可以

```python
List=input().split()
name=input()
print(name in List)
```

## 前言

### list的常见内置函数

my conclusion:
list.function()直接修改list
fuction(list)，返回新的list

-   len() ：求列表元素个数
-   max() ：求列表最大值
-   min() ：求列表最小值
-   sum() ：求列表的和
-   sorted() :求排序后的列表序列
-   list() :将其他数据结构转换成列表

```python
my_list = list(range(0, 19, 2))
print(my_list)

print(list('ddd'))
#['d', 'd', 'd']
```

-   any() :只要列表里有一个True就会返回True
-   all()：表里的所有元素都是True才会返回True
-   enumerate() ：可以配合for loop使用提取列表元素的位置信息
- 输出列表首尾

```python
num_list=[]
for i in range(10,51):
	num_list.append(i) 
print(num_list) 
print(num_list[0],num_list[-1])
```

```python
my_list = list('Python')
```

#### 计数count()

```python
list=input().split()
print(list.count('0'))
```

#### 查找index()

```python
list=input().split()
print(list.index('NiuNiu'))
```

### list的推导式

list=[推导语句 for i in list] ，可以省略append和创建空list这两个步骤。

```python
list=input().split()
name=input()
list.pop(list.index(name))
#list= [i for i in list if i!=name]
#list.remove(name)
print(list)


my_list = [i for i in range(1,51) if i %5 ==0]
for i in my_list:
    print(i)

```

## 遍历
```python
my_list = ['郭德纲', '于']
for i in my_list:
	print(i)

print('*'* 30)
   
j=0
while j < len(my_list):
	print(my_list[j])
	j += 1
````

## enumerate 函数
enemerate 将可迭代序列中元素所在的下标和具体元素数据组合在一块,变成元组
```python
my_list = ['a', 'b', 'c', 'd', 'e']

# for i in my_list:
#     print(i)

for i in my_list:
    print(my_list.index(i), i)  # 下标, 数据值


# enemerate 将可迭代序列中元素所在的下标和具体元素数据组合在一块,变成元组
for j in enumerate(my_list):
    print(j)

```

## split()

![[Day03 容器#字符串分隔 split]]

## 向列表中添加数据
### append
append() 方法用于在列表的末尾追加元素，该方法的语法格式如下：
listname.append(obj)
其中，listname 表示要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。

```python
name = ["Niumei", "YOLO", "Niu Ke Le", "Mona"]
friends = []
friends.append(name)
food = ["pizza", "fish", "potato", "beef"]
friends.append(food)
number = [3, 6, 0, 3]
friends.append(number)
print(friends)
```

### extend
extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。  
extend() 方法的语法格式如下：
listname.extend(obj)
其中，listname 指的是要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等，但不能是单个的数字。

### insert
insert() 的语法格式如下：  
listname.insert(index , obj)
其中，index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。  
  当插入列表或者元祖时，insert() 也会将它们视为一个整体，作为一个元素插入到列表中，这一点和 append() 是一样的。
 ```python
1.  l = ['Python', 'C++', 'Java']
2.  #插入元素
3.  l.insert(1, 'C')
4.  print(l)

6.  #插入元组，整个元祖被当成一个元素
7.  t = ('C#', 'Go')
8.  l.insert(2, t)
9.  print(l)

11.  #插入列表，整个列表被当成一个元素
12.  l.insert(3, ['Ruby', 'SQL'])
13.  print(l)

15.  #插入字符串，整个字符串被当成一个元素
16.  l.insert(0, "http://c.biancheng.net")
17.  print(l)
```

输出结果为：
['Python', 'C', 'C++', 'Java']  
['Python', 'C', ('C#', 'Go'), 'C++', 'Java']  
['Python', 'C', ('C#', 'Go'), ['Ruby', 'SQL'], 'C++', 'Java']  
['http://c.biancheng.net', 'Python', 'C', ('C#', 'Go'), ['Ruby', 'SQL'], 'C++', 'Java']

## 列表中的删除操作
### del：根据索引值删除元素  
del 可以删除列表中的单个元素，格式为：
del listname[index]
其中，listname 表示列表名称，index 表示元素的索引值。  
  
del 也可以删除中间一段连续的元素，格式为：
del listname[start : end]
其中，start 表示起始索引，end 表示结束索引。del 会删除从索引 start 到 end 之间的元素，不包括 end 位置的元素。

### pop()：根据索引值删除元素
Python pop() 方法用来删除列表中指定索引处的元素，具体格式如下：
listname.pop(index)
其中，listname 表示列表名称，index 表示索引值。如果不写 index 参数，**默认会删除列表中的最后一个元素**

```python
num = eval(input())
stack = [1, 2, 3, 4, 5]
for _ in range(2):
    stack.pop()
    print(stack)
stack.append(num)
print(stack)
```

### remove()：根据元素值进行删除
根据元素本身的值来进行删除操作。  
  需要注意的是，remove() 方法只会删除**第一个**和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。

```python
str1=input()
list1=str1.split()
str2=input()
list2=str2.split()
for i in list2:
    list1.remove(i)
print(list1)
```

### clear()：删除列表所有元素

## 列表排序和逆置

==sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list;reverse() 函数没有返回值，但是会对列表的元素进行反向排序。==

### sort排序
sort()函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。默认是正向排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

```python
list = [2, 3, 4, 5, 1]
list.sort()
print(list)
 #[1, 2, 3, 4, 5]
```

### sorted排序
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sorted 语法：
sorted(iterable[, cmp[, key[, reverse]]])
参数说明：
-   iterable -- 可迭代对象。
-   cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
-   key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
-   reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

```python
my_list = ["P", "y", "t", "h", "o", "n"]
print(sorted(my_list))
print(my_list)
my_list.sort(reverse=True)
print(my_list)
```

### reverse反转排序
reverse() 函数没有返回值，但是会对列表的元素进行反向排序。

```python
list = [2, 1, 3, 5, 4]
list.reverse()
print(list)#[4, 5, 3, 1, 2]

```

### 列表中字典排序

![[Day06 函数与文件#列表中字典排序]]

## 列表嵌套

```python
school_names=[['北京大学'，'清华大学']，
			  ['南开大学'，'天津大学'，'天津师范大学门']，
			  ['山东大学'，'中国海洋大学']]
print（school._names[I]）#['南开大学'，'天津大学'，'天津师范大学']
print（school_names[1][1]）#天津大学
print（school_names[1][1][1]）#津

for schools in school names:
#print(schools)#列表
	for name in schools:
		print(name)

```

## 列表推导式

列表推导式, 为了快速的生成一个列表

```python
# 1. 变量 = [生成数据的规则 for 临时变量 in xxx]
# 每循环一次,就会创建一个数据
my_list = [i for i in range(5)]
print(my_list)  # [0, 1, 2, 3, 4]

my_list1 = ['hello' for i in range(5)]
print(my_list1)

my_list2 = [f'num:{i}' for i in my_list]
print(my_list2)
my_list3 = [i+i for i in range(5)]
print(my_list3)

# 2. 变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
# 每循环一次,并且if条件为True,生成一个数据
my_list = [i for i in range(5) if i % 2 == 0]
print(my_list)  # [0, 2, 4]

# 3. 变量 = [生成数据的规则 for 临时变量 in xxx  for j in xxx]
# 第二个for 循环 循环一次,生成一个数据
my_list4 = [(i,j) for i in range(3) for j in range(3)]
print(my_list4)

```

```
[0, 1, 2, 3, 4]
['hello', 'hello', 'hello', 'hello', 'hello']
['num:0', 'num:1', 'num:2', 'num:3', 'num:4']
[0, 2, 4, 6, 8]
[0, 2, 4]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

## 案例: 分配办公室

```python
import random
schools=[[],[],[]]
teachers=['a','b','c','d','e','f','g','h']
for teacher in teachers:
    num=random.randint(0,2)
    schools[num].append(teacher)
print(schools)
for office in schools:
    print(f'该办公室有{len(office)}个教师,分别是:')
    for teacher in office:
        print(teacher,end='')
    print()
```

## 元组tuple
元组和列表（list）的不同之处在于：
-   列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列；
-   而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列。

从形式上看，元组的所有元素都放在一对小括号`( )`中，相邻元素之间用逗号`,`分隔，如下所示：
(element1, element2, ... , elementn)

当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号`,`，否则 Python 解释器会将它视为字符串。(数据元素同)

元组支持下标和切片

tuple()将列表转为元组

```python
a=input()
b=input()
c=a,b
#单个变量赋值时，自动将右边多个变量值打包成元组
print(c)


# print(tuple([input(),input()]))
# print((input(),input()))
t = input(),input()
print(t)
# 可以将列表转换成tuple，也可以直接()创建tuple，或者将多个变量赋值给一个值会自动转换成tuple
```
## try- except代码块

```python
entry_form=('Niuniu','Niumei')
print(entry_form)
try:
    entry_form[1]='Niukele'
except:
    print("The entry form cannot be modified!")
```

```python
x=tuple(input().split())  
print(x[0:3])

c=tuple('abcdefg')
print(c)
# ('a', 'b', 'c', 'd', 'e', 'f', 'g')
```

```python
t = tuple(['Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna'])
print(t,'Congratulations!' if input() in t else 'What a pity!',sep='\n')
```

```python
a=tuple(list(range(1,6)))
print(a,len(a),sep="\n")
b=tuple(list(range(6,11)))
print(a+b,len(a+b),sep="\n")
```