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

- 安装教程：
    - [installation tutorial · Wiki · Alexander Shapeev / MLIP-2 Tutorials · GitLab](https://gitlab.com/ashapeev/mlip-2-tutorials/-/wikis/installation-tutorial)
    - [README.md · master · Alexander Shapeev / LAMMPS-MLIP interface · GitLab](https://gitlab.com/ashapeev/interface-lammps-mlip-2/-/blob/master/README.md)

- 编译步骤：先编译 MLIP-2，再编译 MLIP-2 与 LAMMPS 的接口

```bash
# 导入 oneAPI 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-tbb/2021.4.0

# 编译 MLIP-2
git clone https://gitlab.com/ashapeev/mlip-2.git
cd mlip-2
./configure          # 生成 make/config.mk 文件；会自动检测所在平台是否有 MPI 环境以及编译器（GPU 或 Intel）
make mlp             # 生成 bin 和 obj 目录
make libinterface    # 生成 lib 目录

# 编译 MLI-2P 与 LAMMPS 的接口
cd ..
git clone https://gitlab.com/ashapeev/interface-lammps-mlip-2.git .
cd interface-lammps-mlip-2
cp ../mlip-2/lib/lib_mlip_interface.a .

# 在 preinstall.sh 文件结尾添加需安装的 package
make yes-<package>
# 不需要添加 make yes-STUBS
# 可注释 install.sh 脚本中的 make mpi-stubs 命令

# 编译写法
./install.sh <path-to-lammps> <lammps-target>
# 示例
./install.sh ../lammps-29Aug2024 intel_cpu_intelmpi

# 其他 LAMMPS target
g++_mpich
mpi
g++_serial
serial

# 检查
./intel_cpu_intelmpi -h         # Pair styles 会多出 mlip
```



---

## 相关问题

- 用 cmake 编译 MLIP-2 会报错

```bash
/usr/bin/ld: CMakeFiles/mlp.dir/dev_src/mlp/dev_self_test.cpp.o: warning: relocation against `_ZTV20CombinedAnyLocalMLIP' in read-only section `.text._ZN20CombinedAnyLocalMLIPC2EP12AnyLocalMLIPS1_PSo[_ZN20CombinedAnyLocalMLIPC5EP12AnyLocalMLIPS1_PSo]'
/usr/bin/ld: CMakeFiles/mlp.dir/dev_src/mlp/dev_self_test.cpp.o: in function `RunAllTestsDev(bool)':
/home/XXX/opt/mlip-2/dev_src/mlp/dev_self_test.cpp:167: undefined reference to `CombinedAnyLocalMLIP::CalcE(Configuration&)'
/usr/bin/ld: CMakeFiles/mlp.dir/dev_src/mlp/dev_self_test.cpp.o: in function `CombinedAnyLocalMLIP::~CombinedAnyLocalMLIP()':
/home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: undefined reference to `vtable for CombinedAnyLocalMLIP'
/usr/bin/ld: /home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: undefined reference to `vtable for CombinedAnyLocalMLIP'
/usr/bin/ld: /home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: undefined reference to `vtable for CombinedAnyLocalMLIP'
/usr/bin/ld: /home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: undefined reference to `vtable for CombinedAnyLocalMLIP'
/usr/bin/ld: /home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: undefined reference to `vtable for CombinedAnyLocalMLIP'
/usr/bin/ld: CMakeFiles/mlp.dir/dev_src/mlp/dev_self_test.cpp.o:/home/XXX/opt/mlip-2/dev_src/mlp/../combined_any_local_mlip.h:63: more undefined references to `vtable for CombinedAnyLocalMLIP' follow
/usr/bin/ld: warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/mlp.dir/build.make:650: mlp] Error 1
make[1]: *** [CMakeFiles/Makefile2:874: CMakeFiles/mlp.dir/all] Error 2
make: *** [Makefile:146: all] Error 2
```

- 将 MLIP-2 的 LAMMPS 接口用 cmake 编译会报错： [cmake (#14) · Issues · Alexander Shapeev / LAMMPS-MLIP interface · GitLab](https://gitlab.com/ashapeev/interface-lammps-mlip-2/-/issues/14)

```bash
/usr/bin/ld: liblammps.a(pair_MLIP.cpp.o): in function `LAMMPS_NS::PairMLIP::~PairMLIP()':
/home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:67: undefined reference to `MLIP_finalize()'
/usr/bin/ld: liblammps.a(pair_MLIP.cpp.o): in function `LAMMPS_NS::PairMLIP::compute(int, int)':
/home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:85: undefined reference to `MLIP_calc_nbh(int, int*, int*, int**, int, int, double**, int*, double**, double&, double*, double**)'
/usr/bin/ld: /home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:123: undefined reference to `MLIP_calc_cfg(int, double*, double**, int*, int*, double&, double**, double*)'
/usr/bin/ld: liblammps.a(pair_MLIP.cpp.o): in function `LAMMPS_NS::PairMLIP::init_style()':
/home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:211: undefined reference to `MLIP_init(char const*, char const*, int, double&, int&)'
/usr/bin/ld: /home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:209: undefined reference to `MLIP_init(char const*, char const*, int, double&, int&)'
/usr/bin/ld: /home/XXX/opt/lammps-29Aug2024/src/pair_MLIP.cpp:206: undefined reference to `MLIP_finalize()'
collect2: error: ld returned 1 exit status
```

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

- mpi-stubs 放在 intel_cpu_intelmpi 前的作用：平台中若无 MPI 环境，提供一个虚拟的 MPI 库，“欺骗” 需要 MPI 环境的包，使其正常编译；不会对其造成影响（还是建议将其注释掉）

```bash
make mpi-stubs
make intel_cpu_intelmpi -lgfortran
```

- MTP 机器学习势函数没有 GPU 版本
