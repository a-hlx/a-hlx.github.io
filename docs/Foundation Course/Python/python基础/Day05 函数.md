## 函数传参形式

```python
def func(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")


# 位置传参：按照形参的位置顺序将实参的值传递给形参。
func(1, 2, 3)

# 关键字传参：指定实参给到哪个形参。注意点: 关键字必须是函数的形参名。
func(b=10, a=20, c=30)

# 混合使用：先写位置传参,再写关键字传参。
func(10, b=20, c=30)
```

## 缺省参数(默认参数)

缺省参数:形参在函数定义的时候,给形参一个默认值,这个形参就是缺省参数,
注意点: 缺省参数要写在普通参数的后边
特点: 在函数调用的时候,如果给缺省参数传递实参值,使用的是传递的实参值,如果没有传递,使用默认值

```python
def func(a, b, c=10):  # 形参c 称为缺省形参
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")


func(1, 2)  # 没有给c 传递实参,使用默认值10
func(1, 2, 3)  # 给c传递实参值,使用传递的数据3

# 缺省参数后面全是缺省参数！
# def fun(a=1, b, c):  # 代码报错,语法错误。
#     pass

```

## 不定长参数

```python
# 在形参前边加上一个*, 该形参变为不定长元组形参,可以接收所有的位置实参,类型是元组
# 在形参前边加上两个*, 该形参变为不定长字典形参,可以接收所有的关键字实参,类型是字典
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, 3, 4, 5)
func(a=1, b=2, c=3, d=4)
func(1, 2, 3, a=4, b=5, d=6)
```

结果:
```
(1, 2, 3, 3, 4, 5)
{}
()
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
(1, 2, 3)
{'a': 4, 'b': 5, 'd': 6}
```
### 应用

```python
def my_sum(*args, **kwargs):
    num = 0
    for i in args:
        num += i  # num = num + i
    for j in kwargs.values():
        num += j
    print(f"求和的结果为{num}！")
my_sum(1, 2, 3, a=4, b=5, c=6)


from math import pi
def v(r: int):
    return 4 * pi * (r ** 2)
lists = [1, 2, 4, 9, 10, 13]
for r in lists:
    print(f"{v(r):.2f}")
```

## 函数形参的完整格式

```python
# 普通形参  缺省形参  不定长元组形参   不定长字典形参
def func(a, b=1):  # 先普通再 缺省
    pass


def func1(a, b=1, *args):  # 语法上不会报错,但是缺省参数不能使用默认值
    print('a', a)
    print('b', b)
    print(args)


def func2(a, *args, b=1):  # 普通形参 不定长元组形参 缺省形参
    print('a', a)
    print('b', b)
    print(args)


# 普通形参 不定长元组形参 缺省形参 不定长字典形参
def func3(a, *args, b=1, **kwargs):
    pass


func1(1, 2, 3, 4)
func2(1, 2, 3, 4)
func2(1, 2, 3, 4, b=10)
```

```
a 1
b 2
(3, 4)
a 1
b 1
(2, 3, 4)
a 1
b 10
(2, 3, 4)

```

## 闭包
又称工厂函数:在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

```python
#闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer( a ):
    b = 10
    # inner是内函数
    def inner():
        #在内函数中 用到了外函数的临时变量
        print(a+b)
    # 外函数的返回值是内函数的引用
    return inner

if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    #此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    demo() # 15

    demo2 = outer(7)
    demo2()#17
```

```python
def power(exp):
    def exp_of(base):
        return base**exp
    return exp_of
square=power(2)
code=power(3)
square(5) #25
code(3)  #9
```

## 拆包

注意点: 容器中元素数据的个数需要和变量的个数保持一致.

```python

# 组包：将多个数据值,组成元组,给到一个变量。
a = 1, 2, 3
print(a)  # (1, 2, 3)


def func():
    return 1, 2  # 组包


# 拆包：将容器的数据分别给到多个变量。需要注意: 数据的个数和变量的个数要保持一致。
b, c, d = a  # 拆包
print(b, c, d)  # 1 2 3

e, f = func()
print(e, f)  # 1 2

my_list = [10, 20]
a, b = my_list
print(a, b)  # 10 20

my_dict = {'name': 'isaac', 'age': 18}
a, b = my_dict  # 字典->key值
print(a, b)  # name age
```

### 补充

```python
def func(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    num = 0
    # for i in args:
    #     num += i  # num = num + i
    #
    # for j in kwargs.values():
    #     num += j
    #
    # print(f"求和的结果为{num}")


my_list = [1, 2, 3, 4, 5, 6]
my_dict = {'a': 7, 'b': 8, 'c': 9, 'd': 10}

func(my_list)  # 将列表作为一个数据进行传递
func(*my_list)  # 将列表中的每一个数据作为位置参数进行传递, 拆包
func(my_dict)  # 将my_dict 作为一个位置实参进行传递
func(*my_dict)  # 将my_dict中的key 作为位置实参进行传递
func(**my_dict)  # 将my_dict中键值对作为关键字实参进行传递
```

## 交换两变量值

```python
a = 10
b = 20

# 方法一:
c = a
a = b
b = c
print(a, b)  # 20 10

# 方法二: +/-   */÷
# a = a + b  # a 30
# b = a - b  # b 10
# a = a - b  # a 20
print(a, b)  # 20 10

# 方法三, python中的使用 组包和拆包
a, b = b, a
print(a, b)  # 10 20
```

## 引用

可以使用id()查看变量的引用,可以将id值认为是内存地址的别名。
python中数据值的传递的是引用
赋值运算符可以改变变量的引用
交互终端小整数-5~255范围内使用相同引用地址

