---
title: LAMMPS 安装
top: false
cover:
toc: true
mathjax: true
summary: LAMMPS 安装
description: LAMMPS 安装
tags:
  - LAMMPS
  - 分子动力学
categories:
  - 科研工具
date: 2023-11-13 22:30:00
abbrlink: 581193
password:
---

# LAMMPS 安装

- MPICH（并行计算库）、FFTW（快速傅里叶变换库）

- 参考资料：
    - [安装LAMMPS - lammps-tutorial](https://lammpscn2.vercel.app/Tutorial/install/#step2b-%E4%BD%BF%E7%94%A8%E4%BC%A0%E7%BB%9F%E7%9A%84make%E5%AE%89%E8%A3%85)
    - [Lammps installation - Jia-Xin Zhu](https://chiahsinchu.github.io/blog/2022/lmp-install/)
    - [Linux系统源码编译安装LAMMPS - 我是谁](https://yuhldr.github.io/posts/320.html)
    - [用 Intel® 加速 LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/09/22/intellammps/)
    - [Linux 软件安装⑥|LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/06/16/installlammps/)
    - LAMMPS 所有版本：[LAMMPS Source Download Repository](https://download.lammps.org/tars/index.html)
    - [GitHub - njzjz/lammps-wheel: LAMMPS unofficial Python wheels on PyPi, \`pip install lammps\`](https://github.com/njzjz/lammps-wheel)



---

## cmake 编译

- 适用于较新版本的 LAMMPS

```bash
wget https://download.lammps.org/tars/lammps-2Aug2023.tar.gz
tar -xzvf lammps-2Aug2023.tar.gz
cd lammps-2Aug2023

# 导入 oneAPI 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.4.0
# 建议再导入该 oneAPI 模块
module load intel-oneapi-tbb/2021.4.0
# Pi 上建议再 load 以下模块
module load gcc/11.2.0
module load cmake/3.26.3-gcc-11.2.0

# 列出预设 cmake 文件（自行选择安装 package）
ll cmake/presets

basic.cmake                  # 安装的 package 数目：64
most.cmake                   # 
all_on.cmake                 # 安装的 package 数目：92
oneapi.cmake & intel.cmake   # 不会安装 package


# 创建 build 路径并配置编译选项
# 只含 一些基础的 packages
mkdir build-basic && cd build-basic
cmake -C ../cmake/presets/basic.cmake ../cmake

# 含 大部分的 packages
mkdir build-most && cd build-most
cmake -C ../cmake/presets/most.cmake ../cmake

# cmake 参数
-DCMAKE_C_COMPILER           # 指定 C 编译器
-DCMAKE_CXX_COMPILER         # 指定 CXX 编译器
-DCMAKE_Fortran_COMPILER     # 指定 Fortran 编译器
-DCMAKE_INSTALL_PREFIX       # 安装路径
-DCMAKE_BUILD_TYPE           # 构建类型；Debug / Release
-DBUILD_SHARED_LIBS          # 指定是否安装成共享库；若安装 LAMMPS 的 Python 模块，需指定
-DPython_EXECUTABLE          # 指定 Python 解释器路径

make                         # 编译

make install-python          # 安装 LAMMPS 的 Python 模块；作用是生成 whl 文件

lmp -h                       # 显示已编译的 LAMMPS 版本的所有信息；可查看已安装的 packages
```

- cmake 配置好 Makefile 文件之后，查看输出到屏幕的 `-- Enabled packages` 参数进行检验；示例：

```bash
-- Enabled packages: <None>

-- Enabled packages: KSPACE;MANYBODY;MOLECULE;RIGID

-- Enabled packages: AMOEBA;ASPHERE;BOCS;BODY;BPM;BROWNIAN;CG-DNA;CG-SPICA;CLASS2;COLLOID;COLVARS;CORESHELL;DIELECTRIC;DIFFRACTION;DIPOLE;DPD-BASIC;DPD-MESO;DPD-REACT;DPD-SMOOTH;DRUDE;EFF;EXTRA-COMPUTE;EXTRA-DUMP;EXTRA-FIX;EXTRA-MOLECULE;EXTRA-PAIR;FEP;GRANULAR;INTEL;INTERLAYER;KSPACE;MANIFOLD;MANYBODY;MC;MEAM;MESONT;MGPT;MISC;ML-IAP;ML-POD;ML-RANN;ML-SNAP;MOFFF;MOLECULE;OPENMP;OPT;ORIENT;PERI;PHONON;PLUGIN;POEMS;PTM;QEQ;QTB;REACTION;REAXFF;REPLICA;RIGID;SHOCK;SMTBQ;SPH;SPIN;SRD;TALLY;UEF;YAFF
```

- 其他：
    - 取消使用 JPEG 选项：`-D WITH_JPEG=off`（cmake 配置编译选项时会自动检查）：[8.6.1. Using CMake with LAMMPS — LAMMPS documentation](https://docs.lammps.org/Howto_cmake.html)
    - [ ] 思源一号用 oneapi.cmake 编译选项，其中的 MPI 是 MPI STUBS，而非 intel 的 MPI（2024.03.16）


---

## make 编译

```bash
cd src

make                         # 查看 make 所有选项
make clean-all               # 
make yes-<package>           # 
make yes-all                 #  安装所有 packages
make no-lib                  # 卸载需要外部库的 packages 
make package-update          # 
make serial                  # 编译串行版本
make mpi                     # 编译并行版本
```


---

## MC2 LAMMPS 版本编译

- LAMMPS 版本：22Aug2018
- gibbs_multireplica.ccp 和 gibbs_multireplica.h 需要用到 LAPACK，使用 `make intel_cpu` 命令，由于 master、超算无 libjpeg 库，因此需修改/注释 Makefile.intel_cpu（文件路径：`MAKE/OPTION`） 中的 jpeg 相关选项（共 4 处）

```bash
wget https://download.lammps.org/tars/lammps-22Aug2018.tar.gz

# 修改/注释 jpeg 相关选项
LMP_INC =   -DLAMMPS_GZIP
# LMP_INC = -DLAMMPS_GZIP -DLAMMPS_JPEG

# JPG_INC =
# JPG_PATH =
# JPG_LIB = -ljpeg
```

```bash
# 检查是否已安装 libjpeg
dpkg -l | grep -i 'libjpeg'  # Ubuntu
rpm -qa | grep -i 'libjpeg'  # Centos
yum list installed | grep -i 'libjpeg'  # Centos

# 安装 libjpeg
sudo apt install libjpeg-dev

# 导入 oneAPI 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
# 未导入该模块会报错
module load intel-oneapi-tbb/2021.4.0

cd src/

# 第一次编译
make clean-all
make yes-misc
make yes-user-misc
make yes-user-meamc
make yes-mc
make yes-replica
make yes-manybody
make package-update
make intel_cpu

# 复制 gibbs_multireplica.ccp 及头文件到 USER-MISC 目录

# 第二次编译
make package-update
make intel_cpu
```


---

相关报错

- `make mpi` 编译报错：对 `dgelsd_`（LAPACK 里的东西） 未定义的引用；改用 `make intel_cpu`

```text
/usr/bin/ld: gibbs_multireplica.o: in function `LAMMPS_NS::GibbsMultiReplica::inverse(double*, double*, double*, double)':
/home/yangsl/src/lammps-22Aug18-MC2/src/Obj_mpi/../gibbs_multireplica.cpp:2871: undefined reference to `dgelsd_'
/usr/bin/ld: /home/yangsl/src/lammps-22Aug18-MC2/src/Obj_mpi/../gibbs_multireplica.cpp:2876: undefined reference to `dgelsd_'
collect2: error: ld returned 1 exit status
```

---

- 没有 libjpeg 库：修改/注释 Makefile.intel_cpu 中的 JPEG 相关选项（共 4 处）

```text
../image.cpp(32): catastrophic error: cannot open source file "jpeglib.h"
  #include "jpeglib.h"
                      ^

compilation aborted for ../image.cpp (code 4)
```

```text
ld: cannot find -ljpeg: No such file or directory
```


---

## macOS 安装 LAMMPS GUI

限制较多（without MPI support），不推荐
