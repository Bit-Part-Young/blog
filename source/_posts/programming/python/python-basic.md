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

什么是 Python

- 解释性的脚本语言：通过解释器来直接运行，不需要编译链接成二进制文件
- 动态类型语言：类型在运行时确定，不需要通过代码明文规定
- 面向对象语言：Python 中一切皆对象


---

### 参考资料

- [GitHub - lijin-THU/notes-python: 中文 Python 笔记](https://github.com/lijin-THU/notes-python)（Python 2 版本）

- [Python 基础语法 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/pl/python/basic/)

- Python 速查表
    - [Python Cheatsheet - Python Cheatsheet](https://www.pythoncheatsheet.org/)
    - [GitHub - gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet)
    - [Python 3 备忘清单](https://wangchujiang.com/reference/docs/python.html)

- [GitHub - piglei/one-python-craftsman: 来自一位 Pythonista 的编程经验分享](https://github.com/piglei/one-python-craftsman)

- 《编程不难》书籍源码：[GitHub - Visualize-ML/Book1\_Python-For-Beginners](https://github.com/Visualize-ML/Book1_Python-For-Beginners)

- [GitHub - scruel/pcc\_3e\_slides: 《Python 编程：从入门到实践（第三版）》的官方配套图解讲义资源](https://github.com/scruel/pcc_3e_slides)

- Python tips and tools：[GitHub - pablovegan/Python-tips-tools: Short Python tips and tools talk for the Superconducting Qubit Technology school at Benasque 2023.](https://github.com/pablovegan/Python-tips-tools)

- [Python Cookbook 3rd Edition Documentation — python3-cookbook 3.0.0 文档](https://python3-cookbook.readthedocs.io/zh_CN/latest/)

- [Tagged:"Writing Faster Python" - Sebastian Witowski](https://switowski.com/tags/writing-faster-python/)



---

## 使用

### 安装

建议使用 Miniconda3 安装


---

### 运行

- 在终端运行 Python 脚本

```bash
python script.py
```

- 指定 `UTF-8` 编码

```python
# 在 Python 文件的第一行或第二行，指定使用 UTF-8 编码
# 主要用于 Python 2（Python 3 默认使用 UTF-8 编码）

# 方式 1
# -*- coding: utf-8 -*-
# 方式 2
# coding=utf-8
```

- 在终端执行 Python 代码，用于快速测试一些代码片段或进行简单的计算

```bash
python -c "print('hello world')"
```

- 在终端中使用 Python 模块：`python -m`，通常用于运行可以作为脚本执行的模块，如 `venv`、`pip` 等；[Python's many command-line utilities - Python Morsels](https://www.pythonmorsels.com/cli-tools/)

```bash
# 创建虚拟环境
python -m venv venv

# 安装 package
python -m pip install <package>

# 启动 HTTP 服务；可用于临时接收文件
python -m SimpleHTTPServer port  # python2
python -m http.server port       # python3
```

- 查看 Python 环境变量

```bash
python --help-env
```

- Python 在线编译器：[Python Online Compiler with all Modules and Versions](https://pythononlinecompiler.com/)

- Python 编译器，可输出可执行文件或扩展模块：[GitHub - Nuitka/Nuitka](https://github.com/Nuitka/Nuitka)


---

### 工具

- Python 版本管理工具：[GitHub - pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)

- 包管理工具（支持 Python、C++）：[GitHub - prefix-dev/pixi: Package management made easy](https://github.com/prefix-dev/pixi)

- Python 包管理工具：[GitHub - python-poetry/poetry: Python packaging and dependency management made easy](https://github.com/python-poetry/poetry)

- Python docstring 格式化：[GitHub - PyCQA/docformatter: Formats docstrings to follow PEP 257](https://github.com/PyCQA/docformatter)

- Python GitLab API：[GitHub - python-gitlab/python-gitlab: A python wrapper for the GitLab API.](https://github.com/python-gitlab/python-gitlab)

- Python 多线程：[GitHub - sybrenjansen/mpire: A Python package for easy multiprocessing, but faster than multiprocessing](https://github.com/sybrenjansen/mpire)

- 数据科学 Python（内容感觉一般）：[GitHub - khuyentran1401/Efficient Python tricks and tools for data scientists](https://github.com/khuyentran1401/Efficient_Python_tricks_and_tools_for_data_scientists)

- 将 Python 的计算公式转换成 LaTeX（只能是简单的公式）：[GitHub - connorferster/handcalcs](https://github.com/connorferster/handcalcs)

- 打印 Python objects：[GitHub - gaogaotiantian/objprint](https://github.com/gaogaotiantian/objprint)

- 将打印的内容以表格的形式呈现：[GitHub - astanin/python-tabulate](https://github.com/astanin/python-tabulate)

- Turtle 模块绘制树：[GitHub - Wandrys-dev/FloweringTree: Little tree drawn in Python and Turtle🌲](https://github.com/Wandrys-dev/FloweringTree)

- 实现按 Tab 键命令自动补全（支持 bash 和 zsh）：[GitHub - kislyuk/argcomplete: Python and tab completion, better together.](https://github.com/kislyuk/argcomplete)

```bash
# 安装
pip install argcomplete
activate-global-python-argcomplete

# 激活命令自动补全
eval "$(register-python-argcomplete my-python-app)"
```

- 检查通过 pip 命令安装的包的 License：[GitHub - raimon49/pip-licenses: Dump the license list of packages installed with pip.](https://github.com/raimon49/pip-licenses)

- [GitHub - rsalmei/alive-progress: A new kind of Progress Bar, with real-time throughput, ETA, and very cool animations!](https://github.com/rsalmei/alive-progress)

- 构建 CLI 工具
    - [GitHub - tiangolo/typer](https://github.com/tiangolo/typer)
    - [GitHub - google/python-fire](https://github.com/google/python-fire)
    - click：使用装饰器来设置命令的参数和选项

```python
import click
@click.command()

@click.argument()
@click.option()
```



---

## 语法

### 查看帮助

注：和 `dir()` 函数相比，`__all__` 变量在查看指定模块成员时，它不会显示模块中的特殊成员，同时还会根据成员的名称进行排序显示

```python
import numpy as np

# 查看模块/包的方法、属性（成员）
dir(np)
print(np.__all__)


# 查看模块/包及其方法、属性的帮助文档
help(numpy)
help(np)

help(np.array)
print(np.array.__doc__)
```


---

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

#### 列表

内部元素不要求同一类型

```python
lst = [4, 5, 1, 7, 2, 9]

# 索引
lst[1]            # 第二个元素
lst[-2]           # 倒数第二个元素


# Python 内置函数，创建切片
slice(start, stop, step)

# 切片（获取列表中的一部分值）
lst[1:4]
lst[:4]
lst[1:]
lst[:]            # 整个列表（拷贝一份）
lst[1:4:2]        # 
lst[4:1:-2]       # 
lst[::-1]         # 列表倒序


# 修改元素
lst[1] = item     # 修改元素


# 添加元素
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

lst = [i**2 for i in range(10) if i % 2 == 0]
```


---

#### 元组

可以看成元素不可变的列表，内部也可以包含不同类型的元素

注：元组的生成速度比列表快很多，遍历速度快一点，索引速度差不多

```python
t = (10, 1, 3, 5, 9)

t[1]          # 索引
t[1:3]        # 切片

t = (10,)     # 单个元素的元组
t = (10)      # 单个值，类型为 int

tuple(lst)   # 将列表转换为元组

# 使用和列表推导类似的方法生成元组
tuple(i**2 for i in range(1, 10))
# 只写 () 则只是生成器表达式
(i**2 for i in range(1, 10))
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
d[key]                  # 若 key 不存在，会抛出异常
d.get(key)              # 返回 None
d.get(key, default)     # 返回 default 值
   
d[key] = value          # 添加键值
del d[key]              # 删除键值
d.update(d2)            # 字典更新
d2 = {key: value, **d}  # 在字典首插入键值对

# 有序字典
from collections import OrderedDict

# 将字典字符串还原成 dict
import ast; ast.literal_eval(str(d1))

{k: v for k, v in d.items()}

# 没有内置方法直接通过 value 查找 key
key_specific = [k for k, v in d.items() if v == value_specific][0]

# 使用和列表推导类似的方法生成字典
{key: value for key in ... for value in ... }

# 遍历所有键
for key in d.keys():
    ...

# 遍历所有值
for value in d.values():
    ...

# 遍历键值对；item 为元组
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

### 条件分支

#### 布尔表达式

```python
# 判断元素是否在列表中
if value in lst：      # 如果在则值为 True
    ...

if value not in lst：  # 如果在则为 False
    ...
```


---

#### 条件语句

- 类三目运算符写法 a if condition else b
    - 类似其它语言中的 condition? a: b


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

### 函数

#### 函数定义与返回值

- 使用 `def` 关键字来定义函数；先函数名，然后括号列出参数，下面接代码块
- 使用 `return` 返回
    - 没有 `return` 运行到结尾，返回 None
    - 只有 `return`，返回 None
    - `return` 后接内容，返回内容
    - `return` 的值类型不要求一致
    - `return` 可以返回多个值（利用元组）

```python
# 函数定义与返回值
def func(...):
    ...

    return ...
    #                  没有 return
    # return           只有 return
    # return ..., ...  返回多个值
```


---

#### 函数参数与调用

- 在 Python 中，`*args` 和 `**kwargs` 是用来传递可变数量参数的机制，允许编写灵活的函数（在 Matplotlib 包中这两个参数出现的概率较大，绘图所需参数很多）
- 单个 `*` 星号用于指定所有后续参数必须作为关键字参数传递

```python
def func(a, b):
    ...

func(1, 3)              # 位置参数
func(a=1, b=3)          # 关键字参数；顺序可以打乱

def func(a, b=3):
    ...

func(1)                 # 默认参数

def func(*args):
    ...

func(1, 3, 5)           # 可变数量的位置参数
func(*[1, 3, 5])      

def func(**kwargs):
    ...

func(a=1, b=3, c=5)     # 可变数量的关键字参数
func(**{"a": 1, "b": 3, "c": 5})

def func(*args, **kwargs):
    ...

func(1, 3, c=5, d=7)    # 混合使用

def func(a, *, b, c):
    ...

func(1, b=3, c=5)       # 指定所有后续参数必须作为关键字参数传递
```


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

#### 高阶函数

- 高阶函数：接收函数作为参数的函数；常用的有 `map()`、`filter()`
- `map()`：接收两个参数，一个是函数，一个是 `Iterable`，`map()` 将传入的函数依次作用到序列的每个元素，并把结果作为新的 `Iterator` 返回

```python
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

list(map(lambda x: x * 2, [1, 2]))        # [2, 4]
list(map(str, [1, 2, 3]))                 # ["1", "2", "3"]
list(filter(lambda x: x > 1, [1, 2, 3]))  # [2, 3]
```

```python
f = abs       # 变量可以指向函数（函数本身可以赋值给变量）

abs = 10      # 函数名也是变量（函数名是指向函数的变量）
abs(-10)      # 会报错
```


---

#### main 函数

- 防止导入时运行代码，只允许直接运行脚本时运行
- 通过判断 `__name__`：若是直接运行，则其等于字符串 main；若是被导入的，则其等于模块名

```python
## script.py

...

if __name__ == "__main__":
    print("hello")
else:
    print(__name__)


import script           # 作为模块导入；输出 script
$ python script.py      # 直接运行；输出 hello
```


---

#### 用户输入

- 读取用户输入使用内置的 input 函数
- 函数参数为要显示的提示符，例如 input (“> “)
- 函数的返回值为一个字符串
- 每次读入一行（即读到换行为止

```python

```


---

### 类

- 类可以看成包含一些**属性**和**方法**的框架

- 根据类来创建对象 -> 实例化

- 用 class 关键字来定义类，类的名称 ClassName 通常采用 `CamelCase` 记法

- 类的方法：实例方法、类方法、静态方法

- 实例方法：必须有 `self` 作为第一个参数（`self` 可以写成别的，如 `this` 或 `s` 等），用于访问实例属性和其他方法

- 类方法：
    - 使用 `@classmethod` 装饰器；通常以 `cls` 作为第一个参数，表示类本身
    - 类方法是与类相关联的方法，而不是与类的实例相关联的方法
    - 可访问类的属性和调用其他类方法，但不能直接访问实例属性（不具有对实例的引用）
    - 可通过类本身进行调用，而不需要创建类的实例

- 静态方法：使用 `@staticmethod` 装饰器；不接收 `self` 或 `cls` 作为参数；适用于与类相关但不需要访问类或实例属性的方法

- 构造方法：`__init__()`，在类实例化时会被自动调用；用于设置实例属性



```python
class ClassName():
    """docstring"""

    a = 1

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method(self):
        print(self.arg1, self.arg2, self.a)

    def __str__():
        ...

    def __repr__():
        ...

    @property

    @staticmethod

    @classmethod

obj = ClassName(2, 3)     # 实例化
obj.method()              # 使用实例方法 
print(obj.a, obj.arg1)    # 访问类属性
```


```python
dir()       # 查看类的（实例）所有的属性和方法；函数的所有参数

isinstance()    # 在类的初始化函数中对参数的类型进行判别并抛出异常

# 装饰器
@property       # 将方法伪装成属性；只读不可写
@attr.setter    # 将属性变成可写

# 特殊方法
__init__()
__str__()
__repr__()
__len__()
__add__()

# 特殊属性
__class__
__name__
```


---

### 继承与多态

- 继承：允许一个类（子类）继承另一个类（父类）的属性和方法，实现代码重用和扩展。Python 支持单继承和多继承

- 方法重写：子类可以重写父类的方法，以实现不同的行为

- 多态：指的是不同类的对象可以通过相同的接口调用不同的实现。结合继承和方法重写实现


---

### 装饰器

装饰器：作用对象是函数，作用是在调用函数之前和之后，为函数添加额外功能

函数装饰器

对函数使用装饰器，会导致函数的 `__name__`、`__doc__` 等属性发生改变，保留原函数的名称等属性，需通过使用内置模块 functools 中的 wraps 来保留函数的元信息

```python
from functools import wraps

def XXX(func):  
    @wraps(func)
    def wrapper():  
        func()  

        ...

    return wrapper

@XXX
def ...
```




类装饰器

- [ ] reader writer 装饰器



---

### 文件 IO

- `with ... as ...`: 开启一个上下文管理器（常用在文件 open 上）

- `with` 块开始自动打开，`with` 块结束自动结束；`with` 块结束后变量仍会留存

```python
with open("file", "r", encoding="utf-8") as f:
    s = f.read()
    ...

print(f.closed)  # True

# 行读取
with open(file, "r") as f:
    lines = f.readlines()
```

- 读写 json

```python
import json

json_fn = ...
data = {}

with open(json_fn, "w") as f:
    json.dump(data, f, indent=2)

with open(json_fn, "r") as f:
    json_data = json.load(f)
```

- 读写 yaml

```python
import yaml

yaml_fn = ...
yaml_data = {}

with open(yaml_fn, "w") as f:
    yaml.safe_dump(yaml_data, f, sort_keys=False)

with open(yaml_fn, 'r') as f:
    yaml_data = yaml.safe_load(f)
```


---

### 异常

>[Python进阶笔记.md](https://github.com/LiuQixuan/PythonLearningNote/blob/master/Python%20%E8%BF%9B%E9%98%B6%E7%AC%94%E8%AE%B0.md)

```bash
BaseException              # 所有异常的基类
SystemExit                 # 解释器请求退出
KeyboardInterrupt          # 用户自行中断执行 ^C
Exception                  # 常规错误的基类
StopIteration              # 迭代器溢出
GeneratorExit              # 生成器发生异常后通知退出
StandardError              # 所有标准异常类的基类
ArithmeticError            # 所有数值计算错误的基类
FloattingPointError        # 浮点计算错误
OverflowError              # 数值运算溢出
ZeroDivisionError          # 除零错误
AssertionError             # 断言语句失败
AttributeError             # 对象缺失该属性
EOFError                   # 没有内建输入，到达 EOF 标记
EnvironmentError           # 操作系统错误的基类
IOError                    # 输入/输出操作失败
OSError                    # 操作系统错误
WindowsError               # 系统调用失败
ImportError                # 导入模块/对象失败
LookupError                # 无效数据查询的基类
IndexError                 # 序列中没有此索引
KeyError                   # 映射中没有此键
MemoryError                # 内存溢出
NameError                  # 未声明/初始化对象
UnboundLocalError          # 访问未初始化的本地变量
ReferenceError             # 试图访问已被回收器回收的对象（弱引用）
RuntimeError               # 一般运行时错误
NotImplementedError        # 尚未实现的方法
SyntaxError                # Python 语法错误
IndentationError           # 缩进错误
TabError                   # Tab 和 Space 混用
SystemError                # 一般的解释器系统错误
TypeError                  # 对类型无效的操作
ValueError                 # 传入无效的参数
UnicodeError               # Unicode 相关错误
UnicodeDecodeError         # Unicode 解码时的错误
UnicodeEncodeError         # Unicode 编码时的错误
UnicodeTranslateError      # Unicode 转码时的错误
Warning                    # 警告的基类
DeprecationWarning         # 关于被弃用的特性的警告
FutureWarning              # 关于构造将来语义会有改变的警告
OverflowWarning            # 旧的关于自动提升为长整型 (long) 的警告
pendingDeprecationWarning  # 关于特性将会被废弃的警告
RuntimeWarning             # 可疑的运行时行为的警告
SysntaxWarning             # 可疑语法的警告
UserWarning                # 用户代码生成的警告
```


---

### 模块

#### 模块导入

- 模块可以是一个单独的 `.py` 文件，也可以是一个文件夹（相当于导入其下 `__init__.py` 文件）
- 模块中正常编写函数、类、语句
- 导入时相当于运行了一遍导入的代码

```python
# 模块导入
import time 
time.time()

import time as tm 
tm.time()

from time import time
time()

from time import *
time()
```

---

#### 内部模块

Python 自带了很多实用的模块（标准库）

```python
os sys         # 系统操作
glob           # 文件模式匹配
math           # 数学运算
re             # 正则表达式
datetime       # 日期与时间
subprocess     # 子进程管理
argparse       # 命令行参数解析
logging        # 日志记录
hashlib        # 哈希计算
random         # 随机数
csv json       # 数据格式解析
typing         # 数据类型
collections    # 更多类型
tkinter        # Qt
...
```

---

#### 外部模块安装

- 外部模块（包）可以在 [pypi.org](https://pypi.org/) 找

- `-e` 编辑模式：创建指向项目源代码目录的链接（如 `site-package/package.egg-link` 文件指向源代码 `pacakge/` 目录）；**源代码的任何更改都会立即反映在 Python 环境中，无需重新安装，方便调试开发**

```bash
# 使用 pip 安装（pip / python -m pip）
pip install <package>             # 安装
pip install <package>=version     # 指定版本
pip install -r requirements.txt   # 安装 txt 文件中的所有包
pip list                          # 查看安装的所有包的信息
pip show <package>                # 查看某个包的信息
pip uninstall <package>           # 卸载包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  # 换源安装


# pip 安装本地模块
# 目录下需要包含 setup.py / pyproject.toml
pip install .            # 安装本地模块（拷贝到 site-packages 中）
python setup.py install  # 效果同上
pip install -e .         # 以编辑模式安装本地模块
pip install git+url      # 使用 Git 从 GitHub 下载源码安装
```


---

### 文档字符串 docstring

- 模块开头、函数、类定义下面的三引号字符串
- 使用 `help(...)` 或 `print(xxx.__doc__)` 显示 docstring
- 使用编辑器 +LSP 时，悬停时会显示 docstirng 用来提示
- 一些文档生成工具（Sphinx 等）从中获取文档

```python
"""
docstring for module
"""

def func(...):
    """docstring for function"""
    ...

class ClassName:
    """docstring for class"""
    def __init__(self, ...):
        """docstring for method"""
        ...

```



---

## 常用内置模块

### os

```python
import os

# 获取 用户根目录路径
os.path.expanduser("~")  # 展开 ~
os.getenv("HOME")        # 获取环境变量
os.environ["HOME"]

os.getcwd()           # 当前路径
os.listdir()          # 列出当前路径下的目录/文件
os.chdir()            # 切换路径
os.walk()             # 遍历路径
os.rename(old, new)   # 重命名文件
os.mkdirs()           # 创建单层级目录
os.makedirs()         # 创建多层级目录；exist_ok=True 目录已存在时，命令不会报错

os.path.exists()      # 检查路径是否存在（可以是文件、目录或符号链接等）
os.path.isfile()      # 检查路径是否存在且是否为文件
os.path.isdir()       # 检查路径是否存在且是否为目录
os.path.basename()    # 获取文件路径的文件部分
os.path.dirname()     # 获取文件路径的目录部分
os.path.abspath()     # 获取绝对路径
os.path.join()        # 将各个部分合并成一个路径
os.path.split()       # 分离文件路径和文件名
os.path.splitext()    # 分离文件名与后缀
```


---

### argparse

命令行参数解析

[GitHub - omni-us/jsonargparse: Implement minimal boilerplate CLIs derived from type hints and parse from command line, config files and environment variables](https://github.com/omni-us/jsonargparse)

---

#### 命令行参数解析

- 命令行参数解析

```python
import argparse

# 创建解析器
parser = argparse.ArgumentParser(
    prog=...,
    usage=...,
    description=...,
    epilog=...,
    formatter_class=...,
    add_help=...,
    allow_abbrev=...,
)
# ArgumentParser() 参数
prog              # 程序名称（可不添加）
usage             # 程序使用方法（可不添加）
formatter_class   # 自定义帮助文档的输出格式
description       # 程序描述
epilog            # 在帮助信息结尾添加文本（如作者、版本、联系方式等）
add_help          # 是否自动添加 -h/--help 选项
allow_abbrev      # 是否允许长选项使用非歧义缩写
argument_default  # 所有参数的默认值
conflict_handler  # 处理参数名冲突
exit_on_error     # 遇到错误时是否应该退出程序

# formatter_class 常用值
argparse.HelpFormatter                   # 默认
argparse.ArgumentDefaultsHelpFormatter   # 显示参数默认值；可选参数设置 default 值后会显示，位置参数需设置 default 和 nargs 才会显示
argparse.RawTextHelpFormatter            # 保持原格式


# 若 description 内容很长，可进行以下操作
parser.description += "..."
parser.description += "..."


# 添加参数
parser.add_argument(
    "file",             # 位置参数；必须提供
    "-f",               # 可选参数；短选项；可不用空格分隔直接跟参数值
    "--file",           # 可选参数；长选项
    nargs=...,
    const=...,
    default=...,
    type=...,
    choices=...
    required=...,
    help=...,
)
# add_argument() 参数
name_or_flags     # 命令行参数名称（位置参数或可选参数）
nargs             # 指定命令行中参数应消耗的值的数量；N、?、*、+
const             # 常量值（只指定参数但不带值时，使用该 const 值，需结合 nargs=? 使用） 
default           # 参数的默认值（未指定参数时，使用该 default 值）
type              # 该命令行参数应被转换成的类型
choices           # 参数的允许值
required          # 用于可选参数，默认 False；True 表示该参数必须指定
help              # 参数的帮助信息
metavar           # 将帮助信息中的参数用 metavar 的值替代（类似占位符）
action            # 定义解析命令行选项时，如何处理该选项的值

# action 可选值
store             # 默认值，将参数值存储到变量中
store_true        # 布尔值开关
store_false       # 与 store 相反
append            # 将参数值添加到列表中


# 解析命令行参数
args = parser.parse_args()

# 短、长选项在一起时，需用长选项
file=args.file
```

- 示例代码：

```python
def get_potcar(...):
    ...


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Generate VASP, pymatgen recommended POTCAR.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev=True,
        epilog="Author: SLY.",
    )

    parser.add_argument(
        "-pr",
        "--psp_recommended",
        nargs="?",
        const="vasp",
        default="vasp",
        type=str,
        choices=["vasp", "pymatgen"],
        help="Recommended pseudopotential source.",
    )

    parser.add_argument(
        "structure_file",
        nargs="?",
        default="POSCAR",
        type=str,
        help="Structure file with POSCAR format, eg. POSCAR.",
    )

    ...
```

- 使用示例

```bash
# 可支持的命令行参数
get_potcar.py -h
get_potcar.py
get_potcar.py -pr
get_potcar.py --psp
get_potcar.py --psp_recommended
get_potcar.py -pr pymatgen POSCAR
get_potcar.py --psp pymatgen POSCAR
get_potcar.py --psp_recommended pymatgen POSCAR


# 查看命令行程序描述及使用
usage: get_potcar.py [-h] [-pr [{vasp,pymatgen}]] [structure_file]

Generate VASP, pymatgen recommended POTCAR.

positional arguments:
  structure_file        Structure file with POSCAR format. (default: POSCAR)

options:
  -h, --help            show this help message and exit
  -pr [{vasp,pymatgen}], --psp_recommended [{vasp,pymatgen}]
                        Recommended pseudopotential source. (default: vasp)

Author: SLY.
```


---

#### 多个子命令的命令行参数解析

- 多个子命令的命令行参数解析

- 参考：[\[Python\] argparse处理多个功能和不同的多参数-CSDN博客](https://blog.csdn.net/Spade_/article/details/111059349)

```python
import argparse

# 创建解析器
parser = argparse.ArgumentParser()

# 添加子解析器
subparsers = parser.add_subparsers()

# 添加子命令参数
parser_generate = subparsers.add_parser(
    "generate", 
    help="generate atomate optimization workflows.",
)
parser_generate.add_argument(
    "-c",
    "--character",
    type=str,
    help="the character of workflow. eg. optimization, static.",
)
# 将一个子命令解析器与一个函数关联
parser_generate.set_defaults(func=wf_relaxation_submit)

parser_get_data = subparsers.add_parser(
    "get_data",
    help="get data from mongodb."
)
parser_get_data.add_argument(
    "-c",
    "--character",
    type=str,
    help="the character of workflow. eg. optimization, static."
    )
parser_get_data.set_defaults(func=get_data_mongodb)

# 解析命令行参数并执行
args = parser.parse_args()
# 执行方式 1；简洁
args.func(args)

# 执行方式 2
if hasattr(args, 'func'):
    if args.func == wf_relaxation_submit:
        return args.func(args)
    elif args.func == get_data_mongodb:
        return args.func(args)
```


---

### sys

- 可用于简易的命令行参数解析

```python
import sys

sys.path.append()            # 添加目录到 PATH 搜索路径
sys.argv                     # 命令行参数解析
sys.argv[0]                  # 文件名


def add_two_num(a, b):

    return a + b


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(add_two_num(a, b))
```


---

### shutil

```python
import shutil

shutil.copy()        # 拷贝文件
shutil.copytree()    # 拷贝目录
```


---

### pathlib

```python
from pathlib import Path

# 获取当前脚本文件所在的目录
# __file__ 内置变量，当前脚本的路径
THIS_DIR = Path(__file__).parent

# 创建目录
Path(...).mkdir(parents=True, exist_ok=True)
```


---

### subprocess

```python
# 执行 Shell 命令
import subprocess

subprocess.run(
    command,   # Shell 命令
    shell=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,
    text=True,
    capture_output=True,
)
```


---

### re

```python
import re

re.match()
```

正则表达式语法

```bash
# 符号       # 描述                          
.           # 匹配除了换行符之外的任意字符              
^           # 匹配字符串的开始                    
$           # 匹配字符串的结束                    
*           # 匹配前面的子表达式零次或多次              
+           # 匹配前面的子表达式一次或多次              
?           # 匹配前面的子表达式零次或一次              
{n}         # 精确匹配 n 次                    
{n,}        # 匹配 n 次以上                    
{n,m}       # 匹配 n 至 m 次                  
[abc]       # 匹配方括号内的任一字符                 
[^abc]      # 匹配不在方括号内的任一字符               
\d          # 匹配数字，等价于 [0-9]            
\D          # 匹配非数字，等价于 [^0-9]          
\s          # 匹配任何空白字符，等价于 [\t\n\r\f\v] 
\S          # 匹配任何非空白字符                   
\w          # 匹配字母数字，等价于 [a-zA-Z0-9_]   
\W          # 匹配非字母数字                     
\b          # 单词边界                        
```


---

### threading

```python
import threading
```


---

### multiprocessing

```python
import multiprocessing
```


---

### dataclasses

使用 `@dataclass` 装饰器可以自动为类生成几个魔法方法，包括 `__init__()`、`__repr__()`、`__eq__()` 等

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```


---

### pprint

- 以一种格式化和层次清晰的方式输出 dict 内容

```python
from pprint import pprint

d = {...}
pprint(d)       
```


---

## 其他

在编程语言中，"foo" 和 "bar" 被广泛应用于各种示例代码中，通常用于表示任意的变量、函数或数据结构。

---

Python 本身并不直接支持 OpenMP。OpenMP 主要用于 C/C++ 或 Fortran 等语言

GIL（Global Interpreter Lock）: 互斥锁，它防止多个线程同时执行 Python 字节码。这意味着即使使用多线程，标准的 Python 解释器也无法实现真正的并行执行。不过，某些操作（如 I/O 或某些库函数）可以释放 GIL

---

```python
# copy() 与 deepcopy() 的区别
copy()        # 浅复制，原对象和复制对象可能共享内部对象
deepcopy()    # 深复制，原对象和复制对象是完全独立的，不共享内部对象


# == 与 is 的区别
==            # 检查是否相等
is            # 检查值是否相同
```
