---
title: SciPy 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: SciPy 使用
description: SciPy 使用
tags:
  - SciPy
categories:
  - 编程
  - Python
date: 2024-09-17 16:50:00
abbrlink: 501607
password:
---

# SciPy 使用

## 介绍

参考资料

- [python微分求解 - 我是谁](https://yuhldr.github.io/posts/13877.html)



---

## 使用

```python
# 样条插值
from scipy.interpolate import interp1d

# 三次样条插值：在每个数据点上都是光滑的，且在二阶导数上连续
# cubic 三次；quadratic 二次
interp1d(x, y, kind="cubic")


# 物理常数
from scipy.constants import physical_constants

physical_constants          # 查看所有的物理常数

# 光速
value, unit, uncertainty = physical_constants["XXX"]
"speed of light in vacuum"  # 光速
"Planck constant":          # 普朗克常数
"electron mass"             # 电子质量
"proton mass"               # 质子质量
"Avogadro constant"         # 阿伏伽德罗常数


# smoothing 感觉效果一般？
from scipy.ndimage import gaussian_filter1d

rdf=gaussian_filter1d(rdf, sigma=...)
```