```python
# 将数据10存储到变量a中,本质是将数据10所在内存的引用地址保存到变量a中
a = 10
# 将变量a中保存的引用地址给到b
b = a
# 使用print函数打印变量a和b引用中存储的值：
print(a, b)  # 10 10
print(id(a), id(b))  # 140721731917760 140721731917760
a = 20
print(a, b)  # 20 10
print(id(a), id(b))  # 140721731918080 140721731917760
```

```python
my_list0 = [1, 2, 3]  # 将列表的引用地址保存到变量my_list中
my_list1 = my_list0  # 将my_list 变量中存储的引用地址给到my_list1
print(my_list0, id(my_list0))  # [1, 2, 3] 1643711423040
print(my_list1, id(my_list1))  # [1, 2, 3] 1643711423040

my_list0.append(4)  # 向列表中添加数据4,将数据4 的引用保存到列表中
print(my_list0, id(my_list0))  # [1, 2, 3, 4] 1643711423040
print(my_list1, id(my_list1))  # [1, 2, 3, 4] 1643711423040

my_list0[2] = 5  # 改变my_list0中一个数字的引用
print(my_list0, id(my_list0))  # [1, 2, 5, 4] 1643711423040
print(my_list1, id(my_list1))  # [1, 2, 5, 4] 1643711423040
```

## 可变与不可变类型

类型的可变与不可变: 在不改变变量引用的前提下,能否改变变量中引用中的数据,
如果能改变是可变类型, 如果不能改变,是不可变类型
int float bool str list tuple dict
不可变类型: int float bool str  tuple
可变类型: list dict

```python
a = 1000
b = 1000
print(id(a), id(b))  # python中的内存优化,对于不可变类型进行的,
print(id(a) == id(b))  # True

a = 'hello'
b = 'hello'
print(id(a), id(b))  # python中的内存优化,对于不可变类型进行的,
print(id(a) == id(b))  # True

my_list = [1, 2, 3]
my_list1 = [1, 2, 3]
print(id(my_list), id(my_list1))
print(id(my_list) == id(my_list1))  # False

my_tuple2 = (1, 2, [3, 4])
my_tuple1 = my_tuple2
my_tuple2[2][1] = 10
print(id(my_tuple1) == id(my_tuple2))  # True
```

## 引用做函数参数注意点

```python
# 函数传参传递的也是引用
my_list = [1, 2, 3]  # 全局变量


def func1(a):
    a.append(4)


def func2():
    # 为啥不加global, 因为没有修改my_list中存的引用值
    my_list.append(5)


def func3():
    global my_list
    my_list = [1, 2, 3]  # 修改全局变量的值


def func4(a):
    # += 对于列表来说,类似列表的extend方法,不会改变变量的引用地址
    a += a  # a = a + a, 修改了a变量a的引用
    # print(a)


func1(my_list)  # [1, 2, 3, 4]
print(my_list)  # [1, 2, 3, 4]
func2()  # [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]
func3()  # [1, 2, 3]
print(my_list)  # [1, 2, 3]

b = 10  # 不可变类型
func4(b)
print(b)  # 10

func4(my_list)
print(my_list)  # [1, 2, 3, 1, 2, 3]
```

## 学生管理系统

```python
stu_list = []  # 定义学生列表,保存所有的学生信息


def show_menu():
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


def insert_student():
    # 1. 通过 input 函数获取学生的信息, 姓名, 年龄, 性别
    name = input('请输入学生名字:')
    # [{}, {}, {}]  判断的是字典中的value是否存在
    for stu in stu_list:
        if stu['name'] == name:
            print('----------学生信息存在----------')
            return  # 结束函数的执行
    age = input('请输入学生年龄:')
    gender = input('请输入学生性别:')
    # 2. 将学生信息转换为字典进行保存
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}
    # 3. 将这个学生字典添加的列表中
    stu_list.append(stu_dict)
    print('==============学生信息添加成功==============')


def remove_student():
    # 1. 使用 input 获取要删除/修改/查询的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行删除/修改/查询操作
            stu_list.remove(stu)
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在,无法删除***********')


def modify_student():
    # 1. 使用 input 获取要删除/修改/查询的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行删除/修改/查询操作
            stu['age'] = int(input('请输入新的年龄:'))
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在,无法修改***********')


def search_student():
    # 1. 使用 input 获取要删除/修改/查询的学生姓名
    name = input('请输入要操作的学生的名字:')
    # 2. 判断学生信息是否存在
    for stu in stu_list:
        if stu['name'] == name:
            # 3. 学生存在,对学生进行删除/修改/查询操作
            print(f'姓名:{stu["name"]}, 年龄:{stu["age"]}, 性别:{stu["gender"]}')
            # return
            break
    # 4. 学生信息不存在,直接结束
    else:
        print('***********该学生信息不存在***********')


def show_all_info():
    if len(stu_list) > 0:
        for stu in stu_list:
            print(f'姓名:{stu["name"]}、年龄:{stu["age"]}、性别:{stu["gender"]}')
            # print(stu)
    else:
        print('目前没有学生信息')


def main():
    while True:
        show_menu()
        opt = input('请输入用来选择的操作编号:')
        if opt == '1':
            # print('1. 添加学生')
            insert_student()
        elif opt == '2':
            # print('2. 删除学生')
            remove_student()
        elif opt == '3':
            # print('3. 修改学生信息')
            modify_student()
        elif opt == '4':
            # print('4. 查询单个学生信息')
            search_student()
        elif opt == '5':
            # print('5. 查询所有的学生信息')
            show_all_info()
        elif opt == '6':
            print('欢迎下次使用本系统......')
            break
        else:
            print('输入有误,请再次输入')
            continue
        input('...... 回车键继续操作.......')


main()
```






