# 概念介绍

面向对象(OOP)和面向过程,是两种编程思想.
编程思想是指对待同一个问题,解决问题的套路方式.

-   面向过程: 注重的过程,实现的细节
    -   函数
-   面向对象: 关注的是结果, 
    -   封装, 继承 和多态(三大技术)

# 类和对象

类和对象,是面向对象中非常重要的两个概念

-   类
    -   类是泛指的,指代多个, 是由对象抽象来的
    - 可以理解是一个模板，通过它可以创建出无数个具体实例。
    -   在代码中, 是通过关键字`class`定义的 
-   对象
    -   对象是特指的,指代一个,是具体存在的 
    -   在代码中, 对象是由类创建的
    - 类并不能直接使用，通过类创建出的实例（又称对象）才能使用。

## 类的组成

-   类名   
-   属性: 特性, 变量
    -   一个类的属性有很多,只关注需要使用的,没有用到的不用管     
-   方法: 行为, 函数

## 类的抽象

-   名词提炼法
-   所见即所得

## 类的定义

Python 中定义一个类使用 class 关键字实现，其基本语法格式如下：  

class 类名(object)：  
    多个（≥0）类属性...  
    多个（≥0）类方法...

object 是所有的类基类,即最初始的类
类名: 遵循大驼峰的命名规范,即每个单词首字母大写

```python
# 定义方式一, 推荐
class Dog(object):
    pass

# 定义方式二
class Dog1():   # 括号中的内容可以不写
    pass

# 定义方式三
class Dog2:   # 括号也可以不写
    pass

"""
新式类: 直接或者间接继承object的类, 在python3中,所有的类默认继承object类,即python3中所有的类都是新式类
旧式类(经典类): 已经过时,不推荐使用
```

## 创建对象

在代码中,对象是由类创建的.

```python
# 定义类
class Dog(object):
    # 在类中定义的函数,称为方法, 函数的所有知识都可以使用
    def play(self):  # 暂时不管self ,
        print('小狗快乐的拆家中......')


# 创建对象 变量 = 类名()
dog = Dog()  # 创建一个对象,dog
print(id(dog))

dog1 = Dog()  # 创建一个对象 dog1
print(id(dog1))

# 可以使用对象调用类中的方法.  对象.方法名()
dog.play()
dog1.play()
```

# 类外部添加和获取对象属性

```python
class Dog(object):
    def play(self):
        print('小狗快乐的拆家中.....')


# 创建对象
dog = Dog()
dog.play()

# 给对象添加属性  对象.属性名 = 属性值
dog.name = '大黄'  # 给dog对象添加name属性,属性值是 大黄
dog.age = 2   # 给dog对象添加age属性,属性值是 2

# 获取对象的属性值  对象.属性名
print(dog.name)
print(dog.age)

# 修改属性值 和添加一样,存在就是修改,不存在,就是添加
dog.age = 3  # age 属性已经存在,所以是修改属性值
print(dog.age)

dog1 = Dog()  # 新创建一个对象 dog1
dog1.name = '小白'
print(dog1.name)

```

# 类内部操作属性

```python
class Dog(object):
    # self 作为类中方法的第一个形参,在通过对象调用方法的时候,不需要手动的传递实参值,是python解释器
    # 自动将调用该方法的对象传递给self, 所以self这个形参代表的是对象
    def play(self):
        print(f'self: {id(self)}')
        print(f'小狗 {self.name} 在快乐的拆家中.....')


# 创建对象
dog = Dog()
dog.name = '大黄'
print(f"dog : {id(dog)}")
dog.play()
print('-' * 30)
dog1 = Dog()
dog1.name = '小白'
print(f"dog1: {id(dog1)}")
dog1.play()

```

# 魔法方法

在 python 的类中,有一类方法,这类方法以 `两个下划线开头` 和`两个下划线结尾`, 并且在`满足某个特定条件的情况下,会自动调用`. 这类方法,称为魔法方法

## `__init__()`

调用时机: 在创建对象之后,会立即调用.
作用: 
	1. 用来给对象添加属性,给对象属性一个初始值(构造函数)
	2. 代码的业务需求,每创建一个对象,都需要执行的代码可以写在 `__init__ `中
注意点: 如果 `__init__` 方法中,有出了 self 之外的形参,那么在创建的对象的时候,需要给额外的形参传递实参值 `类名(实参)`

```python
class Dog(object):
    def __init__(self):  # self 是对象
        print('我是__init__方法,我被调用了')
        # 对象.属性名 = 属性值
        self.name = '小狗'


# 创建对象
# Dog()
dog = Dog()
print(dog.name)
dog1 = Dog()
print(dog1.name)
```

**书写带参数的__init__方法**

