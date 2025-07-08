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
    - FFT 傅里叶变换库（FFTW）
    - 若平台中若无 MPI 环境，可使用 `make mpi-stubs` 或安装 `stubs` package，编译过程中，将提供一个虚拟的 MPI 库，“欺骗” 需要 MPI 环境的包，使其正常编译
    - 若没有安装 FFTW，LAMMPS 将会使用自带的 KISS

- 编译选项：[3.4. Basic build options — LAMMPS documentation](https://docs.lammps.org/Build_basics.html)

- 编译步骤：
    - 安装 packages：`make` 使用 `make yes-<package>`； `CMake` 使用 ` -D PKG_<NAME>=on`
    - Build LAMMPS

- **LAMMPS 可在已编译好的基础上添加其他 package 或 pair_style 源码进行增量编译**

```bash
# cmake
cmake -D PKG_XXX=on ../cmake
# make
make yes-XXX


# 可增量编译（cmake 已测试，make 未测试）
# 拷贝 tabgap pair_style 源代码文件
cp lammps/pair_tabgap.* LAMMPS_PATH/src/
# 编译
make -jN
```

- 所有可用的 packages 及其描述：[6.1. Available Packages — LAMMPS documentation](https://docs.lammps.org/Packages_list.html)

- packages 细节：[6.2. Package details — LAMMPS documentation](https://docs.lammps.org/Packages_details.html)

- Accelerator pcakages（加速器）：[7.4. Accelerator packages — LAMMPS documentation](https://docs.lammps.org/Speed_packages.html)
    - INTEL、GPU、KOKKOS、OPENMP、OPT（OPT、OPENMP 易安装）

- 安装 GPU package（需确定 GPU 硬件类型及其架构、精度）

```bash
# cmake；GPU 硬件类型选择 CUDA；sm_86 或 sm_89
-C ../cmake/presets/gpu-cuda.cmake -D GPU_ARCH=sm_86


# sm_30 for Kepler (supported since CUDA 5 and until CUDA 10.x)
# sm_35 or sm_37 for Kepler (supported since CUDA 5 and until CUDA 11.x)
# sm_50 or sm_52 for Maxwell (supported since CUDA 6)
# sm_60 or sm_61 for Pascal (supported since CUDA 8)
# sm_70 for Volta (supported since CUDA 9)
# sm_75 for Turing (supported since CUDA 10)
# sm_80 or sm_86 for Ampere (supported since CUDA 11, sm_86 since CUDA 11.1)
# sm_89 for Lovelace (supported since CUDA 11.8)
# sm_90 for Hopper (supported since CUDA 12.0)
```

- 安装 KOKKOS package：[3.7. Packages with extra build options — LAMMPS documentation](https://docs.lammps.org/Build_extras.html#kokkos)

```bash
# 使用 CUDA (NVIDIA GPU)
# 方式 1
-C ../cmake/presets/kokkos-cuda.cmake

# 方式 2
-D PKG_KOKKOS=ON
-D Kokkos_ENABLE_CUDA=ON
-D Kokkos_ARCH_AMDAVX=ON              # HOSTARCH；需根据自己的 CPU 类型进行修改
-D Kokkos_ARCH_AMPERE100=ON           # GPUARCH；；需根据自己的 GPU 类型进行修改
-D Kokkos_ENABLE_OPENMP=ON
```

- 安装 LAMMPS Python 模块：[2.2. Installation — LAMMPS documentation](https://docs.lammps.org/Python_install.html)

```bash
# 需以 shared mode 编译 LAMMPS
# cmake
-D BUILD_SHARED_LIBS=yes
# make
make mode=shared

# 安装 LAMMPS Python 模块
make install-python

# 验证
from lammps import lammps

lmp = lammps()
```

- 个人常用 packages

```bash
manybody                     # 多体势（金属体系常用）
mc                           # 蒙特卡洛
```

- 参考资料：
    - [安装LAMMPS - lammps-tutorial](https://lammpscn2.vercel.app/Tutorial/install/#step2b-%E4%BD%BF%E7%94%A8%E4%BC%A0%E7%BB%9F%E7%9A%84make%E5%AE%89%E8%A3%85)
    - [Lammps installation - Jia-Xin Zhu](https://chiahsinchu.github.io/blog/2022/lmp-install/)
    - [Linux系统源码编译安装LAMMPS - 我是谁](https://yuhldr.github.io/posts/320.html)
    - [用 Intel® 加速 LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/09/22/intellammps/)
    - [Linux 软件安装⑥|LAMMPS - Jinzhe Zeng's Blog](https://njzjz.win/2018/06/16/installlammps/)
    - LAMMPS 所有版本：[LAMMPS Source Download Repository](https://download.lammps.org/tars/index.html)
    - [GitHub - njzjz/lammps-wheel: LAMMPS unofficial Python wheels on PyPi, \`pip install lammps\`](https://github.com/njzjz/lammps-wheel)
    - OpenMPI 编译：[4.1. Quick start: Installing Open MPI — Open MPI 5.0.x documentation](https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html)
    - Build GPU package：[3.7. Packages with extra build options — LAMMPS documentation](https://docs.lammps.org/Build_extras.html#gpu)



---

## CMake 编译

- 适用于较新版本的 LAMMPS；优点：保持 src 目录干净

- [8.6.1. Using CMake with LAMMPS — LAMMPS documentation](https://docs.lammps.org/Howto_cmake.html)

- 编译步骤精简

```bash
# 导入 Intel oneAPI 套件；Master 可不用
module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.12.1
module load intel-oneapi-tbb/2021.4.0
# Pi 上建议再 load 以下模块
module load gcc/11.2.0
module load cmake/3.26.3-gcc-11.2.0


# 编译配置；oneapi 可改成 intel
mkdir build && cd $_
# FFT 库默认是 KISS（若无单独编译 FFTW 并设置相关环境变量）
# 手动安装 packages
cmake -D PKG_MANYBODY=yes -D FFT=MKL -C ../cmake/presets/oneapi.cmake ../cmake
# 安装预设 packages
cmake -C ../cmake/presets/basic.cmake -D FFT=MKL -C ../cmake/presets/oneapi.cmake ../cmake
# 安装所有 packages，去掉需外部依赖的 packages
# 额外去掉 RHEO、INTEL packages，否则会报错
cmake -C ../cmake/presets/all_on.cmake -C ../cmake/presets/nolib.cmake -D PKG_INTEL=no -D PKG_RHEO=no -D FFT=MKL -D BUILD_SHARED_LIBS=yes -C ../cmake/presets/oneapi.cmake ../cmake


# 编译
make -jN
```

- 在思源平台编译 LAMMPS，得到的可执行文件，其 MPI 是 MPI STUBS，而非 Intel 的 MPI
    - 原因：`module load intel-oneapi-mpi/2021.4.0` 无法识别 Intel MPI，而 `module load intel-oneapi-mpi/2021.12.1` 可成功识别 Intel MPI（其他版本的也可以）

- 报错：`clang++: error: unknown argument: '-qopenmp;-qopenmp-simd'`
    - [Gmake error during cmake build with intel compiler - LAMMPS / LAMMPS Installation - Materials Science Community Discourse](https://matsci.org/t/gmake-error-during-cmake-build-with-intel-compiler/54030)
    - [\[BUG\] OpenMP: omp.h not found by CMake when using oneapi preset · Issue #4033 · lammps/lammps](https://github.com/lammps/lammps/issues/4033)
    - 原因：cmake 版本偏旧，应更新 cmake

```bash
# 编译配置命令: 使用 oneapi.cmake
# 报错内容
clang++: error: unknown argument: '-qopenmp;-qopenmp-simd'
make[2]: *** [CMakeFiles/lammps.dir/build.make:76: CMakeFiles/lammps.dir/home/yangsl/opt/lammps-29Aug2024/src/angle.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:171: CMakeFiles/lammps.dir/all] Error 2
make: *** [Makefile:136: all] Error 2
```

---

- cmake 相关命令及内容

```bash
ll cmake/presets             # 列出预设 cmake 文件（自行选择安装 package）

# 预设的需安装的 packages
basic.cmake                  # package 数目: 4 (KSPACE MANYBODY MOLECULE RIGID)
most.cmake                   # package 数目: 66
all_on.cmake                 # package 数目: 93

# 预设的编译 OPTIONS
oneapi.cmake
intel.cmake
gcc.cmake
clang.cmake


# 配置编译选项 示例
mkdir build-basic && cd $_
cmake -C ../cmake/presets/basic.cmake ../cmake

mkdir build-most && cd $_
cmake -C ../cmake/presets/most.cmake ../cmake

# 叠加配置编译 OPTIONS
cmake -C ../cmake/presets/basic.cmake -C ../cmake/presets/oneapi.cmake ../cmake

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
-D FFT                        # 指定 FFTW 库，默认 FFTW3；可选值 FFTW3、MKL、NVPL、KISS；找不到时会使用 KISS
-D WITH_JPEG=off              # 不使用 JPEG；会自动检查
-D LAMMPS_GZIP=               # 使用


make                          # 编译
make install                  # 安装；默认安装到 ~/.local
make install-python           # 安装 LAMMPS Python 模块；作用是生成 whl 文件


cmake --build . --target clean  # 删除编译的目标、库和可执行文件
make clean                    # 同上


lmp -h                        # 显示已编译的 LAMMPS 版本的所有信息；可查看已安装的 packages

# 调用 GPU 加速计算，需加入 -sf -pk 两个 flag 
mpirun -np 8 lmp_gpu -sf gpu -pk gpu 1 -in in.file
-sf                           # 在所有支持 GPU 加速的脚本命令前加上 gpu 前缀
-pk gpu N                     # GPU 数量
```

- 配置好后，查看输出到屏幕的 `-- <<< Build configuration >>>` 编译配置进行检验，示例：
    - Compilers and Flags
    - MPI flags
    - FT settings

```bash
-- <<< Build configuration >>>
   LAMMPS Version:   20240829
   Operating System: Linux Ubuntu 22.04
   CMake Version:    3.31.5
   Build type:       RelWithDebInfo
   Install path:     /home/XXX/.local
   Generator:        Unix Makefiles using /usr/bin/gmake
-- Enabled packages: AMOEBA;ASPHERE;BOCS;BODY;BPM;BROWNIAN;CG-DNA;CG-SPICA;CLASS2;COLLOID;COLVARS;CORESHELL;DIELECTRIC;DIFFRACTION;DIPOLE;DPD-BASIC;DPD-MESO;DPD-REACT;DPD-SMOOTH;DRUDE;EFF;EXTRA-COMMAND;EXTRA-COMPUTE;EXTRA-DUMP;EXTRA-FIX;EXTRA-MOLECULE;EXTRA-PAIR;FEP;GRANULAR;INTERLAYER;KSPACE;MANIFOLD;MANYBODY;MC;MEAM;MESONT;MGPT;MISC;ML-IAP;ML-POD;ML-RANN;ML-SNAP;ML-UF3;MOFFF;MOLECULE;OPENMP;OPT;ORIENT;PERI;PHONON;PLUGIN;POEMS;PTM;QEQ;QTB;REACTION;REAXFF;REPLICA;RIGID;SHOCK;SMTBQ;SPH;SPIN;SRD;TALLY;UEF;YAFF
-- <<< Compilers and Flags: >>>
-- C++ Compiler:     /opt/software/intel/oneapi/compiler/2022.1.0/linux/bin/icpx
      Type:          IntelLLVM
      Version:       2022.1.0
      C++ Standard:  11
      C++ Flags:     -Wall -Wextra -g -O2 -DNDEBUG
      Defines:       LAMMPS_SMALLBIG;LAMMPS_MEMALIGN=64;LAMMPS_OMP_COMPAT=4;LAMMPS_GZIP;FFT_MKL;FFT_MKL_THREADS;LMP_OPENMP;LMP_PLUGIN
      Options:       -Wno-tautological-constant-compare;-Wno-unused-command-line-argument
-- C compiler:       /opt/software/intel/oneapi/compiler/2022.1.0/linux/bin/icx
      Type:          IntelLLVM
      Version:       2022.1.0
      C Flags:       -Wall -Wextra -g -O2 -DNDEBUG
-- <<< Linker flags: >>>
-- Executable name:  lmp
-- Shared library flags:
-- <<< MPI flags >>>
-- MPI_defines:      MPICH_SKIP_MPICXX;OMPI_SKIP_MPICXX;_MPICC_H
-- MPI includes:     /opt/software/intel/oneapi/mpi/2021.6.0/include
-- MPI libraries:    /opt/software/intel/oneapi/mpi/2021.6.0/lib/libmpicxx.so;/opt/software/intel/oneapi/mpi/2021.6.0/lib/libmpifort.so;/opt/software/intel/oneapi/mpi/2021.6.0/lib/release/libmpi.so;/lib/x86_64-linux-gnu/libdl.a;/lib/x86_64-linux-gnu/librt.a;/lib/x86_64-linux-gnu/libpthread.a;
-- <<< FFT settings >>>
-- Primary FFT lib:  MKL
-- Using double precision FFTs
-- Using threaded FFTs
-- Using builtin distributed FFT algorithms
-- Configuring done (5.1s)
-- Generating done (0.2s)
-- Build files have been written to: /home/XXX/opt/lammps-29Aug2024/build
```



---

## make 编译

- 编译步骤精简

```bash
# 导入 Intel oneAPI 套件；Master 可不用
module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-tbb/2021.4.0
# Pi 上建议再 load 以下模块
module load gcc/11.2.0
module load cmake/3.26.3-gcc-11.2.0


make yes-manybody       # 或 make yes-basic
make oneapi             # FFT 库为 MKL
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
# 根据 OPTIONS 编译；优先考虑使用
serial                       # GNU g++ compiler, no MPI
mpi                          # MPI with its default compiler
intel_cpu_intelmpi           # INTEL package, Intel MPI, MKL FFT
oneapi                       # Intel oneAPI

# 根据 MACHINE 编译
mac                          # Apple PowerBook G4 laptop, c++, no MPI
mac_mpi                      # Apple laptop, MacPorts Open MPI 1.4.3, gcc 4.8, jpeg
ubuntu                       # Ubuntu Linux box, g++, openmpi, FFTW3
ubuntu_simple                # Ubuntu Linux box, g++, openmpi, KISS FFT

# 查看 预设 make 文件
ll MAKE                      # 列出预设 make 文件
Makefile.example             # 示例文件
Makefile.serial              # make serial 使用的该文件
Makefile.mpi                 # make mpi 使用的该文件
```



---

## 检查

- 编译好后，输入 `lmp -h`，检查以下内容
    - OS（同一平台，不会变）
    - Compiler（这个会有差异，如 Intel Classic C++、Intel LLVM C++、GNU C++）
    - C++ standard（C++ 11，不会变）
    - MPI（这个会有差异，如 Intel (R) MPI Library、LAMMPS MPI STUBS）
    - Accelerator configuration（内容一般为空？）
    - FFT information（这个会有差异，KISS、MKL）
    - Installed packages
    - 各种 style options（根据安装的 packages 特性或额外命令，其 options 数目会有不同）

- 若没有安装任何 packages，最后编译得到的 lmp 可执行程序，查看可用 style options（如下所示），会相对较少

```bash
List of individual style options included in this LAMMPS executable

* Atom styles:

atomic          body            charge          ellipsoid       hybrid          
line            sphere          tri             

* Integrate styles:

respa           verlet          

* Minimize styles:

cg              fire/old        fire            hftn            quickmin        
sd              

* Pair styles:

born            buck            buck/coul/cut   coul/cut        coul/debye      
coul/dsf        coul/wolf       meam/c          reax            reax/c          
mesont/tpm      hybrid          hybrid/omp      hybrid/molecular                
hybrid/molecular/omp            hybrid/overlay  hybrid/overlay/omp              
hybrid/scaled   hybrid/scaled/omp               lj/cut          lj/cut/coul/cut 
lj/expand       morse           soft            table           yukawa          
zbl             zero            

* Bond styles:

hybrid          zero            

* Angle styles:

hybrid          zero            

* Dihedral styles:

hybrid          zero            

* Improper styles:

hybrid          zero            

* KSpace styles:


* Fix styles

adapt           addforce        ave/atom        ave/chunk       ave/correlate   
ave/grid        ave/histo       ave/histo/weight                ave/time        
aveforce        balance         box/relax       deform          deposit         
ave/spatial     ave/spatial/sphere              lb/pc           
lb/rigid/pc/sphere              reax/c/bonds    reax/c/species  dt/reset        
efield          enforce2d       evaporate       external        gravity         
halt            heat            indent          langevin        lineforce       
momentum        move            nph             nph/sphere      npt             
npt/sphere      nve             nve/limit       nve/noforce     nve/sphere      
nvt             nvt/sllod       nvt/sphere      pair            planeforce      
press/berendsen press/langevin  print           property/atom   recenter        
restrain        setforce        spring          spring/chunk    spring/self     
store/force     store/state     temp/berendsen  temp/rescale    
thermal/conductivity            vector          viscous         wall/harmonic   
wall/lj1043     wall/lj126      wall/lj93       wall/morse      wall/reflect    
wall/region     wall/table      

* Compute styles:

aggregate/atom  angle           angle/local     angmom/chunk    bond            
bond/local      centro/atom     centroid/stress/atom            chunk/atom      
chunk/spread/atom               cluster/atom    cna/atom        com             
com/chunk       coord/atom      count/type      mesont          dihedral        
dihedral/local  dipole          dipole/chunk    displace/atom   erotate/sphere  
erotate/sphere/atom             fragment/atom   global/atom     group/group     
gyration        gyration/chunk  heat/flux       improper        improper/local  
inertia/chunk   ke              ke/atom         msd             msd/chunk       
omega/chunk     orientorder/atom                pair            pair/local      
pe              pe/atom         pressure        property/atom   property/chunk  
property/grid   property/local  rdf             reduce          reduce/chunk    
reduce/region   slice           stress/atom     temp            temp/chunk      
temp/com        temp/deform     temp/partial    temp/profile    temp/ramp       
temp/region     temp/sphere     torque/chunk    vacf            vcm/chunk       

* Region styles:

block           cone            cylinder        ellipsoid       intersect       
plane           prism           sphere          union           

* Dump styles:

atom            cfg             custom          atom/mpiio      cfg/mpiio       
custom/mpiio    xyz/mpiio       grid            grid/vtk        image           
local           movie           xyz             

* Command styles

angle_write     balance         change_box      create_atoms    create_bonds    
create_box      delete_atoms    delete_bonds    box             kim_init        
kim_interactions                kim_param       kim_property    kim_query       
reset_ids       reset_atom_ids  reset_mol_ids   message         server          
dihedral_write  displace_atoms  info            minimize        read_data       
read_dump       read_restart    replicate       rerun           run             
set             velocity        write_coeff     write_data      write_dump      
write_restart   
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
