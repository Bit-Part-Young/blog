---
title: 结构建模
top: false
cover:
toc: true
mathjax: true
summary: 结构建模
description: 结构建模
tags:
  - pymatgen
  - ASE
  - atomsk
  - PyXtal
  - latgen
  - Material-Studio
  - OVITO
  - VESTA
categories:
  - 科研工具
  - 结构建模
date: 2023-10-15 09:30:00
abbrlink: 381006
password:
---

# 结构建模

## 结构建模常用工具

- [pymatgen](https://pymatgen.org/)
- [ASE](https://wiki.fysik.dtu.dk/ase/)
- [Atomsk](https://atomsk.univ-lille.fr/)
- [latgen](https://github.com/lingtikong/latgen)
- [PyXtal](https://pyxtal.readthedocs.io/)
- Material Studio（Win + Linux）

- 其他：
    - [GitHub - orex/supercell: The program allows you to create regular structure supercell from cif file with partial occupancy and/or substitutions.](https://github.com/orex/supercell)

    - [GitHub - dkratzert/StructureFinder: A crystal structure finder written in PyQt5 and Python3](https://github.com/dkratzert/StructureFinder)

    - [CrystalMaker Software: Crystal & Molecular Structures Modelling and Diffraction](https://crystalmaker.com/)

- 缺陷构型生成：[GitHub - nanyanshouhu/Defect\_generator](https://github.com/nanyanshouhu/Defect_generator)

- 计算材料数据库
    - [NOMAD CoE - NOMAD CoE](https://www.nomad-coe.eu/nomad-coe/)
    - [OQMD](https://www.oqmd.org/)

- 金属建模
    - [金属建模----任意晶向的FCC, BCC单晶建模](https://mp.weixin.qq.com/s/b9IJAirqQYQ3u_vtisDxVw)
    - [文献中常见金属模型建模方法总结-双晶及双相篇](https://mp.weixin.qq.com/s/5iW4ZwFH6xWq_B3pyXx3Vg)



---

## 构型可视化工具

- [OVITO](https://www.ovito.org/)
- [VESTA](https://jp-minerals.org/vesta/en/download.html)
- [VMD](https://www.ks.uiuc.edu/Research/vmd/)
- [OpenMX Viewer](https://www.openmx-square.org/viewer/index.html)

- [如何实现结构原子可视化？](https://mp.weixin.qq.com/s/zfzZ7kRXsXKe9yhyLcPuYQ)

- 用于晶体、分子结构可视化的 Jupyter 组件：[GitHub - nglviewer/nglview: Jupyter widget to interactively view molecular structures and trajectories](https://github.com/nglviewer/nglview)

- 结构可视化
    - MoS2：[Molybdenum Disulfide - MoS2](https://www.chemtube3d.com/ss-mos2/)
    - 金刚石、石墨、C60、碳纳米管：[Introductory Structures Allotropes of Carbon (Diamond and Graphite) and Pentacene](https://www.chemtube3d.com/claydencarbonallotropes/)
    - HCP：[Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/)
    - perovskite：[CaTiO3 - Perovskite: Interactive 3D Structure](https://www.chemtube3d.com/_perovskitefinal/)

- VMD 可计算 RDF、统计键长、可视化磁化密度（magnetization denisty）



---

## 结构分析工具

- crysinfo 程序（孔老师）：6a 选项查看 Wyckoff letter

- 结构原型分析：[GitHub - chuanxun/StructurePrototypeAnalysisPackage: Structure Prototype Analysis Package can analyze symmetry and compare similarity of a large number of atomic structures.](https://github.com/chuanxun/StructurePrototypeAnalysisPackage)

 - CIF 格式文件分析：[GitHub - bobleesj/cifkit: High-throughput .cif analysis made easy. Visit: https://bobleesj.github.io/cifkit/](https://github.com/bobleesj/cifkit)

- 含缺陷超胞生成、前/后处理和分析：[Doped code 介绍](https://mp.weixin.qq.com/s/r3ZabHXYAn2HJgyFxFmA-w)

- Crystal Toolkit 可视化分析工具：
    - 源码：[GitHub - materialsproject/crystaltoolkit](https://github.com/materialsproject/crystaltoolkit)
    - 网页：[Crystal Toolkit - Materials Project](https://next-gen.materialsproject.org/toolkit)

- AFLOW 线上工具：[AFlow - Automatic - FLOW for Materials Discovery](https://aflowlib.org/aflow-online/)；功能
    - 构型文件转换
    - 对称性
    - 结构对比
    - Coordination corrected enthalpies (CCE)
    - K 点
    - Partial OCCupation (POCC)
    - 间隙
    - XRD

- cifcell：将 CIF 构型格式文件转换成其他计算程序格式（较实用）
    - [GitHub - torbjornbjorkman/cif2cell: Generating geometries for electronic structure calculations from CIF files.](https://github.com/torbjornbjorkman/cif2cell)

```bash
cif2cell input.cif -p vasp --vasp-cartesian-positions
```

- findsym：生成有对称性的 cif 文件（ISOTROPY 中的工具之一）
    - [FINDSYM](https://stokes.byu.edu/iso/findsym.php)
    - [如何获得有对称性的cif文件？FINDSYM来解决了。](https://zhuanlan.zhihu.com/p/496042890)
    - [ISOTROPY Software Suite](https://stokes.byu.edu/iso/isotropy.php)

```bash
findsym_cifinput input.cif > input1.cif  # 让 findsym 读起来更方便
findsym input1.cif > output.cif          # 寻找对称性并输出
```

- [全网最全的模拟XRD衍射谱教程](https://mp.weixin.qq.com/s/fF6mKPl9NAqv4pfbzCZyLw)



---

## 构型文件格式

- 注意事项：
    - cif 格式可含对称性、不含对称性两种（前者晶体学信息更全），大部分程序将构型格式转换成 cif 都是不含对称性的（空间群为 P1，即写入所有原子）
    - 原子类型标记：xsf 使用原子序数，cfg 使用相对原子质量和元素符号（使用 atomsk 模型构建时，需要用到中间构型，建议避免用 lmp 以吞掉原子类型）

- 常见构型文件格式：[File input and output — ASE documentation](https://wiki.fysik.dtu.dk/ase/ase/io/io.html)
    - 原子坐标为分数坐标的格式：imd

```bash
POSCAR            # VASP
CONTCAR           # VASP
XDATCAR           # VASP 轨迹文件
.vasp             # VASP
.poscar           # VASP；Material Project 下载的构型格式
.lammpstrj        # LAMMPS 轨迹文件
.xsd              # Material Studio
.cif              # Crystallographic Information File
.xsf              # XCrySDen
.cfg              # AtomEye；configuration 的缩写
.imd              # IMD
.cell             # CASTEP
.stru             # ABACUS
.cube             # Gaussian
.pdb              # Protein Data Bank
.car              # DMol3；Material Studio 可读
.arc              # DMol3；类似轨迹文件；Material Studio 可读
```

- xyz 格式内容示例（第二行为空或含注释）

```bash
# 第二行内容为空
2

Nb      0.000000000000000      0.000000000000000      0.000000000000000
Nb      1.660000000000000      1.660000000000000      1.660000000000000
```

- extxyz 格式内容示例（第二行有晶体学信息）
    - 第 1 行：原子数目
    - 第 2 行：必须有 Lattice、Properties 参数；常见参数有 pbc、energy、stress、virial 等
        - `Properties=property_name:data_type:number_of_columns` 规定原子信息数组每一列的信息
        - 常用 `property_name`：species、pos、Z、mass、force、charge
        - `data_type`：分为 S、I、R、L 分别对应 string、integer、real、logical
    - 第 3+ 行：与 Properties 对应的列

```bash
# extxyz 基本格式示例
32
Lattice="6.57 0.0 0.0 0.0 6.57 0.0 0.0 0.0 11.88" Properties=species:S:1:pos:R:3 pbc="T T T"
Nb       1.09062000       4.37562000      10.09800000
Nb       2.19438000       1.09062000      10.09800000
```

- LAMMPS data 文件格式内容示例

```bash
# atom_style 为 atomic 时的内容
Nb5Si3_alpha.lammps-data (written by ASE)

32 	 atoms
2  atom types
0.0      6.5700000000000003  xlo xhi
0.0      6.5700000000000003  ylo yhi
0.0      11.880000000000001  zlo zhi


Atoms

     1   2      1.0906200000000001      4.3756200000000005      10.098000000000001
     2   2      2.1943800000000002      1.0906200000000001      10.098000000000001
```

- LAMMPS dump 文件格式内容示例

```bash
ITEM: TIMESTEP                                    # 第 N 个时间步长时输出的构型
0
ITEM: NUMBER OF ATOMS                             # 构型原子数
3400
ITEM: BOX BOUNDS pp pp pp                         # x y z 轴起始、终止坐标
0.0000000000000000e+00 3.6150000000000006e+01
0.0000000000000000e+00 3.6150000000000006e+01
0.0000000000000000e+00 7.2300000000000011e+01
ITEM: ATOMS id type xs ys zs                      # 原子 ID、类型、分数坐标等；可通过 dump 命令自定义输出所需内容
1 1 0 0 0.3
2 1 0.05 0.05 0.3
5 1 0.1 0 0.3
...
```



---

## 结构建模

- 元素周期表里元素的晶体结构：[Periodic table (crystal structure) - Wikipedia](https://en.m.wikipedia.org/wiki/Periodic_table_(crystal_structure))

- Springer Materials：[https://materials.springer.com/](https://materials.springer.com/)

- [Aflow Advanced Search](http://aflowlib.duke.edu/search/ui/search/)

- MP 等材料数据库中的结构文件有时对称性不一定正确，查看该数据库中已计算的性质是否与文献中的接近，以及最好进行静态计算检验一下


---

### 常见简单结构

- 简单结构包括：BCC、FCC、HCP、Diamond

- HCP 结构单胞原子位置有两种形式：
    - 一个原子在原点，另一个在胞内：latgen 和 ASE，(0.0 0.0 0.0)、(2/3 1/3 0.5)
    - 两个原子均在胞内：pymatgen 和 PyXtal，(1/3 2/3 1/4)、(2/3 1/3 3/4)
    - 两种形式无本质区别，两者可通过周期性平移进行互相转化
    - [Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/) 有这两种形式的可视化

- 金刚石结构：
    - 原胞原子位置：
        - latgen、ASE：(0.0 0.0 0.0)、(0.25 0.25 0.25)
        - pymatgen：(0.0 0.0 0.0)、(0.75 0.75 0.75)
        - PyXtal：(0.0 0.0 0.0)、(0.75 0.75 0.75)
    - 三种形式无本质区别，两者可通过周期性平移进行互相转化

- HCP、Diamond 常用原子位置分数坐标写法（与 wyckoff positions 不同）

```bash
# HCP 常用原子位置分数坐标写法（ASE、latgen、atomsk）
Mg2
1.0
    2.870000    0.000000    0.000000
   -1.435000    2.485493    0.000000
    0.000000    0.000000    3.500000
Mg
   2
Direct
0.000000    0.000000    0.000000 Mg
0.666667    0.333333    0.500000 Mg


# 金刚石结构常用原子位置分数坐标写法（ASE、latgen、atomsk）
Sn8
1.0
   6.660000    0.000000    0.000000
   0.000000    6.660000    0.000000
   0.000000    0.000000    6.660000
Sn
8
direct
   0.00    0.00    0.00
   0.50    0.50    0.00
   0.00    0.50    0.50
   0.50    0.00    0.50
   0.25    0.25    0.25
   0.75    0.75    0.25
   0.75    0.25    0.75
   0.25    0.75    0.75
```

- BCC、FCC、HCP、Diamond 原胞基矢

```bash
# BCC 原胞基矢；原胞晶格常数 a*√3/2，轴间角 60
-0.5 0.5 0.5
0.5 -0.5 0.5
0.5 0.5 -0.5

# FCC/Diamond 原胞基矢；原胞晶格常数 a*√2/2，轴间角 109.471
0.0 0.5 0.5
0.5 0.0 0.5
0.5 0.5 0.0

# HCP 原胞基矢
0.5a -sqrt(3)/2a 0
0.5a sqrt(3)/2a 0
0 0 c
```


---

### 石墨、石墨烯

- 石墨、石墨烯构建：[Atomsk - Tutorial - Graphene and Nanotubes](https://atomsk.univ-lille.fr/tutorial_nanotubes.php)

- 石墨：六方结构；a=2.46 Å，c=6.7 Å

```bash
#  参考文献
https://doi.org/10.1016/B978-0-12-385469-8.00002-2
https://doi.org/10.1073/pnas.2134173100

# 石墨 POSCAR 文件
graphite
1.0
   2.4638000000000000    0.0000000000000000    0.0000000000000000
  -1.2319000000000000    2.1337133898440999    0.0000000000000000
   0.0000000000000000    0.0000000000000000    6.6959999999999997
C
4
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 C
   0.3333333333333334    0.6666666666666667    0.0000000000000000 C
   0.0000000000000000    0.0000000000000000    0.5000000000000000 C
   0.6666666666666666    0.3333333333333334    0.5000000000000000 C
```

- 石墨烯：二维六方结构结构；石墨单层

```bash
# 参考文献
CASTRO NETO A H, GUINEA F, PERES N M R, 等, 2009. The electronic properties of graphene\[J]. Reviews of Modern Physics, 81(1): 109-162.

石墨烯 POSCAR 文件
graphene
1.0
   2.4680000000000000    0.0000000000000000    0.0000000000000000
  -1.2340000000000000    2.1373506965399902    0.0000000000000000
   0.0000000000000000    0.0000000000000000   15.0000000000000000
C
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 C
   0.3333333333333349    0.6666666666666697    0.0000000000000000 C
```


---

### 碳纳米管

- [Atomsk - Tutorial - Graphene and Nanotubes](https://atomsk.univ-lille.fr/tutorial_nanotubes.php)

- [VASP视频教程-搭建模型-用vnl或ms搭建模型卷曲纳米碳管\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV14M4ye8EVX)

- [VASP 高级教程 7 -- 使用 VESTA 构建纳米管](https://mp.weixin.qq.com/s/6WO5A8Qa-XDyAEM0AbQVhQ)
    - 先构建纳米带，再使其卷曲形成纳米管


---

### 复杂结构

- 方法 1：在文献中查找该结构的晶体学信息，若提到 prototype structure（原型结构），可在数据库（AFLOW、MP、Springer Materials、ICSD 等）中找到对应的 cif 文件（**需留意 Wyckoff position 是否一致或接近，某些含有变量，不同的具体结构变量值会不同**），再将晶格常数和原子种类进行替换，替换为要构建结构的信息

- 方法 2: 手动构建，需以下晶体学信息，使用 PyXtal，ASE，pymatgen 或 Material Studio 构建
    - 晶体结构（crystal structure）
    - 点阵参数（lattice parameter）
    - 空间群（space group number）
    - 原子位置（Wyckoff letter & Wyckoff position）

- 遇到的 Strukturbericht Designation 结构
    - [The A15 Structure](https://www.atomic-scale-physics.de/lattice/struk/a15.html)
    - [The NaCl (B1) Structure](https://www.atomic-scale-physics.de/lattice/struk/b1.html)
    - [The CsCl (B2) Structure](https://www.atomic-scale-physics.de/lattice/struk/b2.html)
    - [The Zincblende (B3) Structure](https://www.atomic-scale-physics.de/lattice/struk/b3.html)
    - [The Wurtzite (B4) Structure](https://www.atomic-scale-physics.de/lattice/struk/b4.html)
    - [The NiAs (B8\_1) Structure](https://www.atomic-scale-physics.de/lattice/struk/b8_1.html)
    - [The AuCd (B19) Structure](https://www.atomic-scale-physics.de/lattice/struk/b19.html)
    - [The Fluorite (C1) Structure](https://www.atomic-scale-physics.de/lattice/struk/c1.html)
    - [The Cu\_2Mg Cubic Laves Structure (C15)](https://www.atomic-scale-physics.de/lattice/struk/c15.html)
    - [The hexagonal omega (C32) Structure](https://www.atomic-scale-physics.de/lattice/struk/c32.html)
    - [The AlFe\_3 (D0\_3) Structure](https://www.atomic-scale-physics.de/lattice/struk/d0_3.html)
    - [The D0\_19 (Ni\_3 Sn) Structure](https://www.atomic-scale-physics.de/lattice/struk/d0_19.html)
    - [The Al\_3 Ti (D0\_22) Structure](https://www.atomic-scale-physics.de/lattice/struk/d0_22.html)
    - [The CuAu (L1\_0) Structure](https://www.atomic-scale-physics.de/lattice/struk/l1_0.html)
    - [The Cu\_3Au (L1\_2) Structure](https://www.atomic-scale-physics.de/lattice/struk/l1_2.html)
    - [The CuTi\_3 (L6\_0) Structure](https://www.atomic-scale-physics.de/lattice/struk/l6_0.html)
    - Cr5B3：[AFLOW Prototype: A3B5\_tI32\_140\_ah\_cl](https://www.aflowlib.org/prototype-encyclopedia/A3B5_tI32_140_ah_cl.html)
    - Mn5Si3：[AFLOW Prototype: A5B3\_hP16\_193\_dg\_g](https://www.aflowlib.org/prototype-encyclopedia/A5B3_hP16_193_dg_g.html)

- 其他：
    - [构建任意形状超胞？](https://mp.weixin.qq.com/s/IxJ_7XXfhI3D0StJo_g9dw)
    - [构建根号n乘根号n的六角晶格(含代码)](https://mp.weixin.qq.com/s/UxAbaCxoH0WSLjLMbxi62A)
    - [转角电子学必备技能：构建转角结构实例](https://mp.weixin.qq.com/s/j6dARDTRI_4c6yiSijTvHQ)


---

### 表面

- 切复杂结构/高指数面的表面时，可优先使用 Material Studio 的 'Build -- Surfaces -- Cleave Surface' 功能，清晰直观，且能快速得到具体的坐标轴（用于 atomsk）

- 不同方法生成常见低指数面的表面模型的区别
    - FCC：(100)、(110) 面正交/立方，(111) 面六方
    - BCC：(100) 面正交/立方，(110)、(111) 面六方
    - HCP 除 (001) 面的结构是六方，其他面的结构均为四方或正交
    - atomsk 构建时，需要求坐标轴正交，因此生成的表面模型总是正交胞
    - ASE 中的部分表面模型总是正交胞，部分可指定为非正交或正交胞
    - latgen 可指定生成的表面模型为非正交或正交胞
    - pymatgen 生成的表面模型总不是正交胞（没有前三个工具好用）

- BCC、FCC、HCP 常见指数面的表面模型示意图
    - BCC/FCC (100)、(110) 面一个最小完整单元有 2 个原子层，(111) 面有 3 个原子层（正常是六方）
    - [1.3: Surface Structures- fcc Metals - Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Surface_Science_(Nix)/01%3A_Structure_of_Solid_Surfaces/1.03%3A_Surface_Structures-_fcc_Metals)
    - [1.4: Surface Structures- hcp Metals - Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Surface_Science_(Nix)/01%3A_Structure_of_Solid_Surfaces/1.04%3A_Surface_Structures-_hcp_Metals)
    - [1.5: Surface Structures- bcc metals - Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Surface_Science_(Nix)/01%3A_Structure_of_Solid_Surfaces/1.05%3A_Surface_Structures-_bcc_metals)

- 添加真空层
    - vaspkit 添加真空层，先加真空层数值，再将原子层移至 z 方向中间（1 \* vac）
    - ASE 中的 `center()` 函数添加真空层是分别往两边加（2 \* vac）
    - atomsk 添加的真空层是在上半部分（1 \* vac）

- 表面模型中 z 方向晶格常数数值计算（n 为 layer 数目，d 为层间距，vac 为真空层厚度）
    - ASE：(n-1) \* d + vac
    - atomsk：n \* d + vac
    - latgen：n \* d + vac（可指定为 n 或 n-1）

- 特殊的表面可能会发生重构现象（Si）

- BCC、FCC、Diamond、HCP 常见表面/位向的具体坐标轴
    - FCC 结构 2 奇 1 偶的晶向对应方向的盒子长度需除以 2
    - BCC 结构 3 奇的晶向对应方向的盒子长度需除以 2

```bash
# BCC、FCC、Diamond（也适用于 B2）

# BCC 单胞 2 个原子，FCC 4 个；均为 2 个原子层
# Diamond 单胞 8 个原子；4 个原子层
"[010]" "[001]" "[100]"            # (100) 面；立方

# BCC 单胞 4 个原子，FCC 2 个；均为 2 个原子层
# Diamond 单胞 4 个原子；4 个原子层
"[01-1]" "[011]" "[100]"           # (100) 面；正交

# BCC 单胞 4 个原子，FCC 2 个；均为 2 个原子层
# Diamond 单胞 4 个原子；2 个原子层
"[1-10]" "[001]" "[110]"           # (110) 面；正交

# BCC、FCC 单胞均为 6 个原子；均为 3 个原子层
# Diamond 单胞 6 个原子； 6 个原子层
"[1-10]" "[11-2]" "[111]"          # (111) 面；正交

# (111) 面；六方；[01-1] * 2 + [1-10] 转正交
"[01-1]" "[1-10]" "[111]"


# HCP
# 单胞 4 个原子；4 个原子层；层间距不相等
# 单胞边长 a c √3a
"[-12-10]" "[0001]" "[-1010]"      # (100) 面

"[0001]" "[1-100]" "[-1-120]"      # (110) 面

"[0001]" "[11-20]" "[1-100]"       # (-110) 面

# (101) 面、(112) 面，latgen 与 atomsk 生成的结构有很大不同，不确定
```

- 使用 VESTA 构建不同位向（本质还是找到晶向的具体坐标轴值）：[VASP 高级教程8 -- 使用 VESTA 切表面 surface slab](https://mp.weixin.qq.com/s/jBXwke0XTDZbloIU0HVlvw)

- LAMMPS 内置命令构建不同位向出现的问题：[好文：从源代码看 lammps 的建模 BUG](https://mp.weixin.qq.com/s/Q32HpdaFeO1ztI2EVuUDOw)
    - LAMMPS 的建模源代码里面没有提供对于特殊晶体取向的判断以修正最小周期长度，而 atomsk 提供了
    - 某些特殊的晶向指数, 在计算其最小的单位边长时, 是需要除以 2 的；BCC：1/2\[111\]、1/2\[531\]；FCC：1/2\[110\]、1/2\[112\]


---

### 界面/异质结

- 使用 Material Studio 的 'Build -- Build Layers' 功能

- [Materials Studio 入门到精通【16】简单界面模型的建立 - 知乎](https://zhuanlan.zhihu.com/p/346859236)

- [如何采用Materials Studio切晶面和建立界面模型\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Av411H7PS)

- [[建模与可视化] 求助Si和α-Al2O3材料界面计算的界面搭建问题 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-47013-1-1.html)

- [GitHub - aguang5241/Interface-Maker: A python3 code to create slabs and interfaces for first-principles calculations.](https://github.com/aguang5241/Interface-Maker)

- [GitHub - rzk1/heterojunction: Create surfaces and heterojunctions from two crystal structures](https://github.com/rzk1/heterojunction)

- 生成界面模型（Fortran 代码）：[Hepplestone / Artemis · GitLab](https://git.exeter.ac.uk/hepplestone/artemis)

- 在 latgen、VASPKIT 和 MS 中，称为 build layer

- VASPKIT 804 选项，会根据用户输入的错配度要求生成满足条件的系列界面构型 POSCAR 文件，并输出 log 信息


---

### 非晶

- [非晶合金建模系列(1):“熔化-淬火”的初始模型构建](https://mp.weixin.qq.com/s/qgmuUjBtUpRMfHwgnnWY7w)

- [非晶合金建模系列(3)-“熔化-淬火”法实现非晶结构](https://mp.weixin.qq.com/s/gKJnYrRH_zz2RP7ilMjG-g)

- 非晶相关结构分析：
    - [结构分析方法(2)-五次对称性(Local five-fold symmetry)](https://mp.weixin.qq.com/s/DUmwlSsVHw6cZ2A7JBDBdQ)
    - [结构分析方法(3)-梯度原子结构(Gradient atomic packing structure）](https://mp.weixin.qq.com/s/HkaZcbVYe80u8RhW3UOL2A)


---

### 晶界

- [任意CSL值晶界建模(一)](https://mp.weixin.qq.com/s/u6qvvsnszPU6pr8u4O0Tgw)、[任意CSL值晶界建模(二)](https://mp.weixin.qq.com/s/ZXrnbjKbsKerm_ZVDSoDFQ)

- aimsgb 程序：[aimsgb documentation](https://aimsgb-docs.readthedocs.io/)、[aimsgb - GitHub](https://github.com/ksyang2013/aimsgb)

- [GitHub - nmdl-mizo/interface\_master: A python package building CSL or approximate CSL interfaces of any two lattices and computing cell of non-identical displacement (CNID).](https://github.com/nmdl-mizo/interface_master)

- [GitHub - ab5424/agility: Repository for the Atomistic Grain Boundary and Interface Utility.](https://github.com/ab5424/agility)

- [GitHub - oekosheri/GB\_code: A grain boundary generation code](https://github.com/oekosheri/GB_code)

- LAMMPS 晶界构建：[Grain-Boundary-Energies-LAMMPS/Code and Scripts/Python and Lammps/FullStackAll/FullStack555/Experiments/Cu/0 at master · vishalsubbiah/Grain-Boundary-Energies-LAMMPS · GitHub](https://github.com/vishalsubbiah/Grain-Boundary-Energies-LAMMPS/tree/master/Code%20and%20Scripts/Python%20and%20Lammps/FullStackAll/FullStack555/Experiments/Cu/0)

- 含晶界构建
    - 旧：[GitHub - wojdyr/gosam: generator of simple atomistic models](https://github.com/wojdyr/gosam)
    - 复刻上述仓库（代码有更新）：[GitHub - akakcolin/gosam: generator of simple atomistic models](https://github.com/akakcolin/gosam)

- aimsgb 程序使用

```python
# 指定旋转轴、sigma、晶面 生成晶界
from aimsgb import Grain, GrainBoundary

initial_structure = Grain.from_file("POSCAR_Fe")
gb = GrainBoundary(
    axis=[0, 0, 1],
    sigma=5,
    plane=[1, 2, 0],
    initial_struct=initial_structure,
)

structure = Grain.stack_grains(
    grain_a=gb.grain_a,
    grain_b=gb.grain_b,
    direction=gb.direction,
)


# 寻找所有可用的晶界信息
from aimsgb import GBInformation

# 参数: 旋转轴和最大 sigma 值
# 返回值: 所有可能的 sigma 及对应的旋转角、晶面和 CSL 矩阵

gb_dict = GBInformation(axis=[1, 1, 0], max_sigma=10)

print(gb_dict)

print(gb_dict.get_gb_info()[3])

# output
"""
Grain boundary information for rotation axis: 110
Show the sigma values up to 10 (Note: * means twist GB, Theta is the rotation angle)
|  Sigma  |  Theta  | GB plane   | CSL matrix   |
|---------+---------+------------+--------------|
|    3    |  70.53  | (-1 1 1)   | -1  1  1     |
|         |         | (1 -1 2)   | 1 -1  1      |
|         |         | (1 1 0)*   | 1  2  0      |
|    9    |  38.94  | (-1 1 -4)  | -1 -2  1     |
|         |         | (-2 2 1)   | 1  2  1      |
|         |         | (1 1 0)*   | -4  1  0     |
"""
```


---


 (Coincidence Site Lattice, CSL) 重合位置点阵理论

对称倾侧（斜）晶界 (Symmetrical Tilting Grain Boundaries, STGB)

tilted grain boundaries 晶界面平行于旋转轴

twisted grain boundary 晶界面垂直于旋转轴

```bash
m, n          # 整数
[u v w]       # 晶粒旋转轴对应的晶向指数
∑             # CSL 值
α             # 奇数
```


根据特定晶界构建

寻找晶界


---

### 位错

- 各向同性下的位错构建
    - [金属建模 - 在各向同性材料中引入位错](https://mp.weixin.qq.com/s/g1LipqYCTSAoAh-BsXw-zQ)
    - 刃位错：[Atomsk - Tutorial - Edge dislocation in Al](https://atomsk.univ-lille.fr/tutorial_Al_edge.php)
    - 螺位错：[Atomsk - Tutorial - Screw dislocation in Al](https://atomsk.univ-lille.fr/tutorial_Al_screw.php)

- 各向异性下的位错构建：[Atomsk - Tutorial - Dislocations in Anisotropic Medium](https://atomsk.univ-lille.fr/tutorial_Fe_disloc.php)


---

## 其他

Ti2AlNb O 相：三元有序 orthorhombic；空间群：Cmcm, oC16

BCC 的第 N 近邻距离：[solid state chemistry - Calculate the third and fourth nearest neighbours in bcc - Chemistry Stack Exchange](https://chemistry.stackexchange.com/questions/99033/calculate-the-third-and-fourth-nearest-neighbours-in-bcc)

[BCC金属中的间隙原子及建模](https://mp.weixin.qq.com/s/49yQ1ncwI5TzFdc5jmGFfw)


- [ ] 原子半径没有统一值？

晶胞正交化、等长化：[晶胞正方化 - Jerkwin](https://jerkwin.github.io/2024/05/14/%E6%99%B6%E8%83%9E%E6%AD%A3%E6%96%B9%E5%8C%96/)

钙钛矿、半导体、绝缘体的点缺陷比金属或金属间化合物的点缺陷要复杂很多

C60 POSCAR 文件：[C60.POSCAR.vasp](https://github.com/Shuyangzero/Ogre/blob/master/structures/C60.POSCAR.vasp)

HCP 结构位错类型：a 型、a+c 型

钙钛矿晶体结构：八面体扭转理论

```text
A Handbook of Lattice Spacings and Structures of Metals and Alloys Volume 4 in International Series of Monographs on Metal Physics and Physical Metallurgy Book • 1958

https://doi.org/10.1016/C2013-0-08243-6

CHAPTER VI
CRYSTALLOGRAPHIC DATA ON "STRUKTURBERICHT" TYPES

CHAPTER VII
TABULATED LATTICE SPACINGS AND DATA OF THE ELEMENTS

CHAPTER VIII
TABULATED LATTICE SPACINGS AND DATA OF INTERMEDIATE PHASES IN ALLOY SYSTEMS

CHAPTER IX
ALPHABETICAL INDEX OF WORK ON BORIDES, CARBIDES, HYDRIDES, NITRIDES, AND
BINARY OXIDES
```

晶胞转换（介绍了几种工具；内容一般）：[晶胞之间相互转换 - ZSaying](https://mixzeng.github.io/2020/12/27/crystal-cell-convert/)
