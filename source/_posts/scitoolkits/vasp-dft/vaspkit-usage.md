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

- [VASPKIT 功能及教程贴汇总](https://mp.weixin.qq.com/s/JjDxW7fxR8EUJDFLgtIQTQ)

- vaspkit 处理 DOS、能带计算数据演示：[13\_vasp/V2PC/01\_K\_Path\_Bulk\_Structure.md at main · Yiwei666/13\_vasp · GitHub](https://github.com/Yiwei666/13_vasp/blob/main/V2PC/01_K_Path_Bulk_Structure.md)

- vaspkit 中的 INCAR 选项
    - SR：标准弛豫，只弛豫原子位置，晶胞体积、形状不变，ISIF=2
    - LR：点阵弛豫，全弛豫，ISIF=3

- vaspkit 生成的 HCP 结构（及对称性不是很高的结构） KPOINTS 文件中的 K 点生成方式是 Gamma-center（无论选择 G 还是 MP，会自动纠正）

- vaspkit K 点设置：推荐精度：0.03（梅师兄）；trick：每个方向上的 k 点数与其对应的晶格常数的乘积 k\*a 值大于 30，为推荐 k 点密度；每个方向上的 ka 尽可能保持相同或接近；0.03 对应的 K 点密度是 1/0.03=33.33

- vaspkit 的能带结构数据获取前提是 K-path 是 Line-Mode 的

- 能带绘制相关数据文件：`REFORMATTED_BAND.dat`、`KLABELS`

- 态密度绘制相关数据文件：`TDOS.dat`、`IDOS.dat`（积分 DOS）

- 没有绘制体系分态密度（总的 s、p、d 轨道）选项

- 将自己的脚本作为 vaspkit 的补充功能（整合进 VASP）：拷贝脚本至 `vaspkit.X.X.X/utilities` 目录，在 `~/.vaspkit` 中的 `#USER_DEFINED` 处按示例格式填写内容（实用性一般）；参考：[atom_constrain.py程序: 固定原子层坐标](https://mp.weixin.qq.com/s/0-ldDyDSb-t2d7yIyC7h_A)

```bash
#USER_DEFINED
#           id      interpreter      script          argv       description
u3        python      layers_count.py   .TRUE.      count_atomic_layer
#END_USER_DEFINED
```

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
POSCARtoolkit/         # 分数坐标向笛卡尔坐标的转换；原子层的固定；固定特定原子；可批量进行
get_entropy.py         # 计算给定温度下熵和焓的振动贡献；零点能
xsd2pos.py             # Material Studio xsd 格式转 VASP POSCAR 格式
cif2pos.py             # cif 转 VASP POSCAR 格式
vbz.py                 # 可视化 Brillouin Zone
get_lattice.f90        #
bader2pqr.py           # 将 bader 输出转成 pqr 文件用于 VMD 可视化
```


---

### vaspkit 功能介绍

- vaspkit 的 04 Structure Editor、06 Symmetry Analysis 功能移至 atomkit 中

```bash
# Task-ID        # 功能
02               # 力学性质
202              # 从弹性张量文件计算弹性性质
203              # 从 OUTCAR 文件提取弹性常数并计算弹性性质 |
205              # EOS 拟合

03               # 能带结构 K-Path
301              # 一维
302              # 二维
303              # Bulk
305              # Wannier90 代码用 K-Path
305              # Phonopy 代码用 K-Path
306              # CP2K 代码用 K-Path
309              # 可视化第一布里渊区 K-Path

05
505              # 线性插值（NEB Images）
508              # Bader2PQR（将 Bader 电荷数据转换成 bader.pqr 文件，在 VMD 中给原子电荷着色）

08               # Advanced Structure Models
800              # 构建正交超胞
801              # 指定方向添加真空层
802              # 构建随机置换合金
803              # 指定 Miller 指数构建表面
804              # 指定两个表面构建界面/异质结
821              # 在超胞模型中构建非等同的空位缺陷
822              # 在超胞模型中构建非等同的置换缺陷

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

31               # 电荷密度分析
311              # 电荷密度
314              # 电荷密度差

72               # AIMD Kit
721              # MSD
722              # MSD（使用 FFT，推荐）
723              # 从 MSD.dat 文件中获取扩散系数和离子迁移率
725              # 从 PCDAT 获取对关联函数
726              # 选中元素的径向分布函数
727              # 速度自关联函数
728              # 从速度自关联函数获取振动态密度
730              # 选中元素的键长分布
731              # 选中元素的键角分布
736              # 选中原子的 MD 轨迹（POSCAR 格式）
737              # 选中原子的 MD 轨迹（PDB 格式）

78               # VASP2other 接口
789              # 声子能带结构排序（phononpy）

91               # 半导体 Kit
911              # 带隙
917              # 费米速度

92               # 2D-Material Kit
920              # 将原子层移动到 z 方向底部
921              # 将原子层移动到 z 方向中心
922              # 重新设置真空层厚度
```


---

### atomkit 功能介绍

- 转换成 cif 构型文件格式，对称性只能识别成 P1

```bash
# Task-ID    # 功能
02           # 对称性分析
201          # 分析晶体结构对称性
202          # 寻找原胞
203          # 寻找单胞
204          # 寻中对称性等同原子
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
