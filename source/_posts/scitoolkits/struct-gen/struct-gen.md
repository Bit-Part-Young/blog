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

## 介绍

### 结构建模常用工具

- [pymatgen](https://pymatgen.org/)
- [ASE](https://wiki.fysik.dtu.dk/ase/)
- atomsk：[Atomsk - GitHub](https://github.com/pierrehirel/atomsk)、[Atomsk 官网](https://atomsk.univ-lille.fr/)
- [latgen](https://github.com/lingtikong/latgen)
- [PyXtal](https://pyxtal.readthedocs.io/)
- Material Studio（Win + Linux）

其他：

- [GitHub - orex/supercell: The program allows you to create regular structure supercell from cif file with partial occupancy and/or substitutions.](https://github.com/orex/supercell)

- [GitHub - dkratzert/StructureFinder: A crystal structure finder written in PyQt5 and Python3](https://github.com/dkratzert/StructureFinder)

- [CrystalMaker Software: Crystal & Molecular Structures Modelling and Diffraction](https://crystalmaker.com/)


---

### 构型可视化工具

- [OVITO](https://www.ovito.org/)
- [VESTA](https://jp-minerals.org/vesta/en/download.html)
- [VMD](https://www.ks.uiuc.edu/Research/vmd/)

[如何实现结构原子可视化？](https://mp.weixin.qq.com/s/zfzZ7kRXsXKe9yhyLcPuYQ)

用于晶体、分子结构可视化的 Jupyter 组件：[GitHub - nglviewer/nglview: Jupyter widget to interactively view molecular structures and trajectories](https://github.com/nglviewer/nglview)

[OpenMX Viewer](https://www.openmx-square.org/viewer/index.html)

---


将晶体对称性降低至 P1，目的是方便对晶体结构进行修改（VESTA 和 Material Studio）



---

### 分析工具

- crysinfo 程序（孔老师）：6a 选项查看 Assign Wyckoff letter（等同位点）
- 结构原型分析：[GitHub - chuanxun/StructurePrototypeAnalysisPackage: Structure Prototype Analysis Package can analyze symmetry and compare similarity of a large number of atomic structures.](https://github.com/chuanxun/StructurePrototypeAnalysisPackage)



---

## 构型文件格式

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

- 注意事项：
    - xyz 格式构型文件通过 ase 读取，其 pbc 为 False（extxyz 格式的 pbc 为 True），保存成 xyz 格式时无晶格参数信息；posconv 转换成 xyz 文件格式会在每行的原子位置后面附加晶格参数信息
    - vaspkit 可以将 xsd 文件转换成 POSCAR
    - [ ] posconv 添加 xsd 转换成其他格式的代码（Fortran）


---

## 结构建模

- 元素周期表里元素的晶体结构：[Periodic table (crystal structure) - Wikipedia](https://en.m.wikipedia.org/wiki/Periodic_table_(crystal_structure))
- Springer Materials：[https://materials.springer.com/](https://materials.springer.com/)
- MP 等数据库中的结构文件有时对称性不一定正确，最好进行静态计算检验一下


---

### 复杂结构

- 方法 1：在文献中查找该结构的晶体学信息，若提到 protype structure（原型结构），可在数据库（ICSD、MP、Aflow、Springer Materials 等）中找到对应原型结构的 cif 文件（需留意 Wyckoff position 是否一致或接近），再将晶格常数和原子种类进行替换，替换为要构建结构的信息

- 方法 2: 手动构建，需以下晶体学信息：晶体结构（crystal structure）、点阵参数（lattice parameter）、空间群（space group number）、原子位置（Wyckoff letter & Wyckoff position）；使用 Pyxtal 或 Material Studio 构建


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


```text
graphene orthogonal
1.0
   4.2747013930799902    0.0000000000000000    0.0000000000000000
   0.0000000000000000    2.4680000000000000    0.0000000000000000
   0.0000000000000000    0.0000000000000000   15.0000000000000000
C
4
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 C
   0.3333333333333333    0.0000000000000000    0.0000000000000000 C
   0.5000000000000000    0.5000000000000000    0.0000000000000000 C
   0.8333333333333333    0.5000000000000000    0.0000000000000000 C

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

空间群、磁性空间群
[GitHub - DanPorter/spacegroups: Load spacegroup and magnetic spacegroup information](https://github.com/DanPorter/spacegroups)

空间群：[Space Group Diagrams and Tables](http://img.chem.ucl.ac.uk/sgp/large/sgp.htm)

晶体学课程内容
>[GitHub - aronwalsh/Crystallography: Online resource for introduction to crystallography at Imperial College London (MATE40004)](https://github.com/aronwalsh/Crystallography)

[晶体化学](https://www.hxzxs.cn/shuju/newpage/jthx.htm)

晶体结构标注：空间群符号、Pearson 符号、典型晶体结构类型（Strukturbericht designation 或 Strukturbericht type）

[典型晶体结构类型 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/wiki/%E5%85%B8%E5%9E%8B%E6%99%B6%E4%BD%93%E7%BB%93%E6%9E%84%E9%A1%9E%E5%9E%8B)

[七大晶系的XRD图谱（部分空间群）](https://mp.weixin.qq.com/s/fMCCPNzhQ0Fr2UNzSZPimg)

二维晶体：10 种点群，17 种空间群（墙纸群 (wallpaper group)）


- [ ] 了解 aflow prototype 中的 primitive vectors 的公式及其含义，及如何实现 unit 与 primitive 互相转变的


- [ ] D019 结构（Ti3Al）原子位点，mp 与 latgen 两者有区别（和 hcp 类似的问题）

---

α2 相晶体学信息：晶体结构：D019；空间群：P63/mmc
有序 B2/β 相晶体学信息：空间群：Pm-3m(3 的上面有横线) CsCl 原型结构
O 相晶体学信息：晶体结构：三元有序 orthorhombic；空间群：Cmcm, oC16

---

- 结构原型百科全书：[aflow.org/prototype-encyclopedia/](http://aflow.org/prototype-encyclopedia/)


- 常见结构的空间群符号：

|    结构    | 空间群符号 | 空间群 number |
|:----------:|:----------:|:------------:|
|   金刚石   |       Fd-3m     |      227        |
|    FCC     |       Fm-3m     |     225          |
|    BCC     |      Im-3m      |       229       |
|    HCP     |      P6_3/mmc      |      194        |
|    岩盐 (rocksalt NaCl)    |        Fm-3m    |              |
| 立方钙钛矿 (perovskite CaTiO3) |      Pm-3m      |              |
| CsCl           |      Pm-3m      |              |

- 一些结构的 prototype

| Prototype | Strukturbericht designation | Pearson symbol | Space group number | Space group symbol |
|:-------: |:-------------------------: |:------------: |:----------------: |:----------------: |
|     W     |             A2              |      cI2       |        229         |       Im-3m        |

BCC：[AFLOW Prototype: A\_cI2\_229\_a](https://www.aflowlib.org/prototype-encyclopedia/A_cI2_229_a.html)

FCC：[AFLOW Prototype: A\_cF4\_225\_a](https://www.aflowlib.org/prototype-encyclopedia/A_cF4_225_a.html)

HCP：[AFLOW Prototype: A\_hP2\_194\_c](https://www.aflowlib.org/prototype-encyclopedia/A_hP2_194_c.html)

$\beta$ -Sn：[AFLOW Prototype: A\_tI4\_141\_a](https://www.aflowlib.org/prototype-encyclopedia/A_tI4_141_a.html)

Cr5B3：[AFLOW Prototype: A3B5\_tI32\_140\_ah\_cl](https://www.aflowlib.org/prototype-encyclopedia/A3B5_tI32_140_ah_cl.html)

Mn5Si3：[AFLOW Prototype: A5B3\_hP16\_193\_dg\_g](https://www.aflowlib.org/prototype-encyclopedia/A5B3_hP16_193_dg_g.html)



BCC

$$
\begin{align}
\mathbf{a_1}& = -\frac{1}{2}\mathbf{x} + \frac{1}{2}\mathbf{y} + \frac{1}{2}\mathbf{z}\\

\mathbf{a_2}& = \frac{1}{2}a\mathbf{x} - \frac{1}{2}a\mathbf{y} + \frac{1}{2}a\mathbf{z}\\

\mathbf{a_3}& = \frac{1}{2}a\mathbf{x} + \frac{1}{2}a\mathbf{y} - \frac{1}{2}a\mathbf{z}

\end{align}
$$

FCC

$$
\begin{align}
\mathbf{a_1}& = \frac{1}{2}a\mathbf{y} + \frac{1}{2}a\mathbf{z} \\

\mathbf{a_2}& = \frac{1}{2}a\mathbf{x} + \frac{1}{2}a\mathbf{z} \\

\mathbf{a_3}& = \frac{1}{2}a\mathbf{x} + \frac{1}{2}a\mathbf{y} \\
\end{align}

$$

HCP

$$
\begin{align}
\mathbf{a_1}& = \frac{1}{2}a\mathbf{y} - \frac{\sqrt{3}}{2}a\mathbf{z}\\

\mathbf{a_2}& = \frac{1}{2}a\mathbf{y} + \frac{\sqrt{3}}{2}a\mathbf{z}\\

\mathbf{a_3}& = c\mathbf{z}\\
\end{align}
$$

---

结构可视化

- MoS2：[Molybdenum Disulfide - MoS2](https://www.chemtube3d.com/ss-mos2/)
- 金刚石、石墨、C60、碳纳米管：[Introductory Structures Allotropes of Carbon (Diamond and Graphite) and Pentacene](https://www.chemtube3d.com/claydencarbonallotropes/)
- hcp：[Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/)
- perovskite：[CaTiO3 - Perovskite: Interactive 3D Structure](https://www.chemtube3d.com/_perovskitefinal/)


hcp 结构原胞原子坐标有两种形式：

- 一个原子在原点，另一个在胞内：latgen 和 ase，(0.0 0.0 0.0) (2/3 1/3 0.5)
- 两个原子均在胞内：pymatgen 和 pyxtal，(1/3 2/3 1/4) (2/3 1/3 3/4)
- 两种形式无本质区别，两者可通过过周期性平移进行互相转化
- [Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/) 有这两种形式的可视化


---

## 其他

BCC 的第 N 近邻距离：[solid state chemistry - Calculate the third and fourth nearest neighbours in bcc - Chemistry Stack Exchange](https://chemistry.stackexchange.com/questions/99033/calculate-the-third-and-fourth-nearest-neighbours-in-bcc)

[BCC金属中的间隙原子及建模](https://mp.weixin.qq.com/s/49yQ1ncwI5TzFdc5jmGFfw)

```text
金刚石结构原胞原子位点位置
0.8750000000000000 0.8750000000000000 0.8750000000000000
0.1250000000000000 0.1250000000000000 0.1250000000000000

还是
0.0 0.0 0.0
0.25 0.25 0.25
```

- [ ] 原子半径没有统一值？

晶胞正交化、等长化：[晶胞正方化 - Jerkwin](https://jerkwin.github.io/2024/05/14/%E6%99%B6%E8%83%9E%E6%AD%A3%E6%96%B9%E5%8C%96/)

钙钛矿、半导体、绝缘体的点缺陷比金属或金属间化合物的点缺陷要复杂很多

C60 POSCAR 文件：[C60.POSCAR.vasp](https://github.com/Shuyangzero/Ogre/blob/master/structures/C60.POSCAR.vasp)

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

pymatgen 中的 BCC 形成的 (111) 表面结构是菱形晶系，latgen 形成的晶系是六方晶系
latgen 中表面的真空层距离数值设置
latgen 可以生成界面（multi-layer）

- [ ] 当 POSCAR 文件中的原子位点出现负值或大于 1 时（分数坐标），可以通过 VESTA 软件进行转换；如何通过 pymatgen 解决上述问题？

---

借鉴该文献中的结构晶体学信息表格写法
![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202406141558921.png)

---

点缺陷

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052005978.png)

>[8.2: Close-packing and Interstitial Sites - Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Book%3A_Introduction_to_Inorganic_Chemistry_(Wikibook)/08%3A_Ionic_and_Covalent_Solids_-_Structures/8.02%3A_Close-packing_and_Interstitial_Sites)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014348.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014588.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014611.png)



[Interstitial Sites: Size, Types, Applications, And Calculations – Materials Science & Engineering](https://msestudent.com/interstitial-sites-size-types-applications-and-calculations/)

[Interstitial Sites (FCC & BCC)](https://lamma.engineering.unt.edu/sites/default/files/class8_handout_mtse_5010_2018.pdf)
