---
title: Julia 常用 packages
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Julia 常用 packages
description: Julia 常用 packages
tags:
  - Julia
categories:
  - 编程
  - Julia
date: 2023-12-28 10:00:00
abbrlink: 281223
password:
---

# Julia 常用 packages

### 其他外部库

Datafames

>[GitHub - bkamins/Julia-DataFrames-Tutorial: A tutorial on Julia DataFrames package](https://github.com/bkamins/Julia-DataFrames-Tutorial)

```julia
# 读取 csv 文件
using CSV
using DataFrames

df = CSV.read(filename, DataFrame)

# 拷贝
df2 = copy(df)

select(df, :ColName)
df.ColName
# 选取多列
df[:, [:Col1, :Col2]]



替换数据
replace!(df, pair)

重命名列
rename!(df, :ColName => :NewColName)
```


VSCode 插件：Julia、Julia Formatter

>[GitHub - carstenbauer/JuliaUCL24: Julia for HPC Course @ UCL ARC](https://github.com/carstenbauer/JuliaUCL24)

>[GitHub - mfherbst/julia-for-materials: Material of the seminar "Julia for Materials Modelling"](https://github.com/mfherbst/julia-for-materials)

>[GitHub - Datseris/whyjulia-manifesto: Why Julia - A Manifesto.](https://github.com/Datseris/whyjulia-manifesto)


CLI 生成
>[GitHub - comonicon/Comonicon.jl: Your best CLI generator in JuliaLang](https://github.com/comonicon/Comonicon.jl)


Julia REPL 语法高亮
>[GitHub - KristofferC/OhMyREPL.jl: Syntax highlighting and other enhancements for the Julia REPL](https://github.com/KristofferC/OhMyREPL.jl)

科研绘图
>[GitHub - liuyxpp/MakiePublication.jl: A Julia package for producing publication quality figures based on Makie.jl.](https://github.com/liuyxpp/MakiePublication.jl)


cheatsheet
>[The Fast Track to Julia](https://cheatsheet.juliadocs.org/)

高性能计算
>[GitHub - carstenbauer/JuliaHLRS22: Julia for High Performance Computing Course @ HLRS](https://github.com/carstenbauer/JuliaHLRS22)

>[GitHub - carstenbauer/JuliaHLRS23: Introduction to Julia for High Performance Computing Course @ HLRS](https://github.com/carstenbauer/JuliaHLRS23)

>[GitHub - cpfiffer/julia-bootcamp-2022](https://github.com/cpfiffer/julia-bootcamp-2022)

Doc 生成
>[GitHub - JuliaDocs/Documenter.jl: A documentation generator for Julia.](https://github.com/JuliaDocs/Documenter.jl)


>[GitHub - JuliaMolSim/Libxc.jl: Julia bindings to the libxc library for exchange-correlation functionals](https://github.com/JuliaMolSim/Libxc.jl)


>[GitHub - omlins/julia-gpu-course: GPU Programming with Julia - course at the Swiss National Supercomputing Centre (CSCS), ETH Zurich](https://github.com/omlins/julia-gpu-course)


>[GitHub - adrhill/julia-ml-course: Julia programming for Machine Learning course at TU Berlin](https://github.com/adrhill/julia-ml-course)


>[course\_julia\_day/09\_Useful\_Packages.ipynb at master · mfherbst/course\_julia\_day · GitHub](https://github.com/mfherbst/course_julia_day/blob/master/09_Useful_Packages.ipynb)

元素周期表
>[GitHub - JuliaPhysics/PeriodicTable.jl: Periodic Table for Julians! :fire:](https://github.com/JuliaPhysics/PeriodicTable.jl)

Julia 的 ASE package 没有 Atoms 的 property

DFTK
>[GitHub - JuliaMolSim/DFTK.jl: Density-functional toolkit](https://github.com/JuliaMolSim/DFTK.jl)

DataFrames
>[Introduction · DataFrames.jl](https://dataframes.juliadata.org/stable/)

>[GitHub - bkamins/Julia-DataFrames-Tutorial: A tutorial on Julia DataFrames package](https://github.com/bkamins/Julia-DataFrames-Tutorial)



OhMyREPL：美化 Julia 的 REPL
>[GitHub - KristofferC/OhMyREPL.jl: Syntax highlighting and other enhancements for the Julia REPL](https://github.com/KristofferC/OhMyREPL.jl)


IJulia


绘图相关：
Plots
>[Home · Plots](https://docs.juliaplots.org/stable/)

PyPlot
>[GitHub - JuliaPy/PyPlot.jl: Plotting for Julia based on matplotlib.pyplot](https://github.com/JuliaPy/PyPlot.jl)


Makie
>[GitHub - MakieOrg/Makie.jl: Interactive data visualizations and plotting in Julia](https://github.com/MakieOrg/Makie.jl)
