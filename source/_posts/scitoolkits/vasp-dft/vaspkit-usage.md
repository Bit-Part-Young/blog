---
title: vaspkit 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: vaspkit 使用
description: vaspkit 使用
tags:
  - vaspkit
  - VASP
categories:
  - 科研工具
  - VASP
date: 2024-05-26 09:00:00
abbrlink: 260624
password:
---

# vaspkit 使用

## 介绍

- VASPKIT 官方教程：[Tutorials — VASPKIT 1.5 documentation](https://vaspkit.com/tutorials.html)

- VASPKIT Features：[Features — VASPKIT 1.5 documentation](https://vaspkit.com/features.html)

- ATOMKIT 介绍：[ATOMKIT Code — VASPKIT 1.5 documentation](https://vaspkit.com/atomkit.html)

- vaspkit.1.5.0.Mac.Intel 版本可以在 Mac M1 上运行

- [vaspkit pro](https://vaspkit.com/vaspkitpro.html) 有进阶功能（能使用 Structure Utility 中的全部功能）


---

## 使用

- vaspkit 生成的 HCP 结构 KPOINTS 文件中的 K 点生成方式是 Gamma 点（无论选择 G 还是 MP）

- vaspkit 的能带结构数据获取前提是 K-path 是 Line-Mode 的

- 能带绘制相关数据文件：`REFORMATTED_BAND.dat`、`KLABELS`

- 态密度绘制相关数据文件：`TDOS.dat`、`IDOS.dat`（积分 DOS）

- 没有绘制体系分态密度（总的 s、p、d 轨道）选项

- vaspkit 源码中的 utilities 目录结构

```bash
utilities
├── INCAR_templates/
├── Makefile
├── POSCARtoolkit/
├── Shermo/
├── am1.5G.dat
├── bader2pqr.py
├── cif2pos.py
├── get_entropy.py
├── get_lattice.exe*
├── get_lattice.f90
├── hello.sh*
├── vbz.py
└── xsd2pos.py


INCAR_templates/       # 不同计算任务的 INCAR 文件模板
Shermo/                # 基于给定的谐振频率、惯性矩、温度、压力、原子质量、转动对称数等信息，Shermo 程序可以输出分子配分函数和理想气体近似下的每 mol 的内能、焓、熵、自由能、热容， 并且平动、转动、振动和电子贡献会独立输出，每种振动模式的贡献也能独立输出。
POSCARtoolkit/         # 分数坐标向笛卡尔坐标的转换；原子层数的固定；固定和放开用户选择的原子；可批量进行
get_entropy.py         # 计算给定温度下熵和焓的振动贡献；零点能
xsd2pos.py             # Material Studio xsd 格式转 VASP POSCAR 格式
cif2pos.py             # cif 转 VASP POSCAR 格式
vbz.py                 # 可视化 Brillouin Zone
get_lattice.f90        #
bader2pqr.py           # 将 bader 输出转成 pqr 文件用于 VMD 可视化
```


---

### vaspkit 功能介绍

```bash
# Task-ID        # 功能
02               # 力学性质
202              # 从弹性张量文件计算弹性性质
203              # 从 OUTCAR 文件提取弹性常数并计算弹性性质 |
205              # EOS 拟合

11               # DOS 态密度
111              # 总 DOS
113              # 每种元素的投影 DOS(PDOS)
114              # 选定原子的 PDOS
115              # 选定原子和轨道的 PDOS
116              # 每种元素的局域 DOS(LDOS)
117              # EIGENVAL 文件的总 DOS

21               # 能带
211              # 能带
212              # 仅选定一个原子的投影能带
213              # 每种元素的投影能带
214              # 选定原子的投影能带
215              # 元素权重的投影能带
216              # 选定原子和轨道的投影能带加和

92               # 2D-Material Kit
920              # 将原子层移动到 z 方向底部
921              # 将原子层移动到 z 方向中心
922              # 重新设置真空层厚度
```


---

### atomkit 功能介绍

```bash
# Task-ID    # 功能
02           # 对称性分析
201          # 分析晶体结构对称性
202          # 寻找原胞
203          # 寻找单胞
204          # 参看等同原子
209          # 分析分子或团簇的对称性


4            # 编辑 structure
401          # 构建超胞
402          # 固定选中原子
403          # 移动选中原子
404          # 删除选中原子
405          # 交换点阵矢量的轴
406          # 沿指定方向对原子坐标排序
409          # 在指定位置添加原子
410          # 取代选中原子
412          # 分数坐标，笛卡尔坐标之间转换
413          # 按照指定顺序排布 structure 中的元素
414          # 给选中原子施加随机位移
416          # 给 structure 施加系列应变

6            # 二维材料工具
601          # 将原子层移动到 z 方向底部
602          # 将原子层移动到 z 方向中间
603          # 调整真空层厚度
604          # Standardize 二维晶胞
```
