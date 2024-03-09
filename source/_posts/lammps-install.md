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
abbrlink: "58117"
password:
---

# LAMMPS 安装

LAMMPS 所有版本：[LAMMPS Source Download Repository](https://download.lammps.org/tars/index.html)

---

### cmake 编译

适用于较新版本的 LAMMPS

most.cmake 安装的 package 数目：64
all_on.cmake 安装的 package 数目：92
oneapi.cmake 和 intel.cmake 不会安装 package

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

# 创建 build 路径并配置编译选项
# 只含 一些基础的 packages
mkdir build-basic && cd build-basic
cmake -C ../cmake/presets/basic.cmake ../cmake

# 含 大部分的 packages
mkdir build-most && cd build-most
cmake -C ../cmake/presets/most.cmake ../cmake

make
# make -j 4
```

>cmake 配置好 Makefile 文件之后，查看输出到屏幕的 `-- Enabled packages` 参数进行检验

示例
```bash
-- Enabled packages: <None>

-- Enabled packages: KSPACE;MANYBODY;MOLECULE;RIGID

-- Enabled packages: AMOEBA;ASPHERE;BOCS;BODY;BPM;BROWNIAN;CG-DNA;CG-SPICA;CLASS2;COLLOID;COLVARS;CORESHELL;DIELECTRIC;DIFFRACTION;DIPOLE;DPD-BASIC;DPD-MESO;DPD-REACT;DPD-SMOOTH;DRUDE;EFF;EXTRA-COMPUTE;EXTRA-DUMP;EXTRA-FIX;EXTRA-MOLECULE;EXTRA-PAIR;FEP;GRANULAR;INTEL;INTERLAYER;KSPACE;MANIFOLD;MANYBODY;MC;MEAM;MESONT;MGPT;MISC;ML-IAP;ML-POD;ML-RANN;ML-SNAP;MOFFF;MOLECULE;OPENMP;OPT;ORIENT;PERI;PHONON;PLUGIN;POEMS;PTM;QEQ;QTB;REACTION;REAXFF;REPLICA;RIGID;SHOCK;SMTBQ;SPH;SPIN;SRD;TALLY;UEF;YAFF
```


查看已编译安装的 packages
```bash
# 显示已编译的 LAMMPS 版本的所有信息
lmp -h
```



取消使用 JPEG 选项：`-D WITH_JPEG=off`（cmake 配置编译选项时会自动检查）
>[8.6.1. Using CMake with LAMMPS — LAMMPS documentation](https://docs.lammps.org/Howto_cmake.html)




---

### make 编译

进入 src 目录

```bash
# 查看 make 所有选项
make

make clean-all

make yes-<package>

make package-update

# 编译串行版本
make serial
# 编译并行版本
make mpi
```

### MC2 LAMMPS 版本编译

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

- `make mpi` 编译报错：对 `dgelsd_`（LAPACK 里的东西 ） 未定义的引用；改用 `make intel_cpu`

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

### Mac 安装 LAMMPS GUI

限制较多，不推荐

```text
LAMMPS and LAMMPS GUI universal binaries for macOS (arm64/x86_64)
=================================================================

This package provides universal binaries of LAMMPS and LAMMPS GUI that should
run on macOS systems running running macOS version 11 (Big Sur) or newer.  Note
the binaries are compiled without MPI support and contain a compatible subset
of the available packages.

The following individual commands are included:
binary2txt lammps-gui lmp msi2lmp phana stl_bin2txt

After copying the LAMMPS_GUI folder into your Applications folder, please follow
these steps:

1. Open the Terminal app

2. Type the following command and press ENTER:

   open ~/.zprofile

   This will open a text editor for modifying the .zprofile file in your home
   directory.

3. Add the following lines to the end of the file, save it, and close the editor

   LAMMPS_INSTALL_DIR=/Applications/LAMMPS_GUI.app/Contents
   LAMMPS_POTENTIALS=${LAMMPS_INSTALL_DIR}/share/lammps/potentials
   LAMMPS_BENCH_DIR=${LAMMPS_INSTALL_DIR}/share/lammps/bench
   MSI2LMP_LIBRARY=${LAMMPS_INSTALL_DIR}/share/lammps/frc_files
   PATH=${LAMMPS_INSTALL_DIR}/bin:$PATH
   export LAMMPS_POTENTIALS LAMMPS_BENCH_DIR PATH

4. In your existing terminal, type the following command make the settings active

   source ~/.zprofile

   Note, you don't have to type this in new terminals, since they will apply
   the changes from .zprofile automatically.

   Note: the above assumes you use the default shell (zsh) that comes with
   MacOS. If you customized MacOS to use a different shell, you'll need to
   modify that shell's init file (.cshrc, .bashrc, etc.) instead with
   appropiate commands to modify the same environment variables.

5. Try running LAMMPS (which might fail, see step 7)

   lmp -in ${LAMMPS_BENCH_DIR}/in.lj

6. Try running the LAMMPS GUI

   lammps-gui ${LAMMPS_BENCH_DIR}/in.rhodo

   Depending on the size and resolution of your screen, the fonts may be too
   small to read. This can be adjusted by setting the environment variable
   QT_FONT_DPI. The default value would be 72, so to increase the fonts by a
   third, one can add to the .zprofile file the line

   export QT_FONT_DPI=96

   and reload as shown above.

7. Give permission to execute the commands (lmp, lammps-gui, msi2lmp, binary2txt, phana, stl_bin2txt)

   MacOS will likely block the initial run of the executables, since they were
   downloaded from the internet and are missing a known signature from an
   identified developer. Go to "Settings" and search for "Security settings".
   It should display a message that an executable like "lmp" was blocked. Press
   "Open anyway", which might prompt you for your admin credentials. Afterwards
   "lmp" and the other executables should work as expected.

```


---

## 使用
