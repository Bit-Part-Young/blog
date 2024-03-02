---
title: ASE 使用
top: false
cover: false
toc: true
mathjax: true
summary: ASE 使用
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


ipython 按 tab 键可查看有哪些可用 method 或 attributes
在函数或 method 后添加?可以查看其 docstring

示例
```bash
In [1]: from ase.build import bulk

In [2]: bulk?
Signature:
bulk(
    name,
    crystalstructure=None,
    a=None,
    b=None,
    c=None,
    *,
    alpha=None,
    covera=None,
    u=None,
    orthorhombic=False,
    cubic=False,
    basis=None,
)
Docstring:
Creating bulk systems.

Crystal structure and lattice constant(s) will be guessed if not
provided.

name: str
    Chemical symbol or symbols as in 'MgO' or 'NaCl'.
crystalstructure: str
    Must be one of sc, fcc, bcc, tetragonal, bct, hcp, rhombohedral,
    orthorhombic, mlc, diamond, zincblende, rocksalt, cesiumchloride,
    fluorite or wurtzite.
a: float
    Lattice constant.
b: float
    Lattice constant.  If only a and b is given, b will be interpreted
    as c instead.
c: float
    Lattice constant.
alpha: float
    Angle in degrees for rhombohedral lattice.
covera: float
    c/a ratio used for hcp.  Default is ideal ratio: sqrt(8/3).
u: float
    Internal coordinate for Wurtzite structure.
orthorhombic: bool
    Construct orthorhombic unit cell instead of primitive cell
    which is the default.
cubic: bool
    Construct cubic unit cell if possible.
File:      ~/src/miniconda3/envs/base_ysl/lib/python3.11/site-packages/ase/build/bulk.py
Type:      function

```


nglview，可用在 jupyter notebook 中查看生成的构型
```bash
# 安装
pip install nglview
```


```python
from ase.visualize import view
from ase.io import read

structure_fn = "XXX.vasp"
structure = read(structure_fn, format="vasp")

view(structure, viewer="ngl")
```

效果图：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401201143207.png)



```bash
# 列出 ASE 可识别的构型文件格式
ase info --formats

# 列出 ASE 的 calculators 以及是否被安装
ase info --calculators
```


---

### 参考资料

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


