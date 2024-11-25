#2024.11.25

name = "Alice"
age = 20
height = 185
is_student = True
#常见数据类型
message = "Hello " + "world!"
print(message[0:5])

#练习
print(f"My name is {name}, I am {age} years old. Student: {is_student}")
#f-string：在字符串前加 f，可以在字符串中直接嵌入变量或表达式，使用大括号 {} 包裹。

#运算符和基础操作
a = 10
b = 3
#加法 `+`，减法 `-`，乘法 `*`，除法 `/`，整除 `//`，取余 `%`，幂运算 `**`
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

#逻辑运算符
x = True
y = False
print(x and y,x or y,not x )
#字符串拼接- 使用 `+` 拼接字符串。- 使用 `*` 重复字符串
print("Hello"+" " ""+"World!")
print(" python " * 3)

ratio = age / height

# 打印结果
print(f"My name is {name}, I am {age} years old.")
print(f"My height is {height} cm, and age-height ratio is {ratio:.2f}.")