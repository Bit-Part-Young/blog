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

- [OVITO](https://www.ovito.org/)

- OVITO 2.9 版本的 Python script 功能可以免费使用，其他需要 Pro 版本

- [OVITO 识别结构的几种方法](https://mp.weixin.qq.com/s/Jh9lQKRbpFyhUnu8aHJSog)

- 选中某层原子：表达式选取 Expression selection

- 无直接计算原子层间距的 Modification

- [ovito_modifiers](https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html)

- POSCAR 格式，单个文件含多帧构型，会无法读取；LAMMPS 格式，单个文件含多帧构型，只会读取第一帧数据

- macOS 版本的 OVITO 无法读取多帧构型数据

- 支持 SFTP，可打开远程构型文件

- OVITO 菜单栏：
    - 主菜单
    - 视图窗口
    - 动画工具条
    - 修正通道（Add Modification）及其属性栏
    - 渲染标签
    - 叠层标签（添加坐标轴、colorbar 等）

- Add Modification 内容

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

- [Ovito可视化弗伦克尔缺陷\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1v2yuYBEVg)
    - WS 缺陷分析：查看空位和间隙原子数目
    - 表达式选择：`Occupancy==0` 空位，`Occupancy>0` 间隙原子
    - 着色：给空位和间隙原子分别着色

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


---

## OVITO Python

- [OVITO Python](https://www.ovito.org/docs/current/python/index.html)

- OVITO Python 脚本（主要是用来可视化构型）：[GitHub - stefanbringuier/HowToSOVITO: A series of recipes and tutorials on how to use python scripting with OVITO](https://github.com/stefanbringuier/HowToSOVITO)

- [How to Script with OVITO - How To Script with OVITO](https://stefanbringuier.github.io/HowToSOVITO)

- [Ovito高质量图片渲染Python模块 - Eastsheng's Wiki](https://eastsheng.github.io/MyWiki/wiki/2023/04/13/softwares/lammps/ovito_plot_rendering/)
