---
title: ATAT 安装与使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: ATAT 安装与使用
description: ATAT 安装与使用
tags:
  - ATAT
categories:
  - 科研工具
date: 2024-03-20 15:00:00
abbrlink: 32015
password:
---

# ATAT 使用

## 介绍

- [ATAT 官网](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/)、[manual pdf](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/manual.pdf)、[ATAT • User Forum](https://brown.edu/Departments/Engineering/Labs/avdw//forum/index.php)（论坛不活跃）
- 最早开发 CE 的工具，现在使用 ATAT 大多是其 mcsqs 模块，用其处理 CE 的不多（ECI 拟合算法默认为最小二乘法，拟合速度较慢，已有文献中的构型计算数最多也是在 3000 以内）
- ATAT 模块
	- mmaps (MIT Multicomponent Ab initio Phase Stability code)；maps 的多主元（multicomponent）版本
	- memc2 (Multicomponent Eazy Monte Carlo Code)；emc2 的多主元版本
	- phb (PHase Boundary code)；没有多主元版本；其他工具可以处理多主元体系
	- cvmclus (Cluster Variation Method CLUSter generator code)
	- genstr：枚举结构
	- mcsqs
	- corrdump


ATAT 和 ICET 枚举得到的结构是一一对应的（相同）

>[How to use SQS for disordered materials](https://cniu.me/2017/08/05/SQS.html)


---

## 安装

- 前提条件：需要有 tcsh/csh shell
- 下载、解压安装包

```bash
# 稳定版本
wget http://alum.mit.edu/www/avdw/atat/atat3_36.tar.gz

# 开发版本 有 mmaps -fa=bayesian
wget http://alum.mit.edu/www/avdw/atat/atat3_48.tar.gz

tar -xzvf atat3_48.tar.gz
mv atat atat-348
```

- 修改 makefile 中的 `BINDIR`，`make mpi` 可以修改 `MPICXX`（`MPICXX=mpiicc` 会报错）

```bash
BINDIR=$(PWD)/bin/

# for MPI: limited implementation at this point
# MPI 实现有限
MPICXX=mpic++ -DATAT_MPI
```

- 编译、安装

```bash
make       # g++ 版本
make mpi   # MPI 版本

make install
```


---

## 使用 mmaps 构建 CE

- 输入文件：lat.in 和 vasp.wrap（类 VASP 的 INCAR 文件中的参数；通常少于 10 行）


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102232637.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102232298.png)

---

- 运行

```bash
mmaps -d &  # 所有参数均使用默认值； & 使其在后台运行
mmaps -l=lat.in -t=1

mmaps -fa=bayesian  # 使用 bayesian 算法
mmaps -l=lat.in -t=1 -fa=bayesian

src/mrefine_skel.c++  # -fa=bayesian 源代码
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102236992.png)


```bash
# 执行 VASP 计算
runstruct_vasp &

# 启动任务管理器检测队列情况
pollmach runstruct_vasp
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102240062.png)

---

- 预期输出文件：

```text
fit.out

predstr.out

gs.out

eci.out

gs_str.out

clusters.out
```


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102255583.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102256918.png)


---


- 分析、绘制

```bash
mmapsrep  # 从 mmaps 得到的 *.out 数据中分析绘制；调用 gnuplot
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102243159.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102244401.png)



---

## 其他

```bash
# 定义 coordinate system 
[a] [b] [c] [alpha] [beta] [gamma]
# 或
[ax] [ay] [az]
[bx] [by] [bz]
[cx] [cy] [cz]
# 定义 lattice vectors 
[ua] [ub] [uc]
[va] [vb] [vc]
[wa] [wb] [wc]
# 定义 atom positions 和 types
# 空位用 Vac 代替
[atom1a] [atom1b] [atom1c] [atom1types]
[atom2a] [atom2b] [atom2c] [atom2types]
```

lat.in 文件格式示例

```bash
# FCC Cu-Au 体系
3.8 3.8 3.8 90 90 90
0   0.5 0.5
0.5 0   0.5
0.5 0.5 0
0 0 0 Cu,Au

# BCC 多主元体系
3.31 3.31 3.31 90 90 90
-0.5 0.5 0.5
0.5 -0.5 0.5
0.5 0.5 -0.5
0 0 0 Ti,Al,Nb,Mo,Zr
```

---

vasp.wrap 文件格式示例

```bash
# vasp.wrap
[INCAR]
PREC = high
ISMEAR = 1
SIGMA = 0.1
NSW=41
IBRION = 2
ISIF = 3
KPPRA = 1000
USEPOT = PAWPBE
DOSTATIC
```

---

str.out 文件格式

```text
n/str.out
Same format as the lattice file, except that
-The coordinate system is always written as 3x3 matrix
-Only one atom is listed for each site.
```

---

已有构型、能量数据，如何只进行拟合：准备好 lat.in + n/str.out + n/energy 三种文件，之后直接运行 maps 或 mmaps

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404102202789.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404112119439.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404112245409.png)


---

一些工具：

- POSCAR 转 lat.in：**vaspkit 414** 选项（1.5.0 版本及以上没有该选项），**atomkit 107** 选项
- str.out 格式转 POSCAR：
	- [GitHub - c-niu/sqs2poscar: A c++ code to convert bestsqs.out from mcsqs (ATAT) to POSCAR for VASP.](https://github.com/c-niu/sqs2poscar)
	- [sqs2poscar - web](https://albertlinda.com/sqs_to_poscar.html)
	- ATAT 自带可执行命令

```bash
str2poscar < str.out > POSCAR
str2cif < str.out > str.cif
```

>[python-atat/findenergy at master · jkitchin/python-atat · GitHub](https://github.com/jkitchin/python-atat/blob/master/findenergy)







结构枚举 Fortran 版本：[GitHub - msg-byu/enumlib: Derivative structure enumeration library](https://github.com/msg-byu/enumlib)

```bash
enum.x input.file
```



```text
Unable to read structure xxx due to geometric incompatibilities with the lattice.
```


maps.out
```text

```




![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404141523194.png)
