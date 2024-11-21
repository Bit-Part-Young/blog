---
title: VASP 使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: VASP 使用
description: VASP 使用
tags:
  - VASP
categories:
  - 科研工具
  - VASP
date: 2023-07-03 15:56:30
abbrlink: 265634
password:
---

# VASP 使用

## 介绍

- VASP 全称：Vienna Ab-initio Simulation Package

多粒子体系的复杂性主要体现在交换关联能 $E_{xc}$ 项上，对交换关联能 $E_{xc}$ 的精确描述是求解 KS 方程的关键所在。

引入关于电子密度函数的近似泛函，如 LDA、GGA、杂化泛函等

LDA 忽略了非均匀效应，认为在具有同等电子密度的前提下，空间任意点的 $E_{xc}$ 相同与均匀电子云的相同

GGA 对 LDA 中忽略的电子密度的非均匀效应进行了修正，即加入电子密度梯度的作用

Perdew-Burke-Ernzerhof (PBE) 形式的 generalized gradient approximation (GGA) 泛函（表达电子间的交换关联作用）

全电子势描述电子 - 原子核相互作用，如 EMTO（The Exact Muffin-Tin Orbitals）

投影缀加平面波赝势（PAW）方法（描述离子 - 电子相互作用）

PAW (Projected Augmented Wave) 投影缀加波，是基于密度泛函理论（DFT）开发的描述电子、原子核行为的全电子方法

APW 是增广平面波方法（Augmented Plane Wave），也是一种全电子方法，将电子分为软、硬两部分，前者用 PW 描述，后者用 LCAO 描述（Linear Combination of Atomic Orbitals，原子轨道的线性组合）

PBE 是泛函，描述电子的交换 - 相关能的拟合函数，以 Perdew-Burke-Ernzerhof 三位开发者的名字缩写命名

PW 是指平面波基组，用于展开波函数或者说原子、分子轨道

PAW 是独立于 PBE 的理论方法，但是我们常常会见到 POTCAR 中称为 PAW-PBE 赝势，把三个概念放在一起了，意思实际上是针对不同的的泛函利用 PAW 方法相应调参优化得到的一致性赝势文件

