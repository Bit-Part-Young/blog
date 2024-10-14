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


VASP ELFCAR 文件


VASP6 用的赝势和 5.4.4 相同



Perdew-Burke-Ernzerhof (PBE) 形式的 generalized gradient approximation (GGA) 泛函（表达电子间的交换关联作用）

投影缀加平面波赝势（PAW）方法（描述离子 - 电子相互作用）

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


---

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



VASP 计算流程：[VASP的计算流程 - Jun's Blog](https://www.jun997.xyz/2021/11/10/61d157e1a6d8.html)


 - NCORE: 指定单个轨道计算所使用的核数量
 - NPAR: 指定同时并行处理的能带数
 - KPAR: 指定同时并行处理的 K 点数量


---

## 使用

### 工具

VASPMO：用于显示 VASP 计算的波函（或分子轨道）。它能够读取 VASP 的输出文件 PROCAR 和 CONTCAR，并产生 Gaussian 输出格式的输出文件，用于其它显示工具，如 Molekel、Chemcraft、Gabedit、Molden 和 JMol 等）读取，进而绘制和观看体系的分子轨道


---

### 算例

[VASP 官网案例——Calculate U for LSDA+U（线性响应方法求 U 值）](https://mp.weixin.qq.com/s/93nuu0ksVPH_MzuSKysqKA)

内含表面能、层间距变化计算公式：[Ni 100 surface relaxation - VASP Wiki](https://www.vasp.at/wiki/index.php/Ni_100_surface_relaxation)

石墨堆叠方向层间距确定：
- GGA level 的半局域（semilocal）DFT 低估了长程色散相互作用，导致石墨晶格在堆叠方向上的错误高估：8.84Å（PBE）对 6.71Å（exp）。
- 使用 Tchatchenko and Scheffler 方法（添加 IVDW 和 LVDW_EWALD 参数）考虑范德华力相互作用（van der Waals interactions）进行纠正

NiO：反铁磁

Ni(100) 表面的 DOS 计算，没有先进行 SCF 计算？
Ni(100) 表面的能带结构计算，K-path 是 reziprok 方式，非 Line-Mode，vaspkit 和 pymatgen 无法获取数据，只能使用 p4vasp？

Ni(111) 表面高精度单点能计算（截断能提高；用以计算吸附能、功函数（添加 LVHAR 参数））：[Ni 111 surface high precision - VASP Wiki](https://www.vasp.at/wiki/index.php/Ni_111_surface_high_precision)

>[Ex49 功函数（work function）的计算（一） | Learn VASP The Hard Way](https://www.bigbrosci.com/2018/09/03/ex49/)

VASP wiki 中的示例 POSCAR 格式和 POTCAR 文件（PAW 格式）较老？

[Fcc Ni DOS - VASP Wiki](https://www.vasp.at/wiki/index.php/Fcc_Ni_DOS)


[Partial DOS of CO on Ni 111 surface - VASP Wiki](https://www.vasp.at/wiki/index.php/Partial_DOS_of_CO_on_Ni_111_surface)


VASP 官网算例中的部分 POSCAR 文件中没有元素符号行（第 6 行，不影响）

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


Si 熔化 AIMD 计算：[Liquid Si - Standard MD - VASP Wiki](https://www.vasp.at/wiki/index.php/Liquid_Si_-_Standard_MD)

只有 1 个 K 点，可以用 vasp_gam 来运行，加快运行速度

Pair correlation function 数据保存在 PCDAT 文件中


Si 结晶 AIMD 计算（扩散系数及 PCF）：[Liquid Si - Freezing - VASP Wiki](https://www.vasp.at/wiki/index.php/Liquid_Si_-_Freezing)

>[利用分子动力学轨迹计算粒子运动的均方位移和扩散系数 - 知乎](https://zhuanlan.zhihu.com/p/542642528)

```bash
#!/bin/bash

for i in 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000; do
    # awk 的作用是什么
    awk <PCDAT.$i >pair.$i ' NR==8 {pcskal=$1} NR==9 {pcfein=$1} NR>=10036 {line=line+1; print (line-0.5)*pcfein/pcskal,$1} '
done

gnuplot -e "set terminal jpeg; set key left; set xlabel 'r (Ang)'; set ylabel 'PCF'; set style data lines; plot 'pair.2000','pair.1400','pair.800' " > pair.jpg
```


---


- [ ] DOS 计算过程中 ISMEAR=0 和 -5 的差别是什么
[Part 2: More silicon](https://www.vasp.at/tutorials/latest/bulk/part2/)

---

## 示例

### 静态计算

WIP...


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

计算流程：
- 弛豫计算（初始构型很好，可忽略此步）
- 静态自洽计算
- 非自洽计算（能带：ICHARG=11，k-path）
- 非自洽计算（态密度：ICHARG=11，k 点密度变大）


---

### Bader 电荷计算

WIP...


---

### AIMD 计算

WIP...


---

### 弹性常数计算

计算得到的弹性常数值不是很准确

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


**DFT 相关内容（梅师兄讲解）：**

POTCAR 中的一些参数

VRHFIN：该元素考虑的价电子（在写论文的计算 method 时会用到）

赝势种类：模守恒赝势、超软赝势（它们应用在哪些体系？）

没有磁性的构型添加自旋，计算速度会变慢（2 倍？），但并不会对计算的性质结果产生影响（可以检查添加自旋后的计算磁矩是否接近 0）

能带计算：先正常/自洽计算，生成 WAVECAR 和 CHGCAR；后进行非自洽计算

自洽与非自洽计算的区别：电子密度是否匹配；**不是静态与弛豫计算的区别！**

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
