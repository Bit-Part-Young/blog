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
  - VASP
date: 2024-06-20 09:00:00
abbrlink: 206045
password:
---

# VASP 编译

## 介绍

- VASP 中的可执行命令无 `-h` 等帮助选项

- 官方安装教程：
    - [Installing VASP.5.X.X - VASP Wiki](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X)
    - [Installing VASP.6.X.X - VASP Wiki](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X)

- 安装参考资料：
    - [【计算材料学-从算法原理到代码实现】视频教程 - 4.1\_VASP安装教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1W24y1N7WK)
    - [【计算材料学-从算法原理到代码实现】视频教程 - 4.1\_VASP的Intel\_OneAPI安装教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1tN411D7Hn/?spm_id_from=333.999.0.0)
    - [intel oneAPI以及vasp5.4.4安装](http://bbs.keinsci.com/thread-28200-1-1.html)
    - [Ubuntu18.04编译VASP5.4.4的详细步骤 - 哔哩哔哩](https://www.bilibili.com/read/cv3794759)
    - [VASP最简单的安装方法（含全程视频演示） - 思想家公社的门口：量子化学·分子模拟·二次元](http://sobereva.com/455)
    - VASP6 编译（含 GPU 版本）：[编译版本6的VASP](https://blog.sbyu.top/post/5)
    - [VASP6.5.0+Intel CPU编译并添加module环境 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/forum.php?mod=viewthread&tid=50668&extra=page%3D1%26filter%3Dauthor%26orderby%3Ddateline)
    - [VASP - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/app/engineeringscience/vasp.html)
    - [Instaling VASP - CodiMD](https://notes.sjtu.edu.cn/s/daoG4JIYX#)

- 含 VASP 版本更新内容简要介绍：
    - VASP 6.5.0（新特性：电声耦合）和 6.4.3: [Changelog - VASP Wiki](https://www.vasp.at/wiki/index.php/Changelog)
    - [VASP - NSC](https://www.nsc.liu.se/software/installed/tetralith/vasp/)

- [1.仅优化二维VASP编译.md](https://github.com/lhycms/QM/blob/main/DFT/VASP/%E7%BC%96%E8%AF%91/1.%E4%BB%85%E4%BC%98%E5%8C%96%E4%BA%8C%E7%BB%B4VASP%E7%BC%96%E8%AF%91.md)

- [VASP固定基矢优化结构 - Misaraty](https://www.misaraty.com/2021-01-11_vasp%E5%9B%BA%E5%AE%9A%E5%9F%BA%E7%9F%A2%E4%BC%98%E5%8C%96%E7%BB%93%E6%9E%84/)：对于二维材料，固定 z 方向晶胞参数不变（固定 z 轴），优化 x、y 晶胞参数



---

## VASP 编译

### 编译前须知

- 编译条件
    - 编译器：Fortran、C、C++
    - 数值计算库：FFTW、BLAS、LAPACK、ScaLAPACK（高扩展的 LAPACK，主要用于分布式内存体系结构）
    - MPI 实现：Intel MPI 或 Open MPI

- 课题组服务器 VASP 安装包路径：Master: `/opt/software`；将其拷贝到自己的用户目录下，传输至超算平台

- `make -jN` 并行编译的特性只有 VASP.6.X.X 才支持，VASP.5.X.X 不支持

- 编译选项：[Compiler options - VASP Wiki](https://www.vasp.at/wiki/index.php/Compiler_options)

- 预编译选项：[Precompiler options - VASP Wiki](https://www.vasp.at/wiki/index.php/Precompiler_options)

- [Linking to libraries - VASP Wiki](https://www.vasp.at/wiki/index.php/Linking_to_libraries)

- [OpenACC GPU port of VASP - VASP Wiki](https://www.vasp.at/wiki/index.php/OpenACC_GPU_port_of_VASP)

- makefile.include 不同架构的含义：[makefile.include - VASP Wiki](https://www.vasp.at/wiki/index.php/Makefile.include)

- make.include 文件选择
    - VASP.5.4.4 只支持 Intel Classic 编译器
    - VASP.6.X.X 支持 Intel Classic 和 Intel oneAPI 编译器

```bash
# Intel Composer suite and oneAPI Base + HPC toolkits for CPUs
makefile.include.linux_intel             # VASP.5.4.4
makefile.include.intel                   # VASP.6.3.X 或 VASP.6.4.X
makefile.include.oneapi                  # VASP.6.4.X

# GNU compilers for CPUs
makefile.include.linux_gnu               # VASP.5.4.4
makefile.include.gnu                     # VASP.6.X.X

# NVIDIA HPC-SDK for CPU and GPU
makefile.include.nvhpc_ompi_mkl_omp_acc  # VASP.6.X.X GPU
```

- 自定义功能：[Customize - makefile.include - VASP Wiki](https://www.vasp.at/wiki/index.php/Makefile.include#Customize)
    - HDF5
    - Wannier90
    - Libxc
    - ...

- VASP.5.4.4 源代码目录结构

```bash
vasp.X.X.X (root directory)
                            |
         ---------------------------------------
        |              |          |             |
       arch           bin       build          src
                                                |
                                         ---------------
                                        |       |       |
                                       lib    parser   CUDA


arch           # 针对不同架构的 Makefile 模板
bin            # 编译后的可执行程序文件目录
build          # 编译时自动复制 src 目录内源码后执行编译，会分别创建三个版本的子目录
src            # 源码目录
lib            # 库目录，对应以前的 vasp.lib 目录
CUDA           # GPU CUDA 代码目录 
```

- VASP.6.X.X 源代码目录结构

```text
                  vasp.x.x.x (root directory)
                               |
         ------------------------------------------------
        |        |        |         |          |         |
       arch     bin     build      src     testsuite   tools
                                    |
                              -------------
                             |      |      |
                            lib   parser  fftlib
```

- 三种版本可分开进行编译：`make std`，`make gam`，`make ncl`

- `bin` 目录若出现 `vasp_std`, `vasp_gam`, `vasp_ncl` 可执行文件，则表示编译成功

- 编译得到的三个版本

```bash
vasp_std             # standard 标准版本
vasp_ncl             # non-collinear 非共线版本；考虑磁性，如 SOC
vasp_gam             # gamma-only 版本
```

- [VASP.6.4.3中新功能：固定轴优化](https://mp.weixin.qq.com/s/cZLf_B4LrvAClRNCmKRh6w)

- 在 `makefile.include` 中的 OFLAG 参数里加入 `-xhost`，会使得编译出的程序能够利用当前机器 CPU 能支持的最高可用的指令集以加速计算


---

### CPU 版本 + Intel oneAPI 套件

- 安装步骤

```bash
# 超算平台编译步骤；Master 可忽略此步骤
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
# AMD CPU 需将 FFLAGS 中的 -xHOST 参数去掉

# 编译；耗时 20-30 分钟
make                # 或 make all
# 单独版本编译
make std            # 或 make gam, make ncl

# 为 vasp_* 等设置符号链接


# 可修改内容
# 添加 -diag-disable=10441 不让 icc 和 icpc 编译器在编译代码时每调用一次就跳出弃用警告
# 修改前
CC_LIB      = icc
CXX_PARS    = icpc
# 修改后
CC_LIB      = icc -diag-disable=10441
CXX_PARS    = icpc -diag-disable=10441
```

- VASP.5.4.4 编译最后可能会出现的 remark（无影响）

```bash
ifort: command line remark #10412: option '-mkl=sequential' is deprecated and will be removed in a future release. Please use the replacement option '-qmkl=sequential'
```

- 对于 2024 及更新的的 Intel oneAPI，不再包含 C++ Compiler Classic（即无 icc、icpc），需对 `makefile.include` 文件内容进行修改

```bash
# 修改前
CC_LIB      = icc
CXX_PARS    = icpc

# 修改后
CC_LIB      = icx
CXX_PARS    = icpx
```

- AMD CPU 使用 Intel oneAPI 套件编译出现的报错：[VASP编译偶遇“Function return parameter requires SSE register while SSE is disabled”](https://zhuanlan.zhihu.com/p/601580449)

```bash
# AMD CPU 直接使用 makefile.include.intel
catastrophic error: Function return parameter requires SSE register while SSE is disabled.
compilation aborted for minimax_functions1D.f90 (code 1)
```

- Master 上选择 intel_omp 编译，运行 `mpirun -n 2 vasp_std` 命令会报错；选择 Intel 编译正常


---

### CPU 版本 + GNU 套件

- Mac M1：[VASP M1 Mac Compilation Guide · GitHub](https://gist.github.com/janosh/a484f3842b600b60cd575440e99455c0)
    - gnu_omp 架构编译 VASP6 + HDF5（耗时 32 min 左右）

- Linux

```bash
# lib 路径
/usr/lib/x86_64-linux-gnu

# Open MPI
sudo apt install libopenmpi-dev

# 数值计算库
sudo apt install libfftw3-dev
sudo apt install libblas-dev    # 或 libopenblas-dev （优化版 BLAS）
sudo apt install liblapack-dev
sudo apt install libscalapack-openmpi-dev  # 或 libscalapack-mpi-dev

# VASP.5.4.4
cp arch/makefile.include.linux_gnu makefile.include
# VASP.6.3.0
cp arch/makefile.include.gnu makefile.include

# 修改数值计算库 lib 在 makefile.include 中的具体路径

make  # 或 make all, make std
```


---

### NVIDIA GPU 版本

- 参考
    - [Ubuntu安装GPU版VASP6.4.3（含NVIDIA显卡驱动安装更新）](https://blog.csdn.net/liouver/article/details/140653183)
    - [vasp安装步骤 - 哔哩哔哩](https://www.bilibili.com/opus/910950614915088404)

- 不建议编译 VASP 5.4.4 的 GPU 版本，建议编译 VASP 6.X.X 的 GPU 版本

- VASP GPU 版本不支持 `-j` 并行编译？

- VASP GPU 版本在小体系下，计算速度与 CPU 版本差不多；大体系下会有加速效果 (400 个原子以上？)

- VASP GPU 版本占用显存较多，可达 GPU 的显存容量

- NVIDIA HPC-SDK 相关环境变量

```bash
export NVIDIA_HPC_SDK_ROOT=/opt/nvidia/hpc_sdk/Linux_x86_64/XX.X
export PATH=${NVIDIA_HPC_SDK_ROOT}/compilers/bin:$PATH
export PATH=${NVIDIA_HPC_SDK_ROOT}/comm_libs/mpi/bin:$PATH
export LD_LIBRARY_PATH=${NVIDIA_HPC_SDK_ROOT}/comm_libs/mpi/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=${NVIDIA_HPC_SDK_ROOT}/compilers/extras/qd/lib:$LD_LIBRARY_PATH

# 可选
# 单独激活 Intel oneAPI MKL
source /opt/intel/oneapi/mkl/XXXX.X.X/env/vars.sh intel64 --force
export MANPATH=${NVIDIA_HPC_SDK_ROOT}/compilers/man:$MANPATH
```

- 修改 makefile.include 文件内容
    - 修改 `CC`、`FC`、`FCL` 中的 ccXX（计算能力与显卡型号匹配） 和 CUDA 版本（安装的 CUDA toolkit 版本）
    - Intel oneAPI MKL 有 SCALAPACK，可将 SCALAPACK_ROOT 所在的 2 行注释掉

- 安装步骤

```bash
# 设置 NVIDIA HPC-SDK 相关环境变量（使用 GPU 版本进行计算时也需要设置）

# 将 bin 目录中的 vasp_* 重命名为对应的 vasp_*_cpu

mkdir build-gpu

# 若已编译 CPU 版本，重命名
cp makefile.include makefile.include.cpu

cp arch/makefile.include.nvhpc_ompi_mkl_omp_acc makefile.include.gpu

# 设置符号链接
ln -s makefile.include.gpu makefile.include

# 修改 makefile.include 文件内容

# 编译 3 个版本
make PREFIX=./build-gpu
# std 版本单独编译
make PREFIX=./build-gpu std

# 将 bin 目录中的 vasp_* 重命名为对应的 vasp_*_gpu
```

- VASP GPU 版本性能
    - [A100还是4090? VASP的GPU性能测试及调优策略 - 硬件配置与采购 - 计算化学公社](http://bbs.keinsci.com/thread-45195-1-1.html)
    - [VASP 用 GPU 加速后似乎没有 CPU 并行快 - 高性能计算、集群、并行技术 - 计算化学公社 - 第2页](http://bbs.keinsci.com/thread-21177-2-1.html)
    - [求助VASP是否编译GPU版本问题 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-35206-1-1.html)

- VASP GPU 版本速度测试（粗略）

```bash
# BCC Nb 4x4x4 128 个原子，KSPACING=0.15，静态计算
node2 60 CPU 核 耗时 42min
1 块 4090 耗时 46min
1 块 3090 耗时 1h 39min
2 块 3090 耗时 1h 10min

# BCC Nb 6x6x6 432 个原子，单个 Γ 点，静态计算（加速效果明显）
1 块 4090 耗时 1h 2min

# BCC 原胞 Nb 6x6x6 216 个原子，KSPACING=0.15，静态计算；报显存不足的错

# FCC Al 3x3x3 108 个原子，KSPACING=0.15，静态计算
1 块 3090 耗时 7min
```

- **目前 openacc 版本的 VASP 用了 nccl，只能用一个 CPU 核带一块 GPU，因而 CPU 单核性能会对计算结果有影响**

- 游戏显卡，跑经典 MD 非常有优势，跑第一性原理无明显优势？

```bash
# 只有 1 块 GPU，使用多个 CPU 核会报错
WARNING: INIT_ACC: several MPI-ranks need to share a GPU, which is not
    supported by NCCL. The use of NCCL will be switched off. To avoid this,
    reduce the number of MPI-ranks: #-of-ranks <= #-of-GPUs (on every node!).
    
The function MPI_FINALIZE was invoked multiple times in a single
process on host node2, PID 3122551.

This indicates an erroneous MPI program; MPI_FINALIZE is only allowed
to be invoked exactly once in a process.

MPI_ABORT was invoked on rank 11 in communicator MPI_COMM_WORLD
with errorcode 1.

NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
You may or may not see output from other processes, depending on
exactly when Open MPI kills them.
```


---

### AMD GPU 版本

- **相对复杂，不建议尝试**

- 使用 AOCC + AOCL 安装（安装相对复杂）
    - [各种版本VASP的编译-AMD yes（并不）篇](https://zhuanlan.zhihu.com/p/293300472)
    - [AMD全家桶（AOCC+AOCL）编译vasp.5.4.4](https://zhuanlan.zhihu.com/p/557466113)
    - [AOCC—AOCl 4.0 安装VASP 6.4.2 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-40792-1-1.html)
    - [在AMD机器上安装DFT计算软件VASP.6.2.0简明教程 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-30264-1-1.html)
    - [AMD EPYC - 基于AMD AOCC+AOCL的VASP编译和部署 & MKL库及平台效率优化\_哔哩哔哩\_bilibili](https://b23.tv/LalDMPO)

```bash

```

- 相关报错

```bash
# 使用 makefile.include.gnu_ompi_aocl_omp；只安装 aocl-linux-gcc
mpif90 -fopenmp -ffree-form -ffree-line-length-none -w -ffpe-summary=invalid,zero,overflow -march=native -fallow-argument-mismatch -O2 -I/opt/AMD/5.0.0/gcc/include  -c minimax_functions1D.f90
f951: Fatal Error: Reading module ‘prec.mod’ at line 1 column 2: Unexpected EOF
compilation terminated.
make[2]: *** [makefile:166: minimax_functions1D.o] Error 1
```


---

### HDF5

- 安装步骤

```bash
wget https://hdf-wordpress-1.s3.amazonaws.com/wp-content/uploads/manual/HDF5/HDF5_1_14_3/src/hdf5-1.14.3.tar.gz

# 配置 Intel 版本
./configure --enable-parallel --enable-fortran --enable-cxx --enable-unsupported \
            CC=mpiicc FC=mpiifort CXX=mpiicpc \
            --prefix=${HOME}/local/hdf5

make
make install


# 显示 HDF5 的编译和配置详细信息
h5cc -showconfig  # 或 h5c++ h5pcc

# 显示用于编译 HDF5 的编译器命令行，包括链接的库和编译器标志
h5cc -show
```

- 未添加 `--enable-parallel` 参数会出现以下报错：

```bash
configure: error: --enable-cxx and --enable-parallel flags are incompatible. Use --enable-unsupported to override this error.
```

- 使用
    - HDF5 Preview 插件：只能打开.hdf5 格式，无法打开.h5 格式
    - Pandas 的 `read_hdf()` 不太好用
    - [vaspout.h5 - VASP Wiki](https://www.vasp.at/wiki/index.php/Vaspout.h5)
    - h5py 暂不能很好地解析 vaspout.h5 文件中的数据

```bash
h5ls data.h5     # 显示 Group 列表

# vaspout.h5 示例
input            # Group
intermediate     # Group
original         # Group
results          # Group
version          # Group

h5dump data.h5   # 输出文件的详细结构和内容
```


---

### VASP + HDF5

- 参考：[编译支持HDF5的VASP - 哔哩哔哩](https://www.bilibili.com/read/cv15039734/)

- 安装步骤

```bash
# 超算平台编译步骤
# 导入 Intel oneAPI 套件；hdf5
module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load hdf5/1.12.2-intel-2021.4.0

# 查看 hdf5/1.12.2-intel-2021.4.0 的安装路径
module show hdf5/1.12.2-intel-2021.4.0

cp arch/makefile.include.intel makefile.include
# 取消 HDF5 相关行注释，将 HDF5_ROOT  ?= 后的内容替换为 hdf5 的安装路径

make  # 或 make all, make std
```

- 可能会出现以下报错

```bash
error while loading shared libraries: libhdf5_fortran.so.102: cannot open shared object file: No such file or directory

# 原因：缺少 libhdf5_fortran.so.102 动态链接库，其实 module load 的 hdf5/1.12.2-intel-2021.4.0 有该动态链接库，不过版本更新一些，为 libhdf5_fortran.so.200

# 解决方法：将 libhdf5_fortran.so.200 软链接为 libhdf5_fortran.so.102；将 ~/lib 写入到 LD_LIBRARY_PATH

ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/hdf5-1.12.2-nxwmp3tddhreojgbib25ldc7wusvzf3m/lib/libhdf5_fortran.so.200 ~/lib/libhdf5_fortran.so.102

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$HOME/lib
```


---

## VASP + VTST

- 在 VASP 添加过渡态计算功能

- 参考：
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

- 备份 `src/chain.F`；拷贝 vtstcode-XXX 中对应 VASP 版本（如 vtstcode5、vtstcode6.3；vtstcode6.3 中多了 `ml_pyamff.F` 文件和 `pyamff_fortran/` 目录）的目录下的所有文件到 `src/`：

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

- VASP.6.3.0 + VTST 出现报错：VTST 源码代码有问题
    - [VASP6.3.2 + vtstcode6.3编译出错 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-46112-1-1.html)
    - [过渡态神器VTST为什么在VASP6.3编译不成功？因为源代码有问题！](https://mp.weixin.qq.com/s/ah33JQ7uTxcm_DakY2yJXA)
    - 解决方法：在 chain.F 第 202 行后添加 `ENDIF`

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

- 计算过程中，OUTCAR 中的每个离子步输出信息会多出以下内容

```bash
stress matrix after NEB project (eV)
     0.00481      0.00000      0.00000
     0.00000      0.00481     -0.00000
     0.00000      0.00000      0.00481
 FORCES: max atom, RMS     0.000000    0.000000
 FORCE total and by dimension    0.000000    0.000000
 Stress total and by dimension    0.008333    0.004811
```
