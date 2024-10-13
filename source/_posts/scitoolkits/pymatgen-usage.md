---
title: pymatgen 使用
top: false
cover:
toc: true
mathjax: true
summary: pymatgen 使用
description: pymatgen 使用
tags:
  - pymatgen
categories:
  - 科研工具
date: 2023-10-18 09:00:00
abbrlink: 124968
password:
---

# pymatgen 使用

## 介绍

- 用于表示 Element、Site、Structure、Molecule 的高度灵活的类。
- 文件输入/输出支持广泛，如 VASP、ABINIT、CIF、Gaussian、XYZ 等（主要依靠 Open Babel 包）。
- 强大的分析工具，包括生成相图、Pourbaix 图、扩散分析、反应等。
- 电子结构分析，如态密度和能带结构。
- 集成 Materials Project REST API、Crystallography Open Database 等其他外部数据源
- 代码文档详细

---

### 参考资料

- pymatgen notebook：[GitHub - yw-fang/pymatgen-notebook](https://github.com/yw-fang/pymatgen-notebook)

- pymatgen 实例代码：[GitHub - materialsvirtuallab/matgenb](https://github.com/materialsvirtuallab/matgenb)

- [Materials Project Documentation](https://docs.materialsproject.org/)

- [Materials Methodology - Materials Project Documentation](https://docs.materialsproject.org/methodology/materials-methodology)（该网址包含了 pymatgen 在材料相关计算中用的具体参数及其说明：如，截断能为 520eV 是由元素周期表所有元素中最大截断能的 1.3 倍得到的）

- [GitHub - computron/pymatgen\_tutorials: Tutorials for using the pymatgen library](https://github.com/computron/pymatgen_tutorials)

- material project workshop:
    - 2021：[The Materials Project Workshop](https://workshop.materialsproject.org/)
    - 2018~2020：[Releases · materialsproject/workshop](https://github.com/materialsproject/workshop/releases)
    - 2017：[GitHub - materialsproject/workshop-2017: Assets for the 2017 Materials Project workshop](https://github.com/materialsproject/workshop-2017)
    - 2016：[GitHub - materialsproject/workshop-2016: Assets for the Materials Project workshop in Aug 2016](https://github.com/materialsproject/workshop-2016)
    - 注：workshop 2020 和 2021 的内容绝大部分相似，lesson3 分别为表面和界面；workshop 2018 和 2019 的内容相似（对 atomate 的讲解稍微详细些）

---

```python
from pymatgen.analysis.diffusion.neb.pathfinder import IDPPSolver

from pymatgen.analysis.defects.generators import SubstitutionGenerator

subs = SubstitutionGenerator(structure, "Bi")

# 晶界相关
from pymatgen.core.interface import GrainBoundary, GrainBoundaryGenerator
```

[求助：过渡态计算新版pymatgen中找不到iddp插值方法 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-19704-1-1.html)

```python
# 过渡态 NEB
from pymatgen.analysis import transition_state
```

确保 VASP 计算符合 MP 数据：[GitHub - materialsproject/pymatgen-io-validation: Comprehensive input/output validator. Made with the initial purpose of ensuring calculations in the MP Database are compatible; now generalized.](https://github.com/materialsproject/pymatgen-io-validation)

里面有讲到 IEEE 标准
[Elastic Constants | Materials Project Documentation](https://docs.materialsproject.org/methodology/materials-methodology/elasticity)

pymatgen 中的 LLL reduction 是什么含义

pymatgen 键长计算（并非只是简单的计算原子对之间的距离）


- [x] pymatgen 如何获取可用的 POTCAR 种类；较难：一般是指定泛函类型

- [x] pymatgen structure 如何通过 structure 来生成 potcar？
解决方法：通过 Poscar 类得到 structure 的元素种类，之后与 PBE 泛函的元素进行比对，之后用 Potcar 类写入 POTCAR（生成新的之前需删掉原来的 POTCAR 文件）



---

## 安装

- 参考：[https://pymatgen.org/installation.html](https://pymatgen.org/installation.html)

- 安装：

```bash
# 稳定版本
pip install -U pymatgen
# 开发版本
pip install -U git+https://github.com/materialsproject/pymatgen
```

- 赝势目录设置

- [change log](https://pymatgen.org/change_log.html)（代码 bug 修复，新功能添加等，可以关注）

- [pymatgen 插件和外部工具](https://pymatgen.org/addons)

- 兼容性：需对进行 `from pymatgen import xxx` 修改（v2022.0.0 版本开始）

```python
# 旧
from pymatgen import IMolecule, IStructure, Molecule, Structure
from pymatgen import PeriodicSite, Site
from pymatgen import Composition
from pymatgen import Lattice
from pymatgen import DummySpecie, DummySpecies, Element, Specie, Species
from pymatgen import SymmOp
from pymatgen import ArrayWithUnit, FloatWithUnit, Unit
from pymatgen import Orbital, Spin
from pymatgen import MPRester

# 新
from pymatgen.core.structure ...
from pymatgen.core.sites ...
from pymatgen.core.composition import Composition
from pymatgen.core.lattice import Lattice
from pymatgen.core.periodic_table ...
from pymatgen.core.operations import SymmOp
from pymatgen.core.units ...
from pymatgen.electronic_structure.core ...
from pymatgen.ext.matproj ...
```



---

## 使用

- 使用：[https://pymatgen.org/usage.html](https://pymatgen.org/usage.html)

- pymatgen 的包 (package、subpackage) 是目录, 模块 (module、submodule) 是文件; import 既可以导入包和子包, 也可以导入模块和子模块； [ug-materials-simulation/pymatgen/包和模块结构.ipynb at master · xiangzhouzhang/ug-materials-simulation · GitHub](https://github.com/xiangzhouzhang/ug-materials-simulation/blob/master/pymatgen/%E5%8C%85%E5%92%8C%E6%A8%A1%E5%9D%97%E7%BB%93%E6%9E%84.ipynb)

- pymatgen 支持的构型文件格式

```python
'prismatic', 'cssr', 'json', 'xsf', 'yaml', 'poscar', 'mcif', 'cif'
```

- MP 晶体 DFT code 用的是 VASP，分子用的是 Q-Chem

- `MSONable` 类：MSON（Monty JSON）；MSONable 对象必须实现 `as_dict()` 方法，该方法须返回可序列化为 JSON 的字典，且须支持无参数。静态方法 `from_dict()`，从 `as_dict()` 方法生成的字典中重建对象。`as_dict()` 方法应该包含 `@module` 和 `@class` 键，这将允许 MontyEncoder 动态反序列化该类。

- `Molecule` 与 `Structure` 类
    - `Molecule` 类的输入参数：`species` 和 `coords`，关键字参数有：`charge`、 `spin_multiplicity`、 `validate_proximity` 和 `site_properties`
    - `Structure` 类还需指定 `lattice` 输入参数
    - `Molecule` 类的 `coords` 参数值需是 Cartesian 坐标形式，`Structure` 类可以是 Cartesian 和分数两种坐标形式
    - `Molecule` 本质上是 Site objects 的列表；`Structure` 本质上是 PeriodicSites objects 的列表；可以像 list 一样操作 `Molecule` 和 `Structure`

- monty 包：对 json/yaml/msgpack 等文件格式进行 serialization

```python
from monty.serialization import loadfn, dumpfn
```


```python
import pymatgen.core
import sys

sys.version                  # 查看 python 版本
pymatgen.core.__version__    # 查看 pymatgen 版本
pymatgen.core.__file__       # 查看 pymatgen 安装路径
```


---

### 工作流

pymatgen 典型工作流

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202310231537005.png)


---

### CLI

- 不是太好用，建议直接写脚本

```bash
pmg subcommand -h  # 查看子命令帮助

# 分析当前路径，会将生成的数据打包压缩成文件
pmg analyze .

# -f 单个文件；--filenames 可多个文件
# 查看结构空间群信息
pmg structure -s 0.00001 -f POSCAR

# 构型文件转换，功能有限
# Supported formats include POSCAR/CONTCAR, CIF, CSSR, etc.
pmg structure --convert --filenames POSCAR *.cif

# 可视化构型；需安装 vtk 包；会报错，不建议
pmg view POSCAR
```

- pymatgen 的 cli 可以使用 argcomplete 库（`pyamtgen/cli/pmg.py`；用于 cli 命令的补全）

```python
    try:
        import argcomplete

        argcomplete.autocomplete(parser)
    except ImportError:
        # argcomplete not present.
        pass
```


---

### structure 创建、保存、分析与变化操作

```python
from pymatgen.core.composition import Composition
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# 结构创建
lattice = Lattice.cubic(4.2)

# 标准方法
structure = Structure(
    lattice,
    ["Cs", "Cl"],
    ...[[0, 0, 0], [0.5, 0.5, 0.5]],
)

# 利用空间群对称性创建结构
structure = Structure.from_spacegroup(
    "Fm-3m",
    Lattice.cubic(3),
    ["Li", "O"],
    [[0.25, 0.25, 0.25], [0, 0, 0]],
)

bcc_fe = Structure.from_spacegroup(
    "Im-3m",
    Lattice.cubic(2.8),
    ["Fe"],
    [[0, 0, 0]],
)

nacl = Structure.from_spacegroup(
    "Fm-3m",
    Lattice.cubic(5.692),
    ["Na+", "Cl-"],
    [[0, 0, 0], [0.5, 0.5, 0.5]],
)

# 保存成其他文件格式
# 不提供 filename 参数，返回 string
structure.to(fmt="poscar")
# 只提供 filename 参数，会自动识别其格式
structure.to(filename="POSCAR") 
structure.to(filename="CsCl.cif")

# 从 str 或文件中读取结构
structure = Structure.from_str(open("CsCl.cif").read(), fmt="cif") 
structure = Structure.from_file("CsCl.cif")

# 改变位点元素种类
structure[1] = "F"

# 改变位点元素种类和坐标
structure[1] = "Cl", [0.51, 0.51, 0.51]

# 元素替换
structure["Cs"] = "K"

# 生成无序结构
# 部分占据的无序结构无法保存成 POSCAR
# 与 SQS 是不同的概念
structure["K"] = "K0.5Na0.5"

# structure 类似 list，支持大部分的 list 方法
# reverse, append, extend, pop, index, count
structure.reverse()
structure.append("F", [0.9, 0.9, 0.9])
```

修改 Structures：`pymatgen.transformations`

分析 Structures：`pymatgen.analysis.structure_matcher`

```python
# 超胞构建
structure * 2
structure * (2, 2, 2)
structure.make_supercell([2, 2, 2])
```


---

pymatgen 的许多 object 都有 `as_dict()` 方法和 `from_dict()` 静态方法的实现。虽然 python 确实提供了 pickling 功能（实现对象序列化和反序列化的方式），但 pickle 在代码修改方面往往是非常脆弱的。`as_dict()` 提供了一种以更稳健的方式保存工作的方法，且更容易阅读。将 object 输入某些数据库，如 MongoDb，也特别有用。`as_dict()` 规范是由 monty 库（pymatgen 产生的一个通用 python 补充库）提供的。

```python
with open('structure.json', 'w') as file:
    json.dump(structure.as_dict(), file)
```

```python
with open('structure.json') as file:
    dct = json.load(file)
    structure = Structure.from_dict(dct)
```

可使用 PyYAML 包的 yaml 代替上述任何 json 命令来创建 yaml 文件（JSON 格式效率高，读写速度快，但可读性差；YAML 解析速度慢，但更适合人类阅读）

更精细地控制从文件读取解析结构，可以使用特定的 io 包。这些包也提供了导出文件格式的方法。

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


---

### Entry

除了核心的 Element、Site、Structure object 外，pymatgen 中的大多数分析（创建相图）都是通过 Entry object 进行的。Entry 的最基本形式是包含一个计算的能量和一个构型成分（可包含其他输入或计算数据）。大多数情况下 `pymatgen. entries.computed_entries` 中定义的 `ComputedEntry` 或 `ComputedStructureEntry` 对象。

### 计算输入输出管理

pymatgen.io 模块包含了一些类，以方便编写计算软件的输入文件和解析输出文件，主要是 VASP。

输入管理的核心类是 `InputSet`。 `InputSet` object 包含计算输入文件所需的所有数据。具体来说，`write_input()` 方法，可将所有文件写到指定位置。InputGenerator 类可以看作是完成特定计算任务的 recipe，而 InputSet 则包含这些 recipes 以应用于特定体系或结构。

也可以使用 `InputSet.from_directory()` 从计算目录中构建 pymatgen InputSet。

许多解析输出文件的类继承自 InputFile，其提供了一个读写文件的标准接口。

---

### 变换操作

- 简单的变换操作：如添加和删除原子位点，替换结构中的元素，到更高级的一对多的转换

- 典型用法：

```python
from pymatgen.transformations.standard_transformations import RemoveSpecieTransformations

structure = ...

# 添加具体的变换操作
t = RemoveSpeciesTransformation(["X"])

# 施加变换操作到构型上
modified_structure = t.apply_transformation(structture)
```


---

### 其他

- pymatgen 构型可视化：[Pymatgen - how to visualize a crystal structure? - Materials Project / Materials Project Data/API - Materials Science Community Discourse](https://matsci.org/t/pymatgen-how-to-visualize-a-crystal-structure/2761)

```python
# 可视化原子构型
import nglview

nglview.show_pymatgen()
nglview.show_ase()
```

---

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
```

---

```python
# 待了解
read_neb()

MITNEBSet class
```

---

复杂结构 pymatgen 无法将其单胞转化成原胞（Al3Ni）

---

- 生成元素置换后的非等同结构（借助 bsym 包）：[bsym_examples](https://nbviewer.org/github/bjmorgan/bsym/blob/master/examples/bsym_examples.ipynb)

```python
from bsym.interface.pymatgen import unique_structure_substitutions

subs_structures = unique_structure_substitutions(
    structure=structure,
    to_substitute="Nb",
    site_distribution={"Al": 2, "Nb": 14},
    verbose=True,
    show_progress=True,
)
```

---

- 解析 VASP 计算目录：[Automated DFT - The Materials Project Workshop](https://workshop.materialsproject.org/lessons/05_automated_dft/Lesson/#parsing-directories-with-atomate-drones)

```python
from atomate.vasp.drones import VaspDrone

drone = VaspDrone()
task_doc = drone.assimilate(path=...)

task_doc.keys()
```

---

[【Pymatgen学习 2】Ewald方法计算静电能](https://zhuanlan.zhihu.com/p/708133858)

[Ewald Summation - Qijing Zheng](http://staff.ustc.edu.cn/~zqj/posts/Ewald-Summation/)

EwaldSummation 是 pymatgen 库中的一个类，用于计算离子晶体的 Ewald 总能量。Ewald 总能量是一种用于处理带电体系的长程库仑相互作用的技术，通常用于计算固体材料中的电势能。该方法将总能量分解为实空间、倒空间、点电荷修正和偶极修正部分，并进行相应的求和计算。



---

## 常用模块

### pymatgen.core

pymatgen 核心模块

---

#### structure

- 有 `IStructure` 和 `Structure` 类，`Structure` 类继承自 `IStructure`

- `Structure` 无 `wrap()` 方法，ase 有：[pymatgen - What Does the coordinate list next to the cartesian coordinates of an atom represent in neighbor\_list - Stack Overflow](https://stackoverflow.com/questions/54356049/what-does-the-coordinate-list-next-to-the-cartesian-coordinates-of-an-atom-repre)

- `Structure` 类相关属性和方法：

```python
from pymatgen.core.structure import Structure

# 属性
num_sites                # 原子数；int
composition.num_atoms    # 原子数；float
n_elems                  # 元素数
symbol_set               # 元素种类；tuple
types_of_specie          # 元素种类；Element
formula                  # 化学式
compsition               # 成分；as_dict() 转换成字典形式
frac_coords              # 分数坐标
cart_coords              # Cartesian 坐标
lattice                  # 点阵
       .abc              # 晶格常数
volume                   # 体积
density                  # 密度
center_of_mass           # 质心

# 方法
remove_species()         # 删除元素种类
replace_species()        # 替换元素种类
translate_sites()        # 移动原子位点
get_space_group_info()   # 获取空间群信息
from_spacegroup()        # 根据空间群构建结构
from_prototype()         # 通过原型结构快速构建结构
to_cell()                # 获取单/原胞
to_conventional()        # 获取单胞；调用 to_cell()
to_primitive()           # 获取原胞；同上
interpolate()            # 在两个结构间插值，用于 NEB 计算
```


---

#### surface

- pymatgen 表面生成无法指定具体的层数（可以指定最第层数）：[https://matsci.org/t/building-a-slab-and-interface/45317](https://matsci.org/t/building-a-slab-and-interface/45317)

```python
# 获取指定晶面指数中的最大数值下其对称性非等同的所有晶面指数
get_symmetrically_distinct_miller_indices()

# 获取指定晶面指数下其对称性等同的所有晶面指数
get_symmetrically_equivalent_miller_indices()

get_d()           # 获取层间距

SlabGenerator     # 类；构建指定晶面指数的 slab 模型

# 方法
get_slabs()       # 获取所有的 slab 构型（数量含义为该 slab 模型下不同终端的数量）
```


---

#### composition

```python
from pymatgen.core.composition import Composition

Composition("LiFePO4").as_dict()

# Composition
alphabetical_formula
chemical_system
```


---

#### periodic_table

```python
from pymatgen.core.periodic_table import Element

# 属性
electronic_structure       # 电子结构（可查看元素价电子排布）
is_metal                   # 是否为金属

# 方法


# 静态方法
print_periodic_table()     # 打印元素周期表

# Element
average_ionic_radius
```


---

#### sites

```python
# 属性
coords
specie
```


---

#### lattice

```python
from pymatgen.core.lattice import Lattice

# lattice 构建
Lattice([[5, 0, 0], [0, 5, 0], [0, 0, 5]])
Lattice.from_parameters(5, 5, 5, 90, 90, 90)
Lattice.cubic(5)

# 属性
reciprocal_lattice          # 倒易点阵

# 方法
get_wigner_seitz_cell()     # wigner seitz 原胞
get_brillouin_zone()        # 布里渊区；倒易点阵的 wigner seitz 原胞
```


---

#### units

```python

```


---

### pymatgen.io.ase

- `AseAtomsAdaptor`：将 ase 中的 `atoms` 类与 pymatgen 中的 `Structure` 类互相转换

```python
from pymatgen.io.ase import AseAtomsAdaptor

# 静态方法
get_structure()     # atoms 转 Structure
get_atoms()         # Structure 转 atoms
```


---

### pymatgen.io.atat

只有 Mcsqs 类（功能较一般）


---

### pymatgen.io.vasp.help

查看 VASP 参数 help

```python
from pymatgen.io.vasp.help import VaspDoc

# 静态方法
VaspDoc.get_incar_tags()
VaspDoc.get_help("IBRION")

# 实例方法（需初始化）
VaspDoc().print_help("IBRION")
# 展示 HTML 格式内容
VaspDoc().print_jupyter_help("IBRION")
```


---

### pymatgen.io.vasp.inputs

- VASP 输入文件模块
- 四种输入文件类都有 `from_dict()`、`from_file()`、`write_file()` 类方法

---

#### Incar

- 在解析 INCAR 文件时，得到的字典的键和值都是字符串，需要对 INCAR 中不同参数的键的值的类型进行正确的转换，因此定义了 `proc_val()` 函数

```python
from pymatgen.io.vasp.inputs import Incar

Incar(params: dict[str, Any] | None = None)
```


---

#### Kpoints

```python
from pymatgen.io.vasp.inputs import Kpoints


automatic()                 # length
automatic_density()         # grid_density
automatic_density_by_vol()  # reciprocal_density
```


---

#### Poscar

```python
from pymatgen.io.vasp.inputs import Poscar


```


---

#### Potcar

读取和写入 POTCAR 文件的 object，由 PotcarSingle object （单个 POTCAR） 的列表组成


```python
from pymatgen.io.vasp.inputs import Potcar

# 写入 POTCAR
element_list = ["Ti", "Al"]
pot = Potcar(element_list)
pot.write_file("POTCAR")
```


---

### pymatgen.io.vasp.sets

- MPRelaxSet、MPStaticSet 等类均继承于 VaspInputSet，这些 InputSet 都有 `write_input()` 方法
- MPStaticSet 有设置 EDIFF 10-4；没有 MPStaticSet.yaml；reciprocal_density=100

```python
pymatgen/io/vasp/MPRelaxSet.yaml         # 弛豫计算，MP 默认的所有输入文件参数设置
pymatgen/io/vasp/VASPIncarBase.yaml      # INCAR 文件中的 MAGMOM 元素磁矩参数


from pymatgen.io.vasp.sets import MPStaticSet, MPRelaxSet, MPMetalRelaxSet

# 方法
write_input(output_dir=..., potcar_spec=True)  # 生成 4 个输入文件

# 静态方法
MPStaticSet.from_prev_calc()            # 基于之前的 VASP 计算目录中生成静态计算输入文件

# 属性
config_dict                             # config_dict["POTCAR"]["Mg"]
```


```text
MPRelaxSet继承的DictSet类，DictSet类继承的VaspInputSet类 MPRelaxSet中的K点生成方式是Kpoints.automatic_density_by_vol() ISMEAR=-5 SIGMA=0.05 io/vasp/MPRelaxSet.yaml KPOINTS: reciprocal_density: 64

MPMetalRelaxSet中的K点生成方式是Kpoints.automatic_density_by_vol()；

ISMEAR=1 SIGMA=0.2 相关参数是在MPRelaxSet.yaml的基础上修改的

class MPMetalRelaxSet(MPRelaxSet): 
""" 
Implementation of VaspInputSet utilizing parameters in the public Materials Project, but with tuning for metals. Key things are a denser k point density, and a 
"""
```


---

### pymatgen.io.vasp.outputs

- 读取并解析 VASP 的输出文件
- Oszicar 类的 `final_energy` 属性选择的是 `E0`；Vasprun 类的 `final_energy` 属性选择的也是 `E0`


---

#### Outcar

Outcar 类能获取的较普适数据的属性和方法较少（主要是解析 Vasprun.xml 文件无法获取到的数据）

```python
from pymatgen.io.vasp.ouputs import Outcar


# 方法
read_pattern()
read_table_pattern()

read_neb()
```

```python
"""
        drift (np.array): Total drift for each step in eV/Atom.
        run_stats (dict): Various useful run stats as a dict including "System time (sec)", "Total CPU time used (sec)",
            "Elapsed time (sec)", "Maximum memory used (kb)", "Average memory used (kb)", "User time (sec)", "cores".
        is_stopped (bool): True if OUTCAR is from a stopped run (using STOPCAR, see VASP Manual).
        final_energy (float): Final energy after extrapolation of sigma back to 0, i.e. energy(sigma->0).
        final_energy_wo_entrp (float): Final energy before extrapolation of sigma, i.e. energy without entropy.
        final_fr_energy (float): Final "free energy", i.e. free energy TOTEN.
"""
```

---

#### Oszicar

```python
from pymatgen.io.vasp.ouputs import Oszicar


# 属性
```


---

#### Vasprun

BSVasprun 类：Vasprun 的优化版本（继承至 Vasprun），只解析能带结构的本征值（忽略结构，参数等）

```python
from pymatgen.io.vasp.ouputs import Vasprun

# 属性
ionic_steps       # 离子步


# 每个 ionic_step 所含的数据 dict key
dict_keys(
    [
        "e_fr_energy",
        "e_wo_entrp",
        "e_0_energy",
        "forces",
        "stress",
        "electronic_steps",
        "structure",
    ]
)
```


---

### pymatgen.electronic_structure

电子结构相关工具与分析

```python
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import (
    BSDOSPlotter,
    BSPlotter,
    BSPlotterProjected,
    DosPlotter,
)

# 获取能带数据
bs_vasprun = Vasprun("./bs/vasprun.xml", parse_projected_eigen=True)
bs_data = bs_vasprun.get_band_structure(line_mode=True)

# 能带绘制
bs_plot = BSPlotter(bs=bs_data)
bs_plot.get_plot()

# 获取态密度数据
dos_vasprun=Vasprun("./dos/vasprun.xml")
dos_data=dos_vasprun.complete_dos

# 态密度（总）绘制
dos_plot = DosPlotter(stack=False, sigma=0.5)
dos_plot.add_dos("Total", dos=dos_data)
dos_plot.get_plot()

# 态密度（投影到轨道 + 总）绘制
pdos_plot = DosPlotter(stack=False, sigma=0.5)
pdos_plot.add_dos("Total", dos=dos_data)
pdos_plot.add_dos_dict(dos_data.get_spd_dos())
pdos_plot.get_plot()

# 态密度（投影到元素 + 总）绘制
edos_plot = DosPlotter(stack=False, sigma=0.5)
edos_plot.add_dos("Total", dos=dos_data)
edos_plot.add_dos_dict(dos_data.get_element_dos())
edos_plot.get_plot()

# 态密度（元素投影到轨道 + 总）绘制
edos_plot = DosPlotter(stack=False, sigma=0.5)
pdos_Nb = dos_data.get_element_spd_dos("Nb")
dos_plot.add_dos("Nb(s)", dos=pdos_Nb[OrbitalType.s])
dos_plot.add_dos("Nb(p)", dos=pdos_Nb[OrbitalType.p])
dos_plot.add_dos("Nb(d)", dos=pdos_Nb[OrbitalType.d])
edos_plot.get_plot()

# 能带 + 态密度绘制
bsdos_plot = BSDOSPlotter(bs_projection=None, dos_projection=None)
bsdos_plot.get_plot(bs=bs_data, dos=dos_data)
```


---

### pymatgen.analysis

#### structure_matcher

结构相似度

```python
from pymatgen.analysis.structure_matcher import StructureMatcher

sm = StructureMatcher()
sm.fit(structure1, structure2)
```


---

#### eos

- 类：`BirchMurnaghan`、`Birch`、`Murnaghan`、`PourierTarantola`、`Vinet` 等

```python
from pymatgen.analysis.eos import BirchMurnaghan


eos = BirchMurnaghan(volumes=..., energies=...)
eos.fit()      # 拟合

eos.e0         # 平衡能量拟合值
eos.b0_GPa     # 体模量B拟合值
eos.v0         # 平衡体积拟合值
eos.results    # 

eos.plot()     # 绘制 EOS 拟合曲线     
```


---

#### interface

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

#### elasticity

```python
# 施加正应变/剪切应变，生成变形后的结构
from pymatgen.analysis.elasticity import DeformedStructureSet

DeformedStructureSet()
```


---

#### electronic_structure

pymatgen 电子结构相关分析很多都是建立在 vasprun.xml 文件中提取数据之上的（与 vaspkit 有不同）


---

#### phase_diagram

- 无法直接使用 `pymatgen.entries` 中的 `Entry` 类初始化，会报错，`energy` 参数为 `ABC` 抽象类型（Doc 有提及），而是用 `pymatgen.analysis.phase_diagram` 中的 PDEntry 类初始化
- label 字体大小无法调节：[How control fontsize in PDPlotter? - pymatgen - Materials Science Community Discourse](https://matsci.org/t/how-control-fontsize-in-pdplotter/36715)

```python
# 绘制相图 Convex Hull
from pymatgen.analysis.phase_diagram import PDEntry, PhaseDiagram
from pymatgen.core.composition import Composition

entry1 = PDEntry(composition=..., energy=...)
entry2 = ...
...

entries = [entry1, entry2, ...]

phasediagram = PhaseDiagram(entries)

phasediagram                       # 稳定相
phasediagram.stable_entries        # 稳定相及其对应能量
phasediagram.get_decomposition()   # 获取特定构型成分分解成哪些稳定相及其比例

# label 字体大小无法修改 可能会导致有重叠
ax = phasediagram.get_plot(
    backend="matplotlib",      # 绘图后端；ploty 或 matplotlib
    show_unstable=False,       # 是否显示非稳定构型
    # label_stable=False,      # 是否显示 label
    )

ax.figure.savefig()
```


---

#### diffraction

XRD 绘制：

- [Pymatgen XRD Plot - Stack Overflow](https://stackoverflow.com/questions/53439514/pymatgen-xrd-plot)
- [How to get the hkl or hkil indices from calculated xrd pattern - pymatgen - Materials Science Community Discourse](https://matsci.org/t/how-to-get-the-hkl-or-hkil-indices-from-calculated-xrd-pattern/45920)

```python
from pymatgen.analysis.diffraction.xrd import XRDCalculator

c = XRDCalculator()

# 方法
get_plot(structure)            # 绘制结构的 XRD

get_pattern(structure)         # 获取衍射花样
get_pattern(structure).hkls
get_pattern(structure).d_hkls
```


---

### pymatgen.symmetry.analyzer

#### SpacegroupAnalyzer

```python
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

sga_analyzer = SpacegroupAnalyzer(structure, symprec=...,)
# 默认对称性精度为 0.01
# 弛豫后的结构，精度可适当放宽（0.1 为 MP 使用的精度）

# 方法
get_conventional_standard_structure()   # 获取单胞
get_primitive_standard_structure()      # 获取原胞
get_symmetrized_structure()             # 获取对称性结构
get_symmetry_dataset()                  # 获取结构的对称性数据集
get_crystal_system()                    # 获取晶系（源码含空间群与晶系之间的关系） 
get_space_group_number()                # 空间群编号（编号越小，对称性越低）
get_space_group_symbol()                # 空间群符号

# 寻找构型中的等同原子
symmetry_dataset = sga.get_symmetry_dataset()
symmetry_dataset['equivalent_atoms']
```

空间群与晶系之间的关系：[Space group - Wikipedia](https://en.wikipedia.org/wiki/Space_group)

```yaml
1-2: "triclinic"
3-15: "monoclinic"
16-74: "orthorhombic"
75-143: "tetragonal"
143-167: "trigonal"
168-194: "hexagonal"
195-230: "cubic"
```


---

### pymatgen.transformations

- `standard_transformations` 和 `advanced_transformations` 定义的类，都有 `apply_transformation()` 方法

```python
from pymatgen.transformations.standard_transformations import 
from pymatgen.transformations.advanced_transformations import SQSTransformation


# 方法
apply_transformation(structure)


# 枚举无序结构
# reference: https://github.com/luzihen/pymatgen_examples/blob/master/enumerate_ordering.py
from pymatgen.transformations.advanced_transformations import EnumerateStructureTransformation

enum = EnumerateStructureTransformation()
enumerated = enum.apply_transformation(structure, return_ranked_list=100)  # return no more than 100 structures
```


---

### pymatgen.phonon

>[https://pymatgen.org/pymatgen.phonon.html](https://pymatgen.org/pymatgen.phonon.html)


---

### API

- 参考：
    - [新版和老版Materials Project API使用指南 - Jun's Blog](https://www.jun997.xyz/2022/04/10/b438dad131c8.html)
    - [利用Materials Project的API下载结构文件](https://zhuanlan.zhihu.com/p/618452536)

- 调用 MP API 获取 MP 数据

- pymatgen 新 API：
    - API Key 获取：[Materials Project - API](https://materialsproject.org/api)
    - 官方教程：[Getting Started - Materials Project Documentation](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)

- 安装

```bash
pip install -U mp_api
```

- 新 API 使用

```python
# 新 API 模块导入
from mp_api.client import MPRester

with MPRester("api-key") as mpr:
    docs = mpr.materials.summary.search(...)

    # 查看可获取内容的字段，可用做筛选 query data 的参数
    mpr.materials.summary.available_fields

    # 根据元素获取 ComputedStructureEntry
    mpr.get_entries_in_chemsys()

    # 能带、DOS
    mpr.get_bandstructure_by_material_id()
    mpr.get_dos_by_material_id()

    # 声子
    mpr.get_phonon_bandstructure_by_material_id()
    mpr.get_phonon_dos_by_material_id()

    # 相图（可绘制二、三、四元相图）
    mpr.materials.thermo.get_phase_diagram_from_chemsys(chemsys=...,)
    chemsys="Ti-Al"          # 二元
    chemsys="Ti-Al-Nb"       # 三元
    chemsys="Ti-Al-Nb-Zr"    # 四元



# search() 参数
material_ids=["mp-149"]  # 根据材料 ID
chemsys="Si-O",          # 仅含 Si O 两种元素的材料
elements=["Si", "O"]     # 至少含 Si O 两种元素的材料
has_props=["dos"]        # 是否有该性质
fields=["band_gap"]      # 字段
is_stable=True           # 是否为稳定材料


# fields 参数常用字段
material_id                # MP 对该材料标注的 ID；需 str()
composition_reduced        # 成分（约化）；需 as_dict()
formula_pretty             # 化学式（约化）
structure                  # 结构
symmetry
        .crystal_system    # 晶系；需 str()
        .symbol            # 空间群
nsites                     # 构型原子数
energy_per_atom            # 能量/原子
formation_energy_per_atom  # 形成能/原子
energy_above_hull          # 形成能与在 Hull 上的形成能差值
is_stable                  # 材料是否是稳定的
fields_not_requested       # 列出未请求的字段
```

- 旧 API 使用

```python
# 旧 API模块导入
from pymatgen.ext.matproj import MPRester

# 从 MP 获取结构
with MPRester("api-key") as mpr:

    mpr.get_structure_by_material_id()  # 根据材料 ID 获取结构
    mpr.get_download_info()             # 获取来自 NoMaD repository 的裸 VASP 输出文件链接
    mpr.get_gb_data()                   # 获取晶界数据
```
