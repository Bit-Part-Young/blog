---
title: VASP 编译
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: VASP 编译
description: VASP 编译
tags:
  - VASP
categories:
  - 科研工具
date: 2024-06-20 09:00:00
abbrlink: 206045
password:
---

# VASP 编译

## 介绍

- VASP 中的可执行命令无 `-h` 等帮助选项

- VASP 编辑得到的三个版本：

```bash
vasp_std             # 标准版本
vasp_ncl             # 考虑磁结构，如 SOC；非共线版
vasp_gam             # Gamma only 版本
```

- 编译条件
    - Fortran、C、C++ 编译器
    - 数值计算库：FFTW、BLAS、LAPACK、ScaLAPACK
    - MPI

- 官方安装教程：
    - [Installing VASP.5.X.X - VASP Wiki](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X)
    - [Installing VASP.6.X.X - VASP Wiki](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X)

- 安装参考资料：
    - [【计算材料学-从算法原理到代码实现】视频教程 - 4.1\_VASP安装教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1W24y1N7WK)
    - [【计算材料学-从算法原理到代码实现】视频教程 - 4.1\_VASP的Intel\_OneAPI安装教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1tN411D7Hn/?spm_id_from=333.999.0.0)
    - [intel oneAPI以及vasp5.4.4安装](http://bbs.keinsci.com/thread-28200-1-1.html)
    - [Ubuntu18.04编译VASP5.4.4的详细步骤 - 哔哩哔哩](https://www.bilibili.com/read/cv3794759)
    - [VASP 5.4.4极简安装方法（CentOS 7.6+ifort 19）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/av39616222/)
    - [VASP最简单的安装方法（含全程视频演示） - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/455)
    - VASP6 编译（含 GPU 版本）：[编译版本6的VASP](https://blog.sbyu.top/post/5)

在 `makefile.include` 中的 OFLAG 参数里加入 -xhost，这样编译器会使得编译出的程序能够利用当前机子 CPU 能支持的最高档次的指令集以加速计算

[VASP.6.4.3中新功能：固定轴优化](https://mp.weixin.qq.com/s/cZLf_B4LrvAClRNCmKRh6w)



---

## VASP 编译

### Intel oneAPI

- VASP.5.4.4 和 6.3.0 版本编译用到的编译器是 icc、icpc、mpiifort

- makefile.include 不同版本的含义：[makefile.include - VASP Wiki](https://www.vasp.at/wiki/index.php/Makefile.include)

- makefile.include.linux\_intel 内容：[makefile.include.linux\_intel - VASP Wiki](https://www.vasp.at/wiki/index.php/Makefile.include.linux_intel)

- VASP.6.3.0 中的 四种 intel makefile
    - makefile.include.intel: Parallelized using MPI, combined with MKL.
    - makefile.include.intel_omp: Parallelized using MPI + OpenMP, combined with MKL.
    - makefile.include.intel_ompi_mkl_omp: Parallelized using OpenMPI + OpenMP, combined with MKL.
    - makefile.include.intel_serial: Not parallelized, strongly reduced feature-set, i.e., not suitable for production.

- Master 上编译 intel_omp 版本，运行 `mpirun -n 2 vasp_std` 命令会报错；编译 Intel 版本正常

```bash
# 超算平台编译步骤
# 导入 oneAPI 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

# 删除 bulid 和 bin 目录中的内容
make veryclean
rm bin/*

# VASP.5.4.4
cp arch/makefile.include.linux_intel makefile.include
# VASP.6.3.0
cp arch/makefile.include.intel makefile.include

# 编译；耗时 20-30 分钟
make  # 或 make all, make std
```

- VASP.5.4.4 编译最后可能会出现的 remark（无影响）：

```bash
ifort: command line remark #10412: option '-mkl=sequential' is deprecated and will be removed in a future release. Please use the replacement option '-qmkl=sequential'
```


---

### GNU

- Linux

```bash
# lib 路径
/usr/lib/x86_64-linux-gnu

# OpenMPI
sudo apt install libopenmpi-dev

# 数值计算库
sudo apt install libfftw3-dev
sudo apt install libblas-dev    # 或者 libopenblas-dev （优化版 BLAS）
sudo apt install liblapack-dev
sudo apt install libscalapack-openmpi-dev  # 或 libscalapack-mpi-dev

# VASP.5.4.4
cp arch/makefile.include.linux_gnu makefile.include
# VASP.6.3.0
cp arch/makefile.include.gnu_omp makefile.include

# 修改 数值计算库 lib 在 makefile.include 中的具体路径

make  # 或 make all, make std
```

- Mac M1：Mac M1 gnu omp 编译 VASP6 + HDF5（耗时 32 min 左右）：[VASP M1 Mac Compilation Guide · GitHub](https://gist.github.com/janosh/a484f3842b600b60cd575440e99455c0)


---

### HDF5

安装步骤：

```bash
wget https://hdf-wordpress-1.s3.amazonaws.com/wp-content/uploads/manual/HDF5/HDF5_1_14_3/src/hdf5-1.14.3.tar.gz

# 配置 intel 版本
./configure --enable-parallel --enable-fortran --enable-cxx --enable-unsupported \
            CC=mpiicc FC=mpiifort CXX=mpiicpc \
            --prefix=${HOME}/local/hdf5

make
make install
```

未添加 `--enable-parallel` 参数会出现以下报错：

```bash
configure: error: --enable-cxx and --enable-parallel flags are incompatible. Use --enable-unsupported to override this error.
```

```bash
# 显示 HDF5 的编译和配置详细信息
h5cc -showconfig  # 或 h5c++ h5pcc

# 显示用于编译 HDF5 的编译器命令行，包括链接的库和编译器标志
h5cc -show
```

---

使用

- HDF5 Preview 插件：只能打开.hdf5 格式，无法打开.h5 格式
- Pandas 的 read_hdf() 不太好用

```bash
h5ls data.h5     # 显示 Group 列表

# vaspout.h5 示例
input                    Group
intermediate             Group
original                 Group
results                  Group
version                  Group

h5dump data.h5   # 输出文件的详细结构和内容
```


---

### VASP.6.3.0 + HDF5

>[编译支持HDF5的VASP - 哔哩哔哩](https://www.bilibili.com/read/cv15039734/)

```bash
# 超算平台编译步骤
# 导入 oneapi 套件；hdf5
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load hdf5/1.12.2-intel-2021.4.0

# 查看 hdf5/1.12.2-intel-2021.4.0 的安装路径
module show hdf5/1.12.2-intel-2021.4.0

cp arch/makefile.include.intel makefile.include
# 删除 MKLROOT    ?= 后的内容 此步可忽略
# 取消 HDF5 相关行注释，将 HDF5_ROOT  ?= 后的内容替换为 hdf5 的安装路径

make  # 或 make all, make std
```

可能会出现以下报错：

```bash
error while loading shared libraries: libhdf5_fortran.so.102: cannot open shared object file: No such file or directory
```

原因：缺少 `libhdf5_fortran.so.102` 动态链接库，其实 module load 的 `hdf5/1.12.2-intel-2021.4.0` 有该动态链接库，不过版本更新一些，为 `libhdf5_fortran.so.200`

解决方法：将 `libhdf5_fortran.so.200` 软链接为 `libhdf5_fortran.so.102`；将 `~/lib` 写入到 `LD_LIBRARY_PATH`

```bash
ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/hdf5-1.12.2-nxwmp3tddhreojgbib25ldc7wusvzf3m/lib/libhdf5_fortran.so.200 ~/lib/libhdf5_fortran.so.102

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$HOME/lib
```


---

## VASP + VTST 编译

VASP + VTST：在 VASP 添加过渡态计算功能

参考：

- [Installation — Transition State Tools for VASP](http://theory.cm.utexas.edu/vtsttools/installation.html)
- [VASP 5.4.1+VTST编译安装](http://hmli.ustc.edu.cn/doc/app/vasp.5.4.1-vtst.htm)

---

安装步骤：

- 下载 VTST Code 和 VTST Scripts：[Download — Transition State Tools for VASP](https://theory.cm.utexas.edu/vtsttools/download.html)

- 修改 `src/main.F` 源码：

```bash
# 替换前 第 3519 行附近
CALL CHAIN_FORCE(T_INFO%NIONS,DYN%POSION,TOTEN,TIFOR, &
     LATT_CUR%A,LATT_CUR%B,IO%IU6)

# 替换后；添加了 TSIF,
CALL CHAIN_FORCE(T_INFO%NIONS,DYN%POSION,TOTEN,TIFOR, &
     TSIF,LATT_CUR%A,LATT_CUR%B,IO%IU6)

# vasp.6.2 及以后，还需进行以下替换
# 替换前
IF (LCHAIN) CALL chain_init( T_INFO, IO)
# 替换后 第 925 行附近
CALL chain_init( T_INFO, IO)
```

- 备份 `src/chain.F`；复制 vtstcode-XXX 中对应 VASP 版本（如 vtstcode5、vtstcode6.3；vtstcode6.3 中多了 `ml_pyamff.F` 文件和 `pyamff_fortran/` 目录）的目录下的所有文件到 `src/`：

```bash
cp src/chain.F src/chain.F-org

cp vtstcode-XXX/vtstcodeXXX/* src/
```

- 修改 `src/.objects` 源码，在 `chain.o` 所在行前添加：

```bash
# vtstcode5 和 vtstcode6.1
bfgs.o dynmat.o instanton.o lbfgs.o sd.o cg.o dimer.o bbm.o \
fire.o lanczos.o neb.o qm.o opt.o \

# vtstcode6.3
bfgs.o dynmat.o instanton.o lbfgs.o sd.o cg.o dimer.o bbm.o \
fire.o lanczos.o neb.o qm.o \
pyamff_fortran/*.o ml_pyamff.o \
opt.o\
```

- 使用 vtstcode6.3，还需修改 `src/makefile` 源码：

```bash
# 替换前
LIB= lib parser
dependencies: sources

# 替换后
LIB= lib parser pyamff_fortran
dependencies: sources libs
```

- 编译：同 VASP 编译步骤

---

VASP.6.3.0 + VTST 出现报错：VTST 源码代码有问题

>[VASP6.3.2 + vtstcode6.3编译出错 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-46112-1-1.html)

>[过渡态神器VTST为什么在VASP6.3编译不成功？因为源代码有问题！](https://mp.weixin.qq.com/s/ah33JQ7uTxcm_DakY2yJXA)

解决方法：在 chain.F 第 202 行后添加 `ENDIF`

```bash
mpiifort -free -names lowercase -assume byterecl -w -xHOST -O2 -I/opt/software/intel/oneapi/mkl/2022.1.0/include/fftw  -c chain.f90
chain.F(179): error #6321: An unterminated block exists.
      IF (LINTERACT) THEN
^
compilation aborted for chain.f90 (code 1)
make[2]: *** [makefile:168: chain.o] Error 1
make[2]: Leaving directory 'XXX/vtst-vasp630/build/std'
cp: cannot stat 'vasp': No such file or directory
make[1]: *** [makefile:130: all] Error 1
make[1]: Leaving directory 'XXX/vtst-vasp630/build/std'
make: *** [makefile:17: std] Error 2
```


---

## 相关问题

- VASP 运行出现 `forrtl` 报错：[forrtl: severe (174): SIGSEGV, segmentation fault occurred - My Community](https://www.vasp.at/forum/viewtopic.php?t=17257)

```bash
# 在提交脚本或终端中添加命令
ulimit -s unlimited
```

---

AMD CPU 与 Intel CPU 编译 VASP 的区别
[VASP编译偶遇“Function return parameter requires SSE register while SSE is disabled”](https://zhuanlan.zhihu.com/p/601580449)

`-xHOST` 是一个编译器标志，通常用于告诉编译器针对运行当前编译过程的机器的最高可用指令集进行优化。这个标志是 Intel 编译器中的一部分，用于生成可以利用当前处理器所有高级特性的代码

SCALAPACK：高扩展的 LAPACK，主要用于分布式内存体系结构

[OneAPI问题：缺少libmkl_intel\_\*\_.so.\*文件的解决](https://zhuanlan.zhihu.com/p/589633827)

[【VASP报错集锦 1】](https://zhuanlan.zhihu.com/p/536705200)

---

自己安装的 Ubuntu 测试，Intel oneAPI 2023 版编译 VASP 6.3.0 报错

```bash
minimax_functions1D.F(46): catastrophic error: Function return parameter requires SSE register while SSE is disabled.
compilation aborted for minimax_functions1D.f90 (code 1)
```

---

- [1.仅优化二维VASP编译.md](https://github.com/lhycms/QM/blob/main/DFT/VASP/%E7%BC%96%E8%AF%91/1.%E4%BB%85%E4%BC%98%E5%8C%96%E4%BA%8C%E7%BB%B4VASP%E7%BC%96%E8%AF%91.md)
