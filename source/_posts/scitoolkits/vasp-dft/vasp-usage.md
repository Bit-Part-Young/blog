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
  - DFT
categories:
  - 科研工具
date: 2023-07-03 15:56:30
abbrlink: 265634
password: d93f517bc1345a0d8ff992410aca5dbc35f2e88087cdc5d9edb0c6d77d8a4c1a
---

# VASP 使用

## 介绍

- VASP 全称：Vienna Ab-initio Simulation Package


VASP6 用的赝势和 5.4.4 相同



Perdew-Burke-Ernzerhof (PBE) 形式的 generalized gradient approximation (GGA) 泛函（表达电子间的交换关联作用）

投影缀加平面波赝势（PAW）方法（描述离子 - 电子相互作用）

PAW (Projected Augmented Wave) 投影缀加波，是基于密度泛函理论（DFT）开发的描述电子、原子核行为的全电子方法

APW 是增广平面波方法（Augmented Plane Wave），也是一种全电子方法，将电子分为软、硬两部分，前者用 PW 描述，后者用 LCAO 描述（Linear Combination of Atomic Orbitals，原子轨道的线性组合）

PBE 是泛函，描述电子的交换 - 相关能的拟合函数，以 Perdew-Burke-Ernzerhof 三位开发者的名字缩写命名

PW 是指平面波基组，用于展开波函数或者说原子、分子轨道

PAW 是独立于 PBE 的理论方法，但是我们常常会见到 POTCAR 中称为 PAW-PBE 赝势，把三个概念放在一起了，意思实际上是针对不同的的泛函利用 PAW 方法相应调参优化得到的一致性赝势文件

