---
title: 晶体学相关
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 晶体学相关
description: 晶体学相关
tags:
  - 晶体学
categories:
  - 结构建模
date: 2024-11-09 15:00:56
abbrlink: 560015
password:
---

# 晶体学相关

## 介绍

- 晶体学课程内容：[GitHub - aronwalsh/Crystallography: Online resource for introduction to crystallography at Imperial College London (MATE40004)](https://github.com/aronwalsh/Crystallography)

- [晶体化学](https://www.hxzxs.cn/shuju/newpage/jthx.htm)

- 单胞、原胞：[晶格常数是原胞（Primitive Cell）边长还是单胞（Convention Unit Cell）边长？](https://www.zhihu.com/question/20083907)

- 单胞：Convention Unit Cell；有时称为晶胞、惯用原胞（结晶学中惯用）；在能够保持晶格对称性的前提下，构成晶体的最小的周期性结构单元；单胞的边矢量称为单胞基矢，通常用 a 、b、c 表示

- 原胞：Primitive Cell；构成晶体的最小的周期性结构单元；不一定能反映晶格的对称性

- 晶格常数：单胞边长

- 晶体结构标注：空间群编号及符号、Pearson 符号、典型晶体结构类型（Strukturbericht Designation 或 Strukturbericht Type）


- 晶体学相关实用链接
    - 晶体学 prototype 百科全书：[Encyclopedia of Crystallographic Prototypes - AFLOW](http://aflow.org/prototype-encyclopedia/)
    - [Crystal Lattice Structures: Index by Prototype - Atomic Scale Physics](https://www.atomic-scale-physics.de/lattice/prototype.html)
    - 空间群：
        - [Space group - Wikipedia](https://en.wikipedia.org/wiki/Space_group)
        - [Space Group Classes - AFLOW](https://www.aflowlib.org/prototype-encyclopedia/space_groups.html)
        - [List of space groups - Wikipedia](https://en.wikipedia.org/wiki/List_of_space_groups)
        - [Space Group Diagrams and Tables](http://img.chem.ucl.ac.uk/sgp/large/sgp.htm)
        - 230 个空间群的晶体结构示例：[The space group list project](https://crystalsymmetry.wordpress.com/230-2/)
    - Pearson 符号：
        - [Pearson symbol - Wikipedia](https://en.wikipedia.org/wiki/Pearson_symbol)
        -  [Pearson Symbols - AFLOW](https://www.aflowlib.org/prototype-encyclopedia/pearson_symbols.html)
    - prototype：
        - prototype 索引：[Prototype Index - AFLOW](https://www.aflowlib.org/prototype-encyclopedia/prototype_index.html)
        - 根据晶体结构匹配 prototype：[AFLOW XtalFinder](http://aflowlib.org/p/xtal-finder.html)
    - Strukturbericht Designation：
        - [Strukturbericht Designations - AFLOW](https://www.aflowlib.org/prototype-encyclopedia/strukturberichts.html)
        - [典型晶体结构类型 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/wiki/%E5%85%B8%E5%9E%8B%E6%99%B6%E4%BD%93%E7%BB%93%E6%9E%84%E9%A1%9E%E5%9E%8B)
    - Prototype、Pearson Symbol、Strukturbericht Designation 和 Space Group 对应关系：[Crystal Lattice Structures: Index by Prototype](https://www.atomic-scale-physics.de/lattice/prototype.html)
    - [七大晶系的XRD图谱（部分空间群）](https://mp.weixin.qq.com/s/fMCCPNzhQ0Fr2UNzSZPimg)



---

## 晶系

- 七大晶系（Crystal System）对应的空间群所属范围

```bash
1-2               # 三斜；Triclinic
3-15              # 单斜；Monoclinic
16-74             # 正交；Orthorhombic
75-142            # 四方；Tetragonal
143-167           # 三方/菱方；Trigonal
168-194           # 六方；Hexagonal
195-230           # 立方；Cubic
```

- 7 种晶系及 14 种布拉维点阵示意图

![crystal-system.jpeg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307161137907.jpeg)


---

### 六方晶系

- Hexagonal Miller-Bravais Coordinate System：四轴坐标系

- 四轴坐标指数的优点：能更好地反映六方晶系的对称性；对于面指数 (hkil)，h、k、i 可以互换位置，反映了六方晶系六次对称轴的特点

- [How to Read Hexagonal Crystal Directions and Planes (Miller-Bravais Indices) – Materials Science & Engineering](https://msestudent.com/hexagonal-miller-bravais-indices/)

```bash
# 方向指数 三指数坐标 [uvw] 转 四指数坐标 [UVTW]
U = (2u-v)/3
V = (2v-u)/3
T = -(U+V)
W = w

# 方向指数 四指数坐标 [UVTW] 转 三指数坐标 [uvw]
u = U - T
v = V - T
w = W

# 面指数 三指数坐标 (hkl) 转 四指数坐标 (hkil)
h+k = -i

# 面指数 四指数坐标 (hkil) 转 三指数坐标 (hkl)
# 直接去掉 i 即可
```



---

## Pearson 符号

- Pearson Symbol：第一个小写英文字母表示晶系，第二个大写英文字母表示布拉维点阵，第三个数字表示单胞中的原子数

```bash
# Pearson Symbol    晶系/布拉维点阵
a                   # 三斜（Anorthic）
m                   # 单斜
o                   # 正交
t                   # 四方
h                   # 六方/正交
c                   # 立方
P                   # primitive
I                   # 体心
F                   # 面心
C                   # 底心（A、B 面的有心化用 C 代替）

```



---

## Strukturbericht Designation

- Strukturbericht Designation：结构符号，由大写英文字母 + 数字组成，字母表示结构的类型，数字表示顺序号

```bash
# SD           晶体结构类型
A              # 元素
B              # AB 型化合物
C              # AB2 型化合物
D              # AmBn 型化合物
E...K          # 更复杂的化合物
L              # 合金
O              # 有机化合物
S              # 硅酸盐
```



---

## 空间群、点群

- 空间群：晶格全部对称操作（平移和转动）的集合；分简单（点）空间群和复杂（非点）空间群；不同的空间群共 230 个（73 个是点空间群）

- 点群：由 10 种对称轴组成的对称操作群；有 32 种点群

- 空间群、磁性空间群：[GitHub - DanPorter/spacegroups: Load spacegroup and magnetic spacegroup information](https://github.com/DanPorter/spacegroups)

- 二维晶体：10 种点群，17 种空间群（墙纸群 (wallpaper group)）

- Hall number：通常指的是与晶体的空间群（space group）相关的一个标识符，用于区分不同的空间群。Hall 符号系统是一种用于描述晶体对称性的方法，由 A. Hall 于 1980 年提出。这个符号系统试图弥补传统的国际标准空间群符号（如 Hermann-Mauguin 符号）的一些局限性，尤其是在描述不同类型的晶体对称性时。Hall 符号系统特别适用于具有 **非传统对称性** 或者 **极高对称性的空间群**，并且广泛用于晶体学、物理学以及化学中的晶体结构分析。（ChatGPT4 生成）

```bash
# Space Group  Number  晶系   Strukturbericht Designation
C2/m       12       单斜   有 SD
C2/c       15       单斜
Pmma       51       正交   B19
Cmmm       65       正交
Fddd       70       正交
Immm       71       正交   无 SD
Imma       74       正交   无 SD
P4_2/n     86       四方   无 SD
I4/m       87       四方   D1_a
P4/mmm     123      四方   L1_0(FCC 结构的 tetragonal distortion)
I4/mmm     139      四方   有 SD
I4/mcm     140      四方   有 SD
I4_1/amd   141      四方
R3         146      三方
R-3        148      三方
P-3m1      164      三方   有 SD
R-3m       166      三方   L1_1、A10
P6/mmm     191      六方   C32(omega 相)、C_h
P6_3/mcm   193      立方   无 SD
P6_3/mmc   194      六方   D0_19
Pm-3m      221      立方   L1_2(原子位置同 FCC 点阵位点)、B2(CsCl)、D0_9(α-ReO3)
Pm-3n      223      立方   A15
Fm-3m      225      立方   A1(FCC)、B1(NaCl)、C1、D0_3、L2_1
Fd-3m      227      立方   C15、A4(Diamond)
Im-3m      229      立方   A2(BCC)


# Strukturbericht Designation  空间群  晶系
D0_19  194     六方
B19    51      正交
L1_0  123      四方 FCC 结构的 tetragonal distortion
L1_2  221      立方 FCC
D0_22  139     四方
A_h            简单立方
A1             FCC
A2             BCC
A3             HCP
A4             Diamond
A5             β-Sn
A6             In
A9             石墨

CaTiO3 立方钙钛矿     Pm-3m

# FCC 相关空间群
F23      196
Fm-3     202
Fd-3     203
F432     209
F4_132   210
F-43m    216
F4-3c    219
Fm-3m    225
Fm-3c    226
Fd-3m    227
Fd-3c    228


# BCC 相关空间群
I23      197
I2_13    199
Im-3     204
Ia-3     206
I432     211
I4_132   214
I-43m    217
I-43d    220
Im-3m    229
Ia-3d    230
```


借鉴该文献中的结构晶体学信息表格写法

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202406141558921.png)
