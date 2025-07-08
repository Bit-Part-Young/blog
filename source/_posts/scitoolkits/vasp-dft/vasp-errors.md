---
title: VASP 报错
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: VASP 报错
description: VASP 报错
tags:
  - VASP
categories:
  - 科研工具
  - VASP
date: 2025-06-07 14:00:00
abbrlink: 206050
password:
---

# VASP 报错

- [【VASP报错集锦 1】](https://zhuanlan.zhihu.com/p/536705200)

- forrtl 报错：[forrtl: severe (174): SIGSEGV, segmentation fault occurred - My Community](https://www.vasp.at/forum/viewtopic.php?t=17257)

```bash
# 在 脚本/终端 中添加命令
ulimit -s unlimited
```

- SYMPREC 报错：
    - 解决方法：在 INCAR 中添加 `ISYM=0`
    - [POSMAP internal error: symmetry equivalent atom not found ... - 知乎](https://zhuanlan.zhihu.com/p/611339883)
    - [用vaspkit中应变能量法计算弹性模量，出现对称度的问题，SYMPREC从-3调整到-9都不行 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-25280-1-1.html)

```bash
# ~/yangsl/work/Ti-Al-Nb-Zr-V-Mo-MLIP/GSFE/Nb-GSFE-123/6
# ISYM=0
POSMAP internal error: symmetry equivalent atom not found,
  you might try decreasing or increasing SYMPREC by an order of magnitude.


# ~/yangsl/work/Ti-Al-Nb-Zr-V-Mo-MLIP/GSFE/V-GSFE/3-123/6
# ISYM=0
VERY BAD NEWS! internal error in subroutine PRICEL (probably precision problem, try to change SYMPREC in INCAR ?):
Sorry, number of cells and number of vectors did not agree.       3
```

- EDDDAV 报错：
    - [VASP报错 Error EDDDAV: Call to ZHEGV failed. Returncode = 25 2 48 - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/forum.php?mod=viewthread&tid=508)
    - 检查在第几步离子步时报错以及原子受力大小

```bash
# ~/work/Ti-Al-Nb-Zr-V-Mo-MLIP/sia/Mo-sia/1-O
# 第一个离子步结束后就报错，部分原子受力过大，尝试减小 POTIM（默认 0.5）
# POTIM=0.2/0.1，未报错
Error EDDDAV: Call to ZHEGV failed. Returncode =  11 2  16
```

- EDDRMM 警告：可不用管

```bash
# 在电子步中，有时会出现该 warning，code 对应的数字会有不同，影响是否大
# 如何解决该问题（无统一的解决方法）
WARNING in EDDRMM: call to ZHEGV failed, returncode =   6  3      3
```

- LAPACK 报错：[请求赐教，VASP计算中报错LAPACK:Routine ZPOTRF failed!是什么原因导致的呀？ - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-23398-1-1.html)

```bash
# 一开始就报错，添加 ISYM=0 可解决
LAPACK: Routine ZPOTRF failed!           5           1           1
LAPACK: Routine ZPOTRF failed!
LAPACK: Routine ZPOTRF failed!          27           1           1
```

- BRMIX 报错（体系较大、电子数很多时有时候会出现）：[VASP error - BRMIX very serious problems the old and the new charge density differ 报错解决方案 - Steven's Blog](https://tpmk.github.io/2022/01/29/VASP-error-BRMIX-very-serious-problems-the-old-and-the-new-charge-density-differ/)

```bash
BRMIX: very serious problems the old and the new charge density differ

# 解决方法
# 方式 1：在 INCAR 中添加
LSCALAPACK = .FALSE.

# 方式 2：在提交脚本中添加
export I_MPI_ADJUST_REDUCE=3
```

- Sub-Space-Matrix 报错
    - [VASP能带计算Sub-Space-Matrix is not hermitian in DAV - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-34266-1-1.html)
    - [如何解决sub space Matrix is not hermitian in DAV 报错？ - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-39103-1-1.html)

```bash
# 在服务器 node 节点上 层错构型计算 出现该报错
WARNING: Sub-Space-Matrix is not hermitian in DAV

# 解决方法
# 方式 1：在 INCAR 中添加
KPAR = 2
```

- Reciprocal lattice and k-lattice 报错（可忽略）：[求助：静态/非自洽计算时出现VERY BAD NEWS - 第一性原理 (First Principle) - 计算化学公社](http://bbs.keinsci.com/thread-41732-1-1.html)

```bash
VERY BAD NEWS! internal error in subroutine IBZKPT:
Reciprocal lattice and k-lattice belong to different class of lattices. Often results are still useful...      48
```

- 离子步中出现 ZBRENT 信息（可忽略？）

```bash
# 没有标注 error 也没有标注 warning，计算最后是收敛
ZBRENT: interpolating
ZBRENT: can not locate minimum, use default step
ZBRENT: increasing intervall
ZBRENT: bracketing found
ZBRENT: interpolating

# ~/work/Ti-Al-Nb-Zr-V-Mo-MLIP/GSFE/Mo-GSFE-112/4
# 拷贝 CONTCAR 为 POSCAR 续算，无报错
ZBRENT: fatal error in bracketing
    please rerun with smaller EDIFF, or copy CONTCAR
    to POSCAR and continue
```
