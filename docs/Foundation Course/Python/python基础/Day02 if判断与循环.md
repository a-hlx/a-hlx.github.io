## if

```python
age=int(input("请输入年龄:"))
if age>=18:
    print("cool!")
print("if 结构结束")
```

## if else

```python
age=int(input("请输入年龄:"))
if age>=18:
    print("cool!")
else:
    print("sad")
```

## if elif
```python
if 	判断条件1:
    判断条件1成立,执行的代码
elif 判断条件2:
    判断条件1不成立,判断条件2 成立,会执行的代码
else:
    判断条件1和判断条件2都不成立,执行的代码
--------
if 判断条件1:
    判断条件1成立执行的代码
    
if 判断条件2:
    判断条件2 成立执行的代码
```

```python
score = eval(input('请输入你的成绩:'))
# 1. 成绩大于等于90 ，输出优秀
if score >= 90:
    print('优秀')
# 2. 成绩大于等于80，小于90，输出良好
elif (score >= 80) and score < 90:
    print('良好')
# 3. 成绩大于等于60，小于80，输出及格
elif score >= 60:  # 想要执行这个判断的前提是,前边两个条件都不成立
    print('及格')
# 4. 小于60，输出不及格
else:
    print('不及格')

print("程序结束")
```

## if 嵌套
```
if 判断条件1:  
    判断条件1 成立,会执行的代码  
    if 判断条件2:  
        判断条件1成立, 判断条件2成立执行的代码  
    else:  
        判断条件1成立, 判断条件2不成立执行的代码  
else:  
    判断条件1不成立,会执行的代码
```

## 随机数
```python
import random  # 导入随机数模块
 #[a, b] 之间的随机整数,包含 a 和 b
num = random.randint(a, b) 
```

伪随机数，可进行攻击
```
x=random.getstate()
random.randint(1,10)
random.setstate(x)
```

### 猜拳游戏
```python
import random
a=int(input("输入你想出的拳，石1，剪2，布3："))
b=random.randint(1, 3)
print(b)
if a==b:
	print('平')
elif (a==1 and b==2) or (a==2 and b==3)  or (a==3 and b==1):
	print('赢')
else:
	print('输')
```

## 目运算

<font color=#FF0212>if else 结构变形</font>

```
变量 = 表达式1 if 判断条件 else 表达式2  # 推荐使用扁平化代码

变量最终存储的结构是: 
    判断条件成立,表达式1的值, 
    条件不成立,表达式2的值
```

```python
a = int(input('请输入一个数字:'))
b = int(input('请输入一个数字:'))

result = a - b if a > b else b - a
result = (a - b) if a > b else (b - a)
print(result)

```

## 循环
while 判断条件:
    判断条件成立,执行的代码
    判断条件成立,执行的代码
    
不在 while 的缩进内,代表和循环没有关系    

while 和 if 的区别:
    if 的代码块,条件成立,只会执行一次
    while 的代码块,只要条件成立,就会一直执行

```python
i=1
sum=0
while i<=100:
	sum=sum+i
	i=i+1
print(sum)
```

```python
my_sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        my_sum += i  # my_sum = my_sum + i
    i += 1
print('求和的结果为', my_sum)
```

`sum+=i     i+=1`

`while True:`

### 猜拳游戏while
```python
while True:
```

## 循环嵌套
while 判断条件1:
    代码1
    while 判断条件2:
        代码2

## for 循环遍历

### for 变量 in 字符串
```python
for i in 'hello':
    print(i, end=' ')
```

### range
```python
# range(n)  会生成 [0, n) 的数据序列, 不包含n
for i in range(5):  # 0 1 2 3 4
    # print(i)
    print('操场跑圈...')

# range(a, b)  会生成 [a, b) 的整数序列, 不包含b
for i in range(3, 7):  # 3 4 5 6
    print(i)

# range(a, b, step) 会生成[a, b) 的整数序列,但是每个数字之间的间隔(步长)是step
for i in range(1, 10, 3):  # 1 4  7
    print(i)
```

## Break 和 continue

1. break 和 continue 是 python 两个关键字  
2. break 和 continue 只能用在循环中  
3. break 是终止循环的执行, 即循环代码遇到 break,就不再循环了  
    continue 是结束本次循环,继续下一次循环, 即本次循环剩下的代码不再执行,但会进行下一次循环

```python
# 有五个苹果
# 1. 吃了三个苹果之后, 吃饱了.后续的苹果不吃了,break
# 2. 吃了三个苹果之后.在吃第四个苹果,发现了半条虫子,这个苹果不吃了,还要吃剩下的苹果,continue

for i in range(1, 6):
    if i == 4:
        print('吃饱了, 不吃了')
        break  # 终止循环的执行
    print(f'正在吃标号为 {i} 的苹果')
```

```python
for i in range(1, 6):
    if i == 4:
        print('发现半条虫子,这个苹果不吃了, 没吃饱,继续吃剩下的')
        continue  # 会结束本次循环,继续下一次循环

    print(f'吃了编号为{i}的苹果')
```

## 循环 else 结构
for x in xx:
    if xxx:
        xx  # if 判断条件成立会执行
    else:
        xxx  # if 判断条件不成立,会执行
else:
    xxx  # for 循环代码运行结束,但是不是被 break 终止的时候会执行

```python
my_str = 'hello python!'
# my_str = 'hello itcast!'

for i in my_str:
    if i == 'p':
        print('包含p这个字符')
        # 已经判断出来包含了,是否还需要继续判断
        break
else:
    print('不包含p这个字符')

```

## 实例

### 打印正方形

```python
while True:
    a=int(input('请输入边长:'))
    j=1
    while j<=a:
        i=1
        while i<=a:
            print('*',end='')
            i+=1
        print()
        j+=1
```

```python
a=int(input('请输入边长:'))
for j in range(a):
	for i in range(a):
		print('*',end='')
	print()
```

### 打印正三角形
```python
n = 5

# 2. 定义变量,记录打印的行数
j = 1  # 将要打印第一行
while j <= n:
    # 1. 定义变量记录一行打印的*个数
    i = 1  # 将要打印第一个
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1


# for循环打印三角形
for i in range(n):  # 控制行数
    for j in range(i+1):  # i  range(i) 不包含i  , 控制一行打印的个数
        print('*', end=' ')
    print()

```

### 求个位十位数

num = 76

使用代码的方法,求出这个数字的个位数和十位数

个位数: num % 10 

十位数: num // 10

