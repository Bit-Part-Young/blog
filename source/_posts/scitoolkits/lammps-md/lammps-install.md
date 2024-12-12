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

## 介绍

- 编译条件
    - 兼容 C++11 标准的编译器
    - 并行计算库（MPICH 或 OpenMPI 或其他 MPI 实现）
    - FFT 傅里叶变换库（FFTW；若没有安装，LAMMPS 将会使用自带的 KISS）
    - 若平台中若无 MPI 环境，可使用 `make mpi-stubs` 或安装 `stubs` package，编译过程中，将提供一个虚拟的 MPI 库，“欺骗” 需要 MPI 环境的包，使其正常编译

- 编译选项：[3.4. Basic build options — LAMMPS documentation](https://docs.lammps.org/Build_basics.html)

- 编译步骤：
    - 安装 packages：`make` 使用 `make yes-<package>`； `CMake` 使用 ` -D PKG_<NAME>=on`
    - Build LAMMPS

- 所有可用的 packages 及其描述：[6.1. Available Packages — LAMMPS documentation](https://docs.lammps.org/Packages_list.html)

- packages 细节：[6.2. Package details — LAMMPS documentation](https://docs.lammps.org/Packages_details.html)

- 金属体系常用 packages：manybody

- 参考资料：
    - [安装LAMMPS - lammps-tutorial](https://lammpscn2.vercel.app/Tutorial/install/#step2b-%E4%BD%BF%E7%94%A8%E4%BC%A0%E7%BB%9F%E7%9A%84make%E5%AE%89%E8%A3%85)
    - [Lammps installation - Jia-Xin Zhu](https://chiahsinchu.github.io/blog/2022/lmp-install/)
    - [Linux系统源码编译安装LAMMPS - 我是谁](https://yuhldr.github.io/posts/320.html)
    - [用 Intel® 加速 LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/09/22/intellammps/)
    - [Linux 软件安装⑥|LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/06/16/installlammps/)
    - LAMMPS 所有版本：[LAMMPS Source Download Repository](https://download.lammps.org/tars/index.html)
    - [GitHub - njzjz/lammps-wheel: LAMMPS unofficial Python wheels on PyPi, \`pip install lammps\`](https://github.com/njzjz/lammps-wheel)
    - OpenMPI 编译：[4.1. Quick start: Installing Open MPI — Open MPI 5.0.x documentation](https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html)



---

## CMake 编译

- 适用于较新版本的 LAMMPS

- 建议编译步骤

```bash
# 导入 Intel oneAPI 套件
module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.4.0
# 建议再导入该 oneAPI 模块
module load intel-oneapi-tbb/2021.4.0
# Pi 上建议再 load 以下模块
module load gcc/11.2.0
module load cmake/3.26.3-gcc-11.2.0

# 编译配置；oneapi 可改成 intel
mkdir build && cd build
cmake -D PKG_MANYBODY=yes -C ../cmake/presets/oneapi.cmake ../cmake

# 编译
make
```

- cmake 相关命令及内容

```bash
ll cmake/presets             # 列出预设 cmake 文件（自行选择安装 package）

# 预设的需安装的 packages
basic.cmake                  # 安装的 package 数目：64
most.cmake                   # 
all_on.cmake                 # 安装的 package 数目：92

# 预设的编译 OPTIONS
oneapi.cmake
intel.cmake
gcc.cmake
clang.cmake


# 配置编译选项 示例
mkdir build-basic && cd build-basic
cmake -C ../cmake/presets/basic.cmake ../cmake

mkdir build-most && cd build-most
cmake -C ../cmake/presets/most.cmake ../cmake

# 叠加配置编译 OPTIONS
cmake -C ../cmake/presets/basic.cmake -C ../cmake/presets/kokkos-cuda.cmake ../cmake

# 手动安装 packages
cmake -D PKG_KSPACE=yes  ../cmake

# cmake 参数；D 可以与后面的编译选项空一格空格
-D BUILD_MPI                  # 构建 MPI 版本
-D LAMMPS_MACHINE
-D CMAKE_C_COMPILER           # 指定 C 编译器
-D CMAKE_CXX_COMPILER         # 指定 CXX 编译器
-D CMAKE_Fortran_COMPILER     # 指定 Fortran 编译器
-D CMAKE_INSTALL_PREFIX       # 安装路径
-D CMAKE_BUILD_TYPE           # 构建类型；Debug / Release
-D BUILD_SHARED_LIBS          # 指定是否安装成共享库；若安装 LAMMPS 的 Python 模块，需指定
-D Python_EXECUTABLE          # 指定 Python 解释器路径
-D PKG_XXX=yes                # 安装 XXX package
-D PKG_GPU=on                 # 导入/安装 GPU package
-D GPU_API                    # opencl 或 cuda

make                          # 编译
make install                  # 安装；默认安装到 ~/.local
make install-python           # 安装 LAMMPS 的 Python 模块；作用是生成 whl 文件


cmake --build . --target clean  # 删除编译的目标、库和可执行文件
make clean                      # 同上


lmp -h                       # 显示已编译的 LAMMPS 版本的所有信息；可查看已安装的 packages

# 调用 GPU 加速计算，需加入 -sf -pk 两个 flag 
mpirun -np 8 lmp_gpu -sf gpu -pk gpu 1 -in in.file
-sf                          # 在所有支持 GPU 加速的脚本命令前加上 gpu 前缀
-pk gpu N                    # GPU 数量
```

- cmake 配置好 Makefile 文件之后，查看输出到屏幕的 `-- <<< Build configuration >>>` 编译配置进行检验；示例：

```bash
-- <<< Build configuration >>>
   LAMMPS Version:   20240829
   Operating System: Linux Ubuntu 22.04
   CMake Version:    3.22.1
   Build type:       RelWithDebInfo
   Install path:     /home/yangsl/.local
   Generator:        Unix Makefiles using /usr/bin/gmake
-- Enabled packages: MANYBODY
-- <<< Compilers and Flags: >>>
-- C++ Compiler:     /opt/software/intel/oneapi/compiler/2022.1.0/linux/bin/icpx
      Type:          IntelLLVM
      Version:       2022.1.0
      C++ Standard:  11
      C++ Flags:     -Wall -Wextra -g -O2 -DNDEBUG
      Defines:       LAMMPS_SMALLBIG;LAMMPS_MEMALIGN=64;LAMMPS_OMP_COMPAT=4;LAMMPS_GZIP
      Options:       -Wno-tautological-constant-compare;-Wno-unused-command-line-argument
-- <<< Linker flags: >>>
-- Executable name:  lmp
-- Static library flags:
-- <<< MPI flags >>>
-- MPI_defines:      MPICH_SKIP_MPICXX;OMPI_SKIP_MPICXX;_MPICC_H
-- MPI includes:     /opt/software/intel/oneapi/mpi/2021.6.0/include
-- MPI libraries:    /opt/software/intel/oneapi/mpi/2021.6.0/lib/libmpicxx.so;/opt/software/intel/oneapi/mpi/2021.6.0/lib/libmpifort.so;/opt/software/intel/oneapi/mpi/2021.6.0/lib/release/libmpi.so;/lib/x86_64-linux-gnu/libdl.a;/lib/x86_64-linux-gnu/librt.a;/lib/x86_64-linux-gnu/libpthread.a;
-- Configuring done
-- Generating done
```

- 报错：[Gmake error during cmake build with intel compiler - LAMMPS / LAMMPS Installation - Materials Science Community Discourse](https://matsci.org/t/gmake-error-during-cmake-build-with-intel-compiler/54030)

```bash
# 编译配置命令: cmake -D PKG_MANYBODY=yes -C ../cmake/presets/oneapi.cmake ../cmake
# 报错内容
clang++: error: unknown argument: '-qopenmp;-qopenmp-simd'
make[2]: *** [CMakeFiles/lammps.dir/build.make:76: CMakeFiles/lammps.dir/home/yangsl/opt/lammps-29Aug2024/src/angle.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:171: CMakeFiles/lammps.dir/all] Error 2
make: *** [Makefile:136: all] Error 2
```

- 其他：
    - 取消使用 JPEG 选项：`-D WITH_JPEG=off`（cmake 配置编译选项时会自动检查）：[8.6.1. Using CMake with LAMMPS — LAMMPS documentation](https://docs.lammps.org/Howto_cmake.html)
    - [ ] 思源一号用 oneapi.cmake 编译选项，其中的 MPI 是 MPI STUBS，而非 intel 的 MPI（2024.03.16）



---

## make 编译

- 简易编译步骤

```bash
# Master 服务器
make yes-manybody

make oneapi


# 个人常用 packages
manybody
mc                           # 蒙特卡洛
```

- make 相关命令及内容

```bash
cd src                       # 进入 src 目录

# 查看编译选项
make                         # 查看编译选项

# 清除；不会删除编译好的可执行程序
make clean-all               # 删除 object 文件
make clean-machine           # 删除 machine 的 object 文件

# package 相关；yes 安装、no 卸载；会更新 src 中的代码
make yes-<package>           # 添加要编译的 packages
make package                 # 列出可用 packages
make yes-basic               # 安装常用 packages
make no-basic
make yes-all                 # 安装所有 packages
make no-all
make yes-most                # 安装大部分 packages
make no-most
make yes-lib                 # 需要额外库的 packages 
make no-lib                  # 
make ps                      # 查看 packages 状态
make pi                      # 列出已安装的 packages
make package-update          # 更新 package

# packages 数目
yes-basic                    # 4 个 packages；kspace、manybody、molecule、rigid
yes-most                     # 56 个 packages
yes-all                      # 93 个 packages；使用 make no-lib 变成 65 个 packages

# Build LAMMPS
make serial                  # 编译串行版本
make mpi                     # 编译并行版本


# 根据 OPTIONS 编译
serial                  # GNU g++ compiler, no MPI
MPI                     # MPI with its default compiler
intel_cpu_intelmpi      # INTEL package, Intel MPI, MKL FFT
oneapi                  # Intel oneAPI

# 根据 MACHINE 编译
mac                     # Apple PowerBook G4 laptop, c++, no MPI
mac_mpi                 # Apple laptop, MacPorts Open MPI 1.4.3, gcc 4.8, jpeg
ubuntu                  # Ubuntu Linux box, g++, openmpi, FFTW3
ubuntu_simple           # Ubuntu Linux box, g++, openmpi, KISS FFT

# 查看 预设 make 文件
ll MAKE                      # 列出预设 make 文件
Makefile.example             # 示例文件
Makefile.serial              # make serial 使用的该文件
Makefile.mpi                 # make mpi 使用的该文件
```



---

## 检查

- 若没有安装 packages，最后编译得到的 lmp 可执行程序，查看可用命令，会相对较少

- 编译好后，需检查的内容
    - OS
    - Compiler
    - C++ standard
    - MPI
    - Accelerator configuration
    - Installed packages
    - 各种 style options



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
