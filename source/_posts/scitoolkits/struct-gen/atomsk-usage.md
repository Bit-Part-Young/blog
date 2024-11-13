---
title: atomsk 使用
top: false
cover:
toc: true
mathjax: true
summary: atomsk 使用
description: atomsk 使用
tags:
  - atomsk
categories:
  - 科研工具
  - 结构建模
date: 2024-06-28 16:00:00
abbrlink: 162806
password:
---

# atomsk 使用

## 介绍

- 强大的建模工具

- atomsk 中的 cfg 格式文件用 OVITO 打开，VESTA 无法打开

- 暂时没有的功能：
    - 单胞转换成原胞
    - 无法直接构造八面体、四面体间隙的点缺陷
    - 可否建立 layer / 界面模型？


---

### 参考资料

- atomsk 官方教程：[Atomsk - Tutorials](https://atomsk.univ-lille.fr/tutorials.php)

- [Atomsk Cheat Sheet](https://atomsk.univ-lille.fr/data/Atomsk_Cheat-Sheet.pdf)

- 查看所有的 options 和 modes 及其用法：[Documentioin - Atomsk](https://atomsk.univ-lille.fr/doc/en/index.html)

- 层错构建：[Atomsk - Tutorial - Stacking fault](https://atomsk.univ-lille.fr/tutorial_stackingfault.php)

- VESTA 中如何变换点阵（六方转正交）：[crystallography - How to transform lattice in VESTA - Matter Modeling Stack Exchange](https://mattermodeling.stackexchange.com/questions/7263/how-to-transform-lattice-in-vesta)

- 六方胞的正交化（里面的示意图可供参考）：[Orthogonalization of a hexagonal unit cell of AlN](https://er-c.org/barthel/drprobe/example-orthcel-aln.html)

- 晶界构建（symmetric tilt、twist）：[Atomsk - Tutorial - Grain Boundaries](https://atomsk.univ-lille.fr/tutorial_grainboundaries.php)

- 位错构建（刃、螺位错）：
    - [Atomsk - Tutorial - Edge Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_edge.php)
    - [Atomsk - Tutorial - Screw Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_screw.php)



---

## 使用

- `options`：应用于体系的变换（transformations），用 `-` 区分

- `modes`：允许执行特定的操作，构造，分析或操纵多个数据文件（operations, constructions, analysis, manipulate），用 `--` 区分


---

### 常用命令实例

```bash
# 构建晶体结构
atomsk --create fcc 4.02 Al vasp
atomsk --create hcp 2.92 4.61 Ti vasp  # 矢量：H1=[2-1-10], H2=[-12-10], H3=[0001]

# 构建不同晶体取向的构型
# zsh [] 中括号需添加引号
atomsk --create fcc 3.53 Ni -orient [1-10] [11-2] [111] vasp

# 构建超胞
atomsk Ni.cfg -duplicate 1 1 4 vasp

# 添加原子
atomsk initial.xsf -add-atom Si at 0.25*box 0.33*box 0.5*box final.cfg

# 原子 Z 轴坐标低于一定值，其 Z 轴被固定
atomsk Ni.cfg -fix Z below 4.05 Z vasp

# 线性插值；用于 NEB
atomsk --interpolate initial.cfg final.cfg 7 cfg

# 将六方胞变成正交胞
atomsk POSCAR -orthogonal-cell -sort species pack vasp

# 笛卡尔、分数坐标互相转换
atomsk POSCAR vasp               # 笛卡尔坐标
atomsk POSCAR -fractional vasp   # 分数坐标

# 格式转换
# 输出文件可以是具体的文件名，也可以是文件格式；输出文件可以是多个
# 写入 cif 文件时，总是假设空间群为 P1，写入所有原子位置
atomsk XXX.cfg xyz        # 常用：xyz lammps vasp/pos cif
# atomsk 支持的构型文件格式
atsk abin bop bx cfg cel cif coo csv d12
dat dd dlp fdf gin imd jems lmp mol
pdb pos pw str vesta xmd xsf xv
xyz exyz sxyz


# 常用 options
-orient                 # 晶体取向
-rmatom N               # 删除原子
-rotate Z 45            # 旋转轴
-orthogonal-cell        # 转变为正交胞
-fractional             # 分数坐标；VASP 格式下
-sort species pack      # 使相同元素在 POSCAR 中是连续的
-fix Z                  # 固定原子坐标轴；Z/all
-shift                  # 平移
-substitute 1 Cu        # 原子类型替换成某种元素
-wrap                   # 将胞外原子施加 PBC 移至胞内
-cell add 10 y          # 在 y 方向上增加 10 埃，原子位置不变；x y z 可分别写成 H1 H2 H3；作用相当于添加真空层；set 设置 某个方向的长度
-center 0/com           # 移动所有原子，使其质心在 box 中心；会使位于 box 边缘的原子位点稍微往胞里靠，和 ase Atoms 的 center 方法效果不同
-add-atom               # 添加原子；可添加笛卡尔坐标及分数坐标（0.5*box 形式）
-wrap                   # 将胞外原子通过 PBC 到胞内

# 常用 modes
--create                # 构建晶体结构
```


---

### 其他

基于 Voronoi tessellation 算法生成多晶模型

```bash
atomsk --create fcc 4.04 Al Al_unitcell.lmp

atomsk --polycrystal Al_unitcell.lmp poly.txt -wrap Al_polycrystal.lmp

# poly.txt
box 200 100 100  # 盒子大小
random 6  # 生成 6 个随机取向&位置的晶粒
```


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090952718.png)


```bash
atomsk --create fcc 3.48 Ni -duplicate 5 5 5 Ni_host.lmp

# 有问题
atomsk Ni_host.lmp -select random 30% Ni -substitute Ni Fe -properties props.txt Fe_Ni.lmp

atomsk Fe_Ni.lmp -select random 20% Ni -substitute Ni Cr -properties props.txt Fe_Cr_Ni.lmp

atomsk --polycrystal Fe_Cr_Ni.lmp poly.txt -wrap incoloy_poly.lmp

# props.txt
Type
Fe 1
Cr 2
Ni 3

# poly.txt
box 100 100 300
random 12
```


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090953911.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090954457.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090955091.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090956815.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405090958113.png)
