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

# DeepMD 使用

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

[learning/notes/DeePMD/DeePMD-kit安装.md at main · wangchr1617/learning · GitHub](https://github.com/wangchr1617/learning/blob/main/notes/DeePMD/DeePMD-kit%E5%AE%89%E8%A3%85.md)

[learning/notes/DeePMD/DeePMD-kit入门.md at main · wangchr1617/learning · GitHub](https://github.com/wangchr1617/learning/blob/main/notes/DeePMD/DeePMD-kit%E5%85%A5%E9%97%A8.md)

DeepMD ASE calculator

```python
from deepmd.calculator import DP

calc = DP(model=...)

atoms.calc = calc

energy = atoms.get_potential_energy()
forces = atoms.get_forces()
stress = atoms.get_stress()
```

描述符

```bash
sel_a

se_e2_a
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


# dpdata
pip install -U dpdata
```



---

## 使用

### 工具

- 生成 Deep Potential：[GitHub - hsulab/GDPy: Generating Deep Potential with Python](https://github.com/hsulab/GDPy)

[机器学习力场训练集可视化 - 知乎](https://zhuanlan.zhihu.com/p/677527443)

```python
from deepmd.infer import DeepPot

dp = DeepPot(args.model)

# 获取 DP 描述符
descriptor = dp.eval_descriptor()

dp.eval()
```



---

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


coord.npy      # 原子坐标
type.raw       # 元素种类
energy.npy     # 体系能量
force.npy      # 原子受力
box.npy        # 模拟盒子，若为非周期性体系，请在训练文件里准备一个超大周期边界条件

virial.raw     # 维里应力
```


- 模型训练参数

```bash
model
learning_rate
loss
training
```

- 示例

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

- dpdata：将多种构型文件格式转换成 deepmd 格式（转换成其他格式的功能一般）

```python
import dpdata

d_outcar = dpdata.LabeledSystem("OUTCAR", fmt="vasp/outcar")

d_outcar["energies"]
d_outcar["forces"]
d_outcar["virials"]

d_outcar.get_nframes()
d_outcar.get_natoms()

# keys；无 stress key
atom_names
atom_numbs
atoms_types
cells                    # 获取的是 VOLUME and BASIS
coords
energies                 # 获取的是 free  energy   TOTEN 
forces
virials                  # 获取的是 FORCE on cell =-STRESS in cart. coord.  units 中的 Total


dpdata.LabeledSystem('OUTCAR').to()


# 预测数据和原始数据之间的比较
training_systems = dpdata.LabeledSystem()
predict = training_systems.predict("graph.pb")

training_systems["energies"]
predict["energies"]
```

- 扰动（点阵 + 原子位置）：
    - [tools/create-perturb.py at main · tang070205/tools · GitHub](https://github.com/tang070205/tools/blob/main/create-perturb.py)
    - [GPUMDkit/Scripts/sample\_structures/perturb\_structure.py at main · zhyan0603/GPUMDkit · GitHub](https://github.com/zhyan0603/GPUMDkit/blob/main/Scripts/sample_structures/perturb_structure.py)

```python
import dpdata

pert_num = 2
perturbed_system = dpdata.System("POSCAR").perturb(
    pert_num=pert_num,
    cell_pert_fraction=0.03,
    atom_pert_distance=0.01,
    atom_pert_style="uniform",
    atom_pert_prob=1.0,
)

for i in range(pert_num):
    # 方式 1
    perturbed_system.to(
        "vasp/poscar",
        f"pert/POSCAR.{i}",
        frame_idx=i,
    )
    # 方式 2
    perturbed_system.sub_system(i).to(
        "vasp/poscar",
        f"pert/POSCAR.{i}",
    )


# 参数
pert_num                     # 每帧构型生成扰动新构型的数目
cell_pert_fraction           # cell 变形比例；对角线 [-x, +x] 均匀分布扰动，非对角线 [-0.5x, +0.5x] 均匀分布扰动
atom_pert_distance           # 原子移/扰动距离
atom_pert_style              # 原子移/扰动距离的分布；normal uniform const
atom_pert_prob               # 每帧构型中要扰动的原子数目比例
```

---

### 势函数使用

[1.4. Install LAMMPS — DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/r2/install/install-lammps.html)

[1.2. Install from source code — DeePMD-kit documentation](https://docs.deepmodeling.com/projects/deepmd/en/r2/install/install-from-source.html#install-the-c-interface)


DeePMD 与 LAMMPS 的接口

先安装 DeePMD-kit 的 C++ 接口

```bash
cd $deepmd_source_dir/source
mkdir build
cd build

cmake -DUSE_TF_PYTHON_LIBS=TRUE -DCMAKE_INSTALL_PREFIX=$deepmd_root ..
```

```bash
cd $deepmd_source_dir/source/build
make lammps          # 生成 USER-DEEPMD module


cp -r $deepmd_source_dir/source/build/USER-DEEPMD path_lammps/src

# 安装 deempd package
make yes-extra-fix
make yes-user-deepmd
```

```bash
pair_style  deepmd graph.pb
pair_coeff  * *
```
