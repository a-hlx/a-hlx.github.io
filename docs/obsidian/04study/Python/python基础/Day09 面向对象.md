# 继承

## 继承的基本语法

继承: 描述的类与类之间所属关系.
基本语法:
class 类B(类A):
    pass

称为类 B 继承类 A
特点: B类的对象可以使用 A类的属性和方法
优点: 代码复用.重复相同的代码不用多次书写.
名词: 
    类A: 父类 		基类
    类B: 子类		派生类

```python
# 1. 定义是个 动物类 animal类
class Animal(object):
    # 2. 在animal类书写 play方法,输出快乐的玩耍....
    def play(self):
        print('快乐的玩耍....')


# 3. 定义Dog类继承animal类,
class Dog(Animal):
    pass


# 4. 创建dog类对象.调用父类的方法
dog = Dog()
dog.play()
```

## 单继承和多层继承

单继承: 如果一个类只有一个父类,把这种继承关系称为单继承
多继承: 如果一个类有多个父类,把这种继承关系称为多继承
多层继承: C--> B --> A
	多层继承中,子类可以使用所有继承链中的类中的方法和属性

## 子类重写父类的同名方法

重写: 子类定义和父类名字相同的方法.
为什么重写: 父类中的方法,不能满足子类对象的需求,所以要重写.
重写之后的特点: 子类对象调用子类自己的方法,不再调用父类的方法,父类对象调用父类自己的方法.

```python
# 1. 定义Dog类, 书写bark方法, 输出 汪汪汪叫
class Dog(object):
    def bark(self):
        print('汪汪汪叫.........')


# 2. 定义XTQ类,继承Dog类. 重写父类中的bark方法, 输出 嗷嗷嗷叫
class XTQ(Dog):
    def bark(self):
        print('嗷嗷嗷叫--------')


# 创建Dog类对象
dog = Dog()
dog.bark()  # 父类自己的

# 创建XTQ类对象
xtq = XTQ()
xtq.bark()

```

## 子类调用父类的同名方法

```python
# 1. 定义Dog类, 书写bark方法, 输出 汪汪汪叫
class Dog(object):
    def bark(self):
        print('汪汪汪叫.........')


# 2. 定义XTQ类,继承Dog类. 重写父类中的bark方法, 输出 嗷嗷嗷叫
class XTQ(Dog):
    def bark(self):
        print('嗷嗷嗷叫--------')

    def see_host(self):
        """看见主人之后,要汪汪汪叫,不能嗷嗷嗷叫"""
        print('看见主人了,', end='')
        # self.bark()
        # 想要在子类中调用父类的同名方法
        # 方法一: 父类名.方法名(self, 其他参数), 通过实例对象.方法名() 调用方法,不需要给self传递实参值,
        # python解释器会自动将对象作为实参值传递给self形参, 如果是通过类名.方法() 调用,python解释器就
        # 不会自动传递实参值,需要手动给self形参传递实参值
        Dog.bark(self)

        # 方法二  super(类A, self).方法名(参数) , 会调用当前类A 的父类中的方法
        super(XTQ, self).bark()  # 调用 XTQ类父类中的bark方法

        # 方法三  是方法二的简写, super().方法名(参数) ==> super(当前类, self).方法名()
        super().bark()


# 创建XTQ类对象
xtq = XTQ()
xtq.see_host()
```

## 继承中的 init

```python
# 1. 定义Dog类
class Dog(object):
    def __init__(self, name):
        # 添加属性
        self.age = 0
        self.name = name

    def __str__(self):
        return f'名字为:{self.name}, 年龄为{self.age}'


# 2. 定义XTQ类继承Dog类
class XTQ(Dog):
    # 子类重写了父类的__init__ 方法,默认不再调用父类的init方法, 需要手动的调用父类的init方法
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f'名字为:{self.name}, 年龄为{self.age}, 毛色为:{self.color}'


# 3. 创建XTQ类对象
xtq = XTQ('小黑', '红色')
print(xtq)
```

## 多继承

如果一个类有两个及以上的父类,就把这种继承关系称为多继承.

```python
# 1. 定义Dog类, 定义bark方法,和 eat方法
class Dog(object):
    def bark(self):
        print('汪汪汪叫.....')

    def eat(self):
        print('啃骨头.....')


# 2. 定义God类, 定义 play方法和eat方法
class God(object):
    def play(self):
        print('在云中飘一会....')

    def eat(self):
        print('吃蟠桃仙丹....')


# 3. 定义XTQ类, 继承Dog类和God类
# class XTQ(Dog, God):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
class XTQ(God, Dog):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
    pass


# 4. 创建XTQ类对象
xtq = XTQ()
xtq.bark()  # 调用 Dog父类中的方法
xtq.play()  # 调用 God父类中的方法

xtq.eat()  # 两个父类都存在eat方法,子类对象调用的是 第一个父类中的方法

```