```python
class Dog(object):
    def __init__(self, name):  # self 是对象
        print('我是__init__方法,我被调用了')
        # 对象.属性名 = 属性值
        self.name = name

    def play(self):
        print(f"小狗{self.name}快乐的拆家中...")


# 创建对象 类名(实参值)
dog = Dog('大黄')
print(dog.name)
dog.play()
dog1 = Dog('小白')
print(dog1.name)
dog1.play()

```

## `__str__()`

调用时机:
	1. `print(对象)`, 会自动调用 `__str__` 方法, 打印输出的结果是 `__str__` 方法的返回值
	2. `str(对象)`  类型转换,将自定义对象转换为字符串的时候, 会自动调用
应用:
	1. 打印对象的时候,输出一些属性信息
	2. 需要将对象转换为字符串类型的时候
注意点:
	`方法必须返回一个字符串`,只有 self 一个参数

```python
class Dog(object):
    def __init__(self, name, age):
        # 添加属性
        self.name = name
        self.age = age

    def __str__(self):
        print('我是__str__, 我被调用了...')
        # 必须返回一个字符串
        return f"小狗的名字是{self.name}, 年龄是{self.age}"


# 创建对象
dog = Dog('大黄', 2)
print(dog)  # 没有定义 __str__ 方法,print(对象) 默认输出对象的引用地址

str_dog = str(dog)  # 没有定义 __str__ 方法, 类型转换,赋值的也是引用地址
print(str_dog)

```

```
我是__str__, 我被调用了...
小狗的名字是大黄, 年龄是2
我是__str__, 我被调用了...
小狗的名字是大黄, 年龄是2
```

## `__del__()`

调用时机:
	对象在内存中被销毁删除的时候(引用计数为 0)会自动调用 __del__ 方法
	1. 程序代码运行结束,在程序运行过程中,创建的所有对象和变量都会被删除销毁
	2. 使用 `del 变量` , 将这个对象的引用计数变为 0.会自动调用 __del__ 方法
应用场景:
	对象被删除销毁的时候,要书写的代码可以写在 `__del__`中.一般很少使用

引用计数: 是 python 内存管理的一种机制, 是指一块内存,有多少个变量在引用,
1. 当一个变量,引用一块内存的时候,引用计数加 1
2. 当删除一个变量,或者这个变量不再引用这块内存.引用计数减 1
3. 当内存的引用计数变为 0 的时候,这块内存被删除,内存中的数据被销毁

```python
class Dog(object):
    def __init__(self, name, age):
        # 添加属性
        self.name = name
        self.age = age

    def __str__(self):
        # 必须返回一个字符串
        return f"小狗的名字是{self.name}, 年龄是{self.age}"

    def __del__(self):
        print(f'我是__del__ 方法,我被调用了, {self.name}被销毁了.......')


# 创建一个对象
# dog = Dog('大黄', 2)
# dog1 = Dog('小白', 1)

dog = Dog('小花', 3)  # 小花 引用计数为1
dog2 = dog   # 小花 引用计数2
print('第一次删除之前')
del dog  # dog 变量不能使用, 小花对象引用计数 1
print('第一次删除之后')
print('第二次删除之前')
del dog2  # dog2变量不能使用, 小花对象的引用计数为 0, 会立即__del__ 方法
print('第二次删除之后')
```

```python
第一次删除之前
第一次删除之后
第二次删除之前
我是__del__ 方法,我被调用了, 小花被销毁了.......
第二次删除之后

```

### 查看对象引用次数

```python
import sys


class Dog(object):
    pass


dog = Dog()  # 1
print(sys.getrefcount(dog))  # 显示的时候,会比实际的多一个,
dog1 = dog  # 2
print(sys.getrefcount(dog))  # 显示的时候,会比实际的多一个,
del dog  # 1
print(sys.getrefcount(dog1))  # 显示的时候,会比实际的多一个,

```

## `__repr__()`

```python
my_list = ['hello', 'python', 'cpp']   # 列表中存储了三个字符串对象

print(my_list)


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def __repr__(self):
        """repr 方法和 str 方法,非常类似,也是必须返回一个字符串"""
        return f"{self.name}"


# 将三个Dog类的对象添加到列表中
my_list1 = [Dog('大黄', 2), Dog('小白', 4), Dog('小花', 6)]
print(my_list1)

dog = Dog('大黄', 2)
print(dog)   # __str__


```

# 修改属性

```python
class Employee(object): 
    def __init__(self,name,salary): 
        self.name = name 
        self.salary = salary 
    def printclass(self): 
        print("%s'salary is %d, and his age is %s" % (self.name, self.salary, self.age))  
name = input()
salary = int(input())
age = int(input()) 
try:
    e = Employee(name, salary, age)
    e.printclass() 
except: 
    print("Error! No age") 
    
try:
    emp = Employee(name, salary)
    emp.age = age  #动态给对象加属性
    emp.printclass()
except: 
    print("Error! No age")
```

