---
title: Python 基础
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Python 基础
description: Python 基础
tags:
  - Python
categories:
  - 编程
  - Python
date: 2023-10-25 10:30:00
abbrlink: 134405
password:
---

# Python 基础

## 介绍

ipython： 按 tab 键可补全可用 method 或 attributes；在函数或 method 后添加 `?` 可以查看其 docstring

在 jupyter notebook 中使用 Python 时，在函数或 method 后添加 `??` 可以查看其 docstring

[GitHub - gto76/python-cheatsheet: Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet)

终端 python 查看模块和函数帮助文档

```python
import numpy as np

help(numpy)
help(np)
help(np.array)

print(np.array.__doc__)
```

终端 python 查看模块和包的成员

```python
import numpy as np
dir(np)

print(np.__all__)
```

注：和 `dir()` 函数相比，`__all__` 变量在查看指定模块成员时，它不会显示模块中的特殊成员，同时还会根据成员的名称进行排序显示

---

什么是 python
- 解释性的脚本语言：通过解释器来直接运行，不需要编译链接成二进制文件
- 动态类型语言：类型在运行时确定，不需要通过代码明文规定
- 面向对象语言：python 中一切皆对象

>[Python 基础语法 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/pl/python/basic/)


>[GitHub - scruel/pcc\_3e\_slides: 《Python 编程：从入门到实践（第三版）》的官方配套图解讲义资源](https://github.com/scruel/pcc_3e_slides)


1. **Python 和 OpenMP**: Python 本身并不直接支持 OpenMP。OpenMP 主要用于 C/C++ 或 Fortran 等语言。然而，你可以通过 Cython 或其他扩展来在 Python 中使用 OpenMP。
2. **GIL（Global Interpreter Lock）**: Python 的 GIL 是一个互斥锁，它防止多个线程同时执行 Python 字节码。这意味着即使使用多线程，标准的 Python 解释器也无法实现真正的并行执行。不过，某些操作（如 I/O 或某些库函数）可以释放 GIL。



---

`copy()` 与 `deepcopy()` 的区别

- 使用 `copy()` 进行浅复制时，原对象和复制对象可能共享内部对象。
- 使用 `deepcopy()` 进行深复制时，原对象和复制对象是完全独立的，不共享内部对象。


---



在不打包的情况下使用其他路径的脚本
```python
import os
import sys

# 将脚本模板所在的目录添加到系统路径
home_path = os.getenv("HOME")
plot_scripts_path = os.path.join(home_path, "scripts/pdepp/2-plot-scripts")
sys.path.append(plot_scripts_path)

from va_elastic_prop_plot import elastic_prop_plot
```


---

### 参考资料

- [GitHub - lijin-THU/notes-python: 中文 Python 笔记](https://github.com/lijin-THU/notes-python)

- Python 速查表
	- [Python 3 备忘清单 & python cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/python.html)
	- [GitHub - gto76/python-cheatsheet: Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet)

- [GitHub - piglei/one-python-craftsman: 来自一位 Pythonista 的编程经验分享，内容涵盖编码技巧、最佳实践与思维模式等方面。](https://github.com/piglei/one-python-craftsman)

- 《编程不难》书籍源码：[GitHub - Visualize-ML/Book1\_Python-For-Beginners: Book\_1](https://github.com/Visualize-ML/Book1_Python-For-Beginners)

- Python tips and tools：[GitHub - pablovegan/Python-tips-tools: Short Python tips and tools talk for the Superconducting Qubit Technology school at Benasque 2023.](https://github.com/pablovegan/Python-tips-tools)





python classmethod 静态方法

在 Python 中，`@classmethod` 是一个装饰器，用于定义类方法（classmethods）。类方法是与类相关联的方法，而不是与类的实例相关联的方法。类方法可以通过类本身进行调用，而不需要创建类的实例。

类方法使用装饰器 `@classmethod` 来标记，通常以 `cls` 作为第一个参数，表示类本身。类方法可以访问类的属性和调用其他类方法，但不能直接访问实例属性，因为类方法不具有对实例的引用。

以下是一个具体的例子，展示了如何使用类方法：
```python
class MyClass:
    counter = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def increase_counter(cls):
        cls.counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter

# 创建两个实例
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# 调用类方法增加计数器的值
MyClass.increase_counter()
MyClass.increase_counter()

# 获取计数器的值
print(MyClass.get_counter())  # 输出: 2

```

在上述示例中，我们定义了一个名为 `MyClass` 的类，其中包含一个类属性 `counter` 和两个类方法 `increase_counter` 和 `get_counter`。类方法 `increase_counter` 通过 `cls` 参数来增加类属性 `counter` 的值。类方法 `get_counter` 通过 `cls` 参数返回类属性 `counter` 的值。

我们创建了两个 `MyClass` 的实例 `obj1` 和 `obj2`，但并没有使用它们来调用类方法。相反，我们直接使用类名 `MyClass` 调用了类方法 `increase_counter` 两次，以增加计数器的值。最后，我们使用类名 `MyClass` 调用了类方法 `get_counter` 来获取计数器的值，并打印出结果为 `2`。

需要注意的是，类方法不需要实例化对象就可以调用，它们是与类本身相关联的方法。




---

## 安装

建议使用 Miniconda3 安装


---

## 运行

- 在终端运行 Python 脚本

```bash
python script.py
```

- 在终端中直接执行 Python 代码，用于快速测试一些代码片段或进行简单的计算

```bash
python -c 'import matplotlib; print(matplotlib.matplotlib_fname())'
```

- 在终端中使用 Python 模块：`python -m`，通常用于运行可以作为脚本执行的模块，如 `venv`、`pip` 等；[Python's many command-line utilities - Python Morsels](https://www.pythonmorsels.com/cli-tools/)

```bash
# 创建虚拟环境
python -m venv venv

# 安装 package
python -m pip install <package>
```

- 查看 python 环境变量

```bash
python --help-env
```



---

## 工具

- 将 python 的计算公式转换成 LaTeX（一般，只能是简单的公式）：[GitHub - connorferster/handcalcs](https://github.com/connorferster/handcalcs)
- 打印 Python objects：[GitHub - gaogaotiantian/objprint](https://github.com/gaogaotiantian/objprint)
- 将打印的内容以表格的形式呈现：[GitHub - astanin/python-tabulate](https://github.com/astanin/python-tabulate)



---

## 语法

### 变量

- 动态类型，不需要规定类型（可通过 `变量名: 类型 = 内容` 来进行类型标注）

```python
x = 3
a: int = 3     # 类型标注
PI  = 3.14     # 全大写一般表示常量
_ = 3          # 临时变量
```


---

### 数据类型

#### 字符串

```python
str = "hello, world"

str1 + str2     # 字符串相加/拼接
str * 3         # 字符串与数字相乘
len(str)        # 字符串长度 


## 方法
# 分割
str.split(sep)    # 按照给定分隔符进行分割得到列表，默认空白

# 连接
lst = ["1", "2", "3"]
" ".join(lst)

# 替换
str.replace(old, new)

# 大小写转换
str.upper()     # 转为大写
str.lower()     # 转为小写
str.title()     # 首字母大写

# 去除多余空格
str.strip()     # 去除两端多余空格
str.lstrip()    # 删除左侧空格
str.rstrip()    # 删除右侧空格


# 多行字符串 用一对 """ 或 ''' 生成
str = """hello, world.
it is a nice day."""

# 代码太长，进行换行
str = "hello, world." \
      "it is a nice day."

str(1)         # 转换为字符串
repr(1)        # 同上
int("1")       # 将字符串转换为整数
float(1.0)     # 将字符串转换为浮点数


# 格式化字符串
# format() 方法
"{} {} {}".format("a", "b", "c")
# 用数字指定传入参数位置
"{2} {1} {0}".format("a", "b", "c")
# 指定传入参数名称
"{x} {y}".format(y="a", x=1.0)
# 可一起混用
"{y} {0}".format("a", y=1)
# 指定格式
"{:.2f}".format(3.1415)


```

f-string：一种用于格式化输出字符串的简洁方式；基本语法为：在字符串前加上 `f` 或 `F`，然后在字符串中用 `{}` 包含变量或表达式

```python
a = 5
b = 10
result = f"{a} + {b}: {a + b}."

# 转义大括号 需写两个 {{
print(f"awk '{{print $0}}' file")


## 格式化语法 f-string format() 通用
# 宽度填充
:[填充字符][对齐方式][宽度]  # < 左对齐，> 右对齐，^ 居中

# 字符截断
:.n                       # 只显示字符串的前 n 个字符

# 数值符号
:+                        # 正数加正号、负数加负号
:-                        # 原样
:                         # 正数加空格、负数加负号（: 跟的是空格）

# 数值精度
:[宽度].[精度]f            # 没有精度默认为 6

:[填充字符][宽度]d          # 格式化整数
```


---

#### 布尔类型

- 运算
    - 可以使用 & | 来表示与和或（但并不会短路）
    - 一般使用 and or not 进行与 / 或 / 非运算（会短路）

```python
True
False

bool(...)    # 非零数字、非空字符串都是 True
```


---

#### 列表

内部元素不要求同一类型


```python
lst = []

# 索引
lst[1]            # 第二个元素
lst[-2]           # 倒数第二个元素

# 切片（获取列表中的一部分值）
lst[1:4]
lst[:4]
lst[1:]
lst[:]            # 整个列表（拷贝一份）
lst[1:4:2]        # 
lst[4:1:-2]       # 
lst[::-1]         # 列表倒序


lst[1] = item     # 修改元素

lst.append()      # 列表末尾加入元素




# 列表拼接
lst3 = lst + lst2 # 直接相加，不改变原列表，得到新的列表
lst.extend(lst2)  # 把一个列表接到当前列表后面


# 排序列表
# 默认从小到大，传入 reverse=True 则从大到小
lst.sort()      # 永久排序（即排序后赋值给当前列表）
sorted(lst)      # 临时排序，返回排序好的新列表

lst.reverse()   # 永久反转
lst[::-1]       # 返回反转的列表



# 统计
len(lst)        # 列表长度
sum(lst)        # 列表元素和；传入 start 参数，指定加和的起始值
max(lst)        # 列表最大值
min(lst)        # 列表最小值


# 列表推导
lst = [i**2 for i in range(10)]

# 等价于
lst = []
for i in range(10):
    lst.append(i**2)

lst1 = [x*y for x in l1 for y in l2]

lst2 = [... for ... in ... if ...]
```



---

#### 元组

可以看成元素不可变的列表，内部也可以包含不同类型的元素

```python
t = (10, 1, 3, 5, 9)

t[1]          # 索引
t[1:3]        # 切片

t = (10,)     # 单个元素的元组
t = (10)      # 单个值，类型为 int

tuple(lst)   # 将列表转换为元组
```



---

#### 字典

```python
d = {key: value,}    
d = {}                # 空字典，而非空集合
d = dict(key=value)   # dict() 函数
d.keys()
d.values()
d.items()

# 访问键 key 对应的值；可读取、修改
d[key]               # 若 key 不存在，会抛出异常
d.get(key)           # 返回 None
d.get(key, default)  # 返回 default 值

d[key] = value       # 添加键值

del d[key]           # 删除键值

d.update(d2)         # 字典更新

d2 = {key: value, **d}  # 在字典首插入键值对

{k: v for k, v in d.items()}


# 遍历所有键
for key in d.keys():
    ...

# 遍历所有值
for value in d.values():
    ...

# 遍历键值对；item 为一个元组
for item in d.items():
    ... 

# 将 item 解包
for key, value in d.items():
    ... 
```


---

#### 集合

无序序列，因此会自动去重；集合放入的元素只能是不可变的对象

```python
s = {1, 2, 3, 1}

s = set()       # 空集合
s = set(lst)    # 将列表转为集合

s1 & s2         # 交集  s1.intersection(s2)
s1 | s2         # 并集  s1.union(s2)
s1 - s2         # 差集  s1.difference(s2)
s1 ^ s2         # 对称差集  s1.symmetric_difference(s2)
s2 <= s1        # 包含关系 s2.issubset(s1)

s.add(5)          # 添加单个元素；若为已有元素，集合不变
s.update([5, 6])  # 添加多个元素
s.remove(1)       # 移除单个元素；元素不存在会报错
s.discard(10)     # 不会报错
s.pop()           # 弹出元素
```



---

### 条件分支

#### 布尔表达式

```python
# 判断元素是否在列表中
value in lst：# 如果在则值为 True

value not in lst：# 如果在则为 False
```


---

#### 条件语句

- 类三目运算符写法 a if condition else b
    - 类似其它语言中的 condition? a : b


---

### 循环

- python 中的 for 循环并不像 c 中是指定一个变量的变化方式，而是从列表 / 元组 / 迭代器等可迭代对象中遍历值

- `range()` 得到的并不是列表，如果要用其生成列表要使用 `list(range(...))`

```python
# 使用 range 来生成一串数字用来循环
for i in range(10):
    pass

for i in range(1, 10):
    pass

for i in range(1, 10, 2):
    pass

lst = list(range(10))      # 生成列表
```

---

#### 元素解包

- 赋值时等号左侧可以是用逗号分隔的多个值，这时会将右侧解包分别赋值给左侧的各个变量
- 右侧也可以是多个值（只要出现逗号就会视为一个元组）
    - 可以通过 a, b = b, a 实现元素交换
- 星号表达式
    - 可以用来在可迭代对象内部解包
    - 也可用来标记一个变量包含多个值
- for 循环可以解包

```python
t = (1, 2, 3)
a, b, c = t # a = 1, b = 2, c = 3
t = (1, 2, (3, 4))
a, b, (c, d) = t # c = 3, d = 4

l = [1, 2, *[3, 4]] # [3, 4] 被解包
## l = [1, 2, 3, 4]
a, *b = [1, 2, 3, 4]
## a = 1, b = [2, 3, 4]

lst = [[1, 2], [3, 4]]
for a, b in lst:
    ... # 第一次循环 a, b 为 1, 2
        # 第二次循环 a, b 为 3, 4

```


---

- enumerate 计数
    - 可以指定初始值
- zip 同时循环多个可迭代对象

```python
for i, value in enumerate(lst, start=...):
    ...


# a 在 lst1 中循环，b 在 lst2 中循环
# 循环次数为最短的对象的长度
for a, b in zip(lst1, lst2):
    ... 
```


---

#### 生成元组/字典

- 可以使用和列表推导类似的方法生成元组和字典
- 生成元组的时候要用 tuple()
    - 只写 () 的话则只是生成器表达式
- 生成字典时循环前用 : 将键值隔开

```python
tuple(i**2 for i in range(1, 10))

(i**2 for i in range(1, 10))
## ^  generator object

{a: b for a in ... for b in ... }

```


---

### 函数

- 使用 def 关键字来定义函数
- 先函数名，然后括号列出参数，下面接代码块
- 使用 return 返回
    - 没有 return 运行到结尾，返回 None
    - 只有 return，返回 None
    - return 后接内容，返回内容
    - return 的值类型不要求一致
    - return 可以返回多个值（利用元组）


函数定义

```python
def func(arg1, arg2):
    ...

def func(arg1, arg2):
    ...
    return ...

def func(arg1, arg2):
    ...
    return ..., ...
```


---

函数参数

- 括号中要列出参数名，供函数体内使用
- 可以在参数后接等号赋默认值
    - 使用默认值的参数在调用时可以不用传
- 利用 * 来接收任意多参数
    - 接收进来是一个元组
    - * 参数后面不能再有其它非关键字参数
- 利用 ** 来接收任意多关键字参数
    - 接收进来是一个字典


---


函数调用

- 通过 函数名 ( 参数 ) 来调用函数，得到返回值
- 直接传参的话要将参数与定义对应上
- 通过关键字传参（参数名）可以打乱顺序
- 带有默认值的参数如果不传则使用默认值
- 如果读任意多关键字参数，则多余的读到字典中

```python
def func(a, b):
    ...

func(1, 2) # a = 1, b = 2
func(b=1, a=2) # a = 2, b = 1

def func2(a, **b):
    ...

func2(a=1, b=2, c=3)
## a = 1, b = {"b": 2, "c": 3}

```


---

`==` 检查是否相等，`is` 检查值是否相同


---

#### 匿名函数

- 可以通过 lambda 表达式来定义匿名函数
- lambda 输入 : 输出表达式
- 可以有多个输入
- 可以将一个函数赋值给一个变量


```python
lambda a: a**2 + 2*a + 1
(lambda a: a**2 + 2*a + 1)(2) # 9

lambda a, b: a*2 + b

f = lambda a: a**2 + 2*a + 1
## 近似等价于
def f(a):
    return a**2 + 2*a + 1

- 避免用 lambda 赋值的形式定义函数
    - 例如 name 属性不会是函数名，而是 "\<lambda>"
```


---

用户输入

- 读取用户输入使用内置的 input 函数
- 函数参数为要显示的提示符，例如 input(“> “)
- 函数的返回值为一个字符串
- 每次读入一行（即读到换行为止



---

#### 高阶函数

- 接收函数作为参数的函数被称为高阶函数
- 比较常用的有 map、filter

```python
list(map(lambda x: x*2, [1, 2]))
## [2, 4]
list(filter(lambda x: x>1, [1, 2, 3]))
## [2, 3]

list(map(str, [1, 2, 3]))
## ["1", "2", "3"]
```


变量可以指向函数（函数本身可以赋值给变量）
```python
f = abs
```


函数名也是变量（函数名是指向函数的变量）
```python
abs = 10
abs(-10)  # 会报错
```


高阶函数：一个函数就接收另一个函数作为参数
```python
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))
```



`map()`：接收两个参数，一个是函数，一个是 `Iterable`，`map` 将传入的函数依次作用到序列的每个元素，并把结果作为新的 `Iterator` 返回
```python
```


函数中的可变参数和字典参数（参数传入机制），可增加代码的灵活性

```python
def func(*args):
    pass

def func(**kwargs):
    pass

# 以下两个函数参数传入效果等效
func(*[1, 2, 3])  # 传入可迭代对象  
func(1, 2, 3)  # 传入多个参数

func(**{'dog': 1, 'cat': 2, 'fish': 3})  # 传入可迭代对象  
func(dog=1, cat=2, fish=3)  # 传入多个参数
```



---

### 类

在类的初始化函数中对参数的类型进行判别并抛出异常
```python
isinstance()
```


`dir()`：查看类的（实例）所有的属性和方法；函数的所有参数


- 类可以看成包含一些**属性**和**方法**的框架
- 根据类来创建对象 -> 实例化
- 用 class 关键字来定义类
- 类中的函数 -> 方法
    - 特殊方法 **init**，在类实例化的时候会被自动调用
    - 其它一般的方法第一个参数都要为 “self”，调用的时候会自动传入


```python
class ClassName():
    a = 1

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method(self):
        print(self.arg1, self.arg2, self.a)

    @property

    @staticmethod

    @classmethod

obj = ClassName(2, 3)
obj.method() # 2 3 1
print(obj.a, obj.arg1) # 1 2

# 直接写在类中的是属性，也可以通过为 self.\<name> 赋值的形式创建属性
# 用类似函数调用的形式实例化类，参数为 **init** 方法的参数
# 直接通过 .\<method> .\<attribute> 的形式调用方法 / 获取属性
```



---

### 装饰器

装饰器

函数装饰器




类装饰器



---

### 文件 IO

- with … as …: 开启一个上下文管理器
- 常用在文件 open 上
    - with 块开始自动打开
    - with 块结束自动结束
- with 块结束后变量仍会留存



```python
with open("file", "r", encoding="utf-8") as f:
    s = f.read()
    ...

print(f.closed)  # True

```


行读取
```python
with open(file, "r") as f:
	lines = f.readlines()
```


读写 json
```python
import json

data = {}

with open(json_fn, "w") as f:
	json.dump(data, f, indent=4)

with open(json_fn, "r") as f:
	json_data = json.load(f)
```



读写 yaml
```python
import yaml

yaml_data = {}

with open(yaml_fn, "w") as f:
	yaml.safe_dump(yaml_data, f, sort_keys=False)

with open(yaml_fn, 'r') as f:
	yaml_data = yaml.safe_load(f)
```



---

### 异常

>[Python进阶笔记.md](https://github.com/LiuQixuan/PythonLearningNote/blob/master/Python%20%E8%BF%9B%E9%98%B6%E7%AC%94%E8%AE%B0.md)

|         异常名称          |                   描述                   |
|:-------------------------:|:----------------------------------------:|
|       BaseException       |            所有异常 K 的基类             |
|        SystemExit         |              解释器请求退出              |
|     KeyboardInterrupt     |            用户自行中断执行^C            |
|         Exception         |              常规错误的基类              |
|       StopIteration       |                迭代器溢出                |
|       GeneratorExit       |         生成器发生异常后通知退出         |
|       StandardError       |           所有标准异常类的基类           |
|      ArithmeticError      |          所有数值计算错误的基类          |
|    FloattingPointError    |               浮点计算错误               |
|       OverflowError       |               数值运算溢出               |
|     ZeroDivisionError     |                 除零错误                 |
|      AssertionError       |               断言语句失败               |
|      AttributeError       |              对象缺失该属性              |
|         EOFError          |       没有内建输入，到达 EOF 标记        |
|     EnvironmentError      |            操作系统错误的基类            |
|          IOError          |            输入/输出操作失败             |
|          OSError          |               操作系统错误               |
|       WindowsError        |               系统调用失败               |
|        ImportError        |            导入模块/对象失败             |
|        LookupError        |            无效数据查询的基类            |
|        IndexError         |             序列中没有此索引             |
|         KeyError          |              映射中没有此键              |
|        MemoryError        | 内存溢出（对于 Python 解释起来说非致命） |
|         NameError         |            未声明/初始化对象             |
|     UnboundLocalError     |          访问未初始化的本地变量          |
|      ReferenceError       |  试图访问已被回收器回收的对象（弱引用）  |
|       RuntimeError        |              一般运行时错误              |
|    NotImplementedError    |              尚未实现的方法              |
|        SyntaxError        |             Python 语法错误              |
|     IndentationError      |                 缩进错误                 |
|         TabError          |            Tab 和 Space 混用             |
|        SystemError        |           一般的解释器系统错误           |
|         TypeError         |             对类型无效的操作             |
|        ValueError         |              传入无效的参数              |
|       UnicodeError        |             Unicode 相关错误             |
|    UnicodeDecodeError     |           Unicode 解码时的错误           |
|    UnicodeEncodeError     |           Unicode 编码时的错误           |
|   UnicodeTranslateError   |           Unicode 转码时的错误           |
|          Warning          |                警告的基类                |
|    DeprecationWarning     |          关于被弃用的特性的警告          |
|       FutureWarning       |      关于构造将来语义会有改变的警告      |
|      OverflowWarning      |  旧的关于自动提升为长整型 (long) 的警告  |
| pendingDeprecationWarning |         关于特性将会被废弃的警告         |
|      RuntimeWarning       |          可疑的运行时行为的警告          |
|      SysntaxWarning       |              可疑语法的警告              |
|        UserWarning        |            用户代码生成的警告            |

---

模块与导入

- 模块可以是一个单独的 .py 文件，也可以是一个文件夹
    - 文件夹相当于导入其下 **init**.py 文件
- 模块中正常编写函数、类、语句
- 通过 import 语句导入模块
    - import code
    - import code as cd
    - from code import …
    - from code import *
- 导入时相当于运行了一遍导入的代码


```python
## code.py
print("hello")
def f():
    print("call func in code.py")
...

```


```python
import code # hello
code.f()
import code as cd # hello
cd.f()
from code import f # hello
f()
from code import * # hello
f()

```


---

main 函数

- 防止导入时运行代码
- 只允许直接运行脚本时运行
- 通过判断 **name**
    - 如果是直接运行，则其等于字符串 **main**
    - 如果是被导入的，则其等于模块名

```python
## code.py
...
if __name__ == "__main__":
    print("hello")
else:
    print(__name__)

```

```python
import code # code
```


```bash
$ python code.py # hello
```


---

内部模块

python 自带了很多实用的模块（标准库）

- os、sys：系统操作
- math：数学运算
- re：正则表达式
- datetime：日期与时间
- subprocess：子进程管理
- argparse：命令行参数解析
- logging：日志记录
- hashlib：哈希计算
- random：随机数
- csv、json：数据格式解析
- collections：更多类型
- …

---

外部模块安装

- [pypi.org](https://pypi.org/) 上有极多别人写好了可以用的模块
    - numpy 矩阵等科学计算、scipy 科学计算、matplotlib 作图……
- 使用 pip 安装（pip / python -m pip）
    - pip install pkg_name
    - pip install pkg_name=… 指定版本
    - pip install -r requirements.txt 安装 txt 文件中的所有包
    - pip install … -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple) 换源
    - pip list、pip show 命令查看安装的所有包 / 某个包的信息
    - pip uninstall pkg_name 卸载包
- pip 安装本地模块
    - 目录下需要包含 setup.py / pyproject.toml
    - pip install . 安装本地模块（复制到 site-packages 中）
    - pip install -e . 可修改形式安装本地模块（在当前位置，可以直接修改代码）


---

文档字符串 docstring

- 模块开头的三引号字符串
- 类、函数定义下面的三引号字符串
- help(…) 的时候可以显示
- obj.**doc** 表示这串字符串
- 编辑器用来提示
- 一些文档生成工具（sphinx 等）从中获取文档


```python
"""
docstring for module
"""

def func(...):
    """docstring for function"""
    ...

class A():
    """docstring for class"""
    def __init__(self, ...):
        """docstring for method"""
        ...

```
