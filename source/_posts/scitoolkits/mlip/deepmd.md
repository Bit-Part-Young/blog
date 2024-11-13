---
title: deepmd 使用
top: true
cover:
toc: true
mathjax: true
summary: deepmd 使用
description: deepmd 使用
tags:
  - deepmodeling
  - 势函数拟合
categories:
  - 科研工具
date: 2023-07-03 15:56:30
abbrlink: 650351
password:
---

# deepmd 使用

[DPMD - Deep Potential Molecular Dynamics-Prepare Dataset](https://mp.weixin.qq.com/s/-2gEpNmOjgNUhwCYsmEkUg)

机器学习势预测精度用 MAE 评估

[Deepmd-kit & DPGEN 使用笔记](https://zhuanlan.zhihu.com/p/362073474)

离线安装

给离线安装的 conda 环境添加环境名

```bash
ln -s ~/src/deepmd-kit ~/src/miniconda3/envs/<new_env_name>
```


```bash
deepmd-kit will now be installed into this location:
/home/yangsl/deepmd-kit

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/yangsl/deepmd-kit] >>> $HOME/src/deepmd-kit
PREFIX=/home/yangsl/src/deepmd-kit
Unpacking payload ...
Notes:
The off-line packages and conda packages require the GNU C Library 2.17 or above[1]. The GPU version requires compatible NVIDIA driver to be installed in advance[2]. It is possible to force conda to override detection when installation[3] (such as CONDA_OVERRIDE_CUDA), but these requirements are still necessary during runtime.

[1] The GNU C Library. https://www.gnu.org/software/libc/
[2] Minor Version Compatibility. NVIDIA Data Center GPU Driver Documentation. https://docs.nvidia.com/deploy/cuda-compatibility/index.html#minor-version-compatibility
[3] Overriding detected packages. conda documentation. https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-virtual.html#overriding-detected-packages


Installing base environment...


Downloading and Extracting Packages


Downloading and Extracting Packages

Preparing transaction: done
Executing transaction: done
Please activate the environment before using the packages:

source /path/to/deepmd-kit/bin/activate /path/to/deepmd-kit

The following executable files have been installed:
1. DeePMD-kit CLi: dp -h
2. LAMMPS: lmp -h
3. DeePMD-kit i-Pi interface: dp_ipi
4. MPICH: mpirun -h
5. Horovod: horovod -h

The following Python libraries have been installed:
1. deepmd
2. dpdata
3. pylammps

If you have any questions, seek help from https://github.com/deepmodeling/deepmd-kit/discussions
```

---


这两个 raw 文件内容对训练是否会有影响？


通配符获取 outcar deepmd 数据，能量顺序不是按第 1-4 步来的


默认 240

将 ICET 的 data 转换成 deepmd 格式

water se_e2_a 80\*3 训练集 80 测试集 type.new 192 行



---


dpdata：将多种构型文件格式转换成 deepmd 格式（转换成其他格式的功能一般）

[GitHub - deepmodeling/dpdata: Manipulating multiple atomic simulation data formats, including DeePMD-kit, VASP, LAMMPS, ABACUS, etc.](https://github.com/deepmodeling/dpdata)
