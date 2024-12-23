---
title: C++ 学习
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: C++ 学习
description: C++ 学习
tags:
  - cpp
categories:
  - 编程
date: 2023-10-25 10:30:00
abbrlink: 520301
password:
---

# C++ 学习

## 介绍

C++ 数值优化库：[GitHub - mlpack/ensmallen: A header-only C++ library for numerical optimization --](https://github.com/mlpack/ensmallen)

---

### 参考资料

- 速查表
    - [C++ 备忘清单 & cpp cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/cpp.html)
    - [C++ Cheat Sheets & Infographics - hacking C++](https://hackingcpp.com/cpp/cheat_sheets.html)
    - [GitHub - mortennobel/cpp-cheatsheet: Modern C++ Cheatsheet](https://github.com/mortennobel/cpp-cheatsheet)

- Effective Modern C++ 中文翻译版：[简介 - Effective Modern C++](https://cntransgroup.github.io/EffectiveModernCppChinese/)

- [Setting up C/C++ compiler • C and C++ Programing](https://pranabdas.github.io/c-cpp/)

- [GitHub - ShujiaHuang/Cpp-Primer-Plus-6th: 《C++ Primer Plus 第6版（中文版）》原书代码、习题答案和个人笔记，仅供学习和交流。](https://github.com/ShujiaHuang/Cpp-Primer-Plus-6th)

- [cppreference.com](https://en.cppreference.com/w/)（页面可转换成中文）

- [GitHub - parallel101/cppguidebook: 小彭老师领衔编写，现代C++的中文百科全书](https://github.com/parallel101/cppguidebook)

- [C++ 面向对象 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/pl/c_cpp/oop/)

- [序言 现代 C++ 教程: 高速上手 C++ 11/14/17/20 - Modern C++ Tutorial: C++ 11/14/17/20 On the Fly](https://changkun.de/modern-cpp/zh-cn/00-preface/)

- [C++基础入门.md](https://github.com/AnkerLeng/Cpp-0-1-Resource/blob/master/%E7%AC%AC1%E9%98%B6%E6%AE%B5C%2B%2B%20%E5%8C%A0%E5%BF%83%E4%B9%8B%E4%BD%9C%20%E4%BB%8E0%E5%88%B01%E5%85%A5%E9%97%A8/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E8%AE%B2%E4%B9%89/C%2B%2B%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8.md)

- [GitHub - pranabdas/c-cpp: Learning programming concepts in C and C++](https://github.com/pranabdas/c-cpp)

- 与化学相关的 cpp 教程：[GitHub - CrawfordGroup/ProgrammingProjects: C++ Programming Tutorial in Chemistry](https://github.com/CrawfordGroup/ProgrammingProjects)

- 一个可供参考的 cpp 源代码（mpi、命令行参数相关）：[GitHub - idocx/CS267-HW2-2](https://github.com/idocx/CS267-HW2-2)

>[GitHub - howardlau1999/server-programming-guide](https://github.com/howardlau1999/server-programming-guide)


[【四、静态库与动态库（共享库）】揭开链接库的神秘面纱：手把手教你制作静态链接库与动态链接库\_Mindtechnist的博客-CSDN博客](https://blog.csdn.net/qq_43471489/article/details/124546183)

>[GitHub - parallel101/course: 高性能并行编程与优化 - 课件](https://github.com/parallel101/course)

>[双笙子佯谬的个人空间-双笙子佯谬个人主页-哔哩哔哩视频](https://space.bilibili.com/263032155)


>[GitHub - asartori86/advanced\_programming\_2021](https://github.com/asartori86/advanced_programming_2021)

- CPP-Primer
    - [GitHub - applenob/Cpp\_Primer\_Practice: 搞定C++:punch:。C++ Primer 中文版第5版学习仓库，包括笔记和课后练习答案。](https://github.com/applenob/Cpp_Primer_Practice)
    - [GitHub - minyez/cpp-primer-plus-6th: C++学习. 笔记和习题解答](https://github.com/minyez/cpp-primer-plus-6th)
    - [GitHub - yanghan234/CppPrimerNotes: My reading notes of C++ Primer, 5th Edition](https://github.com/yanghan234/CppPrimerNotes)


- [C 语言教程 - 网道](https://wangdoc.com/clang/)



---

## 使用

### 工具

- [VsCode中C/C++的launch.json文件模板 - SuiNian's Blog](https://blog.nianbroken.top/archives/254/)

- filesystem 标准库：[Filesystem library (since C++17) - cppreference.com](https://en.cppreference.com/w/cpp/filesystem)

- 命令行参数解析
    - [GitHub - p-ranav/argparse: Argument Parser for Modern C++](https://github.com/p-ranav/argparse)
    - [GitHub - r-lyeh-archived/getopt: Simple command-line options handler (C++11)](https://github.com/r-lyeh-archived/getopt)


---

### 运行

```bash
g++ main.cpp            # 可执行文件名称默认为 a.out
g++ main.cpp -o main    # 指定可执行文件名称


# 编译器标志
-I           # 链接头文件路径
-L           # 链接库路径
-O[0-3]      # 不优化到逐级增强的优化
-Os          # 空间优化
-g           # 生成调试信息
-std         # C++ 标准，c++11 c++14 c++17 c++20
-Wall
-Wunused     # 
-Wextra
-Werror
-fopenmp     # 启用 OpenMP 支持
-static      # 生成静态的可执行文件
-shared      # 生成共享链接的可执行文件

-march=native -mtune=native   # 目标平台，使用 native 一般可以获得最高性能
```

---

头文件搜索规则：

- 从 `-I` 开始
- 找环境变量 `C_INCLUDE_PATH`、`CPLUS_INCLUDE_PATH`、`OBJC_INCLUDE_PATH` 指定的路径
- 找默认目录 `/usr/include`、`/usr/local/include` 等

Linux 头文件路径：`/usr/include` 或 `/usr/local/include`

库文件路径：`/usr/lib` 或 `/usr/local/lib`（`.so` 动态库 `.a` 静态库）

---

- [静态库和动态库的认识](https://mp.weixin.qq.com/s/8-wwPEvhZgypPEkOmWa6CA)

- 静态链接库：`lib*.a` (Linux)、`*.lib` (Windows)
    - 静态链接库本质上是一个归档文件，它包含了一个或多个目标文件（`.o` 文件，包含了编译后的代码和数据）。使用静态链接库时，链接器会将这些目标文件中的代码和数据直接嵌入到最终生成的可执行文件中
    - 优点：运行速度快；缺点：目标文件大，且静态链接不能共享

- 动态链接库：`lib*.so` (Linux; Shared Object，SO，共享对象)、`*.dll` (Windows; Dynamic Link Library, DLL)
    - 在运行时链接对应的库来访问这些函数
    - 可被多个程序所共享

- 构建静态链接库

```bash
# 假设有 add.c minus.c main.c add_minus.h

# 只编译，不链接
gcc -c *.c
# 使用 ar 工具，将 add.o 和 minus.o 打包成静态库
ar rc libadd_minus.a add.o minus.o
# 链接生成目标文件 main
gcc -o main main.o -L. -ladd_minus

-L           # 指定库文件搜索路径
-l           # 指定要链接的库名称
```

- 构建动态链接库

```bash
gcc -fPIC -shared add.c minus.c -o libadd_minus.so

gcc -c main.c

gcc -o main main.o -L. -ladd_minus
```


---

Makefile

```bash
CC=g++
CFLAGS=-O3 -Wall



    $(CC) $(CFLAGS) -o $@ $^


    $(CC) $(CFLAGS) -o $@ -c $^
```


---

### 调试

gdb 或 cppcheck

GDB 使用入门：[Note/wiki/gdb.md at master · Kicamon/Note · GitHub](https://github.com/Kicamon/Note/blob/master/wiki/gdb.md)


```bash
gdb main.o
```



---

## 语法

`\n` 比 `endl` 快（`endl` 会刷新缓冲区）


数组索引从 0 开始，没有像 Python 中一样使用 -1 表示最后一个元素的特殊用法


```cpp
#include <cstdio>          // C 标准 IO
#include <bits/stdc++.h>   // 导入整个 C++ 标准库

using namespace std     // 命名空间；不建议，可能会导致命名冲突


#define a 1        // 宏常量
const int a = 1;   // 声明常量


// 浮点数比较，用 == 很危险
if (abs(a - b) < 1e-9)  
{  
    // a and b are equal  
}


```


---

### 数据类型

十进制整数不能以 0 开头（会被认为是八进制整数）

字符用单引号，字符串用双引号（相当于字符数组）

```cpp

sizeof(int)   // 查看数据类型所占内存大小
sizeof(a)

// 字符型
char ch = 'a';

// 字符串型
char str1[] = "Hello World";  // C 风格

#include <string>

string str2 = "Hello World";  // C++ 风格


// 布尔类型
bool flag = true;
```


---

### 数组

```cpp
// 一维数组定义
int array1[5] = {1};
int array2[5] = {1, 2, 3, 4, 5};
int array3[] = {1, 2, 3, 4, 5};
int array4[5] = {};
int array5[5] = {1, 2};
```

---

### 流程控制

#### if 条件

```cpp
if (condition)  // if 后面不加分号
{
    // commands
}

if (condition)
{
    // commands
}
else
{
    // commands
}

if (condition1)
{
    // commands
}
else if (condition2)
{
    // commands
}
else
{
    // commands
}
```


---

#### for 循环

```cpp

```


基于范围的 for 循环的语法如下：
```c++
for (element_declaration : range_expression) {
    // 循环体
}
```
其中，element_declaration 是一个变量，用于存储每次迭代中的元素值。range_expression 是一个表示要遍历的容器或对象的表达式。


---

### 文件 IO

```cpp
#include <fstream>      // 文件流

```


---

### 格式化输出

```cpp
// 方式 1
#include <iomanip>

setprecision()   // 设置精度 
setw()           // 设置宽度


// 方式 2
#include <cstdio>

printf()


// 方式 3
#include <format> // C++20 引入的头文件

format()
```


---

### 函数

函数中引用参数的作用：修改传递给函数的变量的值：通过引用参数，函数可以修改传递给它们的变量的值，这样可以在函数内部对变量进行修改，并将修改后的值反映到函数外部。


---

### 类

- C++ 中 class 和 struct 并无本质区别，只是默认的访问权限不同（class 默认 private，struct 默认 public）

- 权限有三种：
    - public：公有
    - private：私有（只有同类可以访问）
    - protected：保护（只有同类和子类可以访问）


---

### 结构体

WIP...


---

### 重载

函数重载

运算符重载

---



C++ 新特性

---

### 模板 template

T 表示参数类型

```cpp
template <class T>
```

函数模板


类模板




---

### 其他

字符串转整数：

`stoi()`（标准库中的函数）
`atoi()`（C 风格的函数）

---

解析命令行参数：[c++ - What does int argc, char \*argv[] mean? - Stack Overflow](https://stackoverflow.com/questions/3024197/what-does-int-argc-char-argv-mean)

```cpp
#include <iostream>

int main(int count, char* args[]) {
    std::cout << "参数个数: " << count << std::endl;
    for (int i = 0; i < count; ++i) {
        std::cout << "参数 " << i << ": " << args[i] << std::endl;
    }
    return 0;
}

```



---

## 库

- `<iostream>`：基本输入输出流；`cin`, `cout`, `cerr`, `endl`

- `<fstream>`：文件输入输出流；`ifstream`, `ofstream`, `fstream`

- `<sstream>`：字符串流；`istringstream`, `ostringstream`, `stringstream`

- `<cmath>`：提供数学函数支持；`sin()`, `cos()`, `exp()`, `log()`, `sqrt()`

- `<ctime>`：传统的 C 语言日期和时间函数；`time()`,


---

### string

- [string.h - C 语言教程 - 网道](https://wangdoc.com/clang/lib/string.h)

`string`、`string.h` 和 `cstring` 之间的区别：

1. `string`：`string` 是 C++ 标准库中的一个类，位于命名空间 `std` 中。它提供了一种更高级、更安全和更方便的字符串处理方式。`string` 类提供了许多成员函数和操作符重载，用于操作和处理字符串。使用 `string` 类可以更容易地进行字符串的拼接、查找、替换等操作，而且不需要手动管理内存。
2. `string.h`：`string.h` 是 C 语言标准库中的一个头文件，用于操作 C 风格的字符串（字符数组）。它提供了一些用于字符串操作的函数，如 `strcpy`、`strlen`、`strcat` 等。这些函数需要手动管理内存，并且对于一些边界情况需要特别小心，以避免缓冲区溢出和内存错误。
3. `cstring`：`cstring` 是 C++ 标准库中的一个头文件，对应于 C 语言的 `string.h` 头文件。它提供了与 `string.h` 相同的 C 风格字符串操作函数，如 `strcpy`、`strlen`、`strcat` 等。使用 `cstring` 头文件可以在 C++ 中使用 C 语言的字符串操作函数。


总的来说，`string` 类提供了更高级、更安全和更方便的字符串处理方式，而 `string.h` 和 `cstring` 提供了 C 语言风格的字符串操作函数，需要手动管理内存。在 C++ 中，更推荐使用 `string` 类来进行字符串操作，除非有特定的原因需要使用 C 语言的字符串操作函数。




在 C++ 中，`<cstring>` 头文件是 C 语言标准库中的头文件 `<string.h>` 的 C++ 版本。因此，当包含 `<cstring>` 头文件时，C++ 编译器会自动将 `<string.h>` 中的函数放在 `std` 命名空间中。

因此，当您包含 `<cstring>` 头文件时，可以直接使用 `strcpy` 函数，因为它已经在 `std` 命名空间中。这意味着您可以使用 `std::strcpy` 或者直接使用 `strcpy`，它们是等效的。

而在 `<string.h>` 头文件中，函数是直接定义在全局命名空间中，因此只能使用 `strcpy`，而不能使用 `std::strcpy`。

总结起来，`<cstring>` 头文件提供了 C 语言字符串操作函数的 C++ 版本，并将这些函数放在了 `std` 命名空间中，因此可以使用 `std::strcpy` 或者直接使用 `strcpy`。而 `<string.h>` 头文件中的函数是直接定义在全局命名空间中，只能使用 `strcpy`。


![string cheatsheet](https://hackingcpp.com/cpp/std/string.png)


---

### vector

![vector cheatsheet](https://hackingcpp.com/cpp/std/vector.png)


array


---

### Eigen

><https://eigen.tuxfamily.org/dox/GettingStarted.html>

- 安装：下载源代码，可放到任意路径下

```bash
brew install eigen  # macOS；头文件 /opt/homebrew/include/eigen3
```

- 编译

```bash
g++ main.cpp -o main -I /path/eigen
```
