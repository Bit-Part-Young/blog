---
title: 孔老师程序编译与使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 孔老师程序编译与使用
description: 孔老师程序编译与使用
tags:
  - latgen
  - posconv
  - dumpana
categories: 科研工具
date: 2024-11-18 17:35:11
abbrlink: 173511
password:
---

# 孔老师程序编译与使用

## posconv、NumNei

- posconv：构型文件格式转换。支持格式：
    - POSCAR
    - xyz
    - LAMMPS atomic/dump（dump 格式原子坐标为分数坐标，即为 xs, ys, zs）
    - Material Studio
    - ...

- NumNei：计算 BCC、FCC 和金刚石结构的第 N 近邻原子距离

- 编译：编译器可选择 gfortran 或 ifort（gfortran 已足够；ifort 性能可能更好些）

- posconv 功能一览

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404291005269.png)



---

## latgen

- 结构建模程序，包括
    - BCC、FCC/Diamond、HCP/Graphene 常见晶体结构、A3B、A2B、AB 及 ABXn 型结构
    - BCC、FCC、HCP 晶体结构以 \[001\]、\[110\]、\[111\] 方向作为 z 轴的取向结构
    - BCC、FCC、HCP 间隙点缺陷（四面体、八面体间隙）
    - 置换固溶体
    - 表面、界面模型（Multi-layer）

- latgen 功能一览

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404291006009.png)

---

- 编译：依赖 voro++；编译器可选择 gcc 或 icc

- voro++ 编译

```bash
wget https://math.lbl.gov/voro++/download/dir/voro++-0.4.6.tar.gz

tar -xzvf voro++-0.4.6.tar.gz

cd voro++-0.4.6.tar.gz

# 修改 config.mk 的 PREFIX 选项
PREFIX=${HOME}/local/voro

make && make install
```

- 修改 latgen 中的 Makefile 文件内容（`INC`：voro++ 头文件路径； `LIB`：库路径）

```bash
VoroINC = -I${HOME}/local/voro/include/voro++
VoroLIB = -L${HOME}/local/voro/lib -lvoro++
```

---

- 使用

```bash
latgen -poscar    # 使生成的构型文件格式含 POSCAR
```



---

## dumpana

- LAMMPS dump 文件后处理程序。可计算：
    - CSRO
    - RDF
    - PDF
    - g(r) （径向分布函数）
    - 扩散系数
    - 键长键角
    - 混合构型熵
    - 局域序参数
    - ...

- dumpana、latgen、posconv 和 vaspkit 等程序都可以通过 `latgen < inp.script` 命令，使其不用每次交互输入参数，节约时间（**重要！！！**）

- dumpana 功能一览

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404291006937.png)

---

- 编译：编译依赖 voro++ 和 gsl（C 数值计算库）；编译器可选择 gcc 或 icc

- gsl 编译

```bash
wget https://mirror.ibcp.fr/pub/gnu/gsl/gsl-latest.tar.gz

./configure --prefix=${HOME}/local/gsl

make && make install

# 将 gsl 的 lib 路径添加到 LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/local/gsl/lib:${LD_LIBRARY_PATH}
```

- Master 平台编译

```bash
# 修改 Makefile 文件内容（voro++、gsl 的 INC 和 LIB 路径）

VoroINC = -I${HOME}/local/voro/include/voro++
VoroLIB = -L${HOME}/local/voro/lib -lvoro++

GslINC  = -I${HOME}/local/gsl/include
GslLIB  = -L${HOME}/local/gsl/lib -lgsl -lgslcblas

# Master 上有 voro++、gsl；可不用修改
VoroINC = -I/opt/libs/voro/include/voro++
VoroLIB = -L/opt/libs/voro/lib -lvoro++

GslINC  = -I/opt/libs/gsl/include
GslLIB  = -L/opt/libs/gsl/lib -lgsl -lgslcblas
```

- SiYuan 超算平台编译

```bash
git clone https://github.com/lingtikong/dumpana.git

module purge
module load gsl/2.7.1-intel-2021.4.0
module load intel-oneapi-compilers/2021.4.0

# 编译器选择 icc
# 修改 Makefile 文件的 voro++ 内容，gsl 可不用修改

make


# 若使用时报错，设置 gsl 相关的动态链接库文件的符号链接
ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/gsl-2.7.1-363bjoc7gmwz4mpn2csc7paszwv5h2wk/lib/libgsl.so.27 ~/lib/
ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/gsl-2.7.1-363bjoc7gmwz4mpn2csc7paszwv5h2wk/lib/libgslcblas.so.0 ~/lib/
```



---

## 其他

viscal：计算粘度程序（孔老师编写的 manager 上）

粘度计算：Green-Kubo 公式

ARTn：过渡态搜索；可只指定起点，不指定终点（activation relaxation technique, ART）

- 孔老师 LAMMPS Phonon package：[Phonon package安装与使用 - Eastsheng's Wiki](https://eastsheng.github.io/MyWiki/wiki/2023/04/22/softwares/lammps/phonon_package/)
