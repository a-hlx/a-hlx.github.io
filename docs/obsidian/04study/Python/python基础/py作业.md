# day01
## 1.use print

```python
name="hlx"
height=170
weight=60
print(f"名字是{name},身高{height}cm,体重{weight}kg")
```

```python
height=170
#本来几位小数，默认显示几位
print(f"身高{height}cm")
身高170cm

print(f"身高{height:.2f}cm")
```

`显示位数`
print(f"身高{height`:.2f`}cm")

# day02
### 年龄判断
用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。
年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。
```python
age=int(input('请输入年龄:'))
if (age >= 0) and (age < 17):
    print(f'您的年龄是{age}: 青少年')
elif (age >= 18) and (age < 35): 
    print(f'您的年龄是{age}: 青年')
elif (age >= 35) and (age < 59):
    print(f'您的年龄是{age}: 中年')
elif (age >= 59) and (age < 99):
    print(f'您的年龄是{age}: 老年')
```

### 用户登录
制作用户登录系统：已知A用户注册的用户名为aaa，密码是123456。具体要求如下：
登录时需要验证用户名、密码、验证码(固定验证码为qwer)。
提示：系统先验证验证码是否正确，正确后再验证用户名和密码。

```python
# 用户名、密码、验证码数据
sys_name = 'aaa'
sys_pwd = '123456'
sys_code = 'qwer'

# 用户输入用户名、密码、验证码
user_name = input('请输入用户名：')
user_pwd = input('请输入密码：')
user_code = input('请输入验证码：')

if user_code == sys_code:
    print('验证码正确')
    if user_name == sys_name and user_pwd == sys_pwd:
        print('恭喜您，登录成功')
    else:
        print('用户名或密码错误，请重新输入')
else:
    print('验证码错误，请重新输入')
```

### 过7游戏
设计"过7 游戏” 程序,即在 1- 99 之间的数字中,如果数字 包含 7 或者是 7 的倍数,则输出"过...", 否则输出 具体的数字.

-   判断一个数是否是 7 的倍数，即能否被 7 整除，在 python 可以使用`%` 运算符
-   判断一个数字是否包含 7，可能个位是 7，也可能是十位数字是 7 
    -   判断个位 ，使用 `num % 10 == 7`
    -   判断十位，使用 `num // 10 == 7`

```
i = 1
# 使用循环得到 1-100 之间的数字
while i < 100:
    # 判断是否是 7 的倍数和包含 7 , 两者之间是或的关系,满足一个即输出过
    if (i % 7 == 0) or (i % 10 == 7) or (i // 10 == 7):
        print('过...')
    else:
        # 不是 7 的倍数,也没有包含 7,直接输出数字
        print(i)
    # 一个数字判断结束之后,改变 i 的值
    i += 1
```

```python
for i in range(1,100):
    if i % 7==0:
        print('过')
    else:
        print(i)

```


# day03