## 多继承调用指定父类中的方法

```python
# 1. 定义Dog类, 定义bark方法,和 eat方法
class Dog(object):
    def bark(self):
        print('汪汪汪叫.....')

    def eat(self):
        print('啃骨头.....')


# 2. 定义God类, 定义 play方法和eat方法
class God(object):
    def play(self):
        print('在云中飘一会....')

    def eat(self):
        print('吃蟠桃仙丹....')


# 3. 定义XTQ类, 继承Dog类和God类
# class XTQ(Dog, God):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
class XTQ(God, Dog):  # XTQ 类有两个父类,这个继承关系称为多继承,XTQ类对象,可以调用两个父类中的属性和方法
    def eat(self):
        print('子类重写eat方法,调用子类自己的方法')
        # 调用指定父类中的方法
        # 方法一  类名.方法名(self, 参数)
        # Dog.eat(self)
        # God.eat(self)

        # 方法二 super(类A, self).方法名(参数)  类A的父类(继承顺序链的下一个类)中的方法
        # super(XTQ, self).eat()  # God 类中的方法
        super(God, self).eat()  # 调用的Dog类中的方法
        # super(Dog, self).eat()  # 调用的object类中的方法,注意: object类中没有eat方法,代码报错


# 4. 创建XTQ类对象
xtq = XTQ()
xtq.bark()  # 调用 Dog父类中的方法
xtq.play()  # 调用 God父类中的方法

xtq.eat()  # 两个父类都存在eat方法,子类对象调用的是 第一个父类中的方法

# 类名.__mro__ 可以当前类的继承顺序链,也叫做方法的调用顺序
# print(XTQ.__mro__)


```

## 私有权限

访问权限控制: 在什么地方可以使用和操作.
私有权限: 
	定义: 在方法和属性前加上两个下划线, 就变为私有.
	1. 不能在类外部通过对象直接访问和使用, 只能在类内部访问和使用
	2. 不能被子类继承,
公有: 不是私有的,就是公有的.

### 私有属性

```python
"""
私有属性,只需要在原属性名前加上两个下划线,即可
目的: 保证数据的相对安全,
想要访问和使用私有属性: 定义一个公有的方法,通过这个方法使用
"""


# 案例需求: 定义People 类, 定义属性 ICBC_money , 钱不能随便被修改,必须是合法的终端才可以操作
class People(object):
    def __init__(self):
        # python中的私有本质是 修改属性的名字, 在创建对象的时候,会自动的修改属性名
        # 在属性名的前边加上 _类名前缀
        self.__ICBC_money = 0  # 定义私有属性

    # 定义公有的方法,提供接口,修改余额
    def get_money(self):
        return self.__ICBC_money

    def set_money(self, money):
        num = input('输入金额:')
        self.__ICBC_money += int(num)
        # self.__ICBC_money += money

# 创建People类对象
xw = People()
# 实例对象.__dict__  可以查看对象具有的属性信息,类型是字典,字典的key是属性名, 字典的value是属性值
print('赋值之前:', xw.__dict__)
# print(xw.__ICBC_money)
xw.__ICBC_money = 1000  # 不是修改私有属性,是重新添加一个公有属性
print('赋值之后:', xw.__dict__)
print(xw.__ICBC_money)
print('=' * 20)
print(xw.get_money())  # 0
xw.set_money(1000)
print(xw.get_money())  # 1000
xw.set_money(-500)
print(xw.get_money())  # 500

```

```
赋值之前: {'_People__ICBC_money': 0}
赋值之后: {'_People__ICBC_money': 0, '__ICBC_money': 1000}
1000
====================
0
输入金额:
```

### 私有方法

```python
"""
私有方法: 在方法的前边加上两个__ ,就为私有方法
私有方法,不能在类外部访问
作用: 一般作为类内部的方法使用,不让在外部直接调用, 保证业务逻辑不被破坏
"""


class Dog(object):
    def born(self):
        """生小狗的方法, 生一个小狗,休息30天"""
        print('生了一只小狗...')
        self.__sleep()

    def __sleep(self):
        print('休息30天')


dog = Dog()
# dog.__sleep()
dog.born()
```

## 类属性

对象(实例对象): 通过class定义的类创建的, 即通过类实例化来的, 又称为实例, 实例对象
实例对象定义的属性称为是 实例属性. 通过实例对象(self) 定义的属性都是实例属性
实例属性: 每个实例对象中都存在一份,并且值可能是不一样的