[PAW (Projected Augmented Wave) 全电子理论计算方法](https://mp.weixin.qq.com/s/CffWYOuyAhI2zosScO7IjQ)


含各种类型计算的通用 INCAR 文件： [GitHub - WMD-group/INCAR: A generic INCAR file for the density functional theory package VASP](https://github.com/WMD-group/INCAR)


---

能带计算，ISMEAR=0？

EIGENVAL 文件内容含义

---

DFT-D3：vdW 相互作用修正

Heyd–Scuseria–Ernzerhof 泛函 (HSE06)：更精确，处理电子和光学性质

+U

```bash
# LDAU 等参数
LDAU
LDAUU
LDAUJ
```



自洽计算：均匀 K 点计算（严格一点，先弛豫后静态计算；模型较好，不 care 晶格常数，可直接静态计算）
非自洽计算：特殊 K 点


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

[VASP关键输入参数速查表 - VASPKIT与量化软件](http://vaspkit.cn/index.php/3.html)

- VASP 计算流程：[VASP的计算流程 - Jun's Blog](https://www.jun997.xyz/2021/11/10/61d157e1a6d8.html)


[VASP中POTCAR使用指南 - Jun's Blog](https://next.jun997.xyz/2022/04/14/ba8ff0b84c20.html)


输入文件及参数介绍
>[GitHub - bzkarimi/VASP: Practical guide on how to use VASP](https://github.com/bzkarimi/VASP)


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



 - NCORE: 指定单个轨道计算所使用的核数量
 - NPAR: 指定同时并行处理的能带数
 - KPAR: 指定同时并行处理的 K 点数量


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
    - VASP 官网算例中的部分 POSCAR 文件中没有元素符号行（第 6 行，不影响）
    - VASP wiki 中的示例 POSCAR 格式和 POTCAR 文件（PAW 格式）较老？
    - FCC Ni 及 Ni(100) 表面的 DOS 计算，没有先进行自洽计算
    - Ni(100) 表面的能带结构计算，K-path 是 reziprok 方式，非 Line-Mode，vaspkit 和 pymatgen 无法获取数据，只能使用 p4vasp？
    - NiO：反铁磁


---


- [ ] DOS 计算过程中 ISMEAR=0 和 -5 的差别是什么
[Part 2: More silicon](https://www.vasp.at/tutorials/latest/bulk/part2/)

---

## 示例

### 静态计算

```bash
IBRION  =  -1
NSW     =  0
ISIF    =  2
```


---

### 孤立原子计算

WIP...


---

### 收敛性测试

k 点和 ENCUT


---

### 弛豫计算

vaspkit 标准弛豫（SR） INCAR 示例：

```bash
Global Parameters
ISTART =  1            (Read existing wavefunction, if there)
ISPIN  =  1            (Non-Spin polarised DFT)
# ICHARG =  11         (Non-self-consistent: GGA/LDA band structures)
LREAL  = .FALSE.       (Projection operators: automatic)
# ENCUT  =  400        (Cut-off energy for plane wave basis set, in eV)
# PREC   =  Accurate   (Precision level: Normal or Accurate, set Accurate when perform structure lattice relaxation calculation)
LWAVE  = .TRUE.        (Write WAVECAR or not)
LCHARG = .TRUE.        (Write CHGCAR or not)
ADDGRID= .TRUE.        (Increase grid, helps GGA convergence)
# LVTOT  = .TRUE.      (Write total electrostatic potential into LOCPOT or not)
# LVHAR  = .TRUE.      (Write ionic + Hartree electrostatic potential into LOCPOT or not)
# NELECT =             (No. of electrons: charged cells, be careful)
# LPLANE = .TRUE.      (Real space distribution, supercells)
# NWRITE = 2           (Medium-level output)
# KPAR   = 2           (Divides k-grid into separate groups)
# NGXF    = 300        (FFT grid mesh density for nice charge/potential plots)
# NGYF    = 300        (FFT grid mesh density for nice charge/potential plots)
# NGZF    = 300        (FFT grid mesh density for nice charge/potential plots)

Electronic Relaxation
ISMEAR =  0            (Gaussian smearing, metals:1)
SIGMA  =  0.05         (Smearing value in eV, metals:0.2)
NELM   =  90           (Max electronic SCF steps)
NELMIN =  6            (Min electronic SCF steps)
EDIFF  =  1E-08        (SCF energy convergence, in eV)
# GGA  =  PS           (PBEsol exchange-correlation)

Ionic Relaxation
NSW    =  100          (Max ionic steps)
IBRION =  2            (Algorithm: 0-MD, 1-Quasi-New, 2-CG)
ISIF   =  2            (Stress/relaxation: 2-Ions, 3-Shape/Ions/V, 4-Shape/Ions)
EDIFFG = -2E-02        (Ionic convergence, eV/AA)
# ISYM =  2            (Symmetry: 0=none, 2=GGA, 3=hybrids)
```



---

### 态密度、能带计算

- 参考：
    - [VASP视频教程-HSE06杂化泛函计算能带和分析\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV17i4jeqER4)
    - [VASP+vaspkit计算能带结构+态密度 - 知乎](https://zhuanlan.zhihu.com/p/526969630)

- 计算流程：
    - 弛豫计算（或结构优化；初始构型很好，可忽略此步）
    - 静态自洽计算
    - 态密度计算：拷贝自洽计算生成的 WAVECAR 和 CHGCAR，非自洽计算（ICHARG=11，K 点密度变大）
    - 能带计算：拷贝自洽计算生成的 WAVECAR 和 CHGCAR，非自洽计算（ICHARG=11，K-path）

- 自洽与非自洽计算的区别：电子密度是否匹配；**不是静态与弛豫计算的区别！**

- 开启自旋极化，DOS 会有上下两条线（上下对称、不对称的含义是什么）

- 建议 NEDOS 数值稍微取密一些（多少较为合适）

- 态密度相关输出文件：DOSCAR、PROCAR

```bash
# DOS 相关参数；可不用设置
EMIN
EMAX
NEDOS


grep 'NEDOS' OUTCAR          # 查看 NEDOS 数值
grep 'EMIN' OUTCAR           # 查看 EMIN、EMAX 数值
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

- 计算：与静态计算类似；添加 `LAECHG` 参数，会生成 AECCAR0 AECCAR1 AECCAR2 三个文件

```bash
# INCAR 参数设置
IBRION      = -1
NSW         = 0
LCHARG      = .TRUE.
LAECHG      = .TRUE.      # Bader 计算


# 输出文件
# TODO: 待确认
AECCAR0                   # 全电子中的芯电子部分
AECCAR1                   # 自洽计算前的交叠原子电荷
AECCAR2                   # 全电子中的价电子部分
CHGCAR                    # 自洽计算后赝电子

# 后处理
chgsum.pl AECCAR0 AECCAR2     # 得到 CHGCAR_sum，包含了 VASP 中定义的原子总电荷密度
bader CHGCAR -ref CHGCAR_sum  # 得到 BCF.dat、ACF.dat、AVF.dat

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

### AIMD 计算

- 参考：
    - [【VASP 基础 03】关于 VAPS 分子动力学的计算细节](https://zhuanlan.zhihu.com/p/1103173525)

- 计算：

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

[GitHub - haidi-ustc/VASP-Elastic: Extracts full elastic tensor from VASP OUTCAR and calculates some useful quantities](https://github.com/haidi-ustc/VASP-Elastic)

计算得到的弹性常数值不是很准确

- kBar=0.1GPa

- [ ] Nb 计算得到的弹性常数 C44 < 0，为什么？

```bash
IBRION    =  6
NFREE     =  4  # 4 或 2
ISIF      =  3

# NSW 的设置，非 0 即可，与其具体值关系不大
```


---

### 功函数计算

WIP...


---

### 其他

- [ ] VASP 拉伸模拟

SOC：自旋轨道耦合、旋轨耦合

VASP INCAR 参数 `LSORBIT = T` 开启 SOC 时，需使用 `vasp_ncl`，使用 `vasp_std` 会出现以下报错

```txt
ERROR: non collinear calculations require that VASP is compiled
 without the flag -DNGXhalf and -DNGZhalf
ERROR: non collinear calculations require that VASP is compiled
 without the flag -DNGXhalf and -DNGZhalf
```

pymatgen 解析 SOC 的 Vasprun 文件出现以下 Warning（实际不影响）

```bash
pymatgen/io/vasp/outputs.py:161: UserWarning: Float overflow (*******) encountered in vasprun
warnings.warn("Float overflow (*******) encountered in vasprun")
```

---

红外光谱（Infrared Spectroscopy，IR）

[VASP快速计算红外光谱(IR) 后处理软件vasprun推荐](https://mp.weixin.qq.com/s/LGUFL5t8vZi3iedjtFelJQ)


---


**DFT 相关内容（梅师兄讲解）：**


没有磁性的构型添加自旋，**计算速度会变慢（2 倍及以上）**，但并不会对计算的性质结果产生影响（可以检查添加自旋后的计算磁矩是否接近 0）

vaspkit 在 KPOINTS 文件生成的选项中，若构型是六方等对称性不是很高的结构，若网格方式选择的是 MP，最后生成的 KPOINTS 文件中的网格方式还是 Gamma（会自动纠正）；推荐精度：0.03（梅）；trick：每个方向上的 k 点数与其对应的晶格常数的乘积 ka 值大于 30 或 33.33，为推荐 k 点密度；每个方向上的 ka 尽可能保持相同或接近；**0.03 对应的 K 点密度是 1/0.03=33.33**。

（SR：标准弛豫，只弛豫原子位置；LR：点阵弛豫，全弛豫）

Γ点：原点，每个构型都有一个原点

ALGO 参数：控制电子步迭代的算法，会在 OSZICAR 中看到 DAV、RMM 等不同的算法

NELM 最大设置：300 步（梅）

NELMIN：最小电子步步数；在 AIMD 中，每个离子步中的电子步可能会很少（1-2 步），需对其进行最小步数限制（可能计算结果更准确）

对于金属体系，引入 ISMEAR 和 SIGMA 展宽后，会引入虚假温度，使得 OUTCAR 中的 T*S 项不为零，其值小于 0.001eV 时，为较好的 SIGMA 值（对于金属，ISMEAR=1 或 2，SIGMA=0.2（默认值）；对于半导体，ISMEAR=-5，SIGMA=0.05）

DFT+U：计算能带

一个原子的构型也可以计算弹性常数



---

网络版的 vasp.5.4.4 没什么问题（VASP3 个版本都能编译成功）


---

VASP 相关脚本

>[GitHub - tamaswells/VASP\_script: Useful scripts for VASP](https://github.com/tamaswells/VASP_script)

- 检查 OUTCAR 文件中 T·S 项的数值是否小于 0.001eV，以检查 SIGMA 值是否设置合理：[VASP\_script/sigma.sh at master · tamaswells/VASP\_script · GitHub](https://github.com/tamaswells/VASP_script/blob/master/sigma.sh)

---

基于分子动力学模拟，可以通过对速度自关联函数（velocity autocorrelation function，VACF）进行傅里叶变换得到材料的振动态密度（vibrational density of states， VDOS）。VACF 是根据动力学模拟出来的轨迹文件和速度文件，求算系统在某一时刻的速度与另一时刻速度的关联程度的函数，直接看 VACF 并不能很直观的得到一些信息，而 VDOS 直接对应实验红外光谱，可以直观的对高温或高压下的振动变化情况等进行分析。

>[AIMD结合vaspkit计算振动态密度](https://mp.weixin.qq.com/s/gqM5c1P3BtIqi0h_tVTj5g)

---

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images/202405272344155.png)
