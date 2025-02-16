---
title: Intel oneAPI 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Intel oneAPI 使用
description: Intel oneAPI 使用
tags:
  - Intel-oneAPI
categories:
  - 科研工具
date: 2024-11-13 09:17:24
abbrlink: 172409
password:
---

# Intel oneAPI 使用

- Intel oneAPI 包括对 OpenMP 的支持

- 参考：[安装 Intel® oneAPI Base Toolkit 和 Intel® oneAPI HPC](https://blog.csdn.net/weixin_42487488/article/details/115066980)

- Intel oneAPI 暂不支持 Arch Linux

- Intel-oneAPI 中的 MKL (Math Kernel Library) 提供数学库： FFTW、BLAS、LAPACK、ScaLAPACK、Vector Math Library (VML)、Data Fitting Library、Sparse BLAS 等

```bash
${MKLROOT}/include         # MKL 头文件路径
${MKLROOT}/lib/intel64     # MKL 库文件路径

-lmkl_intel_lp64           # LP64 模型
-lmkl_sequential           # 单线程库
-lmkl_core                 # 核心库

${MKLROOT}/include/fftw    # FFTW
${MKLROOT}/lib/intel64     # BLACS、LAPACK 和 ScaLAPACK
```

- Intel oneAPI 在官网只能下载最新版本；旧版下载：[Intel](https://get.hpc.dev/vault/intel/?sort=name&order=desc)

- Intel-oneAPI/2023.2 是这一系列套件中最后一个支持经典 C/C++/Fortran 编译器的版本（Intel-oneAPI 2024 开始没有了 icc 和 icpc）

- Intel® oneAPI Base Toolkit 2024 版包含的东西（可不用全部安装）

```text
Intel® oneAPI Collective Communications Library
Intel® oneAPI Data Analytics Library
Intel® oneAPI Deep Neural Network Library
Intel® oneAPI DPC++/C++ Compiler (separate download required)
Intel® oneAPI DPC++ Library
Intel® oneAPI Math Kernel Library
Intel® oneAPI Threading Building Blocks
Intel® Advisor
Intel® Distribution for GDB*
Intel® Distribution for Python* (separate download required)
Intel® DPC++ Compatibility Tool
Intel® Integrated Performance Primitives
Intel® VTune™ Profiler
Optional: Intel® FPGA Add-on for oneAPI Base Toolkit
```

- Intel® oneAPI HPC Toolkit 2024 版包含的东西（可不用全部安装；缺少 C++ Compiler Classic）

```text
Intel® oneAPI DPC++/C++ Compiler (separate download required)
Intel® Fortran Compiler & Intel® Fortran Compiler Classic (separate download required)
Intel® Inspector
Intel® MPI Library
Intel® Trace Analyzer and Collector
```

- 安装：先 Base，后 HPC

```bash
# 下载 Offline 安装版本

# 默认安装到 /opt/intel；无 sudo，则默认安装到 ~/intel
sudo sh ./l_BaseKit_p_XXX_offline.sh
sudo sh ./l_HPCKit_p_XXX_offline.sh

# 激活 Intel oneAPI 环境
source /opt/intel/oneapi/setvars.sh intel64
```

- 检查

```bash
icc -v
icpc -v
ifort -v
mpiicc -v
mpiifort -v

icx -v
icpx -v

# icc mpiicc mpicc 三者区别
icc             # Intel C Compiler；Intel 提供的高性能 C 编译器
mpiicc          # MPI Intel C Compiler；基于 icc 的 MPI 版本，特殊的编译器包装器，用于编译使用 MPI 的并行程序；Intel MPI + icc
mpicc           # 广泛用于编译 MPI 程序的通用 C 编译器包装器；Intel MPI + gcc


# Intel Classic 编译器
# /path/oneapi/compiler/2022.1.0/linux/bin/intel64
icc
icpc
ifort

# Intel oneAPI 编译器
# /path/oneapi/compiler/2022.1.0/linux/bin
icx
icpx
ifx

# Intel MPI
# /path/oneapi/mpi/2021.6.0/bin
mpiicc
mpiicpc
mpiifort

# GNU 编译器
gcc
g++
gfortran

# NVHPC 编译器
nvc
nvc++
nvfortran
```

- Intel Classic C++ Compiler 是 Intel 长期提供的传统编译器，也被称为 ICC。它主要是为了优化 Intel 硬件（如 x86 CPU 系列）而设计，并且支持 C++ 和 OpenMP 的多版本

- Intel LLVM C++ Compiler 是基于 LLVM 的编译器，这是 Intel 在 oneAPI 框架下推出的新型编译器，也被称为 DPC++/C++ Compiler。这个编译器旨在提供一个统一的编程模型，支持多种硬件平台，包括 CPU、GPU 和 FPGA

- Intel oneAPI 卸载：[Uninstall oneAPI Toolkits and Components](https://www.intel.com/content/www/us/en/docs/oneapi/installation-guide-linux/2023-1/uninstall-oneapi-toolkits-and-components.html)

```bash
cd /opt/intel/oneapi/installer
sudo ./installer
```
