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
categories:
  - 科研工具
date: 2023-10-18 09:00:00
abbrlink: "12496"
password:
---

# pymatgen 安装与使用

## 介绍

- 用于表示 Element、Site、Structure、Molecule 的高度灵活的类。
- 文件输入/输出支持广泛，如 VASP、ABINIT、CIF、Gaussian、XYZ 等（主要依靠 Open Babel 包）。
- 强大的分析工具，包括生成相图、Pourbaix 图、扩散分析、反应等。
- 电子结构分析，如态密度和能带结构。
- 集成 Materials Project REST API、Crystallography Open Database 等其他外部数据源
- 代码文档详细

---

### 参考资料

- pymatgen 实例代码：[GitHub - materialsvirtuallab/matgenb: Jupyter notebooks demonstrating the utilization of open-source codes for the study of materials science.](https://github.com/materialsvirtuallab/matgenb)
- [Materials Methodology - Materials Project Documentation](https://docs.materialsproject.org/methodology/materials-methodology)（该网址包含了 pymatgen 在材料相关计算中用的具体参数及其说明：如，截断能为 520eV 是由元素周期表所有元素中最大截断能的 1.3 倍得到的）

- material project workshop:
	- 2021：[The Materials Project Workshop](https://workshop.materialsproject.org/)
	- 2018~2020：[Releases · materialsproject/workshop](https://github.com/materialsproject/workshop/releases)
	- 2017：[GitHub - materialsproject/workshop-2017: Assets for the 2017 Materials Project workshop](https://github.com/materialsproject/workshop-2017)
	- 2016：[GitHub - materialsproject/workshop-2016: Assets for the Materials Project workshop in Aug 2016](https://github.com/materialsproject/workshop-2016)

workshop 2020 和 2021 的内容绝大部分相似，lesson3 分别为表面和界面
workshop 2018 和 2019 的内容相似（对 atomate 的讲解稍微详细些）


MP 分子 DFT code 用的是 Q-Chem

```python
from monty.serialization import loadfn, dumpfn

# 对 json/yaml/msgpack 等文件格式进行 serialization
```


```python
import pymatgen.core
import sys

# 查看 pymatgen 版本
pymatgen.core.__version__
# 查看 pymatgen 安装路径
pymatgen.core.__file__

sys.version  # 查看 python 版本
```

Molecule 类的输入参数：`species` 和 `coords`，关键字参数有：`charge`、 `spin_multiplicity`、 `validate_proximity` 和 `site_properties`

Structure 类还需指定 `lattice` 输入参数

Molecule 类的 `coords` 参数值需是 Cartesian 坐标形式，Structure 类的可以是 Cartesian 和分数两种坐标形式

```python
# Molecule 本质上是 Site objects 的列表
# Structure 本质上是 PeriodicSites objects 的列表
# 可以像 list 一样操作 Molecule 和 Structure

# Site object 属性
coords
specie

# Element
average_ionic_radius

# Composition
alphabetical_formula
chemical_system

# Structure
volume
frac_coords
cart_coords
symbol_set
composition.items()
lattice
density
num_sites
composition.num_atoms
center_of_mass  # 质心

get_space_group_info()

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

from pymatgen.core.lattice import Lattice

# lattice 构建
Lattice([[5, 0, 0], [0, 5, 0], [0, 0, 5]])
Lattice.from_parameters(5, 5, 5, 90, 90, 90)
Lattice.cubic(5)
```


- [x] pymatgen structure 如何通过 structure 来生成 potcar？
解决方法：通过 Poscar 类得到 structure 的元素种类，之后与 PBE 泛函的元素进行比对，之后用 Potcar 类写入 POTCAR（生成新的之前需删掉原来的 POTCAR 文件）



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


`MSONable` 类：MSON（Monty JSON）； MSONable 对象必须实现 `as_dict()` 方法，该方法须返回可序列化为 JSON 的字典，且须支持无参数。静态方法 `from_dict()`，从 `as_dict()` 方法生成的字典中重建对象。`as_dict()` 方法应该包含 “@module” 和 “@class” 键，这将允许 MontyEncoder 动态反序列化该类。


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

- POTCAR 设置

- [change log](https://pymatgen.org/change_log.html)（代码 bug 修复，新功能添加等，可以关注）

- [pymatgen 插件和外部工具](https://pymatgen.org/addons)


- 兼容性：需对进行 `from pymatgen import <something>` 修改（v2022.0.0 版本开始）

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

## 使用

使用：[https://pymatgen.org/usage.html](https://pymatgen.org/usage.html)

---

### CLI

>不是太好用，建议直接写脚本

所有子命令：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282023900.png)


所有子命令的 help：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282037019.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282037724.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282038651.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282039179.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282039484.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282041689.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405282040573.png)


```bash
pmg sub-command -h  # 查看子命令帮助

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
# Make a supercell
structure.make_supercell([2, 2, 2])
structure * (2, 2, 2)

# Get a primitive version of the Structure
structure.get_primitive_structure()

# Interpolate between two structures to get 10 structures (typically for NEB calculations.)
structure.interpolate(another_structure, nimages=10)
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

简单的变换操作：如添加和删除位点，替换结构中的元素，到更高级的一对多的转换。

典型用法：

```python
from pymatgen.transformations.standard_transformations import RemoveSpecieTransformations

structure = ...

# 添加具体的变换操作
t = RemoveSpeciesTransformation(["X"])

# 施加变换操作到构型上
modified_structure = t.apply_transformation(structture)
```


---

>[ug-materials-simulation/pymatgen/包和模块结构.ipynb at master · xiangzhouzhang/ug-materials-simulation · GitHub](https://github.com/xiangzhouzhang/ug-materials-simulation/blob/master/pymatgen/%E5%8C%85%E5%92%8C%E6%A8%A1%E5%9D%97%E7%BB%93%E6%9E%84.ipynb)

包 (package、subpackage) 是目录, 模块 (module、submodule) 是文件; import 既可以导入包和子包, 也可以导入模块和子模块;


如何学习模块中的函数或者类:

语法 (一句话概括, 参数及参数类型, 返回值及返回值类型); 包含的方法或属性; 继承的基类 应用示例;




pymatgen 典型工作流

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202310231537005.png)

---

### 其他

`Structure` 没有 `wrap()` 方法，ase 有：[pymatgen - What Does the coordinate list next to the cartesian coordinates of an atom represent in neighbor\_list - Stack Overflow](https://stackoverflow.com/questions/54356049/what-does-the-coordinate-list-next-to-the-cartesian-coordinates-of-an-atom-repre)

```python
# 待了解
get_wigner_seitz_cell()

read_neb()

MITNEBSet class
```


复杂结构 pymatgen 无法将其单胞转化成原胞（Al3Ni）



解析 VASP 计算目录：[Automated DFT - The Materials Project Workshop](https://workshop.materialsproject.org/lessons/05_automated_dft/Lesson/#parsing-directories-with-atomate-drones)

```python
from atomate.vasp.drones import VaspDrone

drone = VaspDrone()
task_doc = drone.assimilate(path="./example_VASP_Al16Cr10")

print(task_doc.keys())
```


---

## 常用模块

### pymatgen.core

#### structure

Structure 类相关属性和方法
```python
remove_species()
replace_species()

num_sites   # 原子数
formula 
compsition
```


---

#### surface

pymatgen 表面生成无法指定具体的层数
>[https://matsci.org/t/building-a-slab-and-interface/45317](https://matsci.org/t/building-a-slab-and-interface/45317)




`get_symmetrically_distinct_miller_indices()` - 获取指定晶面指数中的最大数值下其对称性非等同的所有晶面指数

`get_symmetrically_equivalent_miller_indices()` - 获取指定晶面指数下其对称性等同的所有晶面指数

`get_d()` - 获取层间距

`SlabGenerator` 类 - 构建指定晶面指数的 slab 模型
`get_slabs()` 方法 - 类初始化后，获取 slab 构型，可通过其得到该 slab 模型下不同终端的数量（`len()`）


---

#### composition

```python
from pymatgen.core.composition import Composition

Composition("LiFePO4").as_dict()
```


---

#### periodic_table

```python
from pymatgen.core.periodic_table import Element

# 元素周期表 TUI 绘制
Element.print_periodic_table()

ele = Element("Nb")

# 查看元素价电子排布
ele.electronic_structure
ele.is_metal
```


---

#### sites

---

#### units

---

### pymatgen.io.ase

`AseAtomsAdaptor`：将 ase 中的 `atoms` 类与 pymatgen 中的 `Structure` 类互相转换

```python
from pymatgen.io.ase import AseAtomsAdaptor

# atoms 转 Structure
AseAtomsAdaptor.get_structure()

# Structure 转 atoms
AseAtomsAdaptor.get_atoms()
```


---

### pymatgen.io.atat

只有 Mcsqs 类


---

### pymatgen.io.vasp.help

查看 VASP 参数 help

```python
from pymatgen.io.vasp.help import VaspDoc

# 静态方法
VaspDoc.get_incar_tags()
VaspDoc.get_help("IBRION")

# 需初始化
VaspDoc().print_help("IBRION")
# 展示 HTML 格式内容
VaspDoc().print_jupyter_help("IBRION")
```

### pymatgen.io.vasp.inputs

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

#### Incar

在解析 INCAR 文件时，得到的字典的键和值都是字符串，需要对 INCAR 中不同参数的键的值的类型进行正确的转换，因此定义了 `proc_val()` 函数。



---

#### Kpoints

automatic() length
automatic_density() grid_density
automatic_density_by_vol() reciprocal_density




---

#### Poscar

WIP…


---

#### Potcar

读取和写入 POTCAR 文件的 object，由 PotcarSingle object 的列表组成


---

#### PotcarSingle

单个 POTCAR object



---

### pymatgen.io.vasp.sets

MPRelaxSet、MPStaticSet 等类均继承于 VaspInputSet，这些 InputSet 都有 `write_input()` 方法

```python
write_input(output_dir=..., potcar_spec=True)
```

`pymatgen/io/vasp/MPRelaxSet.yaml`：设置了默认的弛豫计算所有输入文件参数

`pymatgen/io/vasp/VASPIncarBase.yaml`：设置了 INCAR 文件中的 MAGMOM 元素磁矩参数


---


MPStaticSet 有设置 EDIFF 10-4

没有 MPStaticSet.yaml

reciprocal_density=100


基于之前的 VASP 计算目录中生成静态计算输入文件
```python
from pymatgen.io.vasp.sets import MPStaticSet

# from_prev_calc 为静态方法
static_set = MPStaticSet.from_prev_calc("./VASP_Al16Cr10_example/")

print(static_set.incar)
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

读取、执行、写 VASP 的输出文件

`pymatgen/io.vasp/outputs.py`



---

#### Outcar

```python
read_neb()
```

---

#### Oszicar

WIP…


---

#### Vasprun

WIP…

```python
ionic_steps

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

类：`BirchMurnaghan`、`Birch`、`Murnaghan`、`PourierTarantola`、`Vinet` 等


```python
from pymatgen.analysis.eos import BirchMurnaghan
import pandas as pd

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

eos.plot()
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

```


---

#### electronic_structure

pymatgen 电子结构相关分析很多都是建立在 vasprun.xml 文件中提取数据之上的（与 vaspkit 有不同）


---

#### phase_diagram

- 无法直接使用 `pymatgen.entries` 中的 `Entry` 类初始化，会报错，`energy` 参数为 `ABC` 抽象类型（Doc 有提及），而是用 `pymatgen.analysis.phase_diagram` 中的 PDEntry 类初始化
- label 字体大小无法调节：[How control fontsize in PDPlotter? - pymatgen - Materials Science Community Discourse](https://matsci.org/t/how-control-fontsize-in-pdplotter/36715)

```python
# 绘制相图 convex hull
from pymatgen.analysis.phase_diagram import PDEntry, PhaseDiagram
from pymatgen.core.composition import Composition

entry = PDEntry(composition=, energy=)

entries = [entry, entry, ...]

phasediagram = PhaseDiagram(entries)

# 输出稳定相
print(phasediagram)

# 输出稳定相及其对应能量
print(phasediagram.stable_entries)

# 获取特定构型成分分解成哪些稳定相及其比例
phasediagram.get_decomposition()

# label 字体大小无法修改 可能会导致有重叠
ax = phasediagram.get_plot(
	backend="matplotlib",
	show_unstable=False,
	# label_stable=False,  # 不显示 label
	)

ax.figure.savefig("XXX.png")
```


---

#### diffraction

XRD 绘制：

- [Pymatgen XRD Plot - Stack Overflow](https://stackoverflow.com/questions/53439514/pymatgen-xrd-plot)
- [How to get the hkl or hkil indices from calculated xrd pattern - pymatgen - Materials Science Community Discourse](https://matsci.org/t/how-to-get-the-hkl-or-hkil-indices-from-calculated-xrd-pattern/45920)

```python
from pymatgen.analysis.diffraction.xrd import XRDCalculator

c = XRDCalculator()

c.get_plot(structure)

# 获取衍射花样
c.get_pattern(structure)
c.get_pattern(structure).hkls
c.get_pattern(structure).d_hkls
```


---

### pymatgen.symmetry.analyzer

#### SpacegroupAnalyzer

寻找构型中的等同原子
```python
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

sga = SpacegroupAnalyzer(structure)

# symmetrized_structure = sga.get_symmetrized_structure()

symmetry_dataset = sga.get_symmetry_dataset()
symmetry_dataset['equivalent_atoms']
```



---

### pymatgen.transformations

#### standard_transformations

WIP…



---

### pymatgen.phonon

>[https://pymatgen.org/pymatgen.phonon.html](https://pymatgen.org/pymatgen.phonon.html)



---

### API

- 调用 MP API 获取 MP 数据
- pymatgen 新 API：[Materials Project - API](https://materialsproject.org/api)、[Getting Started - Materials Project Documentation](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)

- 安装

```bash
pip install -U mp_api
```

- 使用

```python
# 新 API
from mp_api.client import MPRester

with MPRester("api-key") as mpr:
    ...

# 查看可获取内容的字段，这些字段可用做筛选 query data 的参数
mpr.summary.available_fields
```

```python
# 旧 API
from pymatgen.ext.matproj import MPRester

# 从 MP 获取结构
with MPRester("api-key") as mpr:
    struct = mpr.get_structure_by_material_id("mp-149")
```

使用旧 API 出现的 warning
```bash
***/lib/python3.11/site-packages/pymatgen/ext/matproj_legacy.py:166: UserWarning: You are using the legacy MPRester. This version of the MPRester will no longer be updated. To access the latest data with the new MPRester, obtain a new API key from https://materialsproject.org/api and consult the docs at https://docs.materialsproject.org/ for more information.
  warnings.warn(
```


>[利用Materials Project的API下载结构文件](https://zhuanlan.zhihu.com/p/618452536)

模块具体用法


`get_download_info()`：获取来自 NoMaD repository 的裸 VASP 输出文件链接

`get_gb_data()`：获取晶界数据

- [ ] 如何通过 API 获得 equation of state 和晶界能
