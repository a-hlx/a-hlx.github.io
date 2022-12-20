[(15条消息) 浅析Python运算符重载_viclee108的博客-CSDN博客_python重载运算符](https://blog.csdn.net/goodlixueyong/article/details/52589979)       
       
       Python语言提供了运算符重载功能，增强了语言的灵活性，这一点与C++有点类似又有些不同。鉴于它的特殊性，今天就来讨论一下Python运算符重载。

      Python语言本身提供了很多魔法方法，它的运算符重载就是通过重写这些Python内置魔法方法实现的。这些魔法方法都是以双下划线开头和结尾的，类似于__X__的形式，python通过这种特殊的命名方式来拦截操作符，以实现重载。当Python的内置操作运用于类对象时，Python会去搜索并调用对象中指定的方法完成操作。

       类可以重载加减运算、打印、函数调用、索引等内置运算，[运算符](https://so.csdn.net/so/search?q=%E8%BF%90%E7%AE%97%E7%AC%A6&spm=1001.2101.3001.7020)重载使我们的对象的行为与内置对象的一样。Python在调用操作符时会自动调用这样的方法，例如，如果类实现了__add__方法，当类的对象出现在+运算符中时会调用这个方法。

**常见运算符重载方法**

<table><tbody><tr><td><p>方法名</p></td><td><p>重载说明</p></td><td><p>运算符调用方式</p></td></tr><tr><td><p><span>__init__</span></p></td><td><p><span>构造函数</span></p></td><td><p><span>对象创建: X = Class(args)</span></p></td></tr><tr><td><p><span>__del__</span></p></td><td><p><span>析构函数</span></p></td><td><p><span>X对象收回</span></p></td></tr><tr><td><p><span>__add__/__sub__</span></p></td><td><p>加减运算</p></td><td><p><span>&nbsp;X+Y， X+=Y/X-Y， X-=Y</span></p></td></tr><tr><td><p><span>__or__</span></p></td><td><p><span>运算符|</span></p></td><td><p><span>X|Y, X|=Y</span></p></td></tr><tr><td><p><span>_repr__／__str__</span></p></td><td><p><span>打印／转换</span></p></td><td><p><span>print(X)、repr(X)／str(X)</span></p></td></tr><tr><td><p><span>__call__</span></p></td><td><p><span>函数调用</span></p></td><td><p><span>X(*args, **kwargs)</span></p></td></tr><tr><td><p><span>__getattr__</span></p></td><td><p>属性引用</p></td><td><p><span>X.undefined</span></p></td></tr><tr><td><p><span>__setattr__</span></p></td><td><p><span>属性赋值</span></p></td><td><p><span>X.any=value</span></p></td></tr><tr><td><p><span>__delattr__</span></p></td><td><p><span>属性删除</span></p></td><td><p><span>del X.any</span></p></td></tr><tr><td><p><span>__getattribute__</span></p></td><td><p><span>属性获取</span></p></td><td><p><span>X.any</span></p></td></tr><tr><td><p><span>__getitem__</span></p></td><td><p><span>索引运算</span></p></td><td><p><span>X[key]，X[i:j]</span></p></td></tr><tr><td><p><span>__setitem__</span></p></td><td><p><span>索引赋值</span></p></td><td><p><span>X[key]，X[i:j]=sequence</span></p></td></tr><tr><td><p><span>__delitem__</span></p></td><td><p><span>索引和分片删除</span></p></td><td><p><span>del X[key]，del X[i:j]</span></p></td></tr><tr><td><p><span>__len__</span></p></td><td><p><span>长度</span></p></td><td><p><span>len(X)</span></p></td></tr><tr><td><p><span>__bool__</span></p></td><td><p><span>布尔测试</span></p></td><td><p><span>bool(X)</span></p></td></tr><tr><td><p><span>__lt__, __gt__,&nbsp;</span></p><p><span>__le__, __ge__,&nbsp;</span></p><p><span>__eq__, __ne__</span></p></td><td><p><span>特定的比较</span></p></td><td><p><span>依次为X&lt;Y，X&gt;Y，X&lt;=Y，X&gt;=Y，&nbsp;</span></p><p><span>X==Y，X!=Y&nbsp;</span></p><p><span>注释：（lt: less than, gt: greater than,&nbsp;</span></p><p><span>&nbsp; le: less equal, ge: greater equal,&nbsp;</span></p><p><span>&nbsp; eq: equal, ne: not equal&nbsp;</span></p><p><span>）</span></p></td></tr><tr><td><p><span>__radd__</span></p></td><td><p><span>右侧加法</span></p></td><td><p><span>other+X</span></p></td></tr><tr><td><p><span>__iadd__</span></p></td><td><p><span>实地（增强的）加法</span></p></td><td><p><span>X+=Y(or else __add__)</span></p></td></tr><tr><td><p><span>__iter__, __next__</span></p></td><td><p><span>迭代</span></p></td><td><p><span>I=iter(X), next()</span></p></td></tr><tr><td><p><span>__contains__</span></p></td><td><p><span>成员关系测试</span></p></td><td><p><span>item in X(X为任何可迭代对象)</span></p></td></tr><tr><td><p><span>__index__</span></p></td><td><p><span>整数值</span></p></td><td><p><span>hex(X), bin(X),&nbsp; oct(X)</span></p></td></tr><tr><td><p><span>__enter__, __exit__</span></p></td><td><p><span>环境管理器</span></p></td><td><p><span>with obj as var:</span></p></td></tr><tr><td><p><span>__get__, __set__,&nbsp;</span></p><p><span>__delete__</span></p></td><td><p><span>描述符属性</span></p></td><td><p><span>X.attr, X.attr=value, del X.attr</span></p></td></tr><tr><td><p><span>__new__</span></p></td><td><p><span>创建</span></p></td><td><p><span>在__init__之前创建对象</span></p></td></tr></tbody></table>

       下面对常用的运算符方法的使用进行一下介绍。

**构造函数和析构函数：\_\_init\_\_和\_\_del\_\_**

       它们的主要作用是进行对象的创建和回收，当实例创建时，就会调用\_\_init\_\_构造方法。当实例对象被收回时，析构函数\_\_del\_\_会自动执行。

```
>>> class Human():... def __init__(self, n):... self.name = n...         print("__init__ ",self.name)... def __del__(self):... print("__del__")... >>> h = Human('Tim')__init__  Tim>>> h = 'a'__del__
```

**加减运算：\_\_add\_\_和\_\_sub\_\_**

       重载这两个方法就可以在普通的对象上添加＋－运算符操作。下面的代码演示了如何使用＋－运算符，如果将代码中的\_\_sub\_\_方法去掉，再调用减号运算符就会出错。

```
>>> class Computation():... def __init__(self,value):... self.value = value... def __add__(self,other):... return self.value + other... def __sub__(self,other):... return self.value - other... >>> c = Computation(5)>>> c + 510>>> c - 32
```

**  
对象的字符串表达形式：\_\_repr\_\_和\_\_str\_\_**

       这两个方法都是用来表示对象的字符串表达形式：print()、str()方法会调用到\_\_str\_\_方法，print()、str()和repr()方法会调用\_\_repr\_\_方法。从下面的例子可以看出，当两个方法同时定义时，Python会优先搜索并调用\_\_str\_\_方法。

```
>>> class Str(object):... def __str__(self):... return "__str__ called"    ... def __repr__(self):... return "__repr__ called"... >>> s = Str()>>> print(s)__str__ called>>> repr(s)'__repr__ called'>>> str(s)'__str__ called'
```

**索引取值和赋值：\_\_getitem\_\_, \_\_setitem\_\_**

       通过实现这两个方法，可以通过诸如 X\[i\] 的形式对对象进行取值和赋值，还可以对对象使用切片操作。

```
>>> class Indexer:data = [1,2,3,4,5,6]def __getitem__(self,index):return self.data[index]def __setitem__(self,k,v):self.data[k] = vprint(self.data)>>> i = Indexer()>>> i[0]1>>> i[1:4][2, 3, 4]>>> i[0]=10[10, 2, 3, 4, 5, 6]
```

**设置和访问属性：\_\_getattr\_\_、\_\_setattr\_\_**

       我们可以通过重载\_\_getattr\_\_和\_\_setattr\_\_来拦截对对象成员的访问。\_\_getattr\_\_在访问对象中不存在的成员时会自动调用。\_\_setattr\_\_方法用于在初始化对象成员的时候调用，即在设置\_\_dict\_\_的item时就会调用\_\_setattr\_\_方法。具体例子如下：

```
class A():def __init__(self,ax,bx):        self.a = ax        self.b = bxdef f(self):print (self.__dict__)def __getattr__(self,name):print ("__getattr__")def __setattr__(self,name,value):print ("__setattr__")        self.__dict__[name] = valuea = A(1,2)a.f()a.xa.x = 3a.f()
```

       上面代码的运行结果如下，从结果可以看出，访问不存在的变量x时会调用\_\_getattr\_\_方法；当\_\_init\_\_被调用的时候，赋值运算也会调用\_\_setattr\_\_方法。  

```
__setattr____setattr__{'a': 1, 'b': 2}__getattr____setattr__{'a': 1, 'x': 3, 'b': 2}
```

**迭代器对象: \_\_iter\_\_,  \_\_next\_\_**

       Python中的迭代，可以直接通过重载\_\_getitem\_\_方法来实现，看下面的例子。  

```
>>> class Indexer:... data = [1,2,3,4,5,6]... def __getitem__(self,index):...         return self.data[index]... >>> x = Indexer()>>> for item in x:... print(item)... 123456
```

       通过上面的方法是可以实现迭代，但并不是最好的方式。Python的迭代操作会优先尝试调用\_\_iter\_\_方法，再尝试\_\_getitem\_\_。迭代环境是通过iter去尝试寻找\_\_iter\_\_方法来实现，而这种方法返回一个迭代器对象。如果这个方法已经提供，Python会重复调用迭代器对象的next()方法，直到发生StopIteration异常。如果没有找到\_\_iter\_\_，Python才会尝试使用\_\_getitem\_\_机制。下面看一下迭代器的例子。

```
class Next(object):def __init__(self, data=1):self.data = datadef __iter__(self):return selfdef __next__(self):print("__next__ called")if self.data > 5:raise StopIterationelse:self.data += 1return self.datafor i in Next(3):print(i)print("-----------")n = Next(3)i = iter(n)while True:try:print(next(i))except Exception as e:break
```

       程序的运行结果如下：

```
__next__ called4__next__ called5__next__ called6__next__ called-----------__next__ called4__next__ called5__next__ called6__next__ called
```

       可见实现了\_\_iter\_\_和\_\_next\_\_方法后，可以通过for in的方式迭代遍历对象，也可以通过iter()和next()方法迭代遍历对象。