[PAW (Projected Augmented Wave) 全电子理论计算方法](https://mp.weixin.qq.com/s/CffWYOuyAhI2zosScO7IjQ)


含各种类型计算的通用 INCAR 文件： [GitHub - WMD-group/INCAR: A generic INCAR file for the density functional theory package VASP](https://github.com/WMD-group/INCAR)


---

DFT-D3：vdW 相互作用修正

Heyd–Scuseria–Ernzerhof 泛函 (HSE06)：更精确，处理电子和光学性质


METAGGA

SCAN (Strongly constrained and appropriately normed)

[METAGGA - VASP Wiki](https://www.vasp.at/wiki/index.php/METAGGA)



---

### 参考资料

- VASP INCAR 参数：[Category:INCAR tag - Vaspwiki](https://www.vasp.at/wiki/index.php/Category:INCAR_tag)
- VASP POSCAR：[POSCAR - Vaspwiki](https://www.vasp.at/wiki/index.php/POSCAR)
- VASP KPOINTS：[KPOINTS - Vaspwiki](https://www.vasp.at/wiki/index.php/KPOINTS)
- VASP 赝势推荐：[Available PAW potentials - Vaspwiki](https://www.vasp.at/wiki/index.php/Available_PAW_potentials#Recommended_potentials_for_DFT_calculations)
- VASP 输出文件：[Category:Output files - Vaspwiki](https://www.vasp.at/wiki/index.php/Category:Output_files)
- VASP Manual：[The VASP Manual - Vaspwiki](https://www.vasp.at/wiki/index.php/The_VASP_Manual)
- VASP Categories：[Categories - Vaspwiki](https://www.vasp.at/wiki/index.php/Special:Categories)
- VASP Tutorial：[Category:Tutorials - Vaspwiki](https://www.vasp.at/wiki/index.php/Category:Tutorials)、[Tutorials](https://www.vasp.at/tutorials/latest/)
- VASP Examples：[Category:Examples - Vaspwiki](https://www.vasp.at/wiki/index.php/Category:Examples)

- VASP 计算流程：[VASP的计算流程 - Jun's Blog](https://www.jun997.xyz/2021/11/10/61d157e1a6d8.html)
- [VASP关键输入参数速查表 - VASPKIT与量化软件](http://vaspkit.cn/index.php/3.html)

- [VASP中POTCAR使用指南 - Jun's Blog](https://next.jun997.xyz/2022/04/14/ba8ff0b84c20.html)

- 输入文件参数介绍：[GitHub - bzkarimi/VASP: Practical guide on how to use VASP](https://github.com/bzkarimi/VASP)


VASP 中计算电子基态的算法
>[Algorithms used in VASP to calculate the electronic groundstate - Vaspwiki](https://www.vasp.at/wiki/index.php/Algorithms_used_in_VASP_to_calculate_the_electronic_groundstate)


k 点积分
>[K-point integration - Vaspwiki](https://www.vasp.at/wiki/index.php/K-point_integration)


phonon dispersion 计算
>[Computing the phonon dispersion - Vaspwiki](https://www.vasp.at/wiki/index.php/Computing_the_phonon_dispersion)


原子计算
>[Calculation of atoms - Vaspwiki](https://www.vasp.at/wiki/index.php/Calculation_of_atoms)


分子动力学计算
>[Molecular dynamics calculations - Vaspwiki](https://www.vasp.at/wiki/index.php/Molecular_dynamics_calculations)

>[Molecular dynamics - Tutorial - Vaspwiki](https://www.vasp.at/wiki/index.php/Molecular_dynamics_-_Tutorial)


GW 计算
>[Practical guide to GW calculations - Vaspwiki](https://www.vasp.at/wiki/index.php/Practical_guide_to_GW_calculations)

>[GW approximation](https://www.vasp.at/tutorials/latest/gw/)


内含 VASP 计算相关的案例
>[GitHub - hello-arun/tutorials: Tutorials of codes such as VASP, Quantum Espresso and Lammps](https://github.com/hello-arun/Tutorial-for-kids)


[DFT磁性的计算(本例为用VASP计算FCC Ni的磁矩)](https://mp.weixin.qq.com/s/4ygwBJsAjVVQ3slPZeevhw)


[VASP教学 - 计算材料学](https://ywwang0.github.io/2020/11/09/VASP%E6%95%99%E5%AD%A6/)


---

## 使用

### 工具

- VASPMO：用于显示 VASP 计算的波函（或分子轨道）。它能够读取 VASP 的输出文件 PROCAR 和 CONTCAR，并产生 Gaussian 输出格式的输出文件，用于其它显示工具，如 Molekel、Chemcraft、Gabedit、Molden 和 JMol 等）读取，进而绘制和观看体系的分子轨道


---

### 算例

- [VASP 官网案例——Calculate U for LSDA+U（线性响应方法求 U 值）](https://mp.weixin.qq.com/s/93nuu0ksVPH_MzuSKysqKA)

- 内含表面能、层间距变化计算公式：[Ni 100 surface relaxation - VASP Wiki](https://www.vasp.at/wiki/index.php/Ni_100_surface_relaxation)

- 石墨堆叠方向层间距确定：
    - GGA level 的半局域（semilocal）DFT 低估了长程色散相互作用，导致石墨晶格在堆叠方向上的错误高估：8.84Å（PBE）对 6.71Å（exp）。
    - 使用 Tchatchenko and Scheffler 方法（添加 IVDW 和 LVDW_EWALD 参数）考虑范德华力相互作用（van der Waals interactions）进行纠正


- Ni(111) 表面高精度单点能计算（截断能提高；用以计算吸附能、功函数（添加 LVHAR 参数））：[Ni 111 surface high precision - VASP Wiki](https://www.vasp.at/wiki/index.php/Ni_111_surface_high_precision)

- 功函数相关
    - [Partial DOS of CO on Ni 111 surface - VASP Wiki](https://www.vasp.at/wiki/index.php/Partial_DOS_of_CO_on_Ni_111_surface)
    - [Ex49 功函数（work function）的计算（一） - Learn VASP The Hard Way](https://www.bigbrosci.com/2018/09/03/ex49/)


- [ ] 振动频率计算的意义？NFREE 参数，振动 mode？
>[表面吸附分子的振动自由能计算 - 知乎](https://zhuanlan.zhihu.com/p/397862258)


```text
# 用的是哪个泛函？
   TITEL  = PAW Ni
   TITEL  = PAW C
   TITEL  = PAW O
```


- [ ] K 点网格某方向数值为奇数，$\Gamma$ 中心？
>[VASP K点问题 - 知乎](https://zhuanlan.zhihu.com/p/397873103)

>[晶体高对称点 - 知乎](https://zhuanlan.zhihu.com/p/423772139)

- AIMD 相关
    - Si 熔化 AIMD 计算：[Liquid Si - Standard MD - VASP Wiki](https://www.vasp.at/wiki/index.php/Liquid_Si_-_Standard_MD)
    - Si 结晶 AIMD 计算（扩散系数及 PCF）：[Liquid Si - Freezing - VASP Wiki](https://www.vasp.at/wiki/index.php/Liquid_Si_-_Freezing)
    - 只有 1 个 K 点，可以用 vasp_gam 来运行，加快运行速度
    - [利用分子动力学轨迹计算粒子运动的均方位移和扩散系数 - 知乎](https://zhuanlan.zhihu.com/p/542642528)

- 注意事项：
    - VASP 官网计算示例
    - VASP 官网算例中的部分 POSCAR 文件格式非 VASP5 版本
    - VASP Wiki 中的示例 POSCAR 格式和 POTCAR 文件（PAW 格式）较老？
    - FCC Ni 及 Ni(100) 表面的 DOS 计算，没有先进行自洽计算
    - Ni(100) 表面的能带结构计算，K-path 是 reziprok 方式，非 Line-Mode，vaspkit 和 pymatgen 无法获取数据，只能使用 p4vasp？
    - NiO：反铁磁
    - [ ] DOS 计算过程中 ISMEAR=0 和 -5 的差别是什么：[Part 2: More silicon](https://www.vasp.at/tutorials/latest/bulk/part2/)



---

## 示例

```bash
# 能带结构、DOS 计算
ISTART = 1
ICHARG = 11

# 其余计算
ISTART = 0
ICHARG = 2

# 断点后续算；其他参数值不改变
ISTART = 1
ICHARG = 1
```


---

### 静态计算

- INCAR 参数示例：

```bash
IBRION = -1
NSW    = 0
ISIF   = 2
```


---

### 孤立原子计算

- 建立一个简单立方胞（SC），将原子置于中心；K 点密度为 1\*1\*1，Gamma-centered MP

```bash

```


---

### 收敛性测试

- [精度与成本平衡之道——K点收敛性测试 (qq.com)](https://mp.weixin.qq.com/s?__biz=MzIzODczNjY3OA==&mid=2247484324&idx=1&sn=0fa6af1be7c169a00ac153d22186e642&chksm=e93587edde420efb4c41704560cc2b3dbe50ebc9c3fc138d505313c8e8b12903991df0791af0&scene=21#wechat_redirect)

- [精度与成本平衡之道——ENCUT收敛性测试 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/348826693)

- [自洽计算的K点选取 和 KPOINTS 文件生成方法 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-13066-1-1.html)

- 对 K 点和 ENCUT 进行收敛性测试，同一构型采用超胞和单胞得到的结果类似，单胞的 ENCUT 值可直接用于超胞计算，单胞的 K 点密度等比例缩小用于超胞计算

- 个人收敛性测试步骤（先 K 点后 KPOINTS）：
    - 先粗结构优化（ENCUT 为 1.3ENMAX，K 点密度稍密）
    - 之后进行 K 点测试（ENCUT 为 1.3ENMAX）
    - 之后进行 ENCUT 测试（K 点密度选择达到收敛性标准的）
    - 采用达到收敛性标准的 K 点密度 + ENCUT 进行细结构优化
    - 个人经验：计算体系含 C 时，可不进行 ENCUT 测试，直接使其为 520（C 赝势中的 ENMAX=400）

```bash

```


---

### 弛豫计算

- INCAR 参数示例：

```bash
Global Parameters
ISTART =  0
ICHARG =  2
ISPIN  =  1
ENCUT  =  400
PREC   =  Accurate

Electronic Relaxation
ISMEAR = 0
SIGMA  = 0.05
NELMIN = 6
NELM   = 90
EDIFF  = 1E-06

Ionic Relaxation
NSW    = 100
IBRION = 2
ISIF   = 3
EDIFFG = -1E-02
```


---

### 确定晶格常数

- EOS 拟合方法（扫描法）

在晶格常数的实验值附近取 10 个点，分别进行单点计算；用能量最小值作为判据

- 直接（弛豫）优化方法


用力弛豫时，若存在内变量的体系，如固溶体，溶质原子几乎不会待在在平衡位置（有可能），近邻的溶剂原子偏离其理想位置，因此需要对它们的位置进行弛豫，用扫描的方法，不做弛豫，得不到准确的位置，因此需要用到弛豫的方法；对于计算胞对称性不太好，用扫描法，一般适合只有一个变量变化，变量多，需要用弛豫的方法（hcp 结构）


---

### 点缺陷形成能

空位、间隙原子

超胞尽可能是立方体

要做原子数 n（不能太大）和空位形成能的收敛性测试


---

### 态密度、能带计算

- 参考：
    - [VASP视频教程-HSE06杂化泛函计算能带和分析\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV17i4jeqER4)
    - [VASP+vaspkit计算能带结构+态密度 - 知乎](https://zhuanlan.zhihu.com/p/526969630)

- 计算流程：
    - 弛豫计算（或结构优化；初始构型很好，可忽略此步）
    - 静态自洽计算（可不用拷贝自洽计算生成的 WAVECAR）
    - 态密度计算：拷贝自洽计算生成的 CHGCAR，非自洽计算（ICHARG=11，增加 K 点密度；`K*a=45` 可满足要求）
    - 能带计算：拷贝自洽计算生成的 CHGCAR，非自洽计算（ICHARG=11，K-path）

- 自洽与非自洽计算的区别：电子密度是否匹配；**不是静态与弛豫计算的区别！**

- 开启自旋极化，DOS 会有上下两条线（自旋向上、向下；上下对称、不对称的含义是什么）

- 建议 NEDOS 数值稍微取密一些（NEDOS=2000/3000 足够好）

- DOS、能带计算耗时相对较少

- DOS 计算相比弛豫对截断能没有那么敏感，截断能值可以设小一些（？）

- 态密度相关输出文件：DOSCAR、PROCAR

```bash
# 能带计算
ISMEAR = 0
```


---

### Bader 电荷计算

- 程序：[Code: Bader Charge Analysis](https://theory.cm.utexas.edu/henkelman/code/bader/)

- 参考：
    - [CsPbI3 电荷密度](https://mp.weixin.qq.com/s/eWQQwBizItEMej_ocDzoXw)
    - [Bader电荷可视化](https://mp.weixin.qq.com/s/32R0egD3mZbY598lz6F5ig)
    - [电子结构分析【04】——差分电荷密度和电荷布居要如何分析？要点在这里](https://mp.weixin.qq.com/s/NLEP8tG6KWfLOgnKqA9L_g)
    - [差分电荷和Bader电荷分布 - Dong Fan's Blog](https://agrh.github.io/2019/08/06/ded/)
    - [VASP视频教程-电荷差分与bader分析\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1L6pWeVESu)

- Bader 电荷：
    - DFT 计算中常见的一种电荷分析方法，通过其对电荷的定义计算出每个原子在体系中得失电子的情况，即净电荷
    - 又称为 atom-in-molecule (AIM) charge，是一种将空间中的电子密度的零通量分界面作为划分电荷所属相应原子的方法
    - 通过处理 VASP 得到的 CHGCAR 或 Gaussian 格式的 cube 文件计算体系的 Bader 电荷
    - 电荷的定义或者说划分方法会明显影响计算数值，所以不同的分析方法得到的绝对数值没有太大的意义，而是应该在不同体系之间横向比较
    - 电荷布居分析：统计每个原子带多少电荷的办法；Bader 电荷布居（Bader charge analysis）；还有 Mulliken 布居，Lodwin 布居，Hirshfield 布居等

- 差分电荷密度：charge density difference；原子相互作用后（成键前后）的电荷密度与初始原子电荷密度之差；可分析在成键和成键电子耦合过程中的电荷移动以及成键极化方向等性质

- 计算：与静态计算类似；添加 `LAECHG` 参数（计算内层电荷密度和价电子层电荷密度，将两个文件叠加求得总电荷，再求解 Bader 电荷）

```bash
# INCAR 参数设置
IBRION      = -1
NSW         = 0
LCHARG      = .TRUE.
LAECHG      = .TRUE.      # Bader 计算


# 后处理
chgsum.pl AECCAR0 AECCAR2     # 得到 CHGCAR_sum，包含了 VASP 中定义的原子总电荷密度
bader CHGCAR -ref CHGCAR_sum  # 得到 BCF.dat、ACF.dat、AVF.dat
cat ACF.dat                   # 查看 CHARGE 列

# BCF.dat
# TODO: 待确认
# 电荷极大值序号和坐标；体积内的bader电荷积分；距离极大值最近的原子和距离

# ACF.dat；包含了所有原子的价电子数信息
# TODO: 待确认
# 原子序号和坐标；价电荷数；到零通量面最小距离；原子体积）
# 示例
#         X           Y           Z       CHARGE      MIN DIST  ATOMIC VOL
--------------------------------------------------------------------------------
1    3.164973    3.164973   3.164973    8.129202     2.022066   50.790052
2    0.000000    0.000000   0.000000   13.223566     1.494570   30.667423
3    0.000000    0.000000   3.164973    7.549077     1.582486   57.390231
4    3.164973    0.000000   0.000000    7.549079     1.582486   57.390910
5    0.000000    3.164973   0.000000    7.549079     1.582486   57.390910
--------------------------------------------------------------------------------
VACUUM CHARGE:              0.0000
VACUUM VOLUME:              0.0000
 NUMBER OF ELECTRONS:        44.0000
```


---

### ELF

- 参考：[VASP视频教程-电荷局域分析\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1HP4iecEjM)

- 电子局域化函数 (electron localization function, ELF)

- 在自洽计算中添加/修改以下参数；计算结束后，得到 ELFCAR 文件；使用 VESTA 进行可视化；可将 ELF 图与构型视图叠放在一起，对照效果更好

```bash
PREC        = Accurate
LELF        = .TRUE.
```


---

### 弹性常数计算

- 可以用原胞计算弹性常数

- VASP 计算弹性常数，其 ENCUT 数值要比弛豫计算的更高，通常 1.5 倍 ENMAX

[GitHub - haidi-ustc/VASP-Elastic: Extracts full elastic tensor from VASP OUTCAR and calculates some useful quantities](https://github.com/haidi-ustc/VASP-Elastic)

计算得到的弹性常数值不是很准确

- kBar=0.1GPa

- [ ] Nb 计算得到的弹性常数 C44 < 0，为什么？

```bash
IBRION = 6
NFREE  = 4  # 4 或 2
ISIF   = 3

# NSW 的设置，非 0 即可，与其具体值关系不大
```


---

### 功函数计算

WIP...


---

### AIMD 计算

- 参考：
    - [【VASP 基础 03】关于 VAPS 分子动力学的计算细节](https://zhuanlan.zhihu.com/p/1103173525)

- 参数设置

```bash
# INCAR 参数设置
MDALGO      = 2
SMASS       = 0

TEBEG       = 300
TEEND       = 300


# 数据获取
# 压强
grep "external pressure" OUTCAR | awk '{print $4}'
```


基于分子动力学模拟，可以通过对速度自关联函数（velocity autocorrelation function，VACF）进行傅里叶变换得到材料的振动态密度（vibrational density of states， VDOS）。VACF 是根据动力学模拟出来的轨迹文件和速度文件，求算系统在某一时刻的速度与另一时刻速度的关联程度的函数，直接看 VACF 并不能很直观的得到一些信息，而 VDOS 直接对应实验红外光谱，可以直观的对高温或高压下的振动变化情况等进行分析。

>[AIMD结合vaspkit计算振动态密度](https://mp.weixin.qq.com/s/gqM5c1P3BtIqi0h_tVTj5g)


---

### 其他

- [ ] VASP 拉伸模拟

---

- SOC：自旋轨道耦合、旋轨耦合
    - VASP INCAR 参数 `LSORBIT = T` 开启 SOC 时，需使用 `vasp_ncl`，使用 `vasp_std` 会出现以下报错

```txt
ERROR: non collinear calculations require that VASP is compiled
 without the flag -DNGXhalf and -DNGZhalf
ERROR: non collinear calculations require that VASP is compiled
 without the flag -DNGXhalf and -DNGZhalf
```

```bash
# pymatgen 解析 SOC 的 Vasprun 文件出现以下 Warning（实际不影响）
pymatgen/io/vasp/outputs.py:161: UserWarning: Float overflow (*******) encountered in vasprun
warnings.warn("Float overflow (*******) encountered in vasprun")
```

---

- 红外光谱（Infrared Spectroscopy，IR）：[VASP快速计算红外光谱(IR) 后处理软件vasprun推荐](https://mp.weixin.qq.com/s/LGUFL5t8vZi3iedjtFelJQ)

- 静电势能计算: 在 INCAR 中添加 LVHAR=.TRUE. 参数

- 表面吸附位点：
    - Top 顶位（T）
    - Bridge 桥位（B）
    - Hollow 洞位（H）
