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

- 结构建模工具

- [PyXtal documentation](https://pyxtal.readthedocs.io/en/latest/)



---

## 安装

```bash
pip install -U pyxtal

# 开发版本
pip install -U git+https://github.com/qzhu2017/PyXtal.git@master
```



---

## 使用

```bash
# 查看 0 维点群
pyxtal_symmetry.py -d 0  
```

- 以六方 γ-Nb5Si3 构型构建示例；六方 γ-Nb5Si3 结构信息：
    - $D8_8$，$Mn_5Si_3$ 原型，hP16；
    - 空间群为 P63/mcm（193）；
    - 晶格常数实验值为 a=b=7.58 Å，c=5.23 Å；
    - 单胞 16 个原子；其中 Nb、Si 原子数量比为 10:6，有 3 种不同的原子位点，其中 NbI（4d(0.333, 0.667, 0.0)）与 NbII（6g(0.2473, 0.0, 0.25)）位点分别有 4、6 个原子，SiI（6g(0.6063, 0.0, 0.25)）位点有 6 个原子。
