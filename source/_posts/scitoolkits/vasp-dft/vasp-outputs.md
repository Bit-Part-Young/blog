---
title: VASP 输出文件
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: VASP 输出文件
description: VASP 输出文件
tags:
  - VASP
categories:
  - 科研工具
  - VASP
date: 2024-10-14 11:04:30
abbrlink: 410503
password:
---

# VASP 输出文件

- 输出文件结构示例

```bash
.
├── CHG
├── CHGCAR
├── CONTCAR
├── DOSCAR
├── EIGENVAL
├── IBZKPT
├── INCAR
├── KPOINTS
├── LOCPOT
├── OSZICAR
├── OUTCAR
├── PCDAT
├── POSCAR
├── POTCAR
├── PROCAR
├── REPORT
├── vasprun.xml
├── WAVECAR
└── XDATCAR
```



---

## OUTCAR

- 参考：[VASP学习记录(六)：VASP的输出文件OUTCAR](https://zhuanlan.zhihu.com/p/579705300)

- 给出 VASP 计算过程的具体输出，包括：
    - 输入参数的总结
    - 电子步、KS 本征值信息
    - 应力张量
    - 原子受力
    - 局域电荷和磁矩
    - 介电性质

- 可通过修改 INCAR 中的 NWRITE 参数来选择写入 OUTCAR 文件的输出信息量

- 基本信息（构型、INCAR 参数等）提取

```bash
# 元素符号
grep 'TITEL' OUTCAR  | awk '{print $4}' | awk -F'_' '{print $1}' | awk '!seen[$0]++'

# 元素对应数目
grep 'ions per type' OUTCAR  | tail -n 1 | awk -F'=' '{print $2}'

# 构型原子数
# 方式 1
natoms=$(grep 'NIONS' OUTCAR | tail -n 1 | awk '{print $12}')
# 方式 2
natoms=$(sed -n '7p' POSCAR | awk '{ for(i=1; i<=NF; i++) a+=$i; print a}')

# 平均原子体积
vol=$(grep 'volume of cell' OUTCAR | tail -n 1 | awk -v n=${natoms} '{print $5/n}')


grep 'NSW' OUTCAR                     # 查看 INCAR 相关参数数值
grep 'generate k-points' OUTCAR       # 查看由 KSAPCING 参数生成的 K 点数目
grep 'irreducible k-points' OUTCAR    # 查看不可约 K 点数目
grep 'NKPTS' OUTCAR                   # 查看不可约 K 点数目、能带数
grep 'distr' OUTCAR                   # 查看 KPAR、NPAR、NCORE 参数
```

- 能量信息提取

```bash
# 能量之间的差异
F = E + PV - TS                       # 总能；自由能公式；T=0 时，F=U
free energy TOTEN                     # 自由能
energy without entropy                # 不含 T*S 熵项的自由能
E0                                    # sigma->0 时的能量

# 电子步能量
# 'energy without' 'free energy' 之间只有一个空格
grep 'free energy' OUTCAR
grep  'energy without entropy' OUTCAR

# 离子步能量
# 'energy  without' 或 'free  energy' 之间有两个空格
grep 'free  energy' OUTCAR
grep  'energy  without entropy' OUTCAR

energy=$(grep 'E0' OSZICAR | tail -n 1 | awk '{print $5}')

# 平均原子能量
eng=$(grep 'free  energy' OUTCAR | tail -n 1 | awk -v n=${natoms} '{print $5/n}')
```

- 原子受力提取
    - total drift：每个离子步中，所有原子对应 x y z 方向的受力之和；有数值噪声，会产生误差；若误差值大于设定的 EDIFFG 值，则说明所谓的力收敛是不正确的
    - `TOTAL-FORCE` table 中输出的力是已修正过的（x y z 方向的受力之和为 0）

```bash
# 获取每个离子步的原子位置及对应受力
awk '/TOTAL-FORCE/,/total drift/' OUTCAR

# 获取第 N 个离子步的原子位置及对应受力
awk '/TOTAL-FORCE/ {flag++} flag==N {print} /total drift/ {if (flag==N) {exit}}' N=1 OUTCAR

# 每个离子步的原子受力
n=48
lines=$(awk '{i=0}/TOTAL-FORCE/{getline; while(i<n) {getline; print $4,$5,$6; i++} i=0}' n=$n < OUTCAR)
echo $lines


# total drift 不为 0 的一些示例
# HCP Ti 基态结构 静态计算
POSITION                                       TOTAL-FORCE (eV/Angst)
-----------------------------------------------------------------------------------
     0.00000      0.00000      0.00000        -0.000000      0.000000      0.000000
     1.46785      0.84746      2.32309         0.000000      0.000000      0.000000
-----------------------------------------------------------------------------------
   total drift:                               -0.002829      0.001634      0.000000


# HCP 正交 Ti 基态结构 静态计算
POSITION                                       TOTAL-FORCE (eV/Angst)
-----------------------------------------------------------------------------------
     0.00000      0.00000      0.00000         0.000000     -0.002278     -0.000000
     1.46785      2.54239      0.00000         0.000000     -0.002278     -0.000000
     1.46785      0.84746      2.32309        -0.000000      0.002278     -0.000000
     0.00000      3.38986      2.32309        -0.000000      0.002278      0.000000
-----------------------------------------------------------------------------------
   total drift:                               -0.005658     -0.000032      0.000002
```

- 其他

```bash
# 结构优化/弛豫结束标志
reached required accuracy - stopping structural energy minimisation

# 磁矩 需设置 ISPIN=2
mag=$(grep 'mag=' OSZICAR | awk '{print $10}')

# 耗时
sec=$(grep 'Total CPU time used' OUTCAR | awk '{print $6}')

# 查看每个离子步的耗时
grep -iE 'loop\+' OUTCAR

# 由 KPOINTS 生成的 K 点总数（仅示例）
head -n 38 IBZKPT | tail -n 35 | awk '{sum+=$4} END {print sum}'

# 不可约布里渊区 K 点数
grep 'irreducible k-points' OUTCAR
# 输出内容示例
 Found     35 irreducible k-points:

# 能带数
grep -i 'nbands' OUTCAR
# 输出内容示例；也可得到不可约布里渊区 K 点数
k-points           NKPTS =     35   k-points in BZ     NKDIM =     35   number of bands    NBANDS=      9
```

- OUTCAR 示例内容：[13\_vasp/V2PC/02\_static\_calculation\_output.md at main · Yiwei666/13\_vasp · GitHub](https://github.com/Yiwei666/13_vasp/blob/main/V2PC/02_static_calculation_output.md)

```bash
 vasp.5.4.4.18Apr17-6-g9f103f2a35 (build Nov 17 2020 17:54:46) complex

 executed on             LinuxIFC date 2023.09.26  17:09:42
 running on   64 total cores
 distrk:  each k-point on    8 cores,    8 groups
 distr:  one band on NCORES_PER_BAND=   2 cores,    4 groups


--------------------------------------------------------------------------------------------------------


--------------------------------------- Iteration      1(  14)  ---------------------------------------


    POTLOK:  cpu time    0.0515: real time    0.0635
    SETDIJ:  cpu time    0.4765: real time    0.4766
     EDDAV:  cpu time    0.2827: real time    0.2836
 BZINTS: Fermi energy:  8.683970; 38.000000 electrons
         Band energy: 134.423518;  BLOECHL correction: -0.108454
       DOS:  cpu time    0.0149: real time    0.0149
    --------------------------------------------
      LOOP:  cpu time    0.8256: real time    0.8387

 eigenvalue-minimisations  :  3224
 total energy-change (2. order) :-0.3970183E-05  (-0.5334378E-05)
 number of electron      37.9999994 magnetization       0.0001839
 augmentation part        6.3731527 magnetization       0.0002006

 Free energy of the ion-electron system (eV)
  ---------------------------------------------------
  alpha Z        PSCENC =       140.25282115
  Ewald energy   TEWEN  =     -1636.51123608
  -Hartree energ DENC   =      -101.91636345
  -exchange      EXHF   =         0.00000000
  -V(xc)+E(xc)   XCENC  =      -146.59065512
  PAW double counting   =      3226.49321421    -3016.41118853
  entropy T*S    EENTRO =         0.00000000
  eigenvalues    EBANDS =       134.42351831
  atomic energy  EATOM  =      1329.85235582
  Solvation  Ediel_sol  =         0.00000000
  ---------------------------------------------------
  free energy    TOTEN  =       -70.40753370 eV

  energy without entropy =      -70.40753370  energy(sigma->0) =      -70.40753370


--------------------------------------------------------------------------------------------------------


  FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)
  ---------------------------------------------------
  free  energy   TOTEN  =       -70.40753370 eV

  energy  without entropy=      -70.40753370  energy(sigma->0) =      -70.40753370



--------------------------------------------------------------------------------------------------------


    POTLOK:  cpu time    0.5294: real time    0.5295


--------------------------------------------------------------------------------------------------------


 stress matrix after NEB project (eV)
     -0.50749     -0.00000     -0.00000
      0.00000     -0.50749      0.00000
      0.00000      0.00000     -0.67546
  FORCES: max atom, RMS     0.042143    0.029800
  FORCE total and by dimension    0.084286    0.042143
  Stress total and by dimension    0.985565    0.675456
     LOOP+:  cpu time   12.0820: real time   12.2709
    4ORBIT:  cpu time    0.0000: real time    0.0000



 total charge

# of ion       s       p       d       tot
------------------------------------------
    1        0.480   0.854   3.763   5.097
    2        0.480   0.854   3.795   5.129
    3        0.480   0.854   3.794   5.128
    4        0.480   0.854   3.765   5.099
    5        1.041   1.504   0.000   2.545
    6        1.038   1.505   0.000   2.543
    7        0.891   1.513   0.000   2.405
    8        0.891   1.513   0.000   2.404
--------------------------------------------------
tot          5.782   9.452  15.117  30.351



 magnetization (x)

# of ion       s       p       d       tot
------------------------------------------
    1       -0.000   0.000   0.000   0.000
    2        0.000  -0.000  -0.000  -0.000
    3       -0.000   0.000   0.000   0.000
    4        0.000   0.000  -0.000  -0.000
    5        0.000   0.000   0.000   0.000
    6        0.000  -0.000   0.000  -0.000
    7       -0.000  -0.000   0.000  -0.000
    8       -0.000   0.000   0.000   0.000
--------------------------------------------------
tot          0.000   0.000   0.000   0.000

 BZINTS: Fermi energy:  8.683970; 38.000000 electrons
         Band energy: 134.423518;  BLOECHL correction: -0.108454

 total amount of memory used by VASP MPI-rank0    49266. kBytes
=======================================================================

   base      :      30000. kBytes
   nonlr-proj:       4721. kBytes
   fftplans  :       2354. kBytes
   grid      :       6243. kBytes
   one-center:        124. kBytes
   wavefun   :       5824. kBytes



 General timing and accounting informations for this job:
 ========================================================

                  Total CPU time used (sec):       16.449
                            User time (sec):       14.631
                          System time (sec):        1.818
                         Elapsed time (sec):       16.883

                   Maximum memory used (kb):       85376.
                   Average memory used (kb):           0.

                          Minor page faults:        29744
                          Major page faults:            6
                 Voluntary context switches:         2545
```



---

## vasprun.xml

- xml 格式的输出文件（内容和 OUTCAR 文件类似）



---

## OSZICAR

- 电子步和离子步迭代的具体信息

```bash
N          # 电子结构的迭代步数，通常被称为电子步
E          # 当前电子步的体系能量（自由能）
dE         # 当前电子步和上一步体系能量的差值
d eps      # 能带结构能量的变化
ncg        # 作用于波函数的哈密顿量的求值次数
rms        # 尝试波函数（trial wavefunction）的残差的范数（即它们的近似误差）
rms(c)     # 输入输出电荷密度之差（前几步电荷密度不参与迭代）
```

- 开启自旋计算，每个离子步后会有磁矩信息（`mag=`）

- 文件内容示例

```text
       N       E                     dE             d eps       ncg     rms          rms(c)
DAV:   1     0.262963906782E+03    0.26296E+03   -0.13606E+04  2304   0.140E+03
DAV:   2    -0.147719592593E+02   -0.27774E+03   -0.26887E+03  2384   0.300E+02
DAV:   3    -0.805108877868E+02   -0.65739E+02   -0.64315E+02  3744   0.132E+02
DAV:   4    -0.839490730879E+02   -0.34382E+01   -0.34294E+01  3104   0.324E+01
DAV:   5    -0.840274618995E+02   -0.78389E-01   -0.78495E-01  3160   0.523E+00    0.415E+01
DAV:   6    -0.681149709824E+02    0.15912E+02   -0.12273E+02  3448   0.642E+01    0.127E+01
DAV:   7    -0.678322667781E+02    0.28270E+00   -0.13214E+01  3464   0.237E+01    0.918E+00
DAV:   8    -0.676127626457E+02    0.21950E+00   -0.14812E+00  3504   0.791E+00    0.140E+00
DAV:   9    -0.675766178893E+02    0.36145E-01   -0.17189E-01  3304   0.256E+00    0.398E-01
DAV:  10    -0.675781648484E+02   -0.15470E-02   -0.81316E-02  3208   0.128E+00    0.288E-01
DAV:  11    -0.675770209933E+02    0.11439E-02   -0.89472E-03  3248   0.587E-01    0.204E-01
DAV:  12    -0.675771006993E+02   -0.79706E-04   -0.23153E-03  3088   0.236E-01    0.725E-02
DAV:  13    -0.675771007310E+02   -0.31732E-07   -0.91291E-05  2928   0.667E-02
   1 F= -.67577101E+02 E0= -.67577101E+02  d E =0.000000E+00  mag=    -0.0000
```


---

## CONTCAR

- VASP 计算结束后的构型文件

- CONTCAR 中的 CONT 是继续的意思

- VASP OUTCAR 中晶格常数精度是 10 位有效数字，CONTCAR 中是 16 位有效数字



---

## PROCAR

- 对于静态计算，PROCAR 文件包含每个轨道的 spd 和位点投影波函数特征。在 VASP 中实现了多种确定投影波函数特征的方案，通常由标签 LORBIT 和 RWIGS 控制。当 LORBIT<10 时，必须在 INCAR 文件中指定 RWIGS 标签，在这种情况下，轨道将被投影到由 RWIGS 确定区域内的非零球谐波上。 当 LORBIT>=10 时，不需要 RWIGS 标签，投影将被投影到投影函数上

- LORBIT=11 时的格式

```text
# of k-points:    5         # of bands:   26         # of ions:    3

k-point     1 :    0.00000000 0.00000000 0.00000000     weight = 0.06250000

band     1 # energy  -17.37867948 # occ.  1.00000000

ion      s     py     pz     px    dxy    dyz    dz2    dxz  x2-y2    tot
    1  0.144  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.145
    2  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
    3  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
tot    0.727  0.000  0.013  0.000  0.000  0.000  0.000  0.000  0.000  0.740
```



---

## CHG、CHGCAR

- 体系的电荷密度文件，两者内容基本相同；后者文件内容还包含 PAW one-center occupancies（前者数据精度略低于后者），可用于重启 VASP 计算；前者主要用于可视化和后处理

- 这两个文件在每步迭代过程中都会被更新（设置 ICHARG=11 或 12 除外）

- CHGCAR 文件内容：结构、电荷密度、augmentation occupancies



---

## DOSCAR、EIGENVAL

- 参考：
    - [VASP输出文件内容结构解析(未完成) - Yu-Xuan Blog](https://yxli8023.github.io/2021/08/08/vasp-EIGENVAL.html)
    - [如何分析态密度](https://zhuanlan.zhihu.com/p/671748151)

- DOSCAR：含态密度以及积分态密度

- 前 6 行是 header；第 6 行前两个数据表示能量范围，第三个数据表示带数，它与 `INCAR` 中 `NEDOS` 参数值是相同的，第四个表示费米能

```text
Number of Ions (including empty spheres), Number of Ions, 0 (no partial DOS) or 1 (incl. partial DOS), NCDIJ (currently not used)
Volume of the unit cell [Angst**3], length of the basis vectors (a,b,c [m]), POTIM[s]
the initial Temperature TEBEG
'CAR'
the name of the system as given by SYSTEM in INCAR
E(max), E(min), (the energy range in which the DOS is given), NEDOS,  E(fermi), 1.0000
```

- 从第 7 行开始（到第 `6+NEDOS` 行），每列的含义如下

```bash
# 不开启自旋
energy     DOS     integrated DOS
# 开启自旋
energy     DOS(up) DOS(dwn)  integrated DOS(up) integrated DOS(dwn)
```

- EIGENVAL：每个 K 点的 Kohn-Sham 本征值

- 对于弛豫，DOSCAR 通常没用

- 该两个文件中的能量值都是绝对的，不是以费米能级作为参考零点



---

## XDATCAR

- 含每个离子步的构型（轨迹文件；AIMD 常用）



---

## PCDAT

- 对于 AIMD，写入平均对关联函数（pair correlation function）

- 每行内容的描述
    - 第 1 行：1（固定输出），原子数，1（固定输出），0（固定输出），平均原子体积，温度
    - 第 2 行：CAR（固定输出）
    - 第 3 行：INCAR 文件 Header
    - 第 4 行：0，0，0（全为固定输出）
    - 第 5 行：1（固定输出），NBLOCK
    - 第 6 行：NPACO，NPACO，NPACO
    - 第 7 行：NPACO
    - 第 8 行：0.1\*10\^-9（固定输出）
    - 第 9 行：APACO\*10\^-9/NPACO
    - 第 10 行：NSW/NBLOCK/KBLOCK
    - 第 11 行：POTIM\*10\^-9，norm of lattice vector 1\*10\^-10，norm of lattice vector 2\*10\^-10，norm of lattice vector 3\*10\^-10
    - 第 12 行（第 12 行 - 12+NPACO）：输入平均温度/(NBLOCK\*KBLOCK)，实际平均温度
    - 接下来的 NPACO 行显示每个 speceis combination 的 PCF


---

## IBZKPT

- 含不可约布里渊区 K 点数目、坐标及权重

- 与 KPOINTS 文件兼容，若在 KPOINTS 文件中选择了自动生成 K 点网格，则会生成 IBZKPT 文件

- 生成的 N1 \* N2 \* N3 对应为 IBZKPT 对应 Reciprocal lattice 行后面的第 4 列数据加和

```bash
awk '/Reciprocal/,/Tetrahedra/' IBZKPT | awk '{sum += $4} END {print sum}'
```

- 示例

```bash
Automatically generated mesh
      35
Reciprocal lattice
    0.00000000000000    0.00000000000000    0.00000000000000             1
    0.11111111111111    0.00000000000000    0.00000000000000             8
    0.22222222222222    0.00000000000000    0.00000000000000             8
    0.33333333333333    0.00000000000000    0.00000000000000             8
    0.44444444444444    0.00000000000000    0.00000000000000             8
    0.11111111111111    0.11111111111111    0.00000000000000             6
    0.22222222222222    0.11111111111111    0.00000000000000            24
    0.33333333333333    0.11111111111111    0.00000000000000            24
    0.44444444444444    0.11111111111111    0.00000000000000            24
   -0.44444444444444    0.11111111111111    0.00000000000000            24
   -0.33333333333333    0.11111111111111    0.00000000000000            24
   -0.22222222222222    0.11111111111111    0.00000000000000            24
   -0.11111111111111    0.11111111111111    0.00000000000000            12
    0.22222222222222    0.22222222222222    0.00000000000000             6
    0.33333333333333    0.22222222222222    0.00000000000000            24
    0.44444444444444    0.22222222222222    0.00000000000000            24
   -0.44444444444444    0.22222222222222    0.00000000000000            24
   -0.33333333333333    0.22222222222222    0.00000000000000            24
   -0.22222222222222    0.22222222222222    0.00000000000000            12
    0.33333333333333    0.33333333333333    0.00000000000000             6
    0.44444444444444    0.33333333333333    0.00000000000000            24
   -0.44444444444444    0.33333333333333    0.00000000000000            24
   -0.33333333333333    0.33333333333333    0.00000000000000            12
    0.44444444444444    0.44444444444444    0.00000000000000             6
   -0.44444444444444    0.44444444444444    0.00000000000000            12
    0.33333333333333    0.22222222222222    0.11111111111111            24
    0.44444444444444    0.22222222222222    0.11111111111111            48
   -0.44444444444444    0.22222222222222    0.11111111111111            48
    0.44444444444444    0.33333333333333    0.11111111111111            24
   -0.44444444444444    0.33333333333333    0.11111111111111            48
   -0.33333333333333    0.33333333333333    0.11111111111111            48
   -0.22222222222222    0.33333333333333    0.11111111111111            24
   -0.44444444444444    0.44444444444444    0.11111111111111            24
   -0.33333333333333    0.44444444444444    0.11111111111111            24
   -0.33333333333333    0.44444444444444    0.22222222222222            24
Tetrahedra     # 设置 ISMEAR=-5 才会出现
       115    0.00022862368541
        24         1         2         2         6
        48         2         6         7        13
...
```



---

## WAVECAR

波函数文件（包含波函数系数、特征值、费米权重等信息）



---

## PROCAR

对于静态计算，PROCAR 文件含 spd and site projected wave function character of each orbital，由 LORBIT 和 RWIGS 参数控制。LORBIT>=10 时，不需要 RWIGS 参数
