---
title: Linux 常用程序、库安装
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Linux 常用程序、库安装
description: Linux 常用程序、库安装
tags:
categories:
date: 2024-11-13 10:11:19
abbrlink: 110912
password:
---

# Linux 常用程序、库安装

- 主要在 Ubuntu 和 Arch Linux

- tree

```bash
sudo apt install tree

# 源码编译
# 可能会连接不上
wget https://mama.indstate.edu/users/ice/tree/src/tree-2.1.1.tgz --no-check-certificate

make PREFIX=. install && make clean
```

- g++、gcc

```bash
sudo apt install build-essential

sudo pacman -S gcc
```

- gfortran

```bash
sudo apt install gfortran

sudo pacman -S gcc-fortran
```

- clang

```bash
sudo apt install clang

sudo pacman -S clang

bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
```

- cmake

```bash
sudo apt install cmake
```

- C++ Tools
    - [GitHub - include-what-you-use/include-what-you-use: A tool for use with clang to analyze #includes in C and C++ source files](https://github.com/include-what-you-use/include-what-you-use#how-to-install)
    - [README\_dependencies.md](https://github.com/cpp-best-practices/infiz/blob/main/README_dependencies.md)
    - cppcheck：开源的 C/C++ 代码静态分析工具，用于检测源代码中的潜在错误和代码质量问题
    - conan：开源的 C/C++ 包管理器，用于管理和构建 C/C++ 依赖项、库和二进制包

```bash
sudo apt-get install doxygen
sudo apt-get install graphviz

sudo apt-get install ccache

sudo apt-get install cppcheck

sudo pacman -S cppcheck

sudo pacman -S conan

pip install conan
```

- gsl

```bash
sudo apt install libgsl-dev
# include 路径
/usr/include/gsl
# lib 路径
/usr/lib/x86_64-linux-gnu


sudo pacman -S gsl
# include 路径
/usr/include/gsl
# lib 路径
/usr/lib
```

- voro++

```bash
# Ubuntu 需源码编译
wget https://math.lbl.gov/voro++/download/dir/voro++-0.4.6.tar.gz

tar -xzvf voro++-0.4.6.tar.gz
cd voro++-0.4.6

make && sudo make install

# include 路径
/usr/local/include/voro++
# lib 路径
/usr/local/lib

# 无 root 权限时，需修改 config.mk 中的 PREFIX 参数 ，再编译安装


# Arch Linux
yay -S voro++
# include 路径
/usr/include/voro++
# lib 路径
/usr/lib
```

- Open MPI

```bash
sudo apt install libopenmpi-dev

sudo pacman -S openmpi

# 查看 OpenMPI 的 include 路径
mpicc -showme:compile
```

- boost

```bash
sudo apt install libboost-all-dev
```

- ninja：构建工具

```bash
sudo apt install ninja-build

sudo pacman -S ninja
```

- protobuf：一种轻量级的数据序列化格式

```bash
sudo apt install protobuf-compiler libprotobuf-dev

sudo pacman -S protobuf
```

- tcsh：csh 通常作为 tcsh 的链接或别名；tcsh 是 C Shell 的增强版

```bash
sudo apt install tcsh
```

- 图片查看工具：imagemagick 和 eog

```bash
sudo apt install imagemagick
sudo apt install eog

display figure
identify figure  # 显示图片信息

eog figure
```

- ifconfig

```bash
# 安装 
sudo apt install net-tools

ifconfig      # 查看 IP 地址 Linux/macOS
```

- OpenBLAS（C 代码）

```bash
make
make PREFIX=${HOME}/local/OpenBLAS install

-lopenblas     # 链接 OpenBLAS 库
```

- BLAS（Fortran 代码）

```bash
make

mkdir -p ${HOME}/local/lib/blas
cd ${HOME}/local/lib/blas
ln -s blas_LINUX.a libblas.a

-lblas -lgfortran    # 链接 BLAS 库时同时链接 gfortran（依赖 gfortran）
```

- LAPACK（Fortran 代码）

```bash
cp make.inc.example make.inc
make               # 耗时较长

# 会在当前目录下生成
liblapack.a
librefblas.a       # BLAS 的参考实现
libtmglib.a

# 拷贝编译得到的静态库文件
make -p ${HOME}/local/lib/lapack
cp *.a ${HOME}/lib

-llapack -lrefblas    # 链接 LAPACK 库
```

---

- ScaLAPACK：依赖 BLAS、LAPACK 以及一个 MPI 库

```bash
# make 编译；会报错
cp SLmake.inc.example SLmake.inc

# 修改 SLmake.inc 中的内容
FC
CC
BLASLIB
LAPACKLIB

make

# Master 中的 MPI 默认是 Intel OneAPI MPI Library
# cmake 编译；如下设置不会报错
mkdir -p build && cd build && cmake -DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch" ..
```

- ScaLAPACK 编译报错：
    - [build errors on GCC 10 (gfortran) · Issue #73 · Reference-ScaLAPACK/scalapack · GitHub](https://github.com/Reference-ScaLAPACK/scalapack/issues/73)
    - [Argument mismatches · Issue #92 · Reference-ScaLAPACK/scalapack · GitHub](https://github.com/Reference-ScaLAPACK/scalapack/issues/92)

```bash
# 报错内容
scalapack/SRC/pstrord.f:3264:54:

  490 |      $         CALL IGAMX2D( ICTXT, 'All', TOP, 1, 1, MMAX, 1, -1,
      |                                                      2
......
 3264 |                CALL IGAMX2D( ICTXT, 'All', TOP, 1, 1, INFO, 1, -1,
      |                                                      1
Error: Rank mismatch between actual argument at (1) and actual argument at (2) (rank-1 and scalar)
```

---

- OpenMPI

```bash
# 耗时较长
./configure --prefix=${HOME}/local/OpenMPI

make
make install
```

- MPI 实现常见版本：
    - MPICH
    - Open MPI
    - Intel MPI Library

```bash
# 三个版本都有的 mpi* 可执行程序
mpirun --version
mpiexec
mpif90
mpif77
mpicc
mpicxx

# Intel MPI Library
Intel(R) MPI Library for Linux* OS, Version 2021.6 Build 20220227 (id: 28877f3f32)
Copyright 2003-2022, Intel Corporation.

# Open MPI
mpirun (Open MPI) 5.0.6

Report bugs to https://www.open-mpi.org/community/help/
```

- MPICH

```bash
./configure --prefix=${HOME}/local/MPICH

make  # 耗时很久
make install
```

- FTTW

```bash
./configure --prefix=${HOME}/local/FFTW

# 可添加 --enable-mpi；得到的静态库和头文件会添加 mpi 后缀

make
make install


# Build standalone library of FFTW3 Fortran wrappers to Intel(R) oneMKL
cd /path/intel/oneapi/mkl/20XX/interfaces/fftw3xf
make libintel64
```
