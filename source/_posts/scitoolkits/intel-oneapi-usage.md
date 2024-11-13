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

- 参考：[安装 Intel® oneAPI Base Toolkit 和 Intel® oneAPI HPC](https://blog.csdn.net/weixin_42487488/article/details/115066980)

- Intel oneAPI 暂不支持 Arch Linux

- Intel-oneAPI 中的 FFTW、BLAS、LAPACK 和 SCALAPACK 相关路径

```bash
${MKLROOT}/include/fftw    # FFTW
${MKLROOT}/lib/intel64     # BLACS、LAPACK 和 SCALAPACK
```

- Intel oneAPI 在官网只能下载最新版本；官网未对 Ubuntu23.04 进行测试；旧版下载：[Intel](https://get.hpc.dev/vault/intel/?sort=name&order=desc)

- Intel-oneAPI 2024 版开始没有了 icc 和 icpc

- Intel® oneAPI Base Toolkit 2024 版包含的东西

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

- Intel® oneAPI HPC Toolkit 2024 版包含的东西（缺少 C++ Compiler Classic）

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

# 将以下命令添加到 ~/.bashrc 或 ~/.zshrc 中
# 使得登录开启 Intel oneAPI 环境
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
```

- Intel oneAPI 卸载：[Uninstall oneAPI Toolkits and Components](https://www.intel.com/content/www/us/en/docs/oneapi/installation-guide-linux/2023-1/uninstall-oneapi-toolkits-and-components.html)

```bash
cd /opt/intel/oneapi/installer
sudo ./installer
```