ase 对称性 tutorial
>[Crystal symmetry and spglib | ase-tutorial-symmetry](https://ajjackson.github.io/ase-tutorial-symmetry/)

>[GitHub - ajjackson/ase-tutorial-symmetry: Tutorial notebook for symmetry features in ASE](https://github.com/ajjackson/ase-tutorial-symmetry)


表面吸附、EOS、弹性常数计算（ASE 中无计算弹性常数的模块和类）
>[GitHub - jochym/Elastic: A module for ASE for elastic constants calculation.](https://github.com/jochym/Elastic)

>[Calculation of elastic properties of crystals — Elastic v5.1.0 documentation](https://elastic.readthedocs.io/en/stable/)



---

## 安装

安装
```bash
pip install ase
```

测试
```bash
ase test

# 需要安装 pytest package
pip install pytest
```



---

## 常用模块

### ase.atoms

>[The Atoms object — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/atoms.html#module-ase.atoms)

- attribute -
- `get_XXX()` method -
- `set_XXX()` method -


```python
from ase.atoms import Atoms
from ase.formula import Formula

ats: Atoms
# 化学式
conf_symbol = ats.get_chemical_formula()
# 成分
struct_composition = Formula(conf_symbol).count()
# 原子数
natom = len(ats)
# 元素数
nele = len(set(ats.get_chemical_symbols()))
```


Atoms object 常用 method 和 attribute 示例代码

```python
from ase.io import read

struct_fn = "Nb5Si3_alpha.vasp"
struct = read(filename=struct_fn, format="vasp")

print("Total number of atoms:")
print(len(struct))
print(struct.get_global_number_of_atoms())
print("---" * 25)

print("Atomic symbols:")
print(list(struct.symbols))
print(struct.get_chemical_symbols())
print("---" * 25)

print("Chemical formula:")
print(struct.symbols)
print(struct.get_chemical_formula())
print("---" * 25)

print("Atomic numbers:")
print(struct.numbers)
print(struct.get_atomic_numbers())
print("---" * 25)

print("Structure cell:")
print(struct.cell)
print(struct.get_cell())
print("---" * 25)

print("Structure cell parameters:")
print(struct.cell.cellpar())
# deprecated 写法
# print(struct.get_cell_lengths_and_angles())
print("---" * 25)

print("Structure volume:")
print(struct.get_volume())
print("---" * 25)

print("Structure mass:")
print(struct.get_masses())
print("---" * 25)

print("Structure positions:")
print(struct.positions)
print(struct.get_positions())
print("---" * 25)

print("Structure pbc condition:")
print(struct.pbc)
print(struct.get_pbc())
print("---" * 25)

print(struct.todict())
```


---

### ase.build

#### bulk

>[Building things — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/build/build.html#module-ase.build)

简单 bulk 模型构建 示例代码

```python
from ase.build import bulk
from ase.io import write

# 原胞
primCell = bulk(name="Al", crystalstructure="fcc", a=4.05)
# 单胞
unitCell = bulk(name="Al", crystalstructure="fcc", a=4.05, cubic=True)
# 超胞
superCell = unitCell * (2, 2, 2)
# 构型原子数
print(len(primCell))
print(superCell.get_global_number_of_atoms())

# 保存成 VASP 格式文件
write(filename="Al222.vasp", images=superCell, format="vasp", direct=True)
```

---

简单 bulk 模型的表面构建 示例代码

```python

```


---

将 ASE 生成的 bulk 的原胞形式转换成单胞
```python
from spglib import standardize_cell

lattice, positions, numbers = standardize_cell(cell=Atoms, to_primitive=False)
# lattice返回的是三个基矢的np.array格式

lattice_constant = lattice[0][0]
```


---

#### surface

WIP…



---

### ase.io

文件读入、写出

ase 中可识别的文件格式（部分文件格式只有 `read` 或 `write` 相关的一个函数）
>[File input and output — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/io/io.html)

---

写法一：在 `write()` 函数中的 `format` 参数指定文件格式

```python
from ase.io import read, write

struct = ...
write(filename=struct, images=..., format=...)
```

---

写法二：从 `ase.io` 中导入具体格式的模块及其函数

```python
# LAMMPS data 格式
from ase.io.lammpsdata import read_lammps_data, write_lammps_data
# vasp 格式
from ase.io.vasp import read_vasp, write_vasp
# material studio xsd 格式
from ase.io.xsd import read_xsd, write_xsd
# VASP 输出文件格式
from ase.io.vasp import read_vasp_out

struct = ...
write_vasp(filename=..., atoms=struct)
```

---

ASE io 模块 文件格式转换 示例代码

```python
from ase.io import read, write
from ase.io.extxyz import write_xyz
from ase.io.lammpsdata import write_lammps_data
from ase.io.vasp import read_vasp, write_vasp

struct_fn = "Nb5Si3_alpha.vasp"
struct = read(filename=struct_fn, format="vasp")

output_vasp_fn = "POSCAR"
write_vasp(filename=output_vasp_fn, atoms=struct, direct=True, sort=True)

output_xyz_fn = "Nb5Si3_alpha.xyz"
output_extxyz_fn = "Nb5Si3_alpha_ext.xyz"
write(filename=output_xyz_fn, images=struct, format="xyz")
write(filename=output_extxyz_fn, images=struct, format="extxyz")
write_xyz(fileobj=output_extxyz_fn, images=struct)

ele_list = ["Nb", "Si"]
output_lammps_data_fn = "Nb5Si3_alpha.lammps-data"
write_lammps_data(
    file=output_lammps_data_fn,
    atoms=struct,
	# 指定 atom type 顺序
	specorder=ele_list,
    units="metal",
    atom_style="atomic",
)
```


lammps atom type 如何进行指定排序？
`write_lammps_data()` 的 `specorder` 参数


---

VASP OUTCAR 文件转换为 extxyz 文件 代码示例
>[Convert VASP OUTCAR to extxyz file for NequIP input · GitHub](https://gist.github.com/simonbatzner/c2b05d38789b67f6fe5d3c75a4f2223d)

```python
"""可获取 OUTCAR 中的所有离子步构型的原子位置、能量、受力、应力等信息"""

from ase.io import read, write

vasp_out_fn = "./OUTCAR"
extxyz_fn = "outcar.xyz"

all_confs = read(filename=vasp_out_fn, format="vasp-out", index=":")
print(len(all_confs))

write(filename=extxyz_fn, images=all_confs, format="extxyz", append=True)
```


---

ASE Atoms object 与 pymatgen Structure object 互相转换 示例代码

```python

from ase.build import bulk
from pymatgen.core.structure import Structure
from pymatgen.io.ase import AseAtomsAdaptor

atoms = bulk("Fe", "bcc", a=2.83, cubic=True)
structure = AseAtomsAdaptor.get_structure(atoms)

print("ASE Atoms object transfer to pymatgen Structure object:\n")
print(atoms)
print("---" * 20)
print(structure)
print("\n" + "---" * 20 + "\n")

print("pymatgen Structure object transfer to ASE Atoms object :\n")
structure_pmg = Structure.from_prototype(prototype="fcc", species=["Al"], a=4.05)
structure_ase = AseAtomsAdaptor.get_atoms(structure_pmg)

print(structure_pmg)
print("---" * 20)
print(structure_ase)
```


---

### ase.eos

获取平衡体积，能量和体模量

```python
EquationOfState
```



---

### ase.db

脚本形式（常用）

```python
from ase.db import connect

db_fn = "..."
db = connect(db_fn)

# 获取 db 文件里的结构数目
print(len(db))
print(db.count())
# 添加 selection
print(db.count("vasp_calc=Yes"))

# 筛选 id<=5 的所有结构
# selection 可以是 id 或其他 AtomsRow 中的 key
# 注：中间不能有空格
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

```python
from ase.db.row import AtomsRow
```



---

命令行形式（个人不常用）

```shell
ase build -h

# 构建单个元素的 json 文件
ase build -x fcc Ag

# 转换成 db 数据库
ase convert Ag.json Pd.json database.db

# 查看 db 数据库
ase db database.db
# 查看某个元素的内容
ase db database.db Ag
# 查看某个元素的全部信息
ase db database.db Ag -l
```

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
