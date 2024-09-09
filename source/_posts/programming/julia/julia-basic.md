---
title: Julia 基础
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Julia 基础
description: Julia 基础
tags:
  - Julia
categories:
  - 编程
  - Julia
date: 2023-07-22 15:56:30
abbrlink: 220756
password:
---

# Julia 基础

## 介绍

默认环境：`~/.julia/environments/v1.9/`

科学计算编程语言

`===`：完全相等性比较，还需要具有相同的内存地址

`ByRow(f)`：以 f 函数进行变换

```julia
# 创建未初始化的 Matrix
Matrix{T}(undef, m, n)

# 读取文本所有行，可以不用 open()
readlines()
```


```julia
typeof()
```


---

### 参考资料

- 教程：[Julia语言入门](https://www.math.pku.edu.cn/teachers/lidf/docs/Julia/html/_book/index.html)
- Julia 与其他语言的差异：[与其他语言的显著差异 · Julia中文文档](https://cn.julialang.org/JuliaZH.jl/latest/manual/noteworthy-differences/#Noteworthy-differences-from-Python)
- Julia 速查表：[Julia 备忘清单 & julia cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/julia.html)
- Julia 微积分笔记：[Calculus with Julia](https://jverzani.github.io/CalculusWithJuliaNotes.jl/)
- [GitHub - RoyiAvital/Julia100Exercises: A set of introductory exercises for Julia. Based on \[100 NumPy Exercises\](https://github.com/rougier/numpy-100).](https://github.com/RoyiAvital/Julia100Exercises)
- [GitHub - Leticia-maria/Introduction.jl](https://github.com/Leticia-maria/Introduction.jl)

- [Julia Tips - My digital garden](https://sosiristseng.github.io/julia/)
- [Modern Julia Workflows](https://modernjuliaworkflows.github.io/)



---

## 安装

- 二进制版本下载：
	- [julia-releases - 清华大学镜像站](https://mirror.tuna.tsinghua.edu.cn/julia-releases/bin/)
	- [Download Julia](https://julialang.org/downloads/)

```bash
brew install Julia  # macOS
```

- 官方包注册表：[GitHub - JuliaRegistries/General: The official registry of general Julia packages](https://github.com/JuliaRegistries/General)

- Julia 包镜像：[交大镜像](https://mirror.sjtu.edu.cn/docs/julia)

```bash
# 设置环境变量
export JULIA_PKG_SERVER=https://mirrors.sjtug.sjtu.edu.cn/julia

# 若成功切换镜像，可查询到相关信息 
versioninfo()
```



---

## 使用

### 工具

- 代码格式化：JuliaFormatter

- Julia VSCode 插件：需设置 Julia 二进制文件路径，才能使用查看 API、在 REPL 中执行代码等功能
	- 激活 Julia 环境：输入 “Julia: Activate This Environment”
	- 更换 Julia 环境：输入 “Julia: Change Current Environment”
	- 在 VSCode 中的 Jupyter Notebook 中运行 Julia 代码（只能是默认的 Julia 环境）
	- [ ] 如何在 jupyter notebook 中的使用其他的 julia 环境

```json
{
    "julia.executablePath": "~/bin/julia",
}
```

- IJulia：Julia 的 Jupyter Notebook

```julia
using IJulia

notebook()
```

```bash
# 连接 Jupyter 需输入 token，查看 token
~/.julia/conda/3/x86_64/bin/jupyter server list
```


---

### REPL

- REPL：交互式会话（read-eval-print loop）
- 按 `Tab` 键可以自动补全
- Julia 的 REPL 有四种 mode
- 退出 Juila mode：`Ctrl + D` 键或输入 `exit()`
- 退出 Help、Shell、Search 到 Julia mode：`Backspace` 或 `Crtl + C` 键

```bash
# 四种 mode 的 prompt
julia>                  # Julia
help?>                  # Help；按 ? 键进入；可查看函数等文档帮助
shell>                  # Shell；按 ; 键进入
(reverse-i-search)`':   # Search；按 Ctrl + R 键进入
```


---

### 运行

```bash
julia script.jl              # 基本
julia --project=. script.jl  # 指定环境
julia> include("script.jl")  # REPL 下
```


---

### 使用环境

- 参考：[4. 使用"环境" · Pkg.jl](https://cn.julialang.org/Pkg.jl/dev/environments/)

- 进入 pkg，执行 `activate .`，激活该目录使其成为 “活动项目”；添加 package（会生成 `Project.toml` 项目文件及 `Manifest.toml` 清单文件）

- 使用他人的项目
	- 注：若项目包含 manifest，则以该 manifest 给出的相同状态安装包；否则，将解析与项目兼容的最新版本的依赖项

```bash
# 克隆
git clone https://github.com/JuliaLang/Example.jl.git

# 激活环境
(@v1.8) pkg> activate Example.jl
Activating project at `~/Example.jl`

# 安装依赖/解析
(Example) pkg> instantiate
  No Changes to `~/Example.jl/Project.toml`
  No Changes to `~/Example.jl/Manifest.toml`
```


---

### 包管理

- 参考：
	- [Julia Packages](https://juliapackages.com/)
	- [2. 入门 · Pkg.jl](https://cn.julialang.org/Pkg.jl/dev/getting-started/)

- 键入 `]` 进入 pkg（交互式包管理模式； `BACKSPACE` 或 `Crtl + C` 键退出）

```bash
# 安装 package
# 方式 1：不进入 pkg
julia> using Pkg
# import Pkg
julia> Pkg.add("Example")
# Pkg.add(["AtomsIO", "AtomsIOPython", "ASEconvert"])

# 方式 2：进入 pkg
(@v1.9) pkg> add Example
# 安装多个 package
(@v1.9) pkg> add JSON StaticArrays
# 删除
(@v1.9) pkg> rm JSON StaticArrays
# 更新
(@v1.9) pkg> up
# 查看已安装的包
(@v1.9) pkg> st
# 包括递归依赖包
(@v1.9) pkg> st -m
```


---

#### 创建包

```bash
(@v1.9) pkg> generate HelloWorld
```

目录结构
```bash
. 
├── Project.toml 
└── src 
	└── HelloWorld.jl
```


---

#### 注册包

注册包，类似 Python 的 package 打包发布到 PyPI


---

### 注册表

>[7. 注册表 · Pkg.jl](https://cn.julialang.org/Pkg.jl/dev/registries/)

- 默认自动安装 [General](https://github.com/JuliaRegistries/General) 注册表

```bash
# 进入 pkg
# 添加注册表
registry add General
registry add https://github.com/JuliaRegistries/General 
registry add https://github.com/ACEsuit/ACEregistry

registry st          # 查看已安装的注册表
registry rm General  # 移除注册表
registry up          # 更新注册表

```


---

## 语法

### 注释

```julia
# 单行注释

#= 多行注释
function f(x)
    return x^2 + 1
end
=#
```


---

### 输出

`println` 会自动添加换行符，`print` 不会


```julia
println()
```


---

### 变量

Unicode 字符可以作为变量名（不建议）
```julia
❄ = -12
```

```bash
# 环境变量
JULIA_CPU_THREADS   # 逻辑 CPU 核心数
JULIA_NUM_THREADS   # 设置 Julia 可用线程的最大数
```


复合表达式

- `begin ... end`
- `(..., ..., ...)`
- `...;...`



---

### 数据类型

#### 字符串

字符串属于不可修改类型 (immutable)， 即不能直接修改字符串的内容， 但可以给保存了字符串的变量赋值为一个新的字符串。


字符串连接 - `*`
字符串重复 - `^`
字符串插值 - `$var`，`$(expression)`

Julia 可识别 Unicode math（输入 LaTeX 符号，按 Tab 键，可补全成 Unicode symbols，部分可用作运算符）
>[Unicode Input · The Julia Language](https://docs.julialang.org/en/v1/manual/unicode-input/)

- π `\pi`+TAB
- ÷ `\div`+TAB
- ≥ `\ge`+TAB
- ≤ `\le`+TAB
- ≠ `\ne`+TAB
- ∈ `\in`+TAB
- ⊂ `\subset`+TAB
- ⊃ `\supset`+TAB
- 🐢– `\:turtle:`+TAB
- √ `\sqrt`+TAB


字符串处理相关函数
```julia
parse()
strip()
split()
```



---

#### Symbol

符号是一种特殊的数据类型，用于表示固定且不可变的标识符。它们在代码中以冒号 `:` 开头

```julia
elements = [:Si,]
# elements = [:Si]
```


---

### 函数

```julia
f(x) = x^2 + 3*x + 1

f(2)
f(1.1)
```



```julia
function func(x, y, z)
	...
end

function foo(x, y)
x = Int(x); y = Int(y)
...
end
foo(x, y)

# 添加类型注释
function foo(x::Int, y::Int)::Int
...
end
foo(Int(x), Int(y))
```


```julia
# mysd: Input numeric vector x, output its sample standard deviation.
function mysd(x)
	n = length(x)
	mx = sum(x) / n
	s = 0.0
	for z in x
		s += (z - mx)^2
	end
	sqrt(s / (n-1))
end


# 调用
mysd([1, 2, 3, 4, 5])
```


- [ ] 添加!，含义是什么

用于表示该函数会对其参数进行原地修改（in-place modification）。换句话说，带有 `!` 的函数会改变至少一个传入参数的内容或状态，而不是创建一个新的副本并返回。


`;` 前是位置参数，后是关键字参数

可变参数：参数名添加 `...`

```julia
# 位置参数的示例
function add(x, y)
    return x + y
end

# 关键字参数的示例
function greet(name; title="Mr.")
    println("Hello, $title $name")
end

# 默认参数的示例
function pow(base, exponent=2)
    return base ^ exponent
end

# 可变参数的示例
function sum_all(...args)
    return sum(args)
end

# 类型注解的示例
function divide(x::Float64, y::Float64)
    return x / y
end

# 匿名函数的示例
map(x -> x^2, [1, 2, 3, 4])

# 高阶函数的示例
function apply_function(f, values)
    return f(values)
end

apply_function(sum, [1, 2, 3, 4])

```


---




if-elseif-else-end 结构
```julia
age = 35
if age < 18
  println("未成年")
elseif age < 60
  println("中青年")
elseif age < 100
  println("老年")
else
  println("老寿星！")
end
## 中青年
```


循环

```julia
for loopvar = a:b
  expr1
  expr2
  ...
end
```


```julia
# 方式1
for i in 1:10
	println(i)
end

# 方式2
for i in 1:10
	println(i)
end
```


---

枚举
```julia
arr=collect(1:5)
for (idx, val) in enumerate(arr) 
	println("the $idx-th element is $val") 
end
```


嵌套循环
```julia
# 9x9乘法表
for i=1:9
    for j=1:i
        print(j, "×", i, "=", i*j, " ")
    end
    println()
end
```


---

### 数据结构

missing 对象表示缺失值， 缺失值不区分具体类型， 属于 Missing 数据类型

#### 数组

>索引起始为 1，与 Fortran 相同，与 Python、C++ 不同；end 表示最后一个元素的位置

```julia
v1 = [2, 3, 5, 7, 11, 13, 17]
v2 = [1.5, 3, 4, 9.12]
v3 = ["苹果", "桔子", "香蕉"]
v4 = [123, 3.14, "数学", [1, 2, 3]]

length(v1)

@show v1
```


数组的类型标注为 `Array{Type, N}`，其中 `Type` 是元素类型，`N` 是数组的维度。例如，`Array{Int, 1}` 表示一个整数类型的一维数组。

`@show expr` 可以用比较简洁的带有提示的方式



范围：范围不是向量， 而是一种 “ 可遍历数据结构 “。 用 `collect()` 函数可以将范围转换成向量
```julia
1:5
## 1:5
1:2:7
## 1:2:7
5:-1:1
## 5:-1:1

collect(5:-1:1)
```



```julia
v1 = [2, 3, 5, 7, 11, 13, 17]
v1[:] .= 0; 
@show v1;
## v1 = [0, 0, 0, 0, 0, 0, 0]
```


数组类型：`Array{Int64}`、`Array{Float64}`、`Array{String}`、`Array{Any}`（可容纳任何 Julia 对象作为元素）等；`eltype()` 查看类型


相关函数
```julia
# v为向量，x为元素，u为向量
# 将x添加到向量v的末尾
push!(v, x)
# 将u的所有元素添加到向量v的末尾
append!(v, u)
# 返回v的最后一个元素并从v中删除此元素
pop!(v)
```


Julia 中的函数， 包括自定义函数， 如果可以对单个标量执行， 将函数名加后缀句点后， 就可以变成向量化版本， 对向量和矩阵执行。 这称为**广播**。 运算也是如此，运算符前面加点后就可以将标量运算应用到元素之间的运算。
```julia
sqrt.([1,2,3])
```



列表推导
```julia
xcube = [i^3 for i=1:3]
```


---

#### 元组

同 python


命名元组
```julia
data_keys = (energy_key = "energy", force_key = "forces")

data_keys.energy_key
```


---

#### 字典

- Python 中的 `:` 变成 `=>`；元素访问相同
- `keys()` - 遍历字典键；`values()` - 遍历字典值


```julia
d = Dict("name" => "Li Ming", "age" => 18)

# 指定键和值的数据类型
Dict{String,Int64}("apple" => 1, "pear" => 2, "orange" => 3)

# 用二元组的数组作为初值定义字典
d2orig = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
d2 = Dict(d2orig)

# zip() 函数
x = ["a", "b", "c", "d"]
y = [1, 2, 3, 4]
d2 = Dict(zip(x, y))
```



字典推导
```julia
Dict(x => x * x for x in [2, 3, 5, 7])
```


---

#### 集合

同 python



---

### 模块

`using ModuleName` 使得模块中的所有导出（exported）函数直接可用，不允许重定义或扩展原有函数

`import` 不行（和 Python 一样）

```julia
using JuLIP

read_extxyz()
```

`using` 和 `import` 的区别

```julia
using ModuleName

using ModuleName: x, y
```


---

### 宏

宏：在程序中自动生成代码（表达式）
```julia
# assert (单元测试) 
@assert 

# 查看对特定参数使用的方法/查找函数所在的模块 
@which 

# 运行时间与内存分配统计 
@time 

# 返回执行用时 
@elapsed 

# 查看内存分配 
@allocated 

# 异步任务
@async 

# 显示表达式和表达式的值
@show 
```

宏定义
```julia
macro sayhello()
    return :( println("Hello, World!") )
end

@sayhello

```


---

### 标准库

Base

```julia
Dates  # DateTime, Date

SparseArrays  # sparse, SparseVector, SparseMatrixCSC

Random  # rand, randn, randsubseq

Statistics  # mean, std, cor, median, quantile

LinearAlgebra  # I, eigvals, eigvecs, det, cholesky

Distributed  # @distributed, pmap, addprocs
```

并行计算
```julia
using Distributed
addprocs(4)  # 添加4个进程

@distributed for i in 1:100000
    # 一些并行计算
end

```
