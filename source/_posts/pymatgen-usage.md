---
title: pymatgen 安装与使用
top: false
cover: 
toc: true
mathjax: true
summary: pymatgen 安装与使用
description: pymatgen 安装与使用
tags:
  - pymatgen
  - python
categories:
  - 科研工具
abbrlink: "12496"
password:
---

# pymatgen 安装与使用

## 介绍

material project workshop
2021：[The Materials Project Workshop](https://workshop.materialsproject.org/)

2018~2020：[Releases · materialsproject/workshop](https://github.com/materialsproject/workshop/releases)

2017：[GitHub - materialsproject/workshop-2017: Assets for the 2017 Materials Project workshop](https://github.com/materialsproject/workshop-2017)

2016：[GitHub - materialsproject/workshop-2016: Assets for the Materials Project workshop in Aug 2016](https://github.com/materialsproject/workshop-2016)



该网址包含了 pymatgen 在材料相关计算中用的具体参数及其说明：如，截断能为 520eV 是由元素周期表所有元素中最大截断能的 1.3 倍得到的
>[Materials Methodology - Materials Project Documentation](https://docs.materialsproject.org/methodology/materials-methodology)



复杂结构 pymatgen 无法将其单胞转化成原胞（Al3Ni）


mp-api：mp 的新 api；[https://docs.materialsproject.org/downloading-data/using-the-api/getting-started](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)



pymatgen.io.vasp.outputs Outcar 类有 read_neb() 函数


- [ ] pymatgen tool（不是很好用）
>[GitHub - haidi-ustc/maptools: A open source program for materials simulation data process, which is mainly based on Pymatgen code](https://github.com/haidi-ustc/maptools)


解析 VASP 输出文件目录
>[Automated DFT - The Materials Project Workshop](https://workshop.materialsproject.org/lessons/05_automated_dft/Lesson/#parsing-directories-with-atomate-drones)

```python
from atomate.vasp.drones import VaspDrone

drone = VaspDrone()
task_doc = drone.assimilate(path="./example_VASP_Al16Cr10")

print(task_doc.keys())
```



基于之间的 VASP 计算目录中生成静态计算输入文件
```python
from pymatgen.io.vasp.sets import MPStaticSet

# from_prev_calc为静态方法
static_set = MPStaticSet.from_prev_calc("./VASP_Al16Cr10_example/")

print(static_set.incar)
```



workshop2020 中对 DFT 的介绍：

- DFT is an atomistic method. This means it needs approximate positions of atoms and approximate lattice parameters to perform a calculation.

- DFT is a first-principles method. This means that it uses a minimum of empirical information, so it can handle unusual systems well, including materials that have never been synthesized! It scales well to several hundred atoms, but beyond that other methods need to be used.

- However, DFT does still need some form of correction. The particular type of DFT used in Materials Project (GGA/PBE) systematically under-binds materials, meaning that bond lengths (and hence lattice parameters) are systematically larger than expected by 1-2%. This also results in a systematic error in our formation energies, but we can fix this systematic error by fitting our calculated data to experimental formation enthalpies.

- DFT is a ground-state, 0 K method. It can calculate ground state properties well such as bulk modulus, along with electronic structure information (the shape of your band structures, for example) but it is notably bad at calculating excited states including band gaps, and systematically under-estimates band gaps by a large margin. For this reason, any screening based on band gap has to include a large safety margin of ~0.5 eV.







- [x] pymatgen structure 如何通过 structure 来生成 potcar？
解决方法：通过 Poscar 类得到 structure 的元素种类，之后与 PBE 泛函的元素进行比对，之后用 Potcar 类写入 POTCAR（生成新的之前需删掉原来的 POTCAR 文件）


Structure 类相关属性和方法
```python
remove_species()
replace_species()

num_sites 
formula 
compsition
```






MPStaticSet 有设置 EDIFF 10-4

没有 MPStaticSet.yaml

reciprocal_density=100


```text
pymatgen中的HCP结构单胞的原子位置有些奇怪

Structure Summary 
Lattice abc : 3.234 3.234 5.168 
angles : 90.0 90.0 119.99999999999999 
volume : 46.80941006909575 
A : 3.234 0.0 1.98025387422127e-16 
B : -1.616999999999999 2.800726155838875 1.98025387422127e-16 
C : 0.0 0.0 5.168 
pbc : True True True 
PeriodicSite: Zr (1.6170, 0.9336, 3.8760) [0.6667, 0.3333, 0.7500] 
PeriodicSite: Zr (-0.0000, 1.8672, 1.2920) [0.3333, 0.6667, 0.2500]

相当于沿(-1/3,1/3,-1/4)进行了平移

FCC、六方和面心正交晶体结构只能用Gamma网格

Kpoints.automatic_density_by_vol() reciprocal_density Kpoints.automatic_density() grid_density Kpoints.automatic() length

MPRelaxSet继承的DictSet类，DictSet类继承的VaspInputSet类 MPRelaxSet中的K点生成方式是Kpoints.automatic_density_by_vol() ISMEAR=-5 SIGMA=0.05 io/vasp/MPRelaxSet.yaml KPOINTS: reciprocal_density: 64

MPMetalRelaxSet中的K点生成方式是Kpoints.automatic_density_by_vol()；

ISMEAR=1 SIGMA=0.2 相关参数是在MPRelaxSet.yaml的基础上修改的

class MPMetalRelaxSet(MPRelaxSet): 
""" 
Implementation of VaspInputSet utilizing parameters in the public Materials Project, but with tuning for metals. Key things are a denser k point density, and a 
"""
```




```python
CONFIG = _load_yaml_config("MPRelaxSet")

def __init__(self, structure: Structure, **kwargs):
    """
    :param structure: Structure
    :param kwargs: Same as those supported by DictSet.
    """
    super().__init__(structure, **kwargs)
    self._config_dict["INCAR"].update({"ISMEAR": 1, "SIGMA": 0.2})
    self._config_dict["KPOINTS"].update({"reciprocal_density": 200})
    self.kwargs = kwargs





def automatic_density(structure: Structure, kppa: float, force_gamma: bool = False):
    """
    Returns an automatic Kpoint object based on a structure and a kpoint
    density. Uses Gamma centered meshes for hexagonal cells and
    Monkhorst-Pack grids otherwise.

    Algorithm:
        Uses a simple approach scaling the number of divisions along each
        reciprocal lattice vector proportional to its length.

    Args:
        structure (Structure): Input structure
        kppa (float): Grid density
        force_gamma (bool): Force a gamma centered mesh (default is to
            use gamma only for hexagonal cells or odd meshes)

    Returns:
        Kpoints
    """
    comment = f"pymatgen with grid density = {kppa:.0f} / number of atoms"
    if math.fabs((math.floor(kppa ** (1 / 3) + 0.5)) ** 3 - kppa) < 1:
        kppa += kppa * 0.01
    latt = structure.lattice
    lengths = latt.abc
    ngrid = kppa / structure.num_sites
    mult = (ngrid * lengths[0] * lengths[1] * lengths[2]) ** (1 / 3)

    num_div = [int(math.floor(max(mult / length, 1))) for length in lengths]

    is_hexagonal = latt.is_hexagonal()

    has_odd = any(i % 2 == 1 for i in num_div)
    if has_odd or is_hexagonal or force_gamma:
        style = Kpoints.supported_modes.Gamma
    else:
        style = Kpoints.supported_modes.Monkhorst

    return Kpoints(comment, 0, style, [num_div], (0, 0, 0))






def automatic_density_by_vol(structure: Structure, kppvol: int, force_gamma: bool = False):
    """
    Returns an automatic Kpoint object based on a structure and a kpoint
    density per inverse Angstrom^3 of reciprocal cell.

    Algorithm:
        Same as automatic_density()

    Args:
        structure (Structure): Input structure
        kppvol (int): Grid density per Angstrom^(-3) of reciprocal cell
        force_gamma (bool): Force a gamma centered mesh

    Returns:
        Kpoints
    """
    vol = structure.lattice.reciprocal_lattice.volume
    kppa = kppvol * vol * structure.num_sites
    return Kpoints.automatic_density(structure, kppa, force_gamma=force_gamma)

```



---

# 安装

>[https://pymatgen.org/installation.html](https://pymatgen.org/installation.html)


稳定版本
```bash
pip install pymatgen
```

开发版本
```bash
pip install -U git+https://github.com/materialsproject/pymatgen
```

pymatgen 插件和外部工具

>[https://pymatgen.org/addons](https://pymatgen.org/addons)

change log（代码 bug 修改，新功能添加等，可以关注）

>[https://pymatgen.org/change_log.html](https://pymatgen.org/change_log.html)

POTCAR 设置

兼容性

需对进行 `from pymatgen import <something>` 修改（v2022.0.0 版本开始）

```python
from pymatgen import Composition  # now "from pymatgen.core.composition import Composition"
from pymatgen import Lattice  # now "from pymatgen.core.lattice import Lattice"
from pymatgen import SymmOp  # now "from pymatgen.core.operations import SymmOp"
from pymatgen import DummySpecie, DummySpecies, Element, Specie, Species  # now "from pymatgen.core.periodic_table ..."
from pymatgen import PeriodicSite, Site  # now "from pymatgen.core.sites ..."
from pymatgen import IMolecule, IStructure, Molecule, Structure  # now "from pymatgen.core.structure ..."
from pymatgen import ArrayWithUnit, FloatWithUnit, Unit  # now "from pymatgen.core.units ..."
from pymatgen import Orbital, Spin  # now "from pymatgen.electronic_structure.core ..."
from pymatgen import MPRester  # now "from pymatgen.ext.matproj ..."
```



---

# 使用

当你探索代码时，你可能会注意到许多对象都有一个 as_dict 方法和一个 from_dict 静态方法的实现。对于大多数非基本的对象，我们将 pymatgen 设计成可以很容易地保存对象以供以后使用。虽然 python 确实提供了 pickling 功能，但 pickle 在代码修改方面往往是非常脆弱的。Pymatgen 的 as_dict 提供了一种以更稳健的方式保存你的工作的方法，它还有一个额外的好处就是更容易阅读。dict 表示法对于将这类对象输入某些数据库，如 MongoDb，也特别有用。这个 as_dict 规范是在 monty 库中提供的，monty 库是由 pymatgen 产生的一个通用 python 补充库。

```python
with open('structure.json', 'w') as file:
    json.dump(structure.as_dict(), file)
```

```python
with open('structure.json') as file:
    dct = json.load(file)
    structure = Structure.from_dict(dct)
```

你可以在 PyYAML 包中用 yaml 代替上述任何 json 命令来创建一个 yaml 文件。这两种选择之间有一定的权衡。作为一种格式，JSON 的效率更高，读写速度极快，但可读性却很差。YAML 在解析方面要慢一个数量级甚至更多，但更适合人类阅读。

手动生成 Structures

```python
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure, Molecule

coords = [[0, 0, 0], [0.75,0.5,0.75]]
lattice = Lattice.from_parameters(a=3.84, b=3.84, c=3.84, alpha=120,
                                  beta=90, gamma=60)
# Si
struct = Structure(lattice, ["Si", "Si"], coords)

coords = [[0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 1.089000],
          [1.026719, 0.000000, -0.363000],
          [-0.513360, -0.889165, -0.363000],
          [-0.513360, 0.889165, -0.363000]]
# 甲烷
methane = Molecule(["C", "H", "H", "H", "H"], coords)
```

写入/写出结构/分子

```python
# Read a POSCAR and write to a CIF.
structure = Structure.from_file("POSCAR")
structure.to(filename="CsCl.cif")

# Read an xyz file and write to a Gaussian Input file.
methane = Molecule.from_file("methane.xyz")
methane.to(filename="methane.gjf")
```

为了更精细地控制使用哪个解析，你可以指定特定的 io 包。例如，要从一个 cif 创建一个结构：

```python
from pymatgen.io.cif import CifParser

parser = CifParser("mycif.cif")
structure = parser.get_structures()[0]
```

```python
from pymatgen.io.vasp.inputs import Poscar

poscar = Poscar.from_file("POSCAR")
structure = poscar.structure
```

```python
from pymatgen.io.xyz import XYZ
from pymatgen.io.gaussian import GaussianInput

xyz = XYZ.from_file('methane.xyz')
gau = GaussianInput(xyz.molecule,
                    route_parameters={'SP': "", "SCF": "Tight"})
gau.write_file('methane.inp')
```

可以对 Structures 做的事

修改 Structures：`pymatgen.transformations`

分析 Structures：`pymatgen.analysis.structure_matcher`

```python
# Change the specie at site position 1 to a fluorine atom.
structure[1] = "F"
molecule[1] = "F"

# Change species and coordinates (fractional assumed for Structures,
# Cartesian for Molecules)
structure[1] = "Cl", [0.51, 0.51, 0.51]
molecule[1] = "F", [1.34, 2, 3]

# Structure/Molecule also supports typical list-like operators,
# such as reverse, extend, pop, index, count.
structure.reverse()
molecule.reverse()

structure.append("F", [0.9, 0.9, 0.9])
molecule.append("F", [2.1, 3,.2 4.3])
```

```python
# Make a supercell
structure.make_supercell([2, 2, 2])

# Get a primitive version of the Structure
structure.get_primitive_structure()

# Interpolate between two structures to get 10 structures (typically for NEB calculations.)
structure.interpolate(another_structure, nimages=10)
```

除了核心的 Element, Site and Structure 对象外，pymatgen 中的大多数分析（例如，创建相图）都是通过 Entry 对象进行的。一个条目的最基本形式是包含一个计算能量和一个成分，并可以选择包含其他输入或计算数据。在大多数情况下，你将使用 pymatgen. entries.computed_entries 中定义的 ComputedEntry 或 ComputedStructureEntry 对象。ComputedEntry 对象可以通过手动解析计算数据计算，或者使用 pymatgen.apps.borg 包来创建。

[pymatgen.io](http://pymatgen.io) - 管理计算输入和输出

pymatgen.io 模块包含了一些类，以方便编写输入文件和解析各种计算代码的输出文件，包括 VASP、Q-Chem、LAMMPS、CP2K、AbInit 等等。

管理输入的核心类是 `InputSet`。一个 `InputSet` 对象包含为一个计算写一个或多个输入文件所需的所有数据。具体来说，每个 InputSet 都有一个 `write_input()` 方法，可以将所有必要的文件写到你指定的位置。还有 InputGenerator 类，它产生的 InputSet 具有针对特定计算类型的设置（例如，结构弛豫）。你可以把 InputGenerator 类看作是完成特定计算任务的 “ 配方 “，而 InputSet 则包含应用于特定系统或结构的这些配方。

你也可以使用 InputSet.from_directory() 从一个包含计算输入的目录中构建一个 pymatgen InputSet。

许多代码还包含用于将输出文件解析为 pymatgen 对象的类，这些类继承自 InputFile，它提供了一个读写单个文件的标准接口。

pymatgen.transformations 包是用于对结构进行转换的标准包。目前已经支持许多转换，从简单的转换，如添加和删除位点，替换结构中的物种，到更高级的一对多的转换，如使用静电能量准则从结构中部分删除某个物种的一部分。转换类遵循一个严格的 API。一个典型的用法如下：

```python
from pymatgen.io.cif import CifParser
from pymatgen.transformations.standard_transformations import RemoveSpecieTransformations

# Read in a LiFePO4 structure from a cif.
parser = CifParser('LiFePO4.cif')
struct = parser.get_structures()[0]

t = RemoveSpeciesTransformation(["Li"])
modified_structure = t.apply_transformation(struct)
```

pymatgen.alchemy 包是一个用于进行高通量（HT）结构转化的框架。例如，它允许用户定义一系列应用于一组结构的转换，在此过程中产生新的结构。该框架还被设计成对所有在结构上进行的改变进行适当的记录，并具有无限的撤销功能。主要的类是：

```python
from pymatgen.alchemy.transmuters import CifTransmuter
from pymatgen.transformations.standard_transformations import SubstitutionTransformation, RemoveSpeciesTransformation

trans = []
trans.append(SubstitutionTransformation({"Fe":"Mn"}))
trans.append(RemoveSpecieTransformation(["Lu"]))
transmuter = CifTransmuter.from_filenames(["MultiStructure.cif"], trans)
structures = transmuter.transformed_structures
```


---

使用：[https://pymatgen.org/usage.html](https://pymatgen.org/usage.html)

模块索引：[http://pymatgen.org/genindex.html](http://pymatgen.org/genindex.html)

API：[http://pymatgen.org/modules.html](http://pymatgen.org/modules.html)

>[](https://github.com/xiangzhouzhang/ug-materials-simulation/blob/master/pymatgen/%E5%8C%85%E5%92%8C%E6%A8%A1%E5%9D%97%E7%BB%93%E6%9E%84.ipynb)[https://github.com/xiangzhouzhang/ug-materials-simulation/blob/master/pymatgen/包和模块结构.ipynb](https://github.com/xiangzhouzhang/ug-materials-simulation/blob/master/pymatgen/%E5%8C%85%E5%92%8C%E6%A8%A1%E5%9D%97%E7%BB%93%E6%9E%84.ipynb)

包 (package,subpackage) 是目录 (文件夹), 模块 (module,submodule) 是文件; import 既可以导入包和子包, 也可以导入模块和子模块;

想要查看一个包的完整结构 (层次) 有些繁琐, 此处只查看到二级包 (二级目录) 或与二级包并列的模块, 二级包及与其并列的模块都可以由 import 语句 (有两个点), 同称为包的二级结构; 由于结构上的一致性, 将子包 (目录) 及与其并列的模块 (文件) 等视为一种东西;

如何学习模块中的函数或者类:

语法 (一句话概括, 参数及参数类型, 返回值及返回值类型); 包含的方法或属性; 继承的基类 应用示例;

```text
filters.py 为二级模块

pymatgen/alchemy
├── filters.py
├── __init__.py
├── materials.py
├── __pycache__
└── transmuters.py

abinit 为二级包

pymatgen/io
├── abinit
├── adf.py
├── ase.py
├── atat.py
├── babel.py
├── cif.py
├── common.py
├── core.py
├── cp2k
├── cssr.py
├── exciting
├── feff
├── fiesta.py
├── gaussian.py
├── jarvis.py
├── lammps
├── lmto.py
├── lobster
├── nwchem.py
├── packmol.py
├── phonopy.py
├── prismatic.py
├── pwscf.py
├── __pycache__
├── qchem
├── res.py
├── shengbte.py
├── template.py
├── vasp
├── wannier90.py
├── xcrysden.py
├── xr.py
├── xtb
├── xyz.py
└── zeopp.py
```



pymatgen 典型工作流

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202310231537005.png)




常用 package 和 module

pymatgen.analysis

```python
# package
pymatgen.analysis.elasticity

# module
pymatgen.analysis.eos
```

pymatgen.core

core package 包含构建晶体模型时的基础概念, ex.晶格, 分子, 位点, 元素周期表等

```python
# module
pymatgen.core.structure
pymatgen.core.lattice
pymatgen.core.sites
pymatgen.core.surface
pymatgen.core.periodic_table
pymatgen.core.composition
pymatgen.core.units
pymatgen.core.tensors
```

pymatgen.ext

```python
# module
pymatgen.ext.matproj
```

[pymatgen.io](http://pymatgen.io)

pymatgen.io.lammps

```python
# module
pymatgen.io.lammps.data
pymatgen.io.lammps.inputs
pymatgen.io.lammps.output
pymatgen.io.lammps.utils module
```

pymatgen.io.vasp

```python
# module
pymatgen.io.vasp.inputs
pymatgen.io.vasp.outputs
pymatgen.io.vasp.sets
```

```python
# module
pymatgen.io.ase
pymatgen.io.atat
pymatgen.io.phonopy
```

pymatgen.phonon

```python
# module
pymatgen.phonon.bandstructure
pymatgen.phonon.dos
pymatgen.phonon.plotter
```

pymatgen.symmetry

symmetry 包是关于对称性的包:

```python
# module
pymatgen.symmetry.analyzer
pymatgen.symmetry.bandstructure
pymatgen.symmetry.groups
pymatgen.symmetry.maggroups
pymatgen.symmetry.settings
pymatgen.symmetry.structure
```

pymatgen.transformations

```python
#  module
pymatgen.transformations.advanced_transformations
pymatgen.transformations.defect_transformations
pymatgen.transformations.site_transformations
pymatgen.transformations.standard_transformations
pymatgen.transformations.transformation_abc
```


---

# 常用模块

## pymatgen.core

### structure

```python
from pymatgen.core.periodic_table import Element

ele = Element("Nb")
ele.is_metal
```


---

### surface

pymatgen 表面生成无法指定具体的层数
>[https://matsci.org/t/building-a-slab-and-interface/45317](https://matsci.org/t/building-a-slab-and-interface/45317)




`get_symmetrically_distinct_miller_indices()` - 获取指定晶面指数中的最大数值下其对称性非等同的所有晶面指数

`get_symmetrically_equivalent_miller_indices()` - 获取指定晶面指数下其对称性等同的所有晶面指数

`get_d()` - 获取层间距

`SlabGenerator` 类 - 构建指定晶面指数的 slab 模型
`get_slabs()` 方法 - 类初始化后，获取 slab 构型，可通过其得到该 slab 模型下不同终端的数量（`len()`）


---

### composition

>[module-pymatgen.core.composition](https://pymatgen.org/pymatgen.core.html#module-pymatgen.core.composition)

```python
from pymatgen.core.composition import Composition

# 获取化学式的成分（dict形式）
comp = Composition("LiFePO4")
comp.as_dict()
# output
# {'Li': 1.0, 'Fe': 1.0, 'P': 1.0, 'O': 4.0}
```



---

### periodic_table

pymatgen 查看元素的价电子排布
```python
from pymatgen.core.periodic_table import Element


element_list = ['B','Al','Si','Y','Ti','Zr','Hf','V','Nb','Cr','Mo','Fe','Co','Ni']
for element in element_list:
    ele_struc = Element(f"{element}").electronic_structure
    print(f"{element}, {ele_struc}")
```



---

## pymatgen.io.ase

[pymatgen.io.ase.AseAtomsAdaptor](https://pymatgen.org/pymatgen.io.html#pymatgen.io.ase.AseAtomsAdaptor)

`AseAtomsAdaptor` 将 ase 中的 `atoms` 类与 pymatgen 中的 `Structure` 类互相转换


```python
from ase.build import bulk
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.core.structure import Structure

atoms = bulk("Si", "diamond", a=5.44)
struct = AseAtomsAdaptor.get_structure(atoms)

struct = Structure.from_prototype(prototype="diamond", species=["Si"], a=5.44)
atoms = AseAtomsAdaptor.get_atoms(struct)
```



---

## pymatgen.io.vasp.inputs

`pymatgen/io.vasp/inputs.py`


```python
Incar(params: dict[str, Any] | None = None)
from_file(filename)
write_file(filename)

Kpoints()
from_file(filename)
write_file(filename)

Poscar(structure)
from_file(filename)
write_file(filename)

Potcar(symbols)
from_file(filename)
write_file(filename)
```

---

### Incar

在解析 INCAR 文件时，得到的字典的键和值都是字符串，需要对 INCAR 中不同参数的键的值的类型进行正确的转换，因此定义了 `proc_val()` 函数。



---

### Kpoints

WIP…


---

### Poscar

WIP…


---

### Potcar

读取和写入 POTCAR 文件的 object，由 PotcarSingle object 的列表组成


---

### PotcarSingle

单个 POTCAR object



---

## pymatgen.io.vasp.sets

`pymatgen/io.vasp/sets.py`

### MPRelaxSet

`pymatgen/io.vasp/MPRelaxSet.yaml`
```yaml
# Default VASP settings for calculations in the Materials Project.
# Reasonably robust. Use this if you intend to combine your calculated data
# with Materials Project data for analysis.
PARENT: VASPIncarBase
INCAR:
  ALGO: FAST
  EDIFF_PER_ATOM: 5.0e-05
  ENCUT: 520
  IBRION: 2
  ISIF: 3
  ISMEAR: -5
  ISPIN: 2
  LASPH: true
  LDAU: true
  LDAUJ:
    F:
      Co: 0
      Cr: 0
      Fe: 0
      Mn: 0
      Mo: 0
      Ni: 0
      V: 0
      W: 0
    O:
      Co: 0
      Cr: 0
      Fe: 0
      Mn: 0
      Mo: 0
      Ni: 0
      V: 0
      W: 0
  LDAUL:
    F:
      Co: 2
      Cr: 2
      Fe: 2
      Mn: 2
      Mo: 2
      Ni: 2
      V: 2
      W: 2
    O:
      Co: 2
      Cr: 2
      Fe: 2
      Mn: 2
      Mo: 2
      Ni: 2
      V: 2
      W: 2
  LDAUTYPE: 2
  LDAUU:
    F:
      Co: 3.32
      Cr: 3.7
      Fe: 5.3
      Mn: 3.9
      Mo: 4.38
      Ni: 6.2
      V: 3.25
      W: 6.2
    O:
      Co: 3.32
      Cr: 3.7
      Fe: 5.3
      Mn: 3.9
      Mo: 4.38
      Ni: 6.2
      V: 3.25
      W: 6.2
  LDAUPRINT: 1
  LORBIT: 11
  LREAL: AUTO
  LWAVE: false
  NELM: 100
  NSW: 99
  PREC: Accurate
  SIGMA: 0.05
KPOINTS:
  reciprocal_density: 64
POTCAR_FUNCTIONAL: PBE
POTCAR:
  Ac: Ac
  Ag: Ag
  Al: Al
  Ar: Ar
  As: As
  Au: Au
  B: B
  Ba: Ba_sv
  Be: Be_sv
  Bi: Bi
  Br: Br
  C: C
  Ca: Ca_sv
  Cd: Cd
  Ce: Ce
  Cl: Cl
  Co: Co
  Cr: Cr_pv
  Cs: Cs_sv
  Cu: Cu_pv
  Dy: Dy_3
  Er: Er_3
  Eu: Eu
  F: F
  Fe: Fe_pv
  Ga: Ga_d
  Gd: Gd
  Ge: Ge_d
  H: H
  He: He
  Hf: Hf_pv
  Hg: Hg
  Ho: Ho_3
  I: I
  In: In_d
  Ir: Ir
  K: K_sv
  Kr: Kr
  La: La
  Li: Li_sv
  Lu: Lu_3
  Mg: Mg_pv
  Mn: Mn_pv
  Mo: Mo_pv
  N: N
  Na: Na_pv
  Nb: Nb_pv
  Nd: Nd_3
  Ne: Ne
  Ni: Ni_pv
  Np: Np
  O: O
  Os: Os_pv
  P: P
  Pa: Pa
  Pb: Pb_d
  Pd: Pd
  Pm: Pm_3
  Pr: Pr_3
  Pt: Pt
  Pu: Pu
  Rb: Rb_sv
  Re: Re_pv
  Rh: Rh_pv
  Ru: Ru_pv
  S: S
  Sb: Sb
  Sc: Sc_sv
  Se: Se
  Si: Si
  Sm: Sm_3
  Sn: Sn_d
  Sr: Sr_sv
  Ta: Ta_pv
  Tb: Tb_3
  Tc: Tc_pv
  Te: Te
  Th: Th
  Ti: Ti_pv
  Tl: Tl_d
  Tm: Tm_3
  U: U
  V: V_pv
  W: W_pv
  Xe: Xe
  Y: Y_sv
  # 2023-05-02: change Yb_2 to Yb_3 if POTCAR_FUNCTIONAL=PBE_54 else issue warning if Yb present
  # since Yb_3 didn't exist prior to PBE_54
  # reason: Yb_2 gives incorrect thermodynamics for most systems with Yb3+
  # https://github.com/materialsproject/pymatgen/issues/2968
  Yb: Yb_2
  Zn: Zn
  Zr: Zr_sv
```


pymatgen/io/vasp/VASPIncarBase.yaml
```yaml
INCAR:
  MAGMOM:
    Ce: 5
    Ce3+: 1
    Co: 0.6
    Co3+: 0.6
    Co4+: 1
    Cr: 5
    Dy3+: 5
    Er3+: 3
    Eu: 10
    Eu2+: 7
    Eu3+: 6
    Fe: 5
    Gd3+: 7
    Ho3+: 4
    La3+: 0.6
    Lu3+: 0.6
    Mn: 5
    Mn3+: 4
    Mn4+: 3
    Mo: 5
    Nd3+: 3
    Ni: 5
    Pm3+: 4
    Pr3+: 2
    Sm3+: 5
    Tb3+: 6
    Tm3+: 2
    V: 5
    W: 5
    Yb3+: 1
```


---

### MPStaticSet

WIP…



---

## pymatgen.io.vasp.outputs

>[pymatgen.io.vasp package — pymatgen 2023.10.4 documentation](https://pymatgen.org/pymatgen.io.vasp.html)

读取、执行、写 VASP 的输出文件

`pymatgen/io.vasp/outputs.py`



---

### Outcar

WIP…


---

### Oszicar

WIP…


---

### Vasprun

WIP…



---

## pymatgen.analysis

### eos

类：`BirchMurnaghan`、`Birch`、`Murnaghan`、`PourierTarantola`、`Vinet` 等


示例：
```python
from pymatgen.analysis.eos import BirchMurnaghan
import pandas as pd
# from plot_params import set_plot_params


# fcc Cu的原胞体积和能量数据
# 体模量B实验值为140GPa
data = pd.read_csv("eng_vol.dat", sep=" ")
eng_data = data["energy(eV/cell)"]
vol_data = data["vol/atom"]

eos = BirchMurnaghan(volumes=vol_data, energies=eng_data)
eos.fit()

# 平衡能量拟合值为-3.731eV
print(eos.e0)
# 体模量B拟合值为138.4GPa
print(eos.b0_GPa)
# 平衡体积拟合值为12.015 Ang^3
print(eos.v0)
print(eos.results)

set_plot_params()
eos.plot()

```


---

### interface

```python
from pymatgen.analysis.interfaces.coherent_interfaces import CoherentInterfaceBuilder
from pymatgen.analysis.interfaces.zsl import ZSLGenerator
```

`pymatgen.analysis.interfaces.zsl` 模块 - 实现了 Zur 和 McGill 晶格匹配算法

`ZSLGenerator` - 该类基于 Zur 和 McGill 提出的异质结构界面的晶格矢量匹配方法生成匹配界面超晶格

生成所有可能匹配的超晶格的过程是：

- 减少表面/界面（surfaces）晶格向量并计算表面/界面的面积
- 在最大允许面积内生成所有超晶格变换
- 对于每个超晶格集：
	- 减少超晶格矢量
	- 检查 film 和 substrate 表面超晶格之间的长度和角度

`pymatgen.analysis.interfaces.coherent_interfaces` 模块 - 提供了存储、生成和操作材料界面的类

`CoherentInterfaceBuilder` - 该类构造了两个 slab 之间的共格界面。共格由匹配晶格（matching lattices）而非子平面（sub-planes）定义。


>[Working with Surfaces and Interfaces - The Materials Project Workshop](https://workshop.materialsproject.org/lessons/03_heterointerfaces/Main%20Lesson/)


---

## pymatgen.symmetry.analyzer

### SpacegroupAnalyzer

寻找构型中的等同原子
```python
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


# structure = Structure.from_file("POSCAR_Nb3Si")
structure = Structure.from_file("POSCAR_Nb5Si3-alpha")
sga = SpacegroupAnalyzer(structure)
symmetrized_structure = sga.get_symmetrized_structure()
symmetry_dataset = sga.get_symmetry_dataset()
equivalent_atom = symmetry_dataset['equivalent_atoms']
# [ 0  0  0  0  0  0  0  0  8  8  8  8  8  8  8  8 16 16 16 16 16 16 16 16 24 24 24 24 24 24 24 24] Nb3Si
# [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 16 16 16 16 20 20 20 20 20 20 20 20 28 28 28 28] alpha-Nb5Si3
# print(sga)
# print(symmetrized_structure)
# print(symmetry_dataset)
print(equivalent_atom)
```



---

## pymatgen.transformations

### standard_transformations

WIP…



---

## pymatgen.phonon

>[https://pymatgen.org/pymatgen.phonon.html](https://pymatgen.org/pymatgen.phonon.html)



---

## API

pymatgen 新 API
>[Materials Project - API](https://materialsproject.org/api)
>
>[Getting Started - Materials Project Documentation](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)


安装
```bash
pip install mp-api
pip install mpcontribs-client
```


```python
# old
from pymatgen.ext.matproj import MPRester
# new
from mp_api.client import MPRester

# Get the structure from the Materials Project
with MPRester("api-key") as mpr:
    struct = mpr.get_structure_by_material_id("mp-149")
```

使用旧 API 出现的 warning
```bash
/home/yangsl/src/miniconda3/envs/atomate_env/lib/python3.11/site-packages/pymatgen/ext/matproj_legacy.py:166: UserWarning: You are using the legacy MPRester. This version of the MPRester will no longer be updated. To access the latest data with the new MPRester, obtain a new API key from https://materialsproject.org/api and consult the docs at https://docs.materialsproject.org/ for more information.
  warnings.warn(
```



---

### pymatgen.ext.matproj

调用 MP API 获取 MP 数据

[Usage - pymatgen 2022.5.19 documentation](https://pymatgen.org/usage.html?highlight=materials%20project#pymatgen-matproj-rest-integration-with-the-materials-project-rest-api)

模块具体用法

[pymatgen.ext.matproj module - pymatgen 2022.5.19 documentation](https://pymatgen.org/pymatgen.ext.matproj.html?highlight=pymatgen%20matproj%20rest)

`get_download_info()`：获取来自 NoMaD repository 的裸 VASP 输出文件链接

`get_gb_data()`：获取晶界数据

- [ ] 如何通过 API 获得 equation of state 和晶界能

- [ ] Pymatgen 一些实例代码


>[https://github.com/materialsvirtuallab/matgenb](https://github.com/materialsvirtuallab/matgenb)
