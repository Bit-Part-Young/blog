---
title: Python 基础
top: false
pin: false
cover: false
toc: true
mathjax: true
math: true
summary: Python 基础
tags:
  - Python
categories:
  - 编程
date: 2023-10-25 10:30:00
abbrlink: "13440"
password:
---

# Python 基础

## 介绍

什么是 python
- 解释性的脚本语言：通过解释器来直接运行，不需要编译链接成二进制文件
- 动态类型语言：类型在运行时确定，不需要通过代码明文规定
- 面向对象语言：python 中一切皆对象

>[Python 基础语法 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/pl/python/basic/)


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

在 matplolib 中使用 latex
>[Use latex with matplotlib on HPCs where you can't sudo! · GitHub](https://gist.github.com/chiang-yuan/62fbcaae06bf77f793a8f9b5aed1ba70)


---

### 参考资料

>[GitHub - lijin-THU/notes-python: 中文 Python 笔记](https://github.com/lijin-THU/notes-python)


python 速查表
>[Python 3 备忘清单 & python cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/python.html)
>
>[GitHub - gto76/python-cheatsheet: Comprehensive Python Cheatsheet](https://github.com/gto76/python-cheatsheet)


>[GitHub - piglei/one-python-craftsman: 来自一位 Pythonista 的编程经验分享，内容涵盖编码技巧、最佳实践与思维模式等方面。](https://github.com/piglei/one-python-craftsman)


《编程不难》书籍源码
>[GitHub - Visualize-ML/Book1\_Python-For-Beginners: Book\_1\_《编程不难》 | 鸢尾花书：从加减乘除到机器学习；已文件还会经过至少两轮修改，改动会很大，大家注意下载最新版本。请多提意见，谢谢](https://github.com/Visualize-ML/Book1_Python-For-Beginners)


multiprocess 多进程
>[（数据科学学习手札70）面向数据科学的Python多进程简介及应用 - 费弗里 - 博客园](https://www.cnblogs.com/feffery/p/11621076.html)


进度条
>[（数据科学学习手札91）在Python中妥善使用进度条 - 费弗里 - 博客园](https://www.cnblogs.com/feffery/p/13392024.html)


Python tips and tools
>[GitHub - pablovegan/Python-tips-tools: Short Python tips and tools talk for the Superconducting Qubit Technology school at Benasque 2023.](https://github.com/pablovegan/Python-tips-tools)





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

建议使用 miniconda 安装


---

## 运行

通过命令行运行 python 脚本
```bash
python code.py
```


在命令行中直接执行 python 代码，用于快速测试一些代码片段或进行简单的计算
```bash
python -c 'import matplotlib; print(matplotlib.matplotlib_fname())'
```


查看 python 环境变量
```bash
python --help-env
```


`python -m` - 在命令行中使用 Python 模块（通常用于运行那些设计为可以作为脚本执行的模块，如 `venv`、`pip` 等）

```bash
python -m venv venv

python -m pip install <package>
```


---

## 语法

### 变量

- 动态类型，不需要规定类型（可以通过 `变量名: 类型 = 内容` 来进行类型标注）



临时变量 `_`

---

#### 变量命名规则

全大写一般表示常量


---

### 数据类型

---

#### 字符串

- 拼接：直接将字符串 " 相加 "
- "…".upper()、"…".lower()：转为全大写、全小写
- "…".title()：单词首字母大写
- "…".strip()：删除字符串首尾空白（包含空格和制表符）
- "…".lstrip()、"…".rstrip()：删除左、右端空白
- "…".split(c)：根据字符 c 来拆分字符串得到列表，默认拆分空白


`str.strip()`：用于去除字符串两端指定字符（默认是空格）的函数

---

##### f-string

- 格式化（在填入内容后面加冒号 f"…{ 表达式 : 格式 }…"）
    - 宽度填充：:[ 填充字符 ][ 对齐方式 ][ 宽度 ]，< 左对齐，> 右对齐，^ 居中
    - 字符截断：:[…].n，只显示字符串的前 n 个字符
    - 数值符号：:+ 正数加正号、负数加负号，:- 原样，: （空格）正数加空格、负数加负号
    - 数值精度：:[ 宽度 ][ 分隔符 (,_)].[ 精度 ]f，没有精度默认为 6
    - 进制显示：x 小写十六进制，X 大写十六进制，o 八进制，b 二进制，加 # 显示前缀

```python
struct_id = f"ICET-Training-No-{i+1:05d}"

# 大括号转义 需写两个 {{
sh_cmd = f"grep -m 1 Loop log.lammps | awk '{{print $9}}'"
```

---

#### 布尔类型

- True 和 False，记住首字母大写
- 用 bool(…) 来转换，如果是数字则非零都是 True，如果是字符串则非空都是 True
- 运算
    - 可以使用 & | 来表示与和或（但并不会短路）
    - 一般使用 and or not 进行与 / 或 / 非运算（会短路）


---

#### 列表

内部元素不要求同一类型
- 索引可以是负数，负数即表示倒数，例 lst[-2] 表示倒数第二个元素
- 切片（获取列表中的一部分值）
    - lst[a:b]：从 lst[a] 到 lst[b-1] 的列表
    - lst[:b]：从开头到 lst[b-1] 的列表
    - lst[a:]：从 lst[a] 到结尾的列表
    - lst[:]：表示整个列表（拷贝一份）
    - lst[a:b:c]：从 lst[a] 到 lst[b-1] 每 c 个（即步长）取一个形成的列表
    - c 可以是负数，此时需要 a > b 才能获取到值
    - 有步长时若省略 a、b 记得不要省略冒号，例 lst[::-1] 表示列表倒序



列表操作

- 修改元素：直接通过索引 / 切片，然后等号赋值

- lst.append(…) 在列表末尾加入元素


列表拼接

- 直接相加，不改变原列表，得到新的列表
- lst.extend([…])，把一个列表接到当前列表后面

- 排序列表
    - lst.sort() 永久排序（即排序后赋值给当前列表）
    - sorted(lst) 临时排序，返回排序好的新列表
    - 默认从小到大，如果传入 reverse=True 则从大到小
- 反转列表
    - lst.reverse() 永久反转（意义同上）
    - lst[::-1] 返回反转的列表（利用前面说到的切片）
- 统计操作
    - len(lst) 得到列表的长度
    - sum(lst) 得到列表的元素和（本质上是将 start 参数和每个元素依次相加）
        - 可以传入 start 参数用来指定加和的起始值
    - max(lst) 得到列表中的最大值
    - min(lst) 得到列表中的最小值


---

#### 元组

括号表示元组，可以看成元素不可变的列表，内部也可以包含不同类型的元素

当只有一个元素的时候要写成 (a,) 而不是 (a)（后者是单个值）

- 可以使用 tuple(…) 来将可迭代对象（列表、字符串等）转为元组



---

#### 字典

- 存储键值对，也是大括号括起来，不过逗号分隔的是键值对 {key: value, …}
- {} 是空字典而不是空集合
- 通过 d[key] 来访问字典中 key 对应的值，可以读取、修改
- 添加键值对可以直接通过 d[key] = value 来进行
- 删除键值对可以直接 del d[key]
- 通过 d[key] 访问值时如果不存在 key 这个键会抛出异常
    - 通过 d.get(key) 来访问值时如果不存在则会返回 None
    - 使用 d.get(key, default) 如果没有 key 时会返回 default 值
- d.update(d2) 来用 d2 中的键值对更新 d




参数的形式转换成字典
```python
incar_tags = dict(
    System="initial relax",
    NSW=100,
    POTIM=0.1,
)

# output
# {'System': 'initial relax', 'NSW': 100, 'POTIM': 0.1}
```


---

#### 集合

大括号括起来，会自动去重，可用 set(…) 来将可迭代对象转为元组

- 集合中不能包含列表等不可 hash 化的元素

- 运算
    - s1 & s2、s1 | s2、s1 - s2 交集、并集、差集
    - s1 ^ s2 对称差集

---

### 条件分支

#### 布尔表达式

- 判断元素是否在列表中
    - value in lst：如果在则值为 True
    - value not in lst：如果在则为 False（判断是否不在）

---

#### 条件语句

- 类三目运算符写法 a if condition else b
    - 类似其它语言中的 condition? a : b


---

### 循环

- python 中的 for 循环并不像 c 中是指定一个变量的变化方式，而是从列表 / 元组 / 迭代器等可迭代对象中遍历值

- 可以使用 range 来生成一串数字用来循环
    - range(a, b) 生成从 a 到 b-1 的连续整数
    - range(a, b, c) 以 c 为步长生成
    - range 得到的并不是列表，如果要用其生成列表要使用 list(range(…))

---

#### 遍历字典

```python
# 遍历所有键
for key in d.keys():
    ...

# 遍历所有值
for value in d.values():
    ...

# 遍历键值对
for item in d.items():
    ... # item 为一个元组

for key, value in d.items():
    ... # 将 item 解包

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
    - 循环次数为最短的对象的长度

```python
for i, value in enumerate(lst):
    ... # i 依次为 0，1，2，……

for i, value in enumerate(lst, start=1):
    ... # i 依次为 1，2，3，……

for a, b in zip(lst1, lst2):
    ... # a 在 lst1 中循环
        # b 在 lst2 中循环

```


---

#### 列表推导

```python
lst = []
for i in range(1, 10):
    lst.append(i**2)
## 等价于
lst = [i**2 for i in range(1, 10)]

lst1 = [x*y for x in l1 for y in l2]

lst2 = [... for ... in ... if ...]

```

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
def func_name(arg1, arg2):
    ...

def func_name(arg1, arg2):
    ...
    return ...

def func_name(arg1, arg2):
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
- 函数参数为要显示的提示符，例如 input("> ")
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




---

### 类

`dir`：查看类的（实例）所有的属性和方法；函数的所有参数
```python
dir(struc)
```

- 类可以看成包含一些**属性**和**方法**的框架
- 根据类来创建对象 -> 实例化
- 用 class 关键字来定义类
- 类中的函数 -> 方法
    - 特殊方法 **init**，在类实例化的时候会被自动调用
    - 其它一般的方法第一个参数都要为 "self"，调用的时候会自动传入


```python
class ClassName():
    a = 1
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def method(self):
        print(self.arg1, self.arg2, self.a)

obj = ClassName(2, 3)
obj.method() # 2 3 1
print(obj.a, obj.arg1) # 1 2

- 直接写在类中的是属性，也可以通过为 self.\<name> 赋值的形式创建属性
- 用类似函数调用的形式实例化类，参数为 **init** 方法的参数
- 直接通过 .\<method> .\<attribute> 的形式调用方法 / 获取属性
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

文档字符串

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




---

### 执行 shell 命令

>[python环境下运行bash命令 | Jun's Blog](https://www.jun997.xyz/2022/03/19/e62b13aed44c.html)

- 方式 1（使用简单）

```python
import subprocess

subprocess.run("tar -xzvf *.tar.gz > /dev/null 2>&1", shell=True)
```

>`sed` 命令用这种方式好像有些问题

---

- 方式 2

```python
import subprocess

shell_cmd = f"python copy_data.py 0 100"
subprocess.run(["sed", "-i", f"s/^python.*/{shell_cmd}/g", "run_python.slurm"])
subprocess.run(["sbatch", "run_python.slurm"])
```

注：通配符、重定向和错误处理在 `subprocess.run` 中不能直接使用

```bash
# ×
subprocess.run(["tar", "-xzvf", "**.tar.gz", ">", "/dev/null", "2>&1"])
# √
subprocess.run(["tar", "-xzvf", "txt.tar.gz"],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
```



---

### 命令行参数解析

单个命令行参数解析：`parser.add_argument()`

```python
import argparse

parser = argparse.ArgumentParser(description="POSCAR file coordinates format conversion calling pymatgen.", epilog="Author: YSL.")
parser.add_argument("-f", "--file", type=str, default="POSCAR", help="POSCAR file.")
args = parser.parse_args()

write_poscar(poscar_file=args.file)
```


多个子命令的命令行参数解析：`subparsers = parser.add_subparsers()`


```python
import argparse

parser = argparse.ArgumentParser(description="atomate optimization test.", epilog="Author: ysl.")

subparsers = parser.add_subparsers()

parser_generate = subparsers.add_parser("generate", help="generate atomate optimization workflows.")
parser_generate.add_argument(
	"-c",
	"--character",
	metavar="wf_character",
	type=str,
	help="the character of workflow. eg. optimization, static."
	)
parser_generate.set_defaults(func=wf_relaxation_submit)

parser_get_data = subparsers.add_parser("get_data", help="get data from mongodb.")
parser_get_data.add_argument(
	"-c",
	"--character",
	metavar="wf_character",
	type=str,
	help="the character of workflow. eg. optimization, static."
	)
parser_get_data.set_defaults(func=get_data_mongodb)

args = parser.parse_args()

if hasattr(args, 'func'):
	if args.func == wf_relaxation_submit:
		return args.func(args.character)
	elif args.func == get_data_mongodb:
		return args.func(args.character)
```


`sys.argv`

```python
import sys


def add_two_num(a, b):
    return a + b


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add_two_num(a, b))
```


---

## 常用模块

### os

```python
import os

# 获取 用户根目录路径
home_dir = os.path.expanduser("~")
home_path = os.getenv("HOME")

# 若目录/文件不存在则创建
os.path.exists(path) or os.mkdirs(path)

# 获取文件路径的最后一个文件名
os.path.basename(path)

# 获取路径的父目录名称
os.path.dirname(path)

# 获取环境变量的路径
variable_path = os.environ["PATH"]

# 合并路径
os.path.join()

# 创建多层级目录
os.makedirs(exist_ok=True)

os.chdir()

os.walk()

os.getcwd()
```


---

### shutil

```python
import shutil

# 拷贝文件
shutil.copy()

# 拷贝目录
shutil.copytree()
```


---

### pathlib

```python
from pathlib import Path

THIS_DIR = Path(__file__).parent
```



---

## 多线程、多进程

```python
import threading
```


---

### 并行

mpi4py


分布式内存



共享式内存

---

#### mpi4py

>[Python多进程并行编程实践-mpi4py的使用 - 知乎](https://zhuanlan.zhihu.com/p/25332041)

安装
```bash
python -m pip install mpi4py
```


```python
from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
size = comm.Get_size()


# 阻塞通信
# dest 消息的目标进程的标识符
# tag 消息的标签 整数值 发送者和接收者可以使用相同的标签来匹配消息
comm.send(data, dest=1, tag=11)

# 非阻塞通信
comm.isend(data, dest=1, tag=11)
```


非阻塞发送通常用于提高并行性，允许发送者继续执行其他任务，而不必等待接收者。但需要小心，确保在接收之前不要修改发送的数据，以免出现数据一致性问题。通常需要使用 `comm.irecv` 或其他方法来等待非阻塞发送的消息。



---

## 类型提示

类型提示（type hints），提高代码的质量和可维护性

- 基本 - `int`, `float`, `bool`, `str`
- 容器 - `List`, `Tuple`, `Dict`, `Set`
- `Optional`- 可选，指定变量可以是某个类型或者是 `None`
- `Type Aliases` - 类型别名，简化复杂的类型声明
- 函数类型提示 - 函数的参数和返回值可以有类型提示
- `Union` - 联合，允许变量是多个类型中的一个
- `Literal` - 字面量，指定变量的值只能是特定的几个字面量之一
- `Callable` - 指定对象是可调用的，比如函数或实现了 `__call__` 的对象


```python
from typing import List, Tuple, Dict, Set, Union, Literal
import numpy as np

input_array: np.ndarray

num: int = 5

numbers: List[int] = [1, 2, 3]

name: Optional[str] = None

def greet(name: str) -> str:

def add_num(input: Union[int, str]):

mode: Literal["r", "w", "x"] = "r"
```

>用 `np.ndarray` 做类型标注（无法指定其维数）


---

### 工具

mypy 静态类型检查工具

安装
```bash
pip install mypy
```

使用
```bash
mypy test.py
```

配置文件 `mypy.ini`
```bash
[mypy]
python_version = 3.11
warn_return_any = True
#warn_unused_configs = True
ignore_missing_imports = True

# Per-module options:
#[mypy-mchammer.*]
#disallow_untyped_defs = False
```

---

typeguard: python 类型检查
>[GitHub - agronholm/typeguard: Run-time type checker for Python](https://github.com/agronholm/typeguard)

---

## 代码风格格式化

>[GitHub - PyCQA/isort: A Python utility / library to sort imports.](https://github.com/PyCQA/isort)
>
>[GitHub - psf/black: The uncompromising Python code formatter](https://github.com/psf/black)
>
>[GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust.](https://github.com/astral-sh/ruff)


安装
```bash
pip install black

pip install "black[jupyter]"

pip install isort
```


使用
```bash
black {source_file_or_directory}

isort mypythonfile.py mypythonfile2.py

isort .
```


ruff


---

## 打包

项目打包参考
>[GitHub - CederGroupHub/alab\_control](https://github.com/CederGroupHub/alab_control)

>[setup.py](https://github.com/CederGroupHub/alab_control/blob/main/setup.py)


目录结构
```text
package_name/

setup.py
setup.cfg
pyproject.toml
```


python package 模板参考
>[GitHub - Quantum-Accelerators/template: A template for Python packages. Developed by the @quantum-accelerators](https://github.com/Quantum-Accelerators/template)

---

### 本地安装

```bash
pip install git+url
# or
pip install .
# or
pip install -r requirements.txt
# or
python setup.py install
```

>以上命令将 package 复制到 site-packages 中

---

```bash
# -e --editable
pip install -e .
```

- 编辑模式；创建指向项目源代码目录的链接（如 `site-package/spt.egg-link` 文件指向源代码 `spt/` 目录）；
- **源代码的任何更改都会立即反映在 Python 环境中，无需重新安装，方便调试开发**


---

### 配置文件

有 3 种文件格式（需要用到的一些文件：`requirements.txt` `README.md` `MANIFEST.in` 等）：

- `setup.cfg`（适用于不需要复杂构建逻辑的项目）
- `setup.py`（常用）
- `pyproject.toml`（更现代的方法）

---

`setup.py` 示例

```python
from distutils.core import setup
from setuptools import find_packages
# from setuptools import setup, find_packages

setup(
    name="package_name",
    version="0.0.1",
    description="description",
    long_description=open("README.md").read(),
    author="author_name",
    author_email="email",
    url="url",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.1",
    ],
    python_requires=">=3.6",
    platforms=["all"],
)
```

>`long_description` 参数在 `setup.py` 文件中主要用于提供 package 的详细描述，通常在 PyPI 上显示


在 `setup.py` 文件中指定入口点（`entry_point`）来生成命令行脚本

```python
from setuptools import setup, find_packages

setup(
	...
    entry_points={
        "console_scripts": [
            "va_generation=pdepp.model_generation.vacancy:main",
            "is_all_generation=pdepp.model_generation.interstitial:main",
            "is_va_generation=pdepp.model_generation.interstitial_vacancy:main",
        ],
    },
)
```

---

`setup.cfg` 示例

```ini
[metadata]
name = package_name
version = 0.1
author = Your Name
author_email = your.email@example.com
description = A short description of the project
long_description = file: README.md
long_description_content_type = text/markdown
url = https://example.com/project
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
install_requires =
    requests
    numpy

[options.extras_require]
dev =
    pytest
    flake8
```

---

`pyproject.toml` 文件

>[matplotlib pyproject.toml](https://github.com/matplotlib/matplotlib/blob/main/pyproject.toml)


- 基于 PEP 518 标准提出，旨在提供一个统一的配置格式来替代多个配置文件如 `setup.py`，`setup.cfg`，`requirements.txt` 等）的需要
- `[build-system]` - 指定构建系统的要求
- `[tool.some_tool]` - 配置特定工具的选项（如 pytest、ruff、isort 等）

```toml
[build-system]
requires = [
	"setuptools>=65.0.0", 
	"wheel",
]
build-backend = "setuptools.build_meta"

[project]
name = "spt"
version = "0.2.3"
description = "Scientific matplotlib plot rcParams configuration template python package."
authors = [
    {name = "yangsl", email = "3304839708@qq.com"},
]
maintainers = [
    {name = "yangsl", email = "3304839708@qq.com"},
]
dependencies = [
    "matplotlib>=3.7,<3.8",
    "numpy>=1.20.0",
]
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3"
]

[project.optional-dependencies]
examples = [
    "pandas",
    "scikit-learn",
]

[project.urls]
documentation = "https://github.com/Bit-Part-Young/spt"
repository = "https://github.com/Bit-Part-Young/spt"

[project.entry-points.console_scripts]
va_generation = "pdepp.model_generation.vacancy:main"
is_all_generation = "pdepp.model_generation.interstitial:main"
is_va_generation = "pdepp.model_generation.interstitial_vacancy:main"



```


其他相关设置
```toml
[project]
dynamic = ["version"]

[tool.setuptools_scm]
write_to = "mech2d/_version.py"

[tool.black]
line-length = 88
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.mypy_cache
  | \.venv
  | _build
  | build
  | dist
)/
'''

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
```




---

### 发布到 PyPI

- 在 [PyPI](https://pypi.org/)，[TestPyPI](https://test.pypi.org/)（可选） 注册账号；注册好并登录后需先设置 2FA（安卓端可以使用 Google 身份验证器 app），之后创建 `~/.pypirc` 配置文件（建议使用 API 的形式，而非用户名、密码的形式）

- 配置文件 `.pypirc` 示例

```bash
[distutils]
index-servers=pypi
 
[pypi]
username = __token__
password = pypi-AgEI...
```

- 安装 twine（上传 Python package 到 PyPI 的工具）

```bash
pip install twine

# 安装 pyproject.toml 构建工具
pip install build
```

- 构建 package

```bash
python setup.py sdist bdist_wheel

# 使用 pyproject.toml 构建
python -m build
```

- 上传到 TestPyPI 进行测试（可选）

```bash
twine upload --repository testpypi dist/*
```

- 检查

```bash
twine check dist/*
```

- 上传到 PyPI

```bash
twine upload dist/*
```
