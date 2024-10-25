---
title: VASP 输入文件
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: VASP 输入文件
description: VASP 输入文件
tags:
  - VASP
categories:
  - 科研工具
  - VASP
date: 2024-10-14 11:01:30
abbrlink: 410103
password:
---

# VASP 输入文件

包括 INCAR、POSCAR、KPOINTS 和 POTCAR4 个输入文件。



---

## POSCAR

- 构型文件；生成 POSCAR 文件是 VASP 计算的起点

- 需至少包含体系的几何信息（晶格常数、基矢、元素种类及对应原子数目）和原子位置（以及 AIMD 计算时原子的初始速度（不常用））；可手动生成，也可从一些在线晶体学数据库（Material Project、aflow、icsd 等）中获取
    - 第 1 行：Comment line 注释行；可对体系进行描述，也可空着
    - 第 2-5 行：Scaling factor and lattice，缩放因子和基矢；与体系的晶格常数符合即可；第二行值如果为负数，表示体积
    - 第 6-7 行：Ion species and numbers，元素种类（VASP4 可没有该行）及对应原子数目；**元素种类的顺序需与 POTCAR 文件中的一致**；
    - 第 8-N 行：Ion positions 原子坐标；Direct（首字母大写或只写 D 均可）表示分数坐标，Cartesian（或 C）表示笛卡尔坐标（若第 8 行是 Selective Dynamics，原子位置后面每个方向需添加 T/F，表示是否对 x y z 方向进行固定）
    - 原子坐标信息之后是原子的初始速度信息

- 注意事项：
    - VASP 根据 POSCAR 文件确定体系的对称性。原子位置精度不够（位数太少）是一个常见错误。为更好地利用 VASP 中的对称性，强烈建议在 POSCAR 文件中指定至少 7 位有效数字的原子位置（和晶格参数，最好多一些）

- 示例：

```text
Cubic BN
3.57
0.0 0.5 0.5
0.5 0.0 0.5
0.5 0.5 0.0
B N
1 1
Direct
0.00 0.00 0.00
0.25 0.25 0.25


MgO Fm-3m (No. 225)
1.0
 2.606553 0.000000 1.504894
 0.868851 2.457482 1.504894
 0.000000 0.000000 3.009789
 Mg O
 1 1
direct
 0.000000 0.000000 0.000000 Mg
 0.500000 0.500000 0.500000 O


Cubic BN
3.57
0.00000000 0.50000000 0.50000000
0.50000000 0.00000000 0.50000000
0.50000000 0.50000000 0.00000000
B N
1 1
Selective dynamics
direct
0.00000000 0.00000000 0.00000000 T T F
0.25000000 0.25000000 0.25000000 F F F
```



---

## POTCAR