```python

#属性的添加有两种方式：直接在类定义中添加（类里的属性所有实例化的对象都可以拥有此属性也可以修改），
#另一种方式就是对象添加，这个添加的对象只对该对象有效，其他对象没有此属性
#setattr(object, name, value)
e = Employee(name,salary)
if print(hasattr(e,'age')) :
    e.printclass()
else:
    setattr(e,"age",age)
    e.printclass()
```

# 重载运算

```python
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self,other):
        return Coordinate(self.x+other.x,self.y+other.y)

x1,y1 = list(map(int,input().split()))
x2,y2 = list(map(int,input().split()))
c1 = Coordinate(x1,y1)
c2 = Coordinate(x2,y2)
print(c1+c2)
```

# 案例

## 烤地瓜

```python
class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0

    def cook(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜的状态
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生不熟的'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '烤糊了'

    def __str__(self):
        return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>"


# 创建对象
potato = Potato()
print(potato)
potato.cook(4)
print(potato)
potato.cook(3)
print(potato)
```

## 烤地瓜-调料版

```python
class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.name_list = []  # 保存调料的

    def cook(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜的状态
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生不熟的'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '烤糊了'

    def __str__(self):
        # buf_list = str(self.name_list)  # str([])  ===> '[]'
        # buf_list = buf_list.replace('[', '')
        # 字符串.join(列表), 将字符串添加到列表中的每个元素之间,组成新的字符串
        buf = ','.join(self.name_list)
        if self.name_list:
            return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>, 调料有: {buf}"
        else:
            return f"地瓜的状态<<{self.status}>>, 烧烤总时间为<{self.total_time}>,还没有添加调料"

    def add(self, name):
        self.name_list.append(name)


# 创建对象
potato = Potato()
print(potato)
potato.add('油')
potato.cook(4)
potato.add('辣椒面')
print(potato)
potato.cook(3)
potato.add('孜然')
print(potato)

```

##  搬家具

```python
# 定义家具类 Furniture 类
class Furniture(object):
    def __init__(self, name, area):
        # 类型
        self.name = name
        # 面积
        self.area = area

    def __str__(self):
        return f'家具的类型<{self.name}>, 占地面积<{self.area}>平'


# 定义房子类
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.h_area = area
        self.furniture_list = []
        self.free_area = area  # 房子的剩余面积

    def add_furniture(self, obj_furniture):
        """ 添加家具 obj_furniture:  家具类的对象"""
        if self.free_area > obj_furniture.area:
            self.furniture_list.append(obj_furniture)
            # 修改剩余面积
            self.free_area -= obj_furniture.area
            print(f'家具<{obj_furniture.name}>添加成功')
        else:
            print('添加失败,换个大房子吧')

    def __str__(self):
        return f"房子的地址为<{self.address}>, 占地面积为<{self.h_area}>, 剩余面积为{self.free_area}"


# 创建家具对象
bed = Furniture('豪华双人床', 15)
print(bed)

# 创建一个房子类对象
house = House('意大利农场', 100)
print(house)
house.add_furniture(bed)
print(house)

```

```
家具的类型<豪华双人床>, 占地面积<15>平
房子的地址为<意大利农场>, 占地面积为<100>, 剩余面积为100
家具<豪华双人床>添加成功
房子的地址为<意大利农场>, 占地面积为<100>, 剩余面积为85
```

打印家具列表

```python
# 定义家具类 Furniture 类
class Furniture(object):
    def __init__(self, name, area):
        # 类型
        self.name = name
        # 面积
        self.area = area

    def __str__(self):
        return f'家具的类型<{self.name}>, 占地面积<{self.area}>平'


# 定义房子类
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.h_area = area
        self.furniture_list = []
        self.free_area = area  # 房子的剩余面积

    def add_furniture(self, obj_furniture):
        """ 添加家具 obj_furniture:  家具类的对象"""
        if self.free_area > obj_furniture.area:
            self.furniture_list.append(obj_furniture)
            # 修改剩余面积
            self.free_area -= obj_furniture.area
            print(f'家具<{obj_furniture.name}>添加成功')
        else:
            print('添加失败,换个大房子吧')

    def __str__(self):
        # 自定义家具类,将该类的对象添加到列表中(容器), 直接打印列表,显示的是 自定义对象的引用地址
        # [家具对象, 家具对象, ... ]  ---> [家具类型, 家具类型, .....]
        if self.furniture_list:
            buf_list = [obj.name for obj in self.furniture_list]
            return f"房子的地址为<{self.address}>, 占地面积为<{self.h_area}>, 剩余面积为{self.free_area}," \
                   f"家具有<{','.join(buf_list)}>"
        else:
            return f"房子的地址为<{self.address}>, 占地面积为<{self.h_area}>, 剩余面积为{self.free_area}," \
                   f"还没有购买家具"



# 创建家具对象
bed = Furniture('豪华双人床', 15)
print(bed)

# 创建一个房子类对象
house = House('意大利农场', 100)
print(house)
house.add_furniture(bed)
print(house)

```














