---
title: latgen 安装与使用
top: false
cover:
toc: true
mathjax: true
summary: latgen 安装与使用
description: latgen 安装与使用
tags:
  - 结构建模
  - latgen
categories:
  - 科研工具
date: 2023-07-19 15:56:30
abbrlink: 36493
password:
---

# latgen 安装与使用

## 介绍

构型生成程序，包括 BCC、FCC、HCP、Diamond、含点缺陷、置换固溶体、表面、多晶等构型。



---

## 安装

见 HPC Tutorial。



---

## 使用

- 整体所有选项

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404291006009.png)

---

- multi-layer 选项

---

- A3B 选项

```text
Please select the composition of your lattice:
   1. A3B;
   2. AB3;
Your choice [1]: 1
Your selection : 1
Please select the type of your lattice:
   1. A15;         5. D09;
   2. D019;        6. L12;
   3. D022;        7. L60;
   4. D03;
```

---

- A2B 选项

```text
Please select the composition of your lattice:
   1. AB2;          2. A2B;
Your choice [1]:
Your selection : 1
Please select the type of your lattice:
   1. C1 (Fluorite);
   2. C15 (Cu2Mg);
   3. C32 (AlB2);
```

---

- AB & ABXn 选项

```text
Please select the type of your lattice:
   1. B1 (NaCl);        4. L10 (CuAu);
   2. B2 (CsCl);        5. B81 (a-NiAs);
   3. B3 (Zincblende);  6. B4 (Wurtzite);
----------------------------------------------------------------------
   7. Perovskite;
----------------------------------------------------------------------
```


- 多晶选项

```text
The necessary info for polycrystal info can be provided either by stdin, or
read from a file. In the previous case, the position and the orientation of
each grain are assigned randomly. While in the latter case, such information
can be defined explicitly. If this is preferred, input the file name now:

The necessary information will be read from stdin.
Please input the lower and upper bound of your box along X: 0.0 5.66
Please input the lower and upper bound of your box along Y: 0.0 5.66
Please input the lower and upper bound of your box along Z: 0.0 5.66
Please indicate where you want pbc in x, y, and z (0/1)[1 1 1]: 1 1 1
Please input the desired number of grains in your box: 5
Would you like to assign different atomic types for different grains? (y/n)[n]: n

Your box is bounded by        : [0 5.66], [0 5.66], [0 5.66]
Periodicity in each direction : 1 1 1
Number of grains in the box   : 5
The crystalline grain info will be written to grain_part_info and
grain_cell_info, respectively.

Now to generate the polycrystal ... Done! Total # of atoms: 14
WARNING: there might be overlaped atoms, check by yourself!!!

>>>>>>============= End of Polycrystal generation ==============<<<<<<

```

---

- User defined 选项

```text
Input the file name if you want to read the unit cell information from
a POSCAR file, or simply ENTER to read from stdin:

Please input the lattice constant of the USER lattice [1]: 5.5
Please input the lattice vector A1: 1 0 0
Please input the lattice vector A2: 0 1 0
Please input the lattice vector A3: 0 0 1
Please input the number of atoms per unit cell [1]: 2
Please input the number of atom  types in cell [1]: 1
Please input [type xs ys zs] for atom 1: 1 0 0 0
Please input [type xs ys zs] for atom 2: 1 0.5 0.5 0.5
```

---

latgen 生成结构中的 map.in 文件的含义（FFT map 信息文件）

```text
The atomic configuration will be written to: atomcfg.xyz and POSCAR 
The FFT map information will be written to file: map.in
```

---

latgen 生成 HCP 结构的选项含义，**个人一般使用选项 3**。

1. 四指数坐标 U 沿 x 轴方向，逆时针旋转 60° 为 y 轴方向，并沿 x 轴方向分解；
2. 四指数坐标 V 沿 y 轴方向，顺时针旋转 60° 为 x 轴方向，并沿 y 轴方向分解；
3. 3、4 同理。其中 1、2 之间，3、4 之间的原子位置相同，x、y 方向的基矢稍微有些区别。

```text
   1. U along x,  60 degree;
   2. V along y,  60 degree;
   3. U along x, 120 degree;
   4. V along y, 120 degree;
```

---

选项 1 生成的 hcp Zr POSCAR 文件

```text
hcp Zr
1.0
   3.2340000000000000    0.0000000000000000    0.0000000000000000
   1.6170000000000000    2.8007261558388699    0.0000000000000000
   0.0000000000000000    0.0000000000000000    5.1680000000000001
Zr
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Zr
   0.3333333333333339    0.3333333333333322    0.5000000000000000 Zr
```

---

选项 2 生成的 hcp Zr POSCAR 文件

```text
hcp Zr
1.0
   2.8007261558388699    1.6170000000000000    0.0000000000000000
   0.0000000000000000    3.2340000000000000    0.0000000000000000
   0.0000000000000000    0.0000000000000000    5.1680000000000001
Zr
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Zr
   0.3333333333333322    0.3333333333333339    0.5000000000000000 Zr
```

---

选项 3 生成的 hcp Zr POSCAR 文件

```text
hcp Zr
1.0
   3.2340000000000000    0.0000000000000000    0.0000000000000000
  -1.6170000000000000    2.8007261558388792    0.0000000000000000
   0.0000000000000000    0.0000000000000000    5.1680000000000152
Zr
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Zr
   0.6666666666666700    0.3333333333333300    0.5000000000000000 Zr
```

---

选项 4 生成的 hcp Zr POSCAR 文件

```text
hcp Zr
1.0
   2.8007261558388699   -1.6170000000000000    0.0000000000000000
   0.0000000000000000    3.2340000000000000    0.0000000000000000
   0.0000000000000000    0.0000000000000000    5.1680000000000001
Zr
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Zr
   0.6666666666666680    0.3333333333333340    0.5000000000000000 Zr
```
