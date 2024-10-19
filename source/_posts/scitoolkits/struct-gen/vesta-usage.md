---
title: VESTA 使用
top: false
cover:
toc: true
mathjax: true
summary: VESTA 使用
description: VESTA 使用
tags:
  - VESTA
categories:
  - 科研工具
  - 结构建模
date: 2024-10-18 09:30:45
abbrlink: 450318
password:
---

# VESTA 使用

- [VESTA 使用](https://mp.weixin.qq.com/s/wTxztn1RDWCG4cjVaA3E0A)
- 当 POSCAR 中的原子坐标有负值时，可使用 VESTA 导出使其变为正。
- 无法读取 `.poscar` 格式构型文件（Materials Project），OVITO 可以，建议将其统一为 `.vasp`；无法读取 LAMMPS 的 dump 格式文件
- VESTA 可以获取理论 XRD 图谱：导入构型 - Utilities - Powder Diffraction Pattern - Calculate, Plot


- 扩胞：菜单栏 Objects -- Boundary
- 不在构型视图左侧显示坐标轴：左下角的 Properties -- 取消勾选 "Show compass"
- 修改原子的颜色：左下角的 Properties -- Atoms -- Radius and color
- 切面：菜单栏 Utilities -- 2D Data Display
