---
title: LAMMPS 安装与使用
top: false
cover: false
toc: true
mathjax: true
summary: LAMMPS 安装与使用
tags:
  - LAMMPS
  - 分子动力学
categories:
  - 科研工具
date: 2023-11-13 22:30:00
abbrlink: "58117"
password:
---

# LAMMPS 安装与使用

## 介绍

---

### 参考资料

LAMMPS 官网：[LAMMPS Molecular Dynamics Simulator](https://www.lammps.org)

LAMMPS 手册：[LAMMPS Documentation (2 Aug 2023 version) — LAMMPS documentation](https://docs.lammps.org/Manual.html)

教程：[LAMMPS教程](https://mp.weixin.qq.com/s/y80KyKUvI-46S7VGcuO5gQ)



---

## 安装

使用 cmake 编译（超算平台）
```bash
wget https://download.lammps.org/tars/lammps-2Aug2023.tar.gz
tar -xzvf lammps-2Aug2023.tar.gz
cd lammps-2Aug2023

module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.4.0
# pi 上建议再 load 以下模块
module load gcc/11.2.0
module load cmake/3.26.3-gcc-11.2.0

# 创建 build 路径并编译
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
-- Enabled packages: KSPACE;MANYBODY;MOLECULE;RIGID

-- Enabled packages: AMOEBA;ASPHERE;BOCS;BODY;BPM;BROWNIAN;CG-DNA;CG-SPICA;CLASS2;COLLOID;COLVARS;CORESHELL;DIELECTRIC;DIFFRACTION;DIPOLE;DPD-BASIC;DPD-MESO;DPD-REACT;DPD-SMOOTH;DRUDE;EFF;EXTRA-COMPUTE;EXTRA-DUMP;EXTRA-FIX;EXTRA-MOLECULE;EXTRA-PAIR;FEP;GRANULAR;INTEL;INTERLAYER;KSPACE;MANIFOLD;MANYBODY;MC;MEAM;MESONT;MGPT;MISC;ML-IAP;ML-POD;ML-RANN;ML-SNAP;MOFFF;MOLECULE;OPENMP;OPT;ORIENT;PERI;PHONON;PLUGIN;POEMS;PTM;QEQ;QTB;REACTION;REAXFF;REPLICA;RIGID;SHOCK;SMTBQ;SPH;SPIN;SRD;TALLY;UEF;YAFF
```


查看已编译安装的 packages
```bash
# 显示已编译的 LAMMPS 版本的所有信息
lmp -h
```


---

### Mac 安装 LAMMPS GUI

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
