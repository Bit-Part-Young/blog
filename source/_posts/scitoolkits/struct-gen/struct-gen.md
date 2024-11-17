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
- atomsk：[Atomsk - GitHub](https://github.com/pierrehirel/atomsk)、[Atomsk 官网](https://atomsk.univ-lille.fr/)
- [latgen](https://github.com/lingtikong/latgen)
- [PyXtal](https://pyxtal.readthedocs.io/)
- Material Studio（Win + Linux）

- 其他：
    - [GitHub - orex/supercell: The program allows you to create regular structure supercell from cif file with partial occupancy and/or substitutions.](https://github.com/orex/supercell)

    - [GitHub - dkratzert/StructureFinder: A crystal structure finder written in PyQt5 and Python3](https://github.com/dkratzert/StructureFinder)

    - [CrystalMaker Software: Crystal & Molecular Structures Modelling and Diffraction](https://crystalmaker.com/)



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

- HCP 结构单胞原子位置有两种形式：
    - 一个原子在原点，另一个在胞内：latgen 和 ase，(0.0 0.0 0.0)、(2/3 1/3 0.5)
    - 两个原子均在胞内：pymatgen 和 PyXtal，(1/3 2/3 1/4)、(2/3 1/3 3/4)
    - 两种形式无本质区别，两者可通过过周期性平移进行互相转化
    - [Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/) 有这两种形式的可视化



---

## 分析工具

- crysinfo 程序（孔老师）：6a 选项查看 Assign Wyckoff letter（等同位点）

- 结构原型分析：[GitHub - chuanxun/StructurePrototypeAnalysisPackage: Structure Prototype Analysis Package can analyze symmetry and compare similarity of a large number of atomic structures.](https://github.com/chuanxun/StructurePrototypeAnalysisPackage)

 - CIF 格式文件分析：[GitHub - bobleesj/cifkit: High-throughput .cif analysis made easy. Visit: https://bobleesj.github.io/cifkit/](https://github.com/bobleesj/cifkit)

含缺陷超胞生成、前/后处理和分析：[Doped code 介绍](https://mp.weixin.qq.com/s/r3ZabHXYAn2HJgyFxFmA-w)



---

## 构型文件格式

- 注意事项：
    - CIF 格式有含对称性、不含对称性两种格式，大部分程序将构型格式转换成 CIF 都是不含对称性的（空间群为 P1，写入所有原子）
    - xyz 格式构型文件通过 ase 读取，其 pbc 为 False（extxyz 格式的 pbc 为 True），保存成 xyz 格式时无晶格参数信息；posconv 转换成 xyz 文件格式会在每行的原子位置后面附加晶格参数信息
    - vaspkit 可将 xsd 文件转换成 POSCAR
    - [ ] posconv 添加 xsd 转换成其他格式的代码（Fortran）

```bash
.pdb           # Protein Data Bank，可以用 VMD 软件（跨平台）打开
.xsd           # Material Studio 构型文件格式
.cell          # CASTEP 的输入构型文件格式
.cif           # 部分该格式文件晶体学信息很全
.xsf           # XCrySDen


# xyz 格式内容示例
2

Nb      0.000000000000000      0.000000000000000      0.000000000000000
Nb      1.660000000000000      1.660000000000000      1.660000000000000


# posconv xyz 格式内容示例
2
# BCC(001) cell with dimension 1 x 1 x 1 and a = 3.32
Nb    0.000000000000000    0.000000000000000    0.000000000000000 crystal_vector  1    3.320000000000000    0.000000000000000    0.000000000000000
Nb    1.660000000000000    1.660000000000000    1.660000000000000 crystal_vector  2    0.000000000000000    3.320000000000000    0.000000000000000
```


---

## 结构建模

- 元素周期表里元素的晶体结构：[Periodic table (crystal structure) - Wikipedia](https://en.m.wikipedia.org/wiki/Periodic_table_(crystal_structure))

- Springer Materials：[https://materials.springer.com/](https://materials.springer.com/)

- MP 等材料数据库中的结构文件有时对称性不一定正确，查看该数据库中已计算的性质是否与文献中的接近，以及最好进行静态计算检验一下


---

### 复杂结构

- 方法 1：在文献中查找该结构的晶体学信息，若提到 prototype structure（原型结构），可在数据库（ICSD、MP、Aflow、Springer Materials 等）中找到对应原型结构的 cif 文件（**需留意 Wyckoff position 是否一致或接近**），再将晶格常数和原子种类进行替换，替换为要构建结构的信息

- 方法 2: 手动构建，需以下晶体学信息：晶体结构（crystal structure）、点阵参数（lattice parameter）、空间群（space group number）、原子位置（Wyckoff letter & Wyckoff position）；使用 Pyxtal 或 Material Studio 构建


---

### 表面

pymatgen 中的 BCC 形成的 (111) 表面结构是菱形晶系，latgen 形成的晶系是六方晶系

latgen 中表面的真空层距离数值设置

latgen 可以生成界面（multi-layer）

- 添加真空层：
    - vaspkit 添加真空层，先加数值，再将原子层移至 z 方向居中
    - ase 中的 `center()` 函数添加真空层是分别往两边加
    - atomsk 添加真空层是在 top 上加


---

### 界面/异质结

- [Materials Studio 入门到精通【16】简单界面模型的建立 - 知乎](https://zhuanlan.zhihu.com/p/346859236)

- [如何采用Materials Studio切晶面和建立界面模型\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Av411H7PS)

- [[建模与可视化] 求助Si和α-Al2O3材料界面计算的界面搭建问题 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-47013-1-1.html)

- [GitHub - aguang5241/Interface-Maker: A python3 code to create slabs and interfaces for first-principles calculations.](https://github.com/aguang5241/Interface-Maker)

- [GitHub - rzk1/heterojunction: Create surfaces and heterojunctions from two crystal structures](https://github.com/rzk1/heterojunction)

- 在 latgen、VASPKIT 和 MS 中，称为 build layer

- VASPKIT 804 选项，会根据用户输入的错配度要求生成满足条件的系列界面构型 POSCAR 文件，并输出 log 信息


---

### 晶界

- [任意CSL值晶界建模(一)](https://mp.weixin.qq.com/s/u6qvvsnszPU6pr8u4O0Tgw)、[任意CSL值晶界建模(二)](https://mp.weixin.qq.com/s/ZXrnbjKbsKerm_ZVDSoDFQ)

- aimsgb 程序：[aimsgb documentation](https://aimsgb-docs.readthedocs.io/)、[aimsgb - GitHub](https://github.com/ksyang2013/aimsgb)

- [GitHub - ab5424/agility: Repository for the Atomistic Grain Boundary and Interface Utility.](https://github.com/ab5424/agility)

- [GitHub - oekosheri/GB\_code: A grain boundary generation code](https://github.com/oekosheri/GB_code)

LAMMPS 晶界构建：[Grain-Boundary-Energies-LAMMPS/Code and Scripts/Python and Lammps/FullStackAll/FullStack555/Experiments/Cu/0 at master · vishalsubbiah/Grain-Boundary-Energies-LAMMPS · GitHub](https://github.com/vishalsubbiah/Grain-Boundary-Energies-LAMMPS/tree/master/Code%20and%20Scripts/Python%20and%20Lammps/FullStackAll/FullStack555/Experiments/Cu/0)

- 含晶界构建
    - 旧：[GitHub - wojdyr/gosam: generator of simple atomistic models](https://github.com/wojdyr/gosam)
    - 复刻上述仓库（代码有更新）：[GitHub - akakcolin/gosam: generator of simple atomistic models](https://github.com/akakcolin/gosam)


---


CSL 重合位置点阵理论


tilted grain boundaries 晶界面平行于旋转轴

twisted grain boundary 晶界面垂直于旋转轴


根据特定晶界构建

寻找晶界


---

### 碳纳米管

- [Atomsk - Tutorial - Graphene and Nanotubes](https://atomsk.univ-lille.fr/tutorial_nanotubes.php)
- [VASP视频教程-搭建模型-用vnl或ms搭建模型卷曲纳米碳管\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV14M4ye8EVX)


---

### 石墨烯

- [Atomsk - Tutorial - Graphene and Nanotubes](https://atomsk.univ-lille.fr/tutorial_nanotubes.php)

- 二维；六方结构；最近邻原子间距约为 1.42 埃

注：
- 对于六方结构，其中的原子位置坐标随基矢的选择会有些许不同，但本质一样都是一样的；
- 基矢以逆时针为正方向；
- C 的 ENMAX 为 400（所有元素中最大，所以 pymatgen 中 ENCUT 的默认设置为 520）。




![graphene-structure.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307151658266.png)


>CASTRO NETO A H, GUINEA F, PERES N M R, 等, 2009. The electronic properties of graphene\[J/OL\]. Reviews of Modern Physics, 81(1): 109-162. DOI:10.1103/RevModPhys.81.109.


石墨烯 POSCAR 文件
```text
graphene hexagonal
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

### 石墨

- 六方结构；z 轴方向长度约为 6.7 埃


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152230723.png)

>https://doi.org/10.1016/B978-0-12-385469-8.00002-2.


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152232968.png)

>[10.1073/pnas.2134173100](https://doi.org/10.1073/pnas.2134173100).


石墨 POSCAR 文件
```text
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


---

## 晶体学相关

- [ ] 了解 aflow prototype 中的 primitive vectors 的公式及其含义，及如何实现 unit 与 primitive 互相转变的


- [ ] D019 结构（Ti3Al）原子位点，mp 与 latgen 两者有区别（和 hcp 类似的问题）

D019 Ti3Al 结构：[https://next-gen.materialsproject.org/materials/mp-1823?chemsys=Ti-Al&crystal_system=Hexagonal](https://next-gen.materialsproject.org/materials/mp-1823?chemsys=Ti-Al&crystal_system=Hexagonal)

---

α2 相晶体学信息：晶体结构：D019；空间群：P63/mmc
有序 B2/β 相晶体学信息：空间群：Pm-3m(3 的上面有横线) CsCl 原型结构
O 相晶体学信息：晶体结构：三元有序 orthorhombic；空间群：Cmcm, oC16


---

## 其他

BCC 的第 N 近邻距离：[solid state chemistry - Calculate the third and fourth nearest neighbours in bcc - Chemistry Stack Exchange](https://chemistry.stackexchange.com/questions/99033/calculate-the-third-and-fourth-nearest-neighbours-in-bcc)

[BCC金属中的间隙原子及建模](https://mp.weixin.qq.com/s/49yQ1ncwI5TzFdc5jmGFfw)

金刚石结构原胞原子位点位置：(0.0 0.0 0.0)、(0.25 0.25 0.25)

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

---

A15 A3B 型

B1 NaCl 型

D019 hcp 结构
D022 正交结构

Pearson 符号
3 个符号表示
晶系 +（P I R F SABC I）+ 数字（原子数）

225 FCC 结构

原型结构（最早发现的晶体）

---
