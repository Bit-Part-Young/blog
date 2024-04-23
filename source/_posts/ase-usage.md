---
title: ASE 使用
top: false
cover:
toc: true
mathjax: true
summary: ASE 使用
description: ASE 使用
tags:
  - ASE
categories:
  - 科研工具
date: 2023-10-15 09:00:00
abbrlink: 19935
password:
---

# ASE 使用

## 介绍

atomic simulation environment (ASE)


```python
from ase.atoms import Atoms
from ase.calculators.singlepoint import SinglePointCalculator

results={"energy": -7.0}
atoms.calc = SinglePointCalculator(atoms, **results)
atoms.get_potential_energy()
```

ipython 按 tab 键可补全可用 method 或 attributes
在函数或 method 后添加?可以查看其 docstring

示例
```bash
In [1]: from ase.build import bulk

In [2]: bulk?
```


```python
# ase rdf 计算
from ase.geometry.analysis import Analysis

ana = Analysis(images=...)
rdf = ana.get_rdf()
```


ase 缺陷计算 寻找最优的超胞形状
>[Tools for defect calculations — ASE documentation](https://wiki.fysik.dtu.dk/ase/tutorials/defects/defects.html#supercell-creation)


---

### 参考资料

ase 教程（内容较详细）
>[ASE tutorials](https://ase-workshop-2023.github.io/tutorial/)

>[GitHub - PythonFZ/ase\_md\_example](https://github.com/PythonFZ/ase_md_example)


ase tutorial
>[ASE\_tutorial.ipynb](https://github.com/chenggroup/new-comer-tutorial/blob/master/python/ase/ASE_tutorial.ipynb)


基于 PAW 和 ASE 的 DFT code
>[GPAW: DFT and beyond within the projector-augmented wave method — GPAW](https://wiki.fysik.dtu.dk/gpaw/)


ase 相关脚本案例
>[GitHub - AlexBoucherr/ASExVASP: A serie of script to perform calculations on VASP using the ASE](https://github.com/AlexBoucherr/ASExVASP)

>[GitHub - jkitchin/dft-book: A book on modeling materials using VASP, ase and vasp](https://github.com/jkitchin/dft-book)


ase 结构 2D 和 3D 渲染
>[GitHub - chrisjsewell/ase-notebook: Highly configurable 2D (SVG) & 3D (threejs) visualisations for ASE/Pymatgen structures, within the Jupyter Notebook.](https://github.com/chrisjsewell/ase-notebook)

>[GitHub - superstar54/x3dase: X3D for Atomic Simulation Environment](https://github.com/superstar54/x3dase)


ase.lattice 有生成 graphene 和 graphite modules
>[ase/lattice/hexagonal.py · master · ase / ase · GitLab](https://gitlab.com/ase/ase/-/blob/master/ase/lattice/hexagonal.py)

>[Bravais lattices — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/lattice.html)


ase symmetry 教程（内容一般）
>[GitHub - ajjackson/ase-tutorial-symmetry: Tutorial notebook for symmetry features in ASE](https://github.com/ajjackson/ase-tutorial-symmetry)


表面吸附、EOS、弹性常数计算（ASE 中无计算弹性常数的模块和类）
>[GitHub - jochym/Elastic: A module for ASE for elastic constants calculation.](https://github.com/jochym/Elastic)

>[Calculation of elastic properties of crystals — Elastic v5.1.0 documentation](https://elastic.readthedocs.io/en/stable/)

---


```python
from ase.cell import Cell

# cell 参数转换成 cell matrix
cell = Cell.fromcellpar([3.31, 3.31, 3.31, 90, 90, 90])
cell[:]
```

---

构型可视化

```python
# 方式 1
from ase.visualize.plot import plot_atoms

plot_atoms(atoms)

# 方式 2
from ase.visualize import view

view(atoms, viewer="ngl")
```

nglview，可在 jupyter notebook 中可视化构型
```bash
pip install nglview
```


nglview 效果图：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401201143207.png)

---

crystal 构建

```python
# 方式 1；最简单
from ase.build import bulk

# 方式 2
from ase.atoms import Atoms

# 方式 3
from ase.spacegroup import crystal
```


```python
from ase.spacegroup import Spacegroup

spg = Spacegroup(152)

# 查看等同原子坐标
spg.equivalent_sites([0.4673, 0, 0.3333])
```


超胞

```python
# 方式 1
supercell = atoms * (2, 2, 2)
```


---

## 安装

安装
```bash
pip install ase
```

测试
```bash
ase test

# 需安装 pytest
pip install pytest
```



`db.select(sort)` 中的 `sort` 为 含 key 的 str，含 `-` 时，降序

---

## 常用模块

### ase.atoms

>[The Atoms object — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/atoms.html#module-ase.atoms)

- 属性 -
- 方法
- `get_XXX()` method -
- `set_XXX()` method -


```python
from ase.atoms import Atoms
from ase.formula import Formula

ats: Atoms
# 化学式
conf_symbol = ats.get_chemical_formula()
# 成分 {'Al': 5, 'Ti': 1}
struct_composition = Formula(conf_symbol).count()
# 原子数
natom = len(ats)
# 元素数
nele = len(set(ats.get_chemical_symbols()))
```


---

### ase.build

#### bulk

>[Building things — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/build/build.html#module-ase.build)


简单 bulk 模型构建 示例代码

```python
from ase.build import bulk

# 原胞
primCell = bulk("Al", "fcc", a=4.05)
# 单胞
unitCell = bulk("Al", "fcc", a=4.05, cubic=True)
# 超胞
superCell = unitCell * (2, 2, 2)
```

---

简单 bulk 模型的表面构建 示例代码

```python
# WIP
```

---

#### surface

WIP…



---

### ase.io

- 构型格式文件读入、写出
- 函数 `read()` 可自动识别文件格式；ase 中可识别的文件格式（部分格式只有 `read` 或 `write` 一个函数）：[File input and output — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/io/io.html)
- 可以读取 gz 格式压缩文件，如 OUTCAR.gz

---

写法一：在 `write()` 函数中的 `format` 参数指定文件格式

```python
from ase.io import read, write

write(filename=..., images=..., format=...)
```

---

写法二：从 `ase.io` 中导入具体格式的模块及其函数

```python
# LAMMPS data 格式
from ase.io.lammpsdata import read_lammps_data, write_lammps_data

# vasp 格式
from ase.io.vasp import read_vasp, write_vasp

# VASP 输出文件格式
from ase.io.vasp import read_vasp_out

# material studio xsd 格式
from ase.io.xsd import read_xsd, write_xsd
```


`extxyz.py` 源代码相关 warning：

```bash
/home/yangsl/src/miniconda3/envs/base_ysl/lib/python3.11/site-packages/ase/io/extxyz.py:1000: UserWarning: write_xyz() overwriting array "forces" present in atoms.arrays with stored results from calculator
  warnings.warn('write_xyz() overwriting array "{0}" present '
```



---

### ase.eos

获取平衡体积，能量和体模量

```python
from ase.eos import EquationOfState
from ase.units import kJ

# murnaghan birch vinet
eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()
print(f"v0 = {v0:.3f}")
print(f"e0 = {e0:.3f}")
print(f"B = {B / kJ * 1.0e24:.1f} GPa") 

ax = eos.plot()
ax.set_title(label=None)
```



---

### ase.db

```python
from ase.db import connect
from ase.db.row import AtomsRow

db_fn = "..."
db = connect(db_fn)

# 给 db 添加元数据
db.metadata = {...}

# 获取 db 文件里的结构数目
print(len(db))
print(db.count())
# 添加 selection
print(db.count("vasp_calc=Yes"))

# 筛选 id<=5 的所有结构
# selection 可以是 id 或其他 AtomsRow 中的 key
# 注：字符与符号之间不能有空格
for row in db.select("id<=5"):
	...

# 筛选 id>=5, id<=10 的所有结构
for row in db.select("id>=5, id<=10"):
	...

# 单个 AtomsRow
# id 从 1 开始
row = db.get(id=10)
# 获取 AtomsRow 的 keys
print(row._keys)
# 获取 AtomsRow 的 key_value_pairs
print(row.key_value_pairs)
# 根据 key 获取 value
print(row.vasp_calc)

# 单个 Atoms
atoms_specific = db.get_atoms(id=10)

# 将 db 中的 AtomsRow 的结构和数据写入到其他 db 文件
db_output_fn = "..."
db_output = connect(db_output_fn)

for row in db.select("id<=10"):
    key_value_pairs = row.key_value_pairs
    data = row.data
	# 将 AtomsRow 转化成 Atoms
    atoms = row.toatoms()
    db_output.write(atoms=atoms, key_value_pairs=key_value_pairs, data=data)
```


---

### ase cli tool

>[Command line tool — ASE documentation](https://wiki.fysik.dtu.dk/ase/cmdline.html)

开启 ase 补全（zsh 不行）

```bash
ase completion >> ~/.bashrc
```


```bash
# 列出 ase 可识别的构型文件格式
ase info --formats
# 列出 ase 的 calculators 以及是否被安装
ase info --calculators

# 构型转换
ase convert -i vasp -o extxyz -f -v POSCAR structure.xyz
```

```bash
# 查看 db 文件内容 推荐
ase db test.db

-L N                         # 只显示前 N 行
--offset N                   # 跳过前 N 行
--show-keys                  # 显示所有 keys
--show-values key1,key2,...  # 显示 key 的值；value为数值时，只显示首尾值，如 energy_pa: [-9.18438289..-5.855563642]
```


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404111050491.png)





---

### ase.calculators

>[VASP — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/calculators/vasp.html)

```python
ase.calculators.vasp.Vasp
```

在 Pi 中用 ASE 的 VASP 的 Calculator

申请节点运算（不写提交脚本）

- `srun -p small -n 4 --pty /bin/bash`

---

- `~/.bashrc` 文件添加内容

```bash
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
export I_MPI_FABRICS=shm:ofi

export ASE_VASP_COMMAND="srun --mpi=pmi2 /lustre/home/acct-mseklt/mseklt/yangsl/bin/vasp_std"
```

---

```bash
python *.py
```

写提交脚本

- `~/.bashrc` 文件添加内容

```bash
export ASE_VASP_COMMAND="srun --mpi=pmi2 /lustre/home/acct-mseklt/mseklt/yangsl/bin/vasp_std"
```

---

- `submit_ase.slurm` 脚本

```bash
#!/bin/bash

#SBATCH -J vasp
#SBATCH -p small
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
export I_MPI_FABRICS=shm:ofi

python python-file-name.py
```

---

- `sbatch submit_ase.slurm`

在思源中用 ASE 的 VASP 的 Calculator

- 提交脚本（`ase-submit-sy.slurm`）

```bash
#!/bin/bash

#SBATCH -J ase
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --exclusive
#SBATCH -o %j.out
#SBATCH -e %j.err

module load vasp/5.4.4-intel-2021.4.0

ulimit -s unlimited

python python-file-name.py
```