类(类对象): 通过class定义的,又称为 类对象, 是python解释器在创建类的时候自动创建的
作用: 1. 通过类对象,去定义实例对象   2. 类对象可以保存一些属性信息,称为类属性
类属性的定义: 在类内部,方法外部定义的变量就是类属性
类属性,内存中只有一份

如何确定一个属性是该定义为实例属性还是类属性?
先假设这个属性为实例属性,查看这个属性值对于不同的实例对象, 属性值是否都一样,并且需要同时变化.
如果是, 则可以定义为类属性
如果不是,则可以定义为实例属性

```python
class Dog(object):
    # 定义类属性, 类名
    class_name = '狗类'

    def __init__(self, name, age):
        # 定义的都是实例属性
        self.name = name
        self.age = age


# 创建Dog 类对象
dog = Dog('大黄', 2)
# print(dog.__dict__)  # 打印dog对象具有的属性

# 类名.__dict__  查看类对象具有的属性
# print(Dog.__dict__)

# 访问类属性
# 类名.类属性
print(Dog.class_name)

# 修改类属性  类名.类属性 = 属性值
Dog.class_name = 'Dog类'

print(Dog.class_name)

# 补充, 注意: 如果不存在和实例属性名相同的类属性.则可以使用实例对象访问类属性的值
# 如果存在重名,则使用实例属性访问的一定是实例属性,不是类属性
print(dog.class_name)

```

## 类方法

实例方法: 类中默认定义的方法,就是实例方法, 第一个参数为self,表示实例对象

类方法: 使用 @classmethod 装饰的方法,称为类方法, 第一个参数是cls,代表的是类对象自己
什么情况定义为实例方法,什么情况定义为类方法?
1. 如果在方法中使用了实例属性, 那么该方法必须定义为实例方法
2. 前提:不需要使用实例属性. 需要使用类属性,可以将这个方法定义为类方法

```python
class Dog(object):
    class_name = '狗类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):  # 实例方法
        print(f"小狗{self.name} 在快乐的玩耍....")

    # def get_class_name(self):  # 是实例方法, 因为没有使用实例属性,所以可以定义为类方法
    #     return Dog.class_name

    @classmethod
    def get_class_name(cls):  # cls 是类方法的默认形参,在调用的时候,不需要手动传递,python解释器会自动传递
        return cls.class_name


dog = Dog('大黄', 2)
dog.play()
print(dog.get_class_name())   # 对象.类方法()

# 类名.类方法()
print(Dog.get_class_name())

```

## 静态方法

实例方法: 类中默认定义的方法,就是实例方法, 第一个参数为self,表示实例对象
类方法: 使用 @classmethod 装饰的方法,称为类方法, 第一个参数是cls,代表的是类对象自己
静态方法: 使用 @staticmethod 装饰的方法,称为静态方法, 对参数没有特殊要求,可以有,可以没有
什么情况定义为实例方法,什么情况定义为类方法, 什么情况下静态方法?
1. 如果在方法中使用了实例属性, 那么该方法必须定义为实例方法
2. 前提:不需要使用实例属性. 需要使用类属性,可以将这个方法定义为类方法
3. 前提:不需要使用实例属性,同时也不需要使用类属性, 此时可以将这个方法定义为静态方法

```python
class Dog(object):
    class_name = '狗类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):  # 实例方法
        print(f"小狗{self.name} 在快乐的玩耍....")

    @staticmethod  # 定义静态方法
    def show_info():
        print('这是一个Dog类')


dog = Dog('大黄', 2)
dog.play()
# 对象.方法名()
dog.show_info()
# 类名.方法名()
Dog.show_info()
```

## 多态

在需要使用父类对象的地方,也可以传入子类对象,得到不同的结果 ---- 多态
实现步骤:
1. 子类继承父类
2. 子类重写父类中的同名方法
3. 定义一个共同的方法, 参数为父类对象.在方法中调用子类和父类同名的方法

```python
# 1. 定义Dog类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'小狗{self.name} 在玩耍.......')


# 2. 定义哮天犬类,继承Dog类
class XTQ(Dog):
    # 3. 重写 play方法
    def play(self):
        print(f'{self.name} 在天上追云彩.....')


# 4. 定义一个共同的方法,
def play_with_dog(obj_dog):
    obj_dog.play()


# 创建Dog类对象@
dog = Dog('大黄')
play_with_dog(dog)

# 创建一个XTQ类的对象
xtq = XTQ('小黑')
play_with_dog(xtq)

```

```
小狗大黄 在玩耍.......
小黑 在天上追云彩.....
```

### 鸭子类型

```python
class Cat(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'小猫{self.name} 被撸中...')


cat = Cat('小花')
play_with_dog(cat)
```
