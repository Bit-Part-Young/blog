---
title: OVITO 使用
top: false
cover:
toc: true
mathjax: true
summary: OVITO 使用
description: OVITO 使用
tags:
  - OVITO
categories:
  - 科研工具
  - 结构建模
date: 2023-10-18 20:49:23
abbrlink: 124902
password:
---

# OVITO 使用

## 介绍

- 官网：[OVITO](https://www.ovito.org/)

- OVITO 2.9 版本的 Python script 功能可以免费使用，其他需要 Pro 版本

- [OVITO 识别结构的几种方法](https://mp.weixin.qq.com/s/Jh9lQKRbpFyhUnu8aHJSog)

- 支持 SFTP，可打开远程文件

- OVITO 菜单栏：
    - 主菜单
    - 视图窗口
    - 动画工具条
    - 修正通道（Add Modification）及其属性栏
    - 渲染标签
    - 叠层标签（添加坐标轴、colorbar 等）

- [14-5-Ovito可视化\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1kryVYtEcT)
    - 原子轨迹跟踪显示
    - 熔化过程中自由体积和中心对称参数的变化

- [Ovito可视化堆垛层错、缺陷和原子应力\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1ieyqYnEiq/)

- 输出 RDF

- [OVITO批量导入数据的功能](https://mp.weixin.qq.com/s/R3mmsvt25ZQLnv6X62xYkA)

- OVITO 显示多晶不同颜色
    - 方式 1：添加 CNA Modification
    - 方式 2：添加 'Color coding' Modification，在右下方 'Input property' 选择 'Particle Identifier'，此时，**晶粒被设置为相同的颜色**；在颜色条下方点击 'Adjust range'，设置不同的颜色对应不同的晶粒 ID

- [OVITO 选择原子的几种方法](https://zhuanlan.zhihu.com/p/10934298169)

- [Ovito位错分析mesh透明度设置方法](https://mp.weixin.qq.com/s/LtkGpzszEg-Xx9XBZ0Am8w)

- [OVITO 显示位错和缺陷的一个小技巧](https://mp.weixin.qq.com/s/AC3ZABp4CyhJlHwfbdLWqw)



---

## 使用

- Add Modification 选项
    - 无直接计算原子层间距的 Modification

```bash
# Analysis
Coordination analysis             # 配位分析
Dislocation analysis (DXA)        # 位错分析
Histogram                         # 直方图
Voronoi analysis                  # Voronoi 分析
Wigner-Seitz defect analysis      # WS 缺陷分析

# Coloring
Assign color                      # 分配颜色/着色
Color coding

# Modification
Replicate                         # 扩胞
Slice                             # 切片 
Smooth trajectory                 # 
Unwrap trajectories               # 
Wrap at periodic boundaries       # 将 box 外原子移至 box 内

# Selection
Clear selection                   # 清除选择
Expression selection              # 表达式选择
Manual selection                  # 手动选择
Select type                       # 选择（原子）类型

# Python modifiers (pro)
Calculate local entropy           # 计算局域熵

# Structure identification
Ackland-Jones analysis            # 
Centrosymmetry parameter          # CSP
Common neighbor analysis          # CNA；识别原子对应的晶体结构

# Visualization
```

- 常用 Expression selection 值：[Expression selection - OVITO](https://www.ovito.org/manual/reference/pipelines/modifiers/expression_select.html)

```bash
Position.X              # x 方向位置
Position.Y              # y 方向位置
Position.Z              # z 方向位置；可用于选中原子层
StructureType           # 晶体结构类型

# 添加 WS 缺陷分析 Modification 后新增的 Attributes
Occupancy               # 原子占位
```

- 空位、间隙识别及数目统计步骤：[Ovito可视化弗伦克尔缺陷\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1v2yuYBEVg)
    - Wigner-Seitz defect analysis：识别空位和间隙原子并统计对应数目
    - Expression selection：`Occupancy==0` 空位，`Occupancy>0` 间隙原子
    - Assign color：给空位和间隙原子分别着色以进行区分

- 多面体模板匹配：[Polyhedral template matching — OVITO User Manual 3.11.3 documentation](https://www.ovito.org/docs/current/reference/pipelines/modifiers/polyhedral_template_matching.html)
    - 可识别 Ordering types（L1_0、L1_2、B2、zincblende / wurtzite）



---

## OVITO Python

- 官方教程：[OVITO Python](https://www.ovito.org/docs/current/python/index.html)

- OVITO Python 脚本编写教程（主要是用来可视化）：
    - [GitHub - stefanbringuier/HowToSOVITO: A series of recipes and tutorials on how to use python scripting with OVITO](https://github.com/stefanbringuier/HowToSOVITO)
    - [How to Script with OVITO - How To Script with OVITO](https://stefanbringuier.github.io/HowToSOVITO)

- [Ovito高质量图片渲染Python模块 - Eastsheng's Wiki](https://eastsheng.github.io/MyWiki/wiki/2023/04/13/softwares/lammps/ovito_plot_rendering/)

- [Voronoi 多面体指数计算方法](https://mp.weixin.qq.com/s/D_eXDAn9n96YKfS65tpMzQ)

- Voronoi 多面体指数常用 `<n1, n2, n3, ..., ni, ...>` 形式表示，其中 `ni` 表示 Voronoi 多面体具有的 i 边形数；一般 n1 和 n2 都是 0，可不用写出来；二十面体的多面体指数为 `<0, 0, 12, 0>`，十二面体的多面体指数为 `<20, 0, 0, 0>`

- 支持的输入文件格式：[Input file formats — OVITO User Manual 3.11.3 documentation](https://www.ovito.org/docs/current/reference/file_formats/file_formats_input.html#file-formats-input)

- 可导出的文件格式：[ovito.io.export_file — OVITO Python Reference 3.11.3 documentation](https://www.ovito.org/docs/current/python/modules/ovito_io.html#ovito.io.export_file)

- Pipeline 概念：[Pipeline concept — OVITO User Manual 3.11.3 documentation](https://www.ovito.org/docs/current/usage/pipeline.html#usage-modification-pipeline)
    - OVITO modifiers are analysis or property calculation/setting routines. For anything you want to do, in terms of analyzing your data from a atomistic simulation, you will use a modifier which is appended to the pipeline via `pipeline.modifiers.append(...)`.

- 整体流程：导入构型数据，添加 modifier 进行处理，导出计算数据

```python
from ovito.pipeline import Pipeline
from ovito.modifiers import ...
from ovito.io import import_file

# 导入构型/轨迹文件
pipline = import_file()

modifier = ...

# 添加 modifier（可添加多个，也可不添加）
pipeline.modifiers.append(modifier)

# data 类型 DataCollection（只代表一帧的数据）
data = pipeline.compute()

# 查看 data 相关属性
# 不同 modifier 处理后，particles、attributes、table 会有不同
list(data.particles.keys())                # 原子属性
print(list(data.attributes.keys()))        # 全局属性
list(data.tables.keys())                   # Tabulated data/DataTable


# 处理多帧构型数据
# 方式 1
for frame in range(pipeline.num_frames):
    data = pipeline.compute(frame)
    ...

# 方式 2；该迭代器可直接获取计算的 DataCollection
for data in pipeline.frames:
    ...
```

- Pipeline、DataCollection 类相关

```python
# DataCollection 相关
list(data.particles.keys())    # 查看原子属性；不同输出文件格式，可能会有不同
# POSCAR
['Position', 'Particle Type']
# dump.lammpstrj / xyz
['Particle Identifier', 'Particle Type', 'Position']

data.particles.positions       # 原子位置
data.particles.count           # 原子数

# 查看原子种类及其 ID
for type in data_init.particles.particle_types.types:
    print(type.id, type.name)


# Pipeline 类
# 属性
num_frames                    # 构型帧数
frames                        # 所有构型（数据）

# 方法
add_to_scene()                # 用于可视化
```

- 数据导出

```python
from ovito.io import export_file

export_file(data, file, format, **params)
# 参数
data                  # 可以是 Pipeline、DataCollection、DataObject、None 类型
file                  # 输出文件
foramt                # 输出文件格式

# **params 参数
multiple_frames       # 是否导出多帧的数据，默认只会导出第一帧的数据
start_frame           # 起始帧
end_frame             # 结束帧
every_nth_frame       # 每第 n 帧数据导出
key                   # 若为 "txt/table" 格式，可添加该参数导出对应 key 的数据

# 支持的 format
"txt/attr"            # 导出 global attributes
"txt/table"           # 导出 DataTable
"xyz"
"vasp"
"lammps/data"
"lammps/dump"
"imd"
"netcdf/amber"


# 导出示例
# 导出 VASP 格式
export_file(
    pipeline,
    "xxx.vasp",
    "vasp",
    reduced=True,           # 分数坐标
)

# 导出 LAMMPS data 格式
export_file(
    pipeline,
    "output.data",
    "lammps/data",
    atom_style="atomic",    # 默认值
)

# 导出 LAMMPS dump 格式
export_file(
    pipeline,
    "output.*.dump",
    "lammps/dump",
    multiple_frames=True,
)

for i in range(pipeline.num_frames):
    export_file(pipeline, f"output.{i}.dump", "lammps/dump", frame=i)

# 对于 "lammps/dump" "xyz" "imd" "netcdf/amber" 格式，需通过 column 指定具体的原子属性
export_file(
    pipeline,
    "output.xyz",
    "xyz",
    columns=["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z"],
)

# 导出 "txt/attr"
export_file(
    pipeline,
    "data.txt",
    "txt/attr",
    columns=["Timestep", "CommonNeighborAnalysis.counts.FCC"],
    multiple_frames=True,
)

# 导出 "txt/table"
export_file(
    data=pipeline,
    file=output_fn,
    format="txt/table",
    key="coordination-rdf[average]",
)
```

- [ovito.modifiers — OVITO Python Reference 3.11.3 documentation](https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html)

```python
from ovito.modifiers import ...
from ovito.data import CutoffNeighborFinder, DataCollection


# modifier，对应于 OVITO 软件中的 Modification
VoronoiAnalysisModifier              # Voronoi 分析
ComputePropertyModifier
CoordinationAnalysisModifier         # 配位分析
TimeAveragingModifier                # 时间平均
BondAnalysisModifier                 # 键分析
CreateBondsModifier
CommonNeighborAnalysisModifier
ExpressionSelectionModifier          # 表达式
InvertSelectionModifier
AssignColorModifier                  # 分配颜色/着色
CalculateDisplacementsModifier
```

- 格式转换（OVITO Python 中的 DataCollection 可转换成 ASE、pymatgen 的格式）

```python
from ovito.io.ase import ase_to_ovito, ovito_to_ase
from ovito.io.pymatgen import pymatgen_to_ovito, ovito_to_pymatgen

pipeline = import_file()
data = pipeline.compute()

atoms = ovito_to_ase(data)
structure = ovito_to_pymatgen(data)
```

- 计算 RDF

```python
pipeline.modifiers.append(
    CoordinationAnalysisModifier(
        cutoff=5.0,
        number_of_bins=100,
        partial=False,
    )
)

# 只输出第一帧的数据
print(pipeline.compute().tables["coordination-rdf"].xy())

# 会输出每帧的数据
for data in pipeline.frames:
    print(data.tables["coordination-rdf"].xy())

# 对所有帧的数据做平均
pipeline.modifiers.append(TimeAveragingModifier(operate_on="table:coordination-rdf"))
print(pipeline.compute().tables["coordination-rdf[average]"].xy())
```
