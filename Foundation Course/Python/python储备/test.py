'''
a=0
list1=input().split()
for i in list1:
    a+=int(i)
print( f'%d %.1f' %(a,a/len(list1)))
'''

'''
a=0
list1=input().split()
for i in list1:
    a+=int(i)
print( a,end=' ')
print(a/len(list1))

my_list=[]
for i in range(0,20,2):
    my_list.append(i)
for j in my_list:
    print(j)

my_list = list(range(0, 19, 2))
print(my_list)

my_list=list(range(5,51,5))
for i in my_list:
    print(i)
'''

# for i in range(-5,-1):
#     print(i)

# list1=['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
# for i in range(-5,1):
#     list1.pop(-i)
#     print(list1)


# list1=list(range(1,16))
# for i in list1:
#     if i==13:
#         continue
#     print(i,end=' ')


# list1=[[1,2,3],[4,5,6],[7,8,9]]
# n=int(input())
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         list1[i][j]=list1[i][j]*n
# print(list1)


# a=input()
# b=input()
# c=a,b
# print(c)


'''
entry_form=('Niuniu','Niumei')
print(entry_form)
try:
    entry_form[1]='Niukele'
except:
    print("The entry form cannot be modified!")
'''


# x=tuple(input().split())
# print(x[0:3])


# c=tuple('abcdefg')
# print(c)

# a=input("").split()
# b=tuple(a)
# print(b)

# a='s'
# b=tuple(a)
# print(b)

'''
a='Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna'
print(a)
b=input()
if b in a:
    print('Congratulations!')
else:
    print('What a pity!')

t = tuple(['Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna'])
print(t,'Congratulations!' if input() in t else 'What a pity!',sep='\n')

'''


#66
# a=tuple(list(range(1,6)))
# print(a,len(a),sep="\n")
# b=tuple(list(range(6,11)))
# print(a+b,len(a+b),sep="\n")

#67
# operators_dict={'<' :'less than','==':'equal'}
# print('Here is the original dict:')
# for i in sorted(operators_dict):
#     print(f'Operator {i} means {operators_dict[i]}.')
# operators_dict['>']='greater than'
# print()
# print('The dict was changed to:')
# for j in sorted(operators_dict):
#     print(f'Operator {j} means {operators_dict[j]}.')


# 94
# def cal():
#     x=int(input())
#     y=int(input())
#     print(x-y)
#     print(y-x)
#     return
# cal()

#lambda 匿名函数
# cal = lambda x, y : x-y
# x = int(input())
# y = int(input())
# print(cal(x, y))
# print(cal(y, x))

#95
# def rabbit(n):
#     if n==1:
#         return 2
#     if n==2:
#         return 3
#     else:
#         return rabbit(n-1)+rabbit(n-2)
# i=int(input())
# print(rabbit(i))

# a = 2
# b = 3
# n = int(input())
# for i in range(n-1):
#     a,b = b,a+b
# print(a)
        

#96
# import math
# def surface(r):
#     for i in r:
#         a=int(i)
#         v=4*math.pi*i**2
#         print(f'%.2f' %v)
#     return
# surface([1, 2, 4, 9, 10, 13])



# from math import pi
# def v(r: int):
#     return 4 * pi * (r ** 2)

# lists = [1, 2, 4, 9, 10, 13]
# for r in lists:
#     print(f"{v(r):.2f}")


# 97
# class Student(object):
#     def __init__(self, name,number,grade,level):
#         self.name = name
#         self.number = number
#         self.grade = grade
#         self.level = level
#         self.times = len(level.split(' '))
#     def p(self):
#         return "{}'s student number is {}, and his grade is {}. He submitted {} assignments, each with a grade of {}".format(self.name,self.number,self.grade,self.times,self.level)
# name = input()
# number = input()
# grade = int(input())
# level = input()
# student = Student(name,number,grade,level)
# print(student.p())

#https://zhuanlan.zhihu.com/p/30024792 类属性
# class Circle(object):  # 创建Circle类，Circle为类名
#    pass  # 此处可添加属性和方法
# 在定义 Circle 类时，可以为 Circle 类添加一个特殊的 __init__() 方法，当创建实例时，__init__() 方法被自动调用为创建的实例增加实例属性。
# class Circle(object):  # 创建Circle类
#    def __init__(self, r): # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
#        self.r = r  # 表示给我们将要创建的实例赋予属性r赋值
# 注意：__init__() 方法的第一个参数必须是 self（self代表类的实例，可以用别的名字，但建议使用约定成俗的self），后续参数则可以自由指定，
# 和定义函数没有任何区别。
# circle1 = Circle(1)  # 创建实例时直接给定实例属性，self不算在内
# circle2 = Circle(2)
# print(circle1.r)  # 实例名.属性名 访问属性
# print(circle2.r)  # 我们调用实例属性的名称就统一了
# 注意：实例名.属性名 circle1.r 访问属性，是我们上面Circle类__init__() 方法中 self.r 的 r 这个实例属性名，
# 而不是__init__(self, r)方法中的 r 参数名，如下更加容易理解：

# class Circle(object):  # 创建Circle类
#    def __init__(self, R):  # 约定成俗这里应该使用r，它与self.r中的r同名
#        self.r = R

# circle1 = Circle(1)  
# print(circle1.r)  #我们访问的是小写r
# 面试喜欢问的问题：创建类时，类方法中的self是什么？
# self 代表类的实例，是通过类创建的实例 (注意，在定义类时这个实例我们还没有创建，它表示的我们使用类时创建的那个实例)
# 实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。实例属性访问优先级比类属性高，所以我们访问时优先访问实例属性，
# 它将屏蔽掉对类属性的访问。


# 98
# class Employee(object):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         pass
#     def printclass(self):
#         return "{}'salary is {}, and his age is {}".format(self.name,self.salary,self.age)

# name = input()
# salary = int(input())
# age=int(input())
# try:
#     e = Employee(name, salary, age)
#     e.printclass()
# except:
#     print("Error! No age")

# try:
#     emp = Employee(name, salary)
#     emp.age = age  #动态给对象加属性
#     print(emp.printclass())
# except:
#     print("Error! No age")


# 99
# class Employee(object):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         pass
#     def printclass(self):
#         return "{}'salary is {}, and his age is {}".format(self.name,self.salary,self.age)

# name = input()
# salary = int(input())
# age=int(input())

# e = Employee(name,salary)
# if not hasattr(e,'age'):
#     print(False)
#     setattr(e, "age", age) #此处需用双引号
#     e.printclass(name, salary, age)
# else:
#     print(True)

#属性的添加有两种方式：直接在类定义中添加（类里的属性所有实例化的对象都可以拥有此属性也可以修改），
#另一种方式就是对象添加，这个添加的对象只对该对象有效，其他对象没有此属性
#setattr(object, name, value)
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def printclass(self):
#         try :
#             print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")
#         except :
#             print("Error! No age")
    
# name = input()
# salary = input()
# age= input()
# e = Employee(name,salary)
# if print(hasattr(e,'age')) :
#     e.printclass()
# else:
#     setattr(e,"age",age)
#     e.printclass()
 


#100

# class Coordinate(object):
#     def __init__(self,x,y) -> None:
#         self.x=x
#         self.y=y
#         pass

x1,y1 = [1,2]
print(x1)