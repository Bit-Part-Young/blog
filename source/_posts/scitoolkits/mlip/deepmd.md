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

## 介绍

- [GitHub - deepmodeling/deepmd-kit: A deep learning package for many-body potential energy representation and molecular dynamics](https://github.com/deepmodeling/deepmd-kit)

- [GitHub - deepmodeling/dpgen: The deep potential generator to generate a deep-learning based model of interatomic potential energy and force field](https://github.com/deepmodeling/dpgen)

- [GitHub - deepmodeling/dpdata: A Python package for manipulating atomistic data of software in computational science](https://github.com/deepmodeling/dpdata)

- [已停止维护 - DP library](https://dplibrary.deepmd.net/)

[DeePMD 使用教程、科研案例、问题收集合集 - Bohrium](https://bohrium.dp.tech/notebooks/5515485653)


使用深度神经网络构建势函数

版本：初始版本（v0）、v1、v2


DP library：DP 模型数据库（类似 Material Project）

exploration、labeling、train 三个过程



描述符

```bash
sel_a

se_e2_r
se_e3
se_atten
```

模型压缩


---

### 实例

- [GitHub - kul-group/Ag\_diffusion\_data: Data and inputs for surface diffusion on Ag (111)](https://github.com/kul-group/Ag_diffusion_data)

- [ABACUS+DPGEN+DeePMD+LAMMPS 铜掺杂铍晶体DP势函数拟合过程演示----初版教程 - 飞书云文档](https://ucoyxk075n.feishu.cn/docx/BOtFdzj03o2GXkxYng7cu2Xnnje)

- [一个DeepMD完整例子：water - Eastsheng's Wiki](https://eastsheng.github.io/MyWiki/wiki/2024/10/10/softwares/deepmd/DeepMD_2/)



---

## 安装

### DeePMD-kit

含 CPU 和 GPU 版本

```text

```


---

### dpgen

```bash
# PyPI 安装
pip install dpgen
# Conda 安装
conda install -c conda-forge dpgen
# 源码安装
git clone https://github.com/deepmodeling/dpgen && pip install ./dpgen
```


---

### dpdata

```bash
pip install dpdata
```


---

## 使用

### DeePMD-kit

训练

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202411201630028.png)

训练数据中必要的信息：


```bash
# 训练集数据结构
training_data
├── set.000
│   ├── box.npy
│   ├── coord.npy
│   ├── energy.npy
│   ├── force.npy
│   └── virial.npy
├── type.raw
└── type_map.raw


coord.npy      # 体系的结构文件
type.raw       # 体系的结构文件对应的元素标记
energy.npy     # 体系的结构文件对应的能量
force.npy      # 体系的结构文件对应的力
box.npy        # 体系的结构文件对应的晶胞大小，如果是非周期性体系，请在训练文件里准备一个超大周期边界条件


```


- 模型训练参数

```json
"model":{
    "type_map":    ["H", "C"],                 
    "descriptor":{
        "type":            "se_e2_a",          
        "rcut":            6.00,               
        "rcut_smth":       0.50,               
        "sel":             "auto",             
        "neuron":          [25, 50, 100],       
        "resnet_dt":       false,
        "axis_neuron":     16,                  
        "seed":            1,
        "_comment":        "that's all"
        },
    "fitting_net":{
        "neuron":          [240, 240, 240],    
        "resnet_dt":       true,
        "seed":            1,
        "_comment":        "that's all"
    },
    "_comment":    "that's all"'
},
```

```bash
# 开始训练
dp train input.json
# 重启训练
dp train input.json --restart model.ckpt

train.log           # 训练记录文件
lcurve.out          # 学习曲线



# 提取经过训练的神经网络模型，生成冻结模型 graph.pb
dp freeze -o graph.pb
# 压缩
dp compress -i graph.pb -o graph-compress.pb

# 检查势函数模型
dp test -m graph.pb -s ...
```


---

### dpgen

构建训练集、训练

同步学习

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202411201641080.png)


autoset 功能

使用 DeePMD-kit 同时训练参数初始化不同的 4 个势函数


```bash

# dpgen 命令
init_bulk
init_surf
run

dpgen sub-command PARAM MACHINE
# 参数
PARAM              # 输入参数文件
MACHINE            # 机器配置文件


dpgen.log           # 
```



mdapy 库可生成微扰结构

```python
import mdapy as mp

mp.init()

pert = mp.PerturbModel()
```

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


```bash


disp_freq

```


---

### dpdata

dpdata：将多种构型文件格式转换成 deepmd 格式（转换成其他格式的功能一般）




```python
import dpdata

dpdata.LabeledSystem('OUTCAR').to()


# 预测数据和原始数据之间的比较
training_systems = dpdata.LabeledSystem()
predict = training_systems.predict("graph.pb")

training_systems["energies"]
predict["energies"]
```


---

### 势函数使用

```bash
pair_style  deepmd graph.pb
pair_coeff  * *
```
