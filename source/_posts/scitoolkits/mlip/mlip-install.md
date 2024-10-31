---
title: MLIP 安装
top: true
cover:
toc: true
mathjax: true
summary: MLIP 安装
description: MLIP 安装
tags:
  - LAMMPS
  - MLIP
  - 机器学习势函数
  - MTP
categories:
  - 科研工具
  - LAMMPS
date: 2023-07-03 15:56:30
abbrlink: 305651
password:
---

# MLIP 安装

## 安装

- 安装 Tutorial：
    - [installation tutorial · Wiki · Alexander Shapeev / MLIP-2 Tutorials · GitLab](https://gitlab.com/ashapeev/mlip-2-tutorials/-/wikis/installation-tutorial)
    - [README.md · master · Alexander Shapeev / LAMMPS-MLIP interface · GitLab](https://gitlab.com/ashapeev/interface-lammps-mlip-2/-/blob/master/README.md)

- 编译步骤：先编译 MLIP，再编译 MLIP 与 LAMMPS 的接口

```bash
# 导入 oneAPI 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-tbb/2021.4.0

# 编译 MLIP
git clone https://gitlab.com/ashapeev/mlip-2.git
cd mlip-2
./configure          # 生成 make 目录；自动检测所在平台是否有 MPI 环境
make mlp             # 生成 bin 和 obj 目录
make libinterface    # 生成 lib 目录

# 编译 MLIP 与 LAMMPS 的接口
cd ..
git clone https://gitlab.com/ashapeev/interface-lammps-mlip-2.git .
cd interface-lammps-mlip-2
cp ../mlip-2/lib/lib_mlip_interface.a .

# 在 preinstall.sh 文件结尾添加需安装的 package
make yes-<package>
# 不需要添加 make yes-STUBS，install.sh 脚本中已有 make mpi-stubs 命令

# 编译安装写法
./install.sh <path-to-lammps> <lammps-target>
# 示例
./install.sh ../lammps-29Aug2024 intel_cpu_intelmpi
# 其他 LAMMPS target
g++_mpich 
mpi 
g++_serial 
serial
```



---

## 相关问题

- 不建议在 Arm 平台编译，可 module load 的程序少且版本旧；不建议在 Manager 编译，Intel 版本较老

- 在 `preinstall.sh` 中添加 `make yes-STUBS`，编译报错：需注释 `make yes-STUBS`

```bash
../mpi.cpp:18:24: fatal error: ../version.h: No such file or directory
 #include "../version.h"
                        ^
compilation terminated.
```

- `tbbmalloc` 报错：还需导入 `intel-oneapi-tbb/2021.4.0`

```bash
ld: cannot find -ltbbmalloc
make[1]: *** [Makefile:98: ../lmp_intel_cpu_intelmpi] Error 1
```

- mpi-stubs 放在 intel_cpu_intelmpi 后的作用：不会对其造成影响

```bash
# 平台中若无 MPI 环境，提供一个虚拟的 MPI 库，“欺骗” 需要 MPI 环境的包，使其正常编译
make mpi-stubs
make intel_cpu_intelmpi -lgfortran
```
