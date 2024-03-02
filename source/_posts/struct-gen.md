---
title: 结构建模
top: false
cover:
toc: true
mathjax: true
summary: 结构建模
tags:
  - 结构建模
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
date: 2023-10-15 09:30:00
abbrlink: 38100
password:
---

# 结构建模

结构建模常用工具：

- [pymatgen](https://pymatgen.org/)
- [ASE](https://wiki.fysik.dtu.dk/ase/)
- [latgen](https://github.com/lingtikong/latgen)
- Atomsk：[Atomsk - GitHub](https://github.com/pierrehirel/atomsk)[Atomsk 首页](https://atomsk.univ-lille.fr/)
- [PyXtal](https://pyxtal.readthedocs.io/)
- Material Studio（Win + Linux）

---

构型可视化工具：
- [OVITO](https://www.ovito.org/)
- [VESTA](https://jp-minerals.org/vesta/en/download.html)

当构型文件中的原子坐标为负时，可使用 VESTA 导入导出使其变为正。

VESTA 软件无法读取 `.poscar` 格式构型文件（Materials Project），OVITO 可以，建议将 VASP 格式文件统一为 `.vasp`



二维晶体：10 种点群，17 种空间群（墙纸群 (wallpaper group)）



vaspkit 完整功能列表：[Features — VASPKIT 1.4 documentation](https://vaspkit.com/features.html)


Material Studio 构型文件格式：`.xsd`


CASTEP 的输入构型文件格式：`*.cell`

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202312262058798.png)


CASTEP 赝势路径
```text
BIOVIA\Materials Studio 19.1\share\Resources\Quantum\Castep\Potentials
```

- [ ] 了解 aflow prototype 中的 primitive vectors 的公式及其含义，及如何实现 unit 与 primitive 互相转变的


- [ ] D019 结构（Ti3Al）原子位点，mp 与 latgen 两者有区别（和 hcp 类似的问题）



晶体学库


原型百科全书（prototype-encyclopedia）
>[aflow.org/prototype-encyclopedia/](http://aflow.org/prototype-encyclopedia/)




常见结构的空间群符号

|    结构    | 空间群符号 | 空间群 number |
|:----------:|:----------:|:------------:|
|   金刚石   |       Fd-3m     |      227        |
|    FCC     |       Fm-3m     |     225          |
|    BCC     |      Im-3m      |       229       |
|    HCP     |      P6_3/mmc      |      194        |
|    岩盐 (rocksalt NaCl)    |        Fm-3m    |              |
| 立方钙钛矿 (perovskite CaTiO3) |      Pm-3m      |              |
| CsCl           |      Pm-3m      |              |

一些结构的 prototype

| Prototype | Strukturbericht designation | Pearson symbol | Space group number | Space group symbol |
| :---------: | :--------: | :------: | :-----: | :-----: |
|      W     |              A2               |      cI2          |      229              |            Im-3m        |

BCC
>[AFLOW Prototype: A\_cI2\_229\_a](https://www.aflowlib.org/prototype-encyclopedia/A_cI2_229_a.html)

FCC
>[AFLOW Prototype: A\_cF4\_225\_a](https://www.aflowlib.org/prototype-encyclopedia/A_cF4_225_a.html)

HCP
>[AFLOW Prototype: A\_hP2\_194\_c](https://www.aflowlib.org/prototype-encyclopedia/A_hP2_194_c.html)

$\beta$ -Sn
>[AFLOW Prototype: A\_tI4\_141\_a](https://www.aflowlib.org/prototype-encyclopedia/A_tI4_141_a.html)

Cr5B3
>[AFLOW Prototype: A3B5\_tI32\_140\_ah\_cl](https://www.aflowlib.org/prototype-encyclopedia/A3B5_tI32_140_ah_cl.html)

Mn5Si3
>[AFLOW Prototype: A5B3\_hP16\_193\_dg\_g](https://www.aflowlib.org/prototype-encyclopedia/A5B3_hP16_193_dg_g.html)







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

结构可视化

MoS2
>[Molybdenum Disulfide - MoS2](https://www.chemtube3d.com/ss-mos2/)


金刚石、石墨、C60、碳纳米管
>[Introductory Structures Allotropes of Carbon (Diamond and Graphite) and Pentacene](https://www.chemtube3d.com/claydencarbonallotropes/)

hcp
>[Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/)

perovskite
>[CaTiO3 - Perovskite: Interactive 3D Structure](https://www.chemtube3d.com/_perovskitefinal/)



hcp 结构原胞原子坐标有两种形式：

- 一个原子在原点，另一个在胞内：latgen 和 ase，(0.0 0.0 0.0) (2/3 1/3 0.5)
- 两个原子均在胞内：pymatgen 和 pyxtal，(1/3 2/3 1/4) (2/3 1/3 3/4)
- 两种形式无本质区别，两者可通过过周期性平移进行互相转化
- [Hexagonal close packing - hcp: Interactive 3D Structure](https://www.chemtube3d.com/hexagonal-close-packing/) 有这两种形式的可视化



---

## 基本概念

---

## 复杂结构

---

## 界面/异质结

在 latgen、VASPKIT 和 MS 中，称为 build layer


VASPKIT 804 选项，会根据用户输入的错配度要求生成满足条件的系列界面构型 POSCAR 文件，并输出 log 信息



---

## 晶界

- [任意CSL值晶界建模(一)](https://mp.weixin.qq.com/s/u6qvvsnszPU6pr8u4O0Tgw)、[任意CSL值晶界建模(二)](https://mp.weixin.qq.com/s/ZXrnbjKbsKerm_ZVDSoDFQ)

- aimsgb 程序：[aimsgb documentation](https://aimsgb-docs.readthedocs.io/)、[aimsgb - GitHub](https://github.com/ksyang2013/aimsgb)


CSL 重合位置点阵理论


tilted grain boundaries 晶界面平行于旋转轴

twisted grain boundary 晶界面垂直于旋转轴


根据特定晶界构建

寻找晶界





---

## 碳纳米管

WIP…

---

## 石墨烯晶体结构

二维；六方结构；最近邻原子间距约为 1.42 埃


![graphene-structure.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307151658266.png)


>CASTRO NETO A H, GUINEA F, PERES N M R, 等, 2009. The electronic properties of graphene[J/OL]. Reviews of Modern Physics, 81(1): 109-162. DOI:10.1103/RevModPhys.81.109.



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

>[Atomsk - Tutorial - Graphene and Nanotubes](https://atomsk.univ-lille.fr/tutorial_nanotubes.php)


注：
- 对于六方结构，其中的原子位置坐标随基矢的选择会有些许不同，但本质一样都是一样的；
- 基矢以逆时针为正方向；
- C 的 ENMAX 为 400（所有元素中最大，所以 pymatgen 中 ENCUT 的默认设置为 520）。



---

## 石墨晶体结构

六方结构；z 轴方向长度约为 6.7 埃



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

## atomsk

>[Atomsk - Tutorials](https://atomsk.univ-lille.fr/tutorials.php)


atomsk 中的 cfg 格式文件用 ovito 打开，VESTA 无法打开


介绍及使用



将六方结构转变成正交结构
```bash
atomsk POSCAR -orthogonal-cell -sort species pack vasp
```

>[crystallography - How to transform lattice in VESTA - Matter Modeling Stack Exchange](https://mattermodeling.stackexchange.com/questions/7263/how-to-transform-lattice-in-vesta)
>[Atomsk - Tutorial - VASP](https://atomsk.univ-lille.fr/tutorial_vasp.php)


广义层错
>[Atomsk - Tutorial - Stacking fault](https://atomsk.univ-lille.fr/tutorial_stackingfault.php)



---

## Material Studio

### Material Studio 2019 安装

>需联网安装

>安装路径及 license 文件路径不要有中文

- 打开 “MS2019\\安装文件\\BIOVIA Materials Studio 2019.msi” 或 “setup.exe” 文件，按照提示进行正常安装，直到安装完成。

- 安装成功后，以笔记本方式打开 “MS2019\\激活文件\\msi.lic”，将计算机名复制到许可文件中替换 “this_host”，然后保存即可。

>计算机名必须由英文和数字组成，如果之前已经更改为中文，需要使用计算机的 IP 地址代替计算机名

![msi-lic.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211448615.jpg)

- 在开始菜单页面，打开 BIOVIA 文件夹中的 “License Administrator 2019”，选择 Install License，然后点击 Browser 选择 msi.lic 许可文件

>许可文件所在的文件目录不能包含中文，所以将其复制到 C 盘根目录下，然后选择载入即可

![install-license.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211449950.jpg)

- 弹出如下提示，表明软件成功注册激活

![success-install.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211447160.jpg)

- 至此，Materials Studio 2019 破解版完成破解，运行打开软件，用户可以无限制免费使用了。


---

### 卸载

- 点击安装包中的 Autorun.exe——install material studio——选择 remove
- 在设置中卸载 License Pack（先卸载它，后面的会自动卸载）和 License Pack （X64）

---

### 使用

- 文件保存路径不要有中文
- 很卡的情况
  - 解决方法：tool-option-graphhics 勾选 disable graphic（取消硬件加速）
  - 输入法的兼容性打开

---

复杂结构构建：
- 可通过其他程序构建（如 pymatgen、ase、pyxtal 等），保存成 ase 可读的文件格式，使用 ase 中的 xsd 模块中 write_xsd 函数转换成 xsd 格式文件，之后直接导入到 MS 中即可
- 在 MS 中手动构建


表面构建：表面构建过程中，可以调整 thickness（从最小值调整到 1.0），得到表面不同终端的数目和层间距

MS 中的构型文件可保存成 res 格式，之后使用 posconv 可转换成其他格式