- [Available pseudopotentials - VASP Wiki](https://www.vasp.at/wiki/index.php/Available_pseudopotentials)：含 PBE52、PBE54、PBE64 赝势介绍，赝势加后缀之间的区别

- 赝势文件；包含计算体系中每种元素的赝势（元素种类的数量大于 1，只需将各元素种类的 POTCAR 文件依次连接起来即可，与 POSCAR 文件中元素种类顺序对应）

- PBE 赝势可分为：无后缀、\_pv、\_sv、\_d 和数字后缀，即 semi-core 的 p、s、d 当做价态处理

```bash
# 多个元素种类的 POTCAR 文件合并
cat POTCAR.1 POTCAR.2 > POTCAR    


# POTCAR 文件中的关键参数
ZVAL                     # 价电子数；与 VRHFIN 及第二行内容对应
VRHFIN                   # 该元素赝势的价电子排布（在写论文的计算 method 时会用到）
LEXCH                    # 泛涵；PE
RCORE                    # 最大截止半径，单位是波尔 bohr
ENMAX                    # cutoff 取值一般为 1.3 * ENMAX


#  信息获取
grep -E 'TIT|VRHFIN|ENMAX|ZVAL' POTCAR

grep -A1 '  PAW_PBE' POTCAR
```

- 注意事项：
    - 赝势种类：模守恒赝势、超软赝势 USPP（它们应用在哪些体系？）
    - 赝势目录中每个类型的泛函目录中有一个 data_base 文件，里面包含每个赝势对应元素 3 种可能结构的基态能量数据
    - PSCTR 文件：控制赝势生成文件：[PSCTR](https://www.smcm.iqfr.csic.es/docs/vasp/node251.html)

- POTCAR 文件内容示例：

```text
  PAW_PBE Cu 22Jun2005
   11.0000000000000
 parameters from PSCTR are:
   VRHFIN =Cu: d10 p1
   LEXCH  = PE
   EATOM  =  1390.9808 eV,  102.2342 Ry

   TITEL  = PAW_PBE Cu 22Jun2005
   LULTRA =        F    use ultrasoft PP ?
   IUNSCR =        1    unscreen: 0-lin 1-nonlin 2-no
   RPACOR =    2.000    partial core radius
   POMASS =   63.546; ZVAL   =   11.000    mass and valenz
   RCORE  =    2.300    outmost cutoff radius
   RWIGS  =    2.200; RWIGS  =    1.164    wigner-seitz radius (au A)
   ENMAX  =  295.446; ENMIN  =  221.585 eV
   ICORE  =        3    local potential
   LCOR   =        T    correct aug charges
   LPAW   =        T    paw PP
   EAUG   =  586.980
   DEXC   =    0.000
   RMAX   =    2.344    core radius for proj-oper
   RAUG   =    1.300    factor for augmentation sphere
   RDEP   =    2.302    radius for radial grids
   RDEPT  =    1.771    core radius for aug-charge

   Atomic configuration
    9 entries
     n  l   j            E        occ.
     1  0  0.50     -8850.2468   2.0000
     2  0  0.50     -1062.3498   2.0000
     2  1  1.50      -916.8226   6.0000
     3  0  0.50      -114.6929   2.0000
     3  1  1.50       -72.1325   6.0000
     3  2  2.50        -5.0394  10.0000
     4  0  0.50        -4.6097   1.0000
     4  1  0.50        -4.0817   0.0000
     4  3  2.50        -1.3606   0.0000
   Description
     l       E           TYP  RCUT    TYP  RCUT
     2     -5.0393973     23  2.200
     2     10.8846608     23  2.200
     0     -4.6097109     23  2.200
     0      8.2520465     23  2.200
     1     -2.7211652     23  2.200
     1     21.7055443     23  2.200
     3      2.7211652     23  2.300
   Error from kinetic energy argument (eV)
   NDATA  =      100
   STEP   =   20.000   1.050
  127.      125.      125.      123.      123.      121.      119.      118.
  116.      114.      113.      111.      109.      106.      104.      101.
  98.2      95.5      92.6      88.3      85.3      82.3      77.8      74.7
  71.6      67.1      62.5      59.5      55.1      50.8      46.6      42.6
  38.7      35.0      31.5      28.2      24.2      21.4      18.0      15.7
  12.9      10.5      8.46      6.71      5.25      4.04      3.05      2.10
  1.52     0.979     0.608     0.404     0.234     0.133     0.701E-01 0.473E-01
 0.388E-01 0.367E-01 0.365E-01 0.348E-01 0.310E-01 0.255E-01 0.195E-01 0.132E-01
 0.902E-02 0.584E-02 0.423E-02 0.368E-02 0.359E-02 0.353E-02 0.322E-02 0.265E-02
 0.198E-02 0.138E-02 0.933E-03 0.749E-03 0.697E-03 0.691E-03 0.639E-03 0.533E-03
 0.389E-03 0.272E-03 0.210E-03 0.193E-03 0.190E-03 0.172E-03 0.136E-03 0.960E-04
 0.728E-04 0.670E-04 0.655E-04 0.579E-04 0.427E-04 0.316E-04 0.274E-04 0.269E-04
 0.235E-04 0.179E-04 0.134E-04 0.125E-04
END of PSCTR-controll parameters
```



---

## KPOINTS

- 设置布里渊区 K 点网格采样大小或计算能带结构时沿高对称方向的 K 点

- 对 K 点进行收敛性测试是许多电子最小化计算的基本任务之一

- 常规 K 点网格
    - 第 1 行：注释行
    - 第 2 行：设置 K 点数目，0 表示 k 点网格自动生成
    - 第 3 行：K 点网格划分方式（Monkhorst-Pack 和 Gamma 方法）
    - 第 4 行：3 个方向上具体的网格划分数目
    - 第 5 行：格

```text
Regular k-point mesh
0              ! 0 -> determine number of k points automatically
Gamma          ! generate a Gamma centered mesh
4  4  4        ! subdivisions N_1, N_2 and N_3 along the reciprocal lattice vectors
0  0  0        ! optional shift of the mesh (s_1, s_2, s_3)
```

- 注意事项：
    - Monkhorst-Pack 网格的收敛速度可能快于 Γ- 中心网格；同时需注意避免使用 Monkhorst-Pack 网格破坏对称性。
    - 对于 HCP 结构，采用 Gamma 方法

- 能带计算：当性质依赖于 K 矢量时，通常沿高对称性路径将性质可视化；线模式（line mode）表示在布里渊区用户定义的点之间生成 K 点，最常用的情况是分析能带结构
    - 第 1 行：注释行
    - 第 2 行：设置 K 点数目，非 0 数字表示每条线之间划分的 K 点数目
    - 第 3 行：生成 K 点方式

```text
k points along high symmetry lines
 40              ! number of points per line
line mode
fractional
  0    0    0    Γ
  0.5  0.5  0    X

  0.5  0.5  0    X
  0.5  0.75 0.25 W

  0.5  0.75 0.25 W
  0    0    0    Γ
```



---

## INCAR

- 核心输入文件：用于指定 VASP 计算的参数、算法和设置

- INCAR 准备的原则：**越简单越好，不知道的，不理解的就不往里面放**

- INCAR 参数类型
    - 通用参数：SYSTEM、PREC、ISTART、ICHARG
    - 电子优化相关参数：ALGO、ENLM、NELMIN、ENCUT、EDIFF
    - 离子优化相关参数：IBRION、POTIM、NSW、EDIFFG
    - 态密度积分相关参数：ISMEAR、SIGMA、LORBIT
    - 态密度相关参数：EMIN 、EMAX、NEDOS

- 注意事项：
    - 等号（=）前后可以有空格，也可以没有
    - 不要使用 Tab，用空格替换 Tab
    - INCAR 中的参数中的 L 开头表示逻辑数
    - INCAR 参数名称写错，VASP 会忽略，不影响
    - 参数设置的第一个数值为默认值，忽略后续同参数的数值设置


---

### SYSTEM

- title string，对体系及要执行的计算进行注释说明

- 默认值：unknown system

- 可随便写；该参数可有可没有


---

### ISTART

- 初始化轨道；确定是否读取 WAVECAR 文件

- 默认值：1（若 WAVECAR 文件存在）否则 0


---

### ICHARG

- 决定 VASP 如何构造初始电荷密度；其积分值为电子数

- 默认值：ISTART=0，则 ICHARG=2；否则 ICHARG=0

```bash
0              # 从初始波函数计算电荷密度
1              # 从 CHGCAR 文件读取
2              # 若 ISTART=0，取原子电荷密度的叠加
+10            # 非自洽计算（在整个电子最小化过程中电荷密度保持不变）
11             # 从 CHGCAR 文件获取（能带绘制用）本征值或给定的电荷密度的态密度（DOS）
```


---

### ALGO

- 确定电子最小化算法，或选择 GW 计算类型

- 默认值：Normal

```bash
Normal         # blocked-Davidson 算法
Fast           # 混合算法，初始几步采用 blocked-Davidson(DAV) 算法，之后采用 RMM-DIIS(RMM) 算法
Damped         # damped velocity friction 算法
```


---

### LREAL

- 决定投影算子是在实空间还是在倒空间求值

- 默认值：.FALSE.

```bash
.FALSE.        # 倒空间
.TRUE.
AUTO
```


---

### LCHARG

- 决定电荷密度是否写入 CHGCAR 和 CHG 文件中

- 默认值：.TRUE.


---

### LWAVE

- 决定运行结束后波函数是否写入 WAVECAR 文件中

- 默认值：.TRUE.


---

### ENCUT

- 平面波截断能；收敛性测试指标之一；默认值为 POTCAR 文件中最大的 ENMAX 值


---

### PREC

- 计算精度；设置截断能、FFT grids 和 the projectors in real space ROPT 的精度的默认值

- 默认值：Normal；推荐使用 Normal 或 Accurate

```bash
Normal         # 适用于大多数常规计算
Accurate       # 适用于高精度（如精确的力、声子、应力张量，或需要计算二阶导）
High           # High Medium Low 为弃用值
```


---

### ISMEAR

- 轨道分数占据的展宽（平滑处理）方法

```bash
N              # N 为数字；Methfessel-Paxton order N（默认 1）
0              # Gaussian
-1             # Fermi
-4             # tetrahedron
-5             # Blöchl 纠正的 tetrahedron
```

- 注意事项：
    - DOS 和非常精确的总能计算（金属的非弛豫），使用 ISEMAR=-5
    - 对于金属弛豫，使用 ISMEAR=1 或 ISMEAR=2 以及合适的 SIGMA 值（熵项小于 1meV/atom），合理值通常为 SIGMA=0.2（默认）
    - 对于半导体或绝缘体，使用 ISEMAR=-5，胞太大或只使用 1-2 个 k 点，使用 ISMEAR=0 以及 SIGMA=0.03-0.05
    - Tetrahedron method 需 K 点数目大于等于 4

>tetrahedron 方法，忽略 SIGMA 参数

```bash
 VERY BAD NEWS! internal error in subroutine IBZKPT:
 Tetrahedron method fails for NKPT<4. NKPT =       1
```


---

### SIGMA

- 展宽宽度（单位：eV）

- 默认值：0.2

- 对于金属，默认 0.2，但通常 0.05 就能满足要求


---

### NSW

- 最大离子步步数

- 默认值：0

- IBRION=0 时，必须提供 NSW 数值（AIMD 步数）
- 每个离子步会计算 Hellmann-Feynman 力和应力


---

### IBRION

- 决定离子如何更新和移动

- 默认值：-1（NSW=-1 或 0）；0（其他情况，执行 AIMD）

- 除 0 外，其他算法都最终弛豫到局部能量最小值

- IBRION 选择
    - 弛豫较困难时，推荐使用 IBRION=2
    - 在从非常糟糕的初始猜测值开始的情况下，IBRION=3 通常有用
    - 接近能量局部最小值，推荐使用 IBRION=1

```bash
-1             # 不更新；离子不移动
0              # 分子动力学 AIMD

# 结构优化
1              # RMM-DIIS / quasi-Newton 算法
2              # conjugate gradient algorithm 共轭梯度算法
3              # Damped molecular dynamics 算法

# 计算声子模式；计算二阶导数、海森矩阵和声子频率
5 6            # 有限差分（finite differences）；5 without symmetry, 6 with symmetry
7 8            # 密度泛函扰动理论（density functional perturbation theory, DFPT）；7 without symmetry, 8 with symmetry
```


---

### POTIM

- 离子弛豫步宽或 AIMD 步长


---

### ISIF

- 决定在弛豫及分子动力学运行中胞的体积、形状或原子位置是否发生改变以及应力张量是否计算

- 默认值：0：IBRION=0 时；2：其他情况

- 应力张量计算相对耗时，因此在 AIMD 中将其关掉；力总是会进行计算

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152120807.png)


---

### EDIFF

- 电子步收敛条件



---

### EDIFFG

- 离子步收敛条件


---

### NELM

- 每个离子步中的最大电子步步数

- 默认值：60


---

### NELMIN

- 每个离子步中的最小电子步步数

- 默认值：2；推荐值设置在 4-8 之间


---

### LORBIT

- 和适当的 RWIGS 一起，决定 PROCAR 或 PROOUT 文件是否被写入。LORBIT>=10 时，不需要 RWIGS 标签

- 默认值：None

![LORBIT-tag.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307151730319.png)


---

### ADDGRID

- 添加网格；有助于降低力噪声

- 默认值：.FALSE.


---

### SYMPREC

- 决定 POSCAR 文件中的位置精度

- 默认值：$10^{-5}$


---

### ISYM

- 决定 VASP 处理对称性的方式


- 默认值：1：若 VASP 用 USPPs 运行；3：若 `LHFCALC=.TRUE.`；2：其他情况
- 1 | 2 | 3：对称性打开；-1 | 0：对称性关闭；
- 与 ISYM=1 相比，ISYM=2 采用了更高效、更节省内存的电荷密度对称化方法。这尤其降低了并行版本的内存需求。
- 对于 ISYM=3，VASP 并不直接对称电荷密度。相反，电荷密度是通过对布里渊区不可还原部分 k 点处的轨道进行相关对称运算来构建的。当 LHFCALC=.TRUE 时使用这种对称方法。
- 当 ISYM=0 时，VASP 不使用对称性，但会假定 Ψk=Ψ*-k 并相应减少布里渊区的采样。这个值应该为分子动力学设置，即 IBRION=0。
- 当 ISYM=-1 时，对称性被完全关闭。



- 为什么需要对称：在 LDA 中，超胞和电荷密度的对称性总是相同的。由于在计算中使用了一组不可约对称性的 k 点，因此这种对称性被打破。为了储存正确的电荷密度和力，有必要对称这些量。
- 如果打开对称运算，则 NWRITE=3 将对称运算写入 OUTCAR 文件。


---

### ISPIN

- 是否考虑自旋极化

```bash
1              # 不考虑
2              # 考虑
```


---

### MAGMOM

- 设置磁矩


---

### NWRITE

- 决定往 OUTCAR 文件中写入多少内容

- 默认值：2；可选值：0-4

- 长时间的 MD 运行，建议 NWRITE 设置为 0 或 1；短时间运行设置为 2

```bash
3      # 写入的内容最详细
4      # 只用于 debugging
```

- f+l 表示第一步和最后一步离子步， f 表示第个离子步，i 表示每个离子步，e 表示每个电子步，X 表示适用时（when applicable）

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307162218175.png)


---

### EMIN 、EMAX

- DOS 能量的上下范围


---

### NEDOS

- DOS 和介电函数的网格点数目

- 默认值：301


---

- LAECHG = True

    - 含义：用于控制是否计算电荷密度差异。
    - 值：True 表示计算电荷密度差异。
- LASPH = True

    - 含义：用于控制是否考虑 LDA+U 方法中的自相互作用。
    - 值：True 表示考虑自相互作用。

- LVHAR = True

    - 含义：用于控制是否计算原子的局部势能。
    - 值：True 表示计算局部势能。

- KPAR = 8

    - 含义：用于并行计算中控制 k 点并行的数量。
    - 值：8 表示使用 8 个处理器进行 k 点并行计算。

- NPAR = 4

    - 含义：用于控制并行计算中的分区数量。
    - 值：4 表示将计算任务分成 4 个部分进行并行计算。


>[13\_vasp/V2PC/README.md at main · Yiwei666/13\_vasp · GitHub](https://github.com/Yiwei666/13_vasp/blob/main/V2PC/README.md)


其他

```bash
GGA = PE
```
