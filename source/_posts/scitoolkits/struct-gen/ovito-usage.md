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

- OVITO 2.9 版本的 Python script 功能可免费使用，其他需要 Pro 版本

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

- 球棍模型：添加 create bonds 的 modification

- [OVITO 批量导入数据](https://mp.weixin.qq.com/s/R3mmsvt25ZQLnv6X62xYkA)：先导入一个构型文件，在界面右中区域，Data source 选择文件名称，External file 中的 Search pattern 设置成 `*.xyz` 之类的，下方的 Options 可根据情况设置

- [OVITO 显示多晶不同颜色](https://mp.weixin.qq.com/s/4V4ePbP0DskpSRk1p1GEnA)
    - 方式 1：添加 CNA Modification，晶粒和晶界显示不同的颜色
    - 方式 2：添加 'Color coding' Modification（在右下方 'Input property' 选择 'Particle Identifier'，在颜色条下方点击 'Adjust range'），不同的颜色对应不同的晶粒 ID

- [OVITO 选择原子的几种方法](https://zhuanlan.zhihu.com/p/10934298169)

- [Ovito位错分析mesh透明度设置方法](https://mp.weixin.qq.com/s/LtkGpzszEg-Xx9XBZ0Am8w)

- [OVITO 显示位错和缺陷的一个小技巧](https://mp.weixin.qq.com/s/AC3ZABp4CyhJlHwfbdLWqw)

- OVITO 全局修改所有元素类型的 display radius：Application Settings -- Particles -- Particle types；`Restore built-in defaults` 按钮可恢复默认值；[Particle-related settings — OVITO User Manual 3.12.4 documentation](https://www.ovito.org/manual/reference/app_settings/particle_settings.html)

```bash
# display radius 统一修改成 0.7
# 元素  原始 display radius
Ti     1.47
Al     1.43
Nb     1.47
Mo     1.54
Zr     1.6
V      1.53
```


---

## 使用

- OVITO 无法计算单原子应力（是势函数的工作）

- 利用 OVITO 计算 RDF、键角分布、键长分布：[NEP\_GT/NEP\_RDF/NEP\_RDF.ipynb at main · wangchr1617/NEP\_GT · GitHub](https://github.com/wangchr1617/NEP_GT/blob/main/NEP_RDF/NEP_RDF.ipynb)

- [OVITO常用的无需Python代码的后处理技巧](https://mp.weixin.qq.com/s/5vPyhEsVaOVAQV6XMMEg8g)
    - 仅保留位错与缺陷原子
    - 输出各种位错线长度与位错密度的相关数据
    - 输出每一帧中的不同相原子的数量的相关数据
    - 统计每一帧中裂纹的表面积变化
    - 为模型添加基础的光影（OVITO 提供的基础光影效果 Ambient Occlusion）
    - 统计模型中的孔隙率（只适用 Pro 版）
    - **绘制原子应力应变云图**
    - **根据 dump 文件输出的原子属性数据计算新的原子属性数据（静水应力 (Hydrostatic stress) 与米塞斯应力 (Von mises stress) 的计算）**
    - **对某一原子属性在空间上进行平均（处理原子应力云图）**
    - 对某一原子属性在一维和二维空间上绘制分布图（只适用 Pro 版）
    - 绘制原子模型的表面轮廓线
    - 切割展示模型的某一个晶面（通过 Slice）
    - 结合 DXA 与汤普森四面体判定位错滑移面
    - 选中特定原子修改颜色
    - 修改原子的透明度
    - 辅助建立含有非晶晶界的多晶原子模型
    - 特定 Voronoi 指数的多面体团簇绘制
    - 利用平移与周期性边界条件调整模型（通过 Affine transformation 和 wrap at period boundary）
    - 冻结之前选择的原子以观察原子的移动趋势（通过 Freeze property）
    - 在 OVITO 中绘制粒子属性的散点图与直方图
    - 绘制原子位移矢量图
    - 绘制特定原子的轨迹线

- 直接导入构型/轨迹文件，下方默认有 Particles 信息；添加 Modification 后，会出现 Global Attributes、Data Tables 另外两种类型的数据（添加 DXA，会多出 Dislocation、Surfaces 数据）


---

### Add Modification 选项

- 无直接计算原子层间距的 Modification

```bash
# Analysis
Atomic strain                     # 原子应变
Bond analysis                     # 键分析
Cluster analysis                  # 团簇分析
Coordination analysis             # 配位分析
Dislocation analysis (DXA)        # 位错分析
Displacement vectors
Elastic strain calculation
Grain segmentation
Histogram                         # 直方图
Scatter plot
Spatial binning
Spatial correlation function
Time averaging                    # 时间平均
Time series                       # 时间序列
Voronoi analysis                  # Voronoi 分析
Wigner-Seitz defect analysis      # WS 缺陷分析

# Coloring
Ambient occlusion                 #
Assign color                      # 分配颜色/着色
Color by type                     #
Color coding                      #

# Modification
Affine transformation
Combine datasets
Compute property
Delete selected
Freeze property
Load trajectory
Python script
Replicate                         # 扩胞
Slice                             # 切片
Smooth trajectory                 #
Unwrap trajectories               #
Wrap at periodic boundaries       # 将 box 外原子移至 box 内

# Selection
Clear selection                   # 清除选择
Expand selection
Expression selection              # 表达式选择
Invert selection                  # 反选
Manual selection                  # 手动选择
Select type                       # 选择（原子）类型

# Python modifiers (pro)
Calculate local entropy           # 计算局域熵
Idendity fcc planar faults        #
Render LAMMPS regions             #
Shrink-wrap simulation box        #

# Structure identification
Ackland-Jones analysis            #
Centrosymmetry parameter          # 中心对称参数；CSP
Chill+                            #
Common neighbor analysis          # 共近邻原子分析；CNA
Identify diamond structure        # 识别金刚石结构
Polyhedral template matching      # 多面体模板匹配；PTM

# Visualization
Construct surface mesh
Coordination polyhedra            # 配位多面体
Create bonds
Generate trajectory line          # 生成轨迹线
```


---

### 常用 Expression selection 值

- [Expression selection - OVITO](https://www.ovito.org/manual/reference/pipelines/modifiers/expression_select.html)

```bash
Position.X              # x 方向笛卡尔坐标
Position.Y              # y 方向笛卡尔坐标
Position.Z              # z 方向笛卡尔坐标；可用于选中原子层
ReducedPosition.Z       # z 方向分数坐标
StructureType           # 晶体结构类型

# 添加 WS 缺陷分析 Modification 后新增的 Attributes
Occupancy               # 原子占位
```

- 空位、间隙识别及数目统计步骤：[Ovito可视化弗伦克尔缺陷\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1v2yuYBEVg)
    - Wigner-Seitz defect analysis：识别空位和间隙原子并统计对应数目
    - Expression selection：`Occupancy==0` 空位，`Occupancy>0` 间隙原子
    - Assign color：给空位和间隙原子分别着色以进行区分

- 多面体模板匹配（PTM）：[Polyhedral template matching — OVITO User Manual 3.12.4 documentation](https://www.ovito.org/docs/current/reference/pipelines/modifiers/polyhedral_template_matching.html)
    - 可识别的 Ordering types（L1_0、L1_2、B2、zincblende / wurtzite）；**实际效果不好**

- LAMMPS 与 OVITO 自带的结构分析模块包括：共近邻原子分析（Common Neighbor Analysis）；中心对称参数分析 (Centrosymetric Patameter) 与多面体模板匹配法（Polyhedral Template Matching）等。在分析点缺陷、线缺陷以及各种不同晶体结构时，这些方法是很有力、很方便的。需要指出的是，以上几种方法仅适用于已有良好定义的晶体，如 BCC、FCC、HCP、SC 等。对于不那么规则的晶体，例如单斜、三斜晶系等，可能会被错误的归入其它类别，或是归入 Others 中。

- 局域有序参数法（Local Ordering Parameter）

- [OVITO作图系列（小结）](https://mp.weixin.qq.com/s/0BM2SlTMsjhzH3df0UzcXw)

- OVITO 中的渲染器：OpenGL renderer, Tachyon renderer, OSPRay renderer（后两者收费，其 Python API 可免费使用）

DXA 算法只能单线程运行；CNA，Voronoi analysis，PTM 算法可并行


---

## OVITO Python

- 官方教程：[OVITO Python](https://www.ovito.org/docs/current/python/index.html)

- [ovito的python模块的工作流程](https://mp.weixin.qq.com/s/niqe0NKM6rUYzoZTjsMYpA)

- [OVITO2.9后处理python脚本和一些python后处理代码](https://mp.weixin.qq.com/s/zZ5DTw59W72xkn0WP1D3FA)（前 6 个官网有示例代码）
    - 计算 MSD
    - 自定义序参数（order parameter）
    - 根据粒子的晶向对粒子进行着色
    - 找到模型中所有重叠的原子
    - 将模拟盒子的 6 个方向分别收缩到所有粒子的 6 个方向的坐标极限的
    - 计算局域熵（local entropy）
    - 统计 Voronoi 分析中出现频率最高的前 10 个 Voronoi 指数并将其输出
    - 识别 FCC 晶体中的 ISF、ESF、TB 等面缺陷
    - 识别 BCC 中的点缺陷和面缺陷

- 主要用于可视化：[How to Script with OVITO](https://stefanbringuier.github.io/HowToSOVITO)

- [Ovito高质量图片渲染Python模块 - Eastsheng's Wiki](https://eastsheng.github.io/MyWiki/wiki/2023/04/13/softwares/lammps/ovito_plot_rendering/)

- [Voronoi 多面体指数计算方法](https://mp.weixin.qq.com/s/D_eXDAn9n96YKfS65tpMzQ)

- Voronoi 多面体指数常用 `<n1, n2, n3, ..., ni, ...>` 形式表示，其中 `ni` 表示 Voronoi 多面体具有的 i 边形数；一般 n1 和 n2 都是 0，可不用写出来；二十面体的多面体指数为 `<0, 0, 12, 0>`，十二面体的多面体指数为 `<20, 0, 0, 0>`

- 支持的输入文件格式：[Input file formats — OVITO User Manual 3.11.3 documentation](https://www.ovito.org/docs/current/reference/file_formats/file_formats_input.html#file-formats-input)

- 取消 OVITO Python 相关 warning 的输出

```python
import warnings

warnings.filterwarnings("ignore", message=".*OVITO.*PyPI")

# 选择性添加
import ovito._extensions.pyscript
```

- Pipeline 概念：[Pipeline concept — OVITO User Manual 3.11.3 documentation](https://www.ovito.org/docs/current/usage/pipeline.html#usage-modification-pipeline)
    - OVITO modifiers are analysis or property calculation/setting routines. For anything you want to do, in terms of analyzing your data from a atomistic simulation, you will use a modifier which is appended to the pipeline via `pipeline.modifiers.append(...)`.


---

### 整体流程

- 导入构型数据，添加 modifier 进行处理，导出计算数据（**使用多个 modifier 时，需注意其顺序**）

```python
from ovito.data import DataCollection, Particles, CutoffNeighborFinder, NearestNeighborFinder
from ovito.pipeline import Pipeline
from ovito.modifiers import ...
from ovito.io import import_file

# 导入构型/轨迹文件
pipeline = import_file("dump.lammpstrj")
# 可使用通配符
pipeline = import_file("dump_*.lammpstrj")
# 参数
sort_particles           # 是否对原子进行排序

modifier = ...

# 添加 modifier（可添加多个，也可不添加）
pipeline.modifiers.append(modifier)

# data 类型 DataCollection（只代表一帧的数据）
data = pipeline.compute()

# 查看 data 相关属性
# 不同 modifier 处理后，particles、attributes、table 会有不同
list(data.particles.keys())                # 原子属性
list(data.attributes.keys()                # 全局属性
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


---

### Pipeline 类

```python
# Pipeline 类
# 属性
num_frames                    # 构型帧数；或 source.num_frames
frames                        # 所有构型（的数据）

# 方法
add_to_scene()                # 用于可视化
```


---

### DataCollection 类

```python
# 属性
particles
cell
attributes
tables


# particles 属性
list(data.particles.keys())        # 查看原子属性；不同输出文件格式，可能会有不同
# POSCAR
['Position', 'Particle Type']
# dump.lammpstrj / xyz
['Particle Identifier', 'Particle Type', 'Position']

data.particles.positions           # 原子位置
data.particles.count               # 原子数

# 查看原子种类（元素）及其 ID 信息
for type in data_init.particles.particle_types.types:
    print(type.id, type.name)
```


---

### 构型/数据导出

- 可导出的文件格式：[ovito.io.export_file — OVITO Python Reference 3.11.3 documentation](https://www.ovito.org/docs/current/python/modules/ovito_io.html#ovito.io.export_file)

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
"lammps/data"         # 和 LAMMPS data 文件格式内容有些许差异
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


---

### modifiers

- modifiers Python API 及对应的 GUI 名称：[ovito.modifiers — OVITO Python Reference 3.12.4 documentation](https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html)

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
CommonNeighborAnalysisModifier       # CNA
AffineTransformationModifier
ExpressionSelectionModifier          # 表达式选择
AssignColorModifier                  # 分配颜色/着色
CalculateDisplacementsModifier       # 计算原子的位移矢量；可用于计算 MSD
DislocationAnalysisModifier          # 位错分析；DXA；需给定晶体结构
InvertSelectionModifier              # 反选
SelectTypeModifier                   # 选择类型（结构类型等）
DeleteSelectedModifier               # 删除选择的
```


---

### particles、Global Attributes、Data Tables

```python
data.particles[...]             # 获取 particle 中对应 keyword 的数据
data.attributes[...]            # 获取 Global Attributes 中对应 keyword 的数据
data.tables[...]                # 获取 Data Tables 中对应 keyword 的数据


# CNA attributes
"CommonNeighborAnalysis.counts.BCC"
"CommonNeighborAnalysis.counts.FCC"
"CommonNeighborAnalysis.counts.HCP"
"CommonNeighborAnalysis.counts.ICO"
"CommonNeighborAnalysis.counts.OTHER"
# CNA tables
"structures"


# DXA attributes
"DislocationAnalysis.cell_volume"          # 可用于计算位错密度
"DislocationAnalysis.total_line_length"
"DislocationAnalysis.length.other"
"DislocationAnalysis.length.1/2<110>"
"DislocationAnalysis.length.1/3<100>"
"DislocationAnalysis.length.1/3<111>"
"DislocationAnalysis.length.1/6<110>"


# SelectTypeModifier attributes
"SelectType.num_selected"


# CalculateDisplacementsModifier particles
"Displacement Magnitude"
```


---

### 格式转换

- OVITO Python 中的 DataCollection 可转换成 ASE、pymatgen 的格式

```python
from ovito.io.ase import ase_to_ovito, ovito_to_ase
from ovito.io.pymatgen import pymatgen_to_ovito, ovito_to_pymatgen

pipeline = import_file()
data = pipeline.compute()

atoms = ovito_to_ase(data)
structure = ovito_to_pymatgen(data)
```


---

### 计算 RDF

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

# 输出每帧的数据
for data in pipeline.frames:
    print(data.tables["coordination-rdf"].xy())

# 对所有帧的数据做平均
pipeline.modifiers.append(TimeAveragingModifier(operate_on="table:coordination-rdf"))
print(pipeline.compute().tables["coordination-rdf[average]"].xy())
```


---

### 统计多晶模型中晶界和 Bulk 区域的元素分布及占比

```python
cna_modifier = CommonNeighborAnalysisModifier()
pipeline.modifiers.append(cna_modifier)

select_type_modifier = SelectTypeModifier(
    operate_on="particles",
    property="Structure Type",
    types={
        # Bulk 区域
        # CommonNeighborAnalysisModifier.Type.OTHER,
        # 晶界区域
        # CommonNeighborAnalysisModifier.Type.BCC,
        CommonNeighborAnalysisModifier.Type.FCC,
        CommonNeighborAnalysisModifier.Type.HCP,
        CommonNeighborAnalysisModifier.Type.ICO,
    },
)
pipeline.modifiers.append(select_type_modifier)

pipeline.modifiers.append(DeleteSelectedModifier())

print(pipeline.modifiers)

element_info_list = []
for frame in range(pipeline.num_frames):
    data = pipeline.compute(frame)

    print(f"No. {frame} frame processed.")

    partcle_type_array = data.particles["Particle Type"]
    type_count_tuple = np.unique(partcle_type_array, return_counts=True)
    # {1: 100, ...}
    type_count_dict = dict(zip(type_count_tuple[0], type_count_tuple[1]))

    # {"frame": 1, "Ti": 100, ...}
    element_count_dict = {"frame": frame}
    for type in data.particles.particle_types.types:
        element_count_dict[type.name] = type_count_dict[type.id]

    element_info_list.append(element_count_dict)

df = pd.DataFrame(element_info_list)
```


---

### 位错分析

```python

```


---

### 计算 MSD

- [NEP\_GT/NEP\_MSD/NEP\_MSD.ipynb at main · wangchr1617/NEP\_GT · GitHub](https://github.com/wangchr1617/NEP_GT/blob/main/NEP_MSD/NEP_MSD.ipynb)

```python
```
