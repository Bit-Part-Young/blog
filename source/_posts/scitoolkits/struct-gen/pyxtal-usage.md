---
title: PyXtal 安装与使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: PyXtal 安装与使用
description: PyXtal 安装与使用
tags:
  - PyXtal
categories:
  - 科研工具
  - 结构建模
date: 2023-07-02 15:56:30
abbrlink: 56568
password:
---

# PyXtal 安装与使用

## 介绍

[PyXtal documentation](https://pyxtal.readthedocs.io/en/latest/)



---

## 安装

```bash
pip install pyxtal

# 开发版本
pip install -U git+https://github.com/qzhu2017/PyXtal.git@master
```



---

## 使用

以六方 γ-Nb5Si3 构型构建示例；六方γ-Nb5Si3 结构信息：

- $D8_8$，$Mn_5Si_3$ 原型，hP16；
- 空间群为 P63/mcm（193）；
- 晶格常数实验值为 a=b=7.58 Å，c=5.23 Å；
- 单胞 16 个原子；其中 Nb、Si 原子数量比为 10:6，有 3 种不同的原子位点，其中 NbI（4d(0.333, 0.667, 0.0)）与 NbII（6g(0.2473, 0.0, 0.25)）位点分别有 4、6 个原子，SiI（6g(0.6063, 0.0, 0.25)）位点有 6 个原子。


```python

```

---

输出：

```text
------Crystal from Build------
Dimension: 3
Composition: Nb10Nb10Si6
Group: P 63/m c m (193)
  7.5360,   7.5360,   5.2480,  90.0000,  90.0000, 120.0000, hexagonal
Wyckoff sites:
	Nb @ [ 0.3333  0.6667  0.0000], WP [4d] Site [322]
	Nb @ [ 0.2473  0.0000  0.2500], WP [6g] Site [mm2.]
	Si @ [ 0.6063  0.0000  0.2500], WP [6g] Site [mm2.]
---------------------------------------------------------------------------
Full Formula (Nb10 Si6)
Reduced Formula: Nb5Si3
abc   :   7.536000   7.536000   5.248000
angles:  90.000000  90.000000 120.000000
pbc   :       True       True       True
Sites (16)
  #  SP            a          b      c
---  ----  ---------  ---------  -----
  0  Nb     0.333333   0.666667  -0
  1  Nb     0.666667   0.333333   0.5
  2  Nb     0.666667   0.333333  -0
  3  Nb     0.333333   0.666667   0.5
  4  Nb     0.2473    -0          0.25
  5  Nb     0          0.2473     0.25
  6  Nb    -0.2473    -0.2473     0.25
  7  Nb    -0.2473     0          0.75
  8  Nb     0         -0.2473     0.75
  9  Nb     0.2473     0.2473     0.75
 10  Si     0.6063    -0          0.25
 11  Si     0          0.6063     0.25
 12  Si    -0.6063    -0.6063     0.25
 13  Si    -0.6063     0          0.75
 14  Si     0         -0.6063     0.75
 15  Si     0.6063     0.6063     0.75
---------------------------------------------------------------------------
Atoms(symbols='Si6Nb10', pbc=True, cell=[[6.526367442919531, -3.7679999999999976, 4.614469139187227e-16], [0.0, 7.536, 4.614469139187227e-16], [0.0, 0.0, 5.248]])
```